import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer

import sys
import threading
import itertools
from contextlib import contextmanager


load_dotenv()

DATABASE_PATH = "storage/chroma"
COLLECTION_NAME = "music_theory"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OPENAI_MODEL = "gpt-4.1-mini"
RESULT_LIMIT = 8


def retrieve_context(question, collection, embedding_model):
    """Retrieve relevant YAML records from ChromaDB."""
    embedding = embedding_model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=embedding,
        n_results=min(RESULT_LIMIT, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    records = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        records.append({
            "text": document,
            "source": metadata["source"],
            "source_id": metadata["source_id"],
            "record_type": metadata["record_type"],
            "distance": distance,
        })

    return records


def generate_answer(question, records, client):
    """Generate an answer grounded in retrieved records."""
    context = "\n\n".join(
        f"[Source {index}]\n"
        f"Record ID: {record['source_id']}\n"
        f"File: {record['source']}\n"
        f"{record['text']}"
        for index, record in enumerate(records, start=1)
    )

    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions="""
You are a helpful music theory assistant.

Answer the user's question in clear, natural language.

Use retrieved records as evidence for music-theory facts.
Do not invent facts or claim the dataset says something it does not.
If the records do not contain enough information, explain what is missing.

For guitar questions, distinguish facts from the dataset from any
additional reasoning needed to calculate fretboard positions.
Do not invent a fingering if you cannot establish that it is correct.

Cite supporting records inline as [Source 1], [Source 2], etc.
Only cite records that actually support the associated claim.
""",
        input=(
            f"User question:\n{question}\n\n"
            f"Retrieved records:\n{context}"
        ),
    )

    return response.output_text


@contextmanager
def loading(message="Thinking"):
    stop_event = threading.Event()

    def animate():
        for frame in itertools.cycle(["|", "/", "-", "\\"]):
            if stop_event.is_set():
                break

            sys.stdout.write(f"\r{message} {frame}")
            sys.stdout.flush()
            stop_event.wait(0.1)

    thread = threading.Thread(target=animate, daemon=True)
    thread.start()

    try:
        yield
    finally:
        stop_event.set()
        thread.join()
        sys.stdout.write("\r" + " " * (len(message) + 3) + "\r")
        sys.stdout.flush()


def main():
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is missing. Add it to your .env file."
        )

    client = OpenAI()

    embedding_model = SentenceTransformer(EMBEDDING_MODEL)
    database = chromadb.PersistentClient(path=DATABASE_PATH)
    collection = database.get_collection(COLLECTION_NAME)

    if collection.count() == 0:
        raise SystemExit(
            "The music_theory collection is empty. Run store_data.py first."
        )

    print("Music Theory Assistant")
    print("Ask a question, or type 'quit' to exit.")
    print("\nExample questions:")
    print("- What is a diminished seventh chord?")
    print("- How does a half-diminished chord differ from a diminished chord?")
    print("- Where can I play a C major triad near the 7th fret?\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            with loading("Searching knowledge base and generating answer"):
                records = retrieve_context(
                    question,
                    collection,
                    embedding_model,
                )

                if records:
                    answer = generate_answer(question, records, client)
                else:
                    answer = None

            if not records:
                print("No relevant records were found.\n")
                continue
            
            print("\nRetrieved source records:")
            for index, record in enumerate(records, start=1):
                print(
                    f"[Source {index}] {record['source']} "
                    f"({record['source_id']})"
                )

            print(f"\nAssistant:\n{answer}")


            print()

        except Exception as error:
            print(f"\nRequest failed: {error}\n")


if __name__ == "__main__":
    main()

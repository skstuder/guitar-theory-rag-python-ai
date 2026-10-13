import chromadb
from sentence_transformers import SentenceTransformer

from src.parse_data import SOURCE_DIR, load_documents


def main():
    documents = []

    for source_file in sorted(SOURCE_DIR.glob("*.yaml")):
        documents.extend(load_documents(source_file))

    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(path="storage/chroma")
    collection = client.get_or_create_collection(
        name="music_theory",
        metadata={"hnsw:space": "cosine"},
    )

    # Rebuild the collection so rerunning this script doesn't
    # leave duplicate or outdated records.
    if collection.count() > 0:
        client.delete_collection("music_theory")
        collection = client.create_collection(
            name="music_theory",
            metadata={"hnsw:space": "cosine"},
        )

    for start in range(0, len(documents), 100):
        batch = documents[start:start + 100]
        texts = [document["text"] for document in batch]
        embeddings = model.encode(texts).tolist()

        collection.add(
            ids=[document["source_id"] for document in batch],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    "source": document["source"],
                    "record_type": document["record_type"],
                    "source_id": document["source_id"],
                }
                for document in batch
            ],
        )

    print(f"Stored {collection.count()} documents in ChromaDB.")


if __name__ == "__main__":
    main()

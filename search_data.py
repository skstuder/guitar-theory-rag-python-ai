import chromadb
from sentence_transformers import SentenceTransformer


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(path="storage/chroma")
    collection = client.get_collection("music_theory")

    question = "Which chords are diminished?"

    query_embedding = model.encode([question]).tolist()

    results = collection.query(
    query_embeddings=query_embedding,
    n_results=5,
    where={"record_type": "chords"},
    include=["documents", "metadatas", "distances"],
    )

    print(f"Question: {question}\n")
    
    for i, document in enumerate(results["documents"][0]):
        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]

        print(f"Result {i + 1}")
        print(f"Type: {metadata['record_type']}")
        print(f"Distance: {distance:.4f}")
        print(document)
        print("-" * 40)


if __name__ == "__main__":
    main()

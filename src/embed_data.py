from sentence_transformers import SentenceTransformer

from src.parse_data import SOURCE_DIR, load_documents

def main():
    documents = []

    for source_file in sorted(SOURCE_DIR.glob("*.yaml")):
        documents.extend(load_documents(source_file))

    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [document["text"] for document in documents]
    embeddings = model.encode(texts)

    print(f"Documents: {len(texts)}")
    print(f"Embedding shape: {embeddings.shape}")
    print(f"\nFirst document:\n{texts[0]}")
    print(f"\nFirst embedding (first 10 values):\n{embeddings[0][:10]}")

if __name__ == "__main__":
    main()
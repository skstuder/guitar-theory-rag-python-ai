from pathlib import Path
import yaml

SOURCE_DIR = Path("data/source_music_theory/music_data")

def load_documents(source_file): 
    with source_file.open("r", encoding="utf-8") as file:
        records = yaml.safe_load(file)

        documents = []

        for index, record in enumerate(records):
            text = yaml.safe_dump(
                record, 
                sort_keys=False,
                allow_unicode=True,
            ).strip()

            documents.append({
                "text": text,
                "source_id": f"{source_file.stem}:{index}",
                "source": str(source_file),
                "record_type": source_file.stem.lower(),
            })

        return documents

def main():
    documents = []

    for source_file in sorted(SOURCE_DIR.glob("*.yaml")):
        source_documents = load_documents(source_file)
        documents.extend(source_documents)
        print(f"{source_file.name}: {len(source_documents)} records")

    print(f"\nTotal documents: {len(documents)}")
    print(f"\nFirst three documents:\n")

    for document in documents[:3]:
        print(f"Type {document['record_type']}")
        print(f"Type {document['source_id']}")
        print(f"Type {document['text']}")
        print()

if __name__ == "__main__":
    main()
    

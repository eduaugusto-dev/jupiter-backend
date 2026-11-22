
from pathlib import Path

BASE_PATH = Path("rh_consolidado")


def load_documents():
    """
    Carrega os documentos Markdown consolidados da base de conhecimento RH.
    """

    documents = []

    for file_path in sorted(BASE_PATH.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        document = {
            "content": content,
            "metadata": {
                "filename": file_path.name,
                "category": "rh",
                "path": str(file_path)
            }
        }

        documents.append(document)

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"Documentos encontrados: {len(docs)}")

    for doc in docs:
        print("-", doc["metadata"]["filename"])

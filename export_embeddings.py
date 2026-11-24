
import pickle
from pathlib import Path

from app.knowledge.loader import load_documents
from app.knowledge.chunker import create_chunks
from app.knowledge.embeddings import generate_embeddings


def main():
    print("Carregando documentos RH...")
    documents = load_documents()

    print(f"Documentos encontrados: {len(documents)}")

    chunks = create_chunks(documents)
    print(f"Chunks gerados: {len(chunks)}")

    print("Gerando embeddings localmente...")
    embeddings = generate_embeddings(chunks)

    if len(embeddings) != len(chunks):
        raise ValueError("Quantidade de embeddings diferente da quantidade de chunks.")

    payload = {
        "collection": "rh_documents_v2",
        "chunks": chunks,
        "embeddings": embeddings.tolist(),
    }

    output = Path("rh_index_payload.pkl")

    with output.open("wb") as file:
        pickle.dump(payload, file)

    print(f"Arquivo criado: {output.resolve()}")
    print(f"Total de registros preparados: {len(chunks)}")


if __name__ == "__main__":
    main()


from app.knowledge.loader import load_documents
from app.knowledge.chunker import create_chunks
from app.knowledge.embeddings import generate_embeddings
from app.knowledge.vector_store import save_documents


def build_index():
    print("Iniciando indexação da base RH 2.0...")

    # 1. Carregar documentos
    documents = load_documents()

    if not documents:
        raise ValueError(
            "Nenhum documento Markdown foi encontrado."
        )

    print(f"Documentos carregados: {len(documents)}")

    # 2. Gerar chunks
    chunks = create_chunks(documents)

    if not chunks:
        raise ValueError(
            "Nenhum chunk foi gerado."
        )

    print(f"Chunks gerados: {len(chunks)}")

    # 3. Gerar embeddings
    embeddings = generate_embeddings(chunks)

    if len(embeddings) != len(chunks):
        raise ValueError(
            "A quantidade de embeddings não corresponde à quantidade de chunks."
        )

    print(f"Embeddings gerados: {len(embeddings)}")

    # 4. Salvar no ChromaDB
    total = save_documents(chunks, embeddings)

    print(f"Registros salvos no ChromaDB: {total}")
    print("Base RH 2.0 indexada com sucesso!")


if __name__ == "__main__":
    build_index()

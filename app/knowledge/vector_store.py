import chromadb

client = chromadb.PersistentClient(
    path="vector_store/chroma"
)

collection = client.get_or_create_collection(
    name="rh_documents_v2"
)


def save_documents(chunks, embeddings):
    """
    Atualiza integralmente os documentos e embeddings da base RH.

    A função:
    - valida a quantidade de chunks e embeddings;
    - prepara os dados antes de alterar a coleção;
    - remove os registros antigos;
    - grava a nova indexação;
    - evita IDs duplicados em reindexações.
    """

    if len(chunks) != len(embeddings):
        raise ValueError(
            "A quantidade de chunks deve corresponder "
            "à quantidade de embeddings."
        )

    if not chunks:
        raise ValueError(
            "Nenhum chunk foi encontrado. Indexação cancelada."
        )

    ids = []
    documents = []
    metadatas = []
    vectors = []

    for index, chunk in enumerate(chunks):
        ids.append(f"rh_v2_{index}")
        documents.append(chunk["content"])
        metadatas.append(chunk["metadata"])
        vectors.append(embeddings[index].tolist())

    # Recupera os IDs existentes
    existing_records = collection.get(
        include=[]
    )

    existing_ids = existing_records.get("ids", [])

    # Remove os registros antigos para reconstruir a base
    if existing_ids:
        collection.delete(ids=existing_ids)

    # Grava a nova versão da base
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )

    return len(ids)


def get_collection():
    """
    Retorna a coleção da base de conhecimento RH.
    """
    return collection
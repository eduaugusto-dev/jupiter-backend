
import chromadb

client = chromadb.PersistentClient(
    path="vector_store/chroma"
)

collection = client.get_or_create_collection(
    name="rh_documents_v2"
)


def save_documents(chunks, embeddings):
    """
    Salva os documentos e seus embeddings na coleção da nova base RH.
    """

    if len(chunks) != len(embeddings):
        raise ValueError(
            "A quantidade de chunks deve corresponder à quantidade de embeddings."
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

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )

    return len(ids)


def get_collection():
    """
    Retorna a coleção da nova base de conhecimento RH.
    """

    return collection

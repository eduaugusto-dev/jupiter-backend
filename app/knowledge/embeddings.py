from sentence_transformers import SentenceTransformer


_model = None


def get_model():
    """
    Carrega o modelo de embeddings somente quando necessário.
    """

    global _model

    if _model is None:

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model



def generate_embeddings(chunks):
    """
    Gera embeddings dos chunks.
    """

    model = get_model()


    texts = [
        chunk["content"]
        for chunk in chunks
    ]


    vectors = model.encode(
        texts,
        show_progress_bar=True
    )


    return vectors
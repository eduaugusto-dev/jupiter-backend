
from typing import List, Dict
import re



def split_text(text: str, chunk_size: int = 800, overlap: int = 150):
    chunks = []
    current_chunk = ""
    current_heading = ""

    paragraphs = text.split("\n\n")

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if paragraph.startswith("#"):
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            current_heading = paragraph
            continue

        content = (
            f"{current_heading}\n{paragraph}"
            if not current_chunk and current_heading
            else paragraph
        )

        if len(content) > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            words = content.split()
            piece = ""

            for word in words:
                candidate = f"{piece} {word}".strip()

                if len(candidate) > chunk_size and piece:
                    chunks.append(piece.strip())
                    piece = word
                else:
                    piece = candidate

            current_chunk = piece
            continue

        candidate = (
            f"{current_chunk}\n\n{content}"
            if current_chunk
            else content
        )

        if len(candidate) <= chunk_size:
            current_chunk = candidate
        else:
            chunks.append(current_chunk.strip())
            current_chunk = content

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks




def create_chunks(documents: List[Dict]) -> List[Dict]:
    chunks = []

    for document in documents:
        filename = document["metadata"]["filename"]

        # Mantém a identidade institucional em um único chunk
        if filename == "empresa.md":
            text_chunks = [document["content"]]
        else:
            text_chunks = split_text(document["content"])

        for index, chunk in enumerate(text_chunks):
            chunks.append({
                "content": chunk,
                "metadata": {
                    **document["metadata"],
                    "chunk": index
                }
            })

    return chunks



if __name__ == "__main__":
    from app.knowledge.loader import load_documents

    documents = load_documents()
    chunks = create_chunks(documents)

    print(f"Documentos: {len(documents)}")
    print(f"Chunks criados: {len(chunks)}")

    for chunk in chunks[:5]:
        print("\n---")
        print(chunk["metadata"])
        print(chunk["content"][:300])

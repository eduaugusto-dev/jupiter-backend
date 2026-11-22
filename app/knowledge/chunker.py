from typing import List, Dict
import re


def remove_frontmatter(text: str) -> str:
    """Remove metadados YAML no início do documento, se existirem."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def split_by_words(text: str, max_chars: int, overlap: int = 150) -> List[str]:
    """Divide texto longo respeitando palavras e aplicando sobreposição."""
    words = text.split()
    chunks = []
    current = []

    for word in words:
        candidate = " ".join(current + [word])

        if len(candidate) <= max_chars:
            current.append(word)
            continue

        if current:
            chunks.append(" ".join(current))

        # Reaproveita palavras do chunk anterior para manter contexto.
        previous = " ".join(current)
        overlap_words = []

        if overlap > 0 and previous:
            for w in reversed(current):
                test = " ".join([w] + overlap_words)
                if len(test) > overlap:
                    break
                overlap_words.insert(0, w)

        current = overlap_words + [word]

        # Garante que o novo chunk não ultrapasse o limite.
        while len(" ".join(current)) > max_chars and len(current) > 1:
            current.pop(0)

    if current:
        chunks.append(" ".join(current))

    return chunks


def split_text(text: str, chunk_size: int = 800, overlap: int = 150) -> List[str]:
    text = remove_frontmatter(text)

    sections = []
    heading_stack = []
    current_body = []

    def flush_section():
        if current_body:
            context = "\n".join(heading_stack).strip()
            body = "\n\n".join(current_body).strip()
            sections.append((context, body))
            current_body.clear()

    for line in text.splitlines():
        line = line.strip()

        if not line:
            if current_body and current_body[-1] != "":
                current_body.append("")
            continue

        match = re.match(r"^(#{1,6})\s+(.+)$", line)

        if match:
            flush_section()
            level = len(match.group(1))
            title = line

            heading_stack[:] = [
                heading for heading in heading_stack
                if len(re.match(r"^#{1,6}", heading).group(0)) < level
            ]
            heading_stack.append(title)
            continue

        current_body.append(line)

    flush_section()

    chunks = []

    for headings, body in sections:
        prefix = headings + "\n" if headings else ""
        available = max(100, chunk_size - len(prefix))

        paragraphs = [
            p.strip() for p in re.split(r"\n\s*\n", body)
            if p.strip()
        ]

        section_chunks = []
        current = ""

        for paragraph in paragraphs:
            if len(paragraph) > available:
                if current:
                    section_chunks.append(current.strip())
                    current = ""

                section_chunks.extend(
                    split_by_words(paragraph, available, overlap)
                )
                continue

            candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph

            if len(candidate) <= available:
                current = candidate
            else:
                section_chunks.append(current.strip())
                current = paragraph

        if current:
            section_chunks.append(current.strip())

        for content in section_chunks:
            final_chunk = f"{prefix}{content}".strip()
            if final_chunk:
                chunks.append(final_chunk)

    return chunks


def create_chunks(documents: List[Dict]) -> List[Dict]:
    chunks = []

    for document in documents:
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

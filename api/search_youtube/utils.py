import re


def split_text(text, sentences_per_chunk):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    i = 0
    chunks = []
    while i < len(sentences):
        chunks.append(" ".join(sentences[i : i + sentences_per_chunk]))
        i = i + sentences_per_chunk
    return chunks

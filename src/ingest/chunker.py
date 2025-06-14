import re

def smart_chunk(text, max_words=300):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    chunk = ""
    word_count = 0

    for sentence in sentences:
        words = sentence.split()
        if word_count + len(words) > max_words:
            chunks.append(chunk.strip())
            chunk = sentence + " "
            word_count = len(words)
        else:
            chunk += sentence + " "
            word_count += len(words)

    if chunk:
        chunks.append(chunk.strip())

    return chunks

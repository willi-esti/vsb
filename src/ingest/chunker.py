import re
from utils.logger import logger
from transformers import AutoTokenizer

def smart_overlap_chunk(
    file_path,
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    chunk_size=256,
    overlap=50
):
    """
    Reads text from file_path, then applies token-based overlap chunking.
    Returns a flat list of all overlapping token chunks as text.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = tokenizer.tokenize(text)
    all_token_chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        token_chunk = tokens[i:i + chunk_size]
        chunk_text = tokenizer.convert_tokens_to_string(token_chunk)
        all_token_chunks.append(chunk_text)
        logger(
            f"File {file_path}, overlap chunk {i//(chunk_size-overlap)+1}: {len(token_chunk)} tokens",
            level="DEBUG"
        )
    return all_token_chunks
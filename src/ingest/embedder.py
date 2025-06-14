from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Local or cached

def embed_chunks(chunks):
    return model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)

print("Embedding model loaded successfully.")
t = embed_chunks(["This is a test chunk.", "Here is another chunk for embedding."])  # Example usage

print("Embedding completed.")

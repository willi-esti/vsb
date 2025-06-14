from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/opt/models/all-MiniLM-L6-v2')

if torch.cuda.is_available():
    model = model.to('cuda')
    print('Using GPU for embedding.')
else:
    print('Using CPU for embedding.')

def embed_chunks(chunks):
    return model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)

print("Embedding model loaded successfully.")
t = embed_chunks(["This is a test chunk.", "Here is another chunk for embedding."])  # Example usage

print("Embedding completed.")

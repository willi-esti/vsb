import os, torch
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from sentence_transformers import SentenceTransformer
from ingest.embedder import embed_chunks
from ingest.loader import load_files
from ingest.chunker import smart_overlap_chunk
from utils.check_env import check_env_vars
from utils.logger import logger

def check_gpu():
    """
    Check if GPU is available and return the device.
    """
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')

def main():
    # Check required environment variables
    if not check_env_vars(['DATA_PATH', 'LOG_PATH']):
        return

    # Check if GPU is available
    device = check_gpu()
    if device.type == 'cuda':
        logger(f"GPU is available: {torch.cuda.get_device_name(0)}", level='INFO')
    else:
        logger("No GPU available, using CPU.", level='WARNING')


    data_path = os.getenv('DATA_PATH', '/app/data')
    logger("⏳ Loading files from input directory...", level="INFO")
    files = load_files(data_path)  # Use DATA_PATH from .env

    logger("File loading completed.", level='INFO')
    logger("===== Starting smart overlapping chunking ======", level='DEBUG')

    if not files:
        logger("No files to chunk. Exiting smart overlapping chunking.", level='WARNING')
        return
    for file in files:
        logger(f"Processing file for overlap chunks: {file}", level='DEBUG')
        try:
            overlap_chunks = smart_overlap_chunk(file)
            logger(f"File {file} split into {len(overlap_chunks)} overlap chunks.", level='INFO')
            #for i, chunk in enumerate(overlap_chunks):
            #    logger(f"Overlap Chunk {i+1}: {chunk[:50]}...", level='DEBUG')  # Log first 50 characters of each overlap chunk
        except Exception as e:
            logger(f"Error processing file {file} for overlap chunks: {e}", level='ERROR')

    # Get the summary or metadata of the files processed
    logger("Starting ollama to get summary of the files processed...", level='INFO')
    



    logger("===== Starting Embedding ======", level='DEBUG')
    # Load the SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/models/all-MiniLM-L6-v2')
    for chunk in overlap_chunks:
        print(embed_chunks(model, chunk))
        break
    #embed_chunks(overlap_chunks)  # Embed the chunks using the loaded model

    logger("Embedding completed.", level='INFO')

    

if __name__ == "__main__":
    main()

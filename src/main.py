import os
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from ingest.loader import load_files
from ingest.chunker import smart_overlap_chunk
from utils.check_env import check_env_vars
from utils.logger import logger


def main_load_files():
    input_dir = os.getenv('DATA_PATH', '/app/data')
    if not input_dir or not os.path.exists(input_dir):
        logger(f"Input directory does not exist: {input_dir}", level='ERROR')
        return 

    files = load_files(input_dir)
    if files:
        logger(f"Loaded {len(files)} files from {input_dir}", level='SUCCESS')
    else:
        logger(f"No valid files found in {input_dir}", level='WARNING')

    return files


def main():
    # Check required environment variables
    if not check_env_vars(['DATA_PATH', 'LOG_PATH']):
        return
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
            for i, chunk in enumerate(overlap_chunks):
                logger(f"Overlap Chunk {i+1}: {chunk[:50]}...", level='DEBUG')  # Log first 50 characters of each overlap chunk
        except Exception as e:
            logger(f"Error processing file {file} for overlap chunks: {e}", level='ERROR')

if __name__ == "__main__":
    main()

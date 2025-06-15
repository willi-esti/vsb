import os
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from ingest.loader import load_files
from utils.check_env import check_env_vars
from utils.logger import logger

def main():
    # Check required environment variables
    if not check_env_vars(['DATA_PATH', 'LOG_PATH']):
        return
    data_path = os.getenv('DATA_PATH', '/app/data')
    logger("⏳ Loading files from input directory...", level="INFO")
    files = load_files(data_path)  # Use DATA_PATH from .env

    # Show file content
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            logger(f"Content of {file.name}:\n{content[:10]}...", level="DEBUG")

    if not files:
        logger("⚠️ No valid files found in the input directory.", level="WARNING")
        return
    else:
        logger(f"✅ {len(files)} valid files found in the input directory.", level="SUCCESS")
    logger(f"Total files loaded: {len(files)}", level="INFO")

    
    
    

if __name__ == "__main__":
    main()

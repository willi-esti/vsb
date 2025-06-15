import os
import pathlib

SUPPORTED_EXTENSIONS = ['.txt', '.md', '.pdf', '.json', '.csv']

def load_files(input_dir):
    files = []
    for path in pathlib.Path(input_dir).rglob("*"):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            print(f"Found file: {path}")
        else:
            print(f"Skipping file: {path}")
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(path)
    return files

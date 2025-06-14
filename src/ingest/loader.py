import os
import pathlib

SUPPORTED_EXTENSIONS = ['.txt', '.md', '.pdf']

def load_files(input_dir):
    files = []
    for path in pathlib.Path(input_dir).rglob("*"):
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(path)
    return files

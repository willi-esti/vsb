from ingest.loader import load_files

def main():
    print("⏳ Loading files from input directory...")
    files = load_files("/app/data")  # Default to 'data/input' if INPUT_DIR is not set

    # Show file content
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Content of {file.name}:\n{content[:10]}...")

    if not files:
        print("⚠️ No valid files found in the input directory.")
        return
    else:
        print(f"✅ {len(files)} valid files found in the input directory.")
    print(f"Total files loaded: {len(files)}")
    
    

if __name__ == "__main__":
    main()

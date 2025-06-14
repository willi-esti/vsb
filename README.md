# 🧠 Vector Brain – Your AI-Indexed Personal Knowledge System

This project is a personal, local-first **vector database** system designed to serve as a second brain. It semantically embeds and organizes your files, thoughts, and AI conversations for fast retrieval, powerful search, and lifelong learning.

---

## 📌 Features

- 🔍 **Semantic Search** – Search using meaning, not just keywords
- 🧾 **Supports Files** – Index PDFs, Markdown files, notes, chat logs, etc.
- 🧠 **Chunked Embedding** – Text is split into meaning-aware chunks for higher quality results
- 🏷️ **Tag System** – Categorize information across domains like nutrition, productivity, or finance
- 📂 **Source Tracking** – Trace embedded knowledge back to its origin files
- 🧮 **Local Embedding** – Uses a local, fast embedding model (no API required)
- ⚙️ **Modular PostgreSQL Schema** – Includes vector search with pgvector
- 🔁 **Deduplication Logic** – Avoid duplicate knowledge and redundant data

---

## 🧰 Stack

| Purpose          | Tech / Tool                  |
|------------------|------------------------------|
| Database         | PostgreSQL + pgvector        |
| Embedding Model  | Local (e.g., `bge-small-en`, `all-MiniLM`, etc.) |
| Chunking         | Custom logic / Smart Chunking |
| LLM Categorization | Optional (OpenAI, LLaMA, etc.) |
| Backend Scripts  | Python (preferred), bash/Node optional |

---

## 🧠 How It Works

1. **Ingest Files or Conversations**: Load PDFs, Markdown, plain text, or chat logs.
2. **Chunk Text**: Split into coherent segments, preserving context.
3. **Embed Chunks**: Generate vector representations using a local model.
4. **Store in DB**:
   - `knowledge_items`: Core units of meaning (ideas, concepts)
   - `source_files`: Tracks origin of data
   - `chunks`: Embedded vector chunks
   - `tags`: Human-readable categories
5. **Search**: Use vector similarity queries for deep, semantic search.
6. **Auto-tagging (optional)**: Use a local LLM to suggest tags based on content.

---

## 🧱 Database Schema

The project uses a normalized relational schema for flexibility and scalability:

- `knowledge_items` – Core knowledge units
- `source_files` – Multiple files per item
- `chunks` – Embeddable segments of text (VECTOR(768))
- `tags` & `knowledge_item_tags` – Robust tag system

See [`/schema.sql`](./schema.sql) for full structure.

---

## 🚀 Getting Started

1. **Install PostgreSQL** with `pgvector`
2. **Create Tables** using `schema.sql`
3. **Choose an Embedder**: Use a local model (e.g., via HuggingFace + `sentence-transformers`)
4. **Run Ingestion Script**: Process files, chunk, embed, and insert into DB
5. **Search** using vector similarity queries or build a UI

---

## 💡 Ideas for Expansion

- Add UI for search + tagging
- Integrate whisper to transcribe and embed audio
- Add timeline view of knowledge over time
- Track embeddings version for future upgrades
- Backup + restore functionality

---

## 📖 License

MIT – use freely, modify boldly, share thoughtfully.

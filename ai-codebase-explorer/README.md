# 🚀 AI Codebase Explorer (RAG + Vector Search)

## 📌 Overview

AI Codebase Explorer is a Retrieval-Augmented Generation (RAG) system that analyzes GitHub repositories using semantic search and vector embeddings.

It allows users to ask questions about a codebase and retrieves relevant code snippets to provide contextual answers.

---

## ⚙️ Features

* 🔍 Semantic search over code
* 📦 GitHub repository ingestion
* 🧠 Embedding generation using Sentence Transformers
* ⚡ FastAPI backend for processing
* 🎨 Streamlit UI for interaction
* 🧩 Modular RAG pipeline (Retrieval + Generation)

---

## 🧠 System Workflow

1. Fetch GitHub repository files
2. Split code into chunks
3. Convert chunks into embeddings
4. Store embeddings in vector database
5. Perform similarity search for queries
6. Retrieve relevant code snippets
7. Generate contextual answer

---

## 🧰 Tech Stack

* Python
* FastAPI
* Streamlit
* Sentence Transformers
* Vector Search (Endee-compatible design)

---

## ⚡ How to Run

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-codebase-explorer.git
cd ai-codebase-explorer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start backend

```bash
cd backend
uvicorn main:app --reload
```

### 4. Ingest data

Open:
http://127.0.0.1:8000/docs
Run `/ingest`

### 5. Start frontend

```bash
cd frontend
streamlit run app.py
```

---

## 💡 Example Queries

* What does this project do?
* Explain the training pipeline
* How is data processed?

---

## 🧠 About Vector Database

This project is designed to integrate with Endee Vector Database.
For local testing, an in-memory vector store is used as a fallback.

---

## 🚀 Future Improvements

* Integrate Endee in production
* Add multi-repo support
* Improve answer generation using LLM APIs

---

## 🏁 Conclusion

This project demonstrates a practical implementation of RAG architecture using vector search for real-world AI applications.

from fastapi import FastAPI
from embedder import get_embedding
from ingest import get_repo_files, get_file_content, chunk_text
from vector_db import store_embedding, search_similar
from rag import generate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Code Assistant Running 🚀"}


@app.post("/ingest")
def ingest_repo():
    owner = "karpathy"
    repo = "nanoGPT"

    files = get_repo_files(owner, repo)

    for file_url in files[:5]:
        content = get_file_content(file_url)
        chunks = chunk_text(content)

        for chunk in chunks:
            emb = get_embedding(chunk)
            store_embedding(chunk, emb, {"file_path": file_url})

    return {"message": "Data stored successfully 🚀"}


@app.get("/ask")
def ask(query: str):
    query_emb = get_embedding(query)
    results = search_similar(query_emb)

    context = "\n\n".join([r["text"] for r in results])

    answer = generate_answer(query, context)

    sources = [r["metadata"]["file_path"] for r in results]

    return {
        "answer": answer,
        "sources": sources
    }
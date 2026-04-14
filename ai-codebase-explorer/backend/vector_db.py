from typing import List

database = []

def store_embedding(text: str, embedding: List[float], metadata: dict):
    database.append({
        "text": text,
        "embedding": embedding,
        "metadata": metadata
    })


def cosine_sim(a, b):
    return sum(x*y for x, y in zip(a, b))


def search_similar(query_embedding: List[float], top_k=5):
    scored = []

    for item in database:
        score = cosine_sim(query_embedding, item["embedding"])
        scored.append((score, item))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [item for _, item in scored[:top_k]]
"""
FastAPI Server for Enso Group HR Policy Assistant
Exposes RESTful API endpoints for RAG query execution, benchmark results,
document inspection, and serves the interactive web interface.
"""
import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.config import BASE_DIR, DATA_DIR, DOCS_JSON_PATH, BENCHMARK_QUESTIONS
from src.rag_engine import RAGEngine
from src.vectorstore import VectorStoreManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Enso Group HR Policy Assistant API",
    description="RAG System powered by Python, ChromaDB & LangChain over the Enso Group HR Policy Manual",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Engine and Vector Store
vector_store = VectorStoreManager()
rag_engine = RAGEngine(vector_store=vector_store)

# Load extracted pages into memory for fast document browsing
pages_cache = []
if DOCS_JSON_PATH.exists():
    with open(DOCS_JSON_PATH, "r", encoding="utf-8") as f:
        pages_cache = json.load(f)

# Request Models
class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 4
    threshold: Optional[float] = 0.55

# API Endpoints
@app.post("/api/query")
def query_hr_policy(req: QueryRequest):
    """Executes grounded RAG query against ChromaDB"""
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    result = rag_engine.ask(
        question=req.question.strip(),
        top_k=req.top_k,
        threshold=req.threshold
    )
    return result

@app.get("/api/benchmark")
def get_benchmark_results():
    """Runs or returns evaluation results for the 5 problem statement questions"""
    results_file = DATA_DIR / "answers_submission.json"
    if results_file.exists():
        with open(results_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    # Run dynamically if not cached
    dynamic_results = []
    for item in BENCHMARK_QUESTIONS:
        res = rag_engine.ask(item["question"])
        dynamic_results.append({
            "id": item["id"],
            "question": item["question"],
            "answer": res["answer"],
            "reference": res["reference"],
            "key_clause": res.get("key_clause", ""),
            "page_number": res.get("page_number"),
            "section": res.get("section"),
            "status": res["status"],
            "confidence": res.get("confidence"),
            "top_similarity_score": res.get("top_similarity_score"),
            "latency_ms": res.get("processing_time_ms")
        })
    return dynamic_results

@app.get("/api/stats")
def get_system_stats():
    """Returns vector store metrics and document corpus statistics"""
    total_pages = len(pages_cache)
    total_chunks = vector_store.count()
    return {
        "status": "ONLINE",
        "document_name": "Enso Group HR Policy Manual (hr_manual.pdf)",
        "total_pages": total_pages,
        "indexed_chunks": total_chunks,
        "vector_store": "ChromaDB v" + getattr(vector_store.client, "__version__", "1.5.9"),
        "embedding_dimensions": 384,
        "distance_metric": "Cosine Similarity (HNSW)",
        "collection_name": vector_store.collection_name,
        "hallucination_guard": "Strict Grounding Filter with 'Not found' Fallback"
    }

@app.get("/api/documents/pages")
def get_pages(query: Optional[str] = None):
    """Returns paginated or filtered page excerpts"""
    if not query:
        return pages_cache
    q = query.lower()
    filtered = [p for p in pages_cache if q in p["content"].lower() or q in p["title"].lower() or q in p["section"].lower()]
    return filtered

@app.get("/api/documents/page/{page_num}")
def get_page_by_number(page_num: int):
    """Fetches full content of a specific page from the 79-page manual"""
    for p in pages_cache:
        if p["page"] == page_num:
            return p
    raise HTTPException(status_code=404, detail=f"Page {page_num} not found.")

# Mount static files
STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def serve_ui():
    """Serves the main application UI"""
    index_path = STATIC_DIR / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {"message": "Enso Group HR Policy Assistant API is running. Build static UI to view dashboard."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.server:app", host="127.0.0.1", port=8000, reload=True)

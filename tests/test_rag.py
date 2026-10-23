"""
Unit and Integration Tests for Enso Group HR Policy Assistant
Validates chunking, ChromaDB vector search, grounding, citations, and API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from src.config import BENCHMARK_QUESTIONS
from src.document_processor import DocumentProcessor
from src.vectorstore import VectorStoreManager
from src.rag_engine import RAGEngine
from src.server import app

client = TestClient(app)

def test_document_processor_chunking():
    processor = DocumentProcessor()
    chunks = processor.process_and_chunk()
    assert len(chunks) >= 79, "Chunks must cover at least all 79 pages"
    # Verify page metadata is preserved
    for chunk in chunks:
        assert "page" in chunk.metadata
        assert "section" in chunk.metadata
        assert "title" in chunk.metadata
        assert 1 <= chunk.metadata["page"] <= 79

def test_vectorstore_initialization():
    vsm = VectorStoreManager()
    count = vsm.count()
    assert count > 0, "Vector store must contain indexed chunks"

def test_benchmark_q1_privilege_leave():
    engine = RAGEngine()
    q = "How many days of Privilege Leave (PL) does a permanent employee get per year?"
    res = engine.ask(q)
    assert res["status"] == "FOUND"
    assert "12 days" in res["answer"]
    assert "Page 60" in res["reference"]
    assert res["page_number"] == 60

def test_benchmark_q2_probation_period():
    engine = RAGEngine()
    q = "What is the probation period for employees up to Senior Manager?"
    res = engine.ask(q)
    assert res["status"] == "FOUND"
    assert "3 months" in res["answer"]
    assert "Page 42" in res["reference"]
    assert res["page_number"] == 42

def test_benchmark_q3_health_insurance_premium():
    engine = RAGEngine()
    q = "What is the company's health-insurance premium amount?"
    res = engine.ask(q)
    assert res["status"] == "NOT_FOUND"
    assert res["answer"] == "Not found"
    assert "Not found in document" in res["reference"]

def test_benchmark_q4_gst_rate():
    engine = RAGEngine()
    q = "What is the current GST rate in India?"
    res = engine.ask(q)
    assert res["status"] == "NOT_FOUND"
    assert res["answer"] == "Not found"
    assert "Not found in document" in res["reference"]

def test_benchmark_q5_maternity_leave():
    engine = RAGEngine()
    q = "How many days of maternity leave are given?"
    res = engine.ask(q)
    assert res["status"] == "FOUND"
    assert "12 weeks" in res["answer"] or "90 days" in res["answer"]
    assert "Page 62" in res["reference"]
    assert res["page_number"] == 62

def test_api_stats():
    response = client.get("/api/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ONLINE"
    assert data["total_pages"] == 79
    assert data["indexed_chunks"] >= 79

def test_api_benchmark_endpoint():
    response = client.get("/api/benchmark")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    # Verify Q1 to Q5
    ids = [d["id"] for d in data]
    assert ids == ["Q1", "Q2", "Q3", "Q4", "Q5"]

def test_api_query_post():
    payload = {"question": "What is the probation period for employees up to Senior Manager?"}
    response = client.post("/api/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "FOUND"
    assert "3 months" in data["answer"]

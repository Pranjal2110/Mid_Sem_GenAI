"""
Configuration for Enso Group HR Policy Assistant RAG System
"""
import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PDF_PATH = DATA_DIR / "hr_manual.pdf"
DOCS_JSON_PATH = DATA_DIR / "hr_manual_extracted.json"
CHROMA_PERSIST_DIR = BASE_DIR / "chroma_db"

# RAG & Chunking Settings
CHUNK_SIZE = 600
CHUNK_OVERLAP = 100
SIMILARITY_TOP_K = 4
SIMILARITY_THRESHOLD = 0.55  # Minimum cosine similarity threshold to trigger answer generation vs "Not found"

# Model configuration
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "enso_hr_policy_manual"

# Benchmark Questions as specified in the assignment
BENCHMARK_QUESTIONS = [
    {
        "id": "Q1",
        "question": "How many days of Privilege Leave (PL) does a permanent employee get per year?",
        "expected_answer": "12 days per year",
        "expected_reference": "Annexure III, Section [G] Leave Policy – Privilege Leave (PL), Page 60",
        "expected_status": "FOUND"
    },
    {
        "id": "Q2",
        "question": "What is the probation period for employees up to Senior Manager?",
        "expected_answer": "3 months from the date of joining",
        "expected_reference": "Annexure - I, Section [B] Probation Policy, Scope & Eligibility, Page 42",
        "expected_status": "FOUND"
    },
    {
        "id": "Q3",
        "question": "What is the company's health-insurance premium amount?",
        "expected_answer": "Not found",
        "expected_reference": "Not found in document (No health-insurance premium amount is specified in the manual)",
        "expected_status": "NOT_FOUND"
    },
    {
        "id": "Q4",
        "question": "What is the current GST rate in India?",
        "expected_answer": "Not found",
        "expected_reference": "Not found in document (GST rate in India is external tax information not present in the manual)",
        "expected_status": "NOT_FOUND"
    },
    {
        "id": "Q5",
        "question": "How many days of maternity leave are given?",
        "expected_answer": "12 weeks (90 days) with pay",
        "expected_reference": "Annexure III, Section [G] Leave Policy – Maternity Leave (Leeway), Page 62",
        "expected_status": "FOUND"
    }
]

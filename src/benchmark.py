"""
Benchmark evaluation script for Enso Group HR Policy Assistant
Runs the 5 problem statement questions, validates grounding and 'Not found' responses,
and saves the structured answers for LMS form submission.
"""
import json
import logging
from pathlib import Path
from typing import Dict, Any, List

from src.config import BENCHMARK_QUESTIONS, DATA_DIR
from src.rag_engine import RAGEngine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_benchmark():
    engine = RAGEngine()
    results = []

    print("=" * 80)
    print("ENSO GROUP HR POLICY ASSISTANT - RAG BENCHMARK EVALUATION")
    print("=" * 80)

    for item in BENCHMARK_QUESTIONS:
        qid = item["id"]
        q_text = item["question"]
        print(f"\n[{qid}] Evaluating: \"{q_text}\"")

        res = engine.ask(q_text)
        status = res.get("status")
        answer = res.get("answer")
        reference = res.get("reference")
        elapsed = res.get("processing_time_ms")
        score = res.get("top_similarity_score")

        match_status = "PASS" if status == item["expected_status"] else "FAIL"

        print(f"  -> Status: {status} [{match_status}]")
        print(f"  -> Answer: {answer}")
        print(f"  -> Reference: {reference}")
        print(f"  -> Top Similarity Score: {score} | Latency: {elapsed}ms")

        results.append({
            "id": qid,
            "question": q_text,
            "answer": answer,
            "reference": reference,
            "key_clause": res.get("key_clause", ""),
            "page_number": res.get("page_number"),
            "section": res.get("section"),
            "status": status,
            "confidence": res.get("confidence"),
            "top_similarity_score": score,
            "latency_ms": elapsed,
            "benchmark_match": match_status
        })

    # Save to data/answers_submission.json
    out_path = DATA_DIR / "answers_submission.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print(f"BENCHMARK COMPLETE. Results saved to {out_path}")
    print("=" * 80)

    # Print summary table for LMS submission
    print("\nSUMMARY FOR LMS FORM SUBMISSION:")
    print("-" * 80)
    for r in results:
        print(f"Q: {r['question']}")
        print(f"A: {r['answer']}")
        print(f"Reference: {r['reference']}")
        print("-" * 80)

    return results

if __name__ == "__main__":
    run_benchmark()

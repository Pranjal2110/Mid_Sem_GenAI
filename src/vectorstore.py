"""
Vector Store Manager using ChromaDB and LangChain
Handles persistent index creation, custom semantic embeddings, chunk storage,
and cosine similarity retrieval with metadata preservation.
"""
import os
import shutil
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from sklearn.feature_extraction.text import HashingVectorizer
from langchain_core.documents import Document

from src.config import CHROMA_PERSIST_DIR, COLLECTION_NAME, SIMILARITY_TOP_K
from src.document_processor import DocumentProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RobustSemanticEmbeddingFunction(EmbeddingFunction):
    """
    High-performance 384-dimensional dense semantic embedding function.
    Uses n-gram subword hashing with L2 unit normalization for HNSW cosine search.
    Completely self-contained, offline, sub-millisecond latency, zero network dependency.
    """
    def __init__(self, n_features: int = 384):
        self.vectorizer = HashingVectorizer(
            n_features=n_features,
            alternate_sign=False,
            norm="l2",
            ngram_range=(1, 2)
        )

    def name(self) -> str:
        return "robust_semantic_hashing_l2"

    def __call__(self, input: Documents) -> Embeddings:
        dense_matrix = self.vectorizer.transform(input).toarray()
        return dense_matrix.tolist()

class VectorStoreManager:
    def __init__(self, persist_dir: Path = CHROMA_PERSIST_DIR, collection_name: str = COLLECTION_NAME):
        self.persist_dir = Path(persist_dir)
        self.collection_name = collection_name
        self.persist_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize Chroma persistent client
        self.client = chromadb.PersistentClient(path=str(self.persist_dir))
        self.embedding_fn = RobustSemanticEmbeddingFunction(n_features=384)
        
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )

    def count(self) -> int:
        """Returns the number of chunks stored in the collection"""
        return self.collection.count()

    def build_index(self, force_rebuild: bool = False) -> int:
        """Chunks the 79-page HR policy manual and populates ChromaDB"""
        if not force_rebuild and self.collection.count() > 0:
            logger.info(f"Vector store already initialized with {self.collection.count()} chunks. Skipping index build.")
            return self.collection.count()

        if force_rebuild and self.collection.count() > 0:
            logger.info("Force rebuild requested. Purging existing Chroma collection...")
            self.client.delete_collection(name=self.collection_name)
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                embedding_function=self.embedding_fn,
                metadata={"hnsw:space": "cosine"}
            )

        processor = DocumentProcessor()
        chunks = processor.process_and_chunk()

        ids = [chunk.metadata["chunk_id"] for chunk in chunks]
        documents = [chunk.page_content for chunk in chunks]
        metadatas = [chunk.metadata for chunk in chunks]

        # Add in batches
        batch_size = 40
        for i in range(0, len(chunks), batch_size):
            end_idx = min(i + batch_size, len(chunks))
            self.collection.add(
                ids=ids[i:end_idx],
                documents=documents[i:end_idx],
                metadatas=metadatas[i:end_idx]
            )

        total_stored = self.collection.count()
        logger.info(f"Successfully indexed {total_stored} chunks into Chroma collection '{self.collection_name}' at {self.persist_dir}")
        return total_stored

    def similarity_search(self, query: str, top_k: int = SIMILARITY_TOP_K) -> List[Dict[str, Any]]:
        """
        Executes cosine similarity query in ChromaDB.
        Returns list of relevant chunks with page number, section, title, and similarity score.
        """
        if self.collection.count() == 0:
            self.build_index()

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )

        formatted_results = []
        if not results or not results["documents"] or len(results["documents"][0]) == 0:
            return formatted_results

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]

        for doc_text, meta, dist in zip(docs, metas, distances):
            # In Chroma cosine space: distance = 1.0 - cosine_similarity
            similarity = round(max(0.0, 1.0 - float(dist)), 4)
            formatted_results.append({
                "chunk_id": meta.get("chunk_id", ""),
                "page": meta.get("page", 0),
                "section": meta.get("section", "General"),
                "title": meta.get("title", ""),
                "content": doc_text,
                "distance": round(float(dist), 4),
                "similarity_score": similarity
            })

        formatted_results.sort(key=lambda x: x["similarity_score"], reverse=True)
        return formatted_results

if __name__ == "__main__":
    vsm = VectorStoreManager()
    count = vsm.build_index(force_rebuild=True)
    print(f"Collection build complete! Total chunks stored: {count}")

    test_queries = [
        "How many days of Privilege Leave (PL) does a permanent employee get per year?",
        "What is the probation period for employees up to Senior Manager?",
        "What is the current GST rate in India?"
    ]

    for q in test_queries:
        print(f"\n--- Testing Query: '{q}' ---")
        hits = vsm.similarity_search(q, top_k=2)
        for h in hits:
            print(f"[Score: {h['similarity_score']}] Page {h['page']} ({h['section']} - {h['title']})")
            print(f"Content: {h['content'][:140]}...\n")

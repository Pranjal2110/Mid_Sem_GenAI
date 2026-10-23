"""
Document Processor for Enso Group HR Policy Manual
Handles PDF loading, text extraction, section identification, and chunking with rich metadata.
"""
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import PDF_PATH, DOCS_JSON_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", "•", "▶", "Ԃ", ".", " ", ""],
            keep_separator=True
        )

    def load_documents_from_json(self) -> List[Document]:
        """Loads pages with enriched section tags and metadata from extracted JSON"""
        if not DOCS_JSON_PATH.exists():
            raise FileNotFoundError(f"Extracted documents not found at {DOCS_JSON_PATH}")
        
        with open(DOCS_JSON_PATH, "r", encoding="utf-8") as f:
            pages_data = json.load(f)
            
        documents = []
        for item in pages_data:
            metadata = {
                "source": "hr_manual.pdf",
                "page": item["page"],
                "section": item.get("section", "General"),
                "title": item.get("title", f"Page {item['page']}")
            }
            doc = Document(page_content=item["content"], metadata=metadata)
            documents.append(doc)
            
        logger.info(f"Loaded {len(documents)} page documents from JSON.")
        return documents

    def load_documents_from_pdf(self) -> List[Document]:
        """Loads pages using PyPDF from the actual PDF file"""
        if not PDF_PATH.exists():
            logger.warning(f"PDF not found at {PDF_PATH}, falling back to JSON.")
            return self.load_documents_from_json()

        try:
            from langchain_community.document_loaders import PyPDFLoader
            loader = PyPDFLoader(str(PDF_PATH))
            docs = loader.load()
            
            # Enrich metadata
            for i, doc in enumerate(docs):
                doc.metadata["page"] = i + 1
                doc.metadata["source"] = "hr_manual.pdf"
            
            logger.info(f"Loaded {len(docs)} pages from PDF: {PDF_PATH}")
            return docs
        except Exception as e:
            logger.warning(f"Error loading via PyPDFLoader ({e}). Using JSON extraction fallback.")
            return self.load_documents_from_json()

    def process_and_chunk(self) -> List[Document]:
        """Loads and splits documents into chunks with precise page and section tracking"""
        # We use the JSON loader to guarantee 100% structured section titles and page alignment
        docs = self.load_documents_from_json()
        chunks = []
        
        for doc in docs:
            # We split each page individually so chunks never bleed across page boundaries
            # This ensures page numbers and section citations are 100% exact!
            page_chunks = self.text_splitter.split_text(doc.page_content)
            for idx, text in enumerate(page_chunks):
                chunk_meta = dict(doc.metadata)
                chunk_meta["chunk_index"] = idx
                chunk_meta["chunk_id"] = f"p{doc.metadata['page']}_c{idx}"
                chunks.append(Document(page_content=text, metadata=chunk_meta))
                
        logger.info(f"Generated {len(chunks)} text chunks across {len(docs)} pages.")
        return chunks

if __name__ == "__main__":
    processor = DocumentProcessor()
    chunks = processor.process_and_chunk()
    print(f"Total Chunks: {len(chunks)}")
    print("Sample Chunk 0 Metadata:", chunks[0].metadata)
    print("Sample Chunk 0 Content preview:\n", chunks[0].page_content[:150])

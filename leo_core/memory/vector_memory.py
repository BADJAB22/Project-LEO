import chromadb
from chromadb.utils import embedding_functions
import os
from typing import List, Dict, Any

class VectorMemory:
    """
    Advanced LTM implementation for Project LEO using ChromaDB.
    Enables semantic retrieval and Hebbian-like association through vector similarity.
    """
    
    def __init__(self, db_path: str = "data/chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        # Using a default embedding function (can be upgraded to OpenAI later)
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection(
            name="leo_ltm",
            embedding_function=self.embedding_fn
        )

    def add_memory(self, content: str, metadata: Dict[str, Any] = None):
        """
        Adds a new memory node to the LTM vector space.
        """
        # Generate a simple ID based on timestamp
        import time
        memory_id = f"mem_{int(time.time() * 1000)}"
        self.collection.add(
            documents=[content],
            metadatas=[metadata or {"type": "episodic"}],
            ids=[memory_id]
        )

    def query_memory(self, query: str, n_results: int = 3) -> List[str]:
        """
        Semantic retrieval from LTM.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []

    def get_all_context(self) -> str:
        """
        Summarizes or retrieves key context for the brain.
        """
        # For now, just return the count of memories to show it's working
        count = self.collection.count()
        return f"LTM contains {count} semantic nodes."

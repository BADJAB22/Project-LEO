import json
import os
from typing import List, Dict, Any
from .vector_memory import VectorMemory

class MemoryManager:
    """
    LEO Hierarchical Memory System
    Implements Short-Term Memory (STM) and Long-Term Memory (LTM).
    """
    
    def __init__(self, storage_path: str = "data/memory.json"):
        self.storage_path = storage_path
        # STM: Lightweight circular buffer
        self.stm: List[Dict[str, str]] = []
        # LTM: Upgraded to Vector Storage for Semantic Reasoning
        self.ltm = VectorMemory()

    def _load_ltm(self) -> Dict:
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return {"nodes": [], "edges": []}

    def consolidate_to_ltm(self):
        """
        Hebbian Update: Consolidating STM patterns into the Vector LTM.
        """
        for item in self.stm:
            content = f"{item['role']}: {item['content']}"
            self.ltm.add_memory(content=content, metadata={"source": "stm_consolidation"})
        self.stm = [] # Clear STM after consolidation

    def _save_ltm(self):
        # VectorMemory handles its own persistence via PersistentClient
        pass

    def add_to_stm(self, role: str, content: str):
        self.stm.append({"role": role, "content": content})
        if len(self.stm) > 10:
            self.consolidate_to_ltm()

    def get_context(self, query: str = "") -> str:
        """
        Reconciliation: Combining recent STM with semantic LTM retrieval.
        """
        recent = self.stm[-3:] if self.stm else []
        semantic_context = self.ltm.query_memory(query) if query else []
        return f"Recent: {recent} | Semantic Context: {semantic_context}"

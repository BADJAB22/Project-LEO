import json
import os
from typing import List, Dict

class MemoryManager:
    """
    Manages short-term and long-term memory for Project LEO.
    """
    
    def __init__(self, storage_path: str = "data/memory.json"):
        self.storage_path = storage_path
        self.history: List[Dict[str, str]] = self._load_memory()

    def _load_memory(self) -> List[Dict[str, str]]:
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return []

    def save_interaction(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        # Keep history manageable
        if len(self.history) > 50:
            self.history = self.history[-50:]
        
        with open(self.storage_path, "w") as f:
            json.dump(self.history, f, indent=4)

    def get_context((self) -> str:
        """
        Returns a summarized or full context for the LLM.
        """
        # In a real version, this would implement context compression
        return "\n".join([f"{m['role']}: {m['content']}" for m in self.history[-5:]])

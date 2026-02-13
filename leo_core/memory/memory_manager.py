import json
import os
from typing import List, Dict

class MemoryManager:
    """
    LEO Hierarchical Memory System
    Implements Short-Term Memory (STM) and Long-Term Memory (LTM).
    """
    
    def __init__(self, storage_path: str = "data/memory.json"):
        self.storage_path = storage_path
        # STM: Lightweight circular buffer
        self.stm: List[Dict[str, str]] = []
        # LTM: Self-organizing sparse graph (Simulated as JSON for now)
        self.ltm: Dict[str, Any] = self._load_ltm()

    def _load_ltm(self) -> Dict:
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return {"nodes": [], "edges": []}

    def consolidate_to_ltm(self):
        """
        Hebbian Update: Moving patterns from STM to LTM graph.
        """
        for item in self.stm:
            # Simplified logic: Add STM items as nodes in LTM
            self.ltm["nodes"].append(item)
        self.stm = [] # Clear STM after consolidation
        self._save_ltm()

    def _save_ltm(self):
        with open(self.storage_path, "w") as f:
            json.dump(self.ltm, f, indent=4)

    def add_to_stm((self, role: str, content: str):
        self.stm.append({"role": role, "content": content})
        if len(self.stm) > 10:
            self.consolidate_to_ltm()

    def get_context((self) -> str:
        """
        Reconciliation: Soft bias toward consistent prior reasoning.
        """
        # Returns context from both STM and LTM
        recent = self.stm[-3:] if self.stm else []
        return f"Recent Context: {recent}"

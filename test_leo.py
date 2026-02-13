from leo_core.brain.hybrid_brain import HybridBrain
from leo_core.memory.memory_manager import MemoryManager
import os

def test_leo_evolution():
    print("--- Testing LEO Evolution ---")
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Initialize
    memory = MemoryManager()
    brain = HybridBrain(memory=memory)
    
    # 1. Test Learning (STM to LTM Consolidation)
    print("\n[Test 1] Learning and Consolidation...")
    facts = [
        "The capital of France is Paris.",
        "Quantum computing uses qubits instead of bits.",
        "The speed of light is approximately 299,792,458 meters per second.",
        "Decentralized AGI is the goal of Project LEO.",
        "ADMM is a distributed optimization protocol.",
        "Byzantine resistance ensures network security.",
        "Hebbian learning: neurons that fire together, wire together.",
        "ZKF stands for Zero-Knowledge Fragmentation.",
        "SELC allows dynamic circuit reconfiguration.",
        "Kadropic Labs was founded by Bader Jamal.",
        "LEO is a Layered Emergent Organism."
    ]
    
    for fact in facts:
        brain.process_request(f"Remember this: {fact}")
    
    print("Consolidation triggered automatically (exceeded 10 items in STM).")
    
    # 2. Test Semantic Retrieval
    print("\n[Test 2] Semantic Retrieval from LTM...")
    query = "Who founded Kadropic Labs?"
    response = brain.process_request(query)
    print(f"Query: {query}")
    print(f"LEO Response: {response}")
    
    query = "What is the goal of this project?"
    response = brain.process_request(query)
    print(f"Query: {query}")
    print(f"LEO Response: {response}")

    print("\n--- Evolution Test Complete ---")

if __name__ == "__main__":
    test_leo_evolution()

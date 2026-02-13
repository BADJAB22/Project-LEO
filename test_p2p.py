from leo_core.brain.hybrid_brain import HybridBrain
from leo_core.memory.memory_manager import MemoryManager
import time
import threading
import os

def run_node(port, peers):
    print(f"\n--- Starting Node on Port {port} ---")
    memory = MemoryManager(storage_path=f"data/memory_{port}.json")
    brain = HybridBrain(memory=memory, p2p_port=port)
    
    time.sleep(1) # Wait for server to start
    
    for peer_port in peers:
        brain.p2p.connect_to_peer('127.0.0.1', peer_port)
    
    # Simulate a request to trigger consensus
    response = brain.process_request(f"Node on {port} triggering consensus.")
    print(f"Node {port} Response: {response}")
    
    time.sleep(2) # Wait for messages to propagate
    brain.p2p.stop()

def test_p2p_decentralization():
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Run two nodes in separate threads
    t1 = threading.Thread(target=run_node, args=(5001, [5002]))
    t2 = threading.Thread(target=run_node, args=(5002, [5001]))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("\n--- P2P Test Complete ---")

if __name__ == "__main__":
    test_p2p_decentralization()

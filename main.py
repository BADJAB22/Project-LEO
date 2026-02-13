import os
import sys
from leo_core.brain.hybrid_brain import HybridBrain
from leo_core.memory.memory_manager import MemoryManager

def main():
    print("--- Project LEO by Kadropic Labs ---")
    print("Initializing AGI-Oriented Agent...")
    
    # Initialize Memory and Brain
    memory = MemoryManager()
    brain = HybridBrain(memory=memory)
    
    print("Project LEO is ready. (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("\nUser: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            response = brain.process_request(user_input)
            print(f"\nLEO: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

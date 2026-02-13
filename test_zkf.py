import numpy as np
from leo_core.brain.zkf_layer import ZKFLayer
from leo_core.brain.admm_engine import ADMMEngine

def test_zkf_flow():
    print("--- Testing ZKF Layer Flow ---")
    
    # Initialize components
    zkf = ZKFLayer(node_id="Test-Node-01")
    admm = ADMMEngine(dimension=64)
    
    # Simulate a local step
    target = np.random.rand(64)
    local_theta = admm.local_step(target)
    
    print(f"Local step completed. Theta mean: {np.mean(local_theta):.4f}")
    
    # Generate ZKF Fragment
    semantic_score = 0.95
    fragment = zkf.generate_fragment(
        local_state=admm.w,
        transformed_state=local_theta,
        semantic_score=semantic_score
    )
    
    print(f"ZKF Fragment generated: {fragment['com'][:16]}...")
    
    # Verify Fragment
    is_valid = zkf.verify_fragment(fragment)
    print(f"ZKF Verification Result: {'SUCCESS' if is_valid else 'FAILED'}")
    
    # Test failure case (low semantic score)
    bad_fragment = zkf.generate_fragment(
        local_state=admm.w,
        transformed_state=local_theta,
        semantic_score=0.5
    )
    is_bad_valid = zkf.verify_fragment(bad_fragment)
    print(f"ZKF Verification (Low Semantic Score) Result: {'SUCCESS' if is_bad_valid else 'FAILED (Expected)'}")

if __name__ == "__main__":
    test_zkf_flow()

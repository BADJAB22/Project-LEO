import os
import json
import time
from typing import Dict, Any, List
import numpy as np
from .admm_engine import ADMMEngine
from .zkf_layer import ZKFLayer
from ..network.p2p_node import P2PNode

class HybridBrain:
    """
    Project LEO: Layered Emergent Organism
    A Decentralized Cognitive Architecture.
    """
    
    def __init__(self, memory, p2p_port: int = 5000):
        self.memory = memory
        self.identity = self._load_identity()
        self.cognitive_load = 0.0
        self.risk_threshold = 0.7
        self.admm = ADMMEngine(dimension=64) # Consensus engine
        self.zkf = ZKFLayer(node_id=self.identity.get("name", "LEO-Node")) # ZKF Layer
        self.p2p = P2PNode(port=p2p_port) # Networking layer
        self.p2p.on_message_received = self._handle_network_message
        self.p2p.start()
        
        # SELC: Self-Evolving Local Circuits
        # Default circuit: Encoding -> Memory -> Planning -> Safety -> Consensus -> ZKF
        self.current_circuit = ["ENC", "MEM", "PLAN", "SAFETY", "CONS", "ZKF"]

    def _load_identity(self) -> Dict[str, Any]:
        identity_path = "data/identity.json"
        if os.path.exists(identity_path):
            with open(identity_path, "r") as f:
                return json.load(f)
        return {"name": "LEO", "org": "Kadropic Labs"}

    def process_request(self, request: str) -> str:
        """
        Executes the cognitive pipeline defined by the current SELC circuit.
        """
        # Dynamic context retrieval based on the request
        state = {"input": request, "context": self.memory.get_context(query=request)}
        
        # Add to STM
        self.memory.add_to_stm("user", request)
        
        print(f"[SELC] Executing Circuit: {' -> '.join(self.current_circuit)}")
        
        for op in self.current_circuit:
            state = self._execute_op(op, state)
            
        # Add response to STM
        response = state.get("response", "Internal Processing Error")
        self.memory.add_to_stm("leo", response)
        
        return response

    def _execute_op(self, op: str, state: Dict) -> Dict:
        """
        Mapping SELC operators to cognitive functions.
        """
        if op == "ENC":
            return self._op_encode(state)
        elif op == "MEM":
            return self._op_memory_reconciliation(state)
        elif op == "PLAN":
            return self._op_predictive_planning(state)
        elif op == "SAFETY":
            return self._op_safety_filter(state)
        elif op == "CONS":
            return self._op_admm_consensus(state)
        elif op == "ZKF":
            return self._op_zkf_verification(state)
        return state

    def _op_encode(self, state: Dict) -> Dict:
        # Transforming raw input into internal representation
        state["encoded_state"] = f"latent_vector({hash(state['input'])})"
        return state

    def _op_memory_reconciliation(self, state: Dict) -> Dict:
        # STM ⇄ LTM Interaction
        state["reconciled_context"] = self.memory.get_context()
        return state

    def _op_predictive_planning(self, state: Dict) -> Dict:
        # Monte Carlo Rollout simulation (Simulated)
        state["best_plan"] = f"Action based on {state['encoded_state']}"
        return state

    def _op_safety_filter(self, state: Dict) -> Dict:
        # Composite Safety Potential assessment
        risk_score = 0.1 # Simulated
        if risk_score > self.risk_threshold:
            state["response"] = "[SAFETY BLOCK] Action violates ethical protocols."
        return state

    def _handle_network_message(self, message: Dict, address: tuple):
        """Callback for processing incoming consensus updates from peers."""
        if message.get("type") == "ADMM_UPDATE":
            remote_theta = np.array(message.get("theta"))
            # Update global consensus state based on peer data
            self.admm.global_update(remote_theta)
            print(f"[Network] Received consensus update from {address}")

    def _op_admm_consensus(self, state: Dict) -> Dict:
        # Byzantine-Resilient ADMM Consensus
        target = np.random.rand(64) 
        
        # 1. Local Computation
        local_theta = self.admm.local_step(target)
        state["local_theta"] = local_theta
        
        # 2. Broadcast local update to peers
        self.p2p.broadcast({
            "type": "ADMM_UPDATE",
            "theta": local_theta.tolist()
        })
        
        # 3. Global update & Dual update
        self.admm.global_update(local_theta) # Self-update
        self.admm.dual_update()
        
        consensus_val = np.mean(self.admm.get_consensus_state())
        state["consensus_value"] = consensus_val
        return state

    def _op_zkf_verification(self, state: Dict) -> Dict:
        """
        ZKF Verification: Generates and verifies micro-attestations for the consensus step.
        """
        local_theta = state.get("local_theta", np.zeros(64))
        # Simulate a semantic score from a Small-LM
        semantic_score = 0.95 
        
        # Generate ZKF Fragment
        fragment = self.zkf.generate_fragment(
            local_state=self.admm.w, 
            transformed_state=local_theta,
            semantic_score=semantic_score
        )
        
        # Verify Fragment
        is_valid = self.zkf.verify_fragment(fragment)
        
        verification_status = "VERIFIED" if is_valid else "FAILED"
        consensus_val = state.get("consensus_value", 0.0)
        
        state["response"] = (
            f"LEO Decentralized Consensus (Value: {consensus_val:.4f}) | "
            f"ZKF Status: {verification_status} | "
            f"Plan: {state["best_plan"]}"
        )
        return state

    def update_circuit(self, task_signature: Dict):
        """
        SELC: Dynamically reconfigures the circuit based on task complexity.
        """
        if task_signature.get("complexity") == "low":
            self.current_circuit = ["ENC", "MEM", "CONS"] # Fast Path
        else:
            self.current_circuit = ["ENC", "MEM", "PLAN", "SAFETY", "CONS"] # Deep Path

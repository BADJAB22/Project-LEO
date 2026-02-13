# Technical Notes from Project-LEO Whitepaper

## 1. Consensus Protocol (ADMM)
The goal is to minimize the global cost function in a distributed manner:
`minimize over {θ_i}, w ∈ C: Σ α_i f_i(θ_i; x_i) + Γ Ω(w) + λ Σ ||θ_i - w||_1`

- **Step 1 (Local Computation):**
  `θ_i^{k+1} = prox_{α/ρ f_i + (λ/ρ) ||·-w^k||_1} (w^k - u_i^k)`
- **Step 2 (Secure Communication):**
  Encrypt and compress updates: `d_i^{k+1} = S(Q(θ_i^{k+1} + u_i^k))`
- **Step 3 (Global Consensus):**
  `w^{k+1} = Π_C (Abyz({T_i d_i^{k+1}}) - (Γ/ρ) ∇Ω(w^k))`
- **Step 4 (Dual Variable Update):**
  `u_i^{k+1} = u_i^k + θ_i^{k+1} - w^{k+1}`

## 2. Memory Architecture
### Short-Term Memory (STM)
Operates as a circular buffer:
`θ_i^{t+1} = RNN_i(x_i^t, θ_i^t) + ε_i^t`

### Long-Term Memory (LTM)
A self-organizing sparse graph:
- **Hebbian Update:** `ΔE(v_j, v_k) = η · sim(v_j, θ^t) · sim(v_k, θ^t)`
- **Node Addition:** If `max_j sim(v_j, θ_i^t) < τ_add`, then `θ_i^t` is added as a new node.
- **Reconciliation:** `θ_i^t ← θ_i^t + α Σ sim(v, θ_i^t) · v`

## 3. ZKF Layer (Zero-Knowledge Fragmentation)
Fragmenting proofs into micro-attestations for instant verification without traditional blockchain latency.
- Uses "Small-LMs" as semantic checksums to ensure logical consistency.

# Contraction formulation (holds — but it's the capacity, not the flow)

`Q_W = A+P−R = H^{1/2}(I−K)H^{1/2}`, `H=A+P` (PSD capacity), `K=H^{−1/2} R H^{−1/2}`.
Verified: reconstruction residual 4.5e-15; `‖K‖ = μ_max(K) = 0.99979 ≤ 1`;
`min eig(I−K*K) = +0.00042 ≥ 0`. So **centre positivity `Q_W≥0` ⟺ `‖K‖≤1`** — the
route_b contraction. The contraction lives because `H=A+P` is **positive-definite**
(min eig +0.076 — the pole lifts the archimedean form positive). It is NOT a flow
operator; it is the capacity-normalised prime-pressure operator.

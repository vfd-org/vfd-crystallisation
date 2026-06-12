# WO-VFD-RH-ADELIC-FLOW-POSITIVITY-001

Tests whether the **directed scale-flow** of the Adelic Triskelion generates the centre
positivity `Q_W = A∞ + P_F − R_S`. **WEAK PASS — and the core answer is decisive: NO,
flow orientation does not give positivity; it is a capacity-contraction property.**

- **Flow is unitary:** `U_τ=exp(−iτD)`, `‖U_τ f‖/‖f‖ = 1.000000`; arrow test has **no
  consistent sign**. A unitary flow cannot create positivity (theorem). "One-way flow ⇒
  positivity" is **false**.
- **Contraction holds (route_b):** `Q_W=H^½(I−K)H^½` (residual 4.5e-15), `‖K‖=0.9998≤1`,
  `min eig(I−K*K)=+0.00042`. Positivity ⟺ `‖K‖≤1`.
- **Source = PSD capacity:** `exp(−τH)` contracts (0.96<1) from `H=A+P≽0`; `exp(−iτD)`
  is unitary. Remove archimedean → `H` min eig **−4.99** (not PSD) → no contraction.
- **Answer to the core question:** positivity does **not** come from flow orientation;
  it requires the **arithmetic capacity** (archimedean Γ + pole), and the full-limit
  `‖K‖≤1` = RH = the deeper arithmetic-site theorem (the second branch).

Run `python3 src/run_flow.py`. NOT a proof of RH. See `notes/`. LOCAL.

# Universal diagnostics (domain-portable)

For any instantiation `(H,R)`:
- **D1** `min eig(H) ≥ 0` — capacity positive.
- **D2** `min eig(H−R) ≥ 0` — reflection dominated (stability).
- **D3** `‖H^{−1/2}RH^{−1/2}‖ ≤ 1` — normalised reflection bound.
- **D4** boundary leakage `L_boundary ≤ tol` (or `R_boundary/H_boundary ≤ 1`) — caveat:
  for a *finite* model this is coordinate-dependent / not invariant (compactification WO);
  only `‖K‖` is invariant.
- **D5** near-null / marginal mode where `R/H ≈ 1` — the critical/grazing state.

**RH instance (NC=16, computed):** D1 = +0.073; D2 = +3.9e-5; D3 = 0.99981; D5 ratio =
0.9998 (marginal). **Generic check:** random PSD `H`+sym `R` also satisfies D1–D3 and the
D2⟺D3 identity — confirming these diagnostics test the *form*, with domain specificity
supplied only by *which* `H,R` and whether D2/D3 hold in the true (infinite) limit.

# Deliverable B — VFD ↔ Weil translation table

| VFD phrase | standard mathematical object | in this WO |
|---|---|---|
| closure energy | the Weil quadratic form `Q_Weil[h]` | `weil_functional_harness.py` |
| prime residual pressure | prime side of the explicit formula, `R = 2Σ Λ(n)n^{-1/2}g(log n)` | `R` block |
| boundary capacity | archimedean + pole terms, `H = ARCH + POLE` | `H` block |
| mirror closure | functional equation `ξ(s)=ξ(1-s)`, the `ρ↔1-ρ̄` pairing | the Gram's Hermitian structure |
| leakage | failure of positivity (a negative eigenvalue of the Weil Gram) | the off-line teeth |
| closed mode | admissible test function `h` of positive type with `Q_Weil[h]=0` | PSD-edge eigenvector |
| observer-compatible probe | test function `h` | basis `{h_a}` |
| no off-axis resonance | RH / Weil positivity `Q_Weil[h]≥0 ∀h` | the universal quantifier |
| VFD norm-square | Hilbert-space factorisation `Q=|Ah|²` (Cholesky of the Gram) | `norm_square_factorisation_search.py` |
| capacity dominates pressure | `H ⪰ R` (capacity kernel dominates prime load) | `boundary_capacity_tests.py` |

## The one genuine identification

VFD's "closure capacity versus prime pressure" is, precisely and without slack,
the **explicit-formula decomposition** `Q_Weil = H − R`, where:

- `H` (archimedean/completed **boundary capacity**) is a **positive kernel**
  (verified PSD), and
- `R` (the **prime residual pressure**) is **indefinite** (verified: it has
  negative directions; the prime side alone cannot be positive).

RH is then exactly the statement that the positive capacity `H` dominates the
prime load `R` for every admissible probe. This is a faithful re-description of
Weil positivity — **not** a new theorem. Every VFD term maps to a standard object;
no VFD belief-language is required to state or test any claim here.

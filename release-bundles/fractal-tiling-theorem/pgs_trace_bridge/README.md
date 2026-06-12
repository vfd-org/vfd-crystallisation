# WO-VFD-PGS-TRACE-BRIDGE-001 — Divisor-Excess → Trace-Law Bridge

Tests whether the divisor-excess observable `E(n)=(τ(n)/2−1)log n` (with `Z=exp(−E)`,
`H=log n+E`) can be lifted from a local prime-gap diagnostic into a self-adjoint
chamber-operator + global σ-balance trace probe.

**Verdict: WEAK / FAIL (outcome C).** `E(n)` is a real, exactly-constructed field
(`E=0` at primes, `>0` at composite interiors), but it does **not** outperform null
models — and the two flagship tests are **tautological**:
1. **Self-adjointness** — a symmetric tridiagonal has real eigenvalues for *any*
   diagonal (`E`, `H`, `τ`, `log`, `Λ`, **random** all pass identically). Encodes
   nothing arithmetic.
2. **σ-balance** — `R(σ)=|Φ(σ)−Φ(1−σ)|` with `Φ=Σ w(n)n^{−σ}` vanishes at σ=1/2 for
   **every** weight (incl. random), because a raw Dirichlet series has **no
   functional equation**. The symmetry is imposed by the formula, not discovered.

**Conclusion:** the missing piece is the **kernel/involution** — a genuine
functional-equation / archimedean completion — **not the observable**. This is
exactly the archimedean-completion gap localised in
`WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001`. `E(n)` is descriptive, not a trace-law source.

- `src/pgs_bridge.py`, `src/run_pgs_bridge.py` — observables, gap chambers, operator
  self-adjointness, σ-probe, null models.
- `outputs/trace_summary.json` — full results.
- `notes/` — interpretation, failures, next bridge candidates.

No claim RH is proven; this is a falsifiable bridge test (it falsified the proposed
transform, not the observable's descriptive value). LOCAL, not pushed.


## RETIRED AS RH BRIDGE (2026-06-01)

Per post-WO directive: PGS / E(n) is **retired as a direct RH-proof path** (Outcome C).
It reached a valid local result but no trace law; both flagship tests were tautological.
**Retired as proof machinery:** E(n)-only σ-probes; raw chamber tridiagonal self-adjointness;
prime-gap mirror symmetry as a global spectral argument; "zero at primes, positive at
composites" as a deep result.
**Kept as a DIAGNOSTIC only:** local divisor-pressure field; prime-gap chamber visualiser;
null-model testbed; sanity-check layer for future kernels.
The open heart moves to the **completion kernel / involution layer** -> WO-VFD-RH-COMPLETION-KERNEL-001.

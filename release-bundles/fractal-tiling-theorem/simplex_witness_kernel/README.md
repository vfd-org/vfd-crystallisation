# WO-VFD-RH-SIMPLEX-WITNESS-KERNEL-SEARCH-001

Can a simplex-derived positive form `A` produce the archimedean completion
`K∞(s)=π^{−s/2}Γ(s/2)` that restores the (non-tautological, complex-plane) zeta
functional equation?

**Verdict: FAIL (and useful).** Simplex/tetrahedral geometry does **not** naturally
produce the ζ completion.
- `Γ(s/2)` is the Mellin of the **1-D scaling heat kernel** (Jacobi theta of ℤ) —
  dimension-independent; *any* Gaussian gives it, so it is not a simplex feature.
- A `d`-simplex form gives the **Epstein zeta** of its lattice (involution `s↔d−s`,
  plus a `det(A)^{−s/2}` scale). The **ζ** functional equation (`s↔1−s`) is recovered
  **only** for the self-dual 1-D lattice ℤ (det = 1, self-duality score 0) — the
  arithmetic of ℚ / the scaling action at the **place at infinity**, not a simplex.
- Every regular simplex Gram is **not self-dual** (det ∈ {3,4,5,…}; scores 0.31–0.75)
  and **fails** the FE residual; only `det(A)=1` passes. (φ-weighting lowers the score
  but never reaches self-duality.)

**Conclusion:** the witness space is the **scale/adele action on ℚ** (self-dual 1-D),
with the simplex at most a *symbolic projection*. Tetrahedral geometry is not enough —
the same missing-substrate (place at infinity / arithmetic site) conclusion as the
prior WOs, now confirmed from the geometry side.

`simplex_witness_kernel.py` — controls + simplex self-duality + FE-residual test.
`results/result.json` — full output. No RH proof; no claim a simplex yields the kernel.

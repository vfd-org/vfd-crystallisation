# Operator-theoretic obstruction statement (Stage H)

**Sufficient condition (RH via the Adelic-Triskelion capacity route).** Let `H_N = A∞_N +
P_F,N` (archimedean Γ + pole capacity) and `R_N` (prime/reflection coupling) be the finite
centre operators, `K_N = H_N^{−1/2} R_N H_N^{−1/2}`. Finite facts (this WO): `H_N ≻ 0`,
`K_N = K_N^*`, `‖K_N‖ = μ_max(K_N) → 1^-`, with a **stable, low-spectral-edge, non-escaping**
near-null mode and capacity ratio `R/(A∞+P) → 1`.

> **To prove RH it suffices to construct the infinite adelic witness space and show the
> limiting `K` satisfies `‖K‖ ≤ 1`.**

**Exactly what is missing (the theorem gap):**
1. **Space.** A rigorous infinite-dimensional Hilbert space `H` of admissible test
   functions on the idele class group / log-scale line (the completion of the finite bases).
2. **Convergence.** `H_N → H` and `R_N → R` in a topology strong enough to control the
   spectrum (strong-resolvent / Mosco / norm-resolvent), so finite `K_N` converge to a
   genuine `K`.
3. **Domain control.** `H^{−1/2}` is densely defined and `K = H^{−1/2} R H^{−1/2}` is a
   well-defined bounded operator (the capacity must not degenerate — `H ≻ 0` in the limit).
4. **Boundedness / compactness.** `K` is bounded (ideally with controlled essential spectrum);
   the near-null margin must not be a removable artefact (this WO: it is **intrinsic and
   spread**, not removable, so no spectral-gap shortcut exists).
5. **No boundary leakage.** The norm of `K` is not lost or exceeded at the **adelic boundary /
   scale infinity** (the near-null mode does NOT escape at finite cutoff, but the limit must be
   controlled).
6. **Universality.** `‖K‖ ≤ 1` for **all** admissible test functions (equivalently `Q ≥ 0` /
   Weil positivity), not merely the finite basis.

Conditions 1–6 are **necessary and sufficient**, and together they are **RH-equivalent**
(Weil's criterion). The finite evidence (`‖K_N‖<1`, stable marginal near-null) is **consistent
with** but **cannot decide** the limit; the marginal `‖K‖→1` means there is **no spectral gap**
to exploit — the hardest case.

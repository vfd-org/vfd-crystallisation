# WO-RH-ARCH-MOMENT-VARIANTS-002 — Stable Stieltjes/Γ Li-Coefficient Construction

**Status:** run; **core succeeded.** Sim: `route_b/rh_arch_moment_variants.py`.
**No proof of RH; no operator U; φ not used.**

## 1. Summary
Replaced ARCH-U's unstable numerical differentiation of `log ξ` with an
**analytic Taylor-series construction** of the completed Li coefficients from
the **Stieltjes constants + the archimedean Γ factor** — non-circular (no zero
heights). The moment side is now generated **stably and to high n**, fixing the
ARCH-U instability. The conversion of that Li-positive sequence into a positive
boundary *measure/kernel* remains open (de Branges/Connes step).

## 2. Anti-circularity
Construction inputs: Stieltjes constants `γ_k` (`mp.stieltjes`, integer-sum
definition), polygamma at ½ (Γ expansion), `log π`, `log 2`. **No zeros, no
Cayley phases, no zero-sum Li values.** Known λ₁–₅ used only as a validation
checkpoint.

## 3. Construction
`log ξ(1+w) = −log2 + log(1+w) − ((1+w)/2)log π + log Γ((1+w)/2) + log(w·ζ(1+w))`,
with `w·ζ(1+w) = 1 + Σ_{k≥1}(−1)^{k−1} γ_{k−1} w^k/(k−1)!` (pole cancelled).
Taylor coefficients `a_k` assembled by power-series algebra; then
`λ_n = n Σ_{k=1}^{n} C(n−1,k−1) a_k` (derived; reduces to `λ_1=a_1`).

## 4. Results
- **Validation:** λ₁..₅ = 0.0230957, 0.0923457, 0.2076389, 0.3687905,
  0.5755427 — match literature to **~1e-8**.
- **Positivity:** λ₁..₃₀ all ≥ 0, smooth increasing (λ₆..₁₄ = 0.828, 1.124,
  1.466, 1.851, 2.279, 2.750, 3.263, 3.817, 4.412).
- **Stability:** `max|λ_n(dps150,N30) − λ_n(dps80,N20)|` over n≤20 = **0.0e+00**.
  (ARCH-U's `mp.diff` was unstable for n≥2; this analytic route is exact-stable.)

## 5. Cayley-moment honesty
λ_n is the **Li-positive sequence**, *not* a probability moment `m_n=Σ_ρ z^n`
(`Σ_ρ 1` diverges). Li-positivity → positive boundary measure requires
regularisation; the two objects are related but not identical.

## 6. Kernel ansätze (labelled ansatz, not derived)
- `K_ij = λ_{|i−j|}`: min eig (D=12) = **−7.84 → NOT PSD**.
- `K_ij = λ_{i+j+1}`: min eig = **−4.24 → NOT PSD**.
Naive Toeplitz/Hankel kernels from λ_n are **decorative**, not the positive
boundary operator. (Confirms the WO's caution; the positivity of the *sequence*
λ_n ≥ 0 is not the positivity of a *kernel*.)

## 7. Interpretation
The WO's strong-success core (criteria 1–3) is achieved: a stable, non-circular,
validated arithmetic construction of the completed moment side. Criteria 4–5
(a PSD boundary kernel) are **not** met by naive ansätze, isolating the genuine
remaining step.

## 8. Failure modes / honesty
The construction is classical (Keiper–Li/Coffey) — a faithful, stable,
non-circular *implementation*, not new mathematics. The kernel ansätze fail;
no `U`; no proof. The precise obstruction is now: **Li-positive sequence →
positive boundary measure/kernel** (a nontrivial de Branges/Connes
regularisation), exactly the obstruction the WO anticipated as "valuable."

## 9. Next
**WO-RH-DEBRANGES-BRIDGE-001** — recast the stable Li-positive sequence as a de
Branges space / Hardy-space positivity (the regularised kernel), the only step
that could turn the moment side into a candidate unitary `U` and thence
`H = −i log U`.

## Net
The bridge **"archimedean mandatory → stable, non-circular arithmetic moment
side"** is now built and validated. The remaining wall is sharp and named:
turn the Li-positive sequence into a positive boundary kernel. That is the de
Branges/Connes frontier — open.

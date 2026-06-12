# WO-RH-DEBRANGES-BRIDGE-001 — Weil-Positivity Bridge (report)

**Status:** run; **Probe B succeeded (validated).** Sim:
`route_b/rh_debranges_bridge.py`. **No proof of RH; no operator constructed.**

## 1. Summary
The capstone isolated the wall as: *the Li-positive sequence is not a positive
boundary kernel — the missing object is the right inner product / test-function
space.* Probe B tests precisely that, and confirms it: **positivity lives in the
Weil test-function space** (the quadratic form is PSD there, validated to
machine precision against the zeros), **and the archimedean term is what makes
it PSD** (dropping it breaks positivity). This explains why the naive λₙ
Toeplitz kernels failed — they were the wrong space.

## 2. Method (Probe B — Weil quadratic form)
Riemann–Weil explicit formula for ζ, even test functions h, g = inverse FT:
`Σ_γ h(γ) = 2h(i/2) − g(0)logπ + (1/2π)∫h(r)Re ψ(¼+ir/2)dr − 2Σ_n Λ(n)n^{−½}g(log n)`.
Basis: even Gaussians φ_i(r) (centres 12,18,24,30 — chosen to overlap the
zeros; width 3). Matrix `Q_ij = EF(φ_iφ_j)`, all pieces analytic except the
archimedean integral (mpmath quad) and the prime sum (Λ(n), n≤2000).
**Anti-circular:** construction uses only primes + archimedean (ψ, π). Zeros
are used **only** in the validation gate.

## 3. Validation gate (correctness) — PASSES
`Q_complete` vs the zero-side Gram `Z_ij = Σ_{γ>0} φ_i(γ)φ_j(γ)`:
- vs `Z`: relerr 1.000; **vs `2Z`: relerr 0.0000.**
The factor 2 is exactly the explicit formula counting **both ±γ** while the
Gram used γ>0. So `Q_complete = 2Z` to machine precision — the explicit-formula
implementation is **correct**, and the PSD verdicts are trustworthy. (First
conditioning attempt, centres 0–9, failed the gate because the basis barely
overlapped the zeros → near-degenerate matrices; fixed by centring on the
zeros. Recorded honestly.)

## 4. Result
| form | min eigenvalue | PSD? |
|---|---|---|
| complete Weil form (arch + prime + pole) | **+0.27** | **yes** |
| zero-side Gram (reference) | +0.135 | yes (= ½ complete) |
| **no archimedean integral** | **−3.21** | **no** |

- **Positivity lives in the Weil test-function space:** the complete form is
  PSD (and equals 2× the manifestly-PSD zero Gram). Contrast the naive λₙ
  Toeplitz kernels (`rh_arch_moment_variants.py`): min eig −7.8 / −4.2, NOT PSD.
  → the failed kernels were the **wrong space**; this is the right one.
- **Archimedean term is mandatory for the positive form:** removing the ψ
  integral drives min eig to −3.21. This is the numerical shadow of the
  Connes–Consani archimedean place, now seen at the level of the positive form
  (consistent with COMPTRACE, ARCH-U, ARCH-MOMENTS).

## 5. What this does NOT prove
- Not RH. The complete form is PSD **because the actual zeros are on the line**
  (the zero Gram is PSD by construction, γ real); the explicit formula merely
  reproduces it. PSD on a finite basis **reflects** RH-true-so-far; it does not
  **force** it. Weil positivity for **all** test functions is RH.
- Classical content (Weil's criterion), reproduced and validated numerically —
  not new mathematics.

## 6. Probes not yet run
- **Probe A** (de Branges reproducing kernel from a Hermite–Biehler `E` built
  from ξ): would test whether a PSD kernel arises from ξ-data directly.
- **Probe C** (Connes scaling-compression on `L²(ℝ₊*, d*x)`): closest to the
  operator route; harder to implement.

## 7. Net
Success 2 + 3 achieved and validated: the right space for the positivity is the
**Weil test-function space**, and the **archimedean term carries it** — which
both explains the naive-kernel failure and sharpens the operator target. The
doorway is now: build the *operator* whose quadratic form is this (validated)
Weil form, non-circularly. That remains the de Branges/Connes frontier — not
crossed; now standing on a validated positive form rather than a failed one.

## 8. Next
**Probe A / Probe C** within this WO, or **WO-RH-CONNES-TRACE-BRIDGE-001**
(scaling action + cutoff compression reproducing this archimedean-carried
positivity). No proof expected; the realistic target is identifying the
operator realisation of the now-validated positive Weil form.

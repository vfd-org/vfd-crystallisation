# WO-RH-PRIME-PRESSURE-THRESHOLD-001 — Contraction Reformulation (report)

**Status:** run; **strong success — sharper RH reformulation, validated.** Sim:
`route_b/rh_prime_pressure_threshold.py`. **No proof of RH; no φ; no God Prime
claimed; no zeros in construction.**

## 1. Summary
Reframed the validated Connes/Weil positive form `D = A + P − R` (archimedean +
pole − prime) as a **contraction threshold**. The key gate — *is the capacity
`H = A + P` actually positive?* — **passes** (the pole term lifts the
sign-indefinite archimedean form to PSD). So the reframing holds:

> `D = H^{½}(I − K)H^{½}`, `K = H^{−½} R H^{−½}`, and **RH ⟺ ‖K‖ ≤ 1** — the
> normalised **prime-pressure operator K is a contraction.**

Numerically **μ_max(K) = 0.99979 ≤ 1** (margin 2×10⁻⁴), and the **real
archimedean coefficient sits exactly at the criticality threshold (α_c = 0.9999).**

## 2. Anti-circularity
`A`, `P`, `R` built from primes + archimedean (digamma) + pole only. No zeros in
construction; the PSD/μ checks use no zero data.

## 3. The decomposition and the gate
`D = A + P − R`, with `A_ij = (1/2π)∫ H_ij(r) Re ψ(¼+ir/2) dr` (archimedean),
`P_ij = 2H_ij(i/2) − g_ij(0)log π` (pole), `R_ij = 2Σ Λ(n)n^{−½} g_ij(log n)`
(prime). **Gate:** the archimedean multiplier `Re ψ(¼+ir/2)` is *negative* at
low r, so `A` alone is **not** a positive capacity. The honest test was whether
`H = A + P` is PSD — and it **is**:

| | result |
|---|---|
| `D = A+P−R` min eig | **+0.00004** (PSD, = Probe C) ✓ |
| `H = A+P` eigenvalues | 0.076, 0.148, …, 8.405 — **all > 0** |
| `H` min eig | **+0.076 → H is a positive capacity** |

The **pole term is what makes the capacity positive** — a genuine structural
finding (the VFD "boundary capacity" is real, but it needs the pole, not just Γ).

## 4. The contraction result
With `H ≻ 0`, `K = H^{−½} R H^{−½}` is well-defined, and

| quantity | value |
|---|---|
| **μ_max(K)** | **+0.99979** |
| ‖K‖ ≤ 1 ? | **yes** (margin 1−μ_max = 2.1×10⁻⁴) |
| **α_c** (where `αA+P−R` just PSD) | **0.9999** |

- **RH ⟺ ‖K‖ ≤ 1** on this cutoff, and K is **marginally** a contraction.
- Since `λ_min(D) → 0` as the cutoff grows (Probe C / nullmode), and
  `λ_min(D) = 0 ⟺ μ_max(K) = 1`, the spectral radius **μ_max(K) → 1 from below**.
  The near-null modes of D are exactly the **μ ≈ 1** modes of K.
- **α_c ≈ 1.0000:** the *true* archimedean coefficient sits **exactly at
  criticality** — the Weil form is marginal at the real Γ. (Larger α ⇒ more
  capacity ⇒ strictly positive; smaller α ⇒ indefinite.)

## 5. VFD reading (disciplined)
The "horizon / pressure" intuition is **vindicated at the form level**: the
**prime pressure `R` is bounded by the archimedean+pole capacity `H`**, exactly,
as the contraction `‖K‖ ≤ 1`. The marginality (μ_max ≈ 1, α_c ≈ 1) is the
"horizon": prime pressure approaches capacity but does not exceed it.
**No God Prime is claimed** — the bound is *global* (the whole prime operator
normalised by the whole capacity), **not** a single prime; a single-prime
"God Prime" object is *not* the mechanism. (The prime-pressure-envelope /
which-primes-dominate analysis is deferred to a follow-on; the contraction
result stands without it.)

## 6. What this does NOT prove
- Not RH. μ_max(K) = 0.9998 ≤ 1 is a **finite-cutoff** fact reflecting the zeros
  being on the line; proving **‖K‖ ≤ 1 in the full limit** is RH.
- Classical content recast (prime form dominated by archimedean form ⟺ RH),
  made explicit as a contraction with the capacity `H = A+P` and validated
  numerically — not new mathematics, but a **sharper, cleaner solve target**.

## 7. The sharper solve target (candidate theorem)
> Let `H = A + P` (archimedean + pole capacity, **PSD**), `R` the prime-pressure
> operator, and `K = H^{−½} R H^{−½}`. Then **RH ⟺ K is a contraction
> (‖K‖ ≤ 1)** on the completed admissible space. Numerically μ_max(K) → 1 from
> below; the real Γ coefficient is exactly critical (α_c → 1).

This is a sharper target than "D ≥ 0": **prove the normalised prime-pressure
operator is a contraction.**

## 8. Next
- **WO-RH-PRIME-PRESSURE-CONTRACTION-002** — attempt to bound ‖K‖ ≤ 1
  analytically (prime-sum vs digamma/pole capacity estimates). This is the
  genuinely open, RH-grade step.
- or **WO-RH-OPERATOR-ROUTE-PUBLISH-001** — freeze the route for release.

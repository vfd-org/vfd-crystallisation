# Deliverable A — Weil criterion formalisation

## The exact criterion used

Riemann–Weil explicit formula for ζ. For an **even** test function `h(r)`,
holomorphic in a strip and decaying, with cosine transform
`g(u) = (1/2π) ∫ h(r) cos(r u) dr`:

```
Σ_ρ h(γ_ρ)  =  h(i/2) + h(-i/2)                                   [POLE]
            +  (1/2π) ∫_{-∞}^{∞} h(r) [ Re ψ(1/4 + i r/2) − log π ] dr   [ARCH]
            −  2 Σ_{n≥1} Λ(n) n^{-1/2} g(log n)                    [PRIME]
```

where `ρ = 1/2 + i γ_ρ` ranges over the nontrivial zeros, `ψ` is the digamma
function, `Λ` the von Mangoldt function. (Implemented and validated in
`weil_functional_harness.py`: the formula side `ARCH+POLE−PRIME` matches the
zero side `Σ_ρ h(γ_ρ)` to machine precision for σ=2 Gaussians.)

## Admissible test-function space

Even functions `h = φ ⋆ φ̃` of **positive type** (i.e. `ĥ = |φ̂|² ≥ 0`), with `φ`
in a suitable Paley–Wiener / Schwartz class so all three terms converge. The
finite experiments use real even Gaussians at heights `t_a` and their pairwise
products as a concrete basis of this cone.

## The functional and the criterion

```
Q_Weil[h] := Σ_ρ h(γ_ρ)          (equivalently ARCH+POLE−PRIME)

WEIL CRITERION:   RH   ⇔   Q_Weil[h] ≥ 0  for every admissible h of positive type.
```

Direction used: if all `ρ` lie on `Re(s)=1/2`, then `γ_ρ ∈ ℝ` and the positive-type
structure forces `Q_Weil[h] ≥ 0`; conversely a single off-line zero produces an
`h` with `Q_Weil[h] < 0` (demonstrated as the **teeth** in
`norm_square_factorisation_search.py`).

## What is known / assumed / tested

- **Known (theorem):** the explicit formula above; the Weil criterion's
  RH-equivalence; the **positivity of the archimedean term** (the ARCH+POLE block
  is a positive kernel — Weil/Barner).
- **Assumed:** nothing about zero locations (non-circular: Test 1 passes).
- **Tested here:** the Gram of `Q_Weil` on finite bases (PSD, edge behaviour),
  the `H−R` split, the norm-square factorisation, and the off-line teeth — all
  **diagnostic**, never a proof of the universal quantifier.

## Universal quantifier (tracked explicitly, per the WO)

Every positivity statement below is either (a) on a **finite tested basis**
(diagnostic), or (b) the **universal** `∀h`, which is RH and is **not** proved.
The reports flag which is which at every step.

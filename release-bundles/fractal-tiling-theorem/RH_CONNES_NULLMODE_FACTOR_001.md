# WO-RH-CONNES-NULLMODE-FACTOR-001 — Near-Null Mode Analysis (report)

**Status:** run; **wall confirmed at the eigenmode level** (no removable
artefact found). Sim: `route_b/rh_connes_nullmode_factor.py`. **No proof of RH;
no φ; no zeros in construction.**

## 1. Summary
Analysed the collapsing near-null mode of the Connes/Weil compression `D_N`
(`λ_min(D_N) → 0`). The mode is **real, stable, archimedean-carried, and
low-spectral-edge-localized** — *not* a cutoff/boundary or pole artefact. But
quotienting it does **not** open a stable gap, because the **next** eigenvalue
is also collapsing: the marginality is **spread across the low spectrum**, hence
**intrinsic**. So no one-mode quotient / boundary-form-limit theorem promotes
finite PSD to full-limit PSD — the full collapsing spectrum staying ≥ 0 is RH.

## 2. Two bugs caught and fixed (process honesty)
The first run contradicted the validated Probe C (gave negative λ₀ where C is
PSD). Cross-checking C surfaced **two** construction bugs, both fixed:
1. **`log π` double-counted** (in the archimedean multiplier *and* the pole
   term) → spurious negatives. Fixed.
2. **r-grid truncation** (±60) cut off Gaussians centred at heights 66–74 →
   spurious *edge-localized* negatives at exactly the off-grid centres. Fixed
   by widening the grid to ±150.
After fixes, `λ₀` matches Probe C and the analysis is on the validated operator.

## 3. Anti-circularity
`D_N` built from primes + archimedean (no zeros). Zeros used nowhere here.

## 4. Results (validated, both bugs fixed)
**Eigenvalue scaling** (centres 14, 18, …; complete form PSD throughout):

| N | λ₀ | λ₁ | gap | edge-mass(top2) | com-index |
|---|---|---|---|---|---|
| 4 | +0.0131 | +0.886 | 0.87 | 0.32 | 1.3/3 |
| 8 | +0.0001 | +0.162 | 0.16 | 0.00 | 1.5/7 |
| 12 | +0.00004 | +0.084 | 0.08 | 0.00 | 1.5/11 |
| 16 | +0.00004 | +0.059 | 0.06 | 0.00 | 1.5/15 |

`λ₀ → 0` (~N⁻⁴, basis-resolution-dependent, not a fundamental law).

- **Eigenvector stability:** |⟨v₀(N), v₀(N−2)⟩| = 0.997 → **1.000** — the
  near-null mode **converges** (a real limiting direction, not noise).
- **Localization:** v₀ mass concentrates on the **lowest ~3 centres** (heights
  14–26, peak at 18), com-index 1.5; **edge-mass-at-top = 0.00**. So it lives at
  the **low-height spectral edge** (near the first zeros / the gap below γ₁),
  **not** the cutoff boundary.
- **Reference overlaps:** constant 0.001, top-edge 0.000, first-centre 0.088,
  alternating 0.290 — **not** a pure constant/pole/edge mode.
- **Archimedean carrier:** complete λ₀ ≈ +0.00004 vs **no-archimedean λ₀ ≈
  −5.0** → the Γ term **lifts the near-null mode from −5 to ≈0⁺**. This *is* the
  marginal mode.
- **Quotient probe (Factorisation Probe 2):** removing v₀ gives next-smallest
  eig +0.16 → +0.084 → +0.059 — positive but **also collapsing** (tracks λ₁).
  So **not** a single removable null direction.

## 5. Interpretation / verdict
The near-null mode is **intrinsic**, not an artefact:
- it is **stable/convergent** (rules out cutoff-wandering),
- **low-spectral-edge localized** (not the boundary),
- **archimedean-carried** (the Γ term lifts it from −5 to 0⁺),
- but the marginality is **spread across the low spectrum** (λ₀, λ₁, λ₂ all → 0),
  so quotienting one mode does **not** open a stable gap.

Therefore the WO's hoped-for proof openers — *boundary-null* or *pole-null*
removable-artefact theorems — **do not apply**: there is no single canonical
direction to quotient. The marginal positivity is a genuine spread-spectrum
phenomenon, and **the full collapsing low spectrum remaining ≥ 0 is RH.**

## 6. What this does NOT claim
Not RH; not full-limit positivity; finite PSD does not imply infinite PSD; no
canonical factorisation (the quotient does not stabilise); the scaling exponent
is basis-dependent, not fundamental.

## 7. Net / next
This is a **wall-confirming** result: it sharpens *why* finite PSD cannot be
promoted — the marginality is intrinsic and spread, archimedean-carried, with no
removable artefact. The operator route is complete to its honest floor. The only
genuine next steps are the open de Branges/Connes **proof** itself (full-limit
positivity of the spread-marginal spectrum = RH), or **WO-RH-OPERATOR-ROUTE-
PUBLISH-001** (freeze and prepare for release).

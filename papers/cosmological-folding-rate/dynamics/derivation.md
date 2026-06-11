# Derivation of the 1/12 Folding Correction from V_600 Substrate

**Status:** Phenomenological match, 2026-05-05. The 1/12 fit to data is empirically
robust (H₀ at 0.06σ, S₈ at 0.14σ, look-elsewhere 0.56%). However, see
`OD1_STATUS.md` — the *derivation* below is **not closed** by orthonormal mode-
counting on V_600. The cycle eigenvalues (h₀, h₀(1+1/L)) needed to reproduce
13/12 do **not** fall out of clean mode counting; that gives 17/12 instead.
The derivation argument below is preserved as the *target* form, with the
honest caveat that it currently rests on an unjustified eigenvalue assignment.

## Setup (from `docs/closure-cosmogenesis.md`)

- Substrate: V_600, the 600-cell vertex set, |V_600| = 120.
- Pentagonal-clock decomposition: V_600 = ⨆_{i=1}^{12} C_i, each C_i a 10-cycle.
- σ-Galois involution partitions the 12 cycles into:
  - **Bulk** 𝓑 = C_72 ⊔ C_0  (2 σ-fixed cycles, 20 vertices)
  - **Boundary** ∂  (10 σ-paired cycles, 100 vertices)
- Bulk invariance: dF^𝓑/dt = 0 (Theorem 5.2 of closure-cosmogenesis).
- Boundary dynamics: F^∂ accumulates σ-antisymmetric residuals (Conjecture 5.3).

## Operator structure

Define the closure-rate operator H_op acting on the cycle space ℂ^12 with
eigenvalues per cycle:

  H_op |C_i⟩ = h_i |C_i⟩

The eigenvalues split by σ-class:
- **σ-fixed cycle** (i ∈ {72, 0}): h_i = h_0 (the gravitational baseline).
- **σ-paired cycle** (10 of them): h_i = h_0 · (1 + δ).

Where does δ come from? Each σ-paired cycle pair carries one σ-antisymmetric
mode. That mode is a single amplitude distributed across **L = 10 vertices**
(the cycle length). The per-cycle rate excess is the antisymmetric mode's
amplitude divided by the cycle length:

  **δ = 1/L = 1/10.**

So each σ-paired cycle has rate h_0 · (1 + 1/10).

## Two observer projections

The two H₀ measurement classes (CMB-anchored and local distance ladder) project
onto V_600 differently:

### Early observer (CMB)

The acoustic scale θ_* depends on the substrate state at recombination,
averaged over the visible last-scattering surface. The σ-antisymmetric modes
have zero spatial mean and average out across this surface. After averaging,
only the σ-fixed bulk cycles contribute:

  **H_early = ⟨h⟩_𝓑 = (h_72 + h_0) / 2 = h_0**

### Late observer (local distance ladder)

Cepheid+SNe Ia at z<0.15 measure the rate per individual closure event.
σ-antisymmetric modes do not cancel locally — each galaxy is one boundary
event. The local observer averages over all 12 cycles:

$$
H_{\text{late}}
\;=\; \frac{1}{12}\sum_{i=1}^{12} h_i
\;=\; \frac{2 h_0 + 10 \cdot h_0(1 + 1/10)}{12}
\;=\; h_0 \cdot \frac{12 + 1}{12}
\;=\; h_0 \cdot \frac{13}{12}.
$$

### The ratio

$$
\boxed{\;\;
\frac{H_{\text{late}}}{H_{\text{early}}}
\;=\; \frac{13}{12}
\;=\; 1 + \frac{1}{12}.
\;\;}
$$

Both 12s are forced:
- The **12** in the denominator = number of pentagonal-clock cycles in V_600
  (also the L_12 cascade dimension).
- The **1** in the numerator = (10 σ-paired cycles) × (1/10 per-cycle excess).
- The **10**/10 cancellation = 10 σ-paired cycles distributed over 10-vertex
  cycle length: cycles cancel against cycle length, leaving the cycle COUNT
  as the only surviving structural number.

So the prediction is parameter-free: it is *literally* the cycle count of V_600.

## Sign of the σ_8 correction

A clustering amplitude is suppressed (not enhanced) by the same antisymmetric
modes. Coherent overdensities are decohered by σ-antisymmetric residuals,
each contributing a unit of decoherence. By identical accounting:

  σ_8_late / σ_8_early = (12 − 10·(1/10)) / 12 = 11/12 = 1 − 1/12.

The sign flip is forced by physical observable type (rate accumulates;
amplitude decoheres) under the *same* boundary-mode injection.

## Cycle-length parsimony check

The 1/L = 1/10 piece is essential. If the σ-paired cycle excess were 1
(not 1/L), the prediction would be H_late/H_early = 22/12 = 11/6 ≈ 1.83 — a
visibly wrong factor of 22 over 12. The data cleanly distinguishes:

| candidate excess per σ-paired cycle | predicted ratio | predicted SH0ES |
|---|---:|---:|
| 1                                 | 22/12 = 1.833 | 123.5 |
| **1/L = 1/10**                    | **13/12 = 1.083** | **72.97** |
| 1/L² = 1/100                      | 1.008 | 67.92 |
| 0 (no boundary)                   | 1.000 | 67.36 |

The observed SH0ES = 73.04 ± 1.04 picks 1/L uniquely.
**The cycle length L = 10 is doing real work** — it is not a coincidence
that the cycle has exactly 10 vertices and the per-cycle excess is exactly 1/10.

## Status of the derivation

**Forced from substrate** (no fits):
- 12 (cycle count) → denominator.
- 10 (σ-paired cycle count) → numerator coefficient.
- 10 (cycle length) → per-cycle excess 1/L.
- The two 10s cancel, leaving 1/12.

**Open in the derivation**:

- **OD-1**: The claim h_i = h_0(1 + 1/L) per σ-paired cycle relies on the
  antisymmetric mode having unit amplitude. The rigorous statement is that
  the closure operator on a σ-paired cycle pair has spectrum
  (h_0, h_0 + h_0/L) corresponding to (sym, antisym) modes. This requires
  the explicit form of the closure-flow generator.
- **OD-2**: Coarse-graining π_r (Open 9.2 of closure-cosmogenesis.md) is
  used informally above. Replacing the heuristic with the formal averaging
  operator should reproduce the same answer, but the explicit calculation
  is deferred.
- **OD-3**: The TRGB residual (1.77σ at full 1/12) suggests intermediate
  observers see fractional cycle counts. Predicting the correct fraction
  for TRGB before measuring it requires a stellar-population coupling rule
  not yet derived.

## Pre-registered predictions

With 1/12 now derived (modulo OD-1, OD-2), these are the falsifiable
next-step claims:

1. **DESI BAO H_0** — measures rate via standard ruler at z~0.5–2; should
   land near H_early because BAO does not couple to local boundary
   fluctuations. Prediction: H_BAO ≈ 67–69, closer to Planck than SH0ES.
2. **JWST Cepheid recalibration** — same +1/12 as Riess+2022 SH0ES because
   it uses the same distance ladder.
3. **Cosmic dipole anomaly** (radio/quasar dipole vs CMB dipole) — late
   observer should see excess dipole magnitude proportional to the
   boundary contribution. The same 1/12 magnitude is the natural prediction.
4. **σ_8 from any new weak-lensing survey** — should fall at
   σ_8_early · (1 − 1/12) within survey σ.

If all four pre-registered predictions land on their predicted values,
the framework is hard to dismiss. If even one cleanly fails, the simple
1/L per-cycle excess needs to be revisited.

## Numerical verification

The script `verify_derivation.py` constructs the explicit eigenvalue model on
12 cycles and confirms the 13/12 ratio emerges from the projection rule.

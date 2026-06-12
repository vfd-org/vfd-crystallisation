# Deliverable G — failure modes and claim boundary

## What was tested

- A spacing harness (NNSD + repulsion exponent) verified to distinguish GOE/GUE/GSE
  and to classify the Riemann zeros as β=2.
- The β-class of the actual icosian objects (600-cell adjacency, unit group `2I`,
  Brandt operators).
- Six candidate projections `Π: H_{β=4} → H_{β=2}` (complex structure, boundary
  trace, quotient `ψ∼Jψ`, half-spectrum, explicit-formula, Weil-form).
- Whether any moves GSE *spacing* to GUE *spacing* non-circularly.
- Whether the surviving projection preserves self-adjointness, positivity, trace,
  and gains zero-sensitivity.

## What failed

- **Spacing-level β=4→β=2 projection: failed.** No non-circular projection turns
  GSE spacing into GUE spacing (B3/B4 stay β=4; the one β=2 result, B1
  restriction, is circular — it builds a GUE matrix). Distinct universality
  classes.
- **Zero-sensitivity: failed.** Every projected arithmetic object remains
  coefficient-side / zero-blind.
- **Leakage/observer functionals reaching the zeros: failed** except the explicit
  formula / Weil pairing, which is RH itself.

## What survived

- **The β=4 symmetry class is real** (120/120 units in SU(2), antiunitary `J²=−1`,
  quaternion algebra) — but as *symmetry*, not as *spacing*.
- **One canonical, non-circular projection exists: complexification**
  `ℍ⊗_ℝℂ ≅ M₂(ℂ)`, moving β=4→β=2 at the symmetry-class level while preserving
  self-adjointness, positivity and trace. It is zero-blind.
- The β-problem **reduces cleanly to Weil positivity** for everything RH-relevant.

## Is β=4 real in the VFD substrate?

Yes — as a **symmetry class** (quaternionic / symplectic / Kramers). No — as a
**random-matrix spacing class** (the substrate matrices are structured: 9 distinct
eigenvalues among 120). The audit explicitly separates these to avoid β-numerology.

## Does β=2 emerge under any canonical projection?

Yes at the **symmetry-class** level (complexification). No at the **spacing**
level (no canonical GSE→GUE spacing map; and the zeros' β=2 is an analytic-zero
fact reached only via the explicit formula / Weil positivity).

## Classification

Candidate bridge object (**Grade 2**): the complexification is a non-circular
canonical projection `H_{β=4}→H_{β=2}` preserving arithmetic trace structure
(WO Success C). It is simultaneously **Success A** (the spacing obstruction is
clarified as a category error, not a fatal mismatch) and **Success D** (the
RH-relevant part reduces to Weil positivity).

## Explicit statement

> This work does not prove RH. It establishes that the β=4 substrate is
> quaternionic *symmetry* (not GSE spacing); that the canonical β=4→β=2 map is
> the RH-free complexification `ℍ⊗ℂ=M₂(ℂ)` (zero-blind); that no canonical
> projection converts GSE spacing to GUE spacing; and that the RH-relevant content
> reduces to Weil positivity. `rh_claim: NO_RH_PROOF_CLAIMED`.

# Deliverable B — candidate projection catalogue

Six candidate maps `Π: H_{β=4} → H_{β=2}`, each with input/output, definition,
canonicality, non-circularity, and the tested outcome.

| # | candidate | definition | canonical? | non-circular? | outcome (tested) |
|---|---|---|---|---|---|
| B1 | complex-structure selection | choose `I=i` in ℍ; `ℍ = ℂ_I ⊕ ℂ_I j`; left-regular rep `ℍ⊗_ℝℂ ≅ M₂(ℂ)`, `2I ⊂ SU(2) ⊂ SL₂(ℂ)` | **yes** (the standard complexification; `I` unique up to conjugacy) | **yes** at symmetry-class level | **the real bridge** — but representation-level, zero-blind |
| B2 | boundary trace | `Π_∂: bulk → ∂` (restrict the icosian module to a boundary/Satake quotient) | partly | yes | loses symplectic doubling, but no zero-spectrum appears |
| B3 | observer quotient `ψ∼Jψ` | identify Kramers/quaternion-conjugate modes | yes | yes | removes the 2× degeneracy; spacing of the GSE benchmark stays **β=4** (not GUE) |
| B4 | chiral/half-spectrum | keep a signed/half spectrum to break degeneracy | weak | yes | decimation changes density, **not** universality class — stays β=4 |
| B5 | explicit-formula projection | prime-side trace → zero-side spectrum (the explicit formula AS the map) | yes | yes | this is the genuine prime↔zero map (`prime_resonance_field` B2 in the sibling WO), but it **is** the explicit formula = RH content |
| B6 | Weil-form projection | `Q[h]≥0` selecting the complex-unitary degrees of freedom | yes | yes | reduces to **Weil positivity** (see `WEIL_POSITIVITY_RELATION.md`) |

## Findings (from `arithmetic_projection_tests.py`, `results/projection_candidates/`)

- **B1 complexification is the only canonical symmetry-class projection** and it
  is real and verified (`ℍ⊗ℂ=M₂(ℂ)`, Hamilton relations hold; 120/120 ⊂ SU(2)).
  It sends quaternionic (β=4) structure to complex (β=2) structure — the
  antiunitary `J` leaves the commutant. **But** it is a representation map: it
  does not act on a zero-spectrum and does not produce zeta statistics.
- **At the spacing level, no candidate non-circularly turns GSE spacing into GUE
  spacing.** B3 (drop Kramers) and B4 (half-spectrum) of a true GSE matrix stay
  β=4. The one candidate that *does* return β=2 — "restrict each quaternion block
  to its complex entry" — is **circular**: it literally constructs a GUE matrix,
  not a canonical projection of the arithmetic object. GSE and GUE are distinct
  universality classes; there is no canonical spacing bridge.
- **B5/B6 collapse to known RH content**: the explicit formula and Weil
  positivity. They are not new β-objects; they are the prime↔zero duality and the
  positivity criterion already mapped in the prior WO.

## Net

The only canonical, non-circular projection is **B1 complexification**, and it is
symmetry-class-level and zero-blind. The hoped-for *spacing* projection
(β=4-spacing → β=2-spacing) does not exist canonically — and the substrate has no
GSE spacing to begin with (`BETA_CLASS_AUDIT.md`).

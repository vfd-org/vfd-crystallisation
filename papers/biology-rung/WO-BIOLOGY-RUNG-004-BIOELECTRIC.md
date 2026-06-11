# WO-BIOLOGY-RUNG-004-BIOELECTRIC: Planarian Bioelectric Prepattern Eigenmodes on the 2I-Orbit Cell Graph

**Status:** Stub — opens after WO-2 (amyloid) and WO-3 (tubulin) complete
**Date opened:** 2026-04-23
**Classification:** Biology-rung cascade extension + Levin-bioelectric morphogenetic prediction
**Priority:** High scientific-leverage; queue position 4 per programme schedule

---

## 1. Executive Summary

Michael Levin's bioelectric-morphogenesis group at Tufts has
established that planarians can be induced to grow two heads, no
heads, or heterospecific (other-species) heads by manipulating
bioelectric voltage prepatterns — demonstrating that a **bioelectric
code sits above genetics** in determining morphological outcome.

The open question Levin's group asks openly: *what discrete set of
stable bioelectric prepatterns is physically admissible?* Why do
these specific morphological attractors exist and not others?

**Cascade prediction.** If bioelectric prepatterns are eigenmodes
of a closure-operator Laplacian on the cell-level `2I`-orbit
substrate (the 15 × 40 Hopf cell-fibre structure from
`cascade-bio.md §3.1–§3.2`), then:

1. **Stable prepatterns are quantised** — a discrete spectrum
   keyed to `2I` irreps, not a continuum.
2. **Morphology count is predictable** from the `2I` regular
   representation decomposition: normal anterior-posterior, head-
   only, tail-only, double-head, double-tail, and a small finite
   set of `off-target' patterns corresponding to non-trivial
   `2I`-irreducible components.
3. **Transition thresholds** between prepatterns correspond to
   spectral gaps — predicts which voltage perturbations flip
   morphology vs. which relax back.
4. **φ-scaling** of prepattern wavelengths (from `2I`'s intrinsic
   φ structure) — head-to-tail axis ratios should cluster at
   φ-multiples.

### Why this is groundbreaking-tier

- Levin has the **experimental apparatus already running**:
  voltage-clamp, DEPD voltage imaging, regeneration assays.
- The sim output is **a discrete list of allowed morphologies** —
  a regeneration experiment hits or misses a prediction with a
  single image.
- A hit is the **first first-principles derivation of
  morphogenetic attractor states** — the thing Levin's group
  repeatedly says is missing from the field.
- Falsifier is cheap: predict a forbidden bioelectric pattern
  that should not produce a viable morphology, then attempt to
  induce it. Classical bioelectric-manipulation protocol suffices.

### Secondary target (if planarians are too noisy)

Xenopus **bioelectric "electric face"**: Levin showed facial
organs form at bioelectric-pattern sites **before** genetic markers
appear. Predict the discrete set of face-forming voltage patterns
from `2I` eigenmode structure on embryonic ectoderm.

---

## 2. Goals

### 2.1 Primary (must)

1. **Define** a cascade closure-Laplacian `Δ_casc` on the 600-cell
   cell-level graph (or its `2I`-quotient orbit graph, 5 orbits
   per `R.0` in the WO-1 catalogue).
2. **Compute** its eigenspectrum and identify the first N low-
   lying eigenmodes (N ≈ 10).
3. **Classify** each eigenmode by `2I` irrep type.
4. **Map** eigenmodes onto candidate morphological attractors
   (normal AP axis, double-head, etc.) via a discretised Cartesian
   →-axial projection.
5. **Compare** predicted attractor set against the catalogued
   outcomes in Levin et al.'s published regeneration data
   (particularly Beane et al. 2011, Durant et al. 2017,
   Pietak & Levin 2016).

### 2.2 Secondary (should)

6. **Predict a forbidden morphology** — i.e. an eigenmode or
   combination that the cascade spectrum does not support — and
   state the experimental conditions under which it should fail
   to stabilise.
7. **φ-scaling check** — compare predicted wavelength ratios
   against measured axis ratios in regenerating planarians.

### 2.3 Stretch (cancer / regeneration / disease relevance)

The deep disease-relevance here is **tissue regeneration**: if
morphogenetic attractors are predictable from cascade geometry,
that opens theoretical handles on wound healing, limb regeneration
(Levin's axolotl work), and, speculatively, cancer (where
bioelectric patterns are known to be disrupted in tumour tissue
— see Levin 2021). A sim hit on planarians would justify
extending to these.

---

## 3. Dependencies

- WO-1 complete (closure-operator machinery, catalogue convention)
- WO-2 amyloid (φ-helical orbit infrastructure from `cascade-bio.md §B2`
  is shared with the spatial Laplacian we'd need here)
- WO-3 tubulin (shares the cell-graph Laplacian machinery)
- `cascade-bio.md §3.1–§3.2` (Hopf cell-fibre structure must be
  accessible as a cell graph)
- Public Levin-group data: Beane et al. 2011 *Regeneration*,
  Durant et al. 2017 *Biophys J*, Pietak & Levin 2016 *J R Soc
  Interface*, Levin 2021 *Cell* perspective

---

## 4. Math to Derive (catalogue-style preview)

To be worked out when WO-4 opens. Anticipated new entries:

- **D** cell graph `G_600`: vertices = 600 cells, edges = face-
  sharing adjacency, with `2I`-quotient form `G_{600/2I}` having
  5 vertex orbits.
- **D** cascade closure-Laplacian `Δ_casc` on `G_{600/2I}`
  (restriction of the F2 closure form to graph Laplacian data).
- **T / L** first non-trivial eigenmode identification: expected
  to carry the `4`-dim A_5 irrep (anterior-posterior axial
  symmetry).
- **C** correspondence between low eigenmodes and Levin's
  catalogued morphologies.

---

## 5. Status Log

- 2026-04-23: WO opened as stub after user request to queue the
  Levin prediction as WO-4. Positioned after WO-2 (amyloid) and
  WO-3 (tubulin).
- 2026-04-24: promoted to active via pair-programmer loop.
  Build B_orbits SIM-VERIFIED (5 orbits × 120 cells, free 2I
  action) at `scripts/wo4_sim_close_orbits.py`. Build B_laplacian
  computational evidence (27 distinct eigenvalues, low-mode
  multiplicities = squared dims of first 6 2I irreps, χ(−e)
  parity alternation) at `scripts/wo4_sim_close_laplacian.py`.
  Codex-5.5 gap report at
  `docs/codex-derive/TASK-close-remaining-gaps-20260423T235234Z.md`.

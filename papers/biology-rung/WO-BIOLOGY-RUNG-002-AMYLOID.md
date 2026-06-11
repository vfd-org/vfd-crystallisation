# WO-BIOLOGY-RUNG-002-AMYLOID: Cross-β Amyloid Fibril Twist from 2I-Invariant Helical Orbits

**Status:** Active scope (promoted from stub 2026-04-23 after WO-1 passed codex)
**Date opened:** 2026-04-23
**Classification:** Biology-rung cascade extension + disease-target prediction
**Priority:** Next active WO after WO-1

---

## 1. Executive Summary

Cross-β amyloid fibrils are the shared pathological architecture of
a family of diseases:

- **Type 2 diabetes** — islet amyloid polypeptide (IAPP / amylin)
- **Alzheimer's disease** — amyloid-β (Aβ₁₋₄₀, Aβ₁₋₄₂), tau (paired
  helical filaments in NFTs)
- **Parkinson's disease** — α-synuclein (Lewy body fibrils)
- **Prion diseases** — PrP^Sc
- **Systemic amyloidoses** — light-chain, transthyretin, etc.
- **Cancer-associated aggregation** — gain-of-function oncogenic
  p53 mutants form amyloid-like fibrils

Every cross-β fibril has a measurable **per-strand twist angle**
(~1--5° for most pathological amyloids in cryo-EM structures),
**crossover distance** (~100--1000 Å), and **protofilament count**
(1--4 typically). These geometric parameters are set at the level
of the polypeptide backbone but must be consistent with whatever
discrete helical pitches the underlying substrate admits.

### Upstream substrate: the B2 decagram

`cascade-bio.md §5.1` (B2 result, complete) establishes the cascade's
natural helical substrate: along a 5-fold axis of the 600-cell, the
120 vertices resolve into pentagon layers whose combined orbit is a
**regular decagram** with **10 vertices per 2π turn** — the pitch
that matches DNA's 10 bp/turn B-form (§5.2, B4 result).

Cross-β amyloid fibrils, however, twist at ~2° per strand — much
slower than 36° per step. Either:

- **(a)** a finer helical orbit class in the 600-cell's cell-level
  structure (600 cells, not 120 vertices) admits slower pitches;
- **(b)** a commensurate ratio of two helical orbits (e.g. a
  pentagon in-plane rotation within the decagram axial pitch)
  yields an effective fibril-scale pitch;
- **(c)** amyloid fibrils live on an entirely different cascade orbit
  class than DNA / α-helix / collagen (which are the B2 acceptance
  targets per `cascade-bio.md §B2`).

Settling which of (a)--(c) is correct is the analytic meat of this
WO.

### Prediction this WO tests

Cross-β fibril per-strand twist angles cluster on a **discrete set
of cascade-admissible pitches**. Deviations from that set are
energetically disfavoured; proteins whose backbone geometry lands
close to an admissible pitch are amyloidogenic, those landing far
from one are not. The falsifier is cheap: cryo-EM databases
(Amyloid Atlas, PDB cross-β entries, EMDB maps) tag many fibrils
with a twist angle in degrees.

---

## 2. Goals

### 2.1 Primary (must)

1. **Enumerate** cascade-admissible helical closure orbits on the
   600-cell (both vertex-level and cell-level) with fixed 5-fold
   rotation axis. Derive the admissible per-step twist-angle set
   `{θ_i}` with φ-related structure.
2. **Identify** which subset of `{θ_i}` is compatible with
   cross-β strand spacing of ~4.7 Å (this may exclude the fast
   decagram pitch and pick out slower orbits).
3. **Compare** the predicted admissible twist set against observed
   per-strand twist angles in a curated cryo-EM dataset (Amyloid
   Atlas / PDB cross-β). Report hit / partial / miss per amyloid
   species.

### 2.2 Secondary (should)

4. **Predict** which specific proteins are amyloidogenic vs. not,
   based on backbone-geometry proximity to the admissible pitch
   set. This requires an extra layer of analysis (mapping
   polypeptide backbone helicity parameters to cascade orbit
   classes) but is directly testable against known amyloid vs.
   non-amyloid proteins.
5. **Relate** the cascade-predicted twist to the **p53 oncogenic
   aggregation** literature: cancer-associated p53 missense
   mutants destabilise the native fold and gain amyloid-forming
   capacity. Does the cascade predict which p53 mutations are
   geometrically compatible with amyloid versus not?
6. **Protofilament count**: predict the allowed multi-protofilament
   bundle symmetries (single, paired helical filament, triple,
   quadruple) from 2I subgroup structure.

### 2.3 Disease-specific empirical targets (stretch)

Each target is an individual falsifier:

| Disease | Protein | Observed twist (° / strand) | Prediction bucket |
|---|---|---|---|
| T2D | IAPP (amylin) | varies by polymorph (~2–5°) | set by cascade orbit |
| AD | Aβ₁₋₄₂ | polymorphic; common ~2° | set by cascade orbit |
| AD | Tau PHF | ~1° | set by cascade orbit |
| PD | α-synuclein | ~1.5–2° | set by cascade orbit |
| Prion | PrP^Sc | structure-dependent | set by cascade orbit |
| Cancer-p53 | aggregation-prone mutants | limited data | prediction-first target |

A run against this table with honest hit/partial/miss is a
biology-rung-level result regardless of outcome.

### 2.4 Non-goals

- Kinetics of fibril growth / nucleation / elongation rates.
- De novo drug design against amyloids.
- Native-fold prediction of any individual protein (we predict
  fibril-state geometry, not native-state structure).

---

## 3. Dependencies

- **WO-1 complete** ✓: closure-operator machinery, catalogue
  convention, `μ` / chirality infrastructure, codex-loop review
  workflow.
- **`cascade-bio.md §5.1` (B2 decagram result)**: the baseline
  10-vertex-per-turn helical orbit along a 5-fold axis. Need to
  decide whether slower amyloid pitches come from finer orbits or
  from orbit ratios.
- **`cascade-bio.md §3.2` (Hopf 15×40 fibration, conjectural)**:
  cell-level orbits that could provide slower pitches. Inherits the
  upstream conjectural status — if cell-level orbits are required,
  we need to either prove the Hopf fibration or proceed with the
  same conjectural-status hedge as WO-1's [C.2].
- **Cryo-EM structural-biology public resources**: Amyloid Atlas
  (amyloidatlas.org or equivalent), PDB cross-β entries, EMDB maps
  tagged with fibril geometry. Fetch path via PDB REST API (public,
  stable); not expected to have the endpoint-freshness issue that
  hit WO-1's VIPERdb fetch.

---

## 4. Math to Derive (catalogue-style preview)

Planned new entries (to be opened when WO-2 derivation starts):

- **D** Helical closure orbit: a cascade orbit
  `(c_0, c_1, c_2, \ldots)` with `c_{i+1} = R \cdot c_i` for a
  fixed rotation `R \in 2I` of axial type.
- **D** Admissible pitch spectrum: the set of per-step rotation
  angles realised by such orbits, organised by 2I conjugacy class.
- **T / L** Pitch-enumeration theorem for 600-cell cell-level
  helical orbits (if cell-level is needed; otherwise vertex-level).
- **C** Amyloid-twist selection conjecture: cross-β fibrils select
  the subset of admissible pitches compatible with 4.7 Å strand
  spacing.
- **C** Amyloidogenicity selection rule: a polypeptide is
  amyloidogenic iff its backbone-helicity parameters lie within
  a cascade-specific distance of the admissible pitch set.
- **N** Sim output: enumerate pitches for `T_max` vertex and cell
  depths; compare against curated amyloid twist database.

---

## 5. Scripts (planned)

- `scripts/wo2_helical_orbits.py` — enumerate admissible pitches
- `scripts/wo2_amyloid_fetch.py` — pull observed twist-angle data
  from Amyloid Atlas / PDB / EMDB; same two-mode fetch pattern as
  `wo1_viperdb_fetch.py`
- `scripts/wo2_compare.py` — χ², KL, per-species comparison; same
  pattern as `wo1_compare.py`

---

## 6. Acceptance Criteria

1. Derivation passes codex review: "Publication ready: yes" on
   substantive math / attribution / sim-correctness scope
   (same gate as WO-1).
2. Math-catalogue updated with every new D/L/T/C/N entry.
3. Sim enumerates admissible pitches end-to-end.
4. Empirical comparison against at least one amyloid species
   (preferably multiple) performed, reported honestly.
5. Clear statement of whether (a), (b), or (c) from §1 holds.

---

## 7. Codex Review Invocation

```
bash scripts/review_wo.sh papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md \
  --derivation papers/biology-rung/derivation-amyloid.md \
  --catalogue papers/biology-rung/math-catalogue.md \
  --sim papers/biology-rung/scripts/wo2_helical_orbits.py \
  --focus "Round N: verify ..."  < /dev/null
```

Reuse the review loop pattern from WO-1.

---

## 8. Status Log

- 2026-04-23: WO opened as stub.
- 2026-04-23: WO promoted from stub to active scope after WO-1
  passed codex publication-ready gate (6 rounds). Ready to start
  derivation next session. Math bridge: B2 decagram → amyloid pitch
  via orbit-class enumeration.

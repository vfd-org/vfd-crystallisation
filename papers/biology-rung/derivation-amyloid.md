# Derivation: Cross-β Amyloid Fibril Twist from 2I Helical-Orbit Classes

**WO:** WO-BIOLOGY-RUNG-002-AMYLOID
**Date opened:** 2026-04-23
**Status:** Round 2 post-codex-review, revised

This document explores the hypothesis that *cross-β amyloid fibril
per-strand twist angles sit on a discrete set of cascade-compatible
pitches, arising from commensurability conditions between the
polypeptide backbone's β-strand stacking and cyclic-subgroup
structure on the 600-cell's 5-fold axis*. The hypothesis is
stated conditionally; the main derivation step imports the
classical commensurability rule onto the cascade substrate rather
than deriving it from scratch. It extends the B2 decagram
result (`cascade-bio.md §5.1`) from the single fast helical pitch
of DNA (10 vertices/turn = 36°/step) to the full enumeration of
helical-orbit classes on the 5-fold axis, and asks which classes
are compatible with the ~4.7 Å strand spacing that defines cross-β
architecture.

The disease relevance is that cross-β amyloid fibrils are the
shared pathological architecture of type 2 diabetes (IAPP/amylin),
Alzheimer's (Aβ, tau), Parkinson's (α-synuclein), prion diseases
(PrP^Sc), systemic amyloidoses, and cancer-associated
gain-of-function aggregation (oncogenic p53). A cascade prediction
of the admissible per-strand twist set is simultaneously a
prediction for every disease in this family.

Every new mathematical object introduced here is catalogued in
`math-catalogue.md` with prefix D/L/T/C/R/N prefixed by
``(WO-2)''.

---

## §1. Preliminaries

### 1.1 Cross-β architecture and fibril twist

A cross-β amyloid fibril is a linear polymer of β-strands stacked
perpendicular to the fibril axis, held by main-chain hydrogen
bonds. Canonical geometric parameters (from cryo-EM structures;
see e.g. the Amyloid Atlas):

- **Strand stacking along fibril axis**: `d_β ≈ 4.7 Å` per strand,
  essentially fixed by β-sheet H-bond geometry.
- **Per-strand twist angle**: `θ_twist`, a small rotation about the
  fibril axis that accumulates along the fibril.
  Typical range: `1°–5°` per strand, depending on amyloid species
  and polymorph.
- **Crossover distance**: `L_co = 360° · d_β / θ_twist ≈
  100–500 Å`. A crossover is the axial period after which the
  fibril cross-section returns to the same orientation modulo the
  fibril's own point-group symmetry.
- **Protofilament count**: typically 1, 2, 3, or 4 protofilaments
  bundled together, with inter-protofilament symmetry being `C_n`
  or `D_n` for `n = 1, 2, 3, 4`.

A key empirical observation: across a wide range of amyloid
species, `θ_twist` does not take arbitrary values in `[1°, 5°]`;
cryo-EM surveys find specific discrete clusters (e.g. Aβ₁₋₄₂ at
~1°, ~2°, ~4.7° polymorphs; α-synuclein at ~2°; tau PHF at ~1°).
This paper asks whether these discrete cluster values match the
cascade's 2I-commensurability predictions.

### 1.2 The VFD cascade Life substrate

From WO-1 / `cascade-bio.md §2.1–2.3`: the binary icosahedral group
`2I ⊂ SU(2)` of order 120 acts as the vertex set of the 600-cell;
quotient `I = 2I/{±1} ≅ A_5` of order 60. Along a 5-fold rotation
axis of the 600-cell, the 120 vertices distribute in layers with
pentagon / decagon / equator sub-structure
(`cascade-bio.md §5.1`, B2 result). The natural fast helical orbit
is the **decagram**: 10 vertices per 2π turn, giving 36°/step
(matched to DNA's 10 bp/turn).

For amyloid geometry we need *slower* helical pitches than the
decagram's 36°/step. The question is: what other helical-orbit
classes does the 600-cell admit on a fixed 5-fold axis, and which
of them produce small-angle per-step rotations compatible with
~4.7 Å strand spacing?

---

## §2. Helical Closure Orbits on the 5-Fold Axis

### Definition [D.1] (WO-2) — Helical closure orbit

Fix a 5-fold rotation axis `A ⊂ ℝ⁴` of the 600-cell with unit
axial direction `ẑ`. Let `R_α ∈ 2I` be a rotation about `A` by
angle `α`, and let `T_h` be an axial translation by height `h`
(acting on an infinite stack of 600-cell copies glued along the
axis). A **helical closure orbit of pitch `(α, h)`** is the
orbit of a base point `x_0 ∈ 600`-cell under the infinite cyclic
group `⟨ R_α · T_h ⟩`, i.e.

  `Orb(α, h) = { (R_α · T_h)^n x_0 : n ∈ ℤ }`.

Two pitches `(α_1, h_1)` and `(α_2, h_2)` are **2I-equivalent** if
they differ by conjugation in `2I × ℝ` (i.e. if there is `g ∈ 2I`
and a reparametrisation of the axial period bringing one to the
other).

The orbit is **closure-compatible** if, after finitely many steps,
the orbit closes (returns to its starting cell modulo an axial
translation by one period `P`). Equivalently: `α` is a rational
multiple of `2π` with denominator `q`, so `(R_α)^q = 1 ∈ 2I` and
the orbit has period `qP` axially.

### Lemma [L.1] (WO-2) — Admissible angle set on the 5-fold axis

Fix a 5-fold axis `A` of the icosahedral symmetry type `C_5` in
`I ≅ A_5`. The preimage of `Stab_I(A) ≅ C_5` in the double cover
`2I → I` is cyclic of order 10: the short exact sequence
`1 → {±1} → 2I → I → 1` restricted to this stabiliser gives a
central extension of `C_5` by `C_2`, and since `|C_5| · |C_2| = 10`
is squarefree the extension splits into `C_10 = C_5 × C_2`. The
SU(2) rotation angles (defined as the angle θ such that a lift of
R is `cos(θ/2) + sin(θ/2)·n̂·σ̂` for axis unit vector `n̂`) of the
10 elements of this preimage are

  `Stab_2I(A) = { α : α = 2π k / 10, k = 0, 1, …, 9 } = {0°, 36°, 72°, 108°, 144°, 180°, 216°, 252°, 288°, 324°}`.

These are the 10th roots of unity on SU(2) about the axis `A`,
and form a cyclic subgroup `C_10 ⊂ 2I` of order 10.

**Proof.** Because the central extension
`1 → {±1} → 2I → I → 1` has kernel of order 2 and quotient-
stabiliser of order 5 with `gcd(2, 5) = 1`, it splits over the
5-fold stabiliser subgroup (by the Schur–Zassenhaus theorem, or
equivalently by direct construction: `C_5 × C_2 ≅ C_10` since
the orders are coprime). Cyclic subgroups of order 10 in `SU(2)`
about a fixed axis realise the 10th roots of unity as SU(2)
rotations `exp(i·(α/2)·n̂·σ̂)` with `α = 2πk/10` for
`k = 0, …, 9`. □

**Corollary [C.1 of L.1].** The smallest nonzero angle in
`Stab_2I(A)` is `36°` — the decagram step.

### Remark [R.1] — The small-angle problem

Empirical amyloid twist angles cluster in the `1°–5°` range. By
L.1 / Corollary, these are **not directly achievable by single
2I-element rotations** about a 5-fold axis. Under the fixed
5-fold-axis single-element model, this suggests the small-angle
twist emerges from compounded steps or from structures outside
the strict single-2I-element rotation class. Three candidate
mechanisms to explore:

- **(a) Commensurable compound rotations.** A small twist
  `θ_twist` is the residual of composing a "fast" axial
  reorientation `R_α ∈ Stab_2I(A)` (one of `36°, 72°, …`) with a
  "slow" axial translation that carries the fibril between cells
  differing by an additional small rotation. If the composite is
  nearly-periodic with near-360° return after many strands, the
  per-strand residual can be small.
- **(b) Cell-level orbits (not vertex-level).** The 600 cells of
  the 600-cell are finer than its 120 vertices. Orbits of cells
  under `2I · T_h`-type actions can in principle give more
  orbit classes than pure vertex orbits.
- **(c) Subgroup orbits.** Helical orbits of subgroups of 2I
  (binary tetrahedral `2T`, binary dihedral `2D_n`, or pure
  cyclic `C_n`) acting on 2I itself can generate finer axial
  structures.

We take (a) as the primary hypothesis in this document. (b) and
(c) are sketched in §6 but not worked out.

### Definition [D.2] (WO-2) — Commensurable twist family

Fix `α ∈ Stab_2I(A) \ {0}`, an integer `N ≥ 1`, and integers
`(p, q)` with `gcd(p, q, N) = 1`. The **commensurable twist at
triple `(α; p, q, N)`** is

  `θ(α; p, q, N) := (p · α − q · 2π) / N`  (reduced modulo 2π).

Geometrically: after `N` strands along the fibril axis, the
helical pattern has accumulated `N · θ` of rotation, which equals
`p · α − q · 2π`. In other words: `N` strands make a full closure
advance of `p · α` axially (i.e. `p` applications of `R_α`) minus
`q` full turns about the axis.

`N` is a **parameter of the family**, not a derived quantity: for
each choice of `(α, p, q, N)` we get one twist value. The
earlier draft defined `N` as ``the smallest such'' value, which
was circular — we remove that condition here.

The **commensurable twist set at axis `A` with resolution
`N_max`** is

  `Θ_adm(A; N_max) = { θ(α; p, q, N) : α ∈ Stab_2I(A)\{0}, 1 ≤ N ≤ N_max, 0 ≤ p ≤ N, |q| ≤ N }`.

For `α = 36° = 2π/10`, a direct calculation gives `θ(36°; p, q, N)
= 36°·(p − 10q)/N`, so with `α` fixed the commensurable twists are
integer multiples of `36°/N`. Different `α ∈ Stab_2I(A)` do
**not** enlarge the set of attainable angles (since every α in
`Stab_2I(A)` is itself an integer multiple of 36°, the attainable
twists remain within the `36°/N · ℤ` ladder); this simplifies the
enumeration.

### Lemma [L.2] (WO-2) — Countability and accumulation at zero

`∪_{N_max ≥ 1} Θ_adm(A; N_max)` is countable (as a countable union
of finite sets), dense in `ℝ/2π` by Weyl's equidistribution
theorem (since `36°/(2π)` is rational), and has `0` as an
accumulation point: for each `ε > 0` there exist `(p, q, N)` with
`0 < θ(36°; p, q, N) < ε` (take large `N` and suitable `p, q`).

**Proof sketch.** The commensurable twists are integer multiples
of `36°/N`; as `N → ∞`, `36°/N → 0`, so for any `ε > 0` we can
choose `N > 36°/ε` and take the smallest positive integer
multiple. Density follows from the fact that `{m/N : m ∈ ℤ, N ≥
1}` is dense in `ℝ`. Countability is immediate. □

---

## §3. Amyloid-Scale Commensurability

### Definition [D.3] (WO-2) — Amyloid-scale compatibility

A twist angle `θ` is **amyloid-scale compatible** if there exists
a positive integer `M` with

  `M · θ = 360°` (full crossover) AND
  `M · d_β = M · 4.7 Å ∈ [100 Å, 500 Å]` (observed crossover range).

Solving: `M ∈ [100/4.7, 500/4.7] = [21.28, 106.38]`, so
`M ∈ {22, 23, …, 106}` (integer `M`). The corresponding range of
`θ` is therefore

  `θ_min = 360°/106 ≈ 3.3962°`, `θ_max = 360°/22 ≈ 16.3636°`.

Equivalently: **amyloid-scale-compatible θ ∈ [3.4°, 16.4°]**
(rounded to one decimal). The previous draft's upper bound
`17.1°` corresponded to `M = 21`, which gives crossover
`21 · 4.7 = 98.7 Å`, below the 100 Å lower bound; corrected here.

Ultra-slow-twist polymorphs (observed twists < 3.4°, corresponding
to crossover > 1500 Å in some tau/α-synuclein structures) lie
outside this filter and are discussed in Remark R.2 and
Conjecture C.4.

### Lemma [L.3] (WO-2) — Cascade-admissible amyloid twists (enumeration)

The commensurable twists `θ = 36°·(p − 10q)/N` that lie in
`[3.4°, 16.4°]` for `N ≤ 20` form a finite discrete set. Some
representative values (from `scripts/wo2_helical_orbits.py`
with the corrected window):

  `θ = 36° / N` for `N = 3, 4, 5, 6, 7, 8, 9, 10`
  gives `θ ∈ {12.0°, 9.0°, 7.2°, 6.0°, 5.143°, 4.5°, 4.0°, 3.6°}`.

`36°/11 ≈ 3.273°` is **below** the corrected lower bound
`3.3962°` and so is \emph{not} admissible under D.3 (the earlier
draft's `[3.3962°, 16.3636°]` window included it erroneously).

All admissible twists under D.3 are integer multiples of `36°/N`;
`α ∈ {72°, 108°, 144°, 180°}` gives no new angles beyond this
ladder, as noted in D.2. The enumeration is complete for
`N ≤ 20`.

**Status.** Computational; see sim output at
`data/wo2_prediction.csv`. Sim N.1 below.

### Conjecture [C.1] (WO-2) — Amyloid twist selection rule

Observed cross-β amyloid per-strand twists cluster on the
enumerated subset
`Θ_adm(A) ∩ [3.3962°, 16.3636°]`, with deviations attributable to
polymorph-specific backbone mechanics rather than continuous
distribution over this range.

**Status.** Conjectural; tested empirically against Amyloid Atlas
/ PDB cross-β entries (script `wo2_compare.py` pending, same
WAITING_FOR_DATA design as WO-1).

**Empirical prediction.** A histogram of observed per-strand
twists over a curated amyloid dataset should show peaks at the
L.3-enumerated values with width set by measurement precision
and polymorph heterogeneity. A uniform distribution over
`[3.3962°, 16.3636°]` would falsify.

### Remark [R.2] — Ultra-slow-twist polymorphs

Some tau PHF and α-synuclein polymorphs report per-strand twists
well below 3.4° (sometimes < 1°), corresponding to crossover
distances > 1500 Å. Three non-exclusive explanations:

- **(i)** These sit in `Θ_adm` at higher denominators `N > 106`,
  technically within the definition of L.2 but outside the
  canonical "short" crossover range.
- **(ii)** They represent a different 2I-orbit class (not
  pentagon-stack-derived, but e.g. 3-fold-axis-derived with
  different baseline angular units).
- **(iii)** The cascade prediction bounds `θ_twist` from below
  only loosely at `θ_min = 360°/M_max`, where `M_max` is itself
  set by biological constraints (maximum fibril length / minimum
  fibril stability threshold) rather than purely by cascade
  geometry.

This is flagged as an open question rather than claimed to be
resolved by the current derivation.

---

## §4. Chirality and Protofilament Count

### Conjecture [C.2] (WO-2) — Handedness of the cascade fibril

The `2I` group has intrinsic handedness (per
`cascade-bio.md §2.7` / `§B5`): the god-prime `2^n + 1` structure
selects one enantiomer. If amyloid fibrils inherit their
handedness from the cascade substrate (via the WO-1
chirality-asymmetry thread [C.3]), cross-β fibrils should
empirically show a handedness bias consistent with the L-amino-
acid world.

**Status.** Qualitative. Cryo-EM amyloid handedness data is
available in per-structure form (left-handed vs. right-handed
twist); a meta-analysis across the Amyloid Atlas could test this.
Magnitude of the asymmetry is not derived.

### Conjecture [C.3] (WO-2) — Protofilament count from 2I subgroups

Observed amyloid fibrils bundle into 1, 2, 3, or 4 protofilaments
with `C_n` / `D_n` bundle symmetry. The cascade prediction: the
admissible protofilament bundle symmetries correspond to the
non-trivial cyclic and binary-dihedral subgroups of `2I`:

- `C_1` — single protofilament
- `C_2` — 2-protofilament bundle (paired helical filament)
- `C_3` — 3-protofilament bundle (rare but observed, e.g. in
  some Aβ variants)
- `C_5` — 5-protofilament bundle (predicted but not commonly
  observed; would be a clean falsifier if absent despite careful
  search)
- `D_2` — 4-protofilament bundle with dihedral symmetry
- (others: `C_4`, `D_3`, `D_5` — predictions)

**Status.** Conjectural; testable against cryo-EM protofilament-
count statistics.

---

## §5. Disease-Specific Empirical Targets

The predictions of C.1–C.3 apply uniformly across the amyloid-
disease family. The table below lists per-disease empirical
targets that will be populated when the observed-data pipeline
is built:

| Disease | Protein | Observed twist | Observed crossover | Predicted bucket |
|---|---|---|---|---|
| Type 2 diabetes | IAPP (amylin) | polymorph-dependent; cryo-EM ~4.5° some structures | varies | `Θ_adm` subset |
| Alzheimer's | Aβ₁₋₄₂ polymorphs | ~1° to ~5° range | ~400–800 Å | `Θ_adm` subset |
| Alzheimer's | Tau (PHF) | ~1° | ~800 Å | R.2 regime |
| Parkinson's | α-synuclein | ~2° | ~700 Å | `Θ_adm` subset |
| Prion disease | PrP^Sc | structure-dependent | varies | — |
| Cancer-associated | p53 aggregation-prone mutants | limited data | — | open |

A hit/partial/miss per row is a biology-rung-level result.

---

## §6. Open Items

### C.4 (WO-2) — Cell-level orbit supplement

The present derivation (D.1–D.3, L.1–L.3) uses vertex-level 2I
orbits on a fixed 5-fold axis. Amyloid twists below the L.3
minimum (ultra-slow-twist polymorphs, Remark R.2) may require
cell-level orbits on the 600 tetrahedral cells of the 600-cell.
A full cell-level pitch spectrum is not enumerated here;
constructing it would give a finer admissible twist set and could
absorb the sub-3° polymorphs.

**Status.** Open. Dependency: needs the conjectural 15 × 40 Hopf
cell-fibration of `cascade-bio.md §2.6 / §3.2` to be settled (or
an alternative cell-partition).

### C.5 (WO-2) — Axis selection

This derivation fixes the 5-fold axis. The 600-cell also has
3-fold, 4-fold (not simple), and 2-fold axes. Different amyloid
polymorphs could correspond to different axis choices; a
multi-axis enumeration would test this. Not attempted here.

### C.6 (WO-2) — Relation to the WO-1 closure operator

Whether the amyloid twist selection rule can be framed as the
spectrum of a cascade operator (parallel to the face-level
`𝒯_casc` of WO-1 [T.1]) is an open question. If yes, WO-1 and
WO-2 would share a common closure-operator formalism, extending
the programme's coherence.

---

## §7. Summary

**What is derived ($\blacktriangleright$).**
- **[L.1]** `Stab_2I(A) = {k · 36° : k = 0, …, 9}` for a 5-fold
  axis `A`; smallest nonzero single-2I rotation is 36°.
- **[L.2]** `Θ_adm(A)` (commensurable twist set) is discrete and
  has zero-accumulation points.
- **[L.3]** Finite enumeration of `Θ_adm(A) ∩ [3.3962°, 16.3636°]`
  compatible with amyloid crossover ranges.

**What is identified ($\triangleright$).**
- **[R.1]** Small-angle amyloid twists must emerge from
  commensurable compounds, not from single 2I-element rotations.
- **[R.2]** Ultra-slow-twist polymorphs are flagged as an open
  regime (cell-level orbits, subgroup orbits, or loose lower
  bound).

**What is open ($\circ$).**
- **[C.1]** Amyloid twists select from `Θ_adm ∩ [3.3962°, 16.3636°]` —
  empirical test pending.
- **[C.2]** Cascade chirality prediction for fibrils — qualitative.
- **[C.3]** Protofilament count from 2I subgroups —
  enumerable, test pending.
- **[C.4]** Cell-level orbit supplement — not constructed.
- **[C.5]** Multi-axis enumeration — not attempted.
- **[C.6]** Unified WO-1+WO-2 closure operator — open.

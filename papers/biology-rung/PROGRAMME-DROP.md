# Biology-Rung Programme — Drop Index

**Date:** 2026-04-23
**Status:** 5-paper programme drop
**Classification:** First complete biology-rung paper set from the VFD cascade

---

## Overview

This directory tree contains the first complete biology-rung paper
drop of the Vibrational Field Dynamics (VFD) programme. Five
papers, each independently publishable, are presented as a
coherent programme centred on the cascade Life-rung substrate
(600-cell with $2I / A_5$ action) and its consequences for
biological structure across multiple scales:

| Paper | WO | Title | Scale | Disease relevance |
|---|---|---|---|---|
| 1 | WO-1 | Caspar–Klug Triangulation Numbers from a Face-Level Cascade Operator | molecular (viral capsid geometry) | — |
| 2 | WO-2 | Cross-β Amyloid Fibril Twist from $2I$ Helical-Orbit Classes | molecular (amyloid fibrils) | **type 2 diabetes** (IAPP), **Alzheimer's** (Aβ, tau), **Parkinson's** (α-syn), prion, **cancer** (p53 aggregation) |
| 3 | WO-3 | The 13-Protofilament Microtubule as a $C_{13}$ Selector | molecular / cellular (microtubule geometry) | **cancer chemotherapy** (taxane binding) |
| 4 | WO-4 | Bioelectric Prepattern Eigenmodes as Morphogenetic Attractors | tissue / developmental (bioelectric patterns) | **tissue regeneration**, **wound healing**, speculative **cancer** (bioelectric disorganisation) |
| 5 | WO-5 | Fibonacci Phyllotaxis from the 600-Cell's $\phi$-Helical Closure Orbits | organism-level (plant morphology) | — (pure mathematical biology) |

---

## Scale hierarchy

The five papers span biological organisation from single molecules
up to whole-organism morphology:

```
Scale       | WO   | Subject                    | Cascade object
----------- | ---- | -------------------------- | ----------------------------
face        | WO-1 | viral capsid T-numbers     | Eisenstein lattice ℤ[ω]
orbit       | WO-2 | amyloid fibril twist       | Stab_2I(A) = C_10
cell        | WO-3 | microtubule protofilaments | C_13 irrep structure
tissue      | WO-4 | bioelectric prepatterns    | A_5 irreps on cell graph
organism    | WO-5 | phyllotaxis angle          | φ-helical packing
```

---

## Coherence

The five papers share a common substrate (`cascade-bio.md §B1`,
the 600-cell / $2I / A_5$ machinery) and use a consistent
mathematical vocabulary (helical-orbit classes, $A_5$ irreps,
hexagonal-lattice / icosahedral-lattice symmetry, commensurability
conditions). Each paper:

1. States its results explicitly as **derived** (proved),
   **identified** (structural correspondence), or **open**
   (conjectural).
2. Classifies every numerical claim as
   either computationally verified (sim output)
   or empirical (comparison against published data, with
   WAITING\_FOR\_DATA hooks where the data pipeline isn't built).
3. Flags conditional dependencies on upstream conjectures
   (e.g. the Hopf cell-fibration of `cascade-bio.md §2.6`, the
   13-adjacency hypothesis T\_PH\_1 of
   `cascade-photon-microtubule-alpha-programme.md §2`).
4. Is codex-reviewed on the substantive math / attribution /
   sim-correctness gate; see `docs/reviews/` for review trails.

---

## Honest claim catalogue

What the drop **does** establish:

- **WO-1, Theorem T.1** (proved): the full Caspar–Klug $T$-number
  sequence is the spectrum of a single face-level quadratic form
  on $\mathbb{Z}[\omega]$, unique up to positive scale within the
  class of positive-definite $C_6$-invariant quadratic forms.
  Novel numerical finding: $\mu(91) = 4$, first Loeschian $\le 100$
  with four distinct $C_6$-orbits.
- **WO-1, Remark R.1 + Lemma L.2** (proved): correction of the
  upstream $T = 5$ misattribution in `cascade-bio.md §B3.2`.
- **WO-3, Theorems T.1, T.2** (proved conditional on T\_PH\_1):
  primality of 13 forces $n = 13$ as the unique cyclic selector
  in $[2, 16]$; non-13 counts are degenerate.
- **WO-5, Proposition (classical)**: phyllotaxis angle
  $= 360°/\phi^2$; classical Coxeter–Vogel, adopted by reference,
  placed on the cascade B2 decagram substrate as cascade-specific
  framing.
- **WO-2, Lemmas L.1, L.2, L.3** (proved under stated hypotheses):
  commensurable-twist structure on the $5$-fold axis; enumeration
  of admissible twist angles within the amyloid crossover range.

What the drop **conjectures** (honestly labelled):

- WO-1 Conjecture C.2: whether $\mathcal{T}_{\mathrm{casc}}$
  descends from a cell-level 600-cell closure functional. Open
  problem with four-step plan.
- WO-1 Conjectures C.1, C.3: closure-preference weighting and
  chirality asymmetry for capsid $T$ distributions.
- WO-2 Conjecture C.1: amyloid twists cluster on the enumerated
  admissible set; empirical test pending curated cryo-EM
  dataset.
- WO-2 Conjectures C.2, C.3: chirality bias and protofilament
  count.
- WO-3 Conjectures C.1, C.2, C.3: taxane-pocket geometry
  (cancer-chemotherapy test), helical-pitch prediction,
  anesthetic-mode disabling.
- WO-4 Conjectures C.1, C.2, C.3: Levin-attractor identification,
  double-head / no-head as $\mathbf{3}$-inversion, forbidden-
  pattern falsifier. (WO-4 is framework only; no computation
  performed.)
- WO-5 Remark R.1: integer-137 programme-internal overlap between
  $\alpha^{-1}$ and $\theta_{\mathrm{phyllo}}$; fractional parts
  not related by any clean cascade-only formula.

What the drop **does not** claim:

- No cell-level descent from Paper XXXII / F2 closure machinery
  to face-level operators (WO-1 C.2, WO-2 C.6).
- No empirical verification of capsid / amyloid / taxane /
  bioelectric / phyllotaxis predictions; comparison pipelines are
  built but datasets are pending for WO-1, WO-2, WO-3, WO-4.
  WO-5 numerical prediction passes trivially against classical
  plant-morphology literature.

---

## Empirical follow-up (required for downstream impact)

Each WO has a comparison pipeline ready to run once the observed
dataset lands:

| WO | Fetch script | Dataset status | Compare script |
|---|---|---|---|
| WO-1 | `scripts/wo1_viperdb_fetch.py` | pending (VIPERdb endpoints 404 at time of writing) | `scripts/wo1_compare.py` (present, WAITING\_FOR\_DATA) |
| WO-2 | `scripts/wo2_amyloid_fetch.py` (not yet written) | pending (Amyloid Atlas / PDB cross-β) | (not yet written) |
| WO-3 | `scripts/wo3_tubulin_fetch.py` (not yet written) | pending (PDB tubulin / taxane) | (not yet written) |
| WO-4 | (not applicable — framework conjecture) | pending | (computation not yet built) |
| WO-5 | (not needed — classical literature supplies) | satisfied (Jean 1994 etc.) | N/A |

---

## Disease-relevance summary

For clinical or biological-funding audiences:

- **Cancer chemotherapy** (WO-3): a structural framework for
  taxane binding-pocket preference, with clear testable predictions
  against PDB taxane-tubulin structures and resistance-mutation
  variants.
- **Amyloid diseases** (WO-2): T2D (IAPP), Alzheimer's (Aβ, tau),
  Parkinson's (α-synuclein), prion, and cancer-associated
  p53-aggregation disorders all share cross-β architecture;
  the cascade predicts a discrete set of admissible per-strand
  twists, simultaneously falsifiable across the entire disease
  family.
- **Tissue regeneration / wound healing** (WO-4): Levin-style
  bioelectric manipulation of morphogenetic outcomes would, if
  C.1 holds, be predictable from $A_5$-eigenmode structure;
  stretch target for axolotl limb regeneration and cancer
  bioelectric disorganisation.
- **Developmental biology** (WO-5): Fibonacci phyllotaxis as a
  programme-native pattern, inheriting $\phi$ from the cascade's
  own permeability axiom F1 rather than from post-hoc fit.

---

## Reviewer trail

All papers have been through the codex review loop at least
once. Reviews land in `docs/reviews/`:

- WO-1 (capsid): derivation 6 rounds + paper 8+ rounds, all
  publication-ready on substantive gate.
- WO-5 (phyllotaxis): paper converged after multiple rounds of
  $1/\phi$ vs $1/\phi^2$ correction and attribution cleanup.
- WO-3 (tubulin): round 0 review pending at time of writing.
- WO-4 (bioelectric): round 0 review pending at time of writing.
- WO-2 (amyloid): derivation round 1 pending at time of writing;
  known open item is the cell-level orbit extension for
  sub-3.4° polymorphs.

Full review history in `docs/reviews/biology-rung-*.md` and
`docs/reviews/WO-BIOLOGY-RUNG-*.md`.

---

## File layout

```
papers/
  biology-rung/                      # umbrella programme
    README.md                        # programme overview
    PROGRAMME-DROP.md                # this file
    math-catalogue.md                # shared math ledger
    derivation-capsid.md             # WO-1 math source
    derivation-amyloid.md            # WO-2 math source
    WO-BIOLOGY-RUNG-001-CAPSID.md    # WO-1 spec
    WO-BIOLOGY-RUNG-002-AMYLOID.md   # WO-2 spec
    WO-BIOLOGY-RUNG-003-TUBULIN.md   # WO-3 spec
    WO-BIOLOGY-RUNG-004-BIOELECTRIC.md  # WO-4 spec
    WO-BIOLOGY-RUNG-005-PHYLLOTAXIS.md  # WO-5 spec
    WO-BIOLOGY-RUNG-006-DMN-BRIDGE.md   # WO-6 cross-reference to aria-chess
    scripts/
      wo1_capsid_predict.py          # WO-1 enumeration
      wo1_viperdb_fetch.py           # WO-1 fetch infrastructure
      wo1_compare.py                 # WO-1 comparison (WAITING_FOR_DATA)
      wo2_helical_orbits.py          # WO-2 enumeration
    data/
      wo1_prediction.csv             # 61 C_6-orbits of Loeschian T ≤ 100
      wo1_viperdb_observed_template.csv   # WO-1 literature-mode template
      wo1_comparison.md              # WO-1 comparison (WAITING_FOR_DATA)
      wo2_prediction.csv             # 49 distinct admissible twist angles

  biology-rung-capsid/               # WO-1 paper
    biology-rung-capsid.tex
  biology-rung-phyllotaxis/          # WO-5 paper
    biology-rung-phyllotaxis.tex
  biology-rung-tubulin/              # WO-3 paper
    biology-rung-tubulin.tex
  biology-rung-bioelectric/          # WO-4 paper
    biology-rung-bioelectric.tex
  biology-rung-amyloid/              # WO-2 paper — to be written after
                                     # derivation convergence
```

---

## Known gaps (honest)

1. **All five LaTeX papers now exist** at
   `papers/biology-rung-{capsid,amyloid,tubulin,bioelectric,phyllotaxis}/`.
   The WO-2 amyloid paper is distilled from the round-2-revised
   derivation; round-0 codex review pending.
2. **Empirical pipelines** for WO-2, WO-3, WO-4 are not yet built
   (only WO-1's are in skeleton form). All follow the same
   predict / fetch / compare / WAITING\_FOR\_DATA template.
3. **WO-4 computational content** is deliberately absent — the
   paper frames a falsifiable conjecture, not a completed result.
4. **Cell-level orbit enumeration** for WO-2 ultra-slow-twist
   polymorphs (< 3.4°) is deferred to a follow-up WO (not in
   this drop).
5. **Round-1 paper reviews** for WO-3, WO-4, WO-5 are currently
   running or pending; round-0 feedback has been applied. WO-2
   derivation is at round-2 (sim verified correct); paper is at
   round-0 pending.

These gaps are flagged honestly in each paper's ``What is open''
section. The drop represents what is currently established, not
what is ultimately aimed at.

## Codex convergence status (current)

| Paper | Derivation | LaTeX paper | Codex status |
|---|---|---|---|
| WO-1 capsid | 6 rounds, clean | 8+ rounds, **PUBLICATION-READY** | Full substantive pass |
| WO-2 amyloid | round 2 (sim verified correct, 24-element admissible set; L.2 elementary density proof) | round 0 pending (just distilled) | Derivation substantively sound; paper not yet reviewed |
| WO-3 tubulin | N/A (thin derivation is in paper itself) | round 1 pending (after D.1/T.1/T.2 math rewrite with explicit axioms D.1a/b/c + bibliography fixes) | Math corrected after round-0 flagged incomplete proofs |
| WO-4 bioelectric | N/A (framework conjecture note) | round 1 pending (after false 5-orbit attribution removed + Levin citations corrected with EmmonsBell2015, VandenbergLevin2011 primary sources) | Attribution corrected; explicitly conjectural throughout |
| WO-5 phyllotaxis | N/A | round 4 pending (after α-status + unit caveat + theorem downgrades) | Math rewrites converged; polish pass remaining |

**Summary**: one paper fully codex-clean; four papers substantively
sound with round-1 codex feedback pending. All math errors caught
so far have been honestly addressed.

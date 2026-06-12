# Existence Programme — Refinement Status

**Refinement workspace:** all 10 papers consolidated at
`release-bundles/existence-programme/papers/`. Each paper directory
contains `main.tex`, `main.pdf`, `references.bib`, and figures or
repro/ folder where relevant.

**This is the authoritative workspace for refinement.** Edits made
here should be propagated back to source locations:
- Papers 01–04: `papers/<slug>/` in the `vfd-crystalisation-paper` repo
- Papers 05–10: `experiments/<slug>/paper/` in the `solution-lab` repo

A sync script lives at `scripts/sync_from_sources.sh` for pulling
fresh source-of-truth content, and `scripts/sync_to_sources.sh` for
pushing refinements back (when those exist).

---

## Programme structure

| # | Title | Pages | Role | Status |
|---|---|--:|---|---|
| 01 | Existence as Closure | 31 | Foundation (flagship pair) | refinement-ready |
| 02 | Life as Closure | 41 | Human bridge (flagship pair) | refinement-ready |
| 03 | From Processing to Point of View | 18 | Neuroscience companion | refinement-ready |
| 04 | Cosmic Self-Pruning and Frame Recurrence | 17 | Cosmology companion (held back from v1.0) | refinement-ready |
| 05 | Bioelectric Closure (SL-001) | 20 | Empirical anchor for Levin bridge | release-ready |
| 06 | Cortical Phase Closure (SL-002) | 17 | Empirical anchor for CEMI / anaesthesia bridge | release-ready |
| 07 | Closure-as-Distance (cross-substrate methodology) | 17 | Validated applicability diagnostic CAD-D1–D5-v1 | release-ready |
| 08 | Trauma Cortical Closure (SL-005) | 9 | Real-data: trait anxiety d=+0.79 on ds007609 | first-result, needs paper-grade write-up |
| 09 | Flow Cortical Closure (SL-006) | 9 | FlowIndex-v1, synthetic 5/5 PASS, ds005520 in progress | hostile-review-ready |
| 10 | Hyperscanning Joint Meaning (SL-007) | 8 | Honest negative on ds007471, diagnostic correctly predicted FAIL | needs paper-grade write-up |
| 11 | Anaesthetic Detuning of σ-Paired Dipole Mode (Note G) | 9 | Exploratory probe; volatile ρ=+0.94, sevo-vs-propofol R_phase differential pre-registered | exploratory-draft |

**Programme totals:** 196 pages, 11 papers, 2.9+ MB.

---

## Per-paper refinement status

### 01 — Existence as Closure (foundation)
- **Status:** refinement-ready
- **Strengths:**
  - Formal foundation with theorems and proofs
  - Sim suite (D1–D8) with cross-paper sim references
  - Programme map appendix
  - Hostile-critique response section (§15)
  - Applicability diagnostic cited
  - Frozen prediction list F1–F10
- **Open refinement items:**
  - [ ] Update programme map to reflect all 10 papers (currently lists 4 + Solution Lab references)
  - [ ] Tighten §6 cascade rung tower (dense math; consider moving derivations to appendix)
  - [ ] Final consistency pass on terminology
- **Estimated effort to releasable:** ~2-4 hours

### 02 — Life as Closure (human bridge)
- **Status:** refinement-ready
- **Strengths:**
  - 18 mechanical objects with formal definitions
  - 13 sim demos (L1–L13)
  - Two real-data empirical anchors (SL-002 + SL-005)
  - Frozen prediction list P1–P15
  - "What would falsify this paper" single-sentence section
  - Limitations section
  - Empirical anchor table, glossary, worked example (appendices A, B, C)
- **Open refinement items:**
  - [ ] Address the "comprehensive" risk: consider further tightening the abstract / reader's map
  - [ ] Ensure all citations to SL-005, SL-007 reflect real-data results consistently
  - [ ] Cross-check that the applicability diagnostic story is consistently told
- **Estimated effort to releasable:** ~2-4 hours

### 03 — From Processing to Point of View (neuroscience)
- **Status:** refinement-ready
- **Strengths:**
  - Compact (18 pp), focused
  - Levin bridge with explicit $R_{\mathrm{cl}}$ 5-term formula
  - CEMI bridge with explicit $R_{\mathrm{phase}}$ 6-term formula
  - Solution Lab 002 anchor with LOSO d_z=2.07 refinement
  - 3 sim demos (B1–B3)
- **Open refinement items:**
  - [ ] Add explicit cite to Solution Lab 005 trait-anxiety result for the anaesthesia/dyscoherence link
  - [ ] Tighten cross-paper references
- **Estimated effort to releasable:** ~1-2 hours

### 04 — Cosmic Self-Pruning and Frame Recurrence (held back)
- **Status:** refinement-ready but held back from v1.0 release
- **Strengths:**
  - Structural mechanisms cleanly stated
  - 5 sim demos (C1–C5)
  - Unified hierarchy across cascade rungs
- **Open refinement items:**
  - [ ] Maintain held-back status for v1.0; refinement deferred
  - [ ] When ready: tighten the universe-as-frame-at-totality framing
  - [ ] Strengthen conditional-proposition discipline throughout
- **Estimated effort to releasable:** ~3-5 hours when activated

### 05 — Bioelectric Closure (SL-001)
- **Status:** release-ready (peer-review-style note)
- **Strengths:**
  - BETSE 6-condition planarian panel (N=5×6=30)
  - Default-weight 5-term R_cl residual
  - Survives sham-calibration null, replicates across depolarisers
  - Leave-one-out + leave-condition-out cross-validation
  - 5 preregistered wet-lab predictions (DiBAC4(3))
- **Open refinement items:**
  - [ ] Wet-lab partnership outreach (not paper-content; programme work)
- **Estimated effort to releasable:** ready

### 06 — Cortical Phase Closure (SL-002)
- **Status:** release-ready (16-page peer-review-style note)
- **Strengths:**
  - OpenNeuro ds005620 propofol n=14: 14/14, t=7.11, p<2e-4
  - sLORETA source-localised: 14/14, t=9.72
  - Cross-cohort ds004541: 7/7, t=5.25
  - LOSO refinement: d_z=2.07, 2-feature minimal subset
- **Open refinement items:**
  - [ ] Cross-cite the LOSO refinement consistently with the cross-substrate paper (07)
- **Estimated effort to releasable:** ready

### 07 — Closure-as-Distance (cross-substrate methodology)
- **Status:** release-ready (hostile-review-ready, CAD-D1–D5-v1)
- **Strengths:**
  - 5-criterion applicability diagnostic
  - 14/15 substrates correctly classified
  - 8/8 paired-design + 3/3 negative controls + 3/4 post-draft real-data
  - First-order proxy framing (not full operator)
  - Pre-registered external tests
- **Open refinement items:**
  - [ ] FTD false positive — characterised; recalibration cohort identification is open programme work
- **Estimated effort to releasable:** ready

### 08 — Trauma Cortical Closure (SL-005)
- **Status:** **first real-data result; needs paper-grade write-up to release**
- **Strengths:**
  - First real-data application of cross-substrate methodology to chronic-clinical-state cohort
  - OpenNeuro ds007609 trait anxiety: Cohen's d = +0.79
  - Applicability diagnostic predicted PASS a priori
  - Default SL-002 weights used verbatim (cross-application validation)
- **Open refinement items:**
  - [ ] Expand the 9-page note to a full peer-review-style write-up
  - [ ] Add methodology section detailing the STAI-based grouping logic
  - [ ] Discuss the gap between trait-anxiety proxy and full PTSD-cohort EEG
  - [ ] Add limitations section
  - [ ] Per-subject within-subject variance discussion
  - [ ] Power analysis for the n=24 cohort
- **Estimated effort to releasable:** ~6-10 hours

### 09 — Flow Cortical Closure (SL-006)
- **Status:** hostile-review-ready (FlowIndex-v1)
- **Strengths:**
  - Synthetic-data 5/5 PASS preregistered tests
  - Discriminant pre-test: no single component reproduces the composite
  - ds005520 MOBA-gaming real-data analysis in progress
- **Open refinement items:**
  - [ ] Complete ds005520 real-data analysis; append to paper as addendum
  - [ ] Music-performance, esports cohorts as further validation
  - [ ] ESM time-dilation correlate (H4)
- **Estimated effort to releasable:** ~3-6 hours pending ds005520 result

### 10 — Hyperscanning Joint Meaning (SL-007)
- **Status:** **honest-negative + methodology-validated; needs paper-grade write-up**
- **Strengths:**
  - Real-data on OpenNeuro ds007471 musical joint-action (32 pairs, 64-channel)
  - Honest negative: d_z = +0.23, p=0.43
  - Applicability diagnostic correctly predicted FAIL a priori (D2=0, D3=0.62)
  - Methodology-validation result (negative as predicted)
- **Open refinement items:**
  - [ ] Expand the 8-page note to a full peer-review-style write-up
  - [ ] Frame the honest negative as a methodology-validation success
  - [ ] Identify candidate genuine-dialogue dataset for follow-on
  - [ ] Discuss why musical-joint-action fails the multi-channel integrative criteria
- **Estimated effort to releasable:** ~6-10 hours

---

## Refinement priorities

**Tier 1 — Immediate (gets to clean v1.0):**

1. **02 — Life as Closure** finishing pass (~2-4h)
2. **01 — Existence as Closure** finishing pass (~2-4h)
3. **03 — Processing to Point of View** finishing pass (~1-2h)

**Tier 2 — Brings the empirical wing to release standard:**

4. **08 — SL-005 Trauma** paper-grade write-up (~6-10h)
5. **10 — SL-007 Hyperscanning** paper-grade write-up (~6-10h)
6. **09 — SL-006 Flow** ds005520 addendum (~3-6h)

**Tier 3 — Activation:**

7. **04 — Cosmic** activation when programme moves to v1.1 (~3-5h)

---

## Cross-paper consistency checks

These need to be applied consistently across all 10 papers:

- [ ] Bib key `SmartClosureDistance` references the cross-substrate paper (07)
- [ ] Bib keys `SolutionLab001`, `SolutionLab002`, `SolutionLab005`, `SolutionLab006`, `SolutionLab007` reference papers 05, 06, 08, 09, 10
- [ ] Bib keys `SmartExistenceClosure`, `SmartLifeAsClosure`, `SmartProcessingToPOV`, `SmartCosmicClosure` reference papers 01, 02, 03, 04
- [ ] All "Conditional Proposition" usage is consistent (no "Conditional Theorem")
- [ ] All papers cite the applicability diagnostic from 07 where relevant
- [ ] All papers use the framework's central terminology consistently (closure operator $C_\varphi$, σ-twist $\tau$, per-frame zero-line $\Sigma_\Ical$, etc.)

## Build instructions

From any paper directory:
```bash
cd release-bundles/existence-programme/papers/<NN>-<slug>/
tectonic main.tex
```

To build all:
```bash
cd release-bundles/existence-programme
for d in papers/*/; do
  (cd "$d" && tectonic main.tex 2>&1 | tail -2)
done
```

## Sync workflow

This workspace is downstream of the source-of-truth locations. Until
the sync scripts are built, refinement edits made here should be
manually copied back to:

| Workspace paper | Source location |
|---|---|
| 01–04 | `papers/<slug>/main.tex` in `vfd-crystalisation-paper` |
| 05 | `experiments/001-vfd-bioelectric-closure/paper/paper.tex` in `solution-lab` |
| 06 | `experiments/002-vfd-cortical-phase-closure/paper/paper.tex` |
| 07 | `experiments/closure_cross_substrate/paper/main.tex` |
| 08 | `experiments/005-vfd-trauma-cortical-closure/paper/main.tex` |
| 09 | `experiments/006-vfd-flow-cortical-closure/paper/main.tex` |
| 10 | `experiments/007-vfd-hyperscanning-joint-meaning/paper/main.tex` |

**Recommended workflow going forward:** treat THIS workspace as the
authoritative source. Mark the original locations as mirrors and pull
from workspace via the sync script when ready to release back.

---

*Last refreshed: 2026-05-22*
*Maintainer: Lee Smart (VFD/ARIA Research)*

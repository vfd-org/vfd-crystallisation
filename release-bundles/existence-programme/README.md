# The Existence Programme — Unified Refinement Workspace

A ten-paper coordinated body of work on **existence as recursive geometric
closure** on the 600-cell substrate $V_{600}$, with operator-level
bridges to life, neuroscience, cosmology — and a wing of empirical
Solution Lab experiments grounding the bridges on independently-collected
biological-simulation, EEG, and hyperscanning data.

> **Closure → Living meaning → Point of view → Cosmic recurrence → Empirical realisation.**

This directory is the **authoritative refinement workspace** for all ten papers.
Source files for each paper live in `papers/NN-slug/`. The originals in
`vfd-crystalisation-paper/papers/` and `solution-lab/experiments/`
are mirrors; the workspace stays in sync via `scripts/sync_from_sources.sh`
and `scripts/sync_to_sources.sh`.

## The ten papers

### Existence-programme flagship pair + companions

| # | Title | Pages | Role |
|--|---|--:|---|
| 01 | [Existence as Closure](papers/01-existence-as-closure/main.pdf) | 31 | **Foundation** (flagship pair) |
| 02 | [Life as Closure](papers/02-life-as-closure/main.pdf) | 41 | **Human bridge** (flagship pair) |
| 03 | [From Processing to Point of View](papers/03-processing-to-point-of-view/main.pdf) | 18 | Neuroscience companion |
| 04 | [Cosmic Self-Pruning and Frame Recurrence](papers/04-cosmic-closure-recurrence/main.pdf) | 17 | Cosmology companion (held back from v1.0) |

### Empirical wing (Solution Lab experiments + cross-substrate methodology)

| # | Title | Pages | Status |
|--|---|--:|---|
| 05 | [Bioelectric Closure (SL-001)](papers/05-bioelectric-closure/main.pdf) | 20 | Release-ready; BETSE planarian + 5 preregistered wet-lab predictions |
| 06 | [Cortical Phase Closure (SL-002)](papers/06-cortical-phase-closure/main.pdf) | 17 | Release-ready; 14/14 propofol, sLORETA + cross-cohort replications |
| 07 | [Closure-as-Distance (cross-substrate)](papers/07-closure-cross-substrate/main.pdf) | 17 | Release-ready; **applicability diagnostic CAD-D1–D5-v1**, 14/15 substrates correctly classified |
| 08 | [Trauma Cortical Closure (SL-005)](papers/08-trauma-cortical-closure/main.pdf) | 9 | **First real-data result**: trait anxiety d=+0.79 (ds007609), needs paper-grade write-up |
| 09 | [Flow Cortical Closure (SL-006)](papers/09-flow-cortical-closure/main.pdf) | 9 | Hostile-review-ready FlowIndex-v1; ds005520 in progress |
| 10 | [Hyperscanning Joint Meaning (SL-007)](papers/10-hyperscanning-joint-meaning/main.pdf) | 8 | **Honest negative on ds007471**, applicability diagnostic correctly predicted FAIL |

### Exploratory addendum (Note G, 2026-05-24)

| # | Title | Pages | Status |
|--|---|--:|---|
| 11 | [Anaesthetic Detuning of the σ-Paired Closure Dipole Mode](papers/11-tubulin-dipole-closure/main.pdf) | ~9 | **Exploratory probe** (Note G); volatile Spearman ρ=+0.94, pre-registered sevoflurane-vs-propofol R_phase differential under H-MT-Bridge |

**Total: 196 pages across 11 papers.**

## Workspace structure

```
release-bundles/existence-programme/
├── REFINEMENT_STATUS.md          # per-paper refinement checklist
├── README.md                     # this file
├── LICENSE                       # CC BY-NC 4.0 (prose), Apache-2.0 (code)
├── CITATION.cff                  # programme citation metadata
├── papers/
│   ├── 01-existence-as-closure/{main.tex, main.pdf, references.bib, figures/, repro/}
│   ├── 02-life-as-closure/
│   ├── 03-processing-to-point-of-view/
│   ├── 04-cosmic-closure-recurrence/
│   ├── 05-bioelectric-closure/
│   ├── 06-cortical-phase-closure/
│   ├── 07-closure-cross-substrate/
│   ├── 08-trauma-cortical-closure/
│   ├── 09-flow-cortical-closure/
│   └── 10-hyperscanning-joint-meaning/
├── scripts/
│   ├── build_all_papers.sh       # compile all 10 with tectonic
│   ├── run_all_sims.sh           # run all 28 sim demos at seed 42
│   ├── sync_from_sources.sh      # pull latest from source-of-truth
│   └── sync_to_sources.sh        # push workspace edits back
└── sims/
    ├── existence-as-recursive-closure/closure_demo.py   # D1-D8
    ├── life-as-closure/life_demo.py                      # L1-L13
    ├── cosmic-closure-recurrence/cosmic_demo.py         # C1-C5
    └── processing-to-point-of-view/bridges_demo.py      # B1-B3
```

## Build everything

```bash
# Compile all 10 papers (needs tectonic)
./scripts/build_all_papers.sh

# Check status without recompiling
./scripts/build_all_papers.sh --check

# Compile one paper
./scripts/build_all_papers.sh --paper 02-life

# Run all 28 sim demos (D1-D8 + L1-L13 + C1-C5 + B1-B3)
./scripts/run_all_sims.sh
```

## Refine a paper

```bash
cd papers/02-life-as-closure/
$EDITOR main.tex
tectonic main.tex             # rebuild

# When ready, push back to source-of-truth
cd ../..
./scripts/sync_to_sources.sh --paper 02-life-as-closure
```

## Refinement priorities

See [REFINEMENT_STATUS.md](REFINEMENT_STATUS.md) for the per-paper
status checklist. Tier 1 — Tier 3 estimates total ~25-45 hours of
focused work to bring all 10 papers to v1.0 release standard.

**Tier 1 (immediate, ~5-10h):** Refine flagship pair + Processing
companion (01, 02, 03).

**Tier 2 (empirical wing to release standard, ~15-26h):** Paper-grade
write-ups for the first-result and honest-negative papers (08, 10),
plus completing the in-progress real-data analysis for flow (09).

**Tier 3 (programme expansion, ~3-5h):** Activate Cosmic paper (04)
when programme moves to v1.1.

## Programme empirical record

The structural framework rests on real, independently-collected data:

| Substrate | Source | Result | Predicted by diagnostic? |
|---|---|---|---|
| BETSE planarian regeneration | Solution Lab 001 | Default-weight 5-term R_cl distinguishes 6 chemistries, sham null, LOO+LCO cross-val | PASS, observed PASS |
| OpenNeuro ds005620 propofol n=14 | Solution Lab 002 | 14/14 positive, t=7.11, p<2e-4 | PASS, observed PASS |
| sLORETA source-localised n=14 | Solution Lab 002 | 14/14, t=9.72, d_z=2.60 | PASS, observed PASS |
| OpenNeuro ds004541 clinical anaesthesia n=7 | Solution Lab 002 | 7/7, t=5.25 | PASS, observed PASS |
| Source-localised LOSO n=14 | Solution Lab Closure-Distance | d_z=2.07, Jaccard=1.00, 2-feature minimal | PASS, observed PASS |
| **OpenNeuro ds007609 trait anxiety n=24** | **Solution Lab 005** | **Cohen's d=+0.79** | **PASS predicted, PASS observed** |
| **OpenNeuro ds007471 musical hyperscanning** | **Solution Lab 007** | **Honest negative d_z=+0.23** | **FAIL predicted, FAIL observed** |
| Alzheimer's disease ds004504 | SL-ClosureDistance | d=-0.31 | FAIL predicted, FAIL observed |
| Frontotemporal dementia ds004504 | SL-ClosureDistance | d=+0.02 | PASS predicted, FAIL observed (transparently-characterised false positive) |
| Cardiac AF MIT-BIH | SL-ClosureDistance | Single-axis dominates | FAIL predicted, FAIL observed |
| Climate regime shifts | SL-ClosureDistance | Single-axis dominates | FAIL predicted, FAIL observed |
| Kuramoto coupled oscillators | SL-ClosureDistance | Single-mechanism | FAIL predicted, FAIL observed |
| RNN training | SL-ClosureDistance | Single-mechanism | FAIL predicted, FAIL observed |
| Gaussian noise (negative control) | SL-ClosureDistance | No shift | FAIL predicted, FAIL observed |
| Structured-noise no-shift (control) | SL-ClosureDistance | No shift | FAIL predicted, FAIL observed |
| Single-axis trivial shift (control) | SL-ClosureDistance | Single-axis | FAIL predicted, FAIL observed |

**Diagnostic accuracy: 14 of 15 substrates correctly classified.** The
framework has self-aware scope: it predicts a priori where the closure
methodology applies and where it doesn't.

## Conditional hypotheses

The structural propositions hold whether or not any of these
hypotheses are true. The conditional bridges to neuroscience, life,
cosmology, and phenomenology depend on the named hypotheses where used:

| Hypothesis | Used in | Status |
|---|---|---|
| P-A (Access Principle) | All four structural papers | Open conjecture (hard problem) |
| H-RP-1 (rung–cortical) | Processing, Life | Open |
| H-RP-2 (predictive-coding) | Processing, Life | Open |
| H-RP-3 (bio-substrate) | Processing, Life | Open |
| H-rec (recurrence admissibility) | Cosmic | Open |
| H-evolve (time-dependent C) | Cosmic | Open |

## Conditional propositions: applicability diagnostic

Beyond the named hypotheses, **the operator-level empirical bridges are
scoped by CAD-D1–D5-v1** (Closure-Applicability Diagnostic, version 1).
A substrate must satisfy:

- $D_1$ anisotropy: top-PC variance fraction ≤ 0.70
- $D_2$ multi-feature consistency: ≥ 2 features with ≥ 80% subject sign agreement
- $D_3$ subject-level coherence: ≥ 0.65 per-subject modal-direction fraction
- $D_4$ mechanism complementarity: participation ratio ≥ 1.5
- $D_5$ feature minimality: FDR-passing fraction ≤ 0.50

If a substrate fails the diagnostic, closure-as-distance is not
expected to dominate single-axis baselines. This is the framework's
self-aware applicability boundary.

## Status of each paper

See [REFINEMENT_STATUS.md](REFINEMENT_STATUS.md) for the detailed
per-paper checklist. Summary:

- **3 release-ready solution-lab papers**: SL-001 (Bioelectric), SL-002 (Cortical Phase), SL-Closure-Distance (cross-substrate methodology)
- **3 structural papers in refinement**: Existence, Life, Processing
- **1 cosmic structural paper held back** from v1.0
- **1 first-result paper needing write-up**: SL-005 trauma (d=+0.79)
- **1 hostile-review-ready paper with in-progress real-data**: SL-006 flow (ds005520 in progress)
- **1 honest-negative paper needing write-up**: SL-007 hyperscanning (methodology-validated)

## Reading paths

- **Mathematical reader:** 01 Existence → 04 Cosmic → 02 Life → 03 Processing
- **Consciousness reader:** 02 Life → 03 Processing → 06 SL-002 → 01 Existence
- **Empirical reader:** 06 SL-002 → 07 SL-Closure-Distance → 08 SL-005 → 10 SL-007 → 02 Life
- **New reader:** 02 Life as Closure first (human-facing), then 01 Existence for foundations
- **Methodologist:** 07 SL-Closure-Distance first (the applicability diagnostic)
- **Clinician / experimentalist:** 06 SL-002 → 08 SL-005 → preregistered tests

## Licence

- Code: Apache-2.0
- Prose, figures, papers: CC BY-NC 4.0 (non-commercial commons-of-knowledge)
- Source-available, **not** OSI open source

## Citation

See [CITATION.cff](CITATION.cff). Programme citation:

> Smart, L. (2026). The Existence Programme: ten papers on existence as
> recursive geometric closure with empirical applicability diagnostic.
> *VFD/ARIA Research.* https://github.com/vfd-org/existence-programme

---

*Last refreshed: 2026-05-22*
*Maintainer: Lee Smart (VFD/ARIA Research)*
*Contact: contact@vibrationalfielddynamics.org*

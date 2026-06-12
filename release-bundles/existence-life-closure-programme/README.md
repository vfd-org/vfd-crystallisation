# Existence / Life / Closure Programme

> A reproducible pre-peer-review packet for closure as a structural condition of existence, living systems, and candidate point-of-view formation.

[![Status](https://img.shields.io/badge/status-pre--peer--review-blue)](#status)
[![Version](https://img.shields.io/badge/version-1.0.0--rc1-blue)](CHANGELOG.md)
[![Licence](https://img.shields.io/badge/code-Apache--2.0-green)](LICENSE)
[![Prose](https://img.shields.io/badge/prose-CC%20BY%204.0-green)](LICENSE)

---

## Quick navigation

| If you want to | Go to |
|---|---|
| Understand the programme in one page | [`00-review-packet-overview.md`](00-review-packet-overview.md) |
| See how to falsify the claims | [`01-falsifiers-and-roadmap.md`](01-falsifiers-and-roadmap.md) |
| Start reviewing | [`review/reviewer_start_here.md`](review/reviewer_start_here.md) |
| Read the papers in order | [`review/packet_order.md`](review/packet_order.md) |
| Understand status labels | [`review/status_taxonomy.md`](review/status_taxonomy.md) |
| Find every known limitation | [`review/known_limitations.md`](review/known_limitations.md) |
| Find every non-claim | [`review/non_claims.md`](review/non_claims.md) |
| Reproduce results | [`repro/shared/run_all_smoke_tests.py`](repro/shared/run_all_smoke_tests.py) |
| Find data sources | [`repro/shared/data_access.md`](repro/shared/data_access.md) |

---

## Programme summary

This repository contains the **pre-peer-review Existence / Life / Closure
Programme**: a formal and empirical research packet developing closure as a
structural condition for existence, living systems, and candidate
point-of-view formation. It separates formal theorems, conditional
propositions, empirical proxies, completed empirical results, and
pre-registered future tests.

**Core arc:** closure → bounded reference frames → living-frame mechanics
→ measurable closure-distance proxies → cortical empirical anchor →
conditional consciousness application.

---

## Papers and notes

### Primary review packet (recommended reading order)

| # | Title | Pages | Folder |
|--:|---|--:|---|
| **I** | Existence as Closure | 35 | [`papers/I-existence-as-closure/`](papers/I-existence-as-closure/) |
| **II** | Life as Closure | 44 | [`papers/II-life-as-closure/`](papers/II-life-as-closure/) |
| **C** | Closure-as-Distance (methodology) | 18 | [`notes/Note-C-closure-as-distance/`](notes/Note-C-closure-as-distance/) |
| **B** | Cortical Phase Closure (empirical anchor) | 17 | [`notes/Note-B-cortical-phase-closure/`](notes/Note-B-cortical-phase-closure/) |
| **III** | From Processing to Point of View | 19 | [`papers/III-processing-to-point-of-view/`](papers/III-processing-to-point-of-view/) |

### Empirical appendix notes

| # | Title | Pages | Folder |
|--:|---|--:|---|
| **A** | Bioelectric Closure | 20 | [`notes/Note-A-bioelectric-closure/`](notes/Note-A-bioelectric-closure/) |
| **D** | Trauma / Cortical Closure | 10 | [`notes/Note-D-trauma-cortical-closure/`](notes/Note-D-trauma-cortical-closure/) |
| **E** | FlowIndex | 9 | [`notes/Note-E-flow-cortical-closure/`](notes/Note-E-flow-cortical-closure/) |
| **F** | Dyadic Joint Meaning | 8 | [`notes/Note-F-hyperscanning-joint-meaning/`](notes/Note-F-hyperscanning-joint-meaning/) |

---

## Key claim boundaries

The programme explicitly does **not** claim any of the following:

- That consciousness is proven.
- That empirical proxies directly measure the formal closure operator.
- That suffering reduces to a number.
- That cosmic / speculative extensions are required for the primary results.
- That the Access Principle (P-A) is established (it is named as a conjectural hypothesis).

Empirical proxies (`closure-as-distance`, `R_cl`, `R_phase`, `δ̂_AB^EEG`,
`FlowIndex`, `CCR`) are first-order measurement proxies, licensed only
under the **CAD-D1–D5-v1 applicability diagnostic** of Note C. See
[`review/non_claims.md`](review/non_claims.md) for the full non-claim list.

---

## Reproduce

### Quick check (~30 s)

```bash
git clone https://github.com/vfd-org/existence-life-closure-programme.git
cd existence-life-closure-programme
python -m venv .venv
source .venv/bin/activate            # macOS/Linux
# .venv\Scripts\activate             # Windows
pip install -r repro/shared/requirements.txt
python repro/shared/run_all_smoke_tests.py --quick
```

Runs the lightweight rung-tower + CAD strict-vs-PASS-leaning audit (3/3
deterministic, seed 42). Verifies the structural facts without the
chart-heavy full-paper demos.

### Full check (3–25 min)

```bash
python repro/shared/run_all_smoke_tests.py
```

Runs Paper I D1–D8 substrate facts, Paper II L1–L13 living-frame mechanics,
Paper III B1–B3 consciousness bridges, plus the quick set. Native Linux:
~3–5 min total. WSL + Windows-mounted filesystem (OneDrive): expect
10–25 min due to matplotlib chart-generation I/O.

### Real-data analyses

External-data analyses (OpenNeuro EEG cohorts, BETSE planarian simulations,
HCP cortex) require dataset download. See
[`repro/shared/data_access.md`](repro/shared/data_access.md) — every empirical
claim has a dataset + script + expected-result mapping.

---

## Status taxonomy

Used in every paper and note:

| Status | What it means |
|---|---|
| **Theorem / Definition** | Formal structural claim under stated assumptions. |
| **Conditional Proposition** | Bridge claim conditional on a named hypothesis (H-RP, P-A, substrate mapping, empirical interpretation). |
| **Empirical Result** | Completed data analysis with stated effect size + significance. |
| **Empirical Proxy** | Measurable first-order approximation, not the formal operator. |
| **Pre-registered Proposal** | Future test, not evidence. |

---

## Two τ conventions

Used in Paper I and downstream. Both are involutions and commute with
`C_φ`; dimension-specific claims state which `τ` is used.

| Convention | Definition | dim Fix(τ) | Used in |
|---|---|--:|---|
| **τ_ico** | Icosian Galois action `√5 ↦ -√5` on `ℤ[φ]`-coordinates | **94** | Theorem statements |
| **τ_spec** | Spectral negation of the `+6φ` dipole eigenspace of `A_{V_600}` | **116** | Sim demos |

The icosian-to-spectral basis-change residual on the 96 Type-C vertices
is honestly disclosed in Paper I demo D8 and in
[`review/known_limitations.md`](review/known_limitations.md).

---

## Repository structure

```
existence-life-closure-programme/
├── README.md                          ← this file
├── LICENSE                            ← Apache-2.0 (code) + CC BY 4.0 (prose)
├── CITATION.cff                       ← citation metadata
├── CONTRIBUTING.md                    ← contribution guidelines
├── REVIEW_PACKET.md                   ← reviewer quick reference
├── 00-review-packet-overview.md       ← one-page overview
├── 01-falsifiers-and-roadmap.md       ← what would weaken / falsify each claim
├── CHANGELOG.md                       ← version history
├── RELEASE_CHECKLIST.md               ← release acceptance criteria
├── papers/
│   ├── I-existence-as-closure/        ← paper.pdf + source/ + figures/ + repro/ + README
│   ├── II-life-as-closure/
│   └── III-processing-to-point-of-view/
├── notes/
│   ├── Note-A-bioelectric-closure/
│   ├── Note-B-cortical-phase-closure/
│   ├── Note-C-closure-as-distance/
│   ├── Note-D-trauma-cortical-closure/
│   ├── Note-E-flow-cortical-closure/
│   └── Note-F-hyperscanning-joint-meaning/
├── repro/
│   ├── shared/                        ← requirements, smoke tests, data-access guide, seeds, hashes
│   └── outputs/                       ← deterministic JSON outputs + hash manifest
├── review/                            ← reviewer-facing documents
│   ├── reviewer_start_here.md
│   ├── packet_order.md
│   ├── status_taxonomy.md
│   ├── non_claims.md
│   └── known_limitations.md
└── extensions_withheld/               ← speculative material kept out of primary packet
```

---

## Falsifier catalogue

Every claim has an explicit falsifier. See
[`01-falsifiers-and-roadmap.md`](01-falsifiers-and-roadmap.md) for the full
catalogue. Highlights:

- **Formal**: `dim Fix(τ_ico) ≠ 94`, or `C_φ` does not preserve `Fix(τ)`, falsifies Paper I.
- **Measurement**: 3+ strict-CAD-PASS substrates with closure LOSO `d_z < 1.0` falsify the diagnostic's predictive licence.
- **Clinical**: PTSD therapy responders without measurable CCR reduction falsify the trauma-as-chronic-dyscoherence identification.
- **Joint**: Conversational hyperscanning with CAD-PASS but no `δ̂_AB^EEG` discrimination falsifies the joint-meaning proxy.

---

## How to cite

See [`CITATION.cff`](CITATION.cff). Suggested citation:

```
Smart, L. (2026). Existence / Life / Closure Programme:
A bounded-reference-frame approach to existence, living systems, and
measurable integrative organisation. Pre-peer-review research packet,
Institute of Vibrational Field Dynamics.
https://github.com/vfd-org/existence-life-closure-programme
```

---

## Licence

| Content | Licence |
|---|---|
| Code (Python, scripts, manifests) | **Apache-2.0** |
| Prose, figures, papers | **CC BY 4.0** |
| External datasets | original dataset licences (see [`repro/shared/data_access.md`](repro/shared/data_access.md)) |

External datasets are not redistributed in this repository.

---

## Contact

- **Repository**: https://github.com/vfd-org/existence-life-closure-programme
- **Email**: contact@vibrationalfielddynamics.org
- **Empirical wing** (separate repo): https://github.com/vfd-org/solution-lab

---

## Status

**Version**: 1.0.0-rc1 (pre-peer-review)
**Released**: 2026-05-22
**Hardening**: 5 rounds of codex (gpt-5.x) review iteration; single-author; no independent peer review yet.
**Smoke tests**: 6/6 pass (3/3 in quick mode) at seed 42.
**Build**: all 9 included papers compile cleanly via tectonic with 0 broken refs.

For reviewers: see [`review/reviewer_start_here.md`](review/reviewer_start_here.md).
For contributors: see [`CONTRIBUTING.md`](CONTRIBUTING.md).
For honest disclosure: see [`review/known_limitations.md`](review/known_limitations.md) and [`review/non_claims.md`](review/non_claims.md).

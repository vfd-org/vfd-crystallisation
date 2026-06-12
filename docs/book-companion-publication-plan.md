# Book Companion Publication Plan

**Date:** 2026-06-12
**Goal:** every load-bearing claim in *The Crystal and the Clock* is backed by a standalone, hostile-critique-hardened paper in this repository, each with runnable verification code, so the book can cite a public git record rather than private notes. Papers are standalone (readable without the book) but ordered along the book's narrative.

## 1. The paper set

### New papers (drafted in this pass)

| Paper | Title (working) | Book chapters | Derivation source | Verification |
|---|---|---|---|---|
| **LIV** | The Forced Crystal: the Binary Icosahedral Group as the Unique Perfect Quaternionic Substrate | Ch 3, Ch 4 | `docs/why-this-crystal.md` | `verify_crystal_forcing.py` CF0–CF6, GE0–GE3 (17/17) |
| **LV** | The Rendering Layer: Spectral Dimension, Canonical Kernel, Observer Chart, and Second-Order Time | Ch 4–7 | `docs/rendering-layer.md` | `verify_rendering_layer.py` (21/21) |
| **LVI** | The Gauge-Group Inventory from the Two Arenas | Ch 9 | `docs/gauge-group-from-arenas.md` | `verify_residual_closure.py` SM0–SM6; `verify_crystal_forcing.py` YM1–YM2 |
| **LVII** | Residual Closure of the Gravity Chain: In-House Bootstrap, Non-Gaussian Effective Action, Explicit-Rate Continuum Control, and a Conditional Newton's Constant | Ch 9, Ch 12 | `docs/residual-closure-derivation.md` | `verify_residual_closure.py` RB/RG/RC/RGRAV (24/24) |

### Already-published-in-tree papers the book leans on (updated earlier in this campaign)

| Paper | Status |
|---|---|
| **LIII** Einstein's Equations from Substrate Closure | drafted + residual-upgrade ledger added; 12 pp, compiles clean |
| **XL** Continuum Targets ($D_4$/GR limit) | positioning update added (T1–T2 = the (R-GH) residual) |
| **LII** Muon $g{-}2$ | unchanged; supplies the shell-96 prior for LVII's conditional $G$ |
| XXIV, XXVII, XVIII | event-order kinematics, graph Poisson, Nelson pairing — unchanged |

### Consolidated reference documents (book back matter sources)

- `docs/claim-status-ledger.md` — graded claim table (Ch 8 table, Ch 12 list).
- `docs/verification-manifest.md` — verification appendix (commands, 205 checks).
- `docs/book-companion-map.md` — chapter → paper → doc → sim map (written at the end of this pass).

## 2. Hardening protocol (per paper)

1. Draft from the verified derivation doc; every theorem keeps its sim pointer.
2. Compile clean (pdflatex + bibtex, zero undefined refs).
3. **Codex hostile review** via `scripts/review_paper.sh papers/paper-NN/paper-NN.tex` (review lands in `docs/reviews/`).
4. Triage findings: every must-fix answered **by derivation or by a named, honest gap** — never by silently weakening a claim (the no-retreat discipline). New math needed → derive it and add a sim.
5. Re-review until the review returns no must-fix items, or the remaining items are documented as named opens in the paper itself.
6. Re-run the paper's sim suite; commit paper + review + any new sims together.

## 3. File inventory (for announcements)

### Created in this campaign (2026-06-11 → this pass)

**Papers:** `papers/paper-liii/` (tex+bib+pdf), `papers/paper-liv/`, `papers/paper-lv/`, `papers/paper-lvi/`, `papers/paper-lvii/` (each tex+bib+pdf).

**Derivation docs:** `docs/gr-closure-derivation.md`, `docs/residual-closure-derivation.md`, `docs/gauge-group-from-arenas.md`, `docs/why-this-crystal.md`, `docs/claim-status-ledger.md`, `docs/verification-manifest.md`, `docs/book-companion-publication-plan.md` (this file), `docs/book-companion-map.md`.

**Verification suites:** `scripts/verify_gr_closure.py` (39), `scripts/verify_residual_closure.py` (24), `scripts/verify_crystal_forcing.py` (17) — joining the existing `verify_rendering_layer.py` (21), `verify_rung_dimension_ladder.py` (25), `verify_ladder_completion.py` (29), `verify_narrative_closure.py` (28), `verify_gap_strengthening.py` (22). **Total: 205 checks.**

**Figures:** `scripts/generate_book_figures_v2.py` → `book/figures/ch04-multiplicities`, `ch06-kernel-decay`, `ch08-mass-shells`, `ch09-dispersion`, `ch09-light-bending` (pdf+png each).

**Reviews:** `docs/reviews/paper-l{iv,v,vi,vii}-*.md` (produced by the hardening cycles of this pass).

### Updated

`papers/paper-xl/paper-xl.tex` (positioning), `docs/kappa-derivation-math.md` (closure banners), `docs/narrative-gap-closure.md` (G8 closed), book chapters 9/11/12/13 + appendix + OUTLINE, book builds (PDF/EPUB/HTML).

## 4. Announcement units (each standalone)

1. **The gravity chain is closed** — Paper LIII + LVII; Einstein's equations from the substrate, residuals upgraded, 62 checks.
2. **The crystal is forced** — Paper LIV; unique perfect group, McKay = E8 from the multiplication table, the graph that knows its own shape.
3. **The rendering layer** — Paper LV; dimension three from the spectrum, the canonical kernel, wave-time from the inner mirror.
4. **The gauge inventory** — Paper LVI; SU(3) × SU(2) with the distinguished clock circle from the two arenas' number systems — all three SM factor types, with the independent-hypercharge wiring stated plainly as open.
5. **The verification record** — the manifest: 205 checks, one data file, runnable by anyone.

## 5. Honesty gates (apply to every announcement)

- Structure vs wiring: LVI derives the group *inventory*, not charges/chirality/couplings.
- Conditional means conditional: LVII's $G$ rests on H-shell-96, stated in the abstract, with the look-elsewhere statistic.
- Effective vs rigorous: the gravity chain is physics-grade (sound-from-atoms); (R-GH) stays open and named.
- The failed construction (kappa §6.7) stays in the record.

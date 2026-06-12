# Book Companion Map: Chapter → Paper → Derivation → Verification

**Date:** 2026-06-12
**Purpose:** the routing table between *The Crystal and the Clock* and its standalone supporting record. Each row is independently publishable; together they cover every load-bearing claim in the book. Verification commands and expected pass counts: `docs/verification-manifest.md`. Claim grades: `docs/claim-status-ledger.md`.

| Book chapter | Claim carried | Paper | Derivation doc | Verification (items) |
|---|---|---|---|---|
| Ch 1–2 (view from inside; existence as closure) | framing; closure ladder | existence-programme papers (`papers/existence-as-recursive-closure/` et al.) | `docs/existence-as-closure.md` | existence-programme demos |
| **Ch 3** (the most symmetric thing) | the crystal is forced; vertex set = group; E8 internal | **Paper LIV** | `docs/why-this-crystal.md` | `verify_crystal_forcing.py` CF0–CF6 |
| **Ch 4** (what the spectrum knows) | dimension 3 from spectrum; graph knows its shape | **Paper LV** §2; **LIV** §4 | `docs/rendering-layer.md` §2 | `verify_rendering_layer.py` R1a–f; `verify_crystal_forcing.py` GE0–GE3 |
| **Ch 5** (three directions for free) | canonical 3-frame, no choice | **Paper LV** §4 | `docs/rendering-layer.md` §4.1 | R3a |
| **Ch 6** (looking) | canonical kernel; locality; scene | **Paper LV** §3–4 | `docs/rendering-layer.md` §3–4 | R2a–f, R3b–c |
| **Ch 7** (the mirror that makes time) | inner clock reversal ⟹ second-order time | **Paper LV** §5 | `docs/rendering-layer.md` §5 | R4a–c; T10 |
| **Ch 8** (the measured numbers) | status table; proton radius; b-anomaly; conditional G | claim ledger + Papers XXXII, LII, **LVII** §5 | `docs/claim-status-ledger.md`; `cascade-masses.md` §E3 | `verify_hadron_radii.py`; RGRAV1–2 |
| **Ch 9** (one world, many resolutions) | rung sampling; Newton; Einstein derived; Schrödinger; Maxwell; gauge inventory | **Papers LIII, LVII, LVI**; rung-ladder docs | `docs/gr-closure-derivation.md`; `docs/residual-closure-derivation.md`; `docs/gauge-group-from-arenas.md` | `verify_gr_closure.py` (39); `verify_residual_closure.py` (24); YM1–2 |
| **Ch 10** (the seventh dimension) | arenas only 3D+7D; octonionic ladder | rung-ladder docs (paper pending); **LVI** §1 (A1) | `docs/rung-dimension-ladder.md` | `verify_rung_dimension_ladder.py` (25); `verify_ladder_completion.py` (29); SM6 |
| **Ch 11** (which world happens) | selection = symmetry breaking; history selects | narrative-gap docs (G9) | `docs/narrative-gap-closure.md` | `verify_narrative_closure.py` (28) |
| **Ch 12** (what we don't know) | the named residual list | **LVII** §6 ledger; claim ledger §D | `docs/residual-closure-derivation.md` §5 | — (the list itself) |
| **Ch 13** (why it might be true) | everything has code | verification manifest | `docs/verification-manifest.md` | all suites, 205+ checks |
| Appendix (check it yourself) | commands + counts | verification manifest | `docs/verification-manifest.md` | — |

## The new paper spine (this campaign)

- **Paper LIII** — Einstein's Equations from Substrate Closure (the gravity chain, first pass).
- **Paper LIV** — The Forced Crystal (why this object; McKay/E8; spectral self-embedding).
- **Paper LV** — The Rendering Layer (arena, kernel, chart, second-order time).
- **Paper LVI** — The Gauge-Group Inventory from the Two Arenas (structure derived, wiring open).
- **Paper LVII** — Residual Closure of the Gravity Chain (bootstrap in-house; non-Gaussian; explicit rates; conditional G).
- **Paper LVIII** — Chirality and Charge Quantization from the Two Arenas.
- **Paper LIX** — The Resonance Chain (mass ladder, placements, deviation decomposition, the fenced selection problem; underpins the ledger simulator and web explorer).
- **Paper XL** — (updated) the remaining Gromov–Hausdorff arena programme.

Hostile-review hardening: every paper above goes through the codex referee loop (`scripts/review_paper.sh`); reviews land in `docs/reviews/` and are part of the public record, including the findings and how each was answered.

## Gaps acknowledged (not yet papered)

- A dedicated rung-ladder paper (Ch 9/10's sampling-intertwiner theorem currently lives in `docs/rung-dimension-ladder.md` with 25/25 + 29/29 sims but no standalone tex). Candidate Paper LVIII.
- The selection-layer (Ch 11) work order: G9's reduction is documented; the universal law is the programme's named deep open.
- The S⁷/octonionic rendering note (Ch 10) referenced by the rung docs.

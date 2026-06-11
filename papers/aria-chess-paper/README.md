# aria-chess paper bundle

Maintenance copy of the aria-chess substrate-witness paper for publishing. The
upstream development repo is `aria-chess` (the GitHub repo cited in the paper's
`@misc{ariaChessRepo}` bibtex entry); this bundle is the publication-ready
artifact, kept here so the paper and its supporting evidence can be edited and
released from this repo.

## Layout

```
papers/aria-chess-paper/
├── README.md                          (this file)
├── TASK-aria-paper-completion.md      (work order; see also docs/codex-derive/)
├── paper/
│   ├── main.tex                       LaTeX source (212 lines)
│   ├── main.pdf                       Built PDF (247 KB)
│   ├── references.bib                 Bibliography (180 lines)
│   ├── README.md                      Paper-specific build/repro notes
│   ├── sections/01..10_*.tex          Ten section files (~1900 lines total)
│   └── figures/                       (empty placeholder)
└── brain_mapping_refs/
    ├── PAPER_PREDICTIONS.md                    Preregistration frozen 2026-04-18 (P1–P18)
    ├── PREREG_H4_FINGERPRINT.md                Later prereg battery (2026-04-24)
    ├── PREREG_RUNG_OBSERVABLES.md              Later prereg battery (2026-04-24)
    ├── VALIDATION_RESULTS_2026-04-29.md        18/18 tally with thresholds
    ├── CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md    Six EEG signatures, per-condition
    ├── P4_SYNERGY_FINDING.md                   N=20 C×P deep-dive
    ├── CROSS_DOMAIN_RESULTS.md                 Chess / conversation / HCP
    └── NON_EQUILIBRIUM_FINDING.md              State-reset protocol
```

## What's here

The publication-ready paper plus the eight supporting `brain_mapping/*.md`
documents the paper text references for preregistration provenance, validation
results, and protocol detail. These are the artifacts a reviewer needs to verify
the paper's claims at the documentation level.

## What's intentionally not here

- **Validation scripts** (`demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`,
  `run_preregistered_validation.py`, `run_chess_robustness.py`,
  `reproduce_paper_claims.sh`) — these live in the upstream `aria-chess` repo
  cited via `@misc{ariaChessRepo}` in `paper/references.bib`. The paper §2
  provenance ledger names them so a reviewer can locate them; the bundle isn't
  meant to be a self-contained execution environment.
- **Kernel modules** (`kernel/vfd_closure_kernel.py`, `kernel/sigma_orbit_basis.py`,
  `kernel/dimensional_monitor.py`, `kernel/cascade_descent.py`,
  `kernel/lyapunov_selector.py`, `kernel/self_model_stream.py`,
  `kernel/consciousness_binding.py`, `kernel/consciousness_tensor.py`) — same
  reasoning; ~5,000 lines of repository infrastructure, cited by file:line in
  the paper, but not part of the publication artifact itself.
- **`paper/results.json`, `paper/paper_summary.md`** (in upstream `aria-chess/paper/`) —
  these belong to a *different* paper draft titled "The H₄ Oscillator Law"
  and are not associated with this substrate-witness manuscript. Deliberately
  excluded.
- **`docs/brain_mapping/MANUSCRIPT_V2.md`** — earlier 1253-line draft form of the
  same paper. The `.tex` paper is the canonical publication form; including
  the older draft alongside would create reader confusion about which document
  is canonical.

## Building the paper

```bash
cd paper/
tectonic main.tex
# or pdflatex main / bibtex main / pdflatex main / pdflatex main
```

The build is self-contained — no external file references needed for compilation.
The references in the paper text to `docs/brain_mapping/*.md` are documentary
mentions (the reviewer can find them in `brain_mapping_refs/` here, or in the
upstream `aria-chess` repo).

## Codex hostile-review trail

The paper went through 8 codex review rounds before reaching `Publication ready: yes`:

- Reviews: `docs/reviews/aria-chess-paper-2026043​0T*.md` (eight passes, in this repo)
- Round 7 (b) substantive verdict: *"No over-claim, scope-drift, or numerical inconsistency found."*
- Round 8 (c) verdict: **`Publication ready: yes`** — last cosmetic line-wrap fixed.

## Known paper-text issues (worth fixing before journal submission)

- §2 Provenance ledger cites two scripts that **don't exist in upstream**:
  `run_conversation_robustness.py` and `run_hcp_validation.py`. Either create
  thin wrappers in upstream (preferred — the underlying logic exists in
  `run_preregistered_validation.py` and the HCP analysis pipeline) or change
  the paper text to point to the existing combined script. Not blocking for
  preprint; would surface under journal review.

## Scope discipline (locked)

This is a **substrate witness**, not a selection theorem. The paper does not
claim:
- the substrate IS consciousness;
- 600-cell uniqueness among regular 4-polytopes;
- a Lyapunov function on the reduced flow has been delivered;
- the ACT 4-tuple bridge delivers a selection theorem here.

The 18/18 preregistered tally is reported as methodology refinement (no
threshold modified). See `paper/sections/01_introduction.tex` claim-boundary box
and `paper/sections/09_limitations.tex` five-move guard matrix.

# cascade-mechanism — repro

Self-contained reproduction bundle for the load-bearing data claims of
the paper `cascade-mechanism.tex`.

This bundle re-runs the two scripts that anchor Appendix~A and Appendix~E
of the paper, captures their output to text files for diff-against the
frozen reference outputs in `expected_outputs/`, and confirms the
headline numbers used in the paper's main text and field-signature
audit.

The scripts themselves live in their canonical sibling-paper
directories (see `RUN.md` for paths); this bundle calls them via
relative paths from the repository root, so nothing here duplicates
script source.

## Quick start

From the repository root:

```bash
cd papers/cascade-mechanism/repro
bash run_audit.sh
```

Wallclock: ~10 seconds total on a laptop.

The script writes captured output to `output/` and prints a summary
diff against `expected_outputs/`.  A clean run prints `AUDIT PASSED`
at the end with both scripts matching their reference outputs to the
significant-figure precision recorded in the paper.

## Requirements

- Python 3.8 or newer
- `numpy` (>= 1.20)
- `scipy` (>= 1.7)

Install via:

```bash
pip install -r requirements.txt
```

No external data, no network access, no random seed (eigendecomposition
is deterministic at machine precision).

## What is reproduced

### Appendix~A — σ-attractor spectrum

Script:
`papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py`

Reproduces:

- 600-cell vertex Laplacian has nine distinct eigenvalues, five integer
  (`{0, 9, 12, 14, 15}`, σ-fixed under
  `σ(φ) = 1 − φ = −1/φ`) and four irrational in `Q(√5)`
  (σ-paired).
- Counted with multiplicity: σ-fixed fraction `94/120 = 78.3%`,
  σ-paired fraction `26/120 = 21.7%`.
- σ-fixed eigenvector mass on the binary tetrahedral subgroup `2T`:
  `0.20`, identical to the random-vector baseline `0.20` — the
  honest-negative recorded in §4.2 of the paper, confirming the
  σ-fixed structure is purely spectral, not spatial.

### Appendix~E — closure kernel

Script: `papers/aria-closure-kernel/repro/verify_kernel.py`

Reproduces:

- Vertex count `|V_600| = |2I| = 120`, uniform vertex degree 12.
- Euclidean / conjugacy shell sizes
  `(1, 12, 20, 12, 30, 12, 20, 12, 1)` exact.
- Operator norm `‖C_φ⁻¹‖ ≈ 2.618033988749902`, matching `φ²` to
  machine precision (the paper's analytic identity from
  `λ_min(L_M) = 0` plus the `φ⁻²` shift).
- Per-vertex Pearson correlation between the discrete `C_φ⁻¹`
  response and the continuum closure-kernel Green function
  `G(x) = (φ/2) e^{−|x|/φ}`:
  - `0.9762` (UNWEIGHTED — wins)
  - `0.8884` (PHI_GEOMETRIC weighted)
  - `0.8844` (PHI_ARITHMETIC weighted)
- Multi-source uniformity across all 120 source-vertex sweeps:
  `max − min ≈ 2.0e−15` (numerical-precision floor).
- Honest-negative carried in §4.2 of the paper: φ-cocycle weighted
  variants underperform the unweighted operator. Use
  `C_φ = L + φ⁻²I` only.

## What is *not* reproduced here

The following data points cited in the paper are **imported empirical
witnesses** from external preprints and are not re-executed inside this
bundle:

- ARIA preregistered-correspondences, drug/sleep EEG signatures, and
  HCP brain-functional-connectivity numbers (Appendix~F) — see the
  ARIA-chess preprint
  (`papers/aria-chess-paper/paper/main.tex`) and its frozen working-tree
  snapshot `aria-chess/v4_locked_2026-04-29/` for the upstream
  reproduction. Snapshot identifiers (date, session UUID, substrate
  version, deterministic seeds) are recorded in the cascade-mechanism
  bibliography entry for `ariaChessRepo`.

- The b → s μ⁺μ⁻ angular fit from `SmartBAnomaly` (§6 of the paper)
  — see the sibling repository `BANOMALY-001/vfd-b-anomaly`,
  branch `main`, commit `6bdfc8f8a7da9056ffeb9137d03627d06399bccf`,
  for the upstream reproduction. The cascade-mechanism paper itself
  makes no independent claim on that fit; it cites it as one
  externally-reported substrate-witness use of `C_φ`.

These external witnesses are scoped exactly as described in the
paper's epistemic-status box. The cascade-mechanism bundle covers
the operator-norm identity and shell/spectrum diagnostics — the
mechanism's own internal numerical content — only.

## Determinism

Neither script makes any `numpy.random` calls. Both reduce to
deterministic linear algebra (`numpy.linalg.eigh`,
`numpy.linalg.solve`) plus exact `Q(√5)` `Fraction` arithmetic in
the σ-attractor case. Reruns reproduce all reported numbers to the
precisions recorded in `expected_outputs/`.

## Files in this bundle

- `README.md` — this file.
- `RUN.md` — exact script paths and what each one anchors.
- `run_audit.sh` — single-command audit wrapper.
- `requirements.txt` — minimal Python dependencies.
- `expected_outputs/` — frozen reference outputs (re-run
  `bash run_audit.sh --refresh-expected` to regenerate; do not
  do this casually, the whole point is that they are frozen).
- `output/` — created by `run_audit.sh`; contains the live captured
  output from each script run. Git-ignored.

## Citation

If you use this reproduction bundle, please cite the paper:

```
Smart, L. (2026). Cascade Closure: A Conditional Compatibility
Template for Geometric State Selection Beyond Collapse Language.
Preprint, Institute of Vibrational Field Dynamics.
```

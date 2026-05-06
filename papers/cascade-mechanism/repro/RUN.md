# cascade-mechanism / repro — script anchor map

| Paper anchor | Script (relative to repo root) | Headline reproduction |
|---|---|---|
| Appendix A — σ-attractor spectrum | `papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py` | 600-cell Laplacian spectrum, 94/26 σ-fixed/σ-paired split, `2T`-mass honest-negative |
| Appendix E — closure kernel | `papers/aria-closure-kernel/repro/verify_kernel.py` | `\|C_φ⁻¹\| = φ²` exact, shell sizes, per-vertex correlation `0.976` (UNWEIGHTED wins), multi-source uniformity to ~`1e−15` |

Run both in sequence with `bash run_audit.sh` from this directory.
The wrapper handles `cd` to repo root so the scripts find their
sibling-package imports.

## Why the scripts live in sibling directories rather than here

Both scripts are canonical artefacts of their respective papers
(`cascade-derivation` and `aria-closure-kernel`) and are also cited
by those papers' own reproduction bundles and field-signature audits.
Duplicating them into this directory would create two copies that
could drift out of sync. Instead, this bundle's `run_audit.sh`
calls them by relative path from the repo root and captures their
output to `output/` here, then diffs that output against the frozen
references in `expected_outputs/` here.

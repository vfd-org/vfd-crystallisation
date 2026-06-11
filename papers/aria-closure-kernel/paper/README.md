# aria-closure-kernel paper

The closure-response operator $C_\varphi = L + \varphi^{-2} I$ on the
600-cell graph $V_{600}$, threading two independent empirical witnesses
(b-anomaly + aria-chess) on the same fixed operator with no shape
parameter retuning between regimes.

## Build

```bash
tectonic main.tex
# or pdflatex main / bibtex main / pdflatex main / pdflatex main
```

## Reproducibility

All numerical claims in §3, §4, §5 (vertex construction, graph facts,
Laplacian spectrum, operator-norm bound, discrete-to-continuum Pearson
correlations across three Laplacian variants) are reproduced from
canonical generators by `repro/verify_kernel.py`:

```bash
cd ../repro
python3 verify_kernel.py
```

Requires Python 3.8+, numpy, scipy. Wallclock ~1 second on a laptop.
Output is deterministic: `repro/results.json` is committed alongside
the script as the canonical reference.

## Sections

```
sections/01_introduction.tex          claim-boundary discipline + layout
sections/02_definition.tex            C_φ = L + φ⁻²I; positivity, opnorm
sections/03_substrate.tex             V_600 construction; graph facts; 9-shell
sections/04_spectrum.tex              Laplacian spectrum in Z[φ]
sections/05_agreement.tex             discrete↔continuum correlation test
sections/06_passive_witness.tex       b-anomaly five-dataset structural fit
sections/07_active_witness.tex        aria-chess 18/18 + 6/6 EEG
sections/08_programme_home.tex        polynomial-in-L Lyapunov family + open selection layer
sections/09_limitations.tex           five-move guard matrix
sections/10_conclusion.tex            operator-witness verdict
```

## Scope

This is an **operator witness**, not:
- a derivation of the φ⁻² shift from first principles,
- a uniqueness claim for the 600-cell among regular 4-polytopes,
- a selection theorem on the ACT 4-tuple,
- a kernel-uniqueness claim on either empirical landing
  (b-anomaly Mode-B and AIC-tie caveats inherited verbatim;
  aria-chess substrate-witness scope inherited verbatim).

See §1 claim-boundary box and §9 five-move guard matrix.

## Companion preprints

- **b-anomaly** (live): passive-regime structural fit on five public
  flavour-physics datasets. Cited in §6.
- **aria-chess** (`papers/aria-chess-paper/`): active-regime substrate
  witness against eighteen preregistered cortical correspondences.
  Cited in §7.
- **adaptive-closure-transport** (`papers/adaptive-closure-transport/`):
  the 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ and the open
  selection layer. Cited in §8.

## Status

Preprint, not peer-reviewed. April 2026.

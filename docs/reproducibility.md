# Reproducibility Guide

All results reported in the papers can be reproduced using the commands below, subject to numerical precision and platform consistency.

## Requirements

### Python
- Python >= 3.8
- Dependencies: `pip install -r requirements.txt`
- Or: `pip install numpy scipy matplotlib pytest`

### LaTeX (for PDF generation)
- TeX Live (Linux/Mac) or MiKTeX (Windows)
- Required packages: amsmath, amssymb, amsthm, graphicx, hyperref, booktabs, geometry, natbib

## Running Tests

```bash
# All crystallisation tests
python -m pytest tests/ -v

# Individual test suites
python -m pytest tests/test_crystallisation_operator.py -v    # 24 tests, ~8s
python -m pytest tests/test_benchmark.py -v                   # 62 tests, ~7s
python -m pytest tests/test_falsifiability.py -v              # 38 tests, ~5min
python -m pytest tests/test_estimation.py -v                  # 32 tests, ~7min
```

## Generating Figures

```bash
python scripts/generate_figures.py
```

Produces publication-quality PNGs in `figures/preprint/`. All figures are deterministic (seeded RNG) and produce identical output across platforms.

## Building PDFs

```bash
# Linux/Mac
./scripts/build_pdfs.sh

# Windows PowerShell
.\scripts\build_pdfs.ps1
```

Or build individual papers:
```bash
cd papers/main-preprint/
pdflatex crystallisation-dynamics.tex
bibtex crystallisation-dynamics
pdflatex crystallisation-dynamics.tex
pdflatex crystallisation-dynamics.tex
```

## Running Benchmarks

```bash
python benchmarks/crystallisation_benchmark.py
```

Runs all four models (Lindblad, GRW, OR, crystallisation) on preset scenarios (qubit, biased, multi-level, noise sweep) and prints comparative metrics. The benchmark is intended to demonstrate model distinguishability under controlled conditions, not to establish empirical validation.

## Overleaf

To use with Overleaf:
1. Upload all files from `papers/main-preprint/` (or any paper directory)
2. Set the `.tex` file as main document
3. Compile with pdflatex + bibtex

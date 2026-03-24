# VFD Crystallisation Operator

A testable, constraint-driven model of state resolution formulated as an alternative to probabilistic wavefunction collapse.

State resolution is modelled as minimisation of a closure functional over a constrained manifold, yielding stable coherent structures via attractor dynamics. The framework is compatible with standard open quantum system evolution and yields predictions distinct from decoherence, GRW collapse, and Penrose objective reduction.

This repository presents a testable research framework and supporting reference implementation; it does not assume correctness of the model and is structured to enable independent evaluation.

---

## Start Here

1. **Read the main paper**: [`papers/main-preprint/crystallisation-dynamics.tex`](papers/main-preprint/crystallisation-dynamics.tex)
2. **See the publication plan**: [`docs/overview.md`](docs/overview.md)
3. **Reproduce everything**: [`docs/reproducibility.md`](docs/reproducibility.md)

---

## Core Idea

The crystallisation operator maps an unresolved field configuration to a stable coherent configuration by constrained minimisation:

```
C[Psi] = Psi*  =  argmin_Phi  F[Phi]

F[Phi]  =  alpha * R[Phi]  +  beta * E[Phi]  -  gamma * Q[Phi]
```

- **R** = closure residual (constraint mismatch)
- **E** = energy functional (energetic cost)
- **Q** = coherence metric (phase alignment)

In this framework, what is conventionally treated as collapse is modelled as convergence toward a constraint-compatible attractor.

---

## Papers (1 + 4 structure)

The flagship paper is the primary entry point; the companion papers provide mathematical depth, experimental methodology, structural justification, and a concrete demonstration.

| Role | Paper | Location |
|------|-------|----------|
| **Flagship** | Crystallisation Dynamics as a Deterministic Alternative to Collapse | [`papers/main-preprint/`](papers/main-preprint/) |
| Companion A | Mathematical Structure and Properties | [`papers/formalism/`](papers/formalism/) |
| Companion B | Experimental Signatures, Estimation + Benchmarks | [`papers/experimental/`](papers/experimental/) |
| Companion C | Constraint-Driven Selection as an Emergent Principle | [`papers/inevitability/`](papers/inevitability/) |
| Companion D | Triplet Closure, Regime Structure + ARIA Demonstration | [`papers/mechanism/`](papers/mechanism/) |
| Supplementary | Prediction registry, parameter registry, platform sheets | [`papers/supplementary/`](papers/supplementary/) |

---

## Repository Layout

```
vfd-crystallisation/
├── papers/
│   ├── main-preprint/          Flagship paper
│   ├── formalism/              Companion A: mathematical depth
│   ├── experimental/           Companion B: signatures + estimation + benchmarks
│   ├── inevitability/          Companion C: structural inevitability argument
│   ├── mechanism/              Companion D: triplet closure + ARIA demo
│   └── supplementary/          Registries + platform mapping sheets
├── src/vfd/crystallisation/    Reference implementation
│   ├── operator.py             Core crystallisation operator
│   ├── falsifiability.py       Statistical discrimination
│   ├── estimation.py           Parameter fitting + identifiability
│   ├── synthetic_data.py       Experiment simulators
│   ├── figures.py              Publication figure generation
│   ├── benchmark_metrics.py    Unified comparison metrics
│   └── models/                 4 competing quantum models
├── figures/preprint/           Publication figures
├── benchmarks/                 Benchmark engine + configs
├── notebooks/                  7 Jupyter notebooks
├── tests/                      156 tests (4 suites)
├── scripts/                    Build + generation scripts
└── docs/                       Overview + reproducibility
```

---

## Quick Start

```bash
pip install -r requirements.txt     # Install dependencies
python -m pytest tests/ -v          # Run all tests
python scripts/generate_figures.py  # Generate figures
./scripts/build_pdfs.sh             # Build all PDFs (requires LaTeX)
```

---

## Figures

| Fig | Content | Description |
|-----|---------|-------------|
| 1 | Closure functional F(t) | Illustrates monotonic descent consistent with the gradient-flow structure |
| 2 | Crystallisation vs decoherence | Illustrates structured selection relative to decoherence baseline |
| 3 | Basin selection | Illustrates attractor assignment across varied initial conditions |
| 4 | Transition-time scaling | Illustrates structured, multi-parameter transition-time dependence |

---

## Tests

| Suite | Tests |
|-------|-------|
| Operator | 24 |
| Falsifiability | 38 |
| Estimation | 32 |
| Benchmark | 62 |
| **Total** | **156** |

---

## How to Cite

For citation metadata, see [`CITATION.cff`](CITATION.cff). The flagship paper should be cited when referencing the core framework.

---

## License

MIT. See [`LICENSE`](LICENSE) for details.

Code and documentation are covered by the MIT licence. Paper source files (`.tex`) are included for reproducibility; if reusing paper content beyond code, please cite appropriately.

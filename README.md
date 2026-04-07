# VFD Crystallisation Operator

**A testable, constraint-driven model of state resolution formulated as an alternative to probabilistic wavefunction collapse.**

---

## What Is This?

The quantum measurement problem asks: when a quantum system is in a superposition of states, how does a single definite outcome emerge? The standard formalism provides probabilities (the Born rule) but no mechanism — it tells you *what* you observe, not *how* selection happens.

This repository presents the **crystallisation operator**: a framework in which state selection arises not from random projection but from deterministic convergence toward a stable attractor of a **closure functional**. The system evolves under gradient flow, balancing three requirements — constraint satisfaction, energetic cost, and internal coherence — until it reaches a stable configuration.

The framework is compatible with standard open quantum system evolution (recovering Lindblad dynamics when the crystallisation coupling is zero) and yields predictions that are quantitatively distinct from decoherence, GRW-style stochastic collapse, and Penrose objective reduction.

This repository presents a testable research framework and supporting reference implementation. It does not assume correctness of the model and is structured to enable independent evaluation.

---

## Core Idea

The crystallisation operator maps an unresolved configuration to a stable coherent state by constrained minimisation:

```
C[Psi] = Psi*  =  argmin_Phi  F[Phi]

F[Phi]  =  alpha * R[Phi]  +  beta * E[Phi]  -  gamma * Q[Phi]
```

- **R** = closure residual — how far the configuration is from satisfying the governing constraints
- **E** = energy functional — the energetic or structural cost of the configuration
- **Q** = coherence metric — the degree of internal phase alignment

In this framework, what is conventionally treated as "collapse" is modelled as convergence toward a constraint-compatible attractor. The dynamics is continuous (no discontinuous jumps), the timescale is derived (not postulated), and the selected outcome depends on the geometry of the constraint landscape rather than solely on Hilbert-space amplitudes.

---

## Start Here

1. **Read the flagship paper** (PDF): [`Crystallisation Dynamics as a Deterministic Alternative to Collapse in Open Quantum Systems`](papers/main-preprint/crystallisation-dynamics.pdf)
2. **See the full publication plan**: [`docs/overview.md`](docs/overview.md)
3. **Reproduce everything**: [`docs/reproducibility.md`](docs/reproducibility.md)

---

## Papers

The research programme follows a **1 + 6** structure: one flagship paper supported by six companion papers and a supplementary layer. The flagship paper stands alone; everything else provides depth.

### Flagship

**[Crystallisation Dynamics as a Deterministic Alternative to Collapse in Open Quantum Systems](papers/main-preprint/crystallisation-dynamics.pdf)** ([LaTeX source](papers/main-preprint/crystallisation-dynamics.tex))

The primary paper. Introduces the crystallisation operator, extends it to density matrices, presents simulation results (4 figures), outlines experimental signatures, and states five explicit falsification criteria. Readable in ~15 minutes by a physicist without prior context.

### Companion A — Mathematical Formalism

**[The Crystallisation Operator: Mathematical Structure and Properties](papers/formalism/crystallisation-formalism.pdf)** ([LaTeX source](papers/formalism/crystallisation-formalism.tex))

Full mathematical companion. Formal operator definition, four theorems with proof sketches (existence, stability, monotonic descent, mode selection), spectral reweighting formulation, Hessian analysis, crystallisation timescale. Pure structure, no narrative.

### Companion B — Experimental Framework

**[Experimental Signatures, Parameter Estimation, and Benchmark Comparison of the Crystallisation Operator](papers/experimental/crystallisation-experimental.pdf)** ([LaTeX source](papers/experimental/crystallisation-experimental.tex))

The "can we test this?" paper. Defines six signature classes distinguishing crystallisation from Lindblad, GRW, and Penrose OR. Specifies a nine-parameter estimation framework with identifiability diagnostics. Reports a controlled numerical benchmark across five scenarios with seven metrics and statistical discrimination (KS tests, bootstrap CIs, likelihood ratios). States five falsification criteria.

### Companion C — Structural Inevitability

**[Constraint-Driven Selection as an Emergent Principle in Dynamical Systems](papers/inevitability/constraint-driven-selection.pdf)** ([LaTeX source](papers/inevitability/constraint-driven-selection.tex))

Argues that the crystallisation functional F = alphaR + betaE - gammaQ is not arbitrary but arises naturally from minimal structural requirements for selection in constrained dynamical systems. Presented at the level of dynamical systems — no physical derivation claims.

### Companion D — Mechanism + ARIA Demonstration

**[Crystallisation as a Selection Mechanism: Triplet Closure, Regime Structure, and a Deterministic Demonstration](papers/mechanism/crystallisation-mechanism.pdf)** ([LaTeX source](papers/mechanism/crystallisation-mechanism.tex))

Formalises **triplet closure**: three classes of constraint (internal, boundary, observational) are jointly sufficient for discrete state resolution under generic conditions, whereas any pair alone generically is not. Defines a regime structure governed by Delta = lambda/Gamma. Demonstrates the mechanism in the **ARIA governed reasoning system** — a deterministic pipeline that resolves a canonical request through three candidates to a single output, producing a cryptographically verifiable proof pack. Includes the full [proof-pack artifacts](papers/mechanism/demo/) for independent verification.

### Companion E — Particles, Geometry, and Mass

**[Particles, Geometry, and Mass from Deterministic Field Closure](papers/master-mass/master-mass.pdf)** ([LaTeX source](papers/master-mass/master-mass.tex))

Develops a structural theory of particles and mass within the closure framework. Particles are identified with stable closure classes characterised by discrete shell support, winding number, and symmetry sector. Five assignment rules uniquely determine the electron and proton. A three-order mass law with zero fitted continuous parameters yields the rational exponent 1265/81 and a predicted proton-to-electron ratio of ~1835.8, in structural agreement with the observed value at the 2×10⁻⁴ level. Includes formal no-go for naive lepton assignments and precise diagnosis of the missing winding layer.

### Companion F — Lepton Generations

**[Lepton Generations and the Missing Mass Operator in Deterministic Field Closure](papers/lepton-generations/lepton-generations.pdf)** ([LaTeX source](papers/lepton-generations/lepton-generations.tex))

Companion to Paper E. Proves a formal no-go theorem establishing that shell-support extension cannot produce muon or tau mass ratios. Identifies the required winding-dependent boundary excitation operator f(w) = phi^N (w-1)^(1/phi), where the exponent 1/phi is consistent with hydrogen-like spectral scaling in a space of effective dimension phi, and the coefficient phi^N is the unique phi-integer-power matching the muon mass. Predicts the muon-to-electron ratio to 0.5% and the tau-to-electron ratio to 3.7% with zero fitted continuous parameters.

### Supplementary Material

Reference documents (not standalone papers):

| Resource | Description |
|----------|-------------|
| [Prediction Registry](papers/supplementary/prediction-registry.pdf) ([LaTeX](papers/supplementary/prediction-registry.tex)) | 10 structured predictions with per-model expectations and falsification conditions |
| [Parameter Registry](papers/supplementary/parameter-registry.md) | Full specification of all 9 canonical parameters with units, ranges, and experimental proxies |
| [Platform Mapping Sheets](papers/supplementary/platform-mapping/) | 5 platform-specific experimental guides (qubit, interferometry, cold atom, quantum optics, analog oscillator) |
| [Experimental Signatures](papers/supplementary/signatures.md) | 5 experiment class protocols with full specifications |

---

## Repository Layout

```
vfd-crystallisation/
├── papers/
│   ├── main-preprint/          Flagship paper (tex + pdf + bib)
│   ├── formalism/              Companion A: mathematical depth
│   ├── experimental/           Companion B: signatures + estimation + benchmarks
│   ├── inevitability/          Companion C: structural inevitability argument
│   ├── mechanism/              Companion D: triplet closure + ARIA demo
│   │   └── demo/               ARIA proof-pack artifacts (13 JSON files)
│   ├── master-mass/            Companion E: particles, geometry, and mass
│   ├── lepton-generations/     Companion F: lepton generations + winding operator
│   └── supplementary/          Registries + platform mapping sheets
├── src/vfd/crystallisation/    Reference implementation
│   ├── operator.py             Core crystallisation operator
│   ├── falsifiability.py       Statistical discrimination framework
│   ├── estimation.py           Parameter fitting + identifiability
│   ├── synthetic_data.py       Experiment simulators + data generators
│   ├── figures.py              Publication figure generation
│   ├── benchmark_metrics.py    Unified comparison metrics
│   └── models/                 4 competing quantum models
│       ├── lindblad_model.py   M1: Standard Lindblad (baseline)
│       ├── grw_model.py        M2: GRW stochastic collapse
│       ├── or_model.py         M3: Penrose OR proxy
│       └── crystallisation_model.py  M4: VFD crystallisation
├── figures/preprint/           Publication-quality figures (deterministic, seeded)
├── benchmarks/                 Benchmark engine + 3 YAML configs
├── notebooks/                  7 Jupyter notebooks
├── tests/                      156 tests (4 suites, all passing)
├── scripts/                    PDF build + figure generation scripts
└── docs/                       Overview + reproducibility guide
```

---

## Quick Start

```bash
pip install -r requirements.txt     # Install dependencies
python -m pytest tests/ -v          # Run all 156 tests
python scripts/generate_figures.py  # Generate publication figures
./scripts/build_pdfs.sh             # Build all PDFs (requires LaTeX)
```

---

## Figures

All figures are deterministic (seeded RNG) and reproducible across platforms.

| Fig | Content | Description |
|-----|---------|-------------|
| 1 | Closure functional F(t) | Illustrates monotonic descent consistent with the gradient-flow structure |
| 2 | Crystallisation vs decoherence | Illustrates structured selection relative to decoherence baseline |
| 3 | Basin selection | Illustrates attractor assignment across varied initial conditions |
| 4 | Transition-time scaling | Illustrates structured, multi-parameter transition-time dependence |

---

## Tests

All tests pass. The test suite covers the core operator, statistical discrimination, parameter estimation, and four-model benchmarking.

| Suite | Tests | Coverage |
|-------|-------|----------|
| Operator | 24 | Core functionals, convergence, stability, spectral reweighting |
| Falsifiability | 38 | 6 metrics, 3 model simulators, KS/bootstrap/permutation tests |
| Estimation | 32 | Fitting, bootstrap CI, identifiability, sensitivity, model comparison |
| Benchmark | 62 | 4-model interface compliance, fairness, equivalence/divergence regimes |
| **Total** | **156** | |

---

## Key Claims and Their Scope

This repository makes claims at three levels, which should be evaluated independently:

| Level | Claim | Where |
|-------|-------|-------|
| **Structural** | Constraint-driven selection arises naturally in systems with constraints, cost, and coherence | Inevitability paper, Mechanism paper |
| **Phenomenological** | The crystallisation dynamics yields testable deviations from standard QM in specific regimes | Flagship, Experimental companion |
| **Demonstrative** | The mechanism can be concretely instantiated and independently verified | ARIA demonstration + proof pack |

The framework does not claim to replace quantum mechanics. It proposes a testable extension and provides the tools to evaluate it.

---

## How to Cite

For citation metadata, see [`CITATION.cff`](CITATION.cff).

When referencing the core framework, cite the flagship paper:

> Lee Smart, "Crystallisation Dynamics as a Deterministic Alternative to Collapse in Open Quantum Systems," Preprint, Institute of Vibrational Field Dynamics, 2026.

---

## License

MIT. See [`LICENSE`](LICENSE) for details.

Code and documentation are covered by the MIT licence. Paper source files (`.tex`) are included for reproducibility; if reusing paper content beyond code, please cite appropriately.

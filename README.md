# VFD: Crystallisation, Closure Geometry, and Deterministic Selection

**A testable, constraint-driven model of state resolution and geometric mass structure.**

---

## What Is This?

The quantum measurement problem asks: when a quantum system is in a superposition of states, how does a single definite outcome emerge? The standard formalism provides probabilities (the Born rule) but no mechanism — it tells you *what* you observe, not *how* selection happens.

This repository presents the **crystallisation operator**: a framework in which state selection arises not from random projection but from deterministic convergence toward a stable attractor of a **closure functional**. The system evolves under gradient flow, balancing three requirements — constraint satisfaction, energetic cost, and internal coherence — until it reaches a stable configuration.

The framework is compatible with standard open quantum system evolution (recovering Lindblad dynamics when the crystallisation coupling is zero) and yields predictions that are quantitatively distinct from decoherence, GRW-style stochastic collapse, and Penrose objective reduction.

This repository presents a testable research framework and supporting reference implementation. It does not assume correctness of the model and is structured to enable independent evaluation.

---

## Research Scope

This repository contains two connected research tracks within the broader VFD programme:

1. **Crystallisation dynamics** — a deterministic, constraint-driven selection framework proposed as an alternative to probabilistic collapse in open quantum systems.
2. **The mass programme** — a geometric closure framework for particle mass ratios, developed through Papers I–IV and anchored by Paper IV as the primary external-facing mass paper.

These tracks are related by a common structural theme: state resolution through constrained spectral structure. The crystallisation papers focus on general selection dynamics; the mass papers explore whether analogous closure geometry can organise particle mass structure.

---

## Recommended Reading Order

### For the crystallisation programme
1. Flagship paper (crystallisation dynamics)
2. Companion B (experimental framework)
3. Companion A (mathematical formalism)
4. Companion D (mechanism + ARIA demo)
5. Companion C (structural inevitability)

### For the mass programme
1. **Paper V** (complete particle mass spectrum — start here)
2. Paper IV (proton-electron bridge paper — the foundation)
3. Paper III (spectral support and retraction)
4. Paper II (no-go theorem + conditional winding operator)
5. Paper I (internal mass-development paper)

### For the conceptual bridge (Dirac → Crystallisation)
1. Bridge paper (selection architecture on Dirac solution space)

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

The crystallisation programme follows a **1 + 4** structure: one flagship paper supported by four companion papers and a supplementary layer. The mass programme adds Papers I–IV (see below). The flagship paper stands alone; everything else provides depth.

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

### Mass Programme (Geometric Closure Papers I–V)

The repository also contains a separate but related mass programme, which applies closure geometry and spectral structure to particle mass ratios. **Paper V is the complete mass-spectrum paper**; Paper IV is the proton-electron bridge paper; Papers I–III document the internal development. **Recommended reading order for the mass programme:** start with Paper V for the full result, or Paper IV for the proton-electron foundation.

#### Paper V — Complete Particle Mass Spectrum

**[Toward a Spectral-Geometric Particle-Mass Model from the 600-Cell](papers/paper-v/Toward_a_Spectral_Geometric_Particle_Mass_Model_from_the_600_Cell.pdf)** ([LaTeX source](papers/paper-v/paper-v.tex))

Extends Papers I–IV to a broader spectral-geometric mass framework using the golden ratio φ and the four integer eigenvalues {9, 12, 14, 15} of the 600-cell graph Laplacian. Under explicit framework postulates and structural assignments, yields high-accuracy mass values across 13 non-reference particles (average 0.014%). Also yields a high-precision numerical correspondence for the fine structure constant (0.81 ppm). Includes 6 exact graph theorems, the prediction chain, assignment rules, and full epistemic classification separating exact computations from model assignments and numerical correspondences.

#### Paper IV (Bridge Paper) — Proton–Electron Mass Ratio

**[A φ-Scaled Geometric Ansatz for the Proton–Electron Mass Ratio](papers/pemr/A_phi_Scaled_Geometric_Ansatz_for_the_Proton_Electron_Mass_Ratio.pdf)** ([LaTeX source](papers/pemr/pemr.tex))

The standalone bridge paper. Presents a structured geometric ansatz recovering m_p/m_e = φ^(1265/81) ≈ 1835.8 (experimental: 1836.15, discrepancy 2×10⁻⁴) with zero fitted continuous parameters. The leading exponent ΔC = 15 coincides exactly with a Laplacian eigenvalue of the 600-cell vertex graph (multiplicity 16). The correction terms are organised by the heat-kernel cumulant expansion. Includes the Zamolodchikov–Coldea E₈ precedent, spectral gap theorem λ₁(P₅) = φ⁻², sensitivity analysis, reproducibility section, and a 12-objection adversarial review. Externally readable without prior VFD context.

#### Paper I (Internal) — Closure Geometry and Mass

**[Proton-to-Electron Mass Ratio from Closure Geometry and Graph Invariants](papers/master-mass/Proton_to_Electron_Mass_Ratio_from_Closure_Geometry_and_Graph_Invariants.pdf)** ([LaTeX source](papers/master-mass/master-mass.tex))

The internal mass paper. Develops closure classes, assignment rules R1–R5, the combinatorial invariant, graph Laplacian term, degree-variance correction, and three-order mass law. Includes validation extensions (neutron compatible, muon/tau fail) and forward reference to the 600-cell spectral work.

#### Paper II (Internal) — Lepton Generations

**[Lepton Generations and the Missing Mass Operator in Deterministic Field Closure](papers/lepton-generations/Lepton_Generations_the_Missing_Mass_Operator_in_Deterministic_Field_Closure.pdf)** ([LaTeX source](papers/lepton-generations/lepton-generations.tex))

Proves a formal no-go theorem for shell-extension leptons. Proposes a conditional winding operator f(w) = φ⁵(w−1)^(1/φ), valid only if the relevant effective spectral dimension is identified with d_s = φ. Predicts the muon to 0.5% and the tau to 3.7% with zero fitted continuous parameters. The 600-cell eigenvalue correspondence and F4 numerical motivation are treated only as external support, summarised from Paper III.

#### Paper III (Internal) — Spectral Structure

**[Spectral Structure of the 600-Cell Vertex Graph: Eigenvalue Connections and the F4 Fibonacci Extension](papers/spectral-dimension/Spectral_Structure_of_the_600_Cell_Vertex_Graph.pdf)** ([LaTeX source](papers/spectral-dimension/spectral-dimension.tex))

Reports two spectral results: (1) the exact 600-cell eigenvalue correspondence λ = 15 = ΔC; (2) numerical F4 convergence toward d_s ≈ φ (R² = 0.996). Includes explicit retraction of the earlier d_s ≈ 1.637 claim for the 600-cell vertex graph, with explanation of the windowing artifact.

#### Paper VI — Electroweak Sector

**[Electroweak Structure as a Boundary Projection of φ-Structured Geometry](papers/paper-vi/Electroweak_Structure_as_a_Boundary_Projection_of_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-vi/paper-vi.tex))

Extends the projection framework to the electroweak sector. Gauge symmetry reinterpreted as torsional invariance under projection; mass as closure residual (photon = perfect closure, W/Z = incomplete closure); Weinberg angle as projection-induced rotation. Structurally preserves m_W = m_Z cos(θ_W). Higgs mechanism reinterpreted as closure stabilisation. Reinterpretation, not derivation — accommodates Standard Model structure within the φ-geometry, does not replace it. QCD and gravity flagged as future extensions.

#### Paper VII — Closure Dynamics and Constraints

**[Closure Dynamics and Constraint Operators in φ-Structured Geometry](papers/paper-vii/Closure_Dynamics_and_Constraint_Operators_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-vii/paper-vii.tex))

Formalises the closure operator that Papers V–VI assumed at a schematic level. Defines the admissible state space, three constraint classes (local, multi-node, projection), the closed state set, and the closure operator as metric projection. Introduces a variational formulation with closure functional. Proves existence in finite dimensions, addresses non-uniqueness via variational selection. Connects to mass (closure residual) and gauge structure (projection compatibility). Demonstrates non-arbitrariness of constraints. Mathematical framework paper — defines the machinery, not new predictions.

### Bridge Paper — From Dirac to Crystallisation

**[From Dirac Solutions to Physical Reality: A Crystallisation-Based Selection Architecture](papers/bridge-paper/From_Dirac_Solutions_to_Physical_Reality_A_Crystallisation_Based_Selection_Architecture.pdf)** ([LaTeX source](papers/bridge-paper/bridge-paper.tex))

Conceptual bridge paper connecting the Dirac equation to the crystallisation framework. The Dirac equation defines admissible relativistic quantum states but does not specify a selection mechanism; this paper proposes crystallisation as a deterministic, constraint-based selection architecture acting over a restricted admissible domain via a projected relaxation flow. Defines a schematic constraint functional, interprets candidate stable state classes, antiparticles, and (heuristically) annihilation within the framework. Extends rather than replaces Dirac/QM. Includes comparison to Copenhagen, GRW, and pilot-wave interpretations. The functional is schematic and not uniquely derived; Lorentz covariance, Born-rule recovery, and the operational protocol for F remain open.

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
│   ├── paper-vii/              Paper VII: closure dynamics and constraint operators
│   ├── paper-vi/               Paper VI: electroweak sector reinterpretation
│   ├── bridge-paper/           Dirac → Crystallisation bridge paper
│   ├── paper-v/                Paper V: complete particle mass spectrum
│   ├── pemr/                   Paper IV: bridge paper (proton-electron mass ratio)
│   ├── master-mass/            Paper I: closure geometry and mass (internal)
│   ├── lepton-generations/     Paper II: lepton generations + winding operator (internal)
│   ├── spectral-dimension/     Paper III: 600-cell eigenvalue + F4 spectral (internal)
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

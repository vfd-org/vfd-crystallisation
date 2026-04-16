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

This repository contains nine connected research tracks within the broader VFD programme:

1. **Crystallisation dynamics** — a deterministic, constraint-driven selection framework proposed as an alternative to probabilistic collapse in open quantum systems.
2. **The mass programme** — a geometric closure framework for particle mass ratios, developed through Papers I–V and anchored by Paper IV as the primary external-facing mass paper.
3. **The quantum recovery programme** — a sequence (Papers XV–XXI) showing that Schrödinger-type evolution emerges as the equilibrium tangent limit of a nonlinear closure-paired dynamics, without postulating quantum axioms.
4. **The spectral bridge** — Paper XXII connects all three tracks, showing that a single closure functional on the 600-cell can coherently relate mass eigenvalues, gauge structure, fundamental constants (α⁻¹ at 0.81 ppm, sin²θ_W = 3/8), and generation structure through the φ-permeability of the 600-cell geometry and the E₈ Coxeter projection.
5. **The general-relativity programme** — Papers XXIII–XXVII derive gravitational structure from event-order geometry. Starting from the birth-angle partial order on admissible overlap events, the sequence constructs time, observer kinematics, metric separation, curvature, and source-driven field dynamics without assuming spacetime.
6. **The unification bridge** — Paper XXVIII proposes that the quantum and gravitational tracks are two projections of a single underlying event-order geometry, sharing the same substrate (event set, closure functional, transition graph). The regime boundary is parameterised by the degree of constraint ordering.
7. **Observer placement** — Paper XXIX defines the observer as a bounded, stable, self-referential constraint substructure within the event-order geometry. Quantum measurement is mapped to constraint-induced stabilisation; relativistic frame dependence is mapped to observer embedding. The paper also identifies a structural locus for conscious experience within the dynamics, without claiming a full theory of consciousness.
8. **Probability and the Born rule** — Paper XXX addresses the Born-rule gap: why admissible outcomes have different probabilities and why those probabilities take the quadratic form P_i = |ψ_i|². Four candidate weighting routes are developed; the strongest shows that the Born measure is the stationary measure of the closure dynamics at equilibrium.
9. **Measurement dynamics** — Paper XXXI justifies the key assumption of Paper XXX by showing that measurement interactions dynamically deform the closure landscape, producing well-separated outcome basins with high barriers. Kramers-type transition suppression and cross-term vanishing follow from the barrier structure.

These tracks are related by a common structural theme: state resolution through constrained spectral structure. The crystallisation papers focus on general selection dynamics; the mass papers explore whether analogous closure geometry can organise particle mass structure; the quantum recovery programme derives quantum dynamics from closure; the spectral bridge (Paper XXII) connects them through computation; the GR programme (Papers XXIII–XXVII) separately reconstructs gravitational structure from the same event-order substrate; the unification bridge (Paper XXVIII) proposes that these two tracks admit a common structural interpretation; the observer placement paper (Paper XXIX) defines the observer's structural role across both regimes; and the Born-rule paper (Paper XXX) proposes that outcome probabilities emerge as geometric weights from the stationary measure of the closure dynamics; and the measurement paper (Paper XXXI) justifies the sector-separation assumption through dynamical landscape deformation.

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

### For the full programme (recommended starting point)
1. **Paper XXII** (spectral bridge — connects mass, dynamics, and gauge structure)

### For the quantum recovery programme
1. **Paper XXI** (synthesis — overview of Papers XV–XXI)
2. Paper XVII (dissipative obstruction — the core no-go result)
3. Paper XVIII (Nelson pairing — the mechanism)
4. Paper XIX (residual classification)
5. Paper XX (nonlinear quantum structure)
6. Papers XV–XVI (phase/interference and evolution equation — background)

### For the general-relativity programme (Papers XXIII–XXVII, labelled GR-I through GR-V)
1. **Paper XXIII / GR-I** (event structure and emergent time — the foundation)
2. **Paper XXIV / GR-II** (observer frames and relativity)
3. **Paper XXV / GR-III** (metric emergence — three constructions)
4. **Paper XXVI / GR-IV** (curvature from non-uniform geometry)
5. **Paper XXVII / GR-V** (dynamics and field equations — the capstone)

### For the unification bridge
1. **Paper XXVIII** (structural bridge between quantum and gravitational tracks)

### For observer placement
1. **Paper XXIX** (observer as constraint substructure — bridges QM measurement, GR frames, and consciousness locus)

### For measurement and probability (read in this order)
1. **Paper XXXI** (measurement as dynamical sector separation — justifies sector assumptions)
2. **Paper XXX** (probability as constraint geometry — Born rule from stationary measure of closure dynamics)

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

### Mass and Constraint-Manifold Programme (Papers I–XIII)

The repository contains a comprehensive constraint-geometry programme applying closure structure and spectral geometry to particle mass, force sectors, continuous geometry, dynamics, and interaction. The papers are listed below in sequential reading order.

#### Paper I (Internal) — Closure Geometry and Mass

**[Proton-to-Electron Mass Ratio from Closure Geometry and Graph Invariants](papers/master-mass/Proton_to_Electron_Mass_Ratio_from_Closure_Geometry_and_Graph_Invariants.pdf)** ([LaTeX source](papers/master-mass/master-mass.tex))

Internal development paper. Develops closure classes, assignment rules R1–R5, the combinatorial invariant, graph Laplacian term, degree-variance correction, and three-order mass law. Includes validation extensions (neutron compatible, muon/tau fail).

#### Paper II (Internal) — Lepton Generations

**[Lepton Generations and the Missing Mass Operator in Deterministic Field Closure](papers/lepton-generations/Lepton_Generations_the_Missing_Mass_Operator_in_Deterministic_Field_Closure.pdf)** ([LaTeX source](papers/lepton-generations/lepton-generations.tex))

No-go theorem for shell-extension leptons. Conditional winding operator f(w) = φ⁵(w−1)^(1/φ). Predicts muon to 0.5%, tau to 3.7%. 600-cell eigenvalue and F4 as external support from Paper III.

#### Paper III (Internal) — Spectral Structure

**[Spectral Structure of the 600-Cell Vertex Graph: Eigenvalue Connections and the F4 Fibonacci Extension](papers/spectral-dimension/Spectral_Structure_of_the_600_Cell_Vertex_Graph.pdf)** ([LaTeX source](papers/spectral-dimension/spectral-dimension.tex))

Exact 600-cell eigenvalue correspondence λ = 15 = ΔC. F4 convergence toward d_s ≈ φ (R² = 0.996). Includes retraction of earlier d_s ≈ 1.637 claim.

#### Paper IV — Proton–Electron Mass Ratio (Bridge Paper)

**[A φ-Scaled Geometric Ansatz for the Proton–Electron Mass Ratio](papers/pemr/A_phi_Scaled_Geometric_Ansatz_for_the_Proton_Electron_Mass_Ratio.pdf)** ([LaTeX source](papers/pemr/pemr.tex))

Standalone bridge paper. m_p/m_e = φ^(1265/81) ≈ 1835.8 with zero fitted parameters. ΔC = 15 as 600-cell Laplacian eigenvalue. Heat-kernel cumulant expansion. Zamolodchikov–Coldea E₈ precedent. Sensitivity analysis and 12-objection adversarial review. Externally readable.

#### Paper V — Particle-Mass Model

**[Toward a Spectral-Geometric Particle-Mass Model from the 600-Cell](papers/paper-v/Toward_a_Spectral_Geometric_Particle_Mass_Model_from_the_600_Cell.pdf)** ([LaTeX source](papers/paper-v/paper-v.tex))

Complete mass-spectrum extension. 13 non-reference particles from 600-cell eigenvalues {9, 12, 14, 15}. Average 0.014%. Fine structure constant (0.81 ppm). 6 exact graph theorems, correspondence chain, assignment rules, full epistemic classification.

#### Paper VI — Electroweak Sector

**[Electroweak Structure as a Boundary Projection of φ-Structured Geometry](papers/paper-vi/Electroweak_Structure_as_a_Boundary_Projection_of_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-vi/paper-vi.tex))

Electroweak reinterpretation. Gauge symmetry as torsional projection invariance. Mass as closure residual. Weinberg angle as projection rotation. m_W = m_Z cos(θ_W) preserved. Higgs as closure stabilisation. Reinterpretation, not derivation.

#### Paper VII — Closure Operators and Constraints

**[Closure Dynamics and Constraint Operators in φ-Structured Geometry](papers/paper-vii/Closure_Dynamics_and_Constraint_Operators_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-vii/paper-vii.tex))

Formalises the closure operator. Three constraint classes (local, multi-node, projection). Closed state set. Metric projection. Variational formulation. Connects to mass (closure residual) and gauge (projection compatibility). Mathematical machinery paper.

#### Paper VIII — Confinement

**[Confinement as a Multi-Node Closure Constraint in φ-Structured Geometry](papers/paper-viii/Confinement_as_a_Multi_Node_Closure_Constraint_in_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-viii/paper-viii.tex))

Confinement as connectivity constraint. Disconnected supports excluded by gap penalty. Proton {2,3,4} closure-stable; quark-like {2,4} is not. Composite closure functional with gap-penalty term. Emergent composite classes. Threefold baryon structure as colour analogue — SU(3) not derived.

#### Paper IX — Continuous Geometry

**[From Discrete Closure to Continuous Geometry in φ-Structured Constraint Systems](papers/paper-ix/From_Discrete_Closure_to_Continuous_Geometry_in_phi_Structured_Constraint_Systems.pdf)** ([LaTeX source](papers/paper-ix/paper-ix.tex))

Continuous limit of the discrete closure framework. Closed state set represented as constraint manifold M_cl. Induced Riemannian metric. Curvature from constraint interaction. Mass as distance from manifold, confinement as topology, gauge as orbit structure. Formal construction, not convergence theorem.

#### Paper X — Gravitational Analogy

**[Gravitational Analogy from Constraint-Manifold Curvature in φ-Structured Geometry](papers/paper-x/Gravitational_Analogy_from_Constraint_Manifold_Curvature_in_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-x/paper-x.tex))

Gravity-facing interpretation. Curvature of M_cl as structural analogue of gravitational geometry. Geodesic-like constrained motion on smooth strata. Geodesic deviation as tidal analogue. Local flatness as inertial-frame analogue. Full GR comparison table. Does NOT derive Einstein equations or identify M_cl with spacetime. Structural analogy — pathway, not destination.

#### Paper XI — Standard Model Correspondence

**[A Correspondence Between Constraint-Manifold Geometry and Standard Model Structure](papers/paper-xi/A_Correspondence_Between_Constraint_Manifold_Geometry_and_Standard_Model_Structure.pdf)** ([LaTeX source](papers/paper-xi/paper-xi.tex))

Translation layer. Systematic mapping table (18 rows): admissible states ↔ Hilbert space, constraint manifold ↔ physical states, projection invariance ↔ gauge symmetry, closure residual ↔ mass, connectivity ↔ confinement, curvature ↔ gravity (analogue). Each classified as structural, analogical, or open. Does not derive or replace the Standard Model.

#### Paper XII — Closure Dynamics

**[Closure Dynamics: A Variational and Gradient Formulation of Constraint-Manifold Evolution](papers/paper-xii/Closure_Dynamics_A_Variational_and_Gradient_Formulation_of_Constraint_Manifold_Evolution.pdf)** ([LaTeX source](papers/paper-xii/paper-xii.tex))

Minimal dynamics. Gradient flow of closure functional with monotonic descent. Closure-stable states as attractors. Lagrangian extension. Two modes: transverse (mass) and tangential (geometry). Evolution parameter t is auxiliary, not physical time.

#### Paper XIII — Interaction Dynamics

**[Interaction Dynamics and Basin Transitions in Constraint-Manifold Evolution](papers/paper-xiii/Interaction_Dynamics_and_Basin_Transitions_in_Constraint_Manifold_Evolution.pdf)** ([LaTeX source](papers/paper-xiii/paper-xiii.tex))

Multi-state interaction. Total closure functional F_tot = ΣF(ψ_i) + F_int(Ψ). Four interaction components: proximity, alignment, compatibility, binding. Coupled gradient flow. Interaction as basin deformation. Binding as joint attractor formation. Scattering-like basin transitions. Conservative Lagrangian extension. Structural interaction layer — no S-matrix, no QFT.

#### Paper XIV — Stochastic Closure Dynamics (Quantisation Layer)

**[Quantisation as Stochastic Closure Dynamics in φ-Structured Geometry](papers/paper-xiv/Quantisation_as_Stochastic_Closure_Dynamics_in_phi_Structured_Geometry.pdf)** ([LaTeX source](papers/paper-xiv/paper-xiv.tex))

Stochastic extension of deterministic closure dynamics. Langevin equation dψ = -∇F dt + σ dW on the closure landscape. Fokker-Planck equation with full derivation. Stationary distribution P ∝ exp(-2F/σ²) — proved, concentrates on M_cl. Local Gaussian approximation → excitation spectra from Hessian eigenvalues. Kramers barrier-crossing → transition rates. Onsager-Machlup path integral. Measurement as stochastic basin selection. Full QM comparison table (11 rows). Main theorem with 5 results. Does NOT claim QM equivalence — no unitarity, no interference, no Born rule derivation. Structural probabilistic layer from closure functional + noise.

### Quantum Recovery Programme (Papers XV–XXI)

The following sequence extends the closure dynamics of Papers XII–XIV toward quantum structure. Starting from dissipative gradient-flow dynamics, the programme constructs a layered route to Schrödinger-type evolution — not by postulating quantum axioms, but by deriving quantum structure from the closure framework. The central result is that the Schrödinger equation emerges as the equilibrium tangent limit of an exact nonlinear closure-paired dynamics.

#### Paper XV — Phase-Coherent Closure Dynamics

**[Phase-Coherent Closure Dynamics and the Emergence of Interference](papers/paper-xv/Phase_Coherent_Closure_Dynamics_and_the_Emergence_of_Interference.pdf)** ([LaTeX source](papers/paper-xv/paper-xv.tex))

Extends Papers XII–XIV from dissipative/real-valued dynamics to phase-bearing dynamics. Introduces a complexified Onsager–Machlup action as a minimal ansatz; phase-rotation frequency Ω = F/σ² and amplitude A = exp(−F/σ²) are fixed by internal consistency with Paper XIV. Interference proved (Proposition 5). Double-well worked example. Born-like |A|² structure as formulation feature (not derived as physical law). Does NOT claim QM equivalence. First phase-bearing layer of the closure programme.

#### Paper XVI — Closure Evolution Equation

**[Toward Unitary Closure Dynamics: Oscillatory Limits of the Complexified Closure Path Integral](papers/paper-xvi/Toward_Unitary_Closure_Dynamics_Oscillatory_Limits_of_the_Complexified_Closure_Path_Integral.pdf)** ([LaTeX source](papers/paper-xvi/paper-xvi.tex))

Derives the differential evolution equation generated by Paper XV's complexified path integral: ∂_tΨ = (σ²/2)ΔΨ − ∇F·∇Ψ + (i/σ²)FΨ. Identifies the structural gap: the kinetic term is real diffusion, not imaginary propagation. Drift-free form reveals operator structure as Euclidean QM plus imaginary potential. WKB transport regime with local modulus preservation. Identifies two-step complexification route toward Schrödinger form (formal).

#### Paper XVII — Dissipative Obstruction Theorem

**[The Dissipative Obstruction: Why Kolmogorov-Type Closure Generators Cannot Be Unitary and the Structure of Admissible Extensions](papers/paper-xvii/The_Dissipative_Obstruction_Why_Kolmogorov_Type_Closure_Generators_Cannot_Be_Unitary_and_the_Structure_of_Admissible_Extensions.pdf)** ([LaTeX source](papers/paper-xvii/paper-xvii.tex))

Proves that any generator L_BK + iM (backward Kolmogorov plus any imaginary potential) is dissipative in the equilibrium-weighted inner product — regardless of the choice of M. The obstruction sits in the kinetic sector: phase complexification alone cannot produce unitary evolution. Classifies three candidate routes past the obstruction: Hamiltonian lift (sufficient by construction), Nelson-type pairing (best derivation candidate), dual-generator decomposition (classificatory). Identifies Route B as the most natural continuation.

#### Paper XVIII — Nelson Pairing and Schrödinger Recovery

**[Nelson Pairing for Closure Dynamics: Schrödinger-Type Evolution from Forward and Backward Closure Processes](papers/paper-xviii/Nelson_Pairing_for_Closure_Dynamics_Schrodinger_Type_Evolution_from_Forward_and_Backward_Closure_Processes.pdf)** ([LaTeX source](papers/paper-xviii/paper-xviii.tex))

Carries out Route B from Paper XVII. Pairs the forward closure Langevin process with its time-reversal. Derives: exact continuity equation, automatically irrotational phase function (structural consequence of closure gradient drift), exact closure Madelung pair, exact nonlinear Schrödinger-type wave equation with imaginary kinetic term. At the Paper XIV equilibrium, the nonlinear potential evaluates exactly to give the Schrödinger equation with Witten Hamiltonian H_W; near equilibrium, this persists to leading order. Evades the XVII obstruction because the paired dynamics is not of the L_BK + iM form.

#### Paper XIX — Closure Residual Classification

**[The Closure Residual: Nonlinear Remainder Beyond the Witten-Hamiltonian Regime](papers/paper-xix/The_Closure_Residual_Nonlinear_Remainder_Beyond_the_Witten_Hamiltonian_Regime.pdf)** ([LaTeX source](papers/paper-xix/paper-xix.tex))

Isolates and classifies the nonlinear residual δU_rel = σ²(Δ|Ψ|/|Ψ| − ΔR_st/R_st) — the sole remaining discrepancy between the paired-process dynamics and linear Schrödinger. Proves: equilibrium vanishing, phase invariance, locality, amplitude homogeneity, near-equilibrium O(ε) scaling, exact L² norm conservation. Gauge non-removability by phase or linear-unitary transforms. Defines a residual-strength parameter Ξ classifying dynamics into linear Schrödinger, mixed, and nonlinear closure regimes.

#### Paper XX — Nonlinear Quantum Structure

**[The Closure Residual and Nonlinear Quantum Structure: Equilibrium Quantum Limit and Modulus-Curvature Nonlinearity](papers/paper-xx/The_Closure_Residual_and_Nonlinear_Quantum_Structure.pdf)** ([LaTeX source](papers/paper-xx/paper-xx.tex))

Places the closure residual into nonlinear Schrödinger structure. Defines the closure nonlinear operator N_cl and proves phase covariance, amplitude homogeneity, and equilibrium vanishing. Shows the linear Schrödinger equation is the Fréchet tangent dynamics at equilibrium — not the full closure dynamics, but the distinguished equilibrium tangent limit. Compares structurally with Madelung quantum potential and modulus-curvature NLS classes. The closure equation is a derived member of this class, with coefficient σ² and equilibrium subtraction 2V_W both fixed by the closure geometry, not introduced phenomenologically.

#### Paper XXI — Structural Synthesis

**[From Closure Dynamics to Quantum Structure: A Structural Synthesis of the Dissipative-to-Schrödinger Programme](papers/paper-xxi/From_Closure_Dynamics_to_Quantum_Structure.pdf)** ([LaTeX source](papers/paper-xxi/paper-xxi.tex))

Bridge/synthesis paper for the full XV–XX sequence. Summarises the five-stage construction: closure evolution equation → dissipative obstruction → Nelson pairing → residual isolation → structural classification. Central result: the Schrödinger equation appears as the distinguished equilibrium tangent sector of an exact nonlinear closure-paired dynamics. Explicitly states what is and is not established. Does not claim full quantum mechanics, measurement theory, or experimental predictions. Identifies the physical status of the nonlinear residual as the defining open question.

### Spectral Bridge (Paper XXII)

#### Paper XXII — The Standard Model from 600-Cell Closure Geometry

**[The Standard Model from 600-Cell Closure Geometry: Spectral Bridge, Structural Constants, and the φ-Permeability](papers/paper-xxii/The_Standard_Model_from_600_Cell_Closure_Geometry.pdf)** ([LaTeX source](papers/paper-xxii/paper-xxii.tex))

Bridges all three programme tracks through computation. Constructs an explicit H₄-invariant closure functional on the 600-cell. Computes the complete eigenvalue-representation map (9 eigenvalues, exact algebraic forms). Discovers the integer selection principle: Paper V's mass eigenvalues {9,12,14,15} are exactly the nontrivial integer Laplacian eigenvalues. Establishes the E₈ → H₄ Coxeter projection (240 roots → 120 vertices, 2:1 double cover). Exhibits structural correspondences with α⁻¹ = 137 + π/87 (0.81 ppm) and sin²θ_W = 3/8. Identifies φ-permeability (d₂²-d₁² = 1/φ) as the central geometric mechanism. Proves exact integer/irrational sector decoupling (94 physical modes). Seventeen verification scripts reproduce every computational claim. Does not claim to derive the Standard Model from first principles; presents evidence that a single closure functional can coherently relate mass, gauge structure, constants, and generation structure.

**Verification scripts** (in `papers/paper-xxii/scripts/`): 17 Python scripts covering spectral verification, Coxeter projection, coupling structure, α derivation, generation structure, φ-mass connection, SU(5) branching, UV analysis, and more. All require only `numpy` and `scipy`.

### General-Relativity Programme (Papers XXIII–XXVII)

The following sequence derives gravitational structure from event-order geometry — the partial order on admissible overlap events defined by the crystallisation framework. Starting from the birth-angle construction, the programme builds time, observer kinematics, metric separation, curvature, and source-driven field dynamics without assuming spacetime. The five papers are labelled GR-I through GR-V for easy reference.

| Label | Paper | Layer | Core construction |
|-------|-------|-------|-------------------|
| GR-I | XXIII | Time | Birth-angle partial order on admissible overlap events |
| GR-II | XXIV | Observers | Linear extensions + sampling measures → frame-dependent kinematics |
| GR-III | XXV | Metric | Three separation constructions (chain-length, observer-disagreement, transition-cost) |
| GR-IV | XXVI | Curvature | Non-uniformity of local accessibility profiles |
| GR-V | XXVII | Dynamics | Source-driven field equation via graph Laplacian |

#### Paper XXIII / GR-I — Event Structure and the Emergence of Time

**[Event Structure and the Emergence of Time from Phase-Overlap Geometry](papers/paper-xxiii/Event_Structure_and_the_Emergence_of_Time_from_Phase_Overlap_Geometry.pdf)** ([LaTeX source](papers/paper-xxiii/paper-xxiii.tex))

Defines admissible overlap events and the birth-angle partial order. Proves that no canonical global clock exists (non-uniqueness of linear extensions). Constructs chain time as intrinsic temporal separation. Pentagon worked example with 10 admissible events. Foundation for the GR programme.

#### Paper XXIV / GR-II — Observer Frames and Relativity

**[Observer Frames and Relativity from Event-Order Geometry](papers/paper-xxiv/Observer_Frames_and_Relativity_from_Event_Order_Geometry.pdf)** ([LaTeX source](papers/paper-xxiv/paper-xxiv.tex))

Defines observers as linear extensions of the partial order equipped with sampling measures. Proves simultaneity relativity (two observers generically disagree on simultaneous events). Exhibits time-dilation analogue. Separates chain time from observer elapsed time. Two-observer worked example on the pentagon model.

#### Paper XXV / GR-III — Metric Emergence

**[Metric Emergence from Event-Order Geometry](papers/paper-xxv/Metric_Emergence_from_Event_Order_Geometry.pdf)** ([LaTeX source](papers/paper-xxv/paper-xxv.tex))

Constructs three separation measures: chain-length (directed temporal separation), observer-disagreement (sign structure from frame comparisons), and transition-cost (genuine metric on the Hasse graph, proved). Comparison table with general-relativity analogues. Pentagon model computations for all three constructions.

#### Paper XXVI / GR-IV — Curvature from Non-Uniform Geometry

**[Curvature from Non-Uniform Event-Order Geometry](papers/paper-xxvi/Curvature_from_Non_Uniform_Event_Order_Geometry.pdf)** ([LaTeX source](papers/paper-xxvi/paper-xxvi.tex))

Defines flatness as local uniformity of neighborhood profiles. Three curvature indicators: volume-growth distortion, branching asymmetry (undirected degree), geodesic concentration (betweenness). Flat reference model (K_{5,5}: all indicators zero) and curved bottleneck model (all indicators nonzero). Curvature as departure from local uniformity.

#### Paper XXVII / GR-V — Dynamics and Field Equations

**[Dynamics and Field Equations from Event-Order Geometry](papers/paper-xxvii/Dynamics_and_Field_Equations_from_Event_Order_Geometry.pdf)** ([LaTeX source](papers/paper-xxvii/paper-xxvii.tex))

Capstone of the GR programme. Introduces source field S(e) from local event-content deviation, with density, overlap, and geodesic-traffic candidates compared. Graph-Laplacian field equation Δ_G u = S − S̄ with existence/uniqueness proved (Fredholm alternative). Global balance law and local flow conservation (discrete divergence theorem). Potential-gradient curvature K_pot. Three toy models: vacuum (flat), bottleneck (curved, geodesic concentration), perturbation (single-event geometric response). Source → curvature → geodesic bridge demonstrated explicitly. Does not derive the Einstein equations; establishes a discrete, principled analogue.

### Unification Bridge (Paper XXVIII)

#### Paper XXVIII — Quantum and Gravitational Structure from a Common Event-Order Geometry

**[Quantum and Gravitational Structure from a Common Event-Order Geometry](papers/paper-xxviii/Quantum_and_Gravitational_Structure_from_a_Common_Event_Order_Geometry.pdf)** ([LaTeX source](papers/paper-xxviii/paper-xxviii.tex))

Proposes that the quantum track (Papers XV–XXII) and the gravitational track (Papers XXIII–XXVII) are two projections of a single underlying event-order geometry. Identifies the shared substrate: the triple (E, F, G) — event set, closure functional, and transition graph — all derived from the dual 600-cell system. Presents a proposed structural correspondence table mapping objects across both tracks (path integrals ↔ geodesics, Witten Hamiltonian ↔ graph Laplacian, norm conservation ↔ source balance). Defines the ordering fraction η as a candidate regime-transition parameter. Reinterprets crystallisation as the geometric bridge between quantum multiplicity and gravitational order. Does not derive quantum gravity, the Einstein equations, or a continuum limit. Establishes a structural bridge, not a dynamical unification.

### Observer Placement (Paper XXIX)

#### Paper XXIX — Observer as Constraint: A Field-Theoretic Placement Across Quantum and Relativistic Regimes

**[Observer as Constraint: A Field-Theoretic Placement Across Quantum and Relativistic Regimes](papers/paper-xxix/Observer_as_Constraint.pdf)** ([LaTeX source](papers/paper-xxix/paper-xxix.tex))

Defines the observer as a bounded, dynamically stable, self-referential substructure within the event-order geometry, characterised by a constraint functional that enforces internal coherence. Quantum measurement is mapped to constraint-induced reduction of configuration multiplicity (not external collapse). Relativistic frame dependence is mapped to the observer's embedding within the event partial order. Gödel's theorems are correctly scoped to formal symbolic systems. Crystallisation and observer constraint are distinguished as global vs local mechanisms. A brief section identifies a structural locus for conscious experience (locatable, not explained). Does not derive the Born rule, a consciousness theory, or new experimental predictions. Placement paper: defines where the observer sits and what structural role it plays.

### Probability and the Born Rule (Paper XXX)

#### Paper XXX — Probability as Constraint Geometry: Toward a Derivation of the Born Rule

**[Probability as Constraint Geometry: Toward a Derivation of the Born Rule](papers/paper-xxx/Probability_as_Constraint_Geometry.pdf)** ([LaTeX source](papers/paper-xxx/paper-xxx.tex))

Addresses the Born-rule gap left by Paper XXIX: admissibility determines which outcomes are possible, but not their relative frequencies. Develops four candidate weighting routes: basin-volume measure, stability-depth weighting, stationary-measure inheritance from the Paper XIV equilibrium distribution, and a Gleason-type argument. The strongest result (Proposition 1): at the Paper XIV equilibrium, the Nelson wavefunction satisfies |Ψ|² = ρ = P_st, so the Born measure IS the stationary measure of the closure dynamics, yielding P_i = |c_i|² under stated assumptions. Routes C (dynamical origin) and D (structural uniqueness via Gleason) are complementary. Two-basin toy model demonstrates the mechanism explicitly. Does not claim a complete derivation; identifies a candidate substrate explanation with explicit assumptions and open problems.

### Measurement Dynamics (Paper XXXI)

#### Paper XXXI — Measurement as Dynamical Sector Separation in Closure Dynamics

**[Measurement as Dynamical Sector Separation in Closure Dynamics](papers/paper-xxxi/Measurement_as_Dynamical_Sector_Separation_in_Closure_Dynamics.pdf)** ([LaTeX source](papers/paper-xxxi/paper-xxxi.tex))

Justifies the key assumption of Paper XXX: that measurement produces well-separated outcome sectors. Defines measurement-type interactions as couplings that energetically favour correlated system-apparatus configurations. Shows such interactions deform the closure landscape from single-basin to multi-basin with high barriers (Proposition 1). Kramers-type transition suppression exp(-2ΔF/σ²) follows when barrier height exceeds noise strength. Cross-term suppression and outcome stability derived from the same barrier mechanism. Toy model: system with double-well potential coupled to single-well apparatus; coupling splits landscape into two separated basins with barrier proportional to coupling strength. Timescale hierarchy (separation < relaxation < observation) treated as working hypothesis. Structural comparison to standard decoherence (analogous but does not require environmental tracing). Does not claim a complete measurement solution; provides a dynamical route from interaction to sector separation.

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
│   ├── paper-xxxi/             Paper XXXI: measurement as dynamical sector separation
│   ├── paper-xxx/              Paper XXX: probability as constraint geometry (Born rule)
│   ├── paper-xxix/             Paper XXIX: observer as constraint (placement across regimes)
│   ├── paper-xxviii/           Paper XXVIII: unification bridge (quantum ↔ gravitational)
│   ├── paper-xxvii/            Paper XXVII / GR-V:  dynamics and field equations (capstone)
│   ├── paper-xxvi/             Paper XXVI  / GR-IV: curvature from non-uniform geometry
│   ├── paper-xxv/              Paper XXV   / GR-III: metric emergence (three constructions)
│   ├── paper-xxiv/             Paper XXIV  / GR-II: observer frames and relativity
│   ├── paper-xxiii/            Paper XXIII / GR-I:  event structure and emergent time
│   ├── paper-xxii/             Paper XXII: spectral bridge (600-cell → SM structure) + 17 scripts
│   ├── paper-xxi/              Paper XXI: structural synthesis (dissipative → Schrödinger)
│   ├── paper-xx/               Paper XX: nonlinear quantum structure
│   ├── paper-xix/              Paper XIX: closure residual classification
│   ├── paper-xviii/            Paper XVIII: Nelson pairing and Schrödinger recovery
│   ├── paper-xvii/             Paper XVII: dissipative obstruction theorem
│   ├── paper-xvi/              Paper XVI: closure evolution equation
│   ├── paper-xv/               Paper XV: phase-coherent dynamics (interference)
│   ├── paper-xiv/              Paper XIV: stochastic closure dynamics (quantisation)
│   ├── paper-xiii/             Paper XIII: interaction dynamics and basin transitions
│   ├── paper-xii/              Paper XII: closure dynamics (gradient flow + Lagrangian)
│   ├── paper-xi/               Paper XI: Standard Model correspondence / translation layer
│   ├── paper-x/                Paper X: gravitational analogy from constraint-manifold curvature
│   ├── paper-ix/               Paper IX: continuous limit and constraint-manifold geometry
│   ├── paper-viii/             Paper VIII: confinement as closure constraint
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
| **Quantum recovery** | Schrödinger-type dynamics emerges as the equilibrium tangent limit of a nonlinear closure-paired dynamics | Papers XVII–XXI |
| **No-go** | Single-generator Kolmogorov-type closure dynamics cannot be unitary (proved) | Paper XVII |
| **Spectral bridge** | Integer selection principle, exact sector decoupling, structural correspondences with α⁻¹ and sin²θ_W | Paper XXII |
| **GR programme** | Time, observers, metric, curvature, and source-driven field dynamics derived from event-order geometry without assuming spacetime | Papers XXIII–XXVII |
| **Unification bridge** | Quantum and gravitational tracks proposed as two projections of a single event-order geometry, with shared substrate and structural correspondence | Paper XXVIII |
| **Observer placement** | Observer defined as bounded, stable, self-referential constraint substructure; QM measurement and GR frames unified as constraint mechanisms | Paper XXIX |
| **Born rule** | Outcome probabilities proposed as geometric weights from stationary measure of closure dynamics; Born-like P_i = \|c_i\|² under equilibrium assumptions | Paper XXX |
| **Measurement dynamics** | Measurement interactions dynamically deform closure landscape into well-separated basins; justifies sector-separation assumption of Paper XXX | Paper XXXI |

The framework does not claim to replace quantum mechanics. It proposes a testable extension and provides the tools to evaluate it. The quantum recovery programme (Papers XV–XXI) establishes a mathematical pathway from dissipative closure dynamics to Schrödinger-type evolution but does not claim full quantum mechanics, measurement theory, or experimental predictions from the nonlinear residual.

---

## How to Cite

For citation metadata, see [`CITATION.cff`](CITATION.cff).

When referencing the core framework, cite the flagship paper:

> Lee Smart, "Crystallisation Dynamics as a Deterministic Alternative to Collapse in Open Quantum Systems," Preprint, Institute of Vibrational Field Dynamics, 2026.

---

## License

MIT. See [`LICENSE`](LICENSE) for details.

Code and documentation are covered by the MIT licence. Paper source files (`.tex`) are included for reproducibility; if reusing paper content beyond code, please cite appropriately.

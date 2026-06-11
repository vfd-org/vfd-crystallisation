# Tracing the Full VFD Dynamical Chain
## From the Closure Functional to Loop Corrections — No SM Imports

**Date:** 2026-04-16  
**Purpose:** Map every step from F to observables using only VFD constructions.  
**Rule:** The Standard Model is a CHECKPOINT, not an INPUT.

---

## The Single Root: The 600-Cell Closure Functional

Everything grows from one object:

$$
\mathcal{F}(x) = -\varepsilon^2 \log\!\left(\sum_{i=1}^{120} \exp\!\left(-\frac{|x - v_i|^2}{2\varepsilon^2}\right)\right)
$$

where {v₁,...,v₁₂₀} are the 600-cell vertices on S³ and ε is the
smoothing parameter.

**Properties (Paper XXII, Prop. 1):**
- F(v_i) = 0 at every vertex (constraint-satisfied configurations)
- F(x) > 0 away from vertices (constraint violation)
- H₄-invariant (600-cell symmetry preserved)
- C∞ smooth
- Uniform Hessian at each vertex (by vertex-transitivity)
- Barrier height d²/(4ε²) between adjacent vertices

**ε is NOT a free parameter.** It is the structural scale that controls
the barrier between adjacent configurations. Physically: ε determines
which transitions are accessible at a given energy scale.

---

## Level 0: The Geometry (no dynamics yet)

### 0a. The 600-cell graph

F defines a landscape on R⁴ with 120 minima (the vertices). The
connectivity is given by the vertex adjacency graph:
- 120 vertices, each connected to 12 nearest neighbours
- NN distance d₁ = 1/φ, NNN distance d₂ = 1
- Permeability gap: d₂² - d₁² = 1/φ

### 0b. The spectral decomposition

The adjacency matrix A₆₀₀ commutes with the 2I action. Its eigenvalues
partition into irreps:

| Irrep | dim | mult | Adj. eigenvalue | Lap. eigenvalue | Integer? |
|-------|-----|------|-----------------|-----------------|----------|
| 1     | 1   | 1    | 12              | 0               | Yes      |
| 2     | 2   | 4    | 3+3√5           | 9-3√5           | No       |
| 3     | 3   | 9    | 2+2√5           | 10-2√5          | No       |
| **4** | 4   | 16   | 3               | **9**           | **Yes**  |
| **5** | 5   | 25   | 0               | **12**          | **Yes**  |
| **6** | 6   | 36   | -2              | **14**          | **Yes**  |
| 3'    | 3   | 9    | 2-2√5           | 10+2√5          | No       |
| **4'**| 4   | 16   | -3              | **15**          | **Yes**  |
| 2'    | 2   | 4    | 3-3√5           | 9+3√5           | No       |

The integer eigenvalues {9, 12, 14, 15} form a closed sector (Paper
XXII, Theorem [Exact decoupling]). Total: 16+25+36+16 = 93 modes.

### 0c. The Hopf fiber decomposition

The 120 vertices decompose under the Hopf fibration S³ → S² into 12
decagonal great circles C₁₀, each with 10 vertices.

C₁₀ eigenvalues: E_k = 2 - 2cos(2πk/10)
= {0, 1/φ², 1/φ², 3-φ, 3-φ, φ², φ², 2+φ, 2+φ, 4}

Spectral gap: E₁(C₁₀) = φ⁻² (same as λ₁(P₅))

### 0d. The shell manifold

Nested shells at r_n = r₀φ⁻ⁿ, n = 1,...,5. Support graph G_amb = P₅.
Spectral gap: λ₁(P₅) = 2 - 2cos(π/5) = φ⁻².

**Checkpoint:** φ⁻² appears in three independent geometric structures
(P₅, C₁₀, and d₁²). This is not a coincidence — all encode π/5 = 36°,
the fundamental icosahedral angle.

---

## Level 1: The Stationary-Point Physics

### 1a. Mass from the heat kernel (Papers I-V)

The heat kernel Z(t) = Tr(e^{-tL}) on the support graph G(S) encodes
the mass through the cumulant expansion:

$$
\ln(m/m_{ref}) = [\Delta C + |E|/|V| - \text{Var}(\deg)|E|/|V|^2 + \cdots] \times \ln\varphi
$$

For proton: φ^{1265/81} ≈ 1835.8 (0.02% error).

### 1b. Charge radius from the resolvent (this work)

The resolvent R(z) = (I + zL)⁻¹ at the boundary vertex gives:

$$
r = \sqrt{12 \times \text{Tr}(L)/|V|} \times \lambdabar
$$

For proton: r = 4λ̄_p = 0.841 fm (0.04% error).

### 1c. Coupling constants from eigenvalue algebra (Paper XXII)

$$
\alpha^{-1} = (\lambda_1 - 1)(\lambda_2 - 1) - 1 + \sum \lambda_i = 87 + 50 = 137
$$

### 1d. Gauge structure from projection invariance (Papers VI-VII)

Torsional transformations T_θ: ψ → e^{iθG}ψ that preserve the
projection P are identified as gauge symmetries:

P(T_θ ψ) = P(ψ) for all admissible ψ

The gauge group emerges as the group of projection-compatible
torsional transformations — NOT postulated, but identified from the
constraint structure.

### 1e. Weinberg angle from eigenvalue ratio (Paper XXII)

$$
\sin^2\theta_W = \frac{\lambda_1}{\lambda_1 + \lambda_4} = \frac{9}{9+15} = \frac{3}{8}
$$

This is the NN/NNN angular ratio: 36°/60° = 3/5, giving 3/(3+5) = 3/8.

**Checkpoint:** All Level 1 results use ONLY the stationary points of F
(the vertices and their spectral structure). No dynamics yet.

---

## Level 2: The Dynamics

### 2a. Gradient flow (Paper XII)

$$
\frac{d\psi}{dt} = -\nabla\mathcal{F}(\psi)
$$

This drives the system toward closure (F = 0). Monotonic descent:
dF/dt = -||∇F||² ≤ 0.

### 2b. Stochastic extension (Paper XIV)

$$
d\psi = -\nabla\mathcal{F}\,dt + \sigma\,dW
$$

with stationary distribution P_st(ψ) ∝ exp(-2F/σ²).

σ² = ℏ/m is the noise amplitude (Paper XXII unit matching).

### 2c. The dissipative obstruction (Paper XVII)

**Theorem:** Any generator of the form L_BK + iM (backward Kolmogorov
plus imaginary potential) is DISSIPATIVE. Phase complexification alone
cannot produce unitary evolution.

This means: you CANNOT get quantum mechanics from just adding a phase
to the classical dynamics. You need something more.

### 2d. Nelson pairing (Paper XVIII)

The resolution: pair forward and backward closure processes.

Forward: dψ = b₊ dt + σ dW⁺, b₊ = -∇F
Backward: b₋ = -∇F - σ²∇log ρ

This produces the Nelson wavefunction:
Ψ_N = √ρ × e^{iS/σ²}

with phase S = -F - (σ²/2)log ρ

### 2e. The nonlinear wave equation (Paper XVIII)

The pairing produces:

$$
i\sigma^2 \partial_t \Psi = -\frac{\sigma^4}{2}\Delta\Psi + U[\Psi]\Psi
$$

where U[Ψ] = -σ²V_W + σ⁴(Δ|Ψ|/|Ψ|).

**This is NOT the Schrödinger equation.** It's nonlinear (U depends on Ψ).
The imaginary kinetic term -σ⁴Δ/2 emerges from the pairing — it
EVADES the dissipative obstruction because paired dynamics ≠ L_BK + iM.

### 2f. The Witten Hamiltonian (Paper XVIII)

Rewrite as: i∂_tΨ = H_W Ψ + δU_rel[Ψ]Ψ

where:
- H_W = -(σ²/2)Δ + V_W [the linear part]
- V_W = |∇F|²/(2σ²) - ΔF/2 [the Witten potential, fixed by F]
- δU_rel = σ²(Δ|Ψ|/|Ψ| - ΔR_st/R_st) [the nonlinear residual]

At equilibrium: δU_rel = 0 → i∂_tΨ = H_WΨ (Schrödinger equation).

**Checkpoint:** The Schrödinger equation is NOT a postulate. It's the
linearization of the full nonlinear closure dynamics at the equilibrium
fixed point. It holds when the system is near equilibrium (Ξ << 1).

---

## Level 3: The Loop Structure (the frontier)

### 3a. What the closure residual IS

$$
\delta U_{rel}[\Psi] = \sigma^2\left(\frac{\Delta|\Psi|}{|\Psi|} - \frac{\Delta R_{st}}{R_{st}}\right)
$$

This is the DIFFERENCE between:
- The actual modulus curvature (Δ|Ψ|/|Ψ|)
- The equilibrium modulus curvature (ΔR_st/R_st = 2V_W/σ²)

Properties (Papers XIX-XX):
- Phase-invariant: depends only on |Ψ|, not on arg(Ψ)
- Local: depends only on |Ψ|, ∇|Ψ|, Δ|Ψ| at each point
- Zero at equilibrium: δU_rel[Ψ_st] = 0
- Near equilibrium: δU_rel = O(ε) for Ψ = Ψ_st(1+εη)
- Norm-conserving: d/dt ∫|Ψ|² = 0 (exact, even for nonlinear equation)

### 3b. What δU_rel does physically

When the system is perturbed from equilibrium (by an external field,
by thermal fluctuations, by measurement), the modulus |Ψ| deviates from
R_st. The residual δU_rel measures this deviation and feeds it back
into the dynamics.

**In QED language:** δU_rel IS the vertex correction. When an external
electromagnetic field perturbs the electron/muon state, δU_rel gives
the correction to the interaction vertex.

In QED, this correction comes from a loop integral over virtual photons.
In VFD, it comes from the modulus-curvature response of the closure
state to the perturbation. The SAME physical effect (anomalous magnetic
moment, running couplings) but through a different mathematical route.

### 3c. The critical observation: the 600-cell IS the regulator

In QED, loop integrals diverge and must be regularised (cutoff, dimensional
regularisation, etc.). In VFD, the closure functional lives on the 600-cell,
which has FINITE vertices (120). The "loop integral" becomes a finite sum:

$$
\text{QED: } \int \frac{d^4k}{(2\pi)^4} \to \text{VFD: } \frac{1}{120}\sum_{i=1}^{120}
$$

No UV divergence. No regularisation needed. The 600-cell IS the regulator.

The 94 integer-eigenvalue modes form a closed sector (exact decoupling
theorem). The sum over these 94 modes gives the physical result. The
26 irrational-eigenvalue modes decouple exactly.

### 3d. The energy scale as barrier height

In QED, the energy scale μ appears in the logarithm of the running:
α(μ) = α(μ₀) / [1 + b α(μ₀) ln(μ/μ₀)]

In VFD, the energy scale is the smoothing parameter ε of the closure
functional:
- Large ε: all barriers are transparent → all modes contribute
  → high energy
- Small ε: only NN transitions → only low-lying modes
  → low energy

The running of α with ε:
$$
\alpha^{-1}(\varepsilon) = [\text{eigenvalue algebra restricted to modes accessible at scale } \varepsilon]
$$

At the structural scale (ε → 0): all integer eigenvalues contribute
→ α⁻¹ = 137 + π/87 (the full result of Paper XXII).

At lower scales: fewer modes contribute → α⁻¹ changes.

**This is the VFD β-function.** It comes from the ε-dependence of the
eigenvalue algebra, NOT from borrowed SM β-function coefficients.

---

## Level 3 Computations: What Needs to Be Done

### Computation A: The (g-2) Vertex Correction

**Input:** The 600-cell closure functional F, a uniform magnetic field B.

**Step 1:** Construct the 120×120 system
- 600-cell vertex coordinates v_i ∈ R⁴
- Adjacency matrix A₆₀₀
- Laplacian L = 12I - A

**Step 2:** The equilibrium state
- R_st(v_i) ∝ exp(-F(v_i)/σ²) = constant (by vertex-transitivity)
- ∇log R_st = 0 at every vertex (stationary points)

**Step 3:** The magnetic perturbation
- External field couples through minimal coupling:
  A_field(v_i) = (B × r_i)/2 (where r_i is the 4D position of vertex i)
- Perturbed state: Ψ = R_st × e^{iS} where S includes the magnetic phase
- The magnetic phase at vertex i: φ_i = (e/ℏc) ∫ A·dl

**Step 4:** The perturbed modulus
- |Ψ(v_i)| = R_st × |1 + εη_i| where η_i encodes the response
- At leading order: |Ψ| = R_st(1 + ε Re(η_i))

**Step 5:** The graph Laplacian of the perturbation
- Δ Re(η)(v_i) = Σ_{j~i} [Re(η_j) - Re(η_i)]
- This is a 120×120 matrix-vector product

**Step 6:** The closure residual
- δU_rel = σ² × Δ Re(η) (since ∇log R_st = 0 at vertices)
- This is explicitly computable once η is known

**Step 7:** The anomalous magnetic moment
- a = ⟨δU_rel⟩_spin / (2μ_B B)
- Extract the part of ⟨δU_rel⟩ proportional to S·B

**What this computation requires:**
- The 600-cell vertex coordinates (standard mathematical object)
- The magnetic response η (computed from the resolvent of H_W)
- The graph Laplacian action on η (120×120 matrix product)
- Projection onto the spin-dependent part

This is ~200 lines of numpy code. Each step is well-defined.

### Computation B: The VFD β-Function

**Input:** The 600-cell closure functional F, the smoothing parameter ε.

**Step 1:** For each value of ε, determine which modes are accessible
- Barrier height between adjacent vertices: F_barrier(ε) = d₁²/(4ε²)
- Tunneling amplitude: t(ε) = exp(-F_barrier/σ²)
- At energy scale μ ~ t(ε): modes with eigenvalue gap < μ are accessible

**Step 2:** The scale-dependent eigenvalue algebra
- At full scale: all integer eigenvalues {9, 12, 14, 15} contribute
  → α⁻¹ = 137 + π/87
- At lower scale: only the lowest eigenvalues contribute
  → α⁻¹ = ??? (to be computed)

**Step 3:** The running
- Compute α⁻¹(ε) for a range of ε values
- The β-function: b = d(α⁻¹)/d(ln ε)

**Step 4:** The Weinberg angle running
- Similarly: sin²θ_W(ε) = [eigenvalue ratio at scale ε]
- Run from the structural scale to the electroweak scale

**What this computation requires:**
- The eigenvalue algebra as a function of included modes
- The barrier heights and tunneling amplitudes
- A model for which modes are "accessible" at each scale

This is conceptually simpler than the (g-2) computation but requires
more theoretical input (the scale-dependent mode selection).

---

## The Priority Order

1. **Build the 600-cell vertex graph** (prerequisite for everything)
   - 120 vertex coordinates in R⁴
   - 120×120 adjacency matrix
   - Verify eigenvalues match Paper XXII

2. **Compute the (g-2) vertex correction** (most impactful)
   - The magnetic perturbation on the graph
   - The closure residual response
   - Extract the anomalous magnetic moment
   - Compare to α/(2π)

3. **Compute the VFD β-function** (most novel)
   - Scale-dependent mode counting
   - Running of α⁻¹ with ε
   - Running of sin²θ_W with ε
   - Compare to experiment at the Z-pole

Each step builds on the previous. No shortcuts. No SM imports.
The 600-cell closure functional F is the only input.

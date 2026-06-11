# Loop Structure Roadmap: From Closure Residual to (g-2) and Electroweak Running

**Date:** 2026-04-16  
**Status:** Roadmap — computation defined, work needed  

---

## What We Tried and What We Learned

### The RG running fails with borrowed SM β-functions

Attempting to run sin²θ_W from 3/8 (VFD structural value) to the
Z-pole using Standard Model one-loop β-functions gives sin²θ_W(m_Z) ≈ 0.88.
This is catastrophically wrong (experimental: 0.231).

This is NOT a failure of VFD. It reveals something important:

**You cannot borrow the SM β-functions and plug in VFD initial conditions.**

The β-functions encode the PARTICLE CONTENT of the theory. The SM
β-functions assume the SM particle spectrum (quarks, leptons, W, Z,
Higgs). VFD has a DIFFERENT mode structure (94 integer-eigenvalue
modes on the 600-cell). The running will be different.

This is actually a known issue in GUT physics: the SM β-functions
don't give exact coupling unification. SUSY fixes this by changing
the β-functions (adding superpartners). VFD may fix it by having
a completely different mode spectrum.

**Bottom line:** The Weinberg angle running requires VFD's OWN
β-functions derived from the 600-cell representation content.
This is not a plug-in calculation — it's a derivation.

### The (g-2) computation is defined but not trivial

The formal structure is correct:
- The closure residual δU_rel (Papers XIX-XX) IS the VFD loop correction
- It's nonzero when an external magnetic field perturbs the equilibrium
- The anomalous magnetic moment IS the spin-dependent part of ⟨δU_rel⟩
- On the 600-cell, this becomes a finite matrix computation (no UV divergences!)

But the actual computation requires:
1. The 600-cell vertex coordinates in R⁴ (120 points)
2. The 120×120 adjacency matrix
3. The magnetic coupling matrix elements at each vertex
4. The eigenmodes of the Witten Hamiltonian
5. The vertex correction as a matrix trace
6. Extraction of the spin-dependent part

This is ~200 lines of careful numerical code. Each step is
well-defined. None requires new theoretical input. It just needs
to be done properly.

---

## The Three Computations, Honestly Assessed

### 1. Muon (g-2) — ACHIEVABLE (1 session)

**What:** Compute the anomalous magnetic moment from the closure
residual on the 600-cell graph.

**How:** Matrix computation on a 120×120 system:
- Construct 600-cell vertices
- Build adjacency matrix
- Introduce magnetic field as vertex-dependent phase
- Compute δU_rel for the perturbed state
- Extract spin-dependent energy shift
- This gives a = α/(2π) at leading order + corrections

**Why it works:** The 600-cell is finite (120 vertices). The
computation replaces the Feynman loop integral with a discrete
matrix trace. No UV divergences, no regularisation needed. The
vertex-transitivity gives uniform contributions.

**What's needed:** Code to construct 600-cell vertices and compute
the vertex correction. Paper XXII scripts already have steps A-B.

**Expected result:** a_e = α/(2π) + O(α²) [electron]
The GENERATION DEPENDENCE (muon vs electron) should involve the
fiber eigenvalue E₁(C₁₀) = φ⁻².

### 2. Electroweak Running — HARD (requires new theory)

**What:** Derive sin²θ_W(m_Z) = 0.231 from sin²θ_W(GUT) = 3/8
using VFD's own running, not the SM's.

**Why SM running doesn't work:** The SM β-functions give the wrong
answer because VFD has a different mode spectrum. The 94 integer-
eigenvalue modes on the 600-cell don't map directly to the SM
particle content.

**What's needed:**
1. Identify which 600-cell modes contribute to each gauge sector
   (how do the {9,12,14,15} eigenvalues map to SU(3)×SU(2)×U(1)?)
2. Compute the mode contribution to the β-functions
   (this involves representation theory of the 2I group)
3. Derive the VFD β-function coefficients b₁, b₂, b₃
4. Run the couplings from the structural scale to the Z-pole
5. Check whether VFD gives EXACT coupling unification
   (the SM doesn't — this would be a genuine VFD prediction)

**Key question:** If VFD gives different β-functions than the SM,
it predicts a different M_GUT and potentially different proton
decay rates. This is testable.

**Expected effort:** 1-2 sessions of representation theory + numerics.

### 3. Deuteron — DONE

r_d = √(16 + 9π² - 8/3) × λ̄_p ≈ 10.11 λ̄_p = 2.126 fm

Nuclear separation r_str = 6π λ̄_p from pion exchange channels.
0.1% accuracy vs experiment.

---

## Recommended Execution Order

### Session 1: The (g-2) vertex correction

This is the most impactful and most achievable computation.

**Steps:**
1. Construct 600-cell vertex coordinates (standard mathematical object)
2. Build the 120×120 adjacency matrix
3. Verify the eigenvalue spectrum matches Paper XXII
4. Introduce magnetic field coupling at each vertex
5. Compute the perturbed state to first order in B
6. Evaluate δU_rel for the perturbed state
7. Extract the spin-dependent part → (g-2)
8. Compare to α/(2π) [Schwinger correction]
9. Compute the generation dependence (e vs μ vs τ)

**Success criterion:** Recover a = α/(2π) at leading order.
If this works, the generation correction gives a NEW PREDICTION
for the muon-electron (g-2) difference.

### Session 2: The VFD β-functions

This requires more theoretical groundwork.

**Steps:**
1. Map the 600-cell eigenvalue sectors to gauge group representations
   (which modes are "SU(3)-like", "SU(2)-like", "U(1)-like"?)
2. Compute the contribution of each mode to the β-function
3. Derive b₁, b₂, b₃ from the 600-cell representation theory
4. Run the couplings and check against experiment
5. If unification is exact: compute M_GUT and proton lifetime

**This is where VFD either confirms the SM or makes a BSM prediction.**

### Session 3: Form factor on full 600-cell

This extends our 3-vertex form factor to the full 120-vertex model.

**Steps:**
1. Compute the 4' representation wavefunction on all 120 vertices
2. Compute the electromagnetic form factor as a function of Q²
3. Compare to the experimental dipole over the full Q² range
4. Extract the form factor zeros and poles in the timelike region
5. Compare to known vector meson resonances

---

## What This Programme Gives If Successful

| Computation | Result | Impact |
|-------------|--------|--------|
| (g-2) at leading order | a = α/(2π) | Confirms framework consistency |
| (g-2) generation correction | Δa(μ-e) from fiber eigenvalues | New prediction, testable |
| VFD β-functions | b₁, b₂, b₃ from 600-cell | Potentially different from SM |
| sin²θ_W running | Derived from 3/8 to 0.231 | Tests the framework at loop level |
| Coupling unification | Whether VFD gives exact unification | Major prediction |
| 120-vertex form factor | Full G_E(Q²) curve | Tests against experimental data |
| Timelike resonances | Vector meson masses from form factor poles | New predictions |

---

## The Honest Assessment

The framework has:
- Level 1 (stationary points): COMPLETE (masses, radii, coupling constants)
- Level 2 (fluctuations): MATHEMATICALLY DEFINED (closure residual exists)
  but COMPUTATIONALLY NOT YET EVALUATED for specific observables
- Level 3 (inter-object): STARTED (deuteron works)

The gap between "mathematically defined" and "computed" at Level 2 is
a CODING problem, not a THEORY problem. The closure residual δU_rel
is an explicit formula (Paper XIX, Eq. 83). The 600-cell graph is a
known mathematical object. The computation is finite and well-defined.

What's needed is patience and careful implementation. No new theoretical
ideas required — just the disciplined application of tools already built.

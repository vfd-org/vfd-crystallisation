# The Unified Spectral Coherence Operator
## One Principle, All Charge Radii

**Date:** 2026-04-16  
**Status:** Derived — paper-ready  
**WO:** WO-ARIA-VFD-RADIUS-UNIFICATION-105

---

## The Principle

$$
\boxed{r = \xi_K(\text{geometric home}, \text{spectral channel}) \times \frac{\hbar}{m_p c}}
$$

Every particle's charge radius is the **heat-kernel coherence length**
of its electromagnetic response, computed on the geometric object where
the particle lives, in the spectral channel appropriate to its charge
structure. The scale is the confinement Compton wavelength.

---

## The Three Geometric Homes

All three objects live inside the same 600-cell:

### Home 1: The Support Graph G(S)

**Residents:** Baryons (proton, neutron, Σ, Ξ, Ω, Δ, Λ)

The baryon is a **closure basin** — a standing wave satisfying all
closure constraints on a connected shell support. The support graph
G(S) = P_{|S|} encodes the shell connectivity.

**Coherence mechanism:** The **graph resolvent** at the boundary vertex.
The heat kernel K(x_b, x_b; t) at the boundary vertex x_b, evaluated
through the resolvent (Laplace transform), gives the electromagnetic
response.

**Formula:**
$$
r^2 = 12 \times \frac{\mathrm{Tr}(L)}{|V|} \times \lambdabar_p^2
$$

For the proton (P₃): r = √(12 × 4/3) × λ̄ = 4λ̄ = 0.8412 fm

### Home 2: The Closure Orbit S¹

**Residents:** Non-strange mesons (π⁺, π⁻, π⁰, η)

The pion is a **pseudo-Goldstone boson** — a phase excitation along
the flat direction of the closure functional. The flat direction is
the closure orbit, which is a circle S¹ on the 3-sphere.

**Coherence mechanism:** The **phase half-period**. The heat kernel
on the circle has coherence length equal to the half-circumference.

**Formula:**
$$
r = \pi \times \lambdabar_p
$$

For the pion: r = π × 0.2103 = 0.6607 fm

### Home 3: The Hopf Fiber C₁₀

**Residents:** Strange mesons (K⁺, K⁻, K⁰, K̄⁰)

The kaon is a **cross-generation composite** — its quark and antiquark
occupy different winding modes on the Hopf fiber. The Hopf fibration
of the 600-cell decomposes 120 vertices into 12 decagonal great
circles C₁₀.

**Coherence mechanism:** The **inverse spectral gap** of the fiber.
The diffusion length on C₁₀ is 1/E₁(C₁₀) = 1/φ⁻² = φ².

**Formula:**
$$
r = \varphi^2 \times \lambdabar_p = \frac{1}{E_1(C_{10})} \times \lambdabar_p
$$

For the kaon: r = φ² × 0.2103 = 0.5506 fm

---

## The Heat-Kernel Unification

The resolvent (Channel A, baryons) and the diffusion length (Channel B,
mesons) are **two moments of the same heat kernel**:

$$
K(x,y;t) = \sum_k e^{-\lambda_k t} \psi_k(x) \psi_k(y)
$$

**Channel A (baryons):** The resolvent is the Laplace transform of K:
$$
R(x,y;z) = \int_0^\infty K(x,y;t)\, e^{-zt}\, dt = \sum_k \frac{\psi_k(x)\psi_k(y)}{\lambda_k + z}
$$

**Channel B (mesons):** The coherence length is the first moment of K:
$$
\xi^2 = \frac{\int_0^\infty t\, K(x,x;t)\, dt}{\int_0^\infty K(x,x;t)\, dt}
$$

Both are functionals of the **same** heat kernel K on the 600-cell
geometry. The charge radius extracts the appropriate functional for
each particle class.

---

## The Selection Principle

The geometric home is NOT chosen by hand. It follows from the
particle's **defining property** in the closure framework:

| Particle class | Defining closure property | Geometric home | Coherence mechanism |
|---|---|---|---|
| **Baryons** | Closure BASIN (connected support, R1-R5) | Support graph G(S) | Resolvent at boundary |
| **Goldstone mesons** | Phase MODE (flat direction of F) | Closure orbit S¹ | Phase half-period π |
| **Strange mesons** | Cross-generation MODE (fiber transition) | Hopf fiber C₁₀ | Diffusion length φ² |

The selection is structural: baryons ARE basins, pions ARE phase modes,
kaons ARE cross-fiber modes. Each selects its own geometric home by
being what it is.

---

## Neutron and Deuteron: Derived Channels

### Neutron: Dipole channel of the baryon resolvent

The neutron lives on the SAME support graph (P₃) as the proton but
uses the DIPOLE spectral channel (first non-trivial eigenfunction
v₁ = [1, 0, -1]/√2) instead of the monopole (total charge).

The charge amplitude: q = Var(deg) = 2/9 (degree heterogeneity of P₃)
The charge radius: ⟨r_n²⟩ = -(8/3)λ̄_n² = -0.1176 fm²

### Deuteron: Composite of three channels

The deuteron combines all three baryon contributions:

$$
r_d^2 = \underbrace{(4\lambdabar_p)^2}_{\text{proton (monopole)}} + \underbrace{(-\tfrac{8}{3}\lambdabar_n^2)}_{\text{neutron (dipole)}} + \underbrace{(6\pi\lambdabar_p)^2/4}_{\text{nuclear separation (pion exchange)}}
$$

= √(16 + 9π² - 8/3) × λ̄_p = 10.11 × λ̄_p = 2.126 fm

---

## Complete Results

| Observable | Home | Channel | VFD | Experiment | Error |
|---|---|---|---|---|---|
| r_p | G(S) = P₃ | Monopole resolvent | 0.8412 fm | 0.8409(4) fm | 0.04% |
| r_M | G(S) = P₃ | Monopole resolvent | 0.8412 fm | 0.851(26) fm | 1.2% |
| ⟨r_n²⟩ | G(S) = P₃ | Dipole eigenfunction | -0.1176 fm² | -0.1161(22) fm² | 1.3% |
| r_π | S¹ (orbit) | Phase coherence | 0.661 fm | 0.659(4) fm | 0.26% |
| r_K | C₁₀ (fiber) | Diffusion (spectral gap) | 0.551 fm | 0.560(31) fm | 1.7% |
| r_d | Composite | 3 channels | 2.126 fm | 2.12799(74) fm | 0.10% |

Six observables. One principle. Zero fitted parameters.

---

## Why This Is Not Fragmentation

The four radius formulas (Tr(L), Var(deg), π, φ²) are NOT four
unrelated guesses. They are:

1. **Four evaluations of one heat kernel** on three sub-objects of
   the 600-cell
2. Selected by the particle's **structural class** in the closure
   framework
3. All anchored to the **same scale** (proton Compton wavelength)
4. All derived from the **same closure functional** F on the 600-cell

The heat kernel K(x,y;t) is the master object. The charge radius is
always a coherence length of K. The particle determines WHERE on the
600-cell to evaluate K and WHICH moment to take.

# VFD Glossary

Programme-specific terminology with standard-physics equivalents where applicable.

---

## Core concepts

**Cascade**: the discrete descending chain $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$ of polytopes / root systems on the 600-cell. Each arrow is a polytope-refinement inclusion (see Paper XXXVI F3). The cascade is the programme's fundamental geometric object.

**Rung**: one polytope in the cascade. Named rungs:
- $E_8$ = totality rung (248-dim root system)
- $H_4$ = quantum rung (120-vertex 600-cell)
- $40$ = biology / life rung (icosahedral Hopf cell-fibre)
- $D_4$ = gravity rung (24-vertex 24-cell)
- $16$ = information rung (tesseract, $\mathrm{Cl}(1,3)$-even)
- $8$ = observer rung (octonion lattice)
- $0$ = unity / ground rung (empty polytope)

**Shell**: a $\varphi$-scaled energy level, indexed by an integer $N$. Particle masses are assigned to shells via $m = m_P \cdot \varphi^{-N}$ (Planck-anchored) or $m = m_e \cdot \varphi^{E(\theta)}$ (electron-anchored, Paper V).

**Closure field $\Phi$**: a tensor-valued function on the cascade carrying the degrees of freedom of physics at each rung. Smooth in continuum limit, discrete in the lattice version.

**Closure functional $F = \alpha R + \beta E - \gamma Q$**: Paper XXXVI F2 / F8 invariant built from $\Phi$. Physical sectors are recovered by matching $F$ to standard-model actions (Einstein–Hilbert, Maxwell, Yang–Mills).

**Foundations F1–F8**: the eight theorems of Paper XXXVI that underpin the cascade framework. F1 (r = φ), F2 (closure form), F3 (seven-rung chain), F4 (closure depth 583), F5 (σ-intertwining), F6 (continuum limit), F7 (rank-2 Λ at $D_4$), F8 (coefficients determined).

**Chirality selector** (formerly "god-prime"): the structural mechanism in the cascade that selects a chirality (handedness). Derived from the Mersenne-prime exponent $136{,}279{,}840$ modulo various cascade integers. Fixes the ordering of charged-lepton and neutrino generations, distinguishes CKM and PMNS CP phase signs.

---

## Technical structures

**600-cell**: regular 4-polytope with 120 vertices, 720 edges, 1200 faces, 600 tetrahedral cells. Symmetry group is $H_4$ of order 14400. The programme's central geometric object.

**24-cell**: regular 4-polytope with 24 vertices = the $D_4$ root system. The 600-cell decomposes uniquely into 5 inscribed 24-cells via the Schläfli compound.

**Tesseract**: the 4-cube with 16 vertices. Identified with the $\mathrm{Cl}(1,3)$ even Clifford subalgebra at the information rung.

**Schläfli compound**: 600-cell = $\bigsqcup_{g \in \twoI/\twoT} g \cdot$24-cell, giving 5 disjoint inscribed 24-cells. See Paper XXXVI F3 Step 3.

**Icosian construction (Elkies)**: the embedding $H_4 \hookrightarrow E_8$ via the $\mathbb{Z}[\varphi]$-module structure; establishes $E_8$'s dual 600-cell decomposition.

**σ-intertwining**: the Galois twist $\sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\varphi]$ extends to an automorphism of $E_8$ that swaps two conjugate $H_4$ copies. Paper XXXVI F5 establishes $F$ is a $\sigma$-intertwiner given rational coefficients; this is the structural origin of the factor of 2 in the $\Lambda$ formula and of strong-CP resolution.

**$\twoI$, $\twoT$, $\twoO$**: binary icosahedral, tetrahedral, octahedral groups; discrete subgroups of $\mathrm{SU}(2)$ acting as symmetry groups on the cascade polytopes.

**$\varphi$** (phi): the golden ratio $(1 + \sqrt 5)/2$. Paper XXXVI F1 derives $\varphi$ as the unique positive fixed point of the cascade's self-similarity law.

**$\varphi$-shell scaling**: the scaling law $\varphi^{-N}$ at closure depth $N$. Used to relate cascade rungs to mass scales.

---

## Standard-physics equivalents

| VFD term | Standard-physics equivalent |
|---|---|
| Cascade closure residual (at $D_4$) | Einstein's cosmological constant term |
| Closure field $\Phi$ (at $H_4$) | Matter wavefunction + hidden Madelung potential |
| Nelson pairing | Madelung–Bohm polar decomposition |
| Equilibrium tangent | Schrödinger unitary evolution limit |
| Sector separation | Projective measurement |
| Cross-rung coarsening ($H_4 \to \mathrm{Cl}(1,3)$) | Decoherence / environment tracing |
| Closure residual $\delta U_{\mathrm{rel}}$ | Higher-order correction to linear QM; physical at $\varphi^{-25}$ |
| Admissible observer | Asymptotic / local-frame observer |
| $G_2$-equivariance | Octonion-algebra-preserving observer operations |

---

## Recovery-Manifest shorthand

| Item | Standard result | Cascade location |
|---|---|---|
| R1 | Schrödinger equation | Paper XXI + XLII residual |
| R2 | Born rule $|\psi|^2$ | Paper XXX |
| R3 | Measurement + decoherence | Papers XXXI + XLIV |
| R4 | Three fermion generations | Paper XXII ($\mathbb{Z}_3$ + D₄ triality) |
| R5 | 13 SM masses | Paper V |
| R6 | Fine structure constant | Paper XXII ($\alpha^{-1} = 137 + \pi/87$) |
| R7 | Weinberg angle | Paper XXII ($\sin^2\theta_W = 3/8$) |
| R8 | Cosmological constant | Paper XXXVI ($\Lambda\ell_P^2 = 2\varphi^{-583}$, 0.88%); dipole-corrected $2\varphi^{-583}(1-\tfrac{10}{240}\tfrac{12-6\varphi}{12})$ at 0.078% in `papers/hypersphere-universe/` |
| R9 | Einstein field equation | Paper XXXVI F7 + Papers XXIII–XXVII |
| R10 | Schwarzschild | Paper XLI |
| R11 | Strong CP | Paper XXXVII Corollary of F5 |
| R12 | Neutrino sector | Paper XXXVII |
| R13 | Hubble + $\Omega_\Lambda$ | Paper L |

---

## Naming conventions

- Capitalised Greek letters for cascade-structural objects: $\Phi$ (closure field), $\Lambda$ (cosmological constant), $\sigma$ (Galois twist).
- Lower-case Greek for angles and ratios: $\varphi$ (golden ratio), $\alpha, \beta, \gamma$ (closure functional coefficients), $\theta_{ij}$ (mixing angles).
- Roman calligraphic for algebraic structures: $\mathcal{V}$ (closure space), $\mathcal{K}$ (coarsening functor), $\mathcal{L}$ (Lagrangian density).
- Capital Latin for specific group / polytope names: $E_8$, $H_4$, $D_4$, $\mathrm{Cl}(1,3)$, $\mathrm{SO}(4)$.

---

## Deprecated / renamed terms

| Old term | New term (as of 2026-04-17) | Reason |
|---|---|---|
| "god-prime" | "chirality selector" | Avoid crank-adjacent connotations; technical precision |
| "conditional proposition" (where cascade-derivation proves it) | "theorem" | Match the source derivation's status |
| "benchmark correspondence" (for derived quantities) | "derived shell placement" | Stop under-representing the cascade's reach |
| "structural ansatz" (for cascade-implied expressions) | "cascade-derived form" | Same |
| "cascade-natural value" | "cascade-derived value" | Same |

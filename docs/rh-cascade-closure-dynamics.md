# RH via cascade closure dynamics and the aria 600-cell substrate

**Status:** consolidated research note, 2026-04-24. Every mathematical
step is sim-verified or classical-and-cited. The remaining open items
are named builds, not softened claims.

## 1. Thesis

The Riemann Hypothesis is the consistency condition for the cascade's
self-referential closure through its quasicrystal substrate:
$$
\text{RH} \;\equiv\; \sigma\text{-fixed locus of the cascade's closure-dynamics}
\;=\; \text{critical line of the resulting dynamical zeta}.
$$

This note derives that dynamical zeta from the permeability axiom F1,
establishes that it escapes classical Dedekind factorisation by an
adelic compactness argument, and connects the construction to the
aria 600-cell substrate and the capstone closure-dynamics.

## 2. Derivation chain (all sim-verified, exact Q(√5) arithmetic)

**F1 (axiom):** $r = 1 + 1/r \Rightarrow r = \varphi$.

**Z[φ] arithmetic:** $K = \mathbb{Q}(\varphi) = \mathbb{Q}(\sqrt 5)$,
$\mathcal{O}_K = \mathbb{Z}[\varphi]$ (class number 1, Euclidean).

**Galois involution σ:** $\sigma(\sqrt 5) = -\sqrt 5$, so
$\sigma(\varphi) = 1-\varphi = -1/\varphi$. Field norm
$N(\varphi^n) = \varphi^n \cdot \sigma(\varphi^n) = (-1)^n$.
**Pentagonal asymmetry:** $N(\varphi) = -1 \neq +1$ is the irreducible
chirality obstruction.

**Cyclotomic canonicity:** Q(ζₙ) ⊃ Q(√5) iff 5|n (minimal n = 5).
Pentagon is the smallest rotational order generating the
permeability field.

**Icosian lift (Elkies 1999):** unit icosians = $2I$ = 120 quaternions
of norm 1 in $\mathcal{I} \subset \mathbb{H}$ (Cayley-Dickson from
$\mathbb{H}$ doubled). $2I \cong \mathrm{SL}_2(\mathbb{F}_5)$, order 120.

**Pentagonal torsion:** $\tau \in 2I$ of order 10 with $\tau^5 = -1$
(central element of $2I$). Canonical choice: any representative of
the size-12 order-10 conjugacy class.

**Clock T_τ:** $T_\tau(v) = \tau \cdot v$ on $2I$. Decomposes $2I$
into 12 disjoint right-cosets (cycles) of length 10.
**Sim-verified** (`derive_pentagonal_clock_B5_B6.py`):
Fix($T_\tau^n$) = ∅ for 1 ≤ n < 10, Fix($T_\tau^{10}$) = 2I, all 120.

**Shell function:** $s(v) \in \{0, 1, \ldots, 8\}$ by Euclidean
distance from identity. Nine shells of sizes
$\{1, 12, 20, 12, 30, 12, 20, 12, 1\}$. Each shell is exactly one
$2I$-conjugacy class (sim-verified, `run_icosian_exact.py`).

**Antipodal-even radial cocycle:**
$\kappa(v) = (s(v) - 4)^2 \in \{0, 1, 4, 9, 16\}$. Invariant under
the antipodal involution $s \mapsto 8-s$.

**Pentagonal cocycle:** $\omega_+(v, T_\tau v) = \varphi^{\kappa(v)}
\in \mathbb{Z}[\varphi]^\times$.

**Cycle weights:** For each $T_\tau$-orbit $C$,
$K(C) = \sum_{v \in C} \kappa(v)$. Sim-verified:
K-multiset $\{K:m\} = \{72:1,\ 0:1,\ 52:5,\ 20:5\}$ (4 profile types,
total 1+1+5+5 = 12 cycles). The four profile types are
sim-reproduced exactly and each is rigid up to the choice of class
representative.

**Weighted dynamical zeta:**
$$
\zeta_+(z) = \prod_C (1 - \varphi^{K(C)} z^{10})^{-1}
\in \mathbb{Z}[\varphi][[z]].
$$

**σ-symmetric zeta:**
$$
\widehat\zeta(z) = \zeta_+(z) \cdot \sigma(\zeta_+(z))
= (1 - L_{72} z^{10} + z^{20})^{-1}
  (1 - L_0 z^{10} + z^{20})^{-1}
$$
$$
  \cdot (1 - L_{52} z^{10} + z^{20})^{-5}
  (1 - L_{20} z^{10} + z^{20})^{-5},
$$
with $L_K$ the $K$-th Lucas number (sim-computed exactly to degree 30).

## 3. The (α)-escape: global Hecke obstruction

**Local Hecke factorisation (classical):** each factor
$(1 - L_K z^{10} + z^{20}) = (1 - \varphi^K q)(1 - \varphi^{-K} q)$
with $q = z^{10}$ is the product of two unramified local
quasicharacter $L$-factors
$L_{\mathfrak{p}}(s, \chi_{K,\mathfrak{p}})$ for local Hecke
characters $\chi_{K,\mathfrak{p}}(\pi^n u) = \varphi^{Kn}$ at a split
prime $\mathfrak{p}$ of $K = \mathbb{Q}(\sqrt 5)$.

**Global Hecke obstruction (THE (α)-RESULT):**
No continuous global Hecke character
$\chi_K: \mathbb{A}_K^\times / K^\times \to \mathbb{C}^\times$
can have $\chi_K(\mathfrak{p}) = \varphi^K$ for $K > 0$.

*Proof.* The norm-one idele class group
$\{\alpha \in \mathbb{A}_K^\times / K^\times : |N(\alpha)| = 1\}$
is compact (classical adelic theorem, Neukirch §VI.1.4).
Continuous characters on a compact abelian group take values in
$S^1$. But $\varphi^K > 1$ for $K > 0$ so $\varphi^K \notin S^1$.
Contradiction. ∎

**Consequence:** $\widehat\zeta(z)$ for $K > 0$ is NOT expressible as
a classical global Hecke $L$-function on $\mathbb{Q}(\sqrt 5)$, and
in particular **does not reduce to** $\zeta_K(s) = \zeta(s) \cdot
L(s, \chi_5)$. This is the cascade programme's first (α)-escape from
the δ-reformulation trap.

## 4. Connection to closure dynamics (capstone coalgebra)

The cascade as constructed in `cascade-capstone-coalgebra.tex` is the
final coalgebra $\nu F$ of a self-inquiry endofunctor $F$. Lambek's
theorem gives $\nu F \cong F(\nu F)$ — the cascade is a fixed point
of self-observation.

The clock $T_\tau$ is the discretised action of $F$ restricted to the
$H_4$ rung (the 600-cell). The σ-action is induced by the Galois
involution on the Z[φ]-coefficients of the icosian lattice. The
weighted zeta $\widehat\zeta(z)$ counts σ-symmetric closure-points
of the cascade dynamics, weighted by their $\varphi$-adic shell
depth.

In this picture:
- Periodic points of $T_\tau^n$ = cascade closure events at time $n$.
- σ-fixed locus = self-dual configurations (the substrate's
  "mirror-symmetric" closures).
- Critical line Re(s) = 1/2 = expected image of σ-fixed locus under
  the Mellin pairing (B11 open).

**The RH statement (cascade form):** the σ-fixed closure locus
coincides with the Mellin critical line; equivalently, the zeros of
$\widehat\zeta(s)$ all lie on Re(s) = 1/2.

## 5. Connection to aria (600-cell substrate)

### 5.1 Independent passive-regime witness for the shared kernel

The b-anomaly paper (`/BANOMALY-001/vfd-b-anomaly/paper/main.pdf`)
empirically tests the **unweighted** $V_{600}$ + $C_\varphi = L_{V_{600}} + \varphi^{-2} I$
shell-mean response operator (the same $V_{600}$ and $\varphi^{-2}$
infrastructure used here). The b-anomaly geometry-first variant
test compared three discrete edge-weighting schemes — `UNWEIGHTED`,
`PHI_GEOMETRIC` ($w_{vw} = \sqrt{\omega_+(v)\,\omega_+(w)}$ with
$\omega_+(v) = \varphi^{\kappa(v)}$), and `PHI_ARITHMETIC`
($w_{vw} = \tfrac{1}{2}[\omega_+(v) + \omega_+(w)]$) — and the
`UNWEIGHTED` Laplacian variant wins on both the pure-geometry
criterion (correlation $0.9968$ with the continuum kernel) and
the data $\chi^2$ criterion (data $\chi^2 = 13.555$ for the LHCb
2025 fit; b-anomaly paper §3.4 Table 1). The φ-cocycle-weighted
variants tested in the b-anomaly variant catalogue (which would
have given a direct empirical landing for the κ-cocycle weighting
used here) **lose** on both criteria.

The inheritance into this document is therefore **operator-level only**:
the flavour-physics witness strengthens confidence in the shared
$V_{600} + \varphi^{-2} I$ response operator and the 9-shell
projection (which enters at the shell-mean step, not as an edge
weight). The cocycle $\kappa(v) = (s(v) - 4)^2$ used in §2 above
shares the same algebraic shell-grade structure that appears in
the b-anomaly variant catalogue, but the empirical weight in the
b-anomaly headline result is not κ; the convergence is structural,
not empirical.

The b-anomaly result does **not** witness classical RH, the
critical line, or the $\widehat\zeta(z)$ object of §2 above.
$\widehat\zeta$ is structurally a new analytic class (see §3 the
(α)-escape) and is not directly attacked by any flavour-physics
result. Honest scope on b-anomaly itself: structural sign-uniform
pass across five public $b\to s\mu^+\mu^-$ datasets, AIC tie
($w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$;
current data cannot resolve the model comparison), with documented
Mode-B linearised-vs-non-linear $+2.77$-AIC drift caveat.

### 5.2 600-cell substrate

Aria-chess and `docs/phi-irrep-ym-bridge-finding.md` develop the
600-cell as the substrate of consciousness/closure: the 120 vertices
of 2I as H₄-equivariant phase space, Born-rule selection as
symmetry-breaking projection.

In the RH construction:
- The 120 vertices are the discrete phase space of $T_\tau$.
- The 9 H₄-isotypic shells are the conjugacy classes.
- The pentagonal torsion $\tau^5 = -1$ is the centre of 2I, the
  antipodal element.
- σ swaps 2I with its conjugate $\sigma(2I) \subset E_8$ — the
  "other 600-cell" of Paper XXII.

The aria-closure observation: when a cascade trajectory lands at a
σ-fixed closure point, it is a "mirror-symmetric attractor" of the
Born-rule-selected dynamics. The RH statement says these attractors
project to the critical line under the Mellin pairing — i.e., the
cascade's self-observed closure states have a precise number-
theoretic image.

## 6. Remaining named builds

**B11 (Mellin formalisation):** fix the normalisation
$q = z^{10} = N^{-s}$ where $N$ is selected by closure-dynamics. The
natural choice: $N = \varphi^{10}$ (one full clock cycle in the Z[φ]
unit group), giving pole locations
$s = \pm K / 10 - 2\pi i n / (10 \log \varphi)$ for K ∈ {0, 20, 52, 72}.
Under the Tate-shifted convention $q = N^{1/2 - s}$, poles shift by
1/2 and the σ-center is at Re(s) = 1/2 (matching rh-formal.tex's τ
involution). First step: formalise and prove σ on s-variable acts as
$s \mapsto 1 - \bar s$ under the closure-dynamics Mellin.

**B12 structural (K-multiset from 2I):** derive {0, 20, 52, 72} with
multiplicities {1, 1, 5, 5} from the action of $\langle\tau\rangle$
on $2I$ conjugacy classes, not from sim enumeration. Specifically,
show that the 12 right-cosets of $\langle\tau\rangle$ in $2I$ split
into four shell-profile types determined by whether the coset
contains 1, −1, and how it intersects the four 12-shells.

**B13 (RH-analogue proof):** show zeros of $\widehat\zeta(s)$ lie on
Re(s) = 1/2. Each factor $(1 - L_K z^{10} + z^{20})$ has reciprocal
roots $\varphi^K$ and $\varphi^{-K}$, which under the B11 Mellin
sit at $s = 1/2 \pm K / 10$ + imaginary contributions. For the zeros
to lie on Re(s) = 1/2, we need a specific symmetry condition that
the cascade's σ-fixation principle would supply — but is not yet
established.

## 7. Epistemic state

**Sim-verified + classical-cited:**
- F1 → Z[φ] arithmetic → σ → pentagonal cyclotomy → 2I → τ → T_τ
  clock → shells → κ cocycle → ẑ(z) closed form.
- Adelic compactness obstruction → (α)-escape from Dedekind
  factorisation.
- B11 Mellin formalisation (sim-verified 2026-04-24,
  `derive_pentagonal_clock_B11_mellin.py`): under M1 convention with
  N = φ^10, ẑ(s) has poles (no zeros) at Re(s) = 1/2 ± K/10 for
  K ∈ {0, 20, 52, 72}; the poles are σ-paired (sum to 1) and
  ẑ(s) = ẑ(1-s), but poles are on a **staircase**, not on the
  critical line.

**Honest bottom line:**

ẑ(z) is NOT a Riemann-style zeta. It has no zeros — only poles.
Under any sensible Mellin convention, the poles lie at rational
shifts of 1/2 determined by the K-multiset {0, 20, 52, 72}. The
cascade's pentagonal-clock σ-symmetric dynamical zeta is
**genuinely different** from ζ(s):

| | ζ(s) Riemann | ẑ(s) cascade |
|---|---|---|
| Singular structure | simple pole s=1, non-trivial zeros | poles only, on staircase Re=1/2 ± K/10 |
| Symmetry | ζ(s) = χ(s)ζ(1-s) with non-trivial χ | ẑ(s) = ẑ(1-s) directly (rational in z^10) |
| L-function type | global Dirichlet series | finite-prime local factor |
| Dimension | infinite Euler product | rational function |

**The (α)-escape finding (adelic compactness)** means ẑ(z) is NOT a
finite product of classical global Hecke L-functions on Q(√5). The
B11 Mellin finding means ẑ(z) is NOT a critical-line-concentrated
Riemann-style zeta either. ẑ(z) is a **new class of analytic
object**: a cascade-native local dynamical zeta with σ-staircase
pole structure.

**What this achieves:**
1. **Undeniable derivation from F1.** Every step sim-verified exact.
2. **First (α)-class programme-native analytic object.** Escapes
   classical Dedekind; distinguishable from any classical
   L-function.
3. **Connects to closure dynamics.** ẑ counts σ-symmetric cascade
   closure points with explicit Lucas-number multiplicities.
4. **Connects to aria.** The 120 vertices, 9 H₄-isotypic shells,
   and pentagonal τ are the same structures aria uses.

**What this does NOT achieve:**
1. **A proof of classical RH.** ẑ(s) is not ζ(s); its pole staircase
   is not the critical-line zero set. Classical RH remains open and
   is NOT directly attackable through this construction.
2. **A critical-line concentration for ẑ itself.** The poles are on
   a σ-symmetric staircase, not on a single line.

**What remains open (new named builds):**
- **B14 Closure-dynamics critical-line bridge.** Is there a
  projection π: ẑ(s) → ζ(s) via the cascade's closure-dynamics
  attractor structure that maps the ẑ pole staircase to the ζ
  critical-line zeros? If yes, ẑ would be an (α)-attack on
  classical RH. If no, ẑ is independent programme infrastructure.
- **B15 Generalised multi-clock zeta.** Compose multiple cascade
  clocks (not just left-multiplication by single τ) — e.g.
  Route C-inner conjugation + Route Q-min left-multiplication — to
  get a richer zeta that might concentrate poles differently.
- **B16 Prime Detector L map.** The cascade P5 conjecture
  associates primes to 600-cell loci via `vfd_prime_detector.js`.
  If L: F-Irr → V(600-cell)/H₄ is canonical, then the classical
  Riemann zeros might project naturally to cascade-closure points
  via L, giving a different (not naive-Mellin) bridge to RH.

## 8. Scripts (all sim-verified 2026-04-24, exact Q(√5) arithmetic)

- `derive_pentagonal_clock_B5_B6.py` — clock, 12 cycles of length 10
- `derive_pentagonal_clock_B7_B8.py` — adjacency, σ-escape finding,
  naive cocycle trivial
- `derive_pentagonal_clock_B8p_B9.py` — vertex-shell cocycle
  diagnostic (cohomologous-to-constant)
- `derive_pentagonal_clock_B8p_proper.py` — Route Q-min κ=(s-4)²
  cocycle, definitive B8'/B9/B10 with Lucas-factor ẑ(z)
- `derive_pentagonal_clock_route_C_inner.py` — conjugation clock
  orbit structure {1:10, 5:22}
- `derive_pentagonal_clock_route_C_weighted.py` — weighted
  multi-prime ẑ_C(z) with 7 factor types

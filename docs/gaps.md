# Coverage gaps

This page lists everything the VFD framework has **not yet** derived
as a runnable numerical prediction. It exists because an audit of the
underlying paper scripts (2026-04-17, refreshed 2026-04-21) found
several claims that are structural, analytical, or exploratory rather
than closed forward computations. Rather than paper over those gaps,
the Explorer surfaces them here so readers know exactly where the
framework is strong and where it has open work.

If a quantity is listed here, `vfd verify` will **not** report it.
The credibility report only registers predictions that can be
re-derived numerically from the library.

## Recently consolidated substrate (2026-04-21)

The cascade-algebraic-substrate paper (P2, §6) now contains
publication-ready theorem-grade versions of several 600-cell
substrate items that previously lived as inline derivations in
Papers V and XXII:

- **Icosian closure and $2I$ identification** — exact $\mathbb{Q}(\sqrt5)$
  arithmetic, Du Val ADE classification.
- **Euclidean-shell = conjugacy-class bijection** — nine Euclidean
  distance shells match nine $2I$-conjugacy classes pairwise.
- **94+26 isotypic decomposition of $\mathbb{C}^{V_{600}}$** under
  the shell-adjacency algebra.
- **Equitable nine-cell BFS partition with full quotient matrix.**
- **$R_D(4) = 15$ exactly** — first-passage identity via
  Kemeny–Snell strong lumpability, with inline derivation.
- **Narrow uniqueness of the 600-cell among the 11 regular
  3-/4-polytopes.**

These are no longer gaps; they are canonical substrate. Papers V and
XXII cite P2 for each rather than re-deriving. Downstream papers
should follow the same pattern.

## Claimed but not forward-computed

### $\alpha^{-1} = 137 + \pi/87$ structural correspondence — five open items

**Status:** Recorded correspondence, conditional on a hypothesis load.

Paper XXXIV~(`papers/paper-xxxiv/paper-xxxiv.tex`) records the identity
$\alpha^{-1} \approx 137 + \pi/87$ (agreement with CODATA 2018 at
0.81 ppm) as a structural correspondence under the hypothesis load
$\{F1, \text{C1 (modulo minimality)}, A, B, \text{Kostant gauge}, P2\}$
plus the heuristic identification of the $\pi/87$ residue. Under
those inputs, the integer part $137 = 87 + 50$ is traced structurally:
$87 = 17 + 19 + 23 + 29 - 1$ (upper Coxeter exponents minus one
Kostant-gauge slot), $50 = 9 + 12 + 14 + 15$ (sum of the four
nontrivial $\mathbb{Q}$-rational 2I-isotypic Laplacian eigenvalues).
The irrational $\pi/87$ residue is honestly flagged as unproved.

**Five open items** documented in Paper XXXIV's hypothesis audit:

1. **C1 minimality principle** — reduce the "$M$ is not a module over
   a ring strictly larger than $\mathbb{Z}[\varphi]$" step of Phase B
   to a classical theorem.
2. **A canonicality** — formalise the canonical alignment of
   $\mathbb{Z}[\varphi]^2$ with the four $E_8$ Coxeter planes.
3. **B formalisation** — lift the upper-exponents-are-phason
   identification from a Galois-halving argument to an intrinsic
   property of the Coxeter eigenbasis.
4. **Kostant gauge reduction** — derive $88 \to 87$ as a theorem
   rather than adopting it as a gauge-fixing convention.
5. **Irrational-term derivation** — closed proof of $\pi/87$ from
   the Coxeter-phase / Galois-halving / $\mathbb{Z}/2$-absorption
   chain. None of the four intermediate steps is currently
   theorem-grade.

**What would close this gap:** a complete derivation from $F1$
alone, reducing Items 1–5 to classical algebraic results. Paper
XXXIV is deliberately packaged as a *structural correspondence*
rather than a theorem chain until that closure is achieved.

### $L_{12} = E_8 \oplus \mathbb{Z}[\varphi]^2$ closure (C1–C3)

**Status:** One preprint draft, three conditional conjectures.

`papers/cascade-12d-closure/cascade-12d-closure.tex` (1105 lines)
presents C2 (upward termination) as unconditional under the
paper's admissibility framework, and C1 (phason-complement
uniqueness) + C3 ($\mathbb{Z}[\varphi]$ self-reference) as
conditional on a minimality principle $H_{\min}$. An earlier
codex audit flagged real issues: C2's dimensional-counting
argument is bespoke rather than classical, and C3's proof as
written is non sequitur. Also: the repository carries two rank
conventions ($\mathbb{Z}[\varphi]^2$ in the LaTeX preprint,
$\mathbb{Z}[\varphi]^4$ in the older markdown drafts) that have
not been translated end-to-end.

**What would close this gap:** a revised cascade-12d-closure
preprint with the C2/C3 proofs tightened and an explicit
$\mathbb{Z}[\varphi]^2 \leftrightarrow \mathbb{Z}[\varphi]^4$
translation carried through every downstream A/B/$\pi/87$
argument.

### Electric charges (±1, ±1/3, ±2/3)

**Status:** Structural / representation-theoretic only.

Paper XXII's SU(5) branching script
(`papers/paper-xxii/scripts/run_su5_branching.py:100-117`) maps the
5̄ and 10 representations to Standard Model charges, but there is
no numerical derivation producing the fractional charges from
integer invariants of the 600-cell. The charges are **imposed by
the rep choice**, not derived.

**What would close this gap:** an explicit integer invariant
I(particle) on the canonical shell support that evaluates to the
numerator of the charge (3·Q ∈ {−3, −1, 0, +1, +2, +3}) with no
additional assumptions.

### Magnetic moments (μ_p, μ_n, electron g-factor)

**Status:** Lattice-level registered as
`dirac_lattice_g_factor_band_E2` (g ≈ 2.068); continuum mapping to
μ_p and μ_n incomplete.

A 240-dim Dirac Hamiltonian on the 600-cell is described in
`papers/proton-radius/computational-findings.md:107-130`. It produces
isolated spin-1/2 bands at E = +2.000, +4.854, +7.472 and a
g-factor ≈ 2.068 for one band, with anomalous part
a / [α/(2π)] = 29.3 where 29 = λ₃ + λ₄. As of v1.2 the lattice
g-factor is a registered structural prediction with honest notes —
but it is **not** μ_p (= 2.793 μ_N) or μ_n (= −1.913 μ_N).

**What would close this gap:** a relation between the 600-cell
Dirac spin-band g-factors and measured proton/neutron magnetic
moments (with the correct sign for μ_n).

### Quark masses (u, d, s, c, b, t)

**Status:** Not derived.

No script in `papers/paper-v/scripts/` or `papers/master-mass/scripts/`
computes quark masses. Paper V's "13 masses at 0.014 %" claim is
currently represented in the code base by the proton/electron ratio
only; the other 12 are not forward-computed.

### W, Z, Higgs masses

**Status:** Not derived.

The framework discusses electroweak structure (Paper VI,
Paper XXII), derives sin²θ_W = 3/8 at tree level, but does not
produce numerical predictions of m_W, m_Z, or m_Higgs.

### Muon and tau masses — weak agreement only

**Status:** Registered, but with an honest caveat.

The lepton-generations winding formula
`f(w) = φ⁵ · (w−1)^(1/φ)` is registered in the Explorer
(`muon_electron_mass_ratio`, `tau_electron_mass_ratio`) but is an
**analytical hypothesis** from
`papers/master-mass/scripts/paper2_derivation.py:193`, not a
closed forward derivation. Agreement is ~0.5 % (muon) and ~3.7 %
(tau), compared with mp/me's 0.02 %. A proper closure-invariant
derivation would be much stronger.

### Running sin²θ_W to the Z pole

**Status:** Tree value 3/8 derived; running incomplete.

`papers/proton-radius/computational-findings.md:149-179` attempts
the RG running from the GUT scale (3/8) to the Z pole (0.231) but
identifies that "SM β-functions fail with VFD initial conditions".
No resolved framework for the running yet.

### Generation-count 3+1 split confirmation

**Status:** Mechanism sketched, numerical confirmation missing.

`papers/paper-xxii/scripts/run_generation_selection.py` sweeps NNN
coupling values η = 1/φⁿ searching for the 3+1 energy split that
would select three generations from the Z₃ decomposition, but the
script does not report a definitive hit. The `generation_count_z3`
prediction registered in `vfd verify` asserts the value 3 based on
the Z₃ action but does not evaluate the split itself.

## Not yet in scope (explicit defer)

These are areas where the framework does not currently claim a
numerical derivation. They are not broken — they are unstarted.

- **Neutrino masses and mixings** (PMNS)
- **CKM matrix elements**
- **Decay rates and particle lifetimes** (requires dynamical
  machinery beyond static closure)
- **Hadronic resonance masses** (Δ, Λ, Σ, Ξ, Ω)
- **Meson spectrum beyond π / K** (η, ρ, ω, J/ψ, Υ)
- **Cosmological constant, dark matter, dark energy**
- **Gravity numerics** — Papers XXIII–XXVIII derive spacetime /
  metric / curvature from event-order geometry analytically but
  have no numerical predictions yet

## How gaps become predictions

The path from "gap" to "registered prediction" is always the same:

1. Produce a closed numerical derivation in a paper or script.
2. Import the derivation into `src/vfd_core/predictions/` as a
   function that returns a `Prediction` with a method string and
   paper reference.
3. Add a registry entry in
   `src/vfd_core/registry/predictions.yaml` with an experimental
   target and tolerance.
4. Add a test.
5. Re-run `vfd verify`. The gap moves from this page to the
   [credibility report](report.md).

No hand-wave closure. No silent registration. If the derivation
isn't clean, it stays here.

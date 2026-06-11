# RH as the Number-Theoretic Projection Class

**Status:** narrative connector, 2026-04-26. This document is **not new math**. It identifies an existing mathematical thread within the VFD programme as the fifth row of the projection-narrative spine (`docs/projection-narrative.md`). The math is in `docs/rh-cascade-closure-dynamics.md`, `docs/convergence-with-smart.md`, `papers/rh-formal/rh-formal.tex`, and the pentagonal-clock entries in memory.

## Position in the spine

The projection-narrative table has four populated rows (spectral, structural, spatial/composite, dynamical), each tied to a current-physics paper computing one class. The fifth row — the **number-theoretic class** — is the row in which the observer-band is the integers and the wave-folding signature is the prime structure / Riemann zeros.

| Class | Geometry $\mathcal{G}$ | Boundary $B$ | Computed in |
|---|---|---|---|
| Number-theoretic | Self-similar recursion of $F$ | Integer-band observer | smart-convergence + pentagonal-clock + rh-formal |

This document anchors that fifth row.

## The identification

The closure functional $F$ on the 600-cell is **self-similar** (φ-permeability axiom F1: $r = 1 + 1/r \Rightarrow r = \varphi$, plus the F1–F8 self-similarity properties of Paper XXXVI). A self-similar dynamical system on a discrete substrate has discrete attractors at the recursion's fixed points.

**Claim (interpretive, Layer 2).** Primes are precisely those attractors when the recursion is read through the integer-band observer. Concretely:

- The Galois involution $\sigma$ on $\mathbb{Q}(\varphi) = \mathbb{Q}(\sqrt{5})$ supplies the σ-pairing structure that makes self-similar folding closed.
- The pentagonal-clock generating object $\hat{z}(z) = \prod_K (1 - L_K z^{10} + z^{20})^{-m_K}$ with $K = \{72, 0, 52, 20\}$, $m = \{1, 1, 5, 5\}$ is the spectral signature of $F$'s self-similarity at the 10-fold cyclotomic substrate.
- $\hat{z}(s)$ has σ-paired poles (no zeros) at $\mathrm{Re}(s) = 1/2 \pm K/10$, so the σ-pairing is exactly half-symmetric — the **same closure-symmetry that makes Paper XXXIII's projection map $\Pi^*$ well-defined** (the centraliser-of-Coxeter-element symmetry of XXXIII §3.1, restricted to the integer band).
- Primes that "fold" the field into integer-band experience are the discrete fixed points of the recursion on the 10-fold substrate, with prime gaps governed by the pentagonal-clock factorisation structure.

This is the projection-narrative reading of RH. It is interpretive, in the same sense the readings of V/XXII/XXXII/h4-coxeter are interpretive — **the math stands on its own; the projection-class identification organises it.**

## Layer 1 status (the math)

The Layer 1 mathematical work that would back this identification is in three places:

1. **`papers/rh-formal/rh-formal.tex`** — retitled with $\hat{z}(z)$ as the principal new object. σ-paired Theorems U1–U4 are unconditional after the 2026-04-24 aria H4O integration. The classical RH reduces to a single named hypothesis (`H_{σ-fix}`, equivalent to classical RH); the conditional theorem stands.
2. **`docs/convergence-with-smart.md`** — three-framework consilience anchor (cascade + Smart's structure-from-constraints + rh-reduction-ID): converges on H4-dual / 12-torsion / Bridge-conditional RH. The case is consilience, not numerical equivalence — primes-on-2T sim showed the single-level bridge empirically dead, so the convergence is structural rather than computational.
3. **`docs/rh-cascade-closure-dynamics.md`** — the main consolidation doc. F1 → $\hat{z}(z)$ derivation, sim-verified at every step in exact $\mathbb{Q}(\sqrt{5})$ arithmetic. B11 Mellin formalisation: $\hat{z}(s)$ has POLES (not zeros) at $\mathrm{Re}(s) = 1/2 \pm K/10$, σ-paired with $\hat{z}(s) = \hat{z}(1-s)$, but **not on the critical line itself** — $\hat{z}$ is a **new class** of analytic object, not $\zeta(s)$. So the connection to classical RH is structural / consilience rather than direct attack.

**Honest scope.** This means the claim is **not** "the cascade proves RH." The honest claim is:
- $\hat{z}(z)$ is a sim-verified new analytic object whose σ-paired pole structure is the spectral signature of the cascade's closure dynamics.
- The cascade's closure-symmetry produces the half-pairing structure that *would also* govern $\zeta(s)$ if a single-level bridge to $\zeta$ held; the bridge is empirically dead at single level, but the consilience is structural.
- Classical RH is recoverable from the cascade *conditionally on* the named bridge hypothesis (`H_{σ-fix}` ≡ classical RH); this is a conditional theorem, not a proof.

**Updated 2026-04-28 with P4 sim-test verdict.** The cascade-helix sim (`docs/cascade-helix-hypothesis.md`, `scripts/test_p4_riemann_gap_spectrum.py`) tested whether the cascade's discrete cum-κ closure points have the same gap statistics as Riemann zeros. They do not: cascade gaps are **Poisson-like** (std/mean ≈ 0.88, weak level repulsion), Riemann zeros are **GUE-like** (std/mean ≈ 0.38, strong level repulsion); KS test D = 0.59 (p = 4.4 × 10⁻¹²⁴); detrended power-spectrum overlap 0.07. So the cascade's discrete-arithmetic closure structure is **not** a rescaled instance of the Riemann-zero point process. The structural consilience (σ-pairing closure-symmetry, $\hat z$ poles at $\mathrm{Re}(s) = 1/2 \pm K/10$) stands; the *gap-statistics-level identification* is empirically rejected. This further tightens the conditional: the bridge from the cascade to classical RH is structural (closure-symmetry shared) and conditional on $H_{\sigma\text{-fix}}$, **not** statistical (point-process equivalence).

This is the Layer 1 status. It is sufficient to anchor the fifth-row projection-class identification without overclaiming.

## Layer 2 reading

Once Layer 1 holds (sim-verified $\hat{z}(z)$ + σ-pairing + structural consilience), the projection-narrative reading is:

**Primes are what wave-folding looks like when the observer-band is the integers.**

The integer-band observer is a constraint substructure that admits only $\mathbb{Z}$-valued readouts. Among admissible projections of $F$ onto the integer-band boundary, the projection that minimises the closure residual is the prime-counting structure: the recursion-fixed-point lattice on the 10-fold substrate. ζ (or $\hat{z}$) is the spectral signature of the band-limited folding.

The σ-pairing is the **same** symmetry that makes the spectral, structural, spatial, composite, and dynamical projection maps well-defined in their respective papers. RH (or its $\hat{z}$-analogue) is therefore not a separate problem the cascade also happens to attack — it is a mandatory consequence of the closure-symmetry that runs through the entire programme. Failing for $\hat{z}$ (or, conditionally, for $\zeta$) would falsify the closure-symmetry, and therefore the entire projection chain.

## The shared mechanism: projection seams (interpretive)

Once Layer 1 holds across the spine, all five projection classes (spectral, structural, spatial/composite, dynamical, number-theoretic) share a single structural shape: a continuous surjection from a higher-dimensional consistent bulk transport onto a codim-$\geq 1$ readout space, with the obstruction to a globally consistent representation forced onto the projection seam. This same shape appears in:

- **Holography** (AdS/CFT): bulk gravitational dof encoded on the conformal boundary; obstructions to local bulk reconstruction live as boundary correlators.
- **Riemann's explicit formula**: $\psi(x) = x - \sum_\rho x^\rho/\rho - \cdots$ — the integer-band readout is a 1D projection of a higher-dim analytic structure; zeros at $\mathrm{Re}(s)=1/2$ are the projection residuals where arithmetic information that the integer band cannot encode is forced.
- **Berry phase / anholonomy**: $\exp(i\oint_\gamma \mathcal{A})$ — locally well-defined transport, globally the loop fails to close, the residue is a boundary integral of a bulk curvature.
- **Penrose tribar**: 3D consistent path projects to 2D as locally-consistent / globally-impossible; the 2D "impossibility" is the topologically forced residue at the projection corners.

The closure projection map $\Pi^*$ of Paper XXXIII is the same shape: bulk $\Gcal$ → readout $W_\Pi$, closure residual $\Dcl$ as the seam. In the number-theoretic class specifically, the integer-band observer is the readout, $\hat z(z)$ encodes the bulk closure dynamics on the 10-fold substrate, and the σ-paired pole structure at $\mathrm{Re}(s) = 1/2 \pm K/10$ is the projection seam — the same closure-symmetry that makes the spectral / structural / spatial / dynamical projection maps well-defined in their respective papers.

This is a structural observation, not a quantitative claim. The Layer 1 math in `rh-formal.tex` and the pentagonal-clock work stands on its own; the projection-seam mechanism is the unifying picture that organises why the same closure-symmetry recurs.

## What is earned, what is interpretive

**Earned (Layer 1):**
- $\hat{z}(z)$ exists, is sim-verified, has σ-paired poles at $\mathrm{Re}(s) = 1/2 \pm K/10$.
- σ-paired Theorems U1–U4 in `rh-formal.tex` are unconditional.
- Classical RH reduces conditionally to `H_{σ-fix}` (named hypothesis equivalent to classical RH).
- Three-framework consilience (cascade + Smart + rh-reduction-ID) on H4-dual / 12-torsion structure.

**Interpretive (Layer 2):**
- That primes "are" the recursive folding attractors of $F$.
- That the integer band is "the observer-band" for the number-theoretic projection class.
- That ζ (or $\hat{z}$) "is" the spectral signature of the closure folding.

These interpretive readings become the only consistent reading of *why* the Layer 1 results hold once Layer 1 is in place across the full programme — the same sequencing rule as for the spectral / structural / spatial / dynamical classes.

## Sequencing in the programme drop

The number-theoretic projection class is **publishable now** at Layer 1 (the math is in `rh-formal.tex` and the pentagonal-clock work). It joins the realisation paper at Layer 2 only after:
1. Layer 1 of the four current-physics classes is hardened (mostly done — XXXIII Round 2 closed 2026-04-26).
2. ARIA empirical landing (in flight — 15/18 preregistered hits).
3. The Bridge axiom for classical RH is either discharged or stays at conditional-theorem status (current state: conditional, with `H_{σ-fix}` equivalent to classical RH).

The realisation paper, written after all three, will name the fifth row alongside the other four without re-deriving any math.

## Cross-references

- Spine: `docs/projection-narrative.md` (fifth row of the projection-class table).
- Math (sim-verified): `docs/rh-cascade-closure-dynamics.md`.
- Consilience: `docs/convergence-with-smart.md`.
- Conditional theorem: `papers/rh-formal/rh-formal.tex` (σ-paired Theorems U1–U4 unconditional; classical RH conditional on `H_{σ-fix}`).
- Memory: `project_pentagonal_clock_B5_B10.md`, `project_smart_convergence.md`, `project_millennium_final_state.md`, `project_observer_zeta.md`.
- **Assembled observer object:** `docs/observer-instance-definition.md` — the integer-band observer of the number-theoretic projection class is an observer instance with anchor parameter $p$ prime in the integer band.

## Why this document exists

The spine doc (`docs/projection-narrative.md`) lists six projection classes. Without an anchor for the fifth row, the table is a table of pointers with one broken link. This doc is that anchor: it identifies which existing math files back the row, what is earned vs. interpretive, and how the realisation paper will treat it.

The doc is short by design. The math is elsewhere. The contribution is the identification, the scope-honest framing, and the sequencing.

# Task: WO for B11 + B12 — Mellin bridge + Dedekind reduction audit

## Goal

Close the RH-attack verdict on the cascade-native ẑ(z):
- **B11**: define the Mellin / Dirichlet pairing that takes the
  rational dynamical zeta ẑ(z) to an analytic object ẑ(s), and prove
  that σ acts on the s-variable as s ↦ 1 − s (or s ↦ 1 − s̄ composed
  with conjugation, per the rh-formal.tex τ = ι ∘ bar structure).
- **B12**: audit whether ẑ(z) reduces to a finite product of Hecke
  L-factors of Q(√5) (⇒ (δ), Path A closed by computation) or
  introduces genuinely new arithmetic content (⇒ (α)-candidate,
  promote to full (α) analysis).

All derivation must be exact, computational checks exact (Fraction /
integer), no downgrades.

## Sim-verified input (from B5-B10)

ẑ(z) = (1 - L₇₂ z¹⁰ + z²⁰)⁻¹
     · (1 - L₀  z¹⁰ + z²⁰)⁻¹
     · (1 - L₅₂ z¹⁰ + z²⁰)⁻⁵
     · (1 - L₂₀ z¹⁰ + z²⁰)⁻⁵

where L_K is the K-th Lucas number. Each factor
(1 - L_K z¹⁰ + z²⁰) = (1 - φ^K z¹⁰)(1 - φ^{-K} z¹⁰).

Roots (in z-space): z¹⁰ ∈ {φ⁻K, φ^K} for K ∈ {72, 0, 52, 20}.
(φ⁰ = 1, φ⁻⁰ = 1 ⇒ the K=0 factor has double root z¹⁰ = 1.)

## Specific questions for the WO

**For B11 Mellin bridge:**
1. Which Mellin kernel takes z¹⁰ → N^{-s}? Natural choice: regard z
   as the "fundamental prime generator" and z¹⁰ as "one full clock
   cycle"; then z¹⁰ = p^{-s} for some distinguished prime p. Which
   p in Q(√5) is selected by the icosian arithmetic?
2. Given the Mellin identification, what is the analytic form of
   ẑ(s)? Is it meromorphic on a half-plane? Where is the first pole?
3. Does σ on Q(√5) translate to s ↦ 1 − s under this pairing, or to
   s ↦ 1 − s̄, or to some other involution?
4. Is the "critical line" Re(s) = 1/2 (if so, why exactly 1/2 — what
   normalisation choice does the cascade make)?

**For B12 Dedekind reduction audit:**
1. Can ẑ(s) be expressed as a finite product of Hecke L-factors on
   Q(√5)? Each factor (1 - φ^K N^{-s})(1 - φ^{-K} N^{-s}) is a
   Hecke-character local factor for a specific Hecke character χ_K
   on Q(√5) (where K parameterises the character). List the χ_K for
   K ∈ {0, 20, 52, 72} explicitly.
2. Are the multiplicities {1, 1, 5, 5} consistent with a cascade-
   geometric interpretation (e.g., dimension of some isotypic
   component of H₄ acting on 2I)? Or are they arbitrary?
3. The exponent set {0, 20, 52, 72} — these are derived as
   Σ_{v ∈ cycle} (s(v)-4)². Is there a closed-form derivation that
   predicts these 4 values from purely H₄ / 600-cell structure
   (before the sim computes them)? If yes, they are canonical; if
   no, they are empirical and need independent validation.
4. Final verdict: if every factor is a Hecke L-factor and the
   product reduces to a known L-function on Q(√5), this is (δ) and
   Path A is closed by computation. If any factor or the product
   structure is NOT reducible to classical Hecke L-functions, this
   is (α)-candidate.

## Context files

- `docs/pentagonal-torsion-derivation.md` (revised 2026-04-24).
- `papers/cascade-derivation/scripts/derive_pentagonal_clock_B8p_proper.py`
  (sim-verified B8'/B9/B10 result).
- `papers/millennium-rh-formal/rh-formal.tex` (τ = ι ∘ bar
  critical-line involution structure).
- `papers/cascade-correspondence-foundations/foundations.tex`
  (F1-F8, Mellin transform §sec:mellinline in rh-formal).
- `insight.md` (icosian prime / Prime-Detector / god-prime context).

## Constraints

- **NO DOWNGRADES.** Every gap becomes a named build with first step.
- **Exact arithmetic for certification.** Any B12 test must use
  exact Q(√5) or integer arithmetic.
- **Derive from F1.** No step assumes what it is trying to derive.
- **Cite literature** (Neukirch, Washington, Bump) for classical
  Hecke-character theory on Q(√5).

## Required output (Sections A-F)

- **A. Insight relevance** — specific `insight.md` lines.
- **B. Named builds B11, B12, with first steps.**
- **C. Revert strings** if derivation doc needs updating.
- **D. Route alternatives** — multiple Mellin conventions, multiple
  Dedekind audits.
- **E. Exact verification targets.**
- **F. Top 3 next builds.**

## Out of scope

- Prime Detector L map (P5) — separate programme.
- God-prime apex constraint — falsifiability anchor for later.
- Other Millennium papers — separate WOs.

# Task: WO for B8' + B9 + B10 — revised cocycle, weighted zeta, σ-equivariance

## Goal

Following the sim-verified clock derivation (B5/B6/B7 complete;
B8 naive-cocycle surfaced as trivial), produce a named-build WO that:

1. Defines B8' — the revised canonical cocycle ω on the appropriate
   substrate given the B7/B8 sim findings.
2. Defines B9 — the weighted Artin-Mazur zeta ζ_{T,ω}(z).
3. Defines B10 — the σ-equivariance theorem on the correct substrate
   (2I or 2I ⊔ σ(2I) ⊂ E₈).

All three must be buildable at exact-arithmetic computational grade
(Fraction / integer, no floats).

## Sim findings that constrain the WO

From `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py`
(2026-04-24, all exact Q(√5)):

1. **All 1440 directed adjacency edges have transport element
   g(v,w) = w·v⁻¹ in ONE order-10 conjugacy class of 2I (class 7,
   size 12).** Edges cannot be distinguished by the class of their
   transport; that invariant is constant across the graph.

2. **σ (componentwise Galois √5 → −√5) does NOT preserve 2I.** Only
   24/120 vertices are σ-fixed; the other 96 vertices have σ-images
   outside 2I. Under Elkies' E₈ = icosians ⊕ σ(icosians), σ is the
   map from one 600-cell to the other. σ-covariance of a cocycle
   must therefore be formulated on 2I ⊔ σ(2I), not on 2I alone.

3. **The 12 T_τ-cycles distribute 1/3/8 across three H₄ conjugacy
   classes.** This is the candidate non-trivial structural hook for
   ω.

4. **Naive cocycle ω(v, T_τ(v)) = τ is CONSTANT across all 120 edges
   of the T_τ-orbit graph.** Under this, cycle product = τ^10 = 1
   and the weighted zeta equals the unweighted zeta
   ζ_T(z) = (1−z^10)^(−12).

## Context files

- `docs/pentagonal-torsion-derivation.md` — derivation §1–§8,
  revised 2026-04-24 with surgical edits.
- `papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py` —
  sim for clock, all checks pass.
- `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py` —
  sim that surfaced findings 1–4.
- `papers/paper-xxii/paper-xxii.tex` — two-600-cell conjugate pair,
  E₈ double cover.
- `papers/paper-xxii/scripts/run_icosian_exact.py` — exact Q(√5)
  quaternion arithmetic (14400-table, 9 conjugacy classes, 9
  Euclidean shells).
- `papers/cascade-12d-closure/cascade-12d-closure.tex` — E₈ ⊕ Z[φ]⁴
  lattice closure.
- `insight.md` (auto-included) — conjugate-pair crystallisation
  discussion, god-prime constraint, pentagonal torsion heuristic.

## Specific questions the WO must answer

**For B8':**
- What is the canonical cocycle ω? Choose a specific construction:
  (a) vertex-based weight: ω(v) = φ^{k(v)} where k(v) is derived from
      the 9 Euclidean distance shells (each shell is one 2I-conjugacy
      class, so k(v) is an invariant of v under conjugation in 2I).
  (b) edge-based holonomy on the H₄ bundle: use the fact that 600-cell
      vertices correspond to cosets in H₄/I_stab where I_stab is the
      icosahedral stabilizer, and parallel transport along an edge
      picks up a ±φ^k factor.
  (c) two-600-cell lift: work on 2I ⊔ σ(2I) ⊂ E₈ (240 vertices =
      E₈ roots), with σ the swap. Define ω on the bipartite edge
      structure between the two halves.
- Which construction is minimal in that it depends only on F1 and
  the icosian structure, with no additional choice?
- Under the chosen construction, do the 12 T_τ-cycles acquire
  distinguishable Z[φ]-weights W_C? If not, is there a refined
  cocycle that does?

**For B9:**
- Weighted Artin–Mazur zeta ζ_{T,ω}(z) = ∏_C (1 − W_C z^{|C|})^{-1}
  where the product is over T-orbits C.
- Given the cycle count (12 cycles × length 10), the zeta has the form
  (1 − W₁ z^10)^{-m₁} · (1 − W₂ z^10)^{-m₂} · ... 
  where the W_i are distinct Z[φ]× values and Σm_i = 12.
- Concrete deliverable: compute all W_i exactly for the chosen ω,
  report their Z[φ]-factorisation, and compute ζ coefficients to
  degree 30 for inspection.

**For B10:**
- On the correct substrate (2I, or 2I ⊔ σ(2I)), state and prove:
  σ ∘ T_τ = T_{σ(τ)} ∘ σ (or an orientation-reversed variant).
- Given finding (2) that σ doesn't preserve 2I, this must be stated
  on E₈ with σ as substrate-swap.
- The σ-symmetrised zeta is ζ_{T,ω} · σ(ζ_{T,ω}); state whether this
  is canonically Z-valued (σ-fixed part) or genuinely Z[φ]-valued.

## Required output (SECTIONS A–F, per codex_derive template)

- **A. Insight relevance** — specific insight.md lines.
- **B. Named builds B8', B9, B10 with first steps.**
- **C. Revert strings** if any of the derivation doc needs updating.
- **D. Route alternatives** — if multiple cocycle definitions are
  viable, rank them.
- **E. Exact verification targets** — what sim result would certify
  each build.
- **F. Top three next builds, ranked.**

## Constraints

- **NO DOWNGRADES.** Every open item is a named build with a concrete
  first step. Softening to "conditional" is anti-pattern.
- **Sim must be exact.** Fraction / integer arithmetic. No floats in
  the certification path.
- **Derivation must chain from F1 (permeability)** — no step assumes
  what it is trying to derive.
- Do not touch any paper.tex.

## Out of scope

- Mellin bridge (B11) and Dedekind comparison (B12) are later.
- Prime Detector L map (P5 conjecture) is separate programme.
- God-prime apex constraint is a falsifiability anchor for later.

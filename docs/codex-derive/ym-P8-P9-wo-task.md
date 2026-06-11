# Task: WO for YM P8 + P9 — Der(𝕆) ≅ g₂ with su(3) stabilizer,
# cylindrical SU(3) connection

## Goal

Discharge the two YM-critical hypotheses from classical facts so
`papers/millennium-ym/ym-mass-gap.tex` can be promoted from
"conditional on H_{P8/P9}" to "unconditional from classical
representation theory."

- **P8**: Der(𝕆) ≅ g₂ and the subgroup of Der(𝕆) fixing a specific
  imaginary octonion is su(3). This is a classical theorem of
  Schafer (1966), Jacobson (1971); we just need to state it
  explicitly and cite.
- **P9**: cylindrical SU(3)-connection on the refinement graph of
  the 600-cell. This construction uses P8 + the cascade refinement-
  space framework (P3).
- **P8-sim**: computational verification that a specific imaginary
  octonion has su(3) stabilizer dimension 8 within Der(𝕆) of
  dimension 14 (14 − 8 = 6 = dim(𝕆)/2 boundary, consistent with
  the standard su(3) ⊂ g₂ embedding via octonion triality).

## Context files

- `papers/millennium-ym/ym-mass-gap.tex` — current (β)-conditional
  paper.
- `papers/cascade-derivation/` — P3 refinement spaces, P5 D₄ metric.
- `papers/cascade-algebraic-substrate/` — existing octonion substrate
  derivations.
- Classical references: Schafer, "Introduction to Non-Associative
  Algebras" (1966); Jacobson, "Exceptional Lie Algebras" (1971);
  Baez, "The Octonions" Bull AMS (2002).
- `insight.md` (auto-included) — pair-structure, coupling constant,
  crystallisation triplet.

## Specific deliverables

**P8 derivation:**
1. State octonion multiplication rule (Cayley-Dickson doubling).
2. Define Der(𝕆) = {D : 𝕆 → 𝕆 linear : D(xy) = D(x)y + xD(y)}.
3. Show dim(Der(𝕆)) = 14 (classical).
4. Show Der(𝕆) is simple of type G_2 (classical, via root system).
5. Pick e ∈ 𝕆 imaginary unit (e.g., e = i in standard basis).
6. Show stab_{Der(𝕆)}(e) = {D ∈ Der(𝕆) : D(e) = 0} is a Lie
   subalgebra of dimension 8.
7. Show stab_{Der(𝕆)}(e) ≅ su(3) (standard: the stabilizer of a
   norm-1 imaginary octonion in G_2 acts on the 6-dimensional
   orthogonal complement as SU(3) on ℂ³).

**P8-sim:**
- Explicit 7-dimensional matrix representation of Der(𝕆) on
  imaginary octonions (dim 7).
- Compute Der(𝕆) basis (14 matrices).
- Fix e = i_1 (imaginary unit); compute stab(i_1) = {D : D(i_1) = 0}.
- Check dim(stab(i_1)) = 8.
- Verify Lie-algebra structure matches su(3) (trace, determinant).

**P9 derivation:**
1. Refinement graph Γ of 600-cell (from P3).
2. SU(3) fibre bundle over Γ: at each vertex v, attach su(3)
   stabilizer of distinguished octonion e_v.
3. Connection: on each directed edge (v, w), a parallel-transport
   map from su(3)_v to su(3)_w.
4. Cylindrical structure: connection is determined by an SU(3)-
   valued function on edges modulo gauge transformations.

## Required output (Sections A-F)

Same structure as previous WOs.

## Constraints

- **NO DOWNGRADES.** ym-mass-gap.tex must be promoted from
  conditional to unconditional (or at least to "conditional on
  smaller, more specific hypotheses than H_{P8/P9}").
- Computational verification (matrix rank, Lie bracket structure)
  must use exact arithmetic (sympy, Fraction, or integer matrices).
- Cite Schafer, Jacobson, Baez for classical facts.

## Out of scope

- OS-lift (continuum limit) — separate harder build B_YM_OS.
- Other Millennium papers.

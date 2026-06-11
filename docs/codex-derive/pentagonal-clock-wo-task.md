# Task: audit pentagonal-torsion clock derivation from permeability

## Goal

Produce a named-build work order (B1, B2, ..., Bn) that closes the
pentagonal-torsion clock derivation from the permeability axiom (F1) to
a computable, σ-equivariant weighted Artin–Mazur zeta on the 600-cell
at credibility-bar grade (no downgrades; every open item is a named
build with concrete first step).

## Context files

- `docs/pentagonal-torsion-derivation.md` — Claude's first-pass
  derivation sketch, written today. Contains §1–§9 proposing a chain
  F1 → Z[φ] → σ → Q(ζ₅) → 2I → pentagonal τ → clock T → cocycle ω →
  weighted zeta ζ_T^ω.
- `insight.md` (auto-included) — prior-session content on two 600-cells
  inside E₈, α⁻¹ = 137 + π/87 structural derivation, god-prime
  decomposition 084473 = 137(7×87+8) − 56, pentagonal-torsion
  chirality as irreducible 5-fold Z[φ]-unit obstruction.
- `papers/cascade-correspondence-foundations/foundations.tex` §F1 —
  the permeability axiom as currently published.
- `papers/cascade-12d-closure/cascade-12d-closure.tex` — icosian
  lattice I, Z[φ]⁴ closure.
- `papers/cascade-fine-structure/cascade-fine-structure.tex` —
  α-chain culmination; uses the same 600-cell / 2I / Z[φ] substrate.
- `papers/paper-xxii/paper-xxii.tex` — two-600-cell conjugate pair,
  Coxeter double cover 240/120 = 2, α = coupling.
- `papers/paper-xxii/scripts/run_alpha_oneloop.py` — computational
  verification of the 2-per-vertex Coxeter projection.

## Audit checklist (per step of the draft derivation)

For each of the following from `docs/pentagonal-torsion-derivation.md`,
assess: is the claim derived from its stated source, or is there a
silent assumption / gap?

1. §2.4 σ(φ) = −1/φ — is this the right form of the Galois conjugate?
2. §3.3 Pentagonality is the minimal n with Q(ζ_n) ⊃ Q(√5) for real
   quadratic — is the argument complete for n ∈ {3,4,5,6}?
3. §4.3 Torsion character τ(u) = u·σ(u) — is this a standard object in
   algebraic number theory, and if so, under what name? (Claude drafted
   it without citation; verify.)
4. §4.4 The factor (−1)^n in σ(φ^n) is the pentagonal asymmetry —
   Claude claims this is a \emph{proof} of chirality obstruction.
   Is the claim supported or is it a restatement?
5. §5.2 The pentagonal rotation element τ ∈ 2I with τ⁵ = −1,
   τ¹⁰ = 1 — is this uniquely determined by its order and position in
   the icosian adjacency, or is there a choice being made?
6. §6.1 T(v) = τ·v as the canonical clock — is left multiplication the
   right choice (vs. right multiplication vs. conjugation), and is the
   resulting self-map distinguishable from a classical quasicrystal
   translation dynamic (Bellissard-Kellendonk-Sadun)?
7. §6.3 The cocycle ω(v,w) = φ^{k(v,w)} — is k(v,w) well-defined
   uniquely, or does it depend on a frame choice that has to be fixed
   globally (H₄-equivariance vs σ-covariance interaction)?
8. §7.2 The weighted Artin–Mazur zeta ζ_T^ω(z) ∈ Z[φ][[z]] — is it
   automatically σ-symmetric (if σ acts on the coefficients), and does
   it admit a Mellin pairing that maps σ-fixed coefficients to points
   of the critical line Re(s) = 1/2?

## Required outputs (gap-report, no downgrades)

### Section A (insight relevance)
Cite exact insight.md line ranges that bear on this derivation,
distinguishing:
- already in cascade papers (with paper§line),
- only in insight.md / prior-session (with line range).

### Section B (named builds)
For each gap, produce a build Bn with:
- Object/map/lemma required (domain, codomain, type).
- What it bridges.
- Source route: classical literature (give citation) / new derivation /
  computational verification / alternative route.
- Concrete first step.

### Section C (revert strings, if any)
If the draft derivation has a wrong claim, give exact string-level
fixes `at file:line replace X with Y`. Do not soften; correct.

### Section D (route alternatives)
If there are alternative derivation routes for any build (e.g. a
different definition of the cocycle, a different choice of clock
generator, a different zeta variant), list them with trade-offs.

### Section E (computational verification targets)
For each build, state a specific computable check that would certify
it. The user's standard: sims must use exact arithmetic (Fraction, int),
refuse to hand-tune.

### Section F (top 3 next builds)
Rank the top 3 builds by importance for reaching an undismissable
pentagonal-clock construction, with file:line anchors.

## Constraints

- **NO DOWNGRADES.** Never suggest "demote to conditional" or "mark as
  open". Each gap becomes a named build with a concrete first step.
- **Cite literature** for classical steps (Washington cyclotomic fields,
  Neukirch algebraic number theory, Conway-Sloane sphere packings for
  the icosian construction, Elkies 1999 icosian E₈ paper).
- **Sim targets must be exact.** Any computational claim uses
  `fractions.Fraction`, integers, or symbolic arithmetic. No floats in
  the certification path.
- **Derivation chain must be complete from F1** — no step assumes what
  it is trying to derive.

## Out of scope

- Do not attempt to prove Riemann Hypothesis.
- Do not evaluate ζ_T^ω on the critical line.
- Do not revise rh-formal.tex or any Millennium paper.
- Do not touch any paper.tex; this WO is about the derivation doc and
  the accompanying sim script only.

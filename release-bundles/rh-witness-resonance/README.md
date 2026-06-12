# A Conditional Substrate Localisation of the Hilbert–Pólya Problem

**If a self-adjoint operator with the stated substrate constraints exists on
an infinite-dimensional lift of V₆₀₀'s τ-fixed block, whose positive
eigenvalues are in multiplicity-respecting bijection with ζ's
upper-half-plane non-trivial zeros, then RH follows — by the classical
Hilbert–Pólya argument. Whether RH conversely guarantees an
operator meeting the substrate constraints is open; that converse is the
localisation target, not a result.**

> **Version note.** v1 of this paper ("RH as Witness Resonance") claimed a
> three-way *equivalence* between RH and "substrate spectral completeness".
> Adversarial review (2026-06-12) found that one direction assumed its own
> conclusion, a second clause was definitional, and the finite 94-dimensional
> block cannot carry the infinite spectrum the statement requires. v2
> withdraws the equivalence and restates the content honestly as a
> *conditional localisation*: a constraint list plus the one classical
> implication. The constraint list — ground state at V_min, commutation with
> closure-flow and with the Hecke action of the Hilbert modular lift — is
> the paper's contribution.

## The statement in one paragraph

The substrate framework (siblings below) established the witness invariant
W = V_min as the closure-flow attractor and an embedding of the critical
line into V₆₀₀'s τ-fixed block. This paper defines a **substrate lift**
(a separable infinite-dimensional Hilbert space anchored to the τ-fixed
block, carrying extensions of the closure-flow and Hecke actions) and a
**substrate-localised generator** on it, and proves the one classical
direction: such a generator whose positive eigenvalues are in
multiplicity-respecting bijection with the upper-half-plane non-trivial
zeros (ρ = 1/2 + i·t; the conjugate lower half follows by symmetry) would
imply RH (self-adjointness forces real spectrum; no novelty is claimed for
the deduction). Everything else —
the existence of a lift, the existence of the generator, the converse —
is stated as the open target it is. Without the substrate constraints the
converse is trivial (a diagonal operator does it), so the entire content of
the localisation lies in the constraints.

## What is and is not established

**Established:** the constraint list (the substrate-localised generator
definition); the classical implication (the paper's Proposition); an
analogous conjectural target for L(s, χ₅) on the τ-paired block.

**Not established:** RH; GRH for χ₅; the existence of a substrate lift or of
the generator on any lift; the converse of the implication (v1's claimed
equivalence — withdrawn); any new computation.

## Provenance note

This bundle contains **no simulations and no new computations**. All
structural counts used (120 vertices, the 94+13+13 Galois split, dim
V_min = 1) are imported from the cited sibling artifacts:
[critical-line-pullback](../critical-line-pullback/) (computational
findings with sims) and the
[the-24-600-spectral-bridge](https://github.com/vfd-org/the-24-600-spectral-bridge)
programme. This paper is a specification document over those results.

## Bundle contents

```
rh-witness-resonance/
  paper/
    rh-witness-resonance.tex    ← the localisation paper (v2)
    rh-witness-resonance.pdf
    references.bib
  README.md (this file)
  CHANGELOG.md
  LICENSE
```

## Position in the programme

```
icosian-triad-v600        →  substrate, C_φ, L-function identity
critical-line-pullback    →  computational findings on the critical-line embedding
observer-attractor-theorem→  Witness Invariant Theorem (W = V_min)
rh-witness-resonance      →  THIS PAPER: conditional Hilbert–Pólya
                             localisation target (specification)
```

The current canonical prime/RH surface of the programme is
[closure-positivity-lab](https://github.com/vfd-org/closure-positivity-lab)
(the realization, the L-function provenance, the positivity wall, the prime
phenomena ledger); this paper is upstream interpretive material relative to
that repo and is held to the same scope discipline.

## Status

Pre-peer-review open research preprint, v2.0.0-rc1 (reframed after
adversarial review). Not independently validated. **No claim of RH or GRH
settlement is made anywhere in this document, and no equivalence with RH is
asserted.**

## Licence

Paper and prose: CC BY 4.0.

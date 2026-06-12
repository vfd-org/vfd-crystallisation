# Deliverable G — archimedean–adelic completion analysis

The core conceptual deliverable. Answers, grounded in the computed `H`/`R` split.

## 1. What does the archimedean gamma factor contribute to positivity?

It contributes a **positive-definite quadratic form** `H = ARCH + POLE`
(`K_arch` PSD, verified). The gamma factor `Γ_ℝ(s)=π^{-s/2}Γ(s/2)` enters via
`Re ψ(1/4 + i r/2) − log π`, and the resulting kernel is positive. The
archimedean place is where the positivity *lives*.

## 2. Can the prime side alone ever be positive?

**No.** `R = PRIME` is indefinite (min eig −0.81). The Euler product side,
detached from the completion, has negative directions. There is no positivity in
the primes by themselves.

## 3. Does positivity require the completed adelic object?

**Yes.** Positivity is `H ⪰ R`: the positive *archimedean* capacity must dominate
the indefinite *prime* load. Drop the archimedean place and positivity is
impossible. So the relevant object is the **completed** `ξ(s)` (all places,
archimedean + finite), i.e. the adelic object — not `ζ(s)` alone. This is the
precise sense in which "the completion is mandatory" (and why every prior naive
prime-only resonance attempt failed).

## 4. Can VFD geometry model the gamma factor as boundary capacity?

The VFD "boundary capacity" maps exactly onto `H`. But the model is a
*re-description*: `H` is the digamma/archimedean kernel, and calling it "boundary
capacity" does not change it or supply new positivity. The VFD language is
faithful but not generative here.

## 5. Does the completed object behave like a closed resonator?

In the precise sense that its zeros are the spectrum (explicit formula) and the
positivity `H ⪰ R` is a "capacity ≥ load" closure condition — yes, as an analogy.
But the analogy carries no theorem: the resonator's self-adjointness is the open
part.

## 6. Is there a natural Hilbert space in which the completion is self-adjoint?

This is the Hilbert–Pólya question. We have a finite self-adjoint Weil operator
`K` (Deliverable H), self-adjoint *by construction*, with `K ⪰ 0 ⇔ RH`. A
**canonical** self-adjoint operator on a Hilbert space whose **spectrum is the
zeros** — built from the completion, not from the zeros — is **not** known.
Connes' adele-class space is the leading candidate; the positivity there is again
RH-equivalent.

## 7. Does this point toward an archimedean–adelic Hilbert–Pólya operator?

Yes — it localises the missing object precisely: a self-adjoint operator whose
positivity is the dominance of the (positive) archimedean capacity over the
(indefinite) prime load, realised on the adele-class space. That is exactly the
Connes/Weil programme, and its positivity step is the wall. This WO **sharpens**
the target (capacity-dominates-load on the completion) without supplying the
operator.

## Distinction summary

| layer | object | positivity |
|---|---|---|
| prime side only | `R` (Euler product) | indefinite — never positive alone |
| archimedean completion | `H` (gamma + pole) | **positive kernel** |
| completed closure form | `Q = H − R` | PSD `⇔` RH (the wall) |

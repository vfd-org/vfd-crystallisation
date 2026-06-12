# Deliverable J — claim boundary

## What was proven
Nothing new about RH. Standard facts were re-derived and verified numerically:
the explicit formula, the positivity of the archimedean kernel, the
indefiniteness of the prime kernel, and the RH-equivalence of Weil positivity.

## What was computed
- The Weil Gram from the prime+archimedean side, matching the zero side to
  machine precision (with a truncation study proving independence).
- The canonical split `Q = H − R`: `H` (archimedean capacity) **PSD**, `R`
  (prime load) **indefinite**.
- The norm-square factorisation `Q = |Ah|²` (Cholesky) on PSD bases, with
  **off-line teeth**: PSD at δ=0 (the critical edge), lost for δ>0.
- The Weil kernel/operator `K`, Hermitian, PSD on bases, `K⪰0 ⇔ RH`.

## What remains RH-equivalent
Everything at the universal quantifier: `Q⪰0 ∀h`, `H⪰R ∀h`, `K⪰0` on the full
admissible class — each is RH.

## Is there a new object?
**No new theorem-bearing object.** The `H−R` capacity decomposition and the
norm-square diagnostic are canonical and explanatory, but they are the classical
Weil structure. VFD's closure language (capacity vs pressure) is a faithful
re-description, not a new mechanism.

## Is any object canonical?
Yes: `H = ARCH+POLE` and `R = PRIME` are canonical (the explicit-formula terms),
and the archimedean positivity of `H` is a real structural fact. The missing
canonical object — a self-adjoint operator with the zeros as spectrum, derived
from the completion — is **not** constructed.

## Was positivity proved universally?
**No.** Only on finite tested bases (diagnostic), where the on-line Gram sits at
the positivity **edge**.

## Classification

```
GRADE 2 — candidate bridge object (canonical H−R capacity decomposition with a
          positive archimedean kernel), which REDUCES to Weil positivity.
```

Not Grade 3: the reduction `H⪰R ⇔ RH` is the **classical** Weil criterion, not a
new VFD-produced reduction. Not Grade 4: no universal positivity theorem.

## Mandatory statement

> This work does not prove RH. It does not establish universal Weil positivity
> for the full admissible test-function class. It provides a canonical,
> non-circular, completion-aware decomposition of the Weil functional
> (`Q = H − R`, `H` a positive kernel, `R` indefinite) and a faithful norm-square
> diagnostic with off-line teeth — all RH-equivalent at the universal quantifier.
> `rh_claim: NO_RH_PROOF_CLAIMED`.

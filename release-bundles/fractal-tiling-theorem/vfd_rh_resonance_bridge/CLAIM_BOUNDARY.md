# Deliverable — CLAIM BOUNDARY

## Grade

```
GRADE 2  —  CANDIDATE BRIDGE OBJECT
(not Grade 3 "new reduction", not Grade 4 "proof")
```

A non-circular candidate closure form is defined and connects to known RH
criteria: the **Weil functional** `Q(h)=W(h)=ARCH(h)−PRIME(h)`, with

- a **parameter-free, geometric prime side** (the icosian Brandt eigenvalues
  `a_q`, proven equal to point counts out of sample, zero fitting), and
- a **finite self-adjoint resonance operator** `R=B(P)` whose real spectrum is
  the `a_q` (the Hilbert–Pólya picture, realised on the Hecke side).

`Q(h) ≥ 0` for all `h` is **exactly RH** for this L-function. We verify it on
every tested `h` (archimedean-dominated regime) and locate the wall precisely.

## Why not higher

- **Not Grade 3.** Grade 3 would be a *new* proof-equivalent reduction. The
  reduction `Q≥0 ⟺ RH` here is the *classical* Weil criterion — VFD did not
  produce the reduction; it produced a parameter-free geometric instantiation of
  it. No simplification of RH was achieved.
- **Not Grade 4.** No positivity/self-adjointness theorem is proved. The
  universal positivity quantifier (equivalently, the infinite operator
  `R_∞=R_∞^*` for the zeta zeros) is the open Hilbert–Pólya/Weil wall, and there
  is a concrete obstruction (the β=4/β=2 Dyson-class mismatch).

## Why not lower

- **Not Grade 0/1.** It is more than reframing or a diagnostic: the resonator
  `(H,R,Θ,∂,Q)` is canonical (not chosen/fitted), its operator is genuinely
  self-adjoint with the arithmetically-correct spectrum, and it plugs directly
  into a standard RH criterion. Another mathematician can attack or reject it on
  standard terms.

## What was honestly killed (Deliverable C / validation tests)

- `L1/L2` prime-field mirror imbalance: symmetric about `σ=1/2` **by
  construction** → detects nothing (decorative, circular).
- `L3 = ξ(s)−ξ(1−s)`: **identically zero** (functional equation), `≤1e−27`
  everywhere including off-line and at zeros → detects nothing (forced).
- Naive prime field `P_X(σ,t)`: weak (`|z|<2`) and circular (`P_X` is the
  leading term of `log ζ`) → not a usable diagnostic.

## What is genuinely real (and known)

The prime fluctuation `(ψ(x)−x)/√x` has spectral peaks **at the zeta zeros
`γ_n`** (8/8 matched, `prime_resonance_field.py` B2; plot in `results/plots/`).
This is the explicit formula — real, non-circular — but it is the known
prime↔zero duality, and it does not simplify RH.

## Boundary statement

> This work determines that the VFD resonance/closure framing of RH formalises
> into one non-circular candidate bridge object — the Weil functional with a
> parameter-free geometric prime side and a finite self-adjoint Hecke operator —
> which is exactly the classical Weil/Hilbert–Pólya criterion. It does **not**
> prove RH, does **not** simplify RH, and does **not** produce a new reduction.
> The naive resonance and leakage functionals are decorative or circular. The
> residual gap is the universal positivity quantifier (the infinite
> self-adjoint operator), with a concrete β=4/β=2 symmetry-class obstruction.
> `rh_claim: NO_RH_PROOF_CLAIMED`.

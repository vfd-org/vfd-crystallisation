# Deliverable E — the candidate arithmetic resonator and its theorem targets

## The resonator `A_VFD/RH = (H, R, Θ, ∂, Q)`

Defined precisely enough that another mathematician can attack or reject it.

| component | definition | canonical or chosen? | input data | assumes RH? |
|---|---|---|---|---|
| `H` | the Brandt module `C[Cl(O)]` of the Eichler order of level `(5φ−2)` in the icosian algebra `B=(−1,−1/Q(√5))`; here `dim H = 2` | **canonical** (class number 1) | the icosian ring (geometry) | no |
| `R` | the Hecke/Brandt operators `B(P)`, `P ∤ (5φ−2)` | **canonical** | reduced-norm-`ϖ_P` icosians, geometric | no |
| `Θ` | the involution `s ↦ 1−s`; on `H`/`R` the Atkin–Lehner / functional-equation symmetry | canonical | functional equation | no |
| `∂` | the archimedean completion: gamma factor `Γ_ℂ(s)²`, conductor `775=31·disc(K)²` | canonical | the L-function's data | no |
| `Q` | the Weil functional `W(h)=ARCH(h)−PRIME(h)` (the closure energy) | canonical | `∂` and the `a_P=spec(R)` | no |

**Verified facts about this resonator (parameter-free, no fitting, no zeros used
in construction):**
- `R` is **self-adjoint** in the mass measure `μ=(20,12)` (defect exactly 0);
  its spectrum is real and equals the cuspidal Hecke eigenvalues `a_P`.
- The `a_P` equal the independently point-counted Frobenius traces, out of
  sample (prior WO) — so `R` is the genuine Hecke operator, not a fitted stand-in.
- `Q=W(h)` is assembled with a fully geometric prime side; the ζ-calibrated
  machinery reproduces the known zeta zeros to `1e−6`.

## What theorem would make RH follow

Exactly one of the following, **none currently provable**:

```
(T1)  Q[f] = W(h) ≥ 0   for all test functions h of positive type        ⟹  RH(L)
(T2)  R_∞ = R_∞^*       (a self-adjoint operator whose spectrum is the γ_n) ⟹  ρ = 1/2 + iγ
(T3)  L(σ,t)=0          (a canonical leakage functional)  ⟹  σ = 1/2
```

- **(T1)** is the Weil criterion. We have `Q` and its geometric prime side; the
  universal quantifier over `h` is the open part — it **is** RH. (Grade-3
  classical reduction; not VFD-novel.)
- **(T2)** is Hilbert–Pólya. We have a finite self-adjoint `R` for the *Hecke*
  spectrum; the infinite `R_∞` for the *zeta zeros* is the open object. The
  obstruction is concrete: the icosian substrate is Dyson class β=4 (GSE), the
  zeta zeros are β=2 (GUE) — a symmetry-class mismatch (`DIVISION_ALGEBRA.md`);
  the archimedean/adelic completion onto the β=2 footing is Tier-3 open.
- **(T3)** No canonical non-circular `L` was found (Deliverable C): the prime-
  field imbalance is symmetric-by-construction (decorative); the completed-field
  defect `ξ(s)−ξ(1−s)` is identically zero (detects nothing). The only surviving
  "boundary − residual" object is `Q=W(h)` itself, i.e. (T1).

## The honest gap

`Q[f]=|A_∞ f|²` with a geometrically-derived `A_∞` would prove RH — and writing
that square **is** the proof, not a step toward it. We can write `A` for the
finite coefficient-side forms (`D1`, `D3`); we cannot derive `A_∞` for the
zero-side form (`D2`/T1). That single derivation is the whole problem.

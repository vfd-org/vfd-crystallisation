# WO-RH-BRANDT-POSITIVITY-WALL-001

**The boundary-resonance bridge object, built parameter-free; the exact wall located.**

## What was asked

Build the bridge `prime irreducibility -> completed boundary resonance ->
self-adjoint closure -> Re(s)=1/2` as far as it rigorously goes, parameter-free,
and locate precisely where it stops — without constructing the (currently
impossible) Hilbert-Polya operator for the zeta zeros, and **without claiming a
proof of RH**.

## The bridge object is not missing — it is the Weil functional

The object the resonance picture is reaching for already exists and is a theorem
(Weil's explicit formula). For an L-function,

```
W(h)  =  ARCH(h)         <- completed / archimedean "mirror boundary"  (Theta: s<->1-s)
       -  PRIME(h)        <- prime "residual" (the log p emitters)
      ( =  sum over zeros  h(gamma) )
```

and **Weil's criterion**: `RH for L  <=>  W(h) >= 0 for every test function h of
positive type`. This is exactly the requested shape

```
PrimeResidual(s) + MirrorBoundary(1-s) = ClosedMode(s) = zero,
ClosedMode  =>  Re(s) = 1/2   <=>   W >= 0  for all h.
```

So the bridge from primes to self-adjoint closure on the critical line is
unconditional; the only open part is the single universal positivity quantifier,
which **is** RH.

## The "arithmetic resonator" A_VFD, made concrete

The proposed `A_VFD = (H, R, partial, Theta, Q)` is realised here by objects we
actually have (not fitted):

| A_VFD slot | concrete object (this repo) | status |
|---|---|---|
| `H` Hilbert space of modes | the Brandt module `C[Cl(O)]`, dim `h=2` | built (geometric) |
| `R` resonance operator | the icosian **Brandt/Hecke operators `B(P)`** | built, **self-adjoint** (mu=orbit sizes) |
| `partial / Theta` mirror boundary | functional equation `xi(s)=xi(1-s)`, archimedean gamma factor | unconditional |
| `Q` closure energy / positivity | the **Weil functional `W(h)`** | unconditional object; positivity = RH |
| irreducible emitters | primes, frequencies `log N(P)`, eigenvalues `a_P` | **parameter-free** (geometric `a_P`) |

The genuinely new ingredient: the prime residual `PRIME(h)` is assembled
**entirely from the geometric Brandt eigenvalues** `a_q` (`route_b/geometric_aP.py`
-> `data/geometric_aP.json`): the cuspidal spectrum of the self-adjoint icosian
Brandt operator, 32 prime ideals `N(q) <= 150`, all self-adjoint-sourced, all
Ramanujan-bounded, **zero point-counting and zero fitting on this path**. The
prior WO proved these `a_q` equal the independent point counts out-of-sample.

## What is solid (parameter-free, verified)

1. **Calibration.** The identical bridge machinery, run on Riemann zeta, equals
   the sum over the known zeta zeros to rel.err `1e-2 .. 1e-6` (sigma `3..6`).
   The constants (gamma factor, conductor `775 = 31*disc(K)^2`, pole) are correct.
2. **Parameter-free prime residual.** Every `a_q` in `PRIME(h)` is an eigenvalue
   of a self-adjoint icosian Brandt operator — geometric, Ramanujan-bounded.
   This is the first time the Weil prime side here is sourced from the geometry
   rather than from direct curve point-counting.
3. **Negative control with teeth.** Feeding the Eisenstein bookkeeping channel
   `a_q = N(q)+1` into the same residual violates Ramanujan at all 32 primes
   (`|a_q| > 2 sqrt N(q)`), so the Satake angle is undefined and the object is
   not a positivity-valid L-function. The **cuspidal** geometric `a_q` are
   exactly what the bridge requires.
4. **Bridge holds on every test:** `W(h) >= 0` for all tested `h`.

## What is NOT crossed (the honest wall)

- **Positivity quantifier = RH.** `W(h) >= 0` for *all* `h` is RH for this
  L-function (`= GRH`). We test finitely many `h`; the universal quantifier is
  the wall, and it is **RH-equivalent, not a VFD-specific gap**.
- **Archimedean-dominated regime (honesty).** In the reliable regime
  (`sigma >= 3`, where the zeta gate is valid) the prime residual is tiny vs the
  archimedean boundary (`prime/arch` ratio `1e-4 .. 1e-16`). So `W >= 0` here is
  **consistent with** RH but is **not a sharp test** of the positivity
  quantifier: it is dominated by the (manifestly positive) archimedean term.
  Sharper tests need primes far beyond the Brandt computation's reach (narrow
  test functions), which is a truncation limit, not a result.
- **Symmetry-class gap (for actual zeta).** The icosian substrate is Dyson class
  beta=4 (GSE); the zeta zeros are beta=2 (GUE) (`DIVISION_ALGEBRA.md`). The
  self-adjoint operator we have is for one automorphic L-function's Hecke
  spectrum; the archimedean/adelic completion that would put the **zeta zeros**
  themselves on a self-adjoint footing is Tier-3 open (`ADELIC_SCALING.md`).

## Verdict

```
RH_EQUIVALENT_PARAMETER_FREE_APPROACH
rh_claim: NO_RH_PROOF_CLAIMED
```

VFD geometry supplies **every ingredient of the Weil bridge with zero fitting** —
the self-adjoint resonance operator (Brandt), the irreducible emitters (primes /
geometric `a_q`), the mirror boundary (functional equation) — and the bridge
holds on every test. The residual gap is exactly the RH-equivalent positivity
quantifier, which cannot be closed without the operator/positivity proof that is
currently impossible. This is the **closest parameter-free approach** to RH the
geometry reaches: it proposes the geometric *origin* of the spectral structure,
it does not prove the line.

## Reproduce

```bash
python3 route_b/geometric_aP.py     # geometric a_q cache (Brandt), ~few min
python3 route_b/weil_wall.py        # bridge functional, gate + positivity + control
```

Outputs `data/geometric_aP.json`, `data/weil_wall_results.json`.

## Boundary statement

> This work assembles the Weil boundary-resonance bridge for an icosian
> L-function with a fully geometric, parameter-free prime side, and verifies it
> on every test. It does **not** prove RH. A pass establishes that VFD geometry
> supplies the arithmetic/spectral ingredients of the bridge without fitting; RH
> still requires the separate universal positivity / self-adjointness step,
> which is untouched here.

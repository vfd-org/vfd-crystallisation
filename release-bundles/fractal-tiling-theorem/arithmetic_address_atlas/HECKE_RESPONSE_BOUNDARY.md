# Hecke Response Boundary (family B5)

**The address map stops at splitting.** Two tests, both negative — and that
negative is the load-bearing boundary of the whole atlas.

## Test 5 — ideal selection (PROVEN negative)
`q ∣ Φ_d(2)` depends only on `ord_q(2)`, a rational invariant → **σ-invariant** →
cannot distinguish `𝔮` from `𝔮'`. Example: `q=11, ord=10 (5∣ord)` → the two ideals
give `a ∈ {−4, 4}` — one order-sector, two distinct eigenvalues. The cyclotomic
address selects the **rational prime only** (Theorem 5).

## Test 6 — Hecke bias (EMPIRICAL negative)
Split primes (level-31 form) by `5 ∣ ord_q(2)`, Sato–Tate `x = a_q/2√q`:

| group | n | mean | std |
|---|---|---|---|
| golden (`5∣ord`) | ~128 | −0.016 | 0.463 |
| control (`5∤ord`) | ~162 | +0.025 | 0.498 |

Difference ≈ **0.7σ** — noise. The order-sector carries **no** Hecke information
beyond splitting (`ord_q(2)` ⊥ the form's Galois representation; Sato–Tate).

## Consequence
```
cyclotomic order → Galois splitting   [REAL, Grade C]
        |  BREAKS HERE
        → prime ideal 𝔮 vs 𝔮'        [coarse, Test 5]
        → Hecke value a_𝔮             [decoupled, Test 6]
        → L-function / positivity      [not reached]
```
The RH-relevant layer (Hecke eigenvalues / L-spectrum) is **decoupled** from the
cyclotomic-order address — the precise reason this real address structure does not
advance RH. Atlas grade ceiling for address-derived objects: **D** (and E only for
the form as a whole, never via the address).

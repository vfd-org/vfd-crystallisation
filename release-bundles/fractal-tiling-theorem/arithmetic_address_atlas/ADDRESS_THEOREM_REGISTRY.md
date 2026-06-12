# Address Theorem Registry

All laws used by the atlas. Status: **all are standard, elementary number theory**
(registered here for reuse, not claimed as new). Each is machine-checked in the engines.

## Theorem 1 — Cyclotomic order law  [PROVEN, standard]
If `q ∣ Φ_d(a)` with `q ∤ d` and `q ∤ a`, then `ord_q(a) = d`; hence `d ∣ q−1`.
Exceptional case: a single prime `q ∣ d` may divide `Φ_d(a)` (to first power).
*Engine:* `golden_split_classifier.classify_phi` (intrinsic flag).

## Theorem 2 — Golden split law at base 2  [PROVEN, corollary of T1]
If `5 ∣ d`, `q ∣ Φ_d(2)`, `q ∤ d`, then `q ≡ 1 (mod 5)`, hence **`q` splits in `Q(√5)`**.
*Verified:* golden split-fraction = **1.000** vs control **0.30** (this run).
*Engine:* `golden_split_classifier.split_fraction`.

## Theorem 3 — Minus-sibling route  [PROVEN, standard]
`2^n − 1 = ∏_{d∣n} Φ_d(2)`. So if `5 ∣ n` then `Φ_5(2)=31` is a factor: `31 ∣ 2^n−1`.
*Verified:* `31 ∣ 2^136279840−1` (since `5 ∣ 136279840`).

## Theorem 4 — Plus-sibling route  [PROVEN, standard]
`2^n + 1 = ∏_{d∣2n, d∤n} Φ_d(2)`. For `n = 2^k·m` (m odd), the active `d` have
`v₂(d) = k+1`; the smallest is `d = 2^{k+1}`, giving the forced factor `2^{2^k}+1`.
*Verified:* God `n=2^5·…` → `d=64` → `2^32+1` divides `2^n+1`; `31 ∤ 2^n+1`.

## Theorem 5 — Routing boundary  [PROVEN, σ-invariance]
`q ∣ Φ_d(2)` depends only on `ord_q(2)`, a rational-integer invariant, hence is
invariant under the Galois conjugation `σ: √5↦−√5` that swaps the conjugate prime
ideals `𝔮 ↔ 𝔮'`. Therefore the cyclotomic address **cannot select an individual
ideal** — it determines the rational prime only.
*Engine:* `ideal_refinement_qsqrt5.address_selects_ideal`.

## Empirical boundary — Hecke decoupling  [EMPIRICAL, expected from Sato–Tate]
Split primes grouped by `5 ∣ ord_q(2)` show **no bias** in the level-31 Hecke
eigenvalue (Sato–Tate `x = a_q/2√q`): golden mean −0.016, control +0.025, ~0.7σ.
The cyclotomic-order address is **decoupled** from the Hecke/spectral layer.
*Engine:* `hecke_response_analyser.hecke_by_order_sector`.

---
**Net:** the address laws are real and reusable, but they terminate at the
**rational-split-prime (Grade C)** layer; the ideal (D-fine), Hecke (D/E), and
positivity (F) layers are not reached by the cyclotomic address.

# Out-of-Sample Icosian Brandt Test (WO-VFD-OOS-ICOSIAN-BRANDT-001)

Tests Lee's hypothesis — *is the icosian/600-cell geometry the real plumbing under the
arithmetic?* — in the only honest way: does the geometry generate the genuine Hecke
eigenvalues **without fitting**, on primes it was never shown?

## Setup
- **Target (genuine, parameter-free):** the norm-31 cuspidal Hilbert newform over ℚ(√5),
  eigenvalues `a_P` from brute-force point-counting on the elliptic curve `31.1-a1`
  (`sims/sim_genuine_eigenvalues.py`). No LMFDB eigenvalue table, no fitting. 44/44 satisfy
  Ramanujan `|a_P| ≤ 2√N(P)` → genuinely **cuspidal** (the RH-bearing object).
- **In-sample** = primes of norm ≤ 41 (where the prior substrate file had entries);
  **out-of-sample** = norm 59–200.

## Result (`run_test.py`)
- The geometry's only **computable parameter-free** channel — the level-1 icosian theta is
  Eisenstein, eigenvalue `N(P)+1` — matches the cuspidal target **0/12 in-sample, 0/32
  out-of-sample**. It grows like `N`; the target obeys Ramanujan. It is the **wrong object**
  (exactly what the circle-test audit warned).
- The channel that *could* match — the **icosian Brandt action at level (5φ−2)** — is
  **BLOCKED**: no Magma, and SAGE has no maximal order / Brandt module over ℚ(√5).
- We **refuse to fit** a map to the target (the prior error). So:

> **VERDICT: NOT DEMONSTRATED (cuspidal channel blocked).**

## Honest reading
The geometry reproduces the **Eisenstein** arithmetic parameter-free
(`Θ_𝓘 = ζ_K(s)ζ_K(s−1)`, verified earlier) — the bookkeeping/divisor layer. The
**cuspidal** layer, where the L-function and RH live, is **not yet shown to be geometric**.
That gap is precisely "what we are missing."

## What would unblock it
(a) Magma's quaternion-order / HMF over ℚ(√5); or (b) the from-scratch icosian
Eichler-order class enumeration at level (5φ−2) (scaffold: `route_b/brandt_level31.py`;
acceptance gate: Brandt-module dimension `h=2` via the Eichler mass formula), then compare
ITS cuspidal eigenvalue to `a_P` out-of-sample. **Even a match is not a proof of RH** —
positivity (the Connes wall) remains.

Run: `python3 run_test.py`

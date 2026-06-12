# WO-RH-ARITHMETIC-HORIZON-INVARIANT-001 — Arithmetic Horizon Invariant (report)

**Status:** run; **hypothesis tested and NOT supported — the horizon envelope is
GENERIC, not a prime-specific invariant; no God-Prime envelope.** One sharp
positive by-product. Sim: `route_c/arithmetic_horizon/rh_arithmetic_horizon_invariant.py`.
**No proof of RH; no φ; no zeros in construction; no God Prime claimed.**

## 1. Summary
Tested whether the maximal-pressure (μ≈1) mode of `K = H^{−½}RH^{−½}` defines a
**stable, cutoff-independent, prime-specific** pressure envelope `Π(log n)` — a
candidate new "arithmetic horizon invariant" / "God-Prime envelope." **It does
not.** The envelope is (a) **trivial** — essentially the first 3–4 primes
(participation ratio 2.68); (b) **partly a basis artefact** — its shape drifts
with the test-function width; and, decisively, (c) **generic** — a smoothed-PNT
surrogate (`1/√n` on *every* integer) **reproduces the envelope shape (overlap
+0.96)** and in fact **overshoots the contraction (`μ_max = 1.26 > 1`)**. The
prime-specific content is therefore **not** the envelope but the **cancellation**
that pulls the pressure from 1.26 down to 0.9998 ≤ 1 — i.e. the explicit-formula
fluctuation, which is exactly RH (the `−ζ′/ζ` structure of CONTRACTION-002).

## 2. Why this started route_c, and where it lands
route_b ended with `RH ⟺ ‖K‖ ≤ 1`, blocked because the prime symbol `−ζ′/ζ` is
singular at the zeros (CONTRACTION-002). This WO asked whether the *horizon
modes* hide a new invariant beyond that wall. **Answer: no new invariant.** The
result *re-confirms* the route_b wall from a fresh angle: the prime-specific part
of the horizon law is precisely the fluctuation/cancellation = RH, not a stable
envelope. route_c does **not** open a new theory; it sharpens *why* route_b's
wall is the real one.

## 3. Anti-circularity
`H`, `R`, `K`, all horizon modes, and `Π(log n)` built from primes + prime
powers + archimedean digamma + pole only. **No zero heights, no Cayley phases,
no zero-side Gram, no fitting to zeros, no RH/Weil/Li assumed.** Known zeros
appear nowhere (not even in validation here).

## 4. Horizon / black-hole analogy — *interpretation only*
The picture "prime pressure approaches boundary capacity but never exceeds it"
is evocative, but the data show the analogy is **metaphor, not new structure**:
there is no stable horizon envelope to carry a holographic law. What *is* true
(form level) is the bound `Q_prime[f] ≤ Q_capacity[f]` (= ‖K‖≤1), already known.

## 5. Definitions
`H = A + P` (archimedean + pole capacity, PSD), `R` = prime-pressure,
`K = H^{−½}RH^{−½}`, `C[f] = ⟨f,Rf⟩/⟨f,Hf⟩`. Horizon mode = top eigenvector of
`K` (μ_max). Envelope `q_n[f] = Σ_ij f_i f_j r_ij(n)`, `Σ_n q_n = Q_prime[f]`;
`Π(log n)` = `q_n` binned in `log n`.

## 6. Results

**[1] Real-prime horizon mode (N=12, S=3).** `μ_max = C[f] = 0.99979`,
`Q_prime = 0.9998`, `Q_cap = 1.0000`. Envelope **peak at n=2** (log n=0.69),
centroid 0.97, entropy 1.12, **participation ratio 2.68**. Pressure carriers:

| n | 2 | 3 | 4 | 5 | 7 | ≥8 |
|---|---|---|---|---|---|---|
| q_n | +0.497 | +0.444 | +0.114 | −0.054 | −0.001 | ≈0 |

→ the entire "envelope" is `n = 2,3,4,5`. **Not a rich global object.** Note the
**sign change** at n=5: the envelope already carries the cancellation.

**[2] Basis-width artefact test.** Peak pinned at n=2 (smallest prime = a
boundary), but centroid and μ drift with width S:

| S | μ_max | centroid | (W) |
|---|---|---|---|
| 2.0 | 1.0000 | 1.06 | 1.41 |
| 3.0 | 0.9998 | 0.97 | 2.12 |
| 4.0 | 0.9978 | 0.89 | 2.83 |

→ shape **tracks the basis** (partial artefact). The margin `1−μ` is itself
basis-dependent — not a fundamental horizon number.

**[3] N-scaling.** `μ_max`: 0.99958 → 0.99979 → 0.99981 → 0.99981 (N=8,12,16,24);
**envelope overlap = 1.000** throughout. Stable — but *because* the mode is
pinned to the small primes, indifferent to added high-height centres. Stability
here is a triviality, not evidence of a deep invariant.

**[4] Controls (N=12, S=3) — the decisive test.**

| variant | μ_max | α_c | peak n | env-overlap vs real |
|---|---|---|---|---|
| **real** | **0.99979** | 0.9999 | 2 | — |
| **smoothed-PNT** (`1/√n`, all integers) | **1.26137** | 1.1230 | 2 | **+0.964** |
| primes-only (no prime powers) | 0.89021 | 0.9483 | 2 | +0.999 |
| low<11-removed | 0.00001 | 0.6148 | 11 | +1.000 |
| shuffled-Λ (seed 7) | 0.00000 | 0.6148 | 35 | −0.746 |
| shuffled-Λ (seed 23) | 0.00004 | 0.6148 | 10 | +0.988 |

Reading:
- **smoothed-PNT reproduces the envelope shape (+0.96) yet `μ = 1.26 > 1`**:
  the bulk/envelope is **generic** (smooth log-density gives it), and smooth
  density **overshoots** the contraction. The real primes' *arithmetic*
  (oscillating signed `q_n`) is what pulls pressure **back to 0.9998 ≤ 1**.
- **low<11-removed → μ ≈ 0**: confirms the whole envelope is the first 4 primes.
- **shuffled-Λ → μ ≈ 0**: degrades — but because shuffling moves weight to large
  n where the test-function damps it (the *unfair* direction), so this is **not**
  clean evidence of prime-specificity; it conflates "prime" with "small-n."
- **prime-powers-removed → μ = 0.89**: prime powers carry ~0.11 of the margin.

## 7. Scaling-collapse / boundary-vs-volume
No nontrivial collapse to test: the envelope is ~3 terms pinned at the smallest
primes and N-invariant for trivial reasons. There is **no extended `Π_*(u)`** with
a clean scaling law — the boundary-vs-volume question is moot (the object has no
"interior"). **Obstruction recorded.**

## 8. Capacity profile / α-critical
Real primes: `α_c = 0.9999` (real Γ exactly critical, reproduces THRESHOLD-001).
smoothed-PNT: `α_c = 1.123` (>1: smooth density needs *more* capacity than the
real Γ provides → overshoot). This is the same finding as [4] in capacity
language: **the real arithmetic sits exactly at α=1; the generic surrogate does
not.** The thing that makes α=1 critical is the prime cancellation, not an
envelope.

## 9. God-Prime-like envelope assessment — **NOT supported**

| criterion | result |
|---|---|
| global, not single-prime | ✗ (it's the first 3–4 primes) |
| stable under cutoff growth | ~ (trivially, pinned to small primes) |
| prime-specific vs controls | ✗ (**smoothed-PNT reproduces it, +0.96**) |
| capacity-saturating | the *bound* yes; the *envelope* no |
| information-dense | ✗ (participation 2.68, entropy 1.12) |
| basis-independent | ✗ (centroid/μ drift with S) |
| zero-free construction | ✓ |

**Verdict: `none` / `weak`.** No mathematically defined God-Prime envelope. The
maximal-pressure envelope is generic + basis-shaped + first-few-primes.

## 10. The one sharp positive (and the candidate statement it supports)
The genuinely useful by-product is the **smoothed-PNT overshoot**:

> **Generic-overshoot observation.** The *smoothed* prime density saturates and
> **exceeds** the boundary capacity (`μ_PNT = 1.26 > 1`, `α_c = 1.12`); the
> *actual* prime arithmetic, through the signed/oscillating explicit-formula
> contributions (the `−ζ′/ζ` fluctuation), pulls the normalised pressure back to
> `μ = 0.9998 ≤ 1`, with the real Γ coefficient exactly critical (α_c = 1.0000).

So **RH is carried by the prime *cancellation*, not by a pressure envelope.**
This is consistent with — and sharpens — CONTRACTION-002: the prime-specific
object is the *fluctuation around* the generic envelope (poles of `−ζ′/ζ` at the
zeros), which is exactly the part that does **not** form a stable invariant.

## 11. Obstructions
- Envelope is basis-shaped (centroid drifts with S) and trivial (≤4 primes).
- Shuffled-Λ control conflates prime-specificity with small-n weighting (damping
  artefact); it cannot cleanly establish prime-specificity.
- smoothed-PNT — the *fair* control — **defeats** the prime-specificity claim.
- No extended envelope ⇒ no scaling-collapse / holographic-law test possible.

## 12. What this does and does NOT claim
- **Does NOT:** prove RH; find a new invariant; find a God Prime / God-Prime
  envelope; claim the horizon analogy yields new mathematics; claim prime-
  specificity (the fair control refutes it).
- **Does:** show the maximal-pressure envelope is generic + basis-shaped +
  first-few-primes; quantify that smooth density overshoots (`μ=1.26`) while real
  primes sit at criticality (`α_c=1.0000`); locate the prime-specific content in
  the **cancellation/fluctuation**, re-confirming the route_b wall is the real one.

## 13. Recommended next WO
This is the WO's **WO-RH-HORIZON-GENERIC-CAPACITY-002** outcome (the horizon law
is generic to log-density, not prime-specific) merged with an obstruction report.
There is **no** stable invariant to formalise (so no HORIZON-THEOREM-002, no
GOD-PRIME-ENVELOPE-002). The honest constructive next step remains
**WO-RH-OPERATOR-ROUTE-PUBLISH-001**: freeze route_b + this route_c negative as
the bundle's RH-frontier statement — *"the prime-specific content of the horizon
law is the explicit-formula fluctuation (RH itself), not a separable envelope."*

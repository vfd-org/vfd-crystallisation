# Certificate Candidates

## Found (solved domains)
- Linear contraction → **Lyapunov form** (CLOSED).
- Rotation/cycle → **invariant inner product** (CLOSED).
- Ergodic Markov → **spectral gap + stationary measure** (CLOSED).

## Collatz — the decisive *negative* result
- Rung grammar (T-map parity words) = **full one-sided shift** (Terras 1976 bijection
  Z/2^k → {0,1}^k, **verified here for k≤12**).
- Escape words (ones-fraction > 0.6309) are all admissible:
  794 of them at length 12. The all-ones (max-escape)
  word of length 10 is realised by n=1023 (=2¹⁰−1),
  whose longer trajectory returns to ones-fraction 0.5.
- **Conclusion:** no finite rung-word automaton can certify Collatz closure — there is no
  forbidden finite pattern. **A certificate must be GLOBAL over the realised 2-adic
  measure = the open conjecture.** This *rules out a whole class of attempted certificates*.

## Still missing (open)
- Collatz: global cumulative-drift certificate (not finite-automaton).
- RH: Weil positivity certificate (infinite-dim).
- Navier–Stokes: coercive high-frequency norm (supercritical).

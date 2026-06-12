# Shell-Boundary Search Framework

A problem of *finite rule + indefinite repetition + uncontrolled boundary* is recast as
P=(X,T,h,B,Q): shell index h, transformation T, positive form B, capacity Q. The driver
classifies repeated T relative to h→∞ as CLOSED / CRITICAL / ESCAPING / WRONG_BOUNDARY /
UNKNOWN, and searches for a closure certificate (Lyapunov form, invariant inner product,
stationary measure, positivity form, Diophantine/automaton obstruction, spectral gap).

**Honest scope (guardrail).** This is a *reduction/search method*, not an oracle.
Failure to find a certificate may mean: the problem is open, the shell is wrong, the
certificate class is too weak, or no certificate exists in the chosen formal system.
It solves nothing automatically; it *localises* the obstruction and *excludes
certificate classes*. The Collatz result is exactly such an exclusion: the rung grammar
is the full shift, so no finite rung-automaton certificate exists.

**Grade: MEDIUM PASS.** Calibration domains classify correctly with separating controls;
Collatz recovers Terras 1976 and yields the certificate-class exclusion; no open problem
is solved.

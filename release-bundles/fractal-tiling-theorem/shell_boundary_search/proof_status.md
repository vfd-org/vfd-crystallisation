# Proof Status — Shell-Boundary Search

| Claim | Grade | Basis |
|---|---|---|
| Linear: ρ<1 ⇒ CLOSED (Lyapunov); ρ>1 ⇒ ESCAPING; defective ρ=1 ⇒ CRITICAL | PROVEN | classify_linear + closure_certificate_theory Lem.1–3 |
| Ergodic Markov ⇒ CLOSED (spectral gap + π) | PROVEN | Perron–Frobenius |
| Collatz parity-vector grammar = full shift (Z/2^k ↔ {0,1}^k) | PROVEN (Terras 1976) | verified here k≤12 |
| ⇒ no finite rung-automaton certifies Collatz; obstruction is global | PROVEN (corollary) | full-shift ⇒ no forbidden finite word |
| Collatz convergence | OPEN | global cumulative-drift certificate missing |
| Navier–Stokes capacity falls with viscosity | DIAGNOSTIC | shell sweep; sign-crossing scheme-dependent |
| Navier–Stokes regularity | OPEN | coercive supercritical norm missing |
| RH | OPEN | Weil positivity certificate (infinite-dim) |

**New framing contributed:** the certificate-class *exclusion* for Collatz (no finite
rung automaton), via the known Terras bijection. Recovers Terras 1976; proves nothing
new about Collatz itself.

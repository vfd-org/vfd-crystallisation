# The centre is constructed FROM the arms (not imported)

`Q_W = A∞ + P_F − R_S` — the three arm contributions summed:
- `A∞` = archimedean Γ/digamma kernel (the completion arm),
- `P_F` = finite prime-power pressure (the Euler/p-adic arm),
- `R_S` = scale-action / involution reflection term.
This is exactly the route_b Weil form `D=A+P−R`. The centre is therefore not a second
object: it is `Centre(F,A∞,S)`, induced by the interaction of the three verified arms.
Finite cutoff: `Q_W` min eig = +0.00004 (PSD, near-null). Remove any arm and it breaks
(no-arch → −5.03; fake-Γ → −0.11; random → −3.91; shuffled primes → breaks the explicit
formula / FE-axis though it stays PSD on the form).

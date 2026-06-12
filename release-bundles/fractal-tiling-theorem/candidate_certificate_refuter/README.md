# Candidate-Certificate Refuter

An **honest refuter** for proposed closure certificates at the infinity wall
(RH / Collatz / Navier–Stokes). It is skeptical by construction: it tries to **break**
a candidate on finite truncations and returns either **REFUTED** (with a concrete
witness) or **SURVIVES-TRUNCATIONS** under a hard banner.

> **It refutes; it never certifies.** There is no code path that returns "proved."
> SURVIVES-TRUNCATIONS = evidence on finite cutoffs only. The infinite-limit step is the
> open problem and is not decidable by this finite harness.

## What it does
- `refute_rh(candidate)` — candidate = "the Weil form is PSD via completion X". Computes
  min eigenvalue of the finite Weil form across (NC, P) truncations; REFUTED if indefinite.
  *Result: fake/no-arch completions REFUTED; the correct completion survives (near-null).*
- `refute_collatz_lyapunov(V)` — candidate = "V is a strict Lyapunov function for 3n+1".
  Scans odd n; REFUTED on the first non-decrease (witness n→next).
  *Result: every purely-local Lyapunov is REFUTED (n=3→5) — as the full-shift theorem predicts.*
- `refute_collatz_numeric(N)` — "all n≤N reach 1": SURVIVES = numeric verification, **not** proof.
- `refute_ns_coercive(nu_floor)` — "ν≥floor ⇒ shell capacity ≥0"; REFUTED if some ν breaks it.

## Why this is the honest ceiling
For Collatz we have a theorem (rung grammar = full shift) that **no finite-local certificate
can exist** — so the refuter *should* and *does* kill every local Lyapunov. For RH the finite
Weil form is PSD-with-near-null and no finite basis certifies the limit (= Connes site). The
refuter's power is **killing wrong guesses fast and keeping the bookkeeping honest**; the
surviving candidate still needs the infinite-dimensional proof that is the open problem.

Run: `python3 run_refuter.py` ; `python3 test_refuter.py`

# Triad-Closure Cross-Domain Test (WO-VFD-TRIAD-CLOSURE-CROSSDOMAIN-001)

A **domain-agnostic** instrument that lifts a visible sequence (integers, primes,
simplex states, cognitive states) to a hidden structure and asks one question with
one set of definitions across every domain:

```
n  ↦  (n, phase θ, triad-leg τ, braid-state, closure-capacity Q)
```

> Does repeated application of the step rule `T` produce **closure**, a **critical
> boundary**, or forbidden **escape**?

We do **not** replace the number line — we lift it. Visible bookkeeping stays;
hidden closure structure is attached underneath and *tested*.

## The one object, reused unchanged

`ClosureProblem = (X, T, τ, θ, B, ∂X, Q)` with four diagnostics in `src/closure_engine.py`:

| diagnostic | definition | reads |
|---|---|---|
| `symmetrizer(T)` | PD `B` with `BT = TᵀB` | self-adjoint (monotone) closure — real spectrum |
| `isometry_form(T)` | PD `B` with `TᵀBT = B` | phase-return closure — unit-circle spectrum |
| `triad_grammar_score` | τ-sequence advances A→B→C | triad-cycle admissibility |
| `capacity_drift` | `Q̄ = mean(compression − expansion)` | `>0` stable · `=0` critical · `<0` escape |

## What it found (run, at true strength)

`python3 src/run_crossdomain.py`

- **Collatz — STRONG (family discrimination).** The *same* `Q = a·ln2 − ln q` per
  odd step predicts `3n+1` closes (`Q̄≈+0.27`) while `5n+1`, `7n+1` escape
  (`Q̄<0`). Non-circular control fires. *This is the classical drift heuristic,
  reproduced cleanly — it does not prove Collatz (average drift ≠ no single
  escaping braid; that residual IS the conjecture).*
- **Primes/RH — WEAK.** FE residual `R_FE(Ξ)≈10⁻³¹` selects the unique completion;
  raw/fake completions leak. But this is a *known reflection symmetry*, not zero
  location; the real wall is Weil positivity (open).
- **Simplex — WEAK/structural, but corrects the hypothesis.** Triad 3-cycles close
  by **isometry** (eigenvalues on the unit circle), *not* self-adjointness.
  → closure = *positive invariant form*, of which self-adjoint is the real-spectrum case.
- **Cognition — TOY ONLY.** No ARIA logs used; illustrative plumbing, not evidence.

**Cross-domain verdict: MEDIUM PASS** — one engine, ≥3 domains, non-circular
controls fire, complexity reduced, common structure revealed. Proof-level reached
nowhere.

## Millennium extension

- `MILLENNIUM_CLOSURE_MAP.md` — honest fit grades for all 7 Clay problems.
- `python3 src/run_millennium_probe.py` — Navier–Stokes dyadic-shell capacity probe:
  the same `Q` reproduces the viscosity trichotomy (regular ↔ escape). Best fit;
  Poincaré (solved, via Perelman's monotone W-entropy) shows the shape can be
  decisive; P vs NP and Hodge correctly *don't* fit.

## Discipline (held throughout)

Known answers (the number 1, zeros, blow-up time, mass gap) appear **only in
validation**, never inside `T/τ/θ/Q`. No fitting. **Nothing here proves, partially
proves, or reduces any open problem.** Local; not pushed.

## Files
```
src/closure_engine.py        abstract object + 4 diagnostics (incl. both closure modes)
src/run_crossdomain.py       Collatz / RH / simplex / cognition
src/run_millennium_probe.py  Navier–Stokes dyadic-shell capacity drift
MILLENNIUM_CLOSURE_MAP.md    7-problem honest fit map
outputs/                     crossdomain_results.json, millennium_navier_stokes_probe.json
```

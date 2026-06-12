# Invariant Closure Engine v2 (WO-VFD-INVARIANT-CLOSURE-CROSSDOMAIN-002)

Upgrades the triad-closure diagnostic into a **proof-pressure** framework: it searches
for a positive form `B` under which a transformation `T` closes, classifies the
**closure mode**, runs every domain against **controls**, and extracts each **proof wall**.

## Closure modes (the deepest refinement)

> Closure is a property of the triple `(T, B, ∂X)`, not of `T` alone.
> The question is not "does `T` close?" but "does there exist a positive `B` under which it does?"

| mode | invariant | spectrum | decided by |
|---|---|---|---|
| `DISSIPATIVE` | `TᵀBT ≤ B` | inside unit disc | `ρ(T)<1` → discrete Lyapunov gives `B>0` |
| `ISOMETRIC` | `TᵀBT = B` | unit circle | all `|λ|=1`, diagonalizable → Weyl-average `B` |
| `SELF_ADJOINT` | `BT = TᵀB` | real line | real spectrum, diagonalizable |
| `CRITICAL` | sign of `TᵀBT−B` unresolved | unit circle, **defective** | `ρ=1` + Jordan block (no positive invariant form) |
| `MIXED` | composite | mixed moduli | isometric core + dissipative part |
| `NONE` | — | `ρ>1` | escape |

## Results at true strength — **MEDIUM PASS**

| domain | status | what |
|---|---|---|
| calibration | **PASS** | classifier rediscovers all 8 known modes (cycle→ISO, contraction→DISS, Jordan→CRITICAL, ρ>1→NONE) |
| markov | **PASS** | both chains DISSIPATIVE to stationary; reversibility = real spectrum (self-adjoint in weighted product) |
| collatz family | **PASS** | same `Q` → 3n+1 closes, 5/7/9n+1 escape (non-circular control) |
| collatz cycles | **PASS (known)** | closure Diophantine eliminates 1-cycle class + no small cycles — **reproduces Steiner 1977 via new route** |
| primes | **PASS** | real primes separate from fakes: residue (trivial) + Lemke-Oliver–Soundararajan correlation (**1205× over controls**) |
| polytope | WEAK | triad 3-cycles close by isometry — generic, non-discriminating |
| navier–stokes | WEAK | capacity trend vs viscosity holds; **sign-crossing scheme-dependent — not robust** |
| rh/weil | WEAK | positivity rejects wrong completions; insensitive to prime shuffle; RH wall intact |

## The honest bottom line

The engine does what the WO asked of a *diagnostic*: calibrates on known systems,
separates true from fake in two domains, classifies modes, extracts walls. It hits
**value-test items 1 (reproduce known via new route)** and **4 (correct a false
hypothesis: self-adjoint → positive invariant form)**. It does **not** hit item 3 —
no *new* missing invariant in any open problem. Every wall is the original theorem:

- **Collatz:** no infinite non-closing braid = the conjecture.
- **RH:** infinite-limit Weil positivity = Connes arithmetic site (the positivity form
  is even blind to prime shuffling — the missing object is a positivity *certificate*).
- **Navier–Stokes:** supercriticality → `Q` sign undetermined.

No proof, partial proof, or reduction of anything. Local; not pushed.

## Files
```
closure_mode_classifier.py     mode search + classification (spectrum + Lyapunov)
domains/calibration.py         A1-A3 + Jordan/escape
domains/markov_chains.py       A4-A5 reversible vs non-reversible
domains/collatz_family.py      qn+1 capacity + cycle Diophantine + braid search   ← priority 1
domains/prime_trace_controls.py residue + LO-S transition vs controls             ← priority 2
domains/polytope_search.py     triad closure across polytopes
domains/navier_stokes_shell.py dyadic-shell capacity drift
domains/rh_weil_toy.py         finite Weil-positivity form vs fake completions
run_all.py                     full battery → reports/
reports/                       REPORT_*, PROOF_WALLS, CONTROL_RESULTS, DOMAIN_SCORECARD, results.json, scorecard.csv
```
Run: `python3 run_all.py`

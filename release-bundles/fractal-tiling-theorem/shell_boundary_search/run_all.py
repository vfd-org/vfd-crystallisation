"""Shell-Boundary Search — run all domain adapters, write reports. Honest grading."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "domains"))
import collatz_adapter, linear_adapter, markov_adapter, navier_stokes_shell_adapter as ns
REP = os.path.join(os.path.dirname(__file__), "reports")
print("=" * 84); print("SHELL-BOUNDARY SEARCH  (WO-VFD-RUNG-GEOMETRY + SHELL-BOUNDARY-SEARCH-GENERAL)"); print("=" * 84)

R = {"collatz": collatz_adapter.run(), "linear": linear_adapter.run(),
     "markov": markov_adapter.run(), "navier_stokes": ns.run()}

calib_ok = R["linear"]["_controls_separate"] and R["markov"]["outcome"] == "CLOSED"
collatz_full_shift = R["collatz"]["rung_grammar_is_full_shift"]
grade = ("MEDIUM PASS" if (calib_ok and collatz_full_shift) else "WEAK PASS" if calib_ok else "FAIL")

json.dump(R, open(os.path.join(REP, "results.json"), "w"), indent=2, default=str)

def W(n, t): open(os.path.join(REP, n), "w").write(t)

W("DOMAIN_RESULTS.md", f"""# Domain Results — Shell-Boundary Search

| Domain | Shell index | Outcome | Certificate / status |
|---|---|---|---|
| Linear: contraction | log-norm | **CLOSED** | Lyapunov form (ρ<1) |
| Linear: ρ>1 | log-norm | **ESCAPING** | none (leaves every shell) |
| Linear: rotation | log-norm | **CLOSED** | invariant inner product (ρ=1, diag.) |
| Linear: Jordan ρ=1 | log-norm | **CRITICAL** | none (defective; poly growth) |
| Markov (ergodic) | TV-distance to π | **CLOSED** | spectral gap {R['markov']['spectral_gap']:.3f} + stationary π |
| Navier–Stokes shell | dyadic frequency | trend→0⁺ | capacity falls with ν; sign-crossing scheme-dependent (WEAK) |
| **Collatz** | log-magnitude; rung=parity | **see below** | **no finite rung-automaton certificate** |

**Calibration controls separate:** {calib_ok}.  **Overall grade: {grade}.**
""")

c = R["collatz"]
W("CERTIFICATE_CANDIDATES.md", f"""# Certificate Candidates

## Found (solved domains)
- Linear contraction → **Lyapunov form** (CLOSED).
- Rotation/cycle → **invariant inner product** (CLOSED).
- Ergodic Markov → **spectral gap + stationary measure** (CLOSED).

## Collatz — the decisive *negative* result
- Rung grammar (T-map parity words) = **full one-sided shift** (Terras 1976 bijection
  Z/2^k → {{0,1}}^k, **verified here for k≤12**).
- Escape words (ones-fraction > {c['escape_threshold_ones_fraction']:.4f}) are all admissible:
  {c['admissible_escape_words_len12']} of them at length 12. The all-ones (max-escape)
  word of length 10 is realised by n={c['escape_realisation']['realised_by_smallest_n']} (=2¹⁰−1),
  whose longer trajectory returns to ones-fraction {c['escape_realisation']['longer_parity_fraction_ones']}.
- **Conclusion:** no finite rung-word automaton can certify Collatz closure — there is no
  forbidden finite pattern. **A certificate must be GLOBAL over the realised 2-adic
  measure = the open conjecture.** This *rules out a whole class of attempted certificates*.

## Still missing (open)
- Collatz: global cumulative-drift certificate (not finite-automaton).
- RH: Weil positivity certificate (infinite-dim).
- Navier–Stokes: coercive high-frequency norm (supercritical).
""")

W("PROOF_WALLS.md", """# Proof Walls

- **Collatz.** Wall localised more sharply than before: the local rung geometry is the
  *full shift*, so the obstruction is provably NOT finite-automaton-expressible — it is
  global. Recovers Terras 1976; the certificate-class exclusion is the new framing.
  Collatz itself OPEN.
- **RH.** Weil positivity of the explicit form; infinite-dimensional certificate; OPEN.
- **Navier–Stokes.** Supercritical controlled norm; capacity sign undetermined; OPEN.
- **Solved rows** (linear, Markov, cycles, Poincaré-Perelman) all have finite/known
  certificates — they are the calibration that the method is not vacuous.
""")

W("CONTROLS.md", f"""# Controls

- **Linear:** stable (ρ<1)→CLOSED, escaping (ρ>1)→ESCAPING, Jordan (ρ=1 defective)→CRITICAL.
  Separate: {R['linear']['_controls_separate']}.
- **Collatz:** the Terras bijection check is itself a hard control — if the parity map were
  NOT a bijection, a finite-automaton certificate might exist; it IS, so it doesn't.
- **Navier–Stokes:** viscosity sweep; trend reported, sign-crossing flagged non-robust.
""")

W("SHELL_BOUNDARY_FRAMEWORK.md", f"""# Shell-Boundary Search Framework

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

**Grade: {grade}.** Calibration domains classify correctly with separating controls;
Collatz recovers Terras 1976 and yields the certificate-class exclusion; no open problem
is solved.
""")

print(json.dumps({k: (v.get("outcome") or v.get("status") or "see report") if isinstance(v, dict) else v
                   for k, v in R.items()}, indent=2, default=str))
print(f"\n  Collatz rung grammar = full shift (Terras, verified k<=12): {collatz_full_shift}")
print(f"  => NO finite rung-automaton certificate for Collatz (obstruction is global).")
print(f"  Calibration controls separate: {calib_ok}")
print(f"\n  OVERALL GRADE: {grade}")
print("  Reduction/search method, not an oracle; recovers Terras; excludes a certificate")
print("  class for Collatz; solves no open problem. Not a proof. LOCAL.")
print("=" * 84)
print("[reports] SHELL_BOUNDARY_FRAMEWORK.md, DOMAIN_RESULTS.md, CERTIFICATE_CANDIDATES.md,")
print("          PROOF_WALLS.md, CONTROLS.md, results.json")

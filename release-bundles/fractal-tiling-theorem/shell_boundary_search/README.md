# Shell-Boundary Search (WO-VFD-RUNG-GEOMETRY-CERTIFICATE-001 + WO-VFD-SHELL-BOUNDARY-SEARCH-GENERAL-001)

Recasts *finite rule + indefinite repetition + uncontrolled boundary* problems as
shell-boundary problems `P=(X,T,h,B,Q)` and searches for a closure certificate. A
**reduction/search method, not an oracle.**

## Centrepiece result (Collatz rung geometry)
- Rung = T-map parity bit; rung grammar = **full one-sided shift** (Terras 1976
  bijection `Z/2^k ↔ {0,1}^k`), **verified here for k≤12**.
- Every finite *escape word* (ones-fraction > ln2/ln3 ≈ 0.6309) is admissible
  (794 at length 12); the all-ones length-10 word is realised by **n=1023=2¹⁰−1**.
- **Corollary (new framing):** no finite rung-word automaton can be a Collatz closure
  certificate — there is no forbidden finite pattern. **Any certificate must be global**
  (cumulative drift over the realised 2-adic measure) = the open conjecture. This
  *excludes an entire class of attempted certificates* and sharpens the proof wall.

## Calibration (controls separate)
Linear: contraction→CLOSED (Lyapunov), ρ>1→ESCAPING, rotation→CLOSED (isometric),
Jordan→CRITICAL. Ergodic Markov→CLOSED (spectral gap + π). Navier–Stokes shell: capacity
trend down with viscosity (sign-crossing flagged non-robust).

**Grade: MEDIUM PASS.** Recovers Terras; yields the certificate-class exclusion; solves
no open problem.

## Files
```
core/shell_problem.py                framework + linear classifier
domains/collatz_adapter.py           Terras bijection + escape words + exclusion  ← centrepiece
domains/linear_adapter.py            ρ-based outcomes + controls
domains/markov_adapter.py            spectral-gap certificate
domains/navier_stokes_shell_adapter.py  dyadic capacity sweep
rung_admissibility_search.py         CLI over the parity automaton
run_all.py                           full run → reports/
formal_definitions.md, proof_status.md
reports/  SHELL_BOUNDARY_FRAMEWORK, DOMAIN_RESULTS, CERTIFICATE_CANDIDATES, PROOF_WALLS, CONTROLS, results.json
tests/test_cycles.py
```
Build: `python3 run_all.py` ; `python3 tests/test_cycles.py`

## Guardrail
No claim that all problems are solvable. No-certificate ≠ no-solution. Recovers Terras
1976; proves nothing new about Collatz, RH, Navier–Stokes, or Yang–Mills. Local; not pushed.

# Closure Certificate Theory (WO-VFD-CLOSURE-CERTIFICATE-THEORY-001)

The formal core that was missing from the cross-domain closure diagnostic: the
**closure certificate** — a *finitely checkable* object that controls *infinite*
repetition at a boundary.

> Many hard problems are not about infinity itself, but about whether a finite
> generative rule admits a finite certificate (a Lyapunov form, an invariant inner
> product, a symmetrizer, a Diophantine obstruction, or a positivity proof) that
> controls its behaviour at the boundary of indefinite repetition.

## Contents
- `closure_certificate_theory.tex` / `.pdf` — 7 definitions, 4 lemmas + 1 corollary
  (all proved), 1 proposition (proved), open-problem mapping, non-overclaim boundary.
- `verify_certificates.py` — numerical harness; **14/14 formal-claim checks PASS**.
- `certificate_catalogue.csv` — solved vs missing certificates across 12 domains.
- `proof_status_table.md` — every claim graded PROVEN / DIAGNOSTIC / OPEN.
- `examples/` — finite cycles, Markov chains, Collatz cycle certificate (worked).

## Proved here (PROVEN)
1. **Dissipative certificate ⟺ ρ(T)<1** (Lyapunov form) — recovers discrete Lyapunov stability.
2. **Isometric certificate ⟺ power-bounded invertible** (invariant inner product).
3. **Self-adjoint certificate ⟺ real-diagonalizable** (symmetrizability).
4. **Reversible Markov ⟹ diag(π) self-adjoint certificate**; ergodic ⟹ contraction on 1⊥.
5. **Collatz cycle equation** (finite Diophantine certificate); **only trivial 1-cycle for 3n+1** (recovers Steiner 1977).

## Explicitly NOT claimed
No proof, partial proof, or reduction of Collatz, RH, Navier–Stokes, or Yang–Mills.
For each, the note states the correct closure mode and the **exact missing certificate**;
supplying it *is* the open problem. No physics/consciousness/TOE claims. Local; not pushed.

## Build
```
python3 verify_certificates.py        # 14/14 PASS
pdflatex closure_certificate_theory.tex   # (twice)
```

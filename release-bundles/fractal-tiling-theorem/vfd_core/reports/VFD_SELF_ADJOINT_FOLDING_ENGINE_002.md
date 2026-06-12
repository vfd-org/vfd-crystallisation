# WO-VFD-SELF-ADJOINT-FOLDING-ENGINE-002 — Self-Adjoint Folding Engine (report)

**Status:** run; **engine built, works, and recovers the classical symmetrizability
criterion — a useful falsifiable tool, not new mathematics.** Modules:
`vfd_core/self_adjoint_folding_engine.py`, `run_self_adjoint_folding_engine.py`.
**No proof of RH; no claim of new mathematics.**

## 1. Summary
Generalised the mult-by-φ demo (INVARIANT-TRACE-FORM-LAW-001) into a solver: given a
transformation `T`, find a symmetric invariant form `B` making `T` self-adjoint
(`B T = Tᵀ B`, i.e. `BT` symmetric), and decide whether a **positive-definite** such
`B` exists. Result: the engine cleanly recovers the classical criterion —

> **A PD invariant self-adjoint form exists ⟺ `T` is real-diagonalizable** (real
> spectrum *and* diagonalizable).

## 2. Method
`invariant_form_space(T)`: null space of `B ↦ TᵀB − BT` over symmetric `B` (the space
of `T`-invariant forms). `construct_PD_form(T)`: if `T = PΛP⁻¹` with `Λ` real, build
`B = (P⁻¹)ᵀ(P⁻¹)` and verify `BT` symmetric + `B ≻ 0`.

## 3. Results

| transformation | real spectrum | form-space dim | PD form found | note |
|---|---|---|---|---|
| **mult-by-φ** `{1,√5}` | yes | 2 | **YES** | residual 2e-16 |
| reflection `[[0,1],[1,0]]` | yes | 2 | **YES** | residual 0 |
| real-diag 3×3 | yes | 3 | **YES** | residual 1e-16 |
| rotation π/5 | **no** | 2 | **NO** | complex spectrum |
| order-5 rotation (3D) | **no** | 3 | **NO** | complex spectrum |
| Jordan `[[1,1],[0,1]]` | yes | 2 | **NO** | defective (non-diagonalizable) |

The engine **recovers the mult-by-φ trace form exactly**: its PD form (normalised
`B[0,0]=2`) is `diag(2, 10)` = `Tr(xy)` on `{1,√5}` — the WO-001 form, re-derived
by the solver, not hand-fed.

## 4. Verdict
- **Works as a tool:** cleanly separates symmetrizable (`T` real-diagonalizable →
  PD form found) from non-symmetrizable (complex spectrum → rejected; defective →
  rejected). Falsifiable, bounded, exact.
- **Recovers known theory:** this is the theory of *symmetrizable matrices* /
  self-adjoint operators on inner-product spaces. **Known, not new.**
- **The decisive honest point:** the engine **cannot** manufacture a PD
  self-adjoint form for a genuinely complex-spectrum operator. So it gives **no RH
  shortcut** — RH's closure requires the spectrum to be *real* (the zeros on the
  line); the engine cannot impose that, it can only *detect* whether a given `T`
  already admits a real-self-adjoint structure. It confirms, concretely, the
  INVARIANT-TRACE-FORM-LAW finding that the right form is necessary, not sufficient.

## 5. What this does and does NOT claim
- **Does:** deliver a working, exact, falsifiable engine; recover the
  symmetrizability criterion; re-derive the mult-by-φ trace form; demonstrate the
  no-shortcut boundary (complex spectrum un-symmetrizable).
- **Does NOT:** find a new law; symmetrize a complex-spectrum operator; shortcut RH;
  claim novelty over classical linear algebra.

## 6. Recommended next
The engine is a reusable utility (e.g. to *check* whether a proposed RH operator is
even symmetrizable before deeper work). No new WO is forced; it supports
ARITHMETIC-TRACE-FORM-SEARCH-001 (which addresses where the real-spectrum/positivity
must come from — a geometric substrate, not a form choice).

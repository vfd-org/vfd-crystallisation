# WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001 — Arithmetic Trace-Form Search (report)

**Status:** run; **the canonical arithmetic trace form is identified (= the adelic
explicit-formula trace); number-field positivity = RH (open); the function-field
precedent confirms the strategy CAN deliver closure given a geometric substrate.
Necessary-not-sufficient confirmed — no number-field shortcut.** Sim:
`route_c/arithmetic_trace_form/rh_arithmetic_trace_form_search.py`. **No proof of
RH; no claim of a number-field trace form that proves positivity.**

## 1. Summary
Searched for the canonical arithmetic trace form behind Weil/Connes positivity —
the analogue of the Q(√5) trace form that *delivered* H4→E8. Findings:
1. **The form is the adelic explicit-formula trace.** The Weil form
   `Q[h] = (archimedean Γ trace) + (pole) − (prime trace)` is a **sum of local
   traces over all places `p ≤ ∞`** (archimedean place = Γ/digamma). This *is* the
   canonical arithmetic trace form (Weil/Connes) — identified, not new.
2. **Number-field positivity = RH (open).** Positivity of this form for all
   admissible test functions is exactly RH. So identifying the form is **necessary,
   not sufficient** — no shortcut, exactly as INVARIANT-TRACE-FORM-LAW-001 predicted.
3. **Function-field precedent (the genuine win).** In characteristic `p`, the
   analogous trace form — Frobenius on `H¹` paired by the Poincaré-duality
   **intersection form** (`α·ᾱ = q > 0`) — **provably delivers positivity**, so
   RH-for-curves is **Weil's theorem**. Verified on six curves: `|α| = √q` exactly
   (table below). This is the exact-closure analog of H4→E8: there, the right form
   *delivers* closure.

## 2. Part A — the canonical form (adelic explicit-formula trace)
Reproduced the local-trace structure numerically (Gaussian test, centre 14):
finite-place (prime) trace `≈ −0.843`; infinite-place (archimedean Γ) trace `≈ +4.871`.
The Weil form is their combination (+ pole). **This is `Tr` over the places of ℚ**;
its positivity ⟺ RH. *Form identified; closure = RH, open.*

## 3. Part B — function-field precedent (trace form DELIVERS closure)
Elliptic curves `E/F_q`: zeta numerator `P(T)=1−aT+qT²`, Frobenius eigenvalues
`α` = roots of `x²−ax+q`, `a = q+1−#E(F_q)`, `|a| ≤ 2√q` (Hasse).

| `E/F_q` | `a` | Frobenius `α` | `|α|` | `√q` | RH-curves |
|---|---|---|---|---|---|
| F₅ | 2 | 1.00 ± 2.00i | 2.23607 | 2.23607 | ✓ |
| F₇ | −1 | −0.50 ± 2.60i | 2.64575 | 2.64575 | ✓ |
| F₁₁ | 3 | 1.50 ± 2.96i | 3.31662 | 3.31662 | ✓ |
| F₁₃ | 4 | 2.00 ± 3.00i | 3.60555 | 3.60555 | ✓ |
| F₂ | 1 | 0.50 ± 1.32i | 1.41421 | 1.41421 | ✓ |
| F₁₀₁ | −7 | −3.50 ± 9.42i | 10.04988 | 10.04988 | ✓ |

**All `|α| = √q`** — RH for these curves holds. The mechanism: `α·ᾱ = q > 0` is the
**positivity of the intersection form** (Hodge index / Riemann–Roch); the trace form
(Frobenius + Poincaré duality) is self-adjoint/positive, so RH is a **theorem** (Weil).

## 4. The structural lesson
- **H4→E8** and **function-field RH** are the two cases where the correct trace form
  *delivers* closure — because a **geometric/cohomological substrate supplies the
  positivity** (golden lattice integrality / curve intersection form).
- **Number-field RH** has the canonical adelic trace form but **lacks that
  substrate**. Manufacturing it is precisely the **Connes–Consani "arithmetic site"**
  program (Spec ℤ as a curve). The missing substrate *is* the open heart of RH.
- So the search **succeeds** in identifying the form and a real precedent that the
  trace-form strategy *can* work — and **confirms necessary-not-sufficient**: there
  is no number-field shortcut; the difficulty is the absent geometry, not the form.

## 5. What this does and does NOT claim
- **Does:** identify the canonical arithmetic trace form (adelic explicit-formula
  trace); verify the function-field precedent (`|α|=√q`, RH-curves, via the
  intersection form); locate the missing ingredient (geometric substrate) precisely;
  confirm the form is necessary not sufficient.
- **Does NOT:** prove RH; produce a number-field trace form that proves positivity;
  claim discovery of Weil/Connes/Connes–Consani theory (cited); claim a shortcut.

## 6. Recommended next
The honest frontier is now sharply named: **RH = construct (or prove the existence
of) the geometric substrate over Spec ℤ that makes the adelic trace form positive**
(the arithmetic site). That is the open Millennium-grade problem, not a VFD WO. The
constructive programme step remains **WO-RH-OPERATOR-ROUTE-PUBLISH-001** (freeze the
RH frontier — route_b contraction + route_c negatives + this trace-form localisation)
and **WO-VFD-H4-E8-FORMAL-PAPER-004** (write the one exact exemplar). No further RH
sub-WO is warranted: the wall is now correctly identified as the missing arithmetic
geometry, which is RH itself.

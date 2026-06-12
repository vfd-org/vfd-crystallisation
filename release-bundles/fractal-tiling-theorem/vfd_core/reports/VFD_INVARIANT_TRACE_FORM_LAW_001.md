# WO-VFD-INVARIANT-TRACE-FORM-LAW-001 — Invariant Trace-Form Closure (report)

**Status:** run; **a defensible meta-lens with ONE exact exemplar (H4→E8), one
exact-but-open exemplar (RH), and one analogy (horizon) — explicitly NOT a closure
guarantee (RH is the counterexample).** Modules: `vfd_core/invariant_trace_form.py`,
`run_invariant_trace_form_law.py`. **No proof of RH/physics; no claim E8 is the
universe; no claim the law is universally proven.**

## 1. Summary
Three routes share a pattern: a *naive* form fails, and a *completed invariant
form* repairs it. This WO formalises that as a lens — **self-adjointness /
positivity / integrality is form-relative** — and grades the three cases honestly:

| case | completion term | closure delivered by the form? | status |
|---|---|---|---|
| **H4→E8** | golden trace `c=1+1/√5` | **YES** | proved (exact) |
| **RH/Weil–Connes** | archimedean Γ + pole | **NO** | finite-validated; full positivity = RH (open) |
| **Horizon scattering** | greybody/Jost (Γ-ratio) | **NO** | toy-validated; analogy only |

**Concrete anchor (exact):** multiplication-by-φ on Q(√5) is **not** symmetric
under the naive form (`T=[[½,5/2],[½,½]]`, `T≠Tᵀ`) but **is self-adjoint under the
trace form** `B(x,y)=Tr(xy)` (`B·T=[[1,5],[5,5]]`, symmetric). The *same* operator
is non-symmetric naively and self-adjoint in the trace form — self-adjointness is
form-relative, demonstrated, not asserted.

**The crucial honesty:** the right form is **necessary, not sufficient**. RH is
the standing counterexample — the canonical Weil/Connes form is *known* and
*finite-positive*, yet full positivity *is* RH and stays open. So "right form ⟹
closure" is **false in general**; the law is a lens + search heuristic, not a
theorem that delivers closure.

## 2. Why this followed
H4→E8 (TRACE-FORM-003 / SECOND-SHELL-004) is the one place a naive embedding
failed and the *correct trace form fixed it exactly*. The RH route (CONNES /
PRESSURE / CONTRACTION) and the horizon route (UNIVERSAL-BOUNDARY-SCATTERING)
showed the *same shape* (naive fails, completed form is the right space) without
the same resolution. This WO extracts the common lens and grades the difference.

## 3. Abstract schema
`TraceFormClosureCase(domain, naive_form, naive_failure, completed_form,
completion_term, corrected_property, self_adjoint_or_positive, residual_before,
residual_after, canonical_derived_not_tuned, closure_delivered_by_form, limits)`.
The decisive field is **`closure_delivered_by_form`** — it separates the exact
exemplar (H4→E8) from the lens-only cases.

## 4. Case A — H4→E8 (EXACT; closure delivered)
- Naive: `x→(x,σx)` → inner products `±½`, not even-integral.
- Completed: `B(x,y)=Tr_{Q(√5)/Q}(c⟨x,y⟩)`, `c=1+1/√5` (Tr c = 2), **derived** by
  norm-2 + integrality.
- Result: `shell₁ ∪ (1/φ)shell₁` = 240 roots, norm² = 2, ips `{−2..2}`, root-graph
  `(56,56,126,1,1)`, rank 8, even integral = **canonical E8**.
- Residual before/after: `±½` / **0**. **Closure delivered by the form. ✓**
- Limit: this is the **known** Wilson/Moody–Patera construction, verified exactly.

## 5. Case B — RH / Weil–Connes (EXACT FORM, OPEN CLOSURE)
- Naive: Li/Toeplitz moment kernel; prime-only Euler product; no-Γ → non-PSD,
  divergent; smoothed-PNT over-capacity (`μ=1.26>1`).
- Completed: Weil/Connes `D = H − R`, `H = A(arch Γ) + P(pole)`; `H` PSD after the
  pole lift; `K = H^{−½}RH^{−½}`; **RH ⟺ ‖K‖ ≤ 1**.
- Result: finite compressions PSD (validated); the completed form **is** the
  canonical arithmetic form (the explicit formula). **But** full-limit positivity
  is exactly RH — **open**.
- **`closure_delivered_by_form = False`.** This is the counterexample to a
  guarantee: right form, finite-positive, closure still not delivered.
- Limit (stated plainly, per WO discipline): unlike H4→E8, **this case is not
  solved**; the form is identified, the positivity theorem remains RH.

## 6. Case C — Horizon scattering (ANALOGY)
- Naive: static/compressed-funnel geometry → cosmetic (radius is a bijection; no
  invariant). 
- Completed: scattering determinant / Jost function + greybody (Γ-ratio); response
  = digamma; resonances on lines; damped QNMs for a real (self-adjoint) potential.
- Result: a *genuinely shared* determinant → log-derivative → resonance → stability
  architecture (the known trace-formula / Lax–Phillips picture), but **no proof
  transfer**: the toy is provable because the potential is real (self-adjoint); the
  arithmetic instance of the same statement is Hilbert–Pólya = RH.
- **`closure_delivered_by_form = False`; analogy only.**

## 7. Comparative matrix (the key column)
The three cases agree on *shape* (naive fails → completed invariant form is the
right space) and **differ on delivery**: only H4→E8 has
`closure_delivered_by_form = True`. RH and horizon have the right/parallel form but
the closure (positivity / stability ⟺ RH) is open or untransferable.

## 8. Self-adjointness is form-relative (made explicit)
`T†_B = B^{−1}T†B`; `T` is `B`-self-adjoint iff `B T` is symmetric (for symmetric
`B`). Demonstrated exactly for mult-by-φ (§1). Per case:
- H4/E8: the E8 root structure is even-integral **under `B`**, not under the naive
  form (form-relative integrality).
- RH: the Connes/Weil operator is symmetric/positive **in the completed form**;
  full self-adjoint positivity = RH (open).
- Horizon: the wave operator is self-adjoint for a real potential **under the flux
  form** → damped QNMs; the arithmetic analogue's self-adjointness is open.

## 9. Candidate VFD Invariant Trace-Form Law — defensible statement
> **(Form-relativity, supported.)** Self-adjointness, positivity, and integrality
> are properties **relative to a bilinear/Hermitian/trace/flux form**. A naive
> failure (fractional residual, non-PSD kernel, cosmetic geometry) can be a
> *wrong-form artefact*; completing to the **canonical invariant form** forced by
> the system's symmetry/arithmetic can convert apparent leakage into closed
> structure.
>
> **(Necessity, not sufficiency.)** Possessing the canonical form is **necessary
> but not sufficient** for closure. H4→E8 is the exact case where completion
> *delivers* closure; **RH is the counterexample** where the canonical form is
> known and finite-positive yet closure (full positivity) remains the open problem.

Versions **v1/v2** (form-relativity + completion *can* repair failures) are
defensible; **v3-as-guarantee** ("right form ⟹ closure") is **rejected** (RH).

## 10. What is exact / open / analogy
- **Exact (solved):** H4→E8 — golden trace form delivers even-integral E8.
- **Exact form, open closure:** RH — Weil/Connes form canonical & finite-positive;
  full positivity = RH.
- **Analogy:** horizon scattering — shared determinant/flux architecture; no
  transfer.

## 11. Obstructions (is the law vacuous?)
- The risk the WO flags — "this is just 'choose the right inner product'" — is
  **real**, and the honest defence is: the law is **not** a closure guarantee
  (RH kills that); its content is (a) *form-relativity is concrete and exact*
  (mult-by-φ; H4→E8), and (b) it yields a *specific search heuristic* for RH
  (find the canonical arithmetic trace form), while *honestly flagging* that the
  heuristic points at the hard problem, not a shortcut.
- Canonicality: in H4→E8 the form is **derived** (norm-2 + integrality force
  `c=1+1/√5`). In RH, "canonical" = the explicit formula itself; that canonicality
  does **not** confer positivity. So canonicality ≠ closure.

## 12. What this does and does NOT claim
- **Does:** state a defensible form-relativity lens; demonstrate it exactly
  (mult-by-φ); give one exact exemplar (H4→E8); grade RH (open) and horizon
  (analogy) honestly; reject the guarantee version using RH.
- **Does NOT:** prove RH; claim the law forces closure; claim discovery of
  Wilson/Connes/Weil theory; claim physics; claim the law is more than a
  lens + heuristic.

## 13. Recommended next WOs
- **WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001** — search for a canonical arithmetic
  trace form behind Weil/Connes positivity (necessary, *not* sufficient — flagged).
- **WO-VFD-SELF-ADJOINT-FOLDING-ENGINE-002** — generalise the mult-by-φ demo: search
  invariant forms that make a given transformation self-adjoint (a concrete,
  bounded, falsifiable tool).
- **WO-VFD-H4-E8-FORMAL-PAPER-004** — write up the one exact exemplar, citing
  Wilson/Moody–Patera.

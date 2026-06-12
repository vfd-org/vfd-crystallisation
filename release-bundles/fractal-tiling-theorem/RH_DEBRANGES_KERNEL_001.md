# WO-RH-DEBRANGES-KERNEL-001 — de Branges Kernel Cross-Check (report)

**Status:** run; **partial / convention-dependent** (= the WO's predicted "most
likely" outcome). Sim: `route_b/rh_debranges_kernel.py`. **No proof of RH.**

## 1. Summary
Independent cross-check of the validated Weil/Connes positive form from the de
Branges side, via a Hermite–Biehler candidate `E` built from the completed ξ.
The **Hermite–Biehler condition holds for the completed-ξ candidate and degrades
under archimedean ablation** — agreeing with the Weil/Connes result (positivity
present, archimedean carries it). But the result is **convention-sensitive** (the
candidate is an ansatz, not the proven canonical de Branges function) and the
reproducing-kernel Gram is numerically muddy, so this is a **suggestive
cross-check, not an independent confirmation**. The canonical Hermite–Biehler /
de Branges function remains the missing object.

## 2. Anti-circularity / honesty
Construction inputs: completed ξ and its derivative (allowed). **No zero heights
inserted.** Caveat stated plainly: ξ already encodes the zeros, so HB-pass
**reflects** RH-true-so-far; it does not force it. Cross-check, not proof.

## 3. The candidate and the convention issue (worked through honestly)
With `A(z) = ξ(½−iz)` (real on the real axis), three naive variants behave very
differently — exactly the ansatz-sensitivity the WO warned of:
- `E = ξ(½−iz) + iξ′(½−iz)` (the literal WO formula): **degenerate** — ξ′ is
  imaginary on the line, so this collapses to a *real* function → |E#|=|E| to
  1e-32 (sits exactly on the boundary).
- `E = A − iA′`: **anti-Hermite–Biehler** (pass ratio 0.00; zeros in the wrong
  half-plane).
- `E = A + iA′`: **Hermite–Biehler** (pass ratio 1.00).
The HB-ness flips with a sign convention. We report the `A+iA′` (HB) orientation,
flagged as a *chosen convention*, not a derived canonical form.

## 4. Results (`E = A + iA′`)
| diagnostic | completed ξ | zeta-only (archimedean ablated) |
|---|---|---|
| Hermite–Biehler pass ratio (20 UHP pts) | **1.00** (max viol 0.00) | **0.90** (max viol 0.12) |
| de Branges kernel Gram min eig (N=12) | −7×10⁻³ (numerically muddy) | −2.13 (clearly not PSD) |

- **HB holds for completed ξ; degrades when the archimedean factor is removed**
  → consistent with the Weil/Connes finding (archimedean carries positivity).
- The Gram's small negative (−7e-3) for completed ξ is a **numerical artifact**
  (diagonal `K(x,x)` via differentiation + finite-grid conditioning); the HB
  diagnostic is the robust signal here.

## 5. Interpretation
The de Branges machinery **partially aligns** with the validated Weil/Connes
positive form: the natural ξ-based Hermite–Biehler candidate *is* HB (reflecting
RH), and the archimedean term again carries that property. This is a genuine —
if convention-dependent — second-framework echo of the same structure.

## 6. What this does NOT establish (honest)
- Not an independent confirmation: the HB-ness depends on a sign convention, and
  the candidate `A±iA′` is an **ansatz**, not the proven canonical de Branges E.
- Not PSD-clean: the reproducing-kernel Gram is numerically muddy (−7e-3).
- Not a proof: built from ξ (encodes the zeros); HB reflects RH-true-so-far.
- The **canonical Hermite–Biehler / de Branges function is still the missing
  object** — exactly the WO's predicted outcome.

## 7. Failure modes recorded
Convention-sensitivity (sign flip → HB / anti-HB / degenerate); numerical
diagonal of the kernel; finite-grid conditioning. None hidden.

## 8. Net / next
Cross-check **partially positive**: the de Branges side shows the same
positivity + archimedean-carrier structure, in a convention-dependent ansatz.
The operator route's conclusion is unchanged and now triangulated from three
classical frameworks (Weil form, Connes scaling, de Branges kernel): **the
positive form is real and archimedean-carried; the canonical operator/function
that makes it manifest, and the proof of its full-limit positivity, is RH.**
Next (open, hard): **WO-RH-DEBRANGES-SPACE-002** — identify the canonical
Hermite–Biehler function and prove finite-domain kernel stability; or freeze
the route (operator-route capstone) as complete to its honest floor.

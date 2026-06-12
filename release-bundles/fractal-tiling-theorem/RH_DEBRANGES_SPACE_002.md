# WO-RH-DEBRANGES-SPACE-002 — Canonical de Branges Space Search (report)

**Status:** run; **proof-wall obstruction identified** (= the WO's predicted
outcome). Sim: `route_b/rh_debranges_space.py`. **No proof of RH; no φ; no zeros
inserted.**

## 1. Summary
Searched (Family 1) for a canonical de Branges Hermite–Biehler function from the
completed ξ, of the form `E_a(z) = A(z) + i a A′(z)`, `A(z)=ξ(½−iz)`. Two clean
findings and one sharp obstruction:
1. **Orientation is canonical** — the HB property is robust across the magnitude
   `a` and forced in sign, resolving Probe A's convention worry.
2. **Archimedean completion improves HB** (consistent with Probes B/C/A).
3. **Obstruction:** the candidate's reproducing kernel is **structurally not
   PSD** (a precision-stable negative eigenvalue), so `E_a` is **not** a genuine
   de Branges structure function. The canonical E remains the missing object —
   the de Branges route reaches the **same wall as Connes**.

## 2. Anti-circularity
Built from completed ξ + its derivative only. No zero heights, no Cayley phases,
no fit to the zero-Gram. Known zeros used nowhere here. Finite-domain HB does
**not** imply entire-function HB; entire HB for the *canonical* E is RH.

## 3. Relation to the validated Weil/Connes form
Probe B located the positive form (Weil test-function space), Probe C realised it
as the Connes scaling operator D (non-circular), both PSD-validated, with the
archimedean term as carrier. This WO asked whether a de Branges space realises
the same positivity. Answer: orientation yes, canonical space no (obstruction).

## 4. Results
**Canonicality (Family 1, `E_a = A + iaA′`, completed ξ):**

| test | result |
|---|---|
| HB pass vs magnitude `a∈{0.25,0.5,1,2,4}` | **1.00** all (max viol 0.00) — robust to `a` |
| HB sign (`+iA′` vs `−iA′`) | **+ → 1.00, − → 0.00** — sign HB-forced |
| HB pass vs growing domain (Im ≤ 2,5,10) | **1.00** throughout — domain-stable |
| archimedean ablation (HB: completed vs ζ-only) | **1.00 vs 0.90** — Γ improves HB |

→ The **orientation is canonical**: not a tuned ansatz; the sign is forced by
HB, the magnitude is free, and it is stable across domain. **Probe A's
"convention-dependent" worry is resolved** to a single HB-forced orientation.

**Kernel positivity (the obstruction):**

| precision | de Branges kernel Gram min eig (a=1, N=10) |
|---|---|
| 80 dps | **−7.028×10⁻³** |
| 200 dps | **−7.028×10⁻³** |

The negative eigenvalue is **identical to 4 sig figs at both precisions** — it
does **not** shrink. So it is **structural, not numerical**: `E_a` passes finite
HB *sampling* but its reproducing kernel is **persistently not PSD**. Finite
HB-sampling ≠ a positive reproducing kernel ≠ entire Hermite–Biehler. Hence
`E_a` is **not** a genuine de Branges structure function.

## 5. Canonicality verdict
**`ansatz_only` / `obstruction`.** The `A + iaA′` family is canonical in
*orientation* but is **not** the canonical de Branges space — its kernel carries
a structural positivity defect. The canonical Hermite–Biehler function for ξ
remains unidentified.

## 6. What this does NOT establish
- Not RH; finite HB-sampling does not give entire HB or global kernel PSD.
- The naive derivative family is not the de Branges structure function.
- No Hilbert–Pólya / canonical operator constructed.

## 7. The honest wall (now triangulated and obstruction-marked)
Three classical frameworks now agree, and all stop at the same place:
- **Weil form** (Probe B): positive, archimedean-carried, machine-validated.
- **Connes scaling D** (Probe C): non-circular operator, compression PSD but
  **marginal** (min eig → 0).
- **de Branges** (Probe A + this WO): orientation canonical, archimedean-
  important, but the naive family's kernel is **structurally not PSD** and the
  canonical E is missing.

> The positive form is real and archimedean-carried. The **canonical
> operator/function that makes its positivity manifest in the full limit — and
> the proof of that full-limit positivity — is RH.** No finite construction
> reaches it; the de Branges route now confirms this with a sharp obstruction.

## 8. Next step
This is the honest floor of the de Branges route. Options:
- **WO-RH-DEBRANGES-OBSTRUCTION-REPORT-001** — formalise why naive de Branges
  candidates fail canonicality and why Connes/Weil remains the primary route
  (largely covered by this report).
- **WO-RH-OPERATOR-ROUTE-PUBLISH-001** — freeze and prepare the operator-route
  bundle for release.
The actual de Branges/Connes *proof* (canonical space + full-limit positivity)
is the open Millennium problem, untouched.

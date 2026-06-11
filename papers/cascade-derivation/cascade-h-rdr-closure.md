# H-rdr Closure — Reduction to Theorem P-A at S = Rungs

**Status: CLOSED (reduced to Theorem P-A), conditional on the same hypothesis stack {H-grad, H-meas} that conditions P-A itself, plus a single definitional identification (Lemma 2) that is not a new mathematical claim.**

Closes: Hypothesis H-rdr (`cascade-capstone-coalgebra.tex`, Hyp. 5.X / `\label{hyp:rdr}`), sufficiency-only form.

Parent documents:
- `cascade-access-principle-theorem.md` (Theorem P-A, full form, §5)
- `cascade-capstone-coalgebra.tex` (introduces H-rdr, Lemma 5.2, Theorem 5.3 closure-saturation)
- `cascade-observer-query-algebra.md` (Q_S definition for bare S ⊆ Rungs)

**Date:** 2026-04-22.

---

## 0. Executive summary

**Claim (H-rdr sufficiency).** For the full-access closure data Φ_max over the full rung index Rungs_cascade,

    Q_{(Rungs_cascade, Φ_max)}  =  Γ(G, F).

**Result.** This is a direct corollary of Theorem P-A at S = Rungs, together with a definitional identification Q_{(S, Φ_max)} = Q_S that is forced by Definition 4.1 of the capstone (rung-structure) and Definition 3.1 of `cascade-observer-query-algebra.md` (bare-rung query algebra). No new analytic content is needed beyond what P-A already supplies.

H-rdr is therefore **closed by reduction**: it inherits P-A's conditional stack {H-grad, H-meas} and adds nothing new. The hypothesis label was introduced in the capstone only to avoid silently upgrading the cited P-A source; the reduction presented here performs that upgrade explicitly.

---

## 1. Setup

### 1.1 Two notations for query algebras

Two notations for query algebras appear in the programme:

- **Bare-rung form** (P-A-source, `cascade-observer-query-algebra.md` Def. 3.1): for S ⊆ Rungs,
      Q_S  :=  ⟨Q_r : r ∈ S⟩_{alg}   ⊂   Γ(G, F)
  where Q_r is the sheaf-section subalgebra of rung-r equivariant sections, i.e. the image of the map from the full subgroupoid G_r ⊆ G.

- **Refined form** (capstone, Def. 4.2 / rung-structure): for (S, Φ) with Φ specifying a subgroupoid G_r^Φ ⊆ G_r at each r ∈ S,
      Q_{(S, Φ)}  :=  ⟨Q_r^Φ : r ∈ S⟩_{alg}   ⊂   Γ(G, F)
  where Q_r^Φ is the sheaf-section subalgebra arising from the **restricted** subgroupoid G_r^Φ rather than the full G_r.

### 1.2 The maximal closure data

By capstone Remark 4.3 (`\label{rmk:phi-data}`), the **maximal closure data** Φ_max is the assignment

    Φ_max :  r  ↦  G_r^{Φ_max}  :=  G_r   for every r ∈ S.

Every rung receives its full subgroupoid; Φ_max is the terminal object in the fibre of closure-data assignments over S.

---

## 2. Reduction lemma

> **Lemma 2.1 (Full-closure data coincides with bare rung-set).** For any up-closed rung-set S ⊆ Rungs and the maximal closure data Φ_max over S,
>
>     Q_{(S, Φ_max)}  =  Q_S
>
> as subalgebras of Γ(G, F).

*Proof.* By Definition of Φ_max (§1.2), G_r^{Φ_max} = G_r for each r ∈ S. The induced rung-r sheaf-section subalgebra Q_r^{Φ_max} — sections equivariant under G_r^{Φ_max} — is therefore the sections equivariant under G_r, i.e. Q_r^{Φ_max} = Q_r. Taking algebra-generated subalgebras over S:

    Q_{(S, Φ_max)}  =  ⟨Q_r^{Φ_max} : r ∈ S⟩_{alg}  =  ⟨Q_r : r ∈ S⟩_{alg}  =  Q_S.

This is a definitional unpacking, not a theorem: the "refined" query algebra at full closure data is the same object as the bare-rung query algebra. □

**Remark 2.2.** Lemma 2.1 is genuinely trivial: the only content of the refined form (S, Φ) is to carry strictly smaller subgroupoids G_r^Φ ⊊ G_r. Setting Φ = Φ_max disables that content and collapses the refined form onto the bare form. No analytic or algebraic work is required.

---

## 3. H-rdr as a corollary of P-A

> **Corollary 3.1 (H-rdr sufficiency).** Assume H-grad and H-meas. Then
>
>     Q_{(Rungs_cascade, Φ_max)}  =  Γ(G, F).

*Proof.* By Theorem P-A (`cascade-access-principle-theorem.md` §5.1) applied at S = Rungs_cascade,

    Q_{Rungs_cascade}  =  ⊕_{χ ∈ ⟨C_{Rungs_cascade}⟩}  F(χ).

By Theorem P-A §5.3 (fourth bullet, explicit statement), ⟨C_{Rungs_cascade}⟩ = Ẑ[φ]⁶. Combined with the Pontryagin decomposition Γ(G, F) = ⊕_{χ ∈ Ẑ[φ]⁶} F(χ) (P-A equation (1.1), from Thm M1),

    Q_{Rungs_cascade}  =  ⊕_{χ ∈ Ẑ[φ]⁶}  F(χ)  =  Γ(G, F).

Applying Lemma 2.1 at S = Rungs_cascade:

    Q_{(Rungs_cascade, Φ_max)}  =  Q_{Rungs_cascade}  =  Γ(G, F).

This is the sufficiency direction of H-rdr. □

**Remark 3.2.** The only non-trivial inputs are H-grad and H-meas, already present in the stack that conditions P-A. H-rdr introduces no new hypothesis; it is a notational re-expression of P-A-at-S=Rungs in the capstone's refined category.

---

## 4. Why was H-rdr isolated at all?

The capstone statement (`\label{rmk:H-rdr-status}`) is honest about the reason: "We isolate it as a named hypothesis to avoid silently upgrading the cited source." The P-A source document states the theorem at the bare-rung level (S ⊆ Rungs), not at the refined level ((S, Φ) ∈ catC). Silently applying P-A to a refined-category object would conceal this notational step.

The present note performs the notational upgrade explicitly via Lemma 2.1, closing that gap. The upgrade is definitional and does not expand P-A's mathematical content.

---

## 5. What H-rdr does NOT say (and what still needs separate argument)

H-rdr is a **sufficiency-only** statement: Φ = Φ_max ⟹ Q_{(Rungs, Φ)} = Γ(G, F). It says nothing about necessity, which is handled in the capstone by a distinct argument:

- **Necessity** (Φ ≠ Φ_max ⟹ strict containment) requires H-loc (witness-separation), via capstone Lemma 5.2 (`\label{lem:char-restriction}`). H-loc is a localisation strengthening of meta-layer M3 and is **not** closed by the present note. It remains a genuine open hypothesis in the capstone stack (capstone `\label{rmk:H-loc-status}`).

- **Strict monotonicity** along the closure-data lattice (Φ ⊊ Φ' ⟹ Q_{(S, Φ)} ⊊ Q_{(S, Φ')}) is likewise not claimed by H-rdr and requires H-loc.

The present reduction closes only the sufficiency leg. The necessity leg remains open at H-loc.

---

## 6. Status

| Statement | Status | Note |
|-----------|--------|------|
| H-rdr sufficiency direction | **CLOSED by reduction to Theorem P-A** | This note, Corollary 3.1 |
| H-rdr necessity direction (H-loc) | Open | Capstone Lemma 5.2; not addressed here |
| Theorem 5.3 closure-saturation, sufficiency leg | CLOSED (inherits this note) | Capstone Theorem 5.3 sufficiency is now discharged by Corollary 3.1 directly |
| Theorem 5.3 closure-saturation, necessity leg | Open at H-loc | Unchanged |

**Downstream effect on the capstone hypothesis stack.** The capstone stack {H-FIC, H-lift-fin, H-loc, H-rdr} (atop the P-A imports H-grad, H-meas) reduces to {H-FIC, H-lift-fin, H-loc}. H-rdr drops out. The selection-principle Theorem 5.X (capstone `\label{thm:selection}`) retains three capstone-local hypotheses plus the two P-A-imported ones, rather than four capstone-local.

---

## 7. Summary

- **H-rdr sufficiency is a direct corollary of Theorem P-A at S = Rungs_cascade.** The reduction uses a single definitional identity Q_{(S, Φ_max)} = Q_S (Lemma 2.1), which is not a theorem but an unpacking of the capstone's Def. 4.1 against `cascade-observer-query-algebra.md` Def. 3.1.
- **H-rdr drops out of the capstone hypothesis stack.** Remaining capstone-local hypotheses are H-FIC, H-lift-fin, H-loc (plus the P-A-imported H-grad, H-meas).
- **H-rdr was genuinely a notational rather than mathematical hypothesis.** The capstone's isolation of H-rdr as a named hypothesis was conservative bookkeeping. The present note performs the upgrade explicitly.
- **No additional work is required on the sufficiency leg of closure-saturation.** The necessity leg remains conditional on H-loc.

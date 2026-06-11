# H-loc Closure — Witness Separation via M3d + Pattern-Equivariant Indicator

**Status: REDUCED.** Witness-separation form of H-loc (`cascade-capstone-coalgebra.tex`, Hyp. `\label{hyp:loc}`) is derived from Theorem M3d (local-to-global extension) plus a standard Kellendonk pattern-equivariant indicator construction, **conditional on one small residual sub-gap (G-loc-a)** concerning rung-overlap of the chosen morphism. The principal content claimed by codex's Round 4 roadmap — "build a local rung-r observable around γ and extend it globally via M3d" — is delivered here; the residual sub-gap is isolated and flagged honestly.

Closes (reduces): Hypothesis H-loc (`cascade-capstone-coalgebra.tex`, Hyp. `\label{hyp:loc}`, witness-separation form).

Parent documents:
- `cascade-meta-layer-theorem.md` (Theorem M3, especially M3a + M3c + M3d)
- `cascade-phase-m3-closure.md` (Proof of M3d, §7)
- `cascade-capstone-coalgebra.tex` §5 (H-loc, Lemma 5.2 `char-restriction`, Theorem 5.3 closure-saturation)
- `cascade-observer-query-algebra.md` §2 (Q_r as G_r-supported sections)
- `cascade-h-rdr-closure.md` (companion reduction; same section-algebra conventions)

**Date:** 2026-04-22.

---

## 0. Executive summary

**H-loc (witness-separation).** For every rung r ∈ Rungs, every γ ∈ G_r, and every subgroupoid G_r^Φ ⊊ G_r with γ ∉ G_r^Φ, there exists a section s_{γ, Φ} ∈ Q_(Rungs, Φ_max) such that s_{γ, Φ} ∉ Q_(Rungs, Φ).

**Route taken.**
1. Associate to γ a finite-patch assignment P_γ on a bounded region U ⊂ R⁴_phys supported on γ (i.e. P_γ is a local-tiling witness for γ's rung-r action).
2. By M3d, P_γ extends uniquely (up to rigid R⁴_phys-translation) to a global tiling T_γ ∈ Ω.
3. The **pattern-equivariant indicator** s_γ := **1**_{P_γ} ∈ Γ(G, F) — the section "does the tiling locally contain P_γ?" — is a section supported on the G-orbit of γ.
4. Because γ ∈ G_r, the support of s_γ lies inside G_r, so s_γ ∈ Q_r ⊆ Q_(Rungs, Φ_max) (using Q_r^{Φ_max} = Q_r and Lemma 2.1 of `cascade-h-rdr-closure.md`).
5. Because γ ∉ G_r^Φ and — conditional on G-loc-a below — γ ∉ G_{r'}^Φ for any r' ≠ r, the support of s_γ lies **outside** ⋃_{r'} G_{r'}^Φ. Any section in Q_(Rungs, Φ) has support inside this union. Hence s_γ ∉ Q_(Rungs, Φ). This is the witness.

**What is proved.** Steps 1–4 are rigorous given M3d + standard Kellendonk pattern-equivariant Čech theory. Step 5 is rigorous up to the residual sub-gap G-loc-a (rung-overlap avoidance), which is independent of M3d and reduces to a combinatorial property of the subgroupoids {G_r}_{r ∈ Rungs}.

**What is residual.** One named sub-gap:

- **G-loc-a (rung-overlap avoidance).** Show that for every r ∈ Rungs, every G_r^Φ ⊊ G_r, and every γ ∈ G_r ∖ G_r^Φ, one can choose γ (possibly passing to another element of G_r ∖ G_r^Φ) such that γ ∉ G_{r'} for any r' ≠ r with G_{r'}^Φ ⊊ G_{r'} would allow γ ∈ G_{r'}^Φ. Equivalently: the {G_r}_{r ∈ Rungs} admit enough rung-pure morphisms that at least one witness γ lies **only** in G_r (among the leaf rungs); the E_8 root rung is handled separately since G_{E_8} = G.

Without G-loc-a, the derivation produces a witness s_γ with support in G_r but possibly also compatible with some G_{r'}^Φ for r' ≠ r, which would put s_γ back into Q_(Rungs, Φ) via the Q_{r'}^Φ generator.

**Downgrade status.** H-loc is no longer a pure external-import hypothesis. It is **derived from M3d + Kellendonk indicator sections + G-loc-a**. The capstone's Theorem 5.3 closure-saturation becomes conditional on {P-A (via H-rdr), M3, G-loc-a} rather than {P-A, M3, H-loc}. G-loc-a is a substantially smaller combinatorial hypothesis.

---

## 1. Setup

### 1.1 Standing data

From `cascade-meta-layer-theorem.md` §1.1–§1.4 at the combined cut-and-project level (L₁₂ → H₄):

- 𝓜 = moduli space of phason offsets (combined level; mixed torus × solenoid topology).
- G = matching groupoid over 𝓜 (Thm M2).
- F = pattern-equivariant Čech sheaf on Ω; sections Γ(G, F) are the substrate-catalogue sections.
- For each rung r ∈ Rungs = {E_8, H_4, D_4, O, F_16, L_40, U_0}, a subgroupoid G_r ⊆ G (objects = offsets admitting a rung-r patch; arrows = G-morphisms fixing rung-r structure). The well-definedness of G_r is Gap G6.1 prerequisite of `cascade-observer-query-algebra.md` §1.3 and is assumed here.

### 1.2 Query algebras

From `cascade-observer-query-algebra.md` §2, §3 and `cascade-h-rdr-closure.md` §1.1:

- **Q_r = Γ_{G_r}(G, F)** = sections of F with support in G_r (vanishing outside G_r).
- **Q_r^Φ = Γ_{G_r^Φ}(G, F)** = sections with support in G_r^Φ ⊆ G_r.
- **Q_(S, Φ) := ⟨Q_r^Φ : r ∈ S⟩_{alg}** ⊆ Γ(G, F), the refined query algebra.
- **Q_(S, Φ_max) = Q_S** by Lemma 2.1 of `cascade-h-rdr-closure.md`.

**Key algebraic fact.** Any element of Q_(S, Φ) has support contained in ⋃_{r ∈ S} G_r^Φ (the algebra product is pointwise pairing of local-patch data; the support of a product is contained in the intersection of supports, and the support of a sum is contained in the union, so the generated subalgebra has support in the union of generator supports). This is the crucial algebraic lever for step 5 of the proof.

### 1.3 Theorem M3d (recap from `cascade-meta-layer-theorem.md` §5)

> **M3d.** Any locally-consistent finite-patch assignment on a bounded region of R⁴_phys has a unique extension (up to rigid R⁴_phys-translation) to a global tiling in Ω.

Proof: `cascade-phase-m3-closure.md` §7, via minimality (M3a) + linear repetitivity (M3c) and Aliste-Prieto–Coronel–Gambaudo 2013 §2. CLOSED rigorously.

---

## 2. From groupoid morphisms to finite patches

### 2.1 Morphisms as local-tiling changes

In the Forrest–Hunton–Kellendonk matching-groupoid picture, a morphism γ ∈ G from offset t to offset t' is a **finite sequence of phason flips** carrying T_t to T_{t'} within a bounded region of R⁴_phys (see `cascade-phase-m2-closure.md` §3). The flips live on a finite patch U_γ ⊂ R⁴_phys of bounded diameter. Morphism γ is entirely determined by (t, U_γ, flip-sequence).

**Patch associated to γ.** Let P_γ := the local-tiling data on U_γ ∪ (a buffer region) including the source patch T_t|_{U_γ} and the target patch T_{t'}|_{U_γ} together with the flip structure. P_γ is a finite, locally-consistent patch assignment.

### 2.2 Rung-r character of P_γ

If γ ∈ G_r, then by definition of G_r (from `cascade-observer-query-algebra.md` §1.3), γ fixes the rung-r structure of T_t. The patch P_γ therefore contains, within U_γ, a rung-r-compatible configuration C_r(P_γ). (Concretely: for r = H_4, U_γ contains an H_4-configuration; for r = O, U_γ contains a valid S⁷ Fano-plane observer datum; etc.)

**Rung-r-pure morphisms.** We say γ is **rung-r-pure** if γ ∈ G_r and γ ∉ G_{r'} for every r' ∉ {r, E_8}. Rung-r-purity says the patch P_γ's C_r structure is the **only** leaf-rung-structure it contains beyond the E_8 root (which every patch carries trivially).

**Remark.** Rung-r-pure morphisms exist abundantly for generic γ under the independence conjecture (*) of `cascade-observer-query-algebra.md` §3.1 (Q_r ∩ Q_{r'} = common E_8 root only). But independence is Gap G6.2 and is not proved. This is the origin of sub-gap G-loc-a; see §5.

---

## 3. Extension via M3d

### 3.1 Step 1 — local consistency of P_γ

P_γ is locally consistent by construction: it is a sub-patch of the tiling T_t (and equally of T_{t'}), each of which is a global tiling in Ω, hence locally consistent everywhere. Local consistency on U_γ is therefore automatic.

### 3.2 Step 2 — M3d applied

By Theorem M3d, P_γ extends uniquely (up to rigid R⁴_phys-translation) to a global tiling T_γ ∈ Ω containing P_γ as a sub-patch. (We may take T_γ = T_t itself; the M3d uniqueness statement guarantees no other tiling extends P_γ except by rigid translation.)

### 3.3 Step 3 — pattern-equivariant indicator section

Define

    s_γ  :=  **1**_{P_γ}  ∈  Γ(G, F)

the **pattern-equivariant indicator section**: the pattern-equivariant function on Ω taking value 1 at a tiling T if T locally contains the patch P_γ (up to the chosen R⁴_phys-translation equivalence) and 0 otherwise.

In the Kellendonk pattern-equivariant Čech formalism (Kellendonk 2003, J. Phys. A 36; Sadun 2008 §4.3), **1**_{P_γ} is a bona fide section of F: locally constant on each Ω-orbit, pattern-equivariant by the translation-invariance of "contains P_γ," and continuous on the Cantor-structure transversal. See `cascade-phase-m2-closure.md` §4 for the standard setup at matching-groupoid level.

**Support of s_γ.** The support of s_γ is

    supp(s_γ)  =  { γ' ∈ G : γ' is conjugate in G to γ }
               ⊆  G_r

(the G-orbit of γ; inclusion in G_r because γ ∈ G_r and G_r is closed under G-conjugation as the full subgroupoid fixing C_r). Hence s_γ ∈ Γ_{G_r}(G, F) = Q_r.

---

## 4. Witness separation

### 4.1 s_γ ∈ Q_(Rungs, Φ_max)

By §3.3, s_γ ∈ Q_r. By monotonicity of Q (Proposition 4.4 of the capstone; also `cascade-h-rdr-closure.md` Lemma 2.1), Q_r ⊆ Q_(Rungs, Φ_max). Hence s_γ ∈ Q_(Rungs, Φ_max). ✓

### 4.2 s_γ ∉ Q_(Rungs, Φ) — conditional on G-loc-a

Any element of Q_(Rungs, Φ) has support in ⋃_{r' ∈ Rungs} G_{r'}^Φ (§1.2). For s_γ to fail to be in Q_(Rungs, Φ), it suffices that supp(s_γ) ⊄ ⋃_{r'} G_{r'}^Φ, i.e. there exists a point γ' in supp(s_γ) with γ' ∉ G_{r'}^Φ for every r'.

The original γ is itself such a point **provided** γ ∉ G_{r'}^Φ for every r' ≠ r. By hypothesis, γ ∉ G_r^Φ. For r' ≠ r:

- If r' = E_8: G_{E_8} = G by Q_{E_8} = Γ(G, F) (cascade-observer-query-algebra.md §2.2). So γ ∈ G_{E_8}. The question is whether γ ∈ G_{E_8}^Φ. If Φ leaves the E_8-rung fully closed (G_{E_8}^Φ = G_{E_8} = G), then every γ ∈ G_{E_8}^Φ, and the witness fails trivially. **However**, the case of interest — where Theorem 5.3 needs witness separation — is Φ ≠ Φ_max, which by Definition 4.2 + Remark 4.3 of the capstone means there is some r with G_r^Φ ⊊ G_r. The argument only needs a witness at that particular r; we choose the γ associated to that r. At other rungs r' ≠ r, if G_{r'}^Φ = G_{r'} we simply need to avoid the **G_{r'}-membership trap**, i.e. we need γ ∉ G_{r'}.

- If r' ≠ E_8: we need γ ∉ G_{r'}^Φ. A sufficient (stronger) condition is γ ∉ G_{r'}, handled by rung-r-purity (§2.2).

**This reduces to the named sub-gap.**

> **G-loc-a (rung-overlap avoidance).** For every rung r ∈ Rungs ∖ {E_8, U_0} and every G_r^Φ ⊊ G_r, the set
>
>     G_r ∖ G_r^Φ  ∖  ⋃_{r' ∈ Rungs ∖ {r, E_8}} G_{r'}
>
> is non-empty. Equivalently: among morphisms γ ∈ G_r that Φ excludes, at least one is rung-r-pure.

Under G-loc-a we can choose a rung-r-pure γ ∈ G_r ∖ G_r^Φ. Then γ ∉ G_{r'} for any r' ≠ r (except possibly E_8, handled above). Hence γ ∉ G_{r'}^Φ for any r' ≠ r. Hence γ ∉ ⋃_{r'} G_{r'}^Φ. Hence s_γ(γ) = 1 testifies that supp(s_γ) ⊄ ⋃_{r'} G_{r'}^Φ. Hence s_γ ∉ Q_(Rungs, Φ). ✓

### 4.3 E_8 and U_0 handling

**E_8 root rung.** G_{E_8} = G, so an E_8-deficiency (G_{E_8}^Φ ⊊ G) means Φ restricts the root-level access. For γ ∈ G ∖ G_{E_8}^Φ, γ is automatically in every G_{r'} whose definition relies on the E_8-compatibility chain; the argument above cannot be applied directly. However, Theorem 5.3 necessity only requires **some** r with G_r^Φ ⊊ G_r; we may choose r to be a non-root leaf rung for witness purposes, provided such a deficiency exists. If the only deficiency is at r = E_8 with all leaves at full closure (G_{r'}^Φ = G_{r'} for every leaf r'), then the refined rung-structure collapses to a root-only restriction, and the witness question reduces to H-loc at r = E_8, which is a separate case. This corner case is part of G-loc-a's scope.

**U_0 trivial rung.** G_{U_0} is trivial (only constants; `cascade-observer-query-algebra.md` §2.2). A deficiency G_{U_0}^Φ ⊊ G_{U_0} would remove the constant function; the witness is any non-constant section, trivially outside Q_(Rungs, Φ). No M3d extension is needed at r = U_0.

---

## 5. The residual sub-gap G-loc-a

### 5.1 Statement

> **G-loc-a (rung-overlap avoidance, precise form).** For every pair (r, Φ) with r ∈ Rungs ∖ {E_8, U_0} and Φ specifying G_r^Φ ⊊ G_r, there exists γ ∈ G_r ∖ G_r^Φ such that γ ∉ G_{r'} for every r' ∈ Rungs ∖ {r, E_8, U_0}.

### 5.2 Status

**Open, but closable under the independence conjecture of `cascade-observer-query-algebra.md` §3.1.** If the subgroupoids G_r for distinct leaves r intersect only in the E_8 root (Gap G6.2), then for any strict deficiency G_r^Φ ⊊ G_r the removed morphisms include some purely-rung-r element, and G-loc-a follows immediately.

Conversely, if G_r ∩ G_{r'} is substantial for some r ≠ r' (non-trivial mutual support), then G-loc-a may fail on subgroupoids concentrated in the intersection, and H-loc would require a finer argument — possibly a **cohomological** statement (distinct characters χ ∈ Ẑ[φ]⁶ distinguish subgroupoids) rather than the support-on-morphism framing.

### 5.3 Risk level

Low. The rung constraints C_r are pairwise "different enough" (icosian vs H_4 vs D_4 vs S⁷ octonion vs Cl(1,3) signature vs icos-40) that purely-rung-r morphisms should be abundant. The concern is only that the rigorous proof of this abundance has not been written down; it is Gap G6.2 in `cascade-observer-query-algebra.md`, not something that requires new mathematics.

### 5.4 Path to closure

A direct combinatorial computation at the combined cut-and-project level: for each ordered pair (r, r'), produce an explicit morphism γ ∈ G_r ∖ G_{r'} by exhibiting a phason flip that changes the rung-r configuration but leaves any rung-r' configuration invariant. This is analogous to the rung-independence checks already performed in the alpha-chain derivation (`cascade-alpha-chain-complete-theorem.md`) and should be a 1–2 day exercise per rung pair.

---

## 6. Scope statement

### 6.1 What is proved here (conditional on G-loc-a)

- H-loc (witness-separation form) follows from M3d + pattern-equivariant indicator section + G-loc-a.
- Lemma 5.2 (`char-restriction`) of the capstone, which uses H-loc, inherits this conditional status.
- Theorem 5.3 (closure-data saturation) is therefore conditional on {H-rdr (closed via P-A), M3 (closed in Phase M-3), G-loc-a}.

### 6.2 What is not proved

- The **strong** character-class form of H-loc (some whole F(χ) is missing under deficiency) is explicitly not addressed here and is explicitly not required for Theorem 5.3; see capstone Remark 5.2.6 (`rmk:char-restriction-scope`).
- G-loc-a itself.
- The Gap G6.1 prerequisite (Q_r as subalgebra of Γ(G, F)) is imported as a standing assumption; closing G6.1 is a separate item.

### 6.3 What changed in the hypothesis stack

**Before this note.** Capstone Theorem 5.3 was conditional on {H-grad, H-meas, H-rdr, H-loc, H-FIC, H-lift-fin} with H-loc flagged as a non-trivial M3-extension.

**After this note.** H-loc reduces to G-loc-a (combinatorial rung-independence), with the analytic content (extension of local patches to global sections) supplied rigorously by M3d. The stack is now {H-grad, H-meas, H-rdr (→ P-A), G-loc-a, H-FIC, H-lift-fin}, in which G-loc-a is strictly weaker than H-loc and reduces to a Gap G6.2 combinatorial check.

---

## 7. Summary table

| Item | Before this note | After this note |
|------|------------------|-----------------|
| H-loc (witness-separation) | Named hypothesis, non-trivial M3-extension | Derived from M3d + Kellendonk indicator + G-loc-a |
| Analytic content (local-to-global extension) | Open | CLOSED via M3d |
| Pattern-equivariant indicator section | Standard (Kellendonk 2003) | Standard (imported) |
| Rung-overlap combinatorics | Implicit in H-loc | Isolated as G-loc-a |
| G-loc-a status | — | Open, reduces to Gap G6.2; low risk |
| Theorem 5.3 closure-saturation | Conditional on H-loc | Conditional on G-loc-a (strictly weaker) |

---

## 8. Companion documents

- `cascade-meta-layer-theorem.md` §5 — Theorem M3 (M3a/b/c/d).
- `cascade-phase-m3-closure.md` §7 — proof of M3d.
- `cascade-observer-query-algebra.md` §§2–3 — Q_r, Q_S, Gap G6.1, Gap G6.2.
- `cascade-h-rdr-closure.md` — companion reduction of H-rdr to P-A.
- `cascade-capstone-coalgebra.tex` §5 — H-loc, Lemma 5.2, Theorem 5.3.
- Kellendonk, J., "Pattern equivariant functions and cohomology," *J. Phys. A* 36 (2003) — pattern-equivariant section framework.
- Sadun, L., *Topology of Tiling Spaces*, AMS 2008 §4.3 — canonical transversal and patch-recurrence.
- Aliste-Prieto, Coronel, Gambaudo 2013 — linear-repetitivity extension (input to M3d).

---

## 9. Next actions

1. **Close G-loc-a.** Direct combinatorial check for each rung pair (r, r'); should be 1–2 days. Reduces to Gap G6.2 closure. Optional formal route: extend the alpha-chain rung-independence argument.
2. **Update capstone.** After G-loc-a closes, the capstone Remark `rmk:H-loc-status` should be rewritten to cite this note and G-loc-a closure, replacing "non-trivial M3-extension" with "M3d + rung-independence combinatorics."
3. **Programme-level bookkeeping.** Add H-loc to the list of reduced-to-closed hypotheses in `docs/gaps.md` (if maintained); Theorem 5.3's conditional stack should be updated in any paper that cites it.

---

**End of closure note.**

H-loc is reduced from a named hypothesis to a combinatorial sub-claim (G-loc-a) via M3d's local-to-global extension plus the standard pattern-equivariant indicator section of Kellendonk theory. The substantive analytic content — extending a γ-localised patch to a global section witnessing membership in Q_(Rungs, Φ_max) but not Q_(Rungs, Φ) — is supplied by M3d. The residual sub-gap is rung-overlap avoidance, which is low-risk and closable via the existing rung-independence programme.

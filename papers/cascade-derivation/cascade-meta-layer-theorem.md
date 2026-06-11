# The Cascade Moduli Meta-Layer — Consolidated Theorem Chain

**Status: CONSOLIDATED WORKING NOTE, theorem-grade.** Brings together the three Phase-M closure documents (`cascade-phase-m1-closure.md`, `cascade-phase-m2-closure.md`, `cascade-phase-m3-closure.md`) into a single statement of the complete theorem chain. Individual proofs are in the phase documents; this document states the theorems cleanly, explains their interrelation, and records the honest-closure caveats.

**Date consolidated:** 2026-04-21 (same-day consolidation after phase closures; stress-tested per `cascade-phase-m1-closure.md` / `cascade-phase-m2-closure.md` / `cascade-phase-m3-closure.md` abstracts).
**Parent working note:** `cascade-moduli-meta-layer.md` (architectural; pre-proof).
**Authoritative conventions:** `papers/cascade-12d-closure/cascade-12d-closure.tex` (tex), Z-rank default.

---

## 0. Executive summary

Above the 12D closure L₁₂ = E₈ ⊕ M, there is no geometric extension to higher dimension (tex Theorem C2 rules this out). But there *is* a canonical **moduli / groupoid / sheaf layer** over L₁₂, built from the natural phason structure. This consolidated document states the three theorems establishing that layer:

- **Theorem M1 (Phase M-1):** the moduli space 𝓜 of cuts through L₁₂ is uniquely determined as the abstract Pontryagin dual of the discrete group π_int(L₁₂).
- **Theorem M2 (Phase M-2):** the matching groupoid G over 𝓜 has abelianised vertex group T_meta ≅ M ≅ Z[φ]² (at the upper cut-and-project level).
- **Theorem M3 (Phase M-3):** the tiling hull (Ω, R⁴_phys-action) at the combined cut-and-project level is minimal, uniquely ergodic, and linearly repetitive, with unique local-to-global extension of finite-patch assignments.

**Equivalence relation of tex Def. 4.8** is supplied by Lemma 3.2 (closed in Phase M-1): two phason offsets t, t′ are equivalent iff t − t′ ∈ π_int(L₁₂). This completes the missing formal content the WO-CCC-alpha1 review checklist required.

**Downstream effect.** T_PH_1 of the photon-microtubule-α programme is refined from the original rank-1 conjecture T ∈ {Z, Z[φ]} to the rigorous rank-2 answer T_meta ≅ Z[φ]². The rank-2 structure is consistent with (but does not derive) the two photon polarisations of T_PH_4(d).

---

## 1. Preliminaries

### 1.1 Standing data (classical package)

Fix once and for all:
- K = Q(√5), 𝒪_K = Z[φ], φ = (1+√5)/2.
- σ ∈ Gal(K/Q), σ(φ) = 1 − φ.
- I = icosian ring (rank-4 Z[φ]-module, rank-8 Z-module).
- E₈ realised via the classical icosian construction E₈ ≅ {(x, σ(x)) : x ∈ I} as a Z-submodule of R⁴_phys ⊕ R⁴_int (Conway–Sloane Ch. 8; Moody–Patera Thm. 4.1; Elser–Sloane 1987).
- M — phason complement at the upper cut-and-project level; under tex Hyp. H_min and Thm. C1, M ≅ Z[φ]² as a Z[φ]-module (Z-rank 4).
- L₁₂ = E₈ ⊕ M (Z-rank 12, Z[φ]-rank 6; tex Thms. C1/C2/C3).
- W_lo ⊂ R⁴_int — σ-twisted golden-boundary window (Elser–Sloane acceptance window).
- W_up ⊂ R⁴_int' — second-level σ-twisted acceptance window at the upper cut-and-project.
- W_tot = W_lo × W_up ⊂ R⁸_int (combined-level window).

### 1.2 Cut-and-project levels [clarified post-review round 2, 2026-04-23]

| Level | Physical | Internal | Internal image of L₁₂ | π_int rank | π_int density |
|-------|----------|----------|-----------------------|-----------|---------------|
| Upper (L₁₂ → E₈) | R⁸_phys (contains E₈) | ℍ_int' ≅ R⁴ | M | Z-rank 4, Z[φ]-rank 2 | discrete |
| Lower (E₈ → H₄) | R⁴_phys (contains H₄ vertices) | ℍ_int ≅ R⁴ | σ(I) | Z-rank 8, Z[φ]-rank 4 | dense |
| Combined (L₁₂ → H₄) | R⁴_phys | R⁸_int = ℍ_int ⊕ ℍ_int' | σ(I) ⊕ M | Z-rank 12, Z[φ]-rank 6 | dense |

**Level discipline (explicit).** Different phase closures use different level choices:
- **Phase M-1** constructs 𝓜 at the **combined level** (ambient R¹², internal R⁸_int total). The Pontryagin dual is over the combined discrete group σ(I) ⊕ M.
- **Phase M-2** identifies T_meta at the **upper level** (ambient R⁸ × R⁴_int', internal R⁴_int'). T_meta = Z[φ]² = M here.
- **Phase M-3** applies M3a/b/c/d dynamics at the **combined level** (H₄ quasicrystal tiling).
- **Phase P-1** works with σ-decomposition at upper level (T_meta's diagonal).

These are valid level choices, not contradictions. Pontryagin duality holds at each fixed level; it does not mix levels. When a downstream theorem says "T_meta = X" or "𝓜 = Y", check which level is invoked.

**Level discipline.** All statements of moduli, T_meta, and H¹ are level-dependent. Cross-level identifications are always explicit; Pontryagin duality holds at each fixed level but does not cross levels.

### 1.3 Standing hypotheses

- **F1** — permeability axiom r = 1 + 1/r (tex axiom; proved in `cascade-correspondence-foundations/foundations.tex`).
- **H_min** — phason coefficient ring is the minimal extension of Z compatible with F1 (tex Hyp. 4.10).
- **C1, C2, C3** — tex theorems (closed under H_min in the tex; closure in `cascade-phase-b-c1-c2-c3.md`).

Under F1 + H_min + C1/C2/C3, the standing data of §1.1 is fully determined, and the meta-layer construction below proceeds unconditionally from there.

### 1.4 Tilings as model sets

For any phason offset t ∈ R_int (at the relevant level), the **projected tiling** is

    T_t := π_phys({ ℓ ∈ L : π_int(ℓ) ∈ W + t }),

where L is the relevant lattice (E₈, L₁₂, or whichever cut is considered) and W is the relevant window. For generic t (window-boundary-transversal), T_t is a regular Meyer set.

---

## 2. Theorem M1 — moduli-space uniqueness

### Statement

> **Theorem M1.** At any cut-and-project level, the **moduli space of cuts** 𝓜 is the unique compact Hausdorff topological abelian group admitting a continuous surjection R_int → 𝓜 such that:
>
> (i) σ-equivariance: the Galois involution σ acts on 𝓜;
> (ii) Z[φ]-module structure: 𝓜 is a Z[φ]-module quotient;
> (iii) well-definedness of F: t ↦ T_t factors through the quotient.
>
> **Construction:** 𝓜 is the **abstract Pontryagin dual of π_int(L) viewed as a discrete abelian group**, equivalently the internal fiber of the Bellissard–Kellendonk–Sadun tiling hull.

At the three levels of §1.2, the moduli topology is:

| Level | 𝓜 topology | Character group of 𝓜 |
|-------|-------------|----------------------|
| Upper | T⁴ (genuine 4-torus) | Z[φ]² |
| Lower | 4-solenoid | Z[φ]⁴ |
| Combined | mixed torus × solenoid | Z[φ]⁶ |

### Proof

In `cascade-phase-m1-closure.md` §4 (Steps 1–7) + Check 4.

### Key inputs
Pontryagin duality (Hewitt–Ross); Bellissard–Kellendonk–Sadun tiling hull theory (Sadun 2008 §2.5–§4); Lemma 3.2 below.

### Status
**CLOSED rigorously, Phase M-1.**

---

## 3. Lemma 3.2 — phason equivalence (closes tex Def. 4.8)

### Statement

> **Lemma 3.2.** Two phason offsets t, t′ ∈ R_int (at any level, for generic t, t′) satisfy
>
>     T_t and T_{t′} coincide up to rigid R_phys-translation
>     ⟺
>     t − t′ ∈ π_int(L),
>
> where L is the ambient lattice at that level. The required physical shift is v = −π_phys(ℓ) for any ℓ ∈ L with π_int(ℓ) = t − t′.

### Proof

In `cascade-phase-m1-closure.md` §2 (Forward direction: direct change of variables; Reverse direction: Baake–Moody–Schlottmann model-set rigidity).

### Key inputs
Baake–Moody–Schlottmann rigidity (Schlottmann 2000 Thm. §4; Baake–Grimm *Aperiodic Order* Vol. 1 Prop. 7.2–Thm. 7.3, 2013).

### Closure of tex Def. 4.8

The equivalence relation required by WO-CCC-alpha1 §4.8 is **Lemma 3.2**. Camera-ready tex form in `cascade-phase-m1-closure.md` §3.2, ready for integration as a new `\begin{definition}\label{def:phason-eq}...` block in the tex cascade-12d-closure paper.

### Status
**CLOSED rigorously, Phase M-1.**

---

## 4. Theorem M2 — matching groupoid and T_meta

### Statement

> **Theorem M2.** Let G be the matching groupoid over 𝓜 at the **upper level**, with objects 𝓜_up and morphisms = finite sequences of phason flips (Definitions 2.2–2.3 of `cascade-phase-m2-closure.md`). Then G is a connected groupoid (π₀(G) = {*}) and for any basepoint m ∈ 𝓜_up,
>
>     T_meta := π₁(G, m)_ab ≅ π_int(L₁₂)_up = M ≅ Z[φ]².
>
> **Canonical identification chain:** T_meta ≔ π₁(G, m)_ab ≅ Ȟ¹(Ω_up, Z) ≅ π_int(L₁₂)_up = M ≅ Z[φ]².

### Proof

In `cascade-phase-m2-closure.md` §4 (Steps 1–5).

### Key inputs
Forrest–Hunton–Kellendonk tiling cohomology (Memoirs AMS 159, 2002); Kellendonk pattern-equivariant cohomology (J. Phys. A 36, 2003); Baake–Grimm flip catalogue (Ch. 7, 2013); tex Thm. C1.

### Status
**CLOSED rigorously, Phase M-2.**

### Refinement of T_PH_1

`cascade-photon-microtubule-alpha-programme.md` T_PH_1 originally conjectured T ∈ {Z, Z[φ]} (rank 1). Theorem M2 shows the rigorous answer is **rank 2**: T_meta ≅ Z[φ]². The T_PH_1 document has been updated in place (2026-04-21) to cite Theorem M2.

### Interpretive note (not a theorem)
The rank-2 structure of Z[φ]² is **consistent with** the two photon polarisations of T_PH_4(d), but Phase M-2 does **not derive** the polarisation count. The natural-interpretation reading is in `cascade-phase-m2-closure.md` §5.2; this is an interpretation, not a separate theorem.

---

## 5. Theorem M3 — local-to-global coherence (refined)

### 5.1 The original conjecture is retired

The original Conjecture M3 stated "H¹(𝓜, F) = 0." This is **literally false**: the tiling-hull cohomology computes to

| Level | Ȟ¹(Ω, Z) |
|-------|----------|
| Upper | Z[φ]² |
| Lower | Z[φ]⁴ |
| Combined | Z[φ]⁶ |

Non-zero at all levels. The non-zero H¹ represents **winding observables** (integer winding counts around phason-translation cycles, Pontryagin-dual to T_meta), not gluing obstructions. See §6 below.

### 5.2 Refined M3 statement

The "local-to-global coherence" intuition captured by the working-note's original M3 is, correctly, a **dynamical-systems** statement, not a sheaf-cohomology statement. Phase M-3 splits it into four theorems (all closed):

> **Theorem M3.** At the combined cut-and-project level (L₁₂ → H₄), the tiling hull Ω under R⁴_phys-translation satisfies:
>
> - **(M3a, minimality):** every R⁴_phys-orbit is dense in Ω.
> - **(M3b, unique ergodicity):** there is a unique R⁴_phys-invariant probability measure on Ω.
> - **(M3c, linear repetitivity):** for generic m ∈ 𝓜_combined, T_m is linearly repetitive (every patch of diameter r appears in every ball of radius C·r for some constant C > 0).
> - **(M3d, local-to-global):** every locally-consistent finite-patch assignment on a bounded region of R⁴_phys extends uniquely, up to rigid R⁴_phys-translation, to a global tiling in Ω.

### Proof

In `cascade-phase-m3-closure.md` §§4–7.

### Key inputs
Schlottmann minimality and unique ergodicity (2000, §4); Moody model-set survey (2002, Thm. 10); Lagarias–Pleasants linear repetitivity (2003, Thm. 2.4); Aliste-Prieto–Coronel–Gambaudo local-to-global (2013, §2); Sadun tiling-space topology (2008, §4.3).

### Status
**CLOSED rigorously, Phase M-3 (all four of M3a/b/c/d).** Original H¹(𝓜, F) = 0 framing retired; see §5.1 and §6.

---

## 6. Observables: what H¹(Ω, Z) actually is

Phase M-3 §8 clarifies that the non-zero H¹(Ω, Z) is **not** a gluing obstruction but a set of **winding observables** on the tiling:

- Each generator of Ȟ¹(Ω, Z) corresponds to a phason-translation direction in L₁₂.
- Integrating a 1-cochain against a closed path in Ω picks out the integer winding number in that direction.
- Pontryagin duality: Ȟ¹(Ω, Z) at each level equals T_meta at that level as abstract discrete abelian groups.

**Physical content.** At combined level, Z[φ]⁶ has 6 independent generators. These are **not** "six independent photon modes" — they are abstract winding observables of the L₁₂ tiling. The reduction to photon modes / polarisations / gauge structure requires the descent via T_PH_2 (still open) and is not automatically derivable from H¹ alone.

---

## 7. Interface with the downstream programme

### 7.1 T_PH_1 refinement (done)

`cascade-photon-microtubule-alpha-programme.md` T_PH_1 has been updated:

> **T_PH_1 (refined, 2026-04-21):** Above L₁₂, the abelianised vertex group of the matching groupoid is T_meta ≅ M ≅ Z[φ]² (rank 2 over Z[φ], rank 4 over Z). Proof: Theorem M2. Key inputs: Forrest–Hunton–Kellendonk tiling cohomology + Kellendonk pattern-equivariant identification + tex Thm. C1.

### 7.2 T_PH_2 (descent to U(1)) — still open

The descent Z[φ]² → U(1) requires an additional input beyond Theorem M2. Possibilities noted in `cascade-phase-m2-closure.md` §5.4:
- Diagonal quotient Z[φ]² → Z[φ] (sum coordinate) → R/Z → U(1).
- Polarisation axis fixing: one Z[φ]-factor as "photon axis," the other as orthogonal polarisation.
- Complex U(1) rep on a 2D complex space: the two Z[φ]-factors are independent generator directions within the single U(1) rep.

A Phase M-2-plus or later phase needs to establish which. Theorem M2 supplies the starting object; does not close T_PH_2.

### 7.3 T_MT_1 (13-protofilament count) — orthogonal to the meta-layer

The "13-count" of the microtubule structure is **not** derivable from T_meta = Z[φ]². It must come from a separate structural input — likely an H₄-graph Laplacian spectrum or a specific orbit count on E₈ minimal vectors. See `cascade-phase-m2-closure.md` §5.5.

### 7.4 Relation to tex cascade-12d-closure

The tex paper (`papers/cascade-12d-closure/cascade-12d-closure.tex`) provides C1, C2, C3. The meta-layer theorem chain in this consolidated document:

- **Uses** C1, C2, C3 as inputs (tex is upstream).
- **Supplies** the equivalence relation for Def. 4.8 (Lemma 3.2 here; camera-ready tex form in `cascade-phase-m1-closure.md` §3.2).
- **Does not modify** any C1/C2/C3 statement.
- **Lives outside** the tex's strict scope (tex is about 12D closure; meta-layer is a moduli layer over L₁₂ — a different theorem category).

If a future paper integrates the meta-layer into external publication, it would be a separate tex paper, not an extension of cascade-12d-closure.tex.

---

## 8. Honest caveats and known boundaries

### 8.1 What is genuinely closed

- Lemma 3.2 (phason equivalence) — rigorous.
- Theorem M1 (moduli uniqueness) — rigorous.
- Theorem M2 (T_meta = Z[φ]² at upper level) — rigorous.
- Theorem M3a, M3b, M3c, M3d (minimality, unique ergodicity, linear repetitivity, local-to-global) — rigorous at combined level.

### 8.2 What required reframing

The original Conjecture M3 ("H¹(𝓜, F) = 0") was literally false. Phase M-3 reframed it into M3a/b/c/d and retained the intended "local-to-global coherence" content. This is a conjecture-refinement, honest and explicit; see Phase M-3 §8.

### 8.3 What is not closed

- **T_PH_2 descent** (Z[φ]² → U(1)) — open.
- **T_MT_1 13-count** — decoupled from the meta-layer; separate open problem.
- **Observer-boundary interpretation** — H¹ ≠ 0 means there are winding observables; whether the non-triviality locus of any H¹-class has a physical "observer boundary" interpretation is speculative and not addressed.
- **Consciousness framing** — explicitly out of scope at all phases; the meta-layer is a mathematical construct, consistent with `cascade-consciousness.md`'s separation discipline.

### 8.4 Risk level

Low. All classical inputs are settled theorems in the aperiodic-order literature:
- Schlottmann 2000, Moody 2002 — minimality / unique ergodicity.
- Lagarias–Pleasants 2003 — linear repetitivity.
- Aliste-Prieto–Coronel–Gambaudo 2013 — local-to-global.
- Forrest–Hunton–Kellendonk 2002, Sadun 2008 — tiling cohomology.
- Baake–Grimm 2013 — flip catalogue / rigidity.
- Hewitt–Ross — Pontryagin duality.

No speculative mathematics. The novel content is the **assembly** of these classical results around L₁₂ (verifying hypotheses for the specific cut-and-project package), plus the tex-compatible equivalence relation in Lemma 3.2.

---

## 9. Summary table

| Object | Statement | Phase | Status |
|--------|-----------|-------|--------|
| ~ (phason equivalence) | t ~ t′ iff t − t′ ∈ π_int(L) | M-1 Lemma 3.2 | CLOSED |
| 𝓜 (moduli space) | Pontryagin dual of π_int(L) as discrete group | M-1 Thm. M1 | CLOSED |
| G (matching groupoid) | Objects 𝓜, morphisms = flip sequences | M-2 §3 | RIGOROUS |
| T_meta (upper level) | ≅ M ≅ Z[φ]² | M-2 Thm. M2 | CLOSED |
| Minimality | R⁴_phys action on Ω is minimal | M-3 M3a | CLOSED |
| Unique ergodicity | unique invariant probability measure | M-3 M3b | CLOSED |
| Linear repetitivity | patches repeat in bounded-radius balls | M-3 M3c | CLOSED |
| Local-to-global | local patches extend uniquely globally | M-3 M3d | CLOSED |
| tex Def. 4.8 | equivalence relation, camera-ready | M-1 §3.2 | READY FOR TEX |
| T_PH_1 refinement | T_meta = Z[φ]² (rank 2, not rank 1) | M-2 §5.3 | APPLIED TO PROGRAMME DOC |
| T_PH_2 descent | Z[φ]² → U(1) | — | OPEN |
| T_MT_1 13-count | decoupled from meta-layer | — | OPEN (orthogonal) |
| H¹(Ω, Z) interpretation | winding observables (not obstructions) | M-3 §8 | CLARIFIED |

---

## 10. Recommended next phases

Per `cascade-phase-m3-closure.md` §12.2 Options A/B/C/D:

**Option B — T_PH_2 attack (1–2 weeks).** The natural research sequel. With T_meta = Z[φ]² rigorous, attempt the descent to U(1) via one of the routes in §7.2 above. Would close T_PH_2 and unblock T_PH_3/4 via paper-xxxii's graph-Laplacian photon identification.

**Option C — tex integration (1 week).** Draft an inclusion block for the tex cascade-12d-closure paper containing Lemma 3.2 (ready, M-1 §3.2 camera-ready form) + possibly a reference to this consolidated document. May need a separate cascade-meta-layer.tex paper if the content exceeds tex's C1/C2/C3 scope.

**Option D — wait for codex review.** Submit the three phase-closure docs + this consolidation for the standard codex-review workflow (per `feedback_codex_review_workflow.md`) before any further external steps.

---

## 10b. Prospective empirical landing for M-2 (added 2026-04-29)

Theorem M-2 states T_meta = π₁(G,m)_ab ≅ Z[φ]² as an abstract rank-2 abelian group. Empirical landing of this rank-2 structure is *prospective* via aria-chess preregistered prediction H2 (`aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md`):

> **H2 (2-torus PCA):** Exactly two paired eigenvalue modes (PC1-PC2, PC3-PC4) with |log(λ₁/λ₂)| < 0.1, gap λ₂/λ₃ > 0.5.

Two paired modes is the empirical signature one would expect from a rank-2 Z[φ]² structure embedded in continuous dynamics, with the σ-conjugate pair (φ, 1−φ) producing the matched λ₁/λ₂ and λ₃/λ₄ pairings.

**Status:** Forward prediction, not yet entered as confirmed in `CASCADE_VALIDATION_REPORT.md` as of 2026-04-29. Flag as *prospective* witness; do not cite as confirmation. If H2 is later confirmed in independent EEG/MEG data, this becomes empirical landing for M-2; if rejected, M-2 remains a structural theorem without empirical witness, which is the same status it has now.

Reference: `cascade-empirical-grounding.md` §1.7.

---

## 11. Companion documents

- `cascade-moduli-meta-layer.md` — architectural working note (pre-proof, superseded by this consolidation for proof-level claims).
- `cascade-phase-m1-closure.md` — Lemma 3.2 + Theorem M1 proofs.
- `cascade-phase-m2-closure.md` — Theorem M2 proof + T_PH_1 refinement.
- `cascade-phase-m3-closure.md` — Refined M3 (M3a/b/c/d) proofs + H¹ clarification.
- `papers/cascade-12d-closure/cascade-12d-closure.tex` — tex paper providing C1/C2/C3 inputs.
- `papers/cascade-12d-closure/WO-CCC-alpha1.md` — review checklist; Lemma 3.2 closes the Def. 4.8 hook.
- `cascade-photon-microtubule-alpha-programme.md` — downstream photon/MT/α programme; T_PH_1 updated in place.

---

**End of consolidated theorem chain.**
This document is the canonical statement of what the cascade moduli meta-layer is, what has been proved, and what remains open. For detailed proofs, consult the phase-closure documents. For future integration into external-review material, cite this consolidated document plus the phase closures.

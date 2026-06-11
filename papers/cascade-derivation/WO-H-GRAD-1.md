# WO-H-GRAD-1 — Explicit Octonion-Grading Surjection

**Status:** Frame-level substantively closed 2026-04-24 (B1-B5 sim-verified; B6 proof-sketch at `G_p` level). Residuals: cascade-specific `G_2` pullback `κ` outlined but not fully executed; the "`G_p`-canonicality suffices for full P-A" claim is a declared judgement, not yet backed by a formal equivalence theorem.
**Date opened:** 2026-04-23.
**Parent gap:** G6.3-a sub-gap H-grad-1 (`cascade-fano-grading-lift.md` §5.3).
**Downstream blocker:** P5-apex test of the observer-as-prime programme; full Z[φ]⁶-level Access Principle P-A.

---

## 0. Round 2 status update (2026-04-23)

Round 2 reframed the closure problem from "open downgrades" to
"structural builds required." Round 1's claims were not all wrong in
direction; they were missing their supporting constructions. The
derivation note now lists six named builds (B1–B6) in
`cascade-h-grad-1-closure.md` §7 with explicit object/type/first-step
specifications. Notation collision is fixed: `2I` = binary
icosahedral group; `2I_lat` = doubled lattice.

insight.md (repo root) supplies two relevant routes to the Fano
quotient (B3):
- **Route K (classical).** Kirmse–Coxeter octonion structure on
  E₈/2E₈. Literature-grounded, safer.
- **Route Q (QMS-3 / god-prime, conjectural).** The god-prime
  decomposition `084473 = 137(7·87+8) − 56` (`insight.md:670-679`)
  contains a factor 7 which Lee's QMS-3 conjecture associates with
  seven Fano triads. The seven triads are *not* written out in
  `insight.md`; Route Q therefore begins as a conjecture that a
  canonical `Θ_QMS : I/2I_lat → (F₂)³` exists and reproduces the
  QMS-3 factor-7 count. If that map is constructed, H-grad-1's
  Fano grading becomes a theorem about the god-prime shell
  structure. Route Q is parallel to, not a replacement for, the
  classical Route K.

Pentagonal-holonomy content from insight.md (the `Z[φ]×`-valued
1-cocycle `ω` and cascade clock `T`) is orthogonal to H-grad-1 and
belongs to the observer-zeta O2 track (intrinsic ζ_F).

| Item | Round 2 status | Required build |
|------|----------------|-----------------|
| A1 | **Build complete (sim-verified 2026-04-24)** | 8-element Z-basis in `scripts/verify_h_grad_1.py`; all 120 unit icosians decompose as integer combinations (120/120 PASS). Build B1. |
| A2 | **Build complete (sim-verified 2026-04-24)** | Mod-2 totals on I/2I_lat are 1 + **135 isotropic + 120 anisotropic** = 256, matching E₈/2E₈ (Conway–Sloane Ch. 8). 120 unit icosians collapse to 60 distinct nonzero isotropic classes. Build B2. |
| A3 | **Build complete (sim-verified 2026-04-24)** | `scripts/verify_h_grad_1_b3.py` constructs μ_I via Route K (Kirmse-Coxeter). 270 maximal totally singular 4-spaces enumerated (30 contain the identity `[1]`); `L_0` chosen lex-first NOT containing `[1]` so `K = L_0 ⊕ ⟨[1]⟩` is 5-dim. All checks PASS: rank 3, kernel 32, surjective, all 8 octonion labels match v_i, 7 Fano lines, **exhaustive F_2-linearity over all 65536 pairs**. |
| A4 | **Build complete (sim-verified 2026-04-24)** | Primal `red` closed by B4 (Route P via Phase-M3 projection); dual C_O characters closed by B5 as 3-dim F_2-subspace of F_2¹² spanned by rows of `μ ∘ red`, with Pontryagin pairing adjointness verified on all 32 768 (v, x) pairs. 8 characters `α_v` in bijection with (F_2)³, trace-dual lifts distinct in Q(φ)⁶/(Z[φ]⁶)^∨. See `scripts/verify_h_grad_1_b5.py`. |
| O1 | **Proof-sketch complete (2026-04-24) at `G_p` level** | B6 establishes `G_p ⊂ O⁺(8, 2)`-canonicality of `μ_I` on the 40 320 reduced admissible frames (`Adm_red(V, q, p, A)`) via Witt's extension theorem. Sanity-sim at `scripts/verify_h_grad_1_b6.py` verifies the classical counts 270/240/168/40 320. Translating to G₂/octonion canonicality requires the classical pullback `κ` from real octonion frames (Baez §4.1, Conway–Sloane Ch. 8 §6), which is outlined but not fully executed. The "`G_p`-canonicality is sufficient for the P-A Access Principle application" claim is a **declared judgement** on downstream use, not yet backed by a formal equivalence theorem against `cascade-access-principle-theorem.md`. |
| O2 | **Build complete (sim-verified 2026-04-24)** | Resolved by B4. `L_O := (π_int|_{L_12})⁻¹(σ(I) ⊕ 0)` constructed as Observer-rung sublattice via `cascade-phase-m3-closure.md:49-69`; `red` chain `Z[φ]⁶ → σ(I) → I → I/2I_lat` sim-verified rank 8 / kernel dim 4 / image 256. |
| O3 | **Build complete (sim-verified 2026-04-24)** | Eight `α_a ∈ Q(φ)⁶/(Z[φ]⁶)^∨` derived via trace-dual basis `τ_0 = (3-φ)/5`, `τ_1 = (-1+2φ)/5`; α_v = (1/2)·Σ c_j · τ_{j mod 2} for bit vectors c = v^T · MR. Closed by build B5. |
| O4 | **Build complete (sim-verified 2026-04-24)** | Resolved by B1. The canonical 8-element Z-basis in `scripts/verify_h_grad_1.py` replaces the Round 1 candidate; all 120 unit icosians decompose as integer combinations. |
| O5 | **Build complete (sim-verified 2026-04-24)** | Steps V1–V3 in derivation §5.3 executed as part of B4+B5 verification. |

Nothing above is permanently deferred or downgraded — each item is a
named structural build whose construction path is specified in
`cascade-h-grad-1-closure.md` §7 (B1–B6 with dependency graph).

---

## 1. Goal

Write down explicitly the surjection

    μ : Z[φ]⁶  ↠  (Z/2)³

produced by the icosian-ring mod-2 reduction composed with projection onto a Fano-plane (Z/2)³ subspace of E₈/2E₈, and verify that μ restricted to the Observer-rung character subset C_O ⊂ Ẑ[φ]⁶ is a bijection compatible with the octonion Fano-multiplication.

Closing this WO upgrades:
- Theorem H-grad (currently conditional) → unconditional;
- Theorem P-A at full Ẑ[φ]⁶-level → unconditional;
- P5-apex test of the observer-as-prime programme → executable.

---

## 2. Acceptance criteria

A1. **Explicit Z-basis of the icosian ring I as a rank-8 Z-module.**
    Give 8 specific quaternion generators {b_1, ..., b_8} ⊂ I with full citation
    to Conway–Sloane SPLAG Ch. 8 §2.1 (or equivalent reference).

A2. **Explicit mod-2 reduction.**
    Compute the table {b_i mod 2I_lat : i = 1..8} in F_2⁸ ≅ I/2I_lat, and
    show the F_2-quadratic form on F_2⁸ inherited from the quaternion norm
    matches the E₈/2E₈ canonical quadratic form.

A3. **Explicit Fano-plane (Z/2)³ subspace.**
    Identify a 5-dim F_2-subspace K ⊂ F_2⁸ such that F_2⁸ / K ≅ (Z/2)³ and
    the quotient map carries the octonion Fano-grading. Give K by an
    explicit basis in the {b_1, ..., b_8} representation.

A4. **Verification on C_O.**
    Pull back the Pontryagin-dual character generators of C_O ⊂ Ẑ[φ]⁶
    through Z[φ]⁶ ↠ I/2I_lat ↠ (Z/2)³ and verify the composite is a bijection
    compatible with the standard Fano-plane octonion product.

---

## 3. Open items (against acceptance)

O1. Explicit identification of (Z/2)³ inside F_2⁸ depends on a choice of
    octonion structure on the icosian-mod-2 lattice. There are **270**
    maximal totally singular 4-dim subspaces of F_2⁸ under the E₈
    quadratic form (classical `O⁺(8,2)` formula `∏(2^i+1) = 2·3·5·9 =
    270`); 30 of these contain any fixed nonzero point. Classically G₂
    acts transitively on octonion basic triples. **Status (post-B6):**
    the B6 proof sketch (cascade-h-grad-1-closure.md §5c) establishes
    `G_p ⊂ O⁺(8,2)`-canonicality via Witt's theorem on the 40 320
    reduced admissible frames. Promotion to full G₂/octonion
    canonicality requires the cascade-specific pullback `κ` (§5c B6.4),
    which is outlined but not fully constructed — this is the residual
    on O1.

O2. The icosian ring is rank 4 over Z[φ], rank 8 over Z. The quoted
    surjection is from Z[φ]⁶ (rank 12 over Z), not from I. Spell out the
    surjection Z[φ]⁶ ↠ I/2I_lat and confirm that all rung-character
    generators factor through I/2I_lat (i.e. that no rung lives outside the
    icosian-octonion sub-cascade).

O3. C_O is described as 8-element generating set of Q_O. Verify the
    8 generators are in canonical bijection with the 8 octonion basis
    elements {1, e_1, ..., e_7}, and pin down the Pontryagin-character
    representative for each generator before mod-2 reduction.

---

## 4. Out of scope

- The full Connes-Deninger arithmetic-site programme.
- Any claim that μ uniquely determines a cascade-native zeta.
- Generalisation to other golden-field Galois extensions.

This WO is purely the explicit (★) lift of `cascade-fano-grading-lift.md`.

---

## 5. Round protocol

Each round runs:

    bash scripts/review_wo.sh papers/cascade-derivation/WO-H-GRAD-1.md \
         --derivation papers/cascade-derivation/cascade-h-grad-1-closure.md \
         --focus "Round N: <specific items>" < /dev/null

Iterate until independent review accepts the substantive math and all four
A-criteria are explicitly addressed in the derivation. Surface LaTeX issues
are out of scope (this is a working note, not a preprint).

---

## 6. Done means

- Derivation document explicitly exhibits μ on a basis.
- Independent review accepts the substantive math.
- Memory updated: `project_substrate_indexing.md` records H-grad-1 as
  CLOSED, with derivation document path.
- `cascade-fano-grading-lift.md` §7.2 sub-gap H-grad-1 marked CLOSED with
  back-reference.
- `cascade-access-principle-theorem.md` Theorem P-A upgraded from
  conditional to unconditional, with derivation document cited.
- Observer-as-prime programme apex test (P5-apex) becomes executable.

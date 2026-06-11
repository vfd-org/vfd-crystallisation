# Task — H-grad-1 Build B4 (primal reduction `red : Z[φ]⁶ → I/2I_lat`)

**Task type:** Pair-programmer work (codex writes WO, Claude
implements, codex reviews).
**Scope:** Construct the primal reduction map of build B4 in
`cascade-h-grad-1-closure.md` §7. This is the first "genuinely new"
derivation in the H-grad-1 sequence (B1–B3 were literature lookups
or classical constructions; B4 involves the Observer-rung lattice
`L_O`, which is currently only referenced, not constructed).
**Date opened:** 2026-04-24.

---

## §1 Goal

Produce:

1. A derivation-note section (either new §5a or extending §5) that
   **constructs `L_O ⊂ L_12` explicitly** as a rank-8 Observer-rung
   sublattice, and shows `L_O ≅ I` under the icosian identification.
2. A derivation of the primal reduction chain
   ```
   red : Z[φ]⁶  →  L_O / 2L_O  →  I / 2I_lat  ≅  F_2⁸
   ```
   exhibiting:
   - the embedding `Z[φ]⁶ ↪ L_12` (or an explicit quotient from
     `L_12` to `Z[φ]⁶` — whichever is the right direction);
   - the projection `L_12 → L_O` (if `L_O` is a direct summand of
     `L_12`);
   - mod-2 reduction to `L_O / 2L_O`;
   - identification with `I / 2I_lat`.
3. A sim (`scripts/verify_h_grad_1_b4.py`) that implements `red`
   on an enumeration of `Z[φ]⁶` elements (a small ball) and
   verifies:
   - well-definedness (image lands in `F_2⁸`);
   - compatibility with the B3-verified `μ_I`;
   - the composition `μ_I ∘ red` produces the 8 expected Fano
     grading values on the appropriate generating set of `Z[φ]⁶`.

---

## §2 What codex should produce (WO brief)

Fire `scripts/codex_derive.sh` first. Codex should return a
structured WO with:

- **Section A.** Upstream content. What does
  `cascade-12d-closure.md` say about `L_12 = E_8 ⊕ Z[φ]⁴`
  (§Level 4)? What does `cascade-fano-grading-lift.md:171-175`
  say about `L_O`? What's constructed vs only referenced?
- **Section B.** Priority sub-builds inside B4:
  - B4.1 — Explicit construction of `L_O ⊂ L_12` as a rank-8
    sublattice.
  - B4.2 — Identification `L_O ≅ I` (or `L_O = I` via the
    icosian embedding).
  - B4.3 — Embedding or projection between `Z[φ]⁶` and `L_12`.
  - B4.4 — Explicit `red` via composition.
  - B4.5 — Verify `red` respects the F_2-structure and is
    well-defined.
- **Section C.** Ranked obstructions. Which of these are
  literature-supported (cite) and which require genuinely new
  derivation (flag)?
- **Section D.** Does insight.md contain anything relevant?
  Specifically: the pentagonal-holonomy content and QMS-3
  content — are either of these sources of the right `L_O` /
  `red`?
- **Section E.** Status of the "full rank-6 vs rank-8
  mismatch": `Z[φ]⁶` has Z-rank 12, `I/2I_lat` has F_2-rank 8,
  so `red` cannot be injective on `Z[φ]⁶`. What is its image?
- **Section F.** Top 3 next builds / first steps for Claude.

---

## §3 Acceptance criteria

- **AC1:** Explicit construction of `L_O` (as a sublattice of
  `L_12`, with generators in `E_8 ⊕ Z[φ]⁴` or a chosen identification).
- **AC2:** Proof or explicit sim-verification of `L_O ≅ I` under
  the Z-module isomorphism.
- **AC3:** Explicit linear map (over Z[φ] or over Z depending on
  structure) `red : Z[φ]⁶ → L_O / 2L_O → I / 2I_lat ≅ F_2⁸`.
- **AC4:** Sim `scripts/verify_h_grad_1_b4.py` runs and verifies
  `red` on a small enumeration.
- **AC5:** Composition `μ_I ∘ red : Z[φ]⁶ → (F_2)³` sim-verified
  to produce all 8 octonion grading values on a generating set.
- **AC6:** `cascade-h-grad-1-closure.md` §5 and §7 B4 updated to
  BUILD COMPLETE (sim-verified 2026-04-24) where applicable.
- **AC7:** `cascade-h-grad-1-catalogue.md` Builds table and
  Numerical results updated.
- **AC8:** `WO-H-GRAD-1.md` A4, O2 rows updated (A4 still needs
  B5 — only O2 closes here; A4 remains BUILD REQUIRED).

---

## §4 Scope guardrails

- Do NOT attempt B5 (C_O character representatives) this round.
  B5 requires Pontryagin duality on `Z[φ]⁶`, different machinery.
- Do NOT attempt B6 (G₂ canonicality). Deferred.
- Do NOT modify `cascade-12d-closure.md` significantly — it is
  Task #10-closed. If a clarification is needed, restrict to a
  footnote.
- Do NOT declare H-grad-1 closed. Only B4 (→ O2) closes here.
- If `L_O ⊂ L_12` turns out to NOT exist as a natural Z-rank-8
  sublattice (e.g. if `L_12 = E_8 ⊕ Z[φ]⁴` doesn't have `E_8` as
  a direct summand in the needed basis), STOP and report. This
  becomes a structural open problem.
- If `Z[φ]⁶ → L_12` / `L_O` needs a specific choice of basis
  that's not canonical, document the choice and flag canonicality
  as a sub-open-item (not a blocker for B4 sim-closure).

---

## §5 Context files

Required reading:
- `papers/cascade-derivation/cascade-h-grad-1-closure.md` §5
  (current B4 discussion / primal/dual bridge).
- `papers/cascade-derivation/cascade-12d-closure.md` §Level 4
  (`L_12 = E_8 ⊕ Z[φ]⁴`).
- `papers/cascade-derivation/cascade-fano-grading-lift.md:171-175`
  (`L_O` reference).
- `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:480-514`
  (canonical icosian `I`).
- `papers/cascade-derivation/scripts/verify_h_grad_1.py` (B1+B2
  sim for I and I/2I_lat structure).
- `papers/cascade-derivation/scripts/verify_h_grad_1_b3.py` (B3
  sim, for the `μ_I` that `red` must compose with).
- `insight.md` — check for any prior-session content on `L_O` or
  the primal map.

---

## §6 Reviewer expectations

Claude will, after codex returns the WO:
1. Implement per codex's Section B sub-builds.
2. Write the sim, run it, verify ACs.
3. Flip status tags in derivation / catalogue / WO.
4. Fire `scripts/review_wo.sh` for independent audit.

If codex review returns "Publication ready: yes for B4 scope",
B4 → O2 is closed and we move to B5.

# Task — H-grad-1 Build B3 (Fano quotient μ_I via Route K)

**Task type:** Pair-programmer work (codex writes WO, Claude
implements, codex reviews).
**Scope:** Close build B3 in `cascade-h-grad-1-closure.md` §7 via
Route K (Kirmse–Coxeter), producing a concrete surjection
`μ_I : I/2I_lat ↠ (F_2)³` with sim-verified kernel and Fano
incidence.
**Date opened:** 2026-04-24.

---

## §1 Goal

Produce a sim `scripts/verify_h_grad_1_b3.py` (or extend
`verify_h_grad_1.py`) that:

1. **Enumerates all 270 maximal totally singular 4-dim subspaces
   of I/2I_lat ≅ F_2⁸** under the sim-verified form
   `q_I([x]) = Tr_{Q(φ)/Q}(N(x)) mod 2` (build B2). Then constructs
   / filters the 30 Kirmse–Coxeter admissible pointed frames
   used for B3 (those containing the identity class [1]).

2. **Picks one canonical pointed frame `(L_0, η)`** where `L_0`
   is a 4-dim totally singular subspace through `[1]` and
   `η : (F_2)³ → I/2I_lat` is an octonion-basis labelling. The
   kernel of `μ_I` is the 5-dim subspace `K = L_0 ⊕ ⟨[1]⟩`; the
   8 octonion basis classes `[1], [e_1], …, [e_7]` are a
   labelled transversal of `K`, not a vector-space complement
   `W_0` of `L_0`.

3. **Labels** `[e_1], …, [e_7]` with the canonical
   Kirmse–Coxeter Fano incidence so that the 7 Fano lines
   ```
   {e_1, e_2, e_3}, {e_1, e_4, e_5}, {e_1, e_6, e_7},
   {e_2, e_4, e_6}, {e_2, e_5, e_7},
   {e_3, e_4, e_7}, {e_3, e_5, e_6}
   ```
   correspond exactly to F_2³-sum relations
   `v_i + v_j + v_k = 0` where
   ```
   v_1 = (1,0,0), v_2 = (0,1,0), v_3 = (1,1,0),
   v_4 = (0,0,1), v_5 = (1,0,1), v_6 = (0,1,1), v_7 = (1,1,1).
   ```

4. **Defines** `μ_I : F_2⁸ → (F_2)³` by:
   - Decomposes each class `[x] ∈ F_2⁸` as `ℓ ⊕ w` with
     `ℓ ∈ L_0`, `w ∈ W_0`.
   - On `W_0`: sends `[1] ↦ (0,0,0)`, `[e_i] ↦ v_i`.
   - Extends F_2-linearly; `L_0` is the kernel by construction.

5. **Verifies** computationally:
   - `|μ_I⁻¹(0)| = 32` (kernel dim 5).
   - `μ_I` is surjective (image hits all 8 vectors in `(F_2)³`).
   - For each of the 7 Fano lines, `μ_I([e_i]) + μ_I([e_j]) +
     μ_I([e_k]) = 0` in `(F_2)³`.
   - `μ_I` is F_2-linear (sampled on a few pairs).

6. **Prints** PASS / FAIL for each check. If any fail, STOP and
   report — do not hand-tune.

---

## §2 What codex should produce (WO brief)

This task is fired with `scripts/codex_derive.sh` first. Codex
should return a structured WO with:

- **Section A.** Background / literature pointers for
  Kirmse–Coxeter. Identify specifically the Wilson /
  Conway-Sloane construction of the octonion structure on
  `E_8/2E_8`.
- **Section B.** Concrete sub-builds inside B3:
  - B3.1 — enumerate maximal isotropics.
  - B3.2 — canonicality: are all 30 maximal isotropics
    equivalent under the `Aut(E_8)` action on `E_8/2E_8`? If
    yes, any choice is canonical. If no, we need to pin down
    which orbit to pick.
  - B3.3 — choose complement `W_0`.
  - B3.4 — label `W_0` with octonion basis.
  - B3.5 — define and verify `μ_I`.
- **Section C.** Revert or tighten any stale wording in the
  derivation note about B3 (§4 currently has a candidate
  framework that the Route K construction replaces).
- **Section F.** Top 3 sim/proof outputs ranked by value.

---

## §3 Acceptance criteria

- **AC1:** `scripts/verify_h_grad_1_b3.py` (or extended
  `verify_h_grad_1.py`) exists, runs without errors.
- **AC2:** Reports "30 maximal isotropic 4-dim subspaces" (exact
  count; this is the standard E_8/2E_8 fact).
- **AC3:** `μ_I` kernel has exactly 32 elements; image is all 8
  elements of `(F_2)³`.
- **AC4:** All 7 Fano lines verified.
- **AC5:** F_2-linearity verified on at least 20 random pairs.
- **AC6:** Exact arithmetic only; no floating-point.
- **AC7:** `cascade-h-grad-1-closure.md` §4 and §7 B3 updated to
  "BUILD COMPLETE (sim-verified YYYY-MM-DD)" with sim pointer.
- **AC8:** `cascade-h-grad-1-catalogue.md` Builds table updated
  (B3 → BUILD COMPLETE).
- **AC9:** `WO-H-GRAD-1.md` A3 row flipped to BUILD COMPLETE.
- **AC10:** Canonicality (B3.2): if all 30 isotropics are
  `Aut(E_8)`-equivalent, note it and pick the first. If not,
  document which orbit was picked and cite the reason.

---

## §4 Scope guardrails

- Do NOT attempt B4 (primal `red`) or B5 (C_O characters) this
  round.
- Do NOT modify B1/B2 — they are sim-closed.
- Do NOT touch `cascade-algebraic-substrate.tex` or other papers
  outside `papers/cascade-derivation/`.
- If `Aut(E_8)` is NOT transitive on the 30 maximal isotropics
  (which would be surprising given the standard classification),
  stop and report — the canonicality question changes.
- If you can't produce a linear `μ_I` (e.g. because the Fano
  labeling forces a non-linear extension), stop and report. The
  point of this build is a *linear* quotient.

---

## §5 Context files

Required reading:
- `papers/cascade-derivation/cascade-h-grad-1-closure.md` §4
  (current B3 candidate framework).
- `papers/cascade-derivation/cascade-h-grad-1-closure.md` §7 B3
  (build target specification).
- `papers/cascade-derivation/cascade-fano-grading-lift.md` §5.2
  (upstream Fano grading discussion).
- `papers/cascade-derivation/scripts/verify_h_grad_1.py` (B1+B2
  sim — use its basis + q_I).
- `insight.md:670-679` (QMS-3 for context only — this task is
  Route K; QMS-3 is Route Q, separate).

Standard literature (codex has in pretraining):
- Wilson, *The Finite Simple Groups*, Ch. 5 (octonion structure
  on `E_8`).
- Conway & Sloane, *Sphere Packings, Lattices, and Groups* 3rd
  ed., §8.3 (Cayley integers, octonion lattice).
- Baez, *The Octonions* (Bull. AMS, 2002), §4 (Kirmse's rule +
  Coxeter's correction).

---

## §6 Reviewer expectations

Claude will, after codex returns the WO:
1. Implement per codex's Section B.
2. Run the sim and verify all ACs.
3. Flip the status tags.
4. Fire `scripts/review_wo.sh` with focus on B3 only —
   independent audit of the Kirmse–Coxeter construction.

If codex review returns "Publication ready: yes for B3 scope",
B3 is closed.

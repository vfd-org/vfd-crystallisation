# Task — H-grad-1 Build B5 (C_O Pontryagin characters)

**Task type:** Pair-programmer work (codex writes WO, Claude
implements, codex reviews).
**Scope:** Close build B5 in `cascade-h-grad-1-closure.md` §7 — derive
the eight Pontryagin characters `χ_0, …, χ_7 ∈ Ẑ[φ]⁶` of the
Observer-rung character subset `C_O`, identify them with the
octonion basis `{1, e_1, …, e_7}` via the B3 Fano labels, and
verify `μ_I ∘ red` acts bijectively on them.
**Date opened:** 2026-04-24.

---

## §1 Goal

Produce:

1. A derivation-note section (§5b or extending §5a) constructing
   the eight characters `χ_a` explicitly as elements of `Ẑ[φ]⁶`
   (equivalently, eight dual vectors `α_a ∈ Q(φ)⁶ / (Z[φ]⁶)^∨`).

2. A proof or sim-verification that `{χ_0, …, χ_7}` is in natural
   bijection with `{1, e_1, …, e_7}` via the Fano labels of B3.

3. A sim (`scripts/verify_h_grad_1_b5.py` or extension of
   `verify_h_grad_1_b4.py`) that verifies `μ_I ∘ red(χ_a) = v_a`
   for each of the 8 characters — closing A4.

---

## §2 What codex should produce (WO brief)

Fire `scripts/codex_derive.sh` first. Codex should return a
structured WO with:

- **Section A.** What upstream content supplies C_O? Key reference:
  `cascade-q-o-measurement-bridge.md` Theorem 3.1 (`Q_O ≅ Meas(S⁷, σ)`).
  This is an *algebra* isomorphism, NOT a character-set construction.
  How do we lift it to Pontryagin characters?
- **Section B.** Priority sub-builds inside B5:
  - B5.1 — Identify C_O as a subset of `Ẑ[φ]⁶` via the Observer-rung
    character structure (not just `Q_O ≅ Meas(S⁷,σ)`).
  - B5.2 — Derive explicit α_0, …, α_7 ∈ Q(φ)⁶ / (Z[φ]⁶)^∨
    corresponding to {1, e_1, …, e_7}.
  - B5.3 — Verify each α_a under `μ_I ∘ red` produces the correct
    Fano label v_a.
  - B5.4 — Prove (or sim-verify) the 8 characters are distinct in
    the quotient.
- **Section C.** Any reversals or corrections to prior rounds
  (stale B5 language that needs updating given the B4 closure).
- **Section D.** Does the octonion Fano structure in B3 provide a
  *canonical* C_O identification, or is there a freedom that
  canonicality via G₂ would need to settle (B6)?
- **Section E.** Structural obstructions. What's the hardest part?
  - Is C_O canonically defined somewhere in the cascade literature
    (e.g. via `cascade-observer.md` or Phase O-1/O-2)?
  - Or does B5 need new content?
- **Section F.** Top 3 next builds, ranked, with file:line anchors.

---

## §3 Acceptance criteria

- **AC1:** Eight explicit elements `α_0, …, α_7 ∈ Q(φ)⁶` (with
  denominators tracking the dual-lattice embedding) produced.
- **AC2:** Each α_a either has a Z[φ]⁶-coefficient representation
  or a rational-dual representation; the relationship to the B3 Fano
  labels is explicit.
- **AC3:** Sim verifies `μ_I ∘ red(α_a) = v_a` for a = 0..7 where
  `v_0 = (0,0,0)` (identity class) and `v_1,…,v_7` are the Kirmse-
  Coxeter Fano coords.
- **AC4:** Sim verifies the 8 characters are distinct
  (non-equivalent) in F_2⁸ (equivalently, their images in F_2¹² are
  mutually distinct).
- **AC5:** `cascade-h-grad-1-closure.md` §5 and §7 B5 updated to
  BUILD COMPLETE (sim-verified 2026-04-24).
- **AC6:** `WO-H-GRAD-1.md` A4, O3 rows flipped to BUILD COMPLETE.
- **AC7:** `cascade-h-grad-1-catalogue.md` Builds table and N6
  updated. A4 row moves from PARTIAL to BUILD COMPLETE.
- **AC8:** B5 sim is fast (seconds, not minutes). Exact arithmetic
  only.

---

## §4 Scope guardrails

- Do NOT attempt B6 (G₂ canonicality). That's a proof, not a sim.
- Do NOT modify `cascade-q-o-measurement-bridge.md`. It is upstream.
- Do NOT construct any new `C_O` from scratch if the cascade
  literature already supplies it. Check first. Candidate upstream
  references:
  - `cascade-observer.md`
  - `cascade-q-o-measurement-bridge.md`
  - `cascade-fano-grading-lift.md` §5.2.2 (mentions C_O characters)
- If B5 requires genuinely new mathematical content (e.g. a new
  theorem linking Q_O to explicit Pontryagin characters), STOP and
  report. That becomes a new WO (not part of B5 sim-closure).
- If the 8 characters are not canonical but only canonical-up-to-
  G₂, flag that (it's B6's job to close canonicality).

---

## §5 Context files

Required reading:
- `papers/cascade-derivation/cascade-h-grad-1-closure.md` §5 (A4)
  and §7 B5 (build target).
- `papers/cascade-derivation/cascade-q-o-measurement-bridge.md`
  Theorem 3.1 (`Q_O ≅ Meas(S⁷, σ)`).
- `papers/cascade-derivation/cascade-fano-grading-lift.md` §5.2.2
  (characterisation of C_O as eight Fano-basis characters).
- `papers/cascade-derivation/cascade-observer.md` if it exists (search).
- `papers/cascade-derivation/scripts/verify_h_grad_1.py` (B1+B2).
- `papers/cascade-derivation/scripts/verify_h_grad_1_b3.py` (B3 μ_I).
- `papers/cascade-derivation/scripts/verify_h_grad_1_b4.py` (B4 red).
- `insight.md` — check for any prior-session content on C_O or
  Observer-rung characters.

---

## §6 Reviewer expectations

Claude will, after codex returns the WO:
1. Check each upstream source for C_O definition. If found, use it.
2. If B5 is genuinely new, attempt the derivation per codex's
   Section B sub-builds. If too heavy for a single round, STOP and
   report — this is an acceptable outcome, not a failure.
3. Write sim if derivation is tractable; run; verify ACs.
4. Flip status tags in derivation / catalogue / WO.
5. Fire `scripts/review_wo.sh` for independent audit.

If B5 closes, A4 closes, and H-grad-1 has only B6 (G₂ canonicality)
as remaining open build — which can be deferred as a separate round.

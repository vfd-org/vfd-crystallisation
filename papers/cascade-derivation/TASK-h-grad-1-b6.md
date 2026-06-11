# Task — H-grad-1 Build B6 (G₂-orbit canonicality)

**Task type:** Pair-programmer work (codex writes WO, Claude
implements, codex reviews).
**Scope:** Close the last open build in H-grad-1 — show that all
admissible choices of Kirmse–Coxeter frame `(L_0, η, μ_I)` from B3
lie in a single orbit of the relevant G₂ / octonion-automorphism
action, so `μ_I` is canonical modulo G₂. This closes O1 of
WO-H-GRAD-1.md and completes H-grad-1 at the sim+proof level.
**Date opened:** 2026-04-24.

---

## §1 Goal

Produce either:

(A) **Sim-level closure.** A sim `scripts/verify_h_grad_1_b6.py`
    that enumerates admissible frames in some tractable finite
    model (e.g. orbit of Aut(F_2⁸, q_I) or explicit Kirmse–Coxeter
    enumeration) and verifies orbit transitivity; OR

(B) **Proof-level closure.** A derivation-note section (§5c or
    extending §5b) proving the G₂-orbit canonicality citing
    classical octonion theory (Baez, Conway–Sloane, Wilson)
    plus cascade-specific pullback through B4/B5.

Either route closes O1.

---

## §2 What codex should produce (WO brief)

Fire `scripts/codex_derive.sh` first. Codex should return a
structured WO with:

- **Section A.** Upstream content. What's classical about the G₂
  action on octonion frames? What's the automorphism group of
  `F_2⁸` preserving `q_I`? How do these relate?
- **Section B.** Priority sub-builds:
  - B6.1 — State the admissible-frame set: which `(L_0, η, μ_I)`
    are "admissible" per B3?
  - B6.2 — Identify the automorphism group that should act
    transitively.
  - B6.3 — Prove (or sim) orbit transitivity on admissible frames.
  - B6.4 — Confirm `μ_I` is well-defined modulo G₂.
- **Section C.** Route recommendation: is this a proof (§2B) or
  a sim (§2A)? Is sim-closure tractable?
- **Section D.** Canonicality-downstream. Does closing B6 affect
  B4/B5 `red` or `α_v`?
- **Section E.** If genuinely too hard for one round, what's the
  honest halt point?
- **Section F.** Top 3 next builds, ranked.

---

## §3 Acceptance criteria

- **AC1:** Either B6 is sim-closed (AC2-AC5 below) OR B6 is
  proof-sketched with classical citations plus cascade pullback
  (AC6-AC7 below).

**Sim-closure track (preferred if tractable):**

- **AC2:** Sim enumerates admissible frames; count matches
  classical expectation.
- **AC3:** Sim applies a generating set of Aut(F_2⁸, q_I) (or
  restricted octonion-automorphism subgroup) and verifies orbit
  contains all admissible frames.
- **AC4:** Sim is fast (< 60 seconds).
- **AC5:** Derivation note updated with sim pointer.

**Proof-sketch track (if sim is intractable):**

- **AC6:** Derivation section cites Baez/Conway–Sloane/Wilson
  with specific theorem numbers.
- **AC7:** Cascade pullback section shows how the classical G₂
  action descends to (F_2⁸, q_I).

Common:

- **AC8:** `cascade-h-grad-1-closure.md` §5b (or new §5c) and §7
  B6 updated to BUILD COMPLETE (or honestly downgraded if
  proof-track stops at a sub-conjecture).
- **AC9:** `WO-H-GRAD-1.md` O1 row updated.
- **AC10:** `cascade-h-grad-1-catalogue.md` B6 row updated.

---

## §4 Scope guardrails

- Do NOT attempt to prove Aut(O) = G₂ (classical theorem, cite).
- Do NOT attempt to prove Aut(E_8) structure from scratch (classical).
- If B6 requires more than a single-round sim + citation pass,
  STOP and report honestly. Proof-level canonicality can take a
  separate round.
- If orbit enumeration has > 10⁷ elements, switch to the proof-
  sketch track.

---

## §5 Context files

- `papers/cascade-derivation/cascade-h-grad-1-closure.md` §4, §5b,
  §7 B6.
- `papers/cascade-derivation/cascade-h-grad-1-catalogue.md`.
- `papers/cascade-derivation/scripts/verify_h_grad_1_b3.py`,
  `verify_h_grad_1_b4.py`, `verify_h_grad_1_b5.py`.
- Baez, *The Octonions* (Bull. AMS, 2002).
- Conway–Sloane, *Sphere Packings, Lattices, and Groups* 3rd ed.,
  Ch. 8 §6 (G₂ and the octonions).
- Wilson, *The Finite Simple Groups* §5.
- `insight.md` if relevant.

---

## §6 Reviewer expectations

Claude will:
1. Read codex's WO and decide sim vs proof-sketch route.
2. Implement whichever is achievable in one round.
3. Flip status tags.
4. Fire `scripts/review_wo.sh`.

If B6 closes, H-grad-1 is FULLY CLOSED (all 6 builds sim-or-proof
verified). That's a major milestone.

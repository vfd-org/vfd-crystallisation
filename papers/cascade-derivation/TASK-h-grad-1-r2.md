# Task — H-grad-1 Round 2 (foundational cleanup)

**Task type:** Pair-programmer work (codex lead, Claude review).
**Scope:** Round 2 of `WO-H-GRAD-1.md` after codex Round 1 review.
**Date opened:** 2026-04-23.

---

## §1 Context

Codex Round 1 review
(`docs/reviews/WO-H-GRAD-1-20260423T104006Z.md`) returned
"Publication ready: no" with structural defects going beyond the 4
residuals originally planned. The review exposes that the H-grad-1
closure is at least weeks-scale research work, not a single-round
fix. Rather than attempt to close everything in one round and
spiral, Round 2 is scoped to **foundational cleanup + honest
status**.

Task #10 (icosian coordinatisation) has already been resolved
2026-04-23, which unblocks A1.

---

## §2 Goals for Round 2

### Goal G1 — A1 basis verified or honestly deferred

**Current state:** `cascade-h-grad-1-closure.md` §2 proposes a
`Z[φ]`-basis `{1, ω₁, ω₂, ω₃}` with an "exact lookup pending"
caveat. Codex R1 says this is unsupported and the repo-local
canonical source
(`papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:490-499`)
points to an 8-element `Z`-basis via Conway–Sloane Table 8.1.

**Required outcome (pick exactly ONE):**

- (a) Reproduce the Conway–Sloane Table 8.1 `Z`-basis explicitly and
  derive a `Z[φ]`-basis from it (via the PID-freeness argument). If
  the 4-element `Z[φ]`-basis written in the current §2 eq. 2.1 is
  correct after normalization, show the derivation. If not, replace
  eq. 2.1 with the correct 8-element `Z`-basis and downstream
  derivations accordingly.
- (b) Leave §2 as "A1 open — canonical basis in literature but not
  reproduced here; downstream derivations conditional on external
  reference." Honestly mark A1 as not met in Round 2.

Either is acceptable. What is NOT acceptable: continuing to use the
unverified eq. 2.1 downstream without flagging status.

### Goal G2 — Fix `2I` notation collision

**Current state:** `cascade-h-grad-1-closure.md:53` uses `2I` for
the doubled lattice; `cascade-h-grad-1-closure.md:69-70` uses `2I`
for the binary icosahedral group. This is a real bug in a note
whose main subject is mod-2 reduction.

**Required outcome:** Rename one of them consistently throughout
the note. Suggested convention: `2·I` or `2I_lat` for the doubled
lattice, keep `2I` for the binary icosahedral group
(conventional notation across the cascade programme). Apply a
grep-verified clean rename.

### Goal G3 — Honest status downgrades

**Current state:** §4, §5, §6 make overstated status claims that
the derivation does not support. Specifically:

- Line 35: `"CONSTRUCTED via maximal isotropic + quotient"` is
  false. Only a choice-dependent template is sketched.
- Line 184-205: `μ = deg ∘ π` is "not actually defined" because
  `deg` is ambiguous on arbitrary elements of `W` (admitted at
  191-195).
- Line 218-230: The `C_O ↔ octonion basis` claim attributes more
  to `cascade-q-o-measurement-bridge.md` Theorem 3.1 than that
  theorem supplies. Fix the attribution.
- Line 234-236: `red : Z[φ]⁶ ↠ I/2I` is not constructed; currently
  only hypothetical.
- Line 302-305: `"Framework: μ = deg ∘ π ∘ red is well-posed"` —
  false as stated because both `μ` and `red` are unresolved.
- Line 329-333: `"None of this is conceptually new"` is too strong;
  the missing bridge from mod-2 lattice data to `C_O` is a real
  structural gap, not bookkeeping.

**Required outcome:** Every one of these lines downgraded to
accurately reflect what is / isn't established. Use: "candidate
framework, not constructed"; "hypothetical map, not yet defined";
"attribution limited to X"; etc. Tightness matters.

### Goal G4 — Name the structural gap explicitly

**Current state:** Codex R1 identifies the real missing content:
there is no explicit bridge from the primal lattice side
(`Z[φ]⁶`) to the character-side `C_O ⊂ Ẑ[φ]⁶`. The note elides
this.

**Required outcome:** Add a new short subsection (maybe §6 or
appendix) titled something like **"The primal/dual bridge — open
structural problem"** that:

- States the missing bridge precisely: given a putative lattice
  `L_O` (as in `cascade-fano-grading-lift.md:171-175`) with mod-2
  reduction landing in `I/2I`, derive the character-side identification
  `C_O ⊂ Ẑ[φ]⁶`.
- Flags that `L_O` itself is only referenced, not constructed
  (per `cascade-fano-grading-lift.md` current state).
- Does NOT attempt to close the gap. Just names it clearly.

### Goal G5 — WO-H-GRAD-1.md acceptance-status update

**Current state:** `WO-H-GRAD-1.md` is a work-order spec, not a
derivation. Codex R1 audited A1–A4 and O1–O5 status against the
derivation. After Round 2's goals above, update the WO spec to
reflect the new status of each acceptance criterion:

- A1: met / partially met / open / deferred (pick honestly).
- A2: same.
- A3: open (candidate framework, not construction).
- A4: open.
- O1–O5: status as of Round 2.

Add a "Round 2 status update" note at the top of the WO spec
(after the original header) summarising what Round 2 accomplished
vs. what remains.

---

## §3 Acceptance criteria

- **AC1:** G1 outcome is (a) or (b) and is honestly marked.
- **AC2:** No `2I` collision remains. Grep confirms one meaning
  per symbol.
- **AC3:** Each line in G3 is downgraded; no residual over-claims
  on the flagged lines.
- **AC4:** A new subsection names the primal/dual gap as an open
  structural problem.
- **AC5:** `WO-H-GRAD-1.md` has a Round 2 status update block.
- **AC6:** No "publication ready" declaration. H-grad-1 as a
  whole is NOT closed by Round 2; this is an honest-downgrade +
  scaffolding round.
- **AC7:** Do NOT edit `cascade-algebraic-substrate.tex` or
  `cascade-12d-closure.md` — Task #10 already resolved the
  upstream conflict; those files are stable.

---

## §4 Scope guardrails

- **Do not** attempt to close A3 (construct explicit μ) this
  round. That is weeks-scale Kirmse–Coxeter work.
- **Do not** construct `L_O` or the Observer-rung lattice object
  this round. Just name the gap.
- **Do not** construct `red : Z[φ]⁶ → I/2I` this round. Status:
  open / required.
- **Do** keep the narrative flow of `cascade-h-grad-1-closure.md`
  intact. Surgical downgrades, not rewrites.
- If the primal/dual bridge discussion (G4) turns out to need
  actual new work (not just naming), STOP and report. That is a
  new task.

---

## §5 Context files

Required reading (in order):

1. `docs/reviews/WO-H-GRAD-1-20260423T104006Z.md` — the Round 1
   review this round is responding to. Critical.
2. `papers/cascade-derivation/WO-H-GRAD-1.md` — the WO spec.
3. `papers/cascade-derivation/cascade-h-grad-1-closure.md` — the
   derivation note.
4. `papers/cascade-derivation/cascade-fano-grading-lift.md` —
   upstream source, esp. §5.2 and lines 171–175 (`L_O`).
5. `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex`
   lines 480–514 — canonical icosian definition.
6. `papers/cascade-derivation/cascade-q-o-measurement-bridge.md` —
   specifically Theorem 3.1 (to correctly scope the `C_O`
   attribution).

---

## §6 Reviewer expectations

Claude Code will:

1. `git status` (directory is untracked so `git diff` won't show
   much) and direct file reads to verify edits.
2. Check each of AC1–AC7.
3. Fire `scripts/review_wo.sh` on the Round 2 artefacts with
   focus "Round 2 audit: verify foundational cleanup landed, no
   new over-claims, primal/dual gap clearly named". This is the
   independent codex-reviews-codex check.
4. If review verdict is "Publication ready: yes for Round 2
   scope" (meaning the scoped goals G1–G5 landed cleanly, even
   though H-grad-1 as a whole remains open), Round 2 is done and
   we move to the next item.
5. If review lands residuals, iterate in Round 3 on those specific
   residuals.

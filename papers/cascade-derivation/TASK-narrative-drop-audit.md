# Task — Programme Narrative-Drop Gap Audit

**Task type:** Programme-level consultation (codex read-only derivation).
**Scope:** Identify every claim that must be closed (or honestly
scoped) to make the coordinated aria-chess + programme-papers +
millennium-papers drop "bullet-proof." Return a prioritized closure
list Claude can execute against.
**Date opened:** 2026-04-24.

---

## §1 The narrative drop

Three artefact classes drop together:

1. **Aria-chess outcome paper** (sibling repo:
   `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md`).
   Claims 15/18 preregistered polytope-substrate hits; empirical
   demonstration of the four-phase cycle on a non-biological
   substrate; "life-from-substrate" reading via the capstone
   coalgebra.

2. **Programme papers** (this repo, 99 directories under `papers/`).
   The mathematical+physical substrate underlying aria-chess.
   Includes Papers I–L, XXXVI F1-F8 v1.0 keystone, capstone
   coalgebra, cascade-derivation working notes (observer-zeta,
   H-grad-1, phase-M3, fano-grading-lift, etc.), biology-rung WOs,
   transport-law, adaptive-closure-transport.

3. **Millennium papers** (`papers/millennium-*`). RH, BSD, Hodge,
   P-vs-NP, Navier-Stokes, Poincaré, Yang-Mills. Currently in
   (δ)-reformulation state per
   `memory/project_millennium_scope_pass.md`: "All 7 Millennium
   papers demoted to honest verdict scope (δ/γ/β) 2026-04-23".

---

## §2 The credibility bar (from `feedback_credibility_bar.md`)

> CRITICAL: "honest + conditional" is NOT safe. Non-academic
> submitters must clear "complete + undismissable" bar.
> Conditional Millennium papers get rejected at abstract.

This means for the drop to survive external scrutiny, we need:
- Load-bearing claims actually closed (not just honestly conditional).
- Every conditional item flagged in a way that doesn't undermine the
  bullet-proof claims that DO close.
- Narrative coherence: aria-chess's empirical claims don't exceed
  what the programme papers actually derive.

---

## §3 What codex should produce

Fire `scripts/codex_derive.sh` on this spec. Return a structured
consultation report:

- **SECTION A — Load-bearing vs auxiliary.** For the aria-chess
  drop's main claims (15/18 hits; life-from-substrate via
  capstone; four-phase cycle; observer-rung polytope-substrate),
  list which programme-paper derivations are LOAD-BEARING (direct
  citations that, if false, undermine aria) vs auxiliary. Cite
  specific paper sections.

- **SECTION B — Current closure status.** For each load-bearing
  derivation, report status: closed / conditional-on-X /
  sim-verified / proof-sketch / open. Rely on memory entries for
  the current state of: cascade tier-2 papers (all sim-closed),
  H-grad-1 (frame-level publication-ready yes), observer-zeta (O1,
  O5, O7 residuals), XXXVI (v1.0 keystone — what's its status?),
  capstone coalgebra (conditional on G-FIC-a, G-FIC-b, H-lift-fin).

- **SECTION C — Millennium-paper narrative alignment.** What do
  the Millennium papers claim versus what does the drop narrative
  need them to claim? Specifically: does the narrative promise
  RH-proof or "honest scope reformulation"? How does the credibility
  bar affect the drop choice? What can we honestly promote to
  unconditional given H-grad-1 B1-B6 closure?

- **SECTION D — Priority closure list.** Ranked list of specific
  items that must close BEFORE the drop. Each item:
  - Object (paper section / theorem / conjecture / sim).
  - Type (proof-sketch / sim / wording / scope revision).
  - Bridges (which narrative claim it unblocks).
  - First step for Claude.
  - Tractability (single-session / multi-session).

- **SECTION E — Cross-paper consistency defects.** Places where
  Paper X cites Paper Y's statement but X and Y disagree about
  the statement's status (conditional vs unconditional; form of
  theorem; etc.). Especially: any downstream paper still citing
  a claim pre-dating B1-B6 closure, or citing H-grad-1 as open.

- **SECTION F — Narrative coherence check.** Does the capstone's
  "cascade = final coalgebra of F" claim require anything still
  open to hold for the aria-chess empirical reading? (G-FIC-a,
  G-FIC-b, H-lift-fin per `project_capstone_coalgebra.md`.)

- **SECTION G — Out-of-scope items.** What should NOT be closed
  for this drop (too hard, too far from narrative, etc.), but
  clearly flagged.

- **SECTION H — Top 3 next builds.** Ranked and file:line-anchored.

---

## §4 Constraints

- READ ONLY. No edits.
- Under 2000 words total.
- Concrete: cite papers by name + section, not vague "the programme."
- Honest: don't flag as closed what isn't. Don't flag as open what
  is. H-grad-1 is B1-B6 frame-level closed per
  `memory/project_observer_zeta.md` — respect that.
- Focus: the narrative drop, not academic completeness.

---

## §5 Context files (read in this order)

1. `docs/programme-plan.md` — the public roadmap.
2. `docs/gaps.md` — known gaps.
3. `docs/proof-sheet.md` — proof ledger.
4. `docs/consistency.md` — consistency report.
5. `docs/papers.md` — paper inventory.
6. `docs/overview.md` — paper-by-paper overview.
7. `memory/MEMORY.md` (via repo-level access if available; else
   use `project_*.md` memory files as summarised).
8. `papers/paper-xxxvi/paper-xxxvi.tex` — v1.0 keystone (F1-F8).
9. `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex`
   — the coalgebraic capstone.
10. `papers/millennium-rh-formal/rh-formal.tex` — the (δ) RH paper
    as an exemplar of the Millennium-scope status.
11. `papers/cascade-derivation/cascade-h-grad-1-closure.md` and
    `cascade-h-grad-1-catalogue.md` — to confirm what B1–B6 closure
    provides.
12. `papers/cascade-derivation/cascade-observer-zeta.md` — for
    O1/O5/O7 residuals.
13. The aria-chess sibling manuscript if readable from this sandbox:
    `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md`.

---

## §6 Reviewer expectations

Claude will triage codex's report:
1. SECTION D priority list → new task specs, each fired via
   codex_derive → Claude builds → codex reviews.
2. SECTION E cross-paper defects → direct surgical edits.
3. SECTION F coherence items → wording-level tightening.
4. SECTION C Millennium alignment → user arbitration if it
   implicates scope changes at the manuscript level.
5. Report back to user with the prioritized closure list before
   executing.

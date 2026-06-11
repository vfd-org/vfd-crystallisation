# TASK: Close Remaining Biology-Rung Gaps via Named Builds

**Date:** 2026-04-24
**Mode:** Pair-programmer loop — you (codex-5.5 xhigh) write the WO, Claude implements, codex reviews
**Bar:** "Complete + undismissable", NOT "honest conditional" (see feedback_credibility_bar)

## Context

Biology-rung programme has been through many codex review rounds.
Five LaTeX papers exist in `papers/biology-rung-{capsid,amyloid,tubulin,bioelectric,phyllotaxis}/`.
WO-1 (capsid) is fully codex-clean across 6 derivation + 8 paper rounds.
WO-2, WO-3, WO-4, WO-5 each have substantive review feedback that I've
partially addressed. The previous approach was to downgrade claims to
honest conditionals; the user has now directed us to SIM-CLOSE open
items as named builds instead.

## Remaining review feedback to convert into BUILDS

### WO-4 bioelectric (round 1 verdict)

R4-G1. **False "5 cell-graph orbits" attribution persists** at lines
205-209, 318-320, 413-416 of biology-rung-bioelectric.tex. I
partially fixed line 129 but not the other three. Codex explicitly
says WO-1 R.0 catalogue entry does NOT say this. Source check:
`math-catalogue.md:266` R.0 says only that substrate admits both 2I
and A_5; 5-orbit claim is in WO-4 stub as anticipated, not derived.

R4-G2. **Phenotype-mode assignments too specific** at lines 253-267
and 274-295 — the paper matches specific morphologies (double-head,
electric face, etc.) to specific A_5 irreps WITHOUT any Laplacian
constructed or eigenmodes computed. This is assertion, not
conjecture.

R4-G3. **Xenopus attribution** at lines 335-337 — needs correcting.

R4-G4. **WO-6 miscitation** at line 372.

### WO-3 tubulin (round 1 verdict)

R3-G1. **D.1c + T.1 proof mathematically misaligned** at
biology-rung-tubulin.tex:182-185 and :205-213. The axiom D.1c
("indecomposability") and what T.1 actually uses are not the same
object. Codex says "the paper's main theorem is not soundly stated".

R3-G2. **T_MT upstream has evolved**. Per
`project_moduli_meta_layer.md`, the upstream refinement is
`T_meta = Z[φ]² as T_PH_1 refinement`. Our paper still cites the
older Tier-2 T_PH_1 form. Need to attribute correctly to the
refined T_meta object.

R3-G3. **T.2 abstract summary still oversells** at lines 52-59,
375-392, 412-414 — "confirm", "no falsifier known" etc. beyond
what the revised maths supports.

R3-G4. **Prota2014 bibliography** is about laulimalide/peloruside
A, not taxane-site pocket as described; the reference is being used
to support a claim it does not directly make.

### WO-2 amyloid derivation (round 2 verdict)

R2-G1. **D.3 scope contradiction** — Definition D.3 requires
`M·θ = 360°` exactly (integer M for full crossover), but the
physical interpretation allows crossover modulo the fibril's own
point-group symmetry (C_n for n-protofilament bundle). If the
fibril has C_2 symmetry, a crossover is at 180° not 360°. Need
either to justify why 360° exact is the right filter, or restate
D.3 honestly as a stronger-than-necessary modelling assumption.

R2-G2. **Stale ledger debris** partially cleaned (round 2 applied)
but need final sweep.

R2-G3. **WO-2 LaTeX paper** just distilled from derivation; not
yet codex-reviewed.

### WO-5 phyllotaxis (round 4 verdict)

R5-G1. **Prop 1 (three-distance) and Prop 2 (coxeter-vogel)
classical extremality claims** still stated too strongly at
biology-rung-phyllotaxis.tex:256-308. Need to either cite these
as classical theorems with proper number-theory references, or
prove them directly, not both half-assed.

R5-G2. **T1 summary still misaligned** at :318-364 and :576-581.
Codex wants conditional-placement language uniformly.

R5-G3. **WO-1 comparison at :159-161 and :591-595** — codex says
"the cited source says the opposite". Need to check what exactly
SmartCapsid claims and revise our citation.

## What the TASK asks codex-5.5 to do (read-only)

Treat the above G-labels as **gaps to close via named builds**.
For each, produce:

1. Is this gap closeable by a SIM (enumeration, computation,
   dataset check)? If yes, specify the object/domain/codomain of
   the sim and acceptance criteria.
2. Is it closeable by a DERIVATION (new proof, attribution fix,
   definition restatement)? If yes, specify the new mathematical
   object or claim required.
3. Is it closeable by a LITERATURE LOOKUP (correct citation,
   classical theorem import)? If yes, name the specific result
   and author.

Per the "no downgrades" rule: do NOT recommend softening any
existing claim. Every gap becomes a named build (B1, B2, …) with
a concrete first step. String-level replacements go in Section C.

## Specific sim targets (if you identify them)

- **B_orbits**: Enumerate the 2I action on the 600-cell's 600
  tetrahedral cells and count orbits exactly. If 5 orbits, R4-G1
  is sim-closed (the claim was right, just under-attributed).
  Uses: `papers/paper-xxxii/scripts/build_600cell.py` or existing
  600-cell builder.

- **B_tmeta**: Import the updated T_meta = Z[φ]² structure into
  WO-3, demonstrating that the 13-adjacency content survives.

- **B_crossover**: Enumerate fibril crossover angles modulo
  protofilament bundle symmetry (C_1, C_2, C_3, C_4), showing
  whether D.3's "exact 360°" filter is too tight.

- **B_cross_ref_wo1_wo5**: Check what `biology-rung-capsid.tex`
  actually says about cell-level biology and reconcile.

## After-closure next directions (SECTION G)

Once these gaps close, identify 3–5 additional field-aligned
and narrative-aligned domains where the cascade has a similar
sim-closable prediction. Candidates to evaluate:

- Bacterial flagellar motor 11-fold symmetry (C_11 selector?)
- Collagen triple-helix (3-strand at specific pitch)
- Centriole 9-fold symmetry
- Ribosomal small-subunit symmetry
- Chlorophyll / porphyrin 4-fold structure
- Cell cycle periodicity / circadian
- Others from your pretraining / insight.md

Rank by falsifiability + available data + narrative fit.

## Deliverable

`docs/codex-derive/TASK-close-remaining-gaps-<ts>.md` containing:

- SECTION A. Insight / upstream-content relevance (cite line
  numbers in `insight.md` / `cascade-bio.md` / `project_moduli_meta_layer.md`).
- SECTION B. Builds B1..Bn, each with type/domain/codomain and
  first step.
- SECTION C. String-level revert/apply instructions for the
  four tex files.
- SECTION D. Sim specifications (for B_orbits, B_tmeta,
  B_crossover, B_cross_ref_wo1_wo5 as appropriate).
- SECTION F. Top 3 builds ranked.
- SECTION G. Next field-aligned domains, ranked.

READ-ONLY. Do not edit files. Do not close or downgrade any
claim — name a build that would close it.

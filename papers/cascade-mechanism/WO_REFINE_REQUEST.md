# WO refinement task — integrate ARIA observer-process and Millennium alignment

**Goal.** The existing first-cut WO at `papers/cascade-mechanism/WO-CASCADE-MECHANISM.md`
(372 lines) was written against an older scope spec. Two **load-bearing**
sections from the augmented scope (`papers/cascade-mechanism/WO_SCOPE_REQUEST.md`,
528 lines) are missing from the WO and must be integrated:

1. **ARIA as observer-process implementation** (load-bearing new §6 in the
   eventual paper — currently the WO has §6 as the generic five-case-study
   table). See `WO_SCOPE_REQUEST.md` lines 285–391 (`## ARIA as
   observer-process (load-bearing §6 detail)`).

2. **Millennium-papers alignment scaffolding** (load-bearing new §8 in the
   eventual paper — currently the WO has §8 as Discussion/Conclusion). See
   `WO_SCOPE_REQUEST.md` lines 393–510 (`## Millennium-papers alignment
   scaffolding (load-bearing §8 detail)`).

Your task is to refine `WO-CASCADE-MECHANISM.md` in place so that:

- The recommended paper structure becomes a **9-section** plan (not 8):
  - §1 Motivation: beyond collapse language
  - §2 Core mechanism: instability, cascade, crystallisation
  - §3 Rung model and residual propagation
  - §4 Geometry identification across rungs (the rung table)
  - §5 Visible vs non-visible projection
  - **§6 ARIA as observer-process implementation (NEW load-bearing)**
  - §7 Case studies (renumbered from old §6)
  - **§8 Millennium-papers alignment scaffolding (NEW load-bearing)**
  - §9 Discussion and conclusion (renumbered from old §8)

- The §6 spec block in the refined WO must reproduce the entire
  observer-process architecture from `WO_SCOPE_REQUEST.md` §285–391:
  the `O = <B, S, M, G, I, C, A>` tuple with the per-component table,
  the cascade processing descent (field potential → ... → replay /
  provenance), the seven-step observer loop, the two-telemetry-layer
  bio/synthetic mapping table, the cascade-layers diagram requirement
  (one figure), the verbatim claim boundary paragraph, and the §6 must-not
  list. The WO must also list which ARIA runtime modules
  (`lyapunov_selector.py`, `self_model_stream.py`,
  `consciousness_binding.py`, `vfd_closure_kernel.py`,
  `sigma_orbit_basis.py`, `v66_e8_coxeter.py`, plus the
  `SystemTickCoordinator`-style integrator and polytope memory /
  invariant store referenced in `docs/aria-closure-kernel.md`)
  realise which `O` component. **You must audit the actual ARIA repo paths
  and confirm which files / classes implement each `O` component before
  writing the mapping into the WO.** If you cannot locate a module in the
  repo state, mark that row as "module name reserved; runtime location to
  be confirmed during .tex build" rather than guessing a path.

- The §8 spec block in the refined WO must reproduce the entire
  Millennium-alignment scaffolding from `WO_SCOPE_REQUEST.md` §393–510:
  the framework-level `H_{Mill-Proj}` hypothesis, the seven-Millennium
  projection table, the "give the game away" requirement (a–d), the
  honest-verdict-scope discipline (δ / γ / β / coherence per
  `project_millennium_scope_pass`), the drop-order coordination, and
  the cite-only-do-not-derive discipline. **You must audit the actual
  in-repo state of each Millennium paper at WO time** and add a column
  to the seven-Millennium table stating *what fraction of each
  Millennium paper's reduction is unconditional vs conditional on which
  named hypothesis* (per the user's explicit requirement at
  `WO_SCOPE_REQUEST.md` §437–439). Use `grep -rn "Hypothesis\|H_{" papers/millennium-*`
  or similar to verify named hypotheses actually exist with those names
  in the corresponding `.tex` sources.

- §9 (renumbered Discussion / conclusion) absorbs whatever was in the
  old §8 conclusion content from the first-cut WO.

- The dependency tables in §3 of the WO must be extended to include the
  ARIA runtime module file paths (after audit) and the Millennium paper
  file paths and current line counts (use `wc -l`).

- The acceptance criteria, risk register, and effort phasing must be
  updated to reflect the two new sections. Specifically:
  - Acceptance criteria must add: "§6 includes the cascade-layers
    diagram, the bio/synthetic telemetry table, and the verbatim
    observer-process claim boundary"; "§8 includes the seven-Millennium
    projection table with per-row conditional/unconditional fractions
    and named hypotheses, and reproduces honest verdict scopes without
    upgrade".
  - Risk register must add: "treating ARIA as proof of consciousness
    (mitigation: §6 verbatim boundary)"; "upgrading Millennium verdict
    scopes (mitigation: §8 cite-only discipline + memory cross-check)".
  - Effort phasing must insert §6 (3–5 days) and §8 (3–5 days) before
    the build/review loop step.
  - Page estimate must increase to 60–100 pages to reflect the two
    additional load-bearing sections (per the user's explicit guidance
    in the most recent message: "this may be a big paper but needed and
    important").

- The "Why this paper matters" closing must be updated to reflect that
  the paper is **also** the Millennium-drop framework-positioning paper,
  not just the consolidation paper.

**Constraints.**

- Do NOT delete the existing §1–§8 content of the WO; refine and renumber.
- Do NOT change the mechanism-statement triad (Instability → Cascade →
  Crystallisation); it stands.
- Preserve all existing audited dependencies in §3.
- Do NOT mark the WO itself "publication ready" or "complete" — that's
  the user's call.
- Do NOT touch git state.
- Use markdown tables, not LaTeX, in the WO (the WO is markdown, not
  the eventual paper).
- The refined WO will be ~500–700 lines. That's fine.

**Reference documents (READ FULLY).**

- `papers/cascade-mechanism/WO_SCOPE_REQUEST.md` (528 lines — the augmented
  scope spec; the source of truth for the new §6 and §8 content)
- `papers/cascade-mechanism/WO-CASCADE-MECHANISM.md` (372 lines — the
  first-cut WO to refine in place)
- `~/.claude/projects/-mnt-c-Users-nexus-OneDrive-Documents-My-Projects-vfd-crystalisation-paper/memory/project_millennium_scope_pass.md`
  (verdict scopes — do not upgrade them in §8)
- `docs/aria-closure-kernel.md` (operator + module references)
- `papers/aria-chess-paper/aria-chess-paper.tex` and
  `papers/aria-closure-kernel/paper/main.tex` (case-study substrate)
- `papers/millennium-rh-formal/rh-formal.tex`,
  `papers/millennium-ym/`,
  `papers/millennium-bsd-formal/bsd-formal.tex`,
  `papers/millennium-ns-formal/ns-formal.tex`,
  `papers/millennium-pnp-formal/pnp-formal.tex`,
  `papers/millennium-poincare-formal/poincare-formal.tex`,
  `papers/millennium-hodge-formal/hodge-formal.tex`
  (audit per-paper state for the §8 table)

**Acceptance for this refinement task.**

- `WO-CASCADE-MECHANISM.md` is rewritten in place with the 9-section
  paper-structure layout above.
- The new §6 spec block in the WO is fully present (architecture tuple
  + telemetry table + diagram requirement + claim boundary).
- The new §8 spec block in the WO is fully present (H_{Mill-Proj} +
  seven-Millennium table with audited fractions + drop-order +
  verdict-scope discipline).
- §3 audited dependencies extended with ARIA runtime modules and the
  Millennium papers (with current line counts).
- Acceptance criteria, risk register, effort phasing, and page estimate
  updated as above.
- Stdout summary lists: files edited, files created, key decisions,
  residual uncertainty, open sub-questions.

Direct voice. No padding.

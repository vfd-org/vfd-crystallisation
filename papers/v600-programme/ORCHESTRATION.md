# V_600 Programme — Build Orchestration Plan

**Goal:** Ship Papers 1–5 as a coherent, release-ready repo. Each paper goes through the same codex-paired build loop. Claude (this session) builds and orchestrates; codex generates work orders and runs reviews.

## Repo layout (release-ready)

```
papers/v600-programme/
├── NARRATIVE.md              ← master arc (done)
├── NOTATION.tex              ← shared symbols (done)
├── ORCHESTRATION.md          ← this file
├── RELEASE.md                ← release checklist + version manifest
├── references-shared.bib     ← shared citations across all five papers
├── lib/                      ← shared computation
│   └── vfd_v600/             ← Python package, hot path for verification
│       ├── __init__.py
│       ├── icosian.py        ← exact icosian arithmetic (vendored from paper-xxii)
│       ├── group.py          ← V_600 vertex/cycle/coset construction
│       ├── sigma.py          ← σ-Galois twist + 24-cell
│       ├── tau_sigma.py      ← τ_σ involution loader
│       └── operators.py      ← K-class projectors, trace formalism
├── tests/                    ← shared test suite (pytest)
│   ├── test_v600_construction.py
│   ├── test_dic5_subgroup.py
│   ├── test_24cell_incidence.py
│   ├── test_tau_sigma.py
│   └── test_operator_traces.py
└── data/
    └── tau_sigma_canonical.txt    ← canonical 120-vertex map

papers/bekenstein-incidence/        ← Paper 1
papers/v600-hawking-quantum/        ← Paper 2
papers/tau-sigma-construction/      ← Paper 3
papers/v600-cosmic-tensions/        ← Paper 4
papers/v600-unified/                ← Paper 5

Each paper directory contains:
├── SCOPE.md                  ← one-shot scope (already drafted for all 5)
├── WO.md                     ← work order (codex-generated)
├── <paper-slug>.tex          ← LaTeX manuscript (Claude builds)
├── references.bib            ← paper-specific cites + \input shared
├── verify.py                 ← single-file verification driver
└── reviews/                  ← codex review history per round
```

## The build loop (per paper)

For each Paper N ∈ {1, 2, 3, 4, 5}, in sequence:

```
[Step 1] Claude → codex_derive.sh     (generate WO from SCOPE.md)
   ↓
[Step 2] Codex returns WO.md          (sections, theorems, sims, acceptance criteria)
   ↓
[Step 3] Claude → write LaTeX + verify.py  (implement WO)
   ↓
[Step 4] Claude → review_wo.sh        (codex hostile-review the artifact)
   ↓
[Step 5] Codex returns review         (verdict: ready / not-ready)
   ↓
[Step 6] If not-ready: Claude fixes named issues, GOTO Step 4
         If ready:    move to Paper N+1
```

Loop count target per paper: **3-6 review rounds** (matches existing programme history — see paper-xxxvi etc.).

## Sequencing

The five papers share infrastructure (NOTATION.tex, vfd_v600 package, tests, shared.bib), so we build the infrastructure FIRST, then papers:

```
Phase 0: Infrastructure (one-time)
  0.1  Vendor exact-icosian module from paper-xxii into lib/vfd_v600/
  0.2  Build group.py, sigma.py, tau_sigma.py, operators.py
  0.3  Build pytest suite covering all V_600 facts used across papers
  0.4  Migrate canonical τ_σ map to data/
  0.5  Build references-shared.bib from existing programme cites

Phase 1: Paper 1 (Bekenstein 1/4)
  1.1  Codex generates WO from SCOPE.md
  1.2  Claude writes paper-1 LaTeX + verify.py
  1.3  Codex review round 1 → fixes
  1.4  Codex review round 2 → fixes
  1.5  Iterate until "Publication ready: yes"
  1.6  Final consistency check against shared lib

Phase 2: Paper 2 (Hawking quantum) — same loop
Phase 3: Paper 3 (τ_σ construction) — same loop
Phase 4: Paper 4 (cosmic tensions) — same loop
Phase 5: Paper 5 (unified synthesis) — same loop

Phase 6: Release
  6.1  Cross-paper consistency audit (codex)
  6.2  Build all PDFs from a single make target
  6.3  Tag git release v600-programme-v1.0
  6.4  Generate RELEASE.md manifest with arXiv-ready bundle
```

## Reviewer discipline

Codex review rounds use `scripts/review_wo.sh` with paper-specific focus strings. Per `feedback_codex_review_workflow.md`:

- Pipe via `< /dev/null` to keep STDIN clean.
- Use `--focus "round N: <specific concern>"` to drive each round.
- "Drift patterns to watch for": codex sometimes downgrades claims when it should name a missing build. Don't accept downgrades — convert to named build.

## Build-loop guardrails

These come from existing programme experience and apply to every paper:

1. **No claim moves without a verification script.** If a paper says "we prove X", `verify.py` must compute X. If X isn't computable (pure proof), state explicitly.
2. **Catalogue discipline.** Each paper has a math catalogue (D/L/T/C/N entries) that round 1 establishes; later rounds keep it in sync.
3. **Scope gates.** If codex review proposes adding scope, *reject by default* — only add if a named missing piece can't fit anywhere else.
4. **No back-citations.** Paper N never cites Paper N+k. Enforced by build order.
5. **Honest verdicts.** "Publication ready: yes" requires no must-fix items; tone, polish, and surface latex issues do not gate.

## Release deliverable (Phase 6)

Final shape:

```
v600-programme-v1.0.tar.gz
├── README.md                 ← top-level pitch + how to read the set
├── RELEASE.md                ← version manifest
├── LICENSE
├── NARRATIVE.md
├── NOTATION.tex
├── lib/vfd_v600/             ← Python package
├── tests/                    ← pytest suite (must pass)
├── papers/
│   ├── 01-bekenstein-incidence/
│   ├── 02-v600-hawking-quantum/
│   ├── 03-tau-sigma-construction/
│   ├── 04-v600-cosmic-tensions/
│   └── 05-v600-unified/
│       (each contains: scope.md, wo.md, paper.tex, paper.pdf, references.bib, verify.py)
└── arxiv/                    ← arXiv-ready tarballs per paper
    ├── paper-01.tar.gz
    ├── paper-02.tar.gz
    ├── paper-03.tar.gz
    ├── paper-04.tar.gz
    └── paper-05.tar.gz
```

A single `make all` builds every PDF, runs every test, and produces the arxiv tarballs.

## Tracking

Each paper's progress lives in TaskList (#36–#40 forthcoming). Each WO round, each review round, each fix cycle gets its own task.

## Owner

Claude (this session) orchestrates and implements. Codex generates WOs and reviews. User confirms milestone gates (scope-frozen, ready-to-ship, ready-to-release).

# VFD Crystallisation — Paper Architecture and Publication Plan

This document describes how the crystallisation framework is organised for presentation, review, and testing.

The materials in this repository are intended to present a testable framework; they do not assume correctness of the model and are structured to enable independent evaluation.

## Structure: 1 + 4

This research programme is presented as **one flagship paper** supported by **four companion papers** and a **supplementary layer**. This is not a collection of independent publications — it is one coherent narrative with structured depth.

---

## Flagship Paper

**"Crystallisation Dynamics as a Deterministic Alternative to Collapse in Open Quantum Systems"**
`papers/main-preprint/crystallisation-dynamics.tex`

- **Role**: The primary outward-facing paper. This is what people read first.
- **Content**: Introduction, operator definition, quantum-compatible formulation, simulation results (4 figures), condensed signatures, falsification criteria, discussion.
- **Audience**: Physicists in foundations/quantum info/collapse models. Readable in ~15 minutes.
- **Claim level**: Testable dynamical extension, not a replacement for QM.
- **Status**: Prepared for review.

---

## Companion Paper A — Formalism

**"The Crystallisation Operator: Mathematical Structure and Properties"**
`papers/formalism/crystallisation-formalism.tex`

- **Role**: Full mathematical depth. Pure structure, no narrative.
- **Content**: Formal operator definition, four theorems with proof sketches, spectral formulation, Hessian analysis, dynamical flow, crystallisation timescale.
- **Audience**: Mathematical physicists wanting the rigorous foundation.
- **Claim level**: Mathematical properties of the operator (existence, stability, descent, mode selection).
- **Status**: Prepared for review.

---

## Companion Paper B — Experimental

**"Experimental Signatures, Parameter Estimation, and Benchmark Comparison of the Crystallisation Operator"**
`papers/experimental/crystallisation-experimental.tex`

- **Role**: The "can we test this?" paper. Provides falsifiability, parameter estimation, and benchmarking in one coherent companion.
- **Content**: Competing models, signature taxonomy (SGT-1 through SGT-6), experimental platforms (EP1-EP5), parameter estimation framework, identifiability/sensitivity, benchmark results, falsification criteria (F1-F5).
- **Audience**: Experimentalists, reviewers, and critics evaluating testability.
- **Claim level**: Framework for empirical discrimination. No claims of validation.
- **Narrative arc**: signatures -> measurement -> comparison -> falsification
- **Status**: Prepared for review.

---

## Companion Paper C — Inevitability

**"Constraint-Driven Selection as an Emergent Principle in Dynamical Systems"**
`papers/inevitability/constraint-driven-selection.tex`

- **Role**: Shows that the crystallisation functional is not arbitrary but arises naturally from minimal structural requirements for selection in constrained dynamical systems.
- **Content**: Problem statement, minimal requirements (R, E, Q), emergence of the selection functional, inevitability of attractors, deterministic vs stochastic selection, connection to the crystallisation framework, limitations.
- **Audience**: Dynamical systems researchers and physicists evaluating whether the framework has structural justification beyond being a proposal.
- **Claim level**: Structural naturalness, not physical derivation. The functional form is shown to be minimal given stated assumptions; no claim of fundamental law.
- **Status**: Prepared for review.

---

## Companion Paper D — Mechanism + Demonstration

**"Crystallisation as a Selection Mechanism: Triplet Closure, Regime Structure, and a Deterministic Demonstration"**
`papers/mechanism/crystallisation-mechanism.tex`

- **Role**: Formalises the triplet closure result and demonstrates the mechanism in a concrete system. Makes three logically independent contributions: structural (triplet closure), phenomenological (regime structure), and demonstrative (ARIA proof pack).
- **Content**: Constraint space formalism, crystallisation mechanism, triplet closure (three constraint classes sufficient, two not), regime structure (Delta = lambda/Gamma), observable consequences, ARIA governed reasoning demonstration with cryptographic proof pack, limitations.
- **Audience**: Researchers evaluating the mechanism's structural grounding and wanting to see it operate in a verifiable system.
- **Claim level**: Structural mechanism + phenomenological conjecture + concrete demonstration. Claims are explicitly separated and should be evaluated independently.
- **Status**: Prepared for review.

---

## Supplementary Layer

`papers/supplementary/`

Not standalone papers. Reference material:

| Resource | Content |
|----------|---------|
| `prediction-registry.tex` | 10 structured predictions with per-model expectations |
| `parameter-registry.md` | Full 9-parameter specification with units/ranges/proxies |
| `platform-mapping/*.md` | 5 platform-specific experimental guides |
| `signatures.md` | 5 experiment class protocols |

---

## Publication Order

1. **Flagship first** — main preprint on arXiv + website + GitHub
2. **Experimental second** — shows testability and falsifiability
3. **Inevitability third** — shows the functional form is structurally natural
4. **Mechanism fourth** — triplet closure + ARIA demonstration
5. **Formalism fifth** — for readers wanting full mathematical depth

Supplementary published alongside as downloadable references.

---

## X (Twitter) Strategy

Do NOT post 3 separate papers. Instead:

**One main post** with the flagship paper:
- Core idea in 2 sentences
- Key figure (Fig 3 or Fig 4)
- Link to GitHub repo
- Mention companion papers exist for depth

**Thread** (optional):
- What the operator does
- How it differs from decoherence/GRW/OR
- What would falsify it
- Link to experimental companion

---

## Review Order

1. Review main preprint ONLY
2. Review experimental companion
3. Review formalism companion
4. Review supplementary

---

## Release Tags

| Tag | Content |
|-----|---------|
| `v0.1-internal` | Internal review of main preprint |
| `v0.2-cleaned` | Main preprint + experimental companion public |
| `v1.0-public` | Full programme: all papers + supplementary |

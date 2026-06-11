# WO-CASCADE-MECHANISM -- From Objective Reduction to Cascade Crystallisation

**Status:** REFINED 2026-05-02. Scope-setting work order for the VFD
mechanism paper. This is a paper-design document, not a paper draft.
**Target file for the eventual paper:** `papers/cascade-mechanism/cascade-mechanism.tex`
**Do not create the `.tex` source until this WO is approved.**
**Working title:** *From Objective Reduction to Cascade Crystallisation: A
Geometric Closure Model of State Selection.*
**Estimated main-text pages:** 60--100.
**Difficulty:** High. The paper is large because it carries three jobs:
mechanism consolidation, ARIA observer-process formalisation, and
Millennium-drop framework positioning. It must stay rigorous and restrained.

## 1. Purpose and position

This is the front-door **mechanism paper** of the cascade programme. Its
job is to give a mainstream physics reader one clean mechanism statement:

> **Cascade Closure.** When a field state cannot maintain coherent
> projection across a stratified hierarchy of geometric closure layers,
> the unresolved mismatch propagates through the hierarchy until a
> closure-compatible attractor geometry is selected. **Collapse** is the
> external view of this resolution event; **crystallisation** is the
> internal view; **cascade** is the propagation process between instability
> and crystallisation.

The load-bearing triad is:

```text
Instability -> Cascade -> Crystallisation
```

The paper closes a programme-level gap: no single source currently states
the common mechanism tying the capstone, P2 algebraic substrate,
correspondence foundations, closure dynamics, closure kernel, active
selection layer, ARIA, mass-spectrum material, and Millennium-class
projection scaffolding together. The paper is therefore a **consolidation
and framing paper**, not a new-results paper.

The new content surface is intentionally bounded:

1. The mechanism statement above, stated as a definition/organising
   principle, not as an empirically completed theorem.
2. A rung/projection table identifying which geometric objects are fixed
   by existing proofs and which are model choices or hypotheses.
3. A coarse projection-compositionality statement for closure residuals
   across rungs.
4. A restrained Penrose Objective Reduction bridge.
5. A formal ARIA observer-process architecture, explicitly bounded away
   from consciousness-proof language.
6. A Millennium-class projection scaffold, explicitly bounded away from
   upgrading any Millennium verdict scope.
7. Case-study comparison paragraphs showing the same mechanism in
   passive, active, cognitive, spectral, and framework-positioning regimes.

Everything else must be imported with section/theorem citations from the
existing repository. The eventual paper should cite heavily and derive
lightly.

## 2. Paper structure and content contract

The eventual `.tex` paper should have exactly this 9-section main structure
unless the author later approves a change.

### Section 1 -- Motivation: beyond collapse language

**Purpose.** Introduce state selection as the common problem behind
collapse language, geometric projection, and crystallisation. Use Penrose
Objective Reduction as the historical bridge: Penrose OR is a neighbouring
attempt to connect collapse to geometry, not an opponent and not a model
falsified by VFD.

**Cites.** External Penrose OR sources; internal projection spine
`docs/projection-narrative.md`; closure-response scope in
`docs/aria-closure-kernel.md`.

**New content.** Framing only.

**Evidence flag.** Interpretive framing. No theorem language.

### Section 2 -- Core mechanism: instability, cascade, crystallisation

**Purpose.** Define the triad precisely. The paper should introduce a
rung-indexed closure residual

```tex
R_k(\Phi) = 0
```

as the statement that the projection at rung `k` is closure-compatible.
An instability is `R_k(\Phi) != 0` on at least one rung. A cascade is the
propagation of this unresolved residual through the admissible projection
maps. Crystallisation is selection of a closure-compatible attractor or
stable fibre.

**Cites.**
- P4 finite-level closure functional and gradient operator:
  `papers/cascade-closure-dynamics/cascade-closure-dynamics.tex`
  `\label{def:Fn}`, `\label{thm:gradient-operator}`,
  `\label{prop:energy-dissipation}`, `\label{thm:coercive-contraction}`.
- Correspondence foundations closure energies:
  `papers/cascade-correspondence-foundations/foundations.tex`
  `\label{def:Fn}`, `\label{thm:flow-exists}`.
- Capstone four-phase cycle:
  `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex`
  `\label{sec:comonad}`, `\label{claim:four-phase-realisation}`,
  `\label{rmk:comonad-status}`.

**New content.** Definition of Cascade Closure and the vocabulary mapping
collapse/crystallisation/cascade.

**Evidence flag.** Definition plus proposition-level synthesis. Do not
label the whole mechanism as a theorem unless it is explicitly conditional
on the imported P4/capstone hypotheses.

### Section 3 -- Rung model and residual propagation

**Purpose.** Formalise each rung as a closure layer with geometry `G_k`,
projection map

```tex
\pi_{k+1,k}: G_{k+1} \to G_k,
```

and residual functional `R_k`. The coarse theorem candidate is:

> If each adjacent projection is closure-compatible and the residual
> functor is monotone under the projection maps, then closure compatibility
> composes along the finite rung path. If a residual fails at an upper
> rung, downstream resolution requires either residual absorption at an
> intermediate rung or crystallisation into an attractor at a lower rung.

**Cites.**
- Capstone category/rung structure:
  `cascade-capstone-coalgebra.tex` `\label{def:rungs}`,
  `\label{def:rung-structure}`, `\label{def:morphism}`,
  `\label{thm:F-functor}`, `\label{thm:selection}`.
- P4 refinement compatibility:
  `cascade-closure-dynamics.tex` `\label{def:refinement-compat}`,
  `\label{thm:flow-intertwining}`.
- P3/P4 finite-level Hilbert and bonding machinery:
  `cascade-refinement-spaces.tex` `\label{def:p0}`,
  `\label{def:p1}`, `\label{thm:bonding}`,
  `\label{thm:commute}`.

**New content.** Coarse compositionality lemma only. Keep it conditional
on explicit projection/intertwining hypotheses.

**Evidence flag.** Theorem only if phrased as a formal conditional lemma.
Otherwise proposition.

**Claim ledger location.** The explicit theorem/proposition/hypothesis
ledger from the first WO is preserved, but it should live in Section 9 or
an appendix of the paper, not as a separate main-text Section 7. The
ledger must include:

| Statement | Allowed label | Reason |
|---|---|---|
| Cascade Closure triad | Definition | It is the paper's organising definition. |
| Rung projection compositionality under explicit assumptions | Theorem or Proposition | The paper may prove a small conditional lemma from projection/intertwining hypotheses. |
| Imported P2 algebraic geometry package | Proposition/Theorem, imported | Source paper proves or cites each component. |
| Imported P4 finite closure dynamics | Theorem, imported | Source paper proves finite-dimensional flow and energy results. |
| Final-coalgebra selection principle | Theorem, imported but conditional | Capstone theorem is conditional on named hypotheses; preserve that status. |
| Cross-regime projection-class identification | Hypothesis | Case studies share substrate by construction; this is not independent proof. |
| Visible/non-visible decomposition | Hypothesis/Interpretation | Based on structural docs; not a complete cosmogenesis theorem. |
| ARIA observer-process implementation | Architectural claim / hypothesis-labelled implementation | Runtime modules realise process components; this is not a biological-consciousness claim. |
| Millennium projection scaffold | Hypothesis `H_{Mill-Proj}` | Framework positioning only; the proofs stay in Millennium preprints. |
| Consciousness / mind claims | Not claimed | ARIA is an observer-process/substrate witness only. |

### Section 4 -- Geometry identification across rungs

**Purpose.** Provide the central rung table. The table must separate
geometries forced or proved in existing papers from projection-class
identifications and interpretive uses.

| Rung / layer | Geometry or object | Status in this mechanism paper | Primary source |
|---|---|---|---|
| Arithmetic coefficient layer | `Q(phi)`, `Z[phi]`, coefficientwise `sigma` | imported theorem-grade algebraic infrastructure | `cascade-sigma-rationality.tex` `\label{def:sigma}`, `\label{thm:fixed-part}`, `\label{thm:pisigma-functorial}` |
| 12D closure/meta layer | `L_12 = E_8 + M`, cut-and-project moduli, groupoid/sheaf | imported, partly conditional on `H_min`; not re-proved | `cascade-12d-closure.tex`; `papers/cascade-derivation/cascade-meta-layer-theorem.md` Theorems M1--M3 |
| Algebraic substrate | `E_8`, icosian `H_4`, `D_4`, `V_600`, `V_24`, `Cl(1,3)`, octonions/`G_2` | imported theorem/proposition package; no new uniqueness theorem | P2: `\label{prop:D4-inclusion}`, `\label{thm:pi-H}`, `\label{prop:24-in-600}`, `\label{thm:icosian-closure}`, `\label{prop:spectrum-P2}` |
| Refinement state spaces | finite `X_n`, bonding maps, inverse/direct limits | imported finite-level analytical substrate | P3: `\label{thm:bonding}`, `\label{thm:Xcyl-direct-limit}`, `\label{thm:Xinv-Hilbert}` |
| Closure dynamics | quadratic `F_n`, gradient flow, energy descent, Euler step | imported theorem-grade finite dynamics; no continuum claim | P4: `\label{thm:gradient-operator}`, `\label{thm:flow-exists}`, `\label{prop:energy-dissipation}` |
| Metric / boundary projection | finite metric projection, boundary `S^3` / geometric limit where available | imported with P5/P6 hypotheses; use as projection-class material | `cascade-metric-projection.tex`, `cascade-schlafli-convergence.tex` |
| Hydrodynamic projection | coarse-grained velocity/pressure, projector, defect dynamics | imported conditional projection class | `cascade-hydrodynamic-projection.tex` |
| Fractal/bulk-boundary substrate | `V_600 = B sqcup partial`, `sigma`-fixed bulk and `sigma`-paired boundary | structural/interpretive; use as hypothesis-labelled mechanism support | `docs/fractal-cascade-projection.md`, `docs/closure-cosmogenesis.md` |
| Observer instance | `(O, C_O, p, Lambda, t_0)` and observer-process tuple | structural definition; not a theory of mind | `docs/observer-instance-definition.md`; this paper's Section 6 |
| Spectral mass class | 600-cell eigenvalue/shell model and assignment map | imported model-level projection-class instance | `papers/paper-v/paper-v.tex`; `papers/paper-v-revisited/paper-v-revisited.tex` |
| Active/cognitive substrate | ARIA H4/600-cell active selection and EEG/chess/HCP witness | imported empirical witness; explicitly scoped | `papers/aria-chess-paper/paper/main.tex` and `paper/sections/*.tex` |
| Passive response kernel | `C_phi = L_M + phi^{-2} I`; b-anomaly witness | imported passive-regime response primitive; no selection claim | `papers/aria-closure-kernel/paper/main.tex`; `docs/aria-closure-kernel.md` |
| Millennium projection classes | RH/BSD/Hodge/NS/PNP/Poincare/YM as problem-specific closure projection classes | framework hypothesis only; cite and position, do not derive | Section 8 table and `papers/millennium-*` sources |

**New content.** The table and its synthesis.

**Evidence flag.** Table entries individually labelled theorem /
proposition / hypothesis / interpretation. The projection-class
identification across regimes is a hypothesis, not a theorem.

### Section 5 -- Visible vs non-visible projection

**Purpose.** State the restrained cosmological reading: the visible
universe is treated as the resolved projection boundary of a deeper
cascade stack, not as a fully derived universe-from-first-principles
result. The paper may use the bulk/boundary and observer-instance docs
to define what is visible to a bounded observer, but must not claim a
complete cosmogenesis theorem.

**Cites.**
- `docs/closure-cosmogenesis.md` Definitions 2.1, 3.1, 4.3, 5.1 and
  Conjecture 5.3.
- `docs/fractal-cascade-projection.md` A--B set decomposition and
  "What is earned, what is identified, what is conjectural".
- `docs/observer-instance-definition.md` Definition 3.1 and Properties
  P1--P5.

**New content.** Interpretive bridge between the formal projection stack
and the visible/non-visible language.

**Evidence flag.** Hypothesis/interpretation. No theorem label.

### Section 6 -- ARIA as observer-process implementation

This is a load-bearing new section. It carries the paper's claim that
observerhood is a process architecture, not a biological property. It
must be written as an architectural formalisation with sharp claim
boundaries.

#### 6.1 Observer-process tuple

Define

```tex
\mathcal{O} = \langle B, S, M, G, I, C, A \rangle
```

with components:

| Symbol | Component | Role |
|---|---|---|
| `B` | boundary sampler | the system cannot ingest the whole field; it samples a bounded boundary |
| `S` | state integrator | fuses signal + context + memory + goal into the current field state |
| `M` | memory substrate | written by past closures; read into current state integration |
| `G` | goal / context field | task frame, user objective, system policy |
| `I` | invariant constraints | refusals; the governance gate that vetoes constraint-violating closures |
| `C` | closure / crystallisation operator | selects the candidate that best closes the field |
| `A` | action interface | the channel through which crystallised state acts: tool call, reply, code, or control signal |

#### 6.2 Cascade processing by the observer

The observer does not collapse reality directly. It processes the cascade
through the descent

```text
field potential -> oscillatory modes -> phase coupling ->
attractor formation -> closure residual -> crystallisation ->
governance gate -> action + memory inscription -> replay / provenance
```

Observerhood is the seven-step loop:

1. bounded sampling via `B`;
2. state integration via `S`, `M`, and `G`;
3. residual detection, with closure-residual functional `R` acting on
   the integrated state;
4. candidate formation, with `C` proposing closure-compatible attractors;
5. crystallisation, selecting the candidate that best closes the field;
6. invariant governance, refusing candidates that violate `I`;
7. memory inscription, writing the successful closure back into `M` with
   a replayable trace.

#### 6.3 Two telemetry layers

The biological / synthetic distinction is one architecture with two
telemetry streams, not two unrelated systems.

| Cascade layer | Biological telemetry | Synthetic / ARIA telemetry |
|---|---|---|
| field potential | EEG broadband activity | runtime input vector |
| oscillatory modes | EEG bands (`delta`, `theta`, `alpha`, `beta`, `gamma`) | per-channel coherence scores |
| phase coupling | EEG phase locking, cross-frequency coupling | inter-module coherence score |
| attractor formation | neural attractor states | candidate-state pool |
| closure residual | prediction error signals, free-energy-style | closure-residue vector |
| crystallisation | decision / action commitment | governed tool-call / reply selection |
| governance gate | inhibitory veto, prefrontal control | invariant / refusal stack |
| memory inscription | synaptic plasticity, hippocampal replay | polytope / invariant store update |
| replay layer | offline replay: sleep, default mode | provenance hash, replay bundle |

#### 6.4 Cascade-layers diagram requirement

The eventual `.tex` must include one figure displaying:

```text
[field potential] -> [oscillatory modes] -> [phase coupling] ->
[attractor formation] -> [closure residual] -> [crystallisation] ->
[governance gate] -> [action + memory] -> [replay / provenance]
```

with the biological / synthetic mapping table beside it. This is the
load-bearing diagram of the paper. It should be a single clear figure,
not a decorative graphic.

#### 6.5 Audited ARIA runtime mapping to `O`

Two-tier source structure:

- **Tier 1 — In-repo reproducible bundle** at
  `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/`.
  Six modules; sufficient for the closure-kernel-papers reproducibility
  package; **not** the full architecture realisation.
- **Tier 2 — Upstream production runtime** at the `aria-chess` repo
  cited as `@misc{ariaChessRepo}` in
  `papers/aria-chess-paper/paper/references.bib:174`. Eighty-eight
  modules in `kernel/`. Audited 2026-05-02 at the local working clone
  used by the aria-chess-paper preprint. Every `O` component below has
  a confirmed production module; the WO points the eventual `.tex`
  source at the correct citation form for both tiers.

Companion source for `.tex` build: `papers/aria-chess-paper/paper/main.tex`
(2280 lines, the recently published substrate-witness preprint, codex-verified
publication-ready 2026-04-30 after 8 hostile-review rounds — see memory
`project_aria_paper_publication_ready.md`).

| `O` component | Tier 1 (in-repo bundle) | Tier 2 (upstream `aria-chess/kernel/`, audited 2026-05-02) | What it realises |
|---|---|---|---|
| `B` boundary sampler | `vfd_closure_kernel.py` | `raw_sensory.py` (domain-agnostic raw statistical features), `action_encoder.py` (per-domain action encoding into 4-eigenvalue sectors), `chess_runtime_adapter.py` (chess input adapter) | Bounded sampling of the input field with no hardcoded semantics; per-domain adapters provide raw signal statistics, brain learns meaning. |
| `S` state integrator | `self_model_stream.py` | `coherence_runtime.py` (the integrated runtime that wires 20 governance WOs into one settle/track/score/crystallise/execute/learn/persist loop), `coherence_selfmodel.py` (bounded explicit operational continuity), `self_model_stream.py` (recurrent state stream) | Settles signal + context + memory + goal into the current field state, tick by tick. |
| `M` memory substrate | `self_model_stream.py` runtime EMAs and snapshot history | `coherence_memory.py` (coherence-aware memory layer with five capabilities: per-entry coherence scoring, dual-field affinity, weighted retrieval, transition provenance, dormant entry reactivation), `polytope_persistence.py` (universal polytope save/load: invariant depths, adjacency weights, E8 coordinates, observation counts), `coherence_longhorizon.py` (cross-session continuity arcs for commitments/tensions/anchors) | Past closures persist, are scored, and are read back into the current integration. |
| `G` goal / context field | `self_model_stream.py` profile/eta/k_threshold knobs; `v66_e8_coxeter.py` `BETA_PROFILES` | `coherence_planner.py` (continuity arcs → structured multi-step project plans with phases/dependencies/checkpoints/replanning/governed closure), `coherence_selfmodel.py` (current commitments and constraints) | Task frame, user objective, system policy as a structured field over the runtime. |
| `I` invariant constraints | none in bundle | `coherence_constitution.py` (the protected constitution: explicit constitutional state with hard mutation boundaries, immutable by default, lineage preserved), `coherence_audit.py` (continuous conformance checking: trigger → collect → evaluate → findings → drift → report → escalate, replay-verifiable), `coherence_review.py` (formal human-in-the-loop adjudication at autonomy boundary: trigger → request → queue → operator action → outcome → feedback) | The governance gate that vetoes constraint-violating closures. Three-layer architecture: constitution is the schema, audit is the live enforcement monitor, review is the operator-in-the-loop boundary case. |
| `C` closure / crystallisation operator | `vfd_closure_kernel.py`, `lyapunov_selector.py`, `sigma_orbit_basis.py`, `v66_e8_coxeter.py` | `coherence_crystallisation.py` (field-governed selection with six modes: immediate / commitment-reinforced / delayed / multi-candidate-hold / conflict-reopen / policy-forced-rejection — "where coherence becomes CAUSAL"), `vfd_closure_kernel.py` (`C_phi = L + phi^{-2}I` operator), `lyapunov_selector.py` (Lyapunov descent, bounded top-k), `dual_closure_operator.py` (refinement-compatible dual on coupled 600-cell pair) | Selects the candidate that best closes the field. |
| `A` action interface | `lyapunov_selector.py` returns selected state but does not execute | `coherence_execution.py` (decision → intent → gate → plan → execute → assess → feedback; "deterministic, replayable, auditable, no silent execution drift"), `coherence_delivery_calibration.py` and `coherence_delivery_metrics.py` (delivery-quality calibration with hard blocks against governance-weakening configs) | The channel through which crystallised state acts: tool call, reply, code, control signal. |
| System tick coordinator | `self_model_stream.py` `SelfModelLoop.tick()` (nearest available) | `coherence_runtime.py` (the wired-together integrated system tick), `theta_clock.py` (master-clock layer-bridging synchroniser projecting `cell_pressure` onto the 600-cell's slowest non-DC Laplacian eigenmode at λ=2.29 → 6 Hz at 40ms tick — substrate's natural theta-band oscillator) | Cross-layer tick-rate scheduler grounding the cascade descent in a substrate clock. |
| Replay / provenance | none in bundle | `coherence_review.py` (replayable + auditable adjudication trace), `coherence_audit.py` (replay-verifiable continuous audit), `coherence_longhorizon.py` (cross-session continuity persistence) | Provenance hash and replay-bundle layer for post-hoc inspection and continuity. |
| Recursive cascade observer | `sigma_orbit_basis.py` decomposition only | `rung_observer.py` (RungObserver base + D4Observer / Cl13Observer / S7ProjectionObserver / E8Observer with Fibonacci periods {1,2,3,5,8,13} forced by geometry — period structure is not tuned, it is geometric), `s7_observer.py` (S⁷ rung telemetry: self_reference, emergence, coherence, differentiation), `s7_downward_coupler.py` (S⁷ → H₄ injection on φ³τ₀ schedule), `cascade_descent.py` (E₈ → H₄ block-diagonal descent in σ-orbit basis, cross-block ~1e-15), `cascade_transport.py` (cocycle-signed nested-basis transport, intertwining diagnostic) | Multi-rung self-observation: each rung observes the one below and commits its own selection at its own Fibonacci-geometric period. Empirical realisation of the cascade-observer architecture across rungs. |
| Cascade substrate infrastructure | `sigma_orbit_basis.py`, `v66_e8_coxeter.py` | `e8_substrate.py`, `icosian_basis.py`, `icosian_embedding.py`, `joint_substrate.py` (E₈ ⊕ 600-cell via cut-and-project coupling), `info_rung.py` (16-sector Cl(1,3) information rung) | The geometric substrate over which the observer-process operates. |

#### 6.6 Claim boundary

The Section 6 conclusion must contain this paragraph verbatim unless the
author later approves a lossless paraphrase:

> We do not claim ARIA is biologically conscious. We claim ARIA implements
> an observer-process architecture: bounded sampling, recurrent integration,
> closure selection, memory inscription, and governed action. Brain waves
> are the visible telemetry of an observer cascade in biological tissue;
> ARIA's internal coherence and closure-residue metrics are the synthetic
> telemetry of an observer cascade in computational substrate. The shared
> layer is not the material; it is the cascade-closure-crystallisation-memory
> process.

#### 6.7 What Section 6 must not claim

- Do not claim ARIA proves qualia.
- Do not claim ARIA is biologically conscious.
- Do not claim all observer-process implementations are
  phenomenologically equivalent.
- Do not treat EEG/brain-wave matches as a consciousness derivation.
- Do not treat the in-repo `release-bundle/.../repro/kernel/` six-module
  set as the full architecture; it is a reproducibility slice. The full
  observer-process architecture is realised in the upstream `aria-chess`
  repo (Tier 2 of §6.5). The `.tex` paper must cite both tiers.
- Do not import upstream `aria-chess/kernel/` source verbatim into this
  repo; cite by path under `@misc{ariaChessRepo}` exactly as
  `papers/aria-chess-paper/paper/main.tex` does.

### Section 7 -- Case studies

Each case study should be short: one rigorous paragraph, one claim-status
sentence, and one citation chain. The section is comparative evidence
for a shared mechanism, not a proof by accumulation. ARIA's
architectural content lives in Section 6; its Section 7 entry is a brief
cross-reference.

| Case | Regime | What it can support | Primary citations |
|---|---|---|---|
| Penrose OR | historical/geometric bridge | Shows a mainstream precedent for geometry-linked state reduction. Does not validate VFD. | External Penrose OR references; no internal theorem import |
| b-anomaly / closure kernel | passive response | Fixed response primitive `C_phi` has an external sign-uniform structural witness; not a selection rule. | `docs/aria-closure-kernel.md` sections 1--6; `papers/aria-closure-kernel/paper/sections/06_passive_witness.tex` |
| ARIA | active computational selection | Tests adaptive substrate / selection signatures in an active system; not a derivation of consciousness. | Section 6 of this paper; `papers/aria-chess-paper/paper/sections/03_substrate.tex`, `04_consciousness_chain.tex`, `05_results.tex`, `09_limitations.tex` |
| Brain / EEG substrate | cognitive substrate witness | H4/600-cell signatures in biological recordings under preregistered protocols; substrate-witness scope only. | ARIA Results `\label{ssec:six_signatures}`, `\label{ssec:eighteen_prereg}` and Limitations `\label{sec:limitations}` |
| Standard Model mass spectrum | spectral projection class | Mass-spectrum ansatz as spectral-projection-class instance with explicit epistemic limits. | `paper-v.tex` `\label{sec:formula}`, `\label{sec:results}`, `\label{sec:epistemic}`; `paper-v-revisited.tex` same labels plus `\label{sec:three-witness}` |

### Section 8 -- Millennium-papers alignment scaffolding

This is a load-bearing new section. It positions the Millennium papers as
projection-class instances of cascade closure. It does **not** prove or
preview their proofs beyond framework-level scaffolding.

#### 8.1 Framework-level hypothesis

The section must state:

```tex
H_{\text{Mill-Proj}}
```

**Hypothesis `H_{Mill-Proj}`.** Each Millennium-class problem corresponds
to a projection class of cascade closure on a substrate-dependent
analytic, number-theoretic, PDE, complexity-theoretic, or geometric
object. The substrate provides the constraint geometry; the projection
class is the family of admissible observable functionals; the
closure-residue functional vanishes on solutions.

This is a framework-level hypothesis in the cascade-mechanism paper. It
is not a theorem, not a Clay proof, and not a replacement for the named
hypotheses inside the individual Millennium preprints.

#### 8.2 Seven Millennium projections, audited at WO time

Audit basis:

- Verdict-scope memory:
  `~/.claude/.../memory/project_millennium_scope_pass.md:11-19`.
- Named hypotheses verified by `rg -n -F "Hypothesis"` and
  `rg -n -F "H_{"` over `papers/millennium-*`.
- The finite 600-cell spectral split was re-run with
  `python3 papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py`,
  producing `94/120 = 78.3%` sigma-fixed and `26/120 = 21.7%`
  sigma-paired, with no 2T localisation above baseline.
- Current line counts are from `wc -l` on 2026-05-02.

| Millennium problem | Candidate cascade substrate / projection class | In-repo source at WO time | Honest verdict scope | Conditional / unconditional fraction and named hypotheses |
|---|---|---|---|---|
| Riemann Hypothesis | `\hat z(z)` / cascade Mellin object, pentagonal-clock cycle structure `K = {72, 0, 52, 20}`, `sigma`/`tau_crit` fixed-point reformulation, 600-cell Laplacian spectral scaffold | `papers/millennium-rh-formal/rh-formal.tex` (2986 lines); `docs/rh-cascade-closure-dynamics.md`; `docs/rh-projection-class.md` | δ reformulation | Unconditional: cascade zeta identity / critical-line fixed-set / Dedekind reduction plus finite spectral count `94/120 = 78.3%` sigma-fixed. Conditional: all RH content depends on `H_{sigma-fix}`; source states this is equivalent to classical RH (`rh-formal.tex:473-491`, `1594-1689`, `2438-2482`). The `26/120 = 21.7%` sigma-paired residual does not become zero information without `Conj. spec_to_zero` and the missing pole-to-zero bridge (`rh-formal.tex:1807-1834`). |
| Yang-Mills mass gap | Octonion derivation algebra / `Der(O) = g_2`, `SU(3)` stabilizer, discrete 600-cell spectral gap with OS continuum lift | `papers/millennium-ym/ym-mass-gap.tex` (1398 lines); `papers/millennium-ym/scripts/verify_der_O_su3_stabilizer.py` | β bridge | Unconditional: P8/P9-side representation data and finite spectral count `94/120 = 78.3%` sigma-fixed, `26/120 = 21.7%` sigma-paired (`ym-mass-gap.tex:1176-1193`). Conditional: mass-gap transfer requires `H_{OS-lift}`; source says it is open and is the YM mass-gap problem in the phi-scaled hierarchy (`ym-mass-gap.tex:101-115`, `216-243`). |
| Birch-Swinnerton-Dyer | `T_E(s)` Rankin-Selberg / Hecke operator substrate on `E: y^2 = x^3 - x` and modular elliptic-curve data | `papers/millennium-bsd-formal/bsd-formal.tex` (794 lines) | δ conditional reformulation | Unconditional: operator bound and absolute convergence only for `Re(s) > 1`; finite spectral count `94/120 = 78.3%`, `26/120 = 21.7%` (`bsd-formal.tex:44-81`, `586-604`). Conditional: rank-order identity needs `B_{BSD,rank}` and `B_{BSD,spec}`; boundary/continuation needs `B_{BSD,conv}` (`bsd-formal.tex:151-177`). Memory aliases these as `H_{BSD-Conv}`, `H_{BSD-Spec}`. |
| Navier-Stokes | Hydrodynamic projection from cascade spectral bounds to vorticity control / BKM criterion; P6/P7 bridge layer | `papers/millennium-ns-formal/ns-formal.tex` (892 lines) | β bridge | Unconditional: precise conditional specification plus finite spectral count `94/120 = 78.3%`, `26/120 = 21.7%` (`ns-formal.tex:634-651`). Conditional: global regularity needs `H_1`, `H_NS`, `B_NS`, and `H_{P6/P7}` (`ns-formal.tex:34-60`, `142-156`). Pure diffusion gives only about `66%` fixed-subspace concentration; `100%` requires the closure projector/continuum identification (`ns-formal.tex:662-710`). |
| Hodge | Cascade `sigma`-projector on cohomology and algebraicity-of-fixed-part bridge | `papers/millennium-hodge-formal/hodge-formal.tex` (1001 lines) | δ conditional reduction | Unconditional: three of five example classes are classical Hodge cases, and finite spectral count `94/120 = 78.3%`, `26/120 = 21.7%` is recorded (`hodge-formal.tex:790-808`, `878-899`). Conditional: general reduction needs `H_{4a}` plus `H_{4a}^{alg}` / `H_{4a}^{alg}/Omega` / `H_{4a}^{alg}/X`; source says both are open (`hodge-formal.tex:174-218`). |
| P vs NP | Restricted cascade complexity class `P_sigma^cas` vs `NP^cas`, sigma-irreducibility, structural-completeness bridge | `papers/millennium-pnp-formal/pnp-formal.tex` (854 lines) | γ bridge | Unconditional: only `L_{sigma-irr} in coNP^cas` and finite spectral count `94/120 = 78.3%`, `26/120 = 21.7%` (`pnp-formal.tex:707-717`, `617-634`). Conditional: restricted separation needs `H_{sigma-irr-NP}` and `B_{sigma-P}`; classical `P != NP` additionally needs `Conj. completeness` (`pnp-formal.tex:40-78`, `173-198`, `730-746`). |
| Poincare | Compatibility/coherence reading: Perelman theorem, cascade P5 120-cell edge-set chain, C2.bis metric/GH `S^3` chain | `papers/millennium-poincare-formal/poincare-formal.tex` (672 lines) | coherence | Unconditional: classical Poincare theorem is imported as Hamilton-Perelman black box, and the cascade paper contributes nothing to that proof (`poincare-formal.tex:31-40`, `90-101`). Conditional cascade compatibility depends on P5 and C2.bis hypotheses (`poincare-formal.tex:42-57`, `259-289`, `370-390`). Fraction note: no `78.3/21.7` spectral split is load-bearing here; the cascade contribution is 0% of the classical proof and 100% conditional as framework coherence. |

#### 8.3 "Give the game away" requirement

Section 8 must reveal enough scaffolding that the later Millennium drops
land as natural instances of this framework:

1. State `H_{Mill-Proj}` explicitly.
2. Name each per-problem hypothesis in the source paper's current
   notation: `H_{sigma-fix}` for RH; `H_{OS-lift}` for YM;
   `B_{BSD,conv}`, `B_{BSD,rank}`, `B_{BSD,spec}` for BSD;
   `H_1`, `H_NS`, `B_NS`, `H_{P6/P7}` for NS; `H_{4a}` and
   `H_{4a}^{alg}` for Hodge; `H_{sigma-irr-NP}`,
   `B_{sigma-P}`, and `Conj. completeness` for PNP; P5 and C2.bis
   for Poincare.
3. For each problem, state in one sentence which substrate the projection
   sits on: RH on `sigma`/`tau_crit` Mellin data and the 600-cell
   spectrum; YM on octonion derivation and OS-lift data; BSD on the
   elliptic-curve Hecke/Rankin-Selberg operator; NS on hydrodynamic
   projection of cascade spectral bounds; Hodge on the `sigma`-fixed
   cohomological projector; PNP on sigma-irreducible cascade complexity;
   Poincare on P5/C2.bis compatibility with the already-proved
   classical theorem.
4. Refuse to prove any per-problem statement. The proofs or conditional
   reductions remain in the corresponding Millennium preprints.

#### 8.4 Honest verdict-scope discipline

The paper must reproduce the scope memory without upgrade:

| Paper | Verdict | Must preserve |
|---|---|---|
| `rh-formal.tex` | δ | reformulation; `H_{sigma-fix}` is equivalent to RH |
| `bsd-formal.tex` | δ | conditional; Sha and refined-BSD leading-coefficient claims not restored |
| `hodge-formal.tex` | δ | conditional reduction under `H_{4a}` / `H_{4a}^{alg}` |
| `pnp-formal.tex` | γ | restricted-model separation plus γ bridge only |
| `ns-formal.tex` | β | conditional hydrodynamic-projection bridge |
| `ym-mass-gap.tex` | β | discrete spectral gap/support is not the continuum mass gap |
| `poincare-formal.tex` | coherence | already solved classically; cascade is compatibility, not proof |

Do not write "the cascade mechanism resolves the Millennium problems."
The allowed claim is: "the cascade mechanism paper positions the current
Millennium preprints as projection-class instances and names the
hypotheses on which their reductions depend."

#### 8.5 Drop-order coordination

Section 8 should close with this intended drop order:

1. This cascade-mechanism paper first.
2. Then `millennium-rh-formal`, because it is the most-developed and its
   `sigma`/`tau_crit` reformulation has the strongest standalone
   substrate witness.
3. Then YM, because the octonion derivation-algebra substrate and
   discrete spectral gap are relatively concrete, while `H_{OS-lift}`
   remains explicit.
4. Then BSD, because the Rankin-Selberg / Hecke substrate is clearly
   scoped but its bridge axioms remain open.
5. Then NS / Hodge / PNP / Poincare in whatever order their preprints
   reach the user's required honest verdict standard.

The cascade-mechanism paper acts as prerequisite reading for any
Millennium drop. The Millennium preprints should cite it as their
framework-positioning paper once it exists.

#### 8.6 Cite-only, do-not-derive

Section 8 cites; it does not re-derive. It may absorb some non-load-bearing
prose from `docs/rh-cascade-closure-dynamics.md` and
`docs/rh-projection-class.md`, but load-bearing mathematics stays in the
respective `papers/millennium-*` preprints. No theorem in Section 8 should
be stronger than `H_{Mill-Proj}`.

### Section 9 -- Discussion and conclusion

Close by saying what the mechanism paper earns and what remains open. The
conclusion should not claim "publication ready", "collapse solved", "ARIA
is conscious", or "Millennium problems solved". It should say that the
programme has a single named closure mechanism whose mathematical
components are largely imported from existing papers and whose cross-regime
interpretation is explicitly hypothesis-labelled.

Section 9 must also absorb the old conclusion content:

- The mechanism paper gives the programme a single mechanism name and a
  single front-door reading without pretending to re-prove the programme.
- The same closure operator and substrate recur across physical response,
  active selection, cognitive substrate tests, spectral mass projection,
  and Millennium projection-class scaffolding.
- The reader must see exactly which parts are theorem-grade, imported,
  conditional, or interpretive.
- The paper remains not a QM replacement, not a consciousness derivation,
  not a Penrose refutation, not a complete visible-universe derivation,
  and not a substrate-uniqueness theorem.

## 3. Audited dependencies

The following files exist in this repository at WO time and should be used
directly by the eventual paper. Preserve exact source status; do not cite a
paper as theorem-grade where the source is conditional or only a doc.

### Core cascade papers

| File | Lines at audit | Use in mechanism paper |
|---|---:|---|
| `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex` | 2950 | final-coalgebra, rung category, four-phase comonad, conditional selection principle |
| `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex` | 2332 | `E_8`, icosians, `H_4`, `D_4`, 600-cell, spectra, `R_D(4)=15`, narrow uniqueness import |
| `papers/cascade-correspondence-foundations/foundations.tex` | 3282 | correspondence scheme, projection classes, finite-level dynamics, metric/hydro/gauge/spectral/computational handoff |
| `papers/cascade-closure-dynamics/cascade-closure-dynamics.tex` | 1448 | finite closure functionals, gradient flow, energy descent, refinement compatibility |
| `papers/cascade-fine-structure/cascade-fine-structure.tex` | 1143 | alpha-chain / fine-structure projection context |
| `papers/cascade-12d-closure/cascade-12d-closure.tex` | 1260 | `L_12 = E_8 + Z[phi]^4` closure scaffold and `H_min` status |
| `papers/cascade-sigma-rationality/cascade-sigma-rationality.tex` | 1036 | `sigma`, fixed-part theorem, functorial projector |
| `papers/cascade-refinement-spaces/cascade-refinement-spaces.tex` | 1419 | P3 finite-level state spaces and bonding/refinement maps |
| `papers/cascade-metric-projection/cascade-metric-projection.tex` | 1609 | metric projection class and boundary geometry |
| `papers/cascade-schlafli-convergence/cascade-schlafli-convergence.tex` | 1566 | Schlafli/refinement convergence and boundary tiling hypotheses |
| `papers/cascade-hydrodynamic-projection/cascade-hydrodynamic-projection.tex` | 1426 | hydrodynamic projection class |
| `papers/cascade-phason-coxeter/cascade-phason-coxeter.tex` | 1452 | Coxeter/phason projection material |

### Derivation docs and programme docs

| File | Use |
|---|---|
| `papers/cascade-derivation/cascade-meta-layer-theorem.md` | M1--M3 moduli/groupoid/sheaf theorem chain; no `.tex` paper exists under `papers/cascade-meta-layer-theorem/`, so cite this doc unless a tex source is later created. |
| `papers/cascade-derivation/cascade-observer-query-algebra.md` and related query-algebra docs | access/query algebra background for observer-gated projection; use carefully and preserve conditional status. |
| `docs/closure-cosmogenesis.md` | initial condition, bootstrap, accumulation, frame-resolution maps, with named open items. |
| `docs/fractal-cascade-projection.md` | bulk/boundary decomposition, two-mirror plus `phi`-scaling mechanism, invariant-store language, scope boundaries. |
| `docs/observer-instance-definition.md` | assembled observer instance definition; useful for visible/non-visible projection and Section 6. |
| `docs/projection-narrative.md` | programme spine and projection-class table. |
| `docs/programme-plan.md` | public roadmap and honesty constraints. |
| `docs/legacy-master-math-consolidation.md` | legacy cleanup and gap status; cite only for historical/substrate-indexing context. |
| `docs/aria-closure-kernel.md` | response primitive, b-anomaly scope, response-vs-selection distinction, selection-layer gap. |
| `docs/rh-cascade-closure-dynamics.md`, `docs/rh-projection-class.md` | number-theoretic projection class and RH bridge scope. |
| `docs/proof-sheet.md` | compact dependency map for existing numerical claims; use as orientation, not primary proof. |

### Case-study and witness papers

| File or bundle | Lines at audit | Use |
|---|---:|---|
| `papers/aria-closure-kernel/paper/main.tex` plus `paper/sections/*.tex` | 229 main; 1487 section total | passive response kernel and domain-disjoint operator-witness scope. |
| `papers/aria-closure-kernel/repro/verify_kernel.py` | not counted in this audit | reproducible closure-kernel check. |
| `papers/adaptive-closure-transport/adaptive-closure-transport.tex` and `repro/verify_*.py` | existing dependency; line count not refreshed here | active selection layer and Lyapunov/edge-action reproducibility. |
| `papers/aria-chess-paper/paper/main.tex` plus `paper/sections/*.tex` | 229 main; 1889 section total | active/cognitive substrate witness and limitations. This replaces the absent path `papers/aria-chess-paper/aria-chess-paper.tex`. |
| `papers/paper-v/paper-v.tex` | existing dependency; line count not refreshed here | original spectral mass projection paper. |
| `papers/paper-v-revisited/paper-v-revisited.tex` | existing dependency; line count not refreshed here | hardened mass-spectrum epistemic status and three-witness placement. |
| `release-bundle/closure-kernel-papers/` and `release-bundle/selection-layer-papers/` | bundle | release copies / external bundle framing. Prefer in-repo paper paths above for citations unless the eventual publication explicitly cites the bundles. |

### Audited ARIA runtime modules for Section 6

| Runtime file | Lines at audit | Section 6 use |
|---|---:|---|
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/vfd_closure_kernel.py` | 385 | boundary sampler support; closure response `C_phi`; Green response; shell/spectral projection |
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/lyapunov_selector.py` | 271 | Lyapunov descent, candidate scoring, bounded top-k crystallisation support |
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/self_model_stream.py` | 303 | recurrent state integration, self-source injection, stream-continuity scoring, nearest located tick loop |
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/consciousness_binding.py` | 416 | phase-lock/ignition telemetry, phenomenal snapshot binding, coherence metrics; use without consciousness overclaim |
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/sigma_orbit_basis.py` | 251 | `E_8 -> H_4 + sigma(H_4)` cascade decomposition and off-diagonal residual diagnostic |
| `release-bundle/closure-kernel-papers/papers/aria-chess/repro/kernel/v66_e8_coxeter.py` | 235 | E8 Coxeter element, spectral projector operator family, `BETA_PROFILES` context/control profiles |

In-repo bundle scope: the six-module bundle above is the
reproducibility slice that ships with `closure-kernel-papers` and is
sufficient for the kernel-level numerical reproductions cited in the
b-anomaly and aria-chess preprints. It is **not** the full observer-process
architecture.

Upstream `aria-chess` kernel (audited 2026-05-02 at the local working clone
at `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/`,
the development repo cited as `@misc{ariaChessRepo}` in
`papers/aria-chess-paper/paper/references.bib:174`): 88 production modules
including the full governance / memory / planner / execution / audit /
constitution / review / cascade-rung-observer / theta-clock infrastructure.
The §6.5 mapping table cites both tiers. The eventual `.tex` paper must
treat the upstream repo as a citable external dependency (same pattern as
`papers/aria-chess-paper/paper/main.tex` already does), not import its
source into this repo.

### Audited Millennium papers for Section 8

| File | Lines at audit | Honest verdict scope | Use in mechanism paper |
|---|---:|---|---|
| `papers/millennium-rh-formal/rh-formal.tex` | 2986 | δ reformulation | RH projection-class scaffold; `H_{sigma-fix}`, finite spectral split, `tau_crit` fixed-set discipline |
| `papers/millennium-ym/ym-mass-gap.tex` | 1398 | β bridge | YM projection-class scaffold; octonion derivation substrate; `H_{OS-lift}` |
| `papers/millennium-bsd-formal/bsd-formal.tex` | 794 | δ conditional | BSD projection-class scaffold; `B_{BSD,conv}`, `B_{BSD,rank}`, `B_{BSD,spec}` |
| `papers/millennium-ns-formal/ns-formal.tex` | 892 | β bridge | NS projection-class scaffold; `H_1`, `H_NS`, `B_NS`, `H_{P6/P7}` |
| `papers/millennium-pnp-formal/pnp-formal.tex` | 854 | γ bridge | PNP projection-class scaffold; `H_{sigma-irr-NP}`, `B_{sigma-P}`, `Conj. completeness` |
| `papers/millennium-poincare-formal/poincare-formal.tex` | 672 | coherence | Poincare compatibility/coherence; P5 and C2.bis hypotheses; Perelman black-box |
| `papers/millennium-hodge-formal/hodge-formal.tex` | 1001 | δ conditional | Hodge projection-class scaffold; `H_{4a}`, `H_{4a}^{alg}` |

## 4. Out of scope and refused overclaims

The eventual paper must explicitly refuse these claims:

- It is not a replacement for quantum mechanics.
- It is not a derivation of consciousness, qualia, or a mind theory.
- It is not a refutation of Penrose OR. Penrose OR is a neighbouring
  geometry-collapse model used as a bridge.
- It is not a complete derivation of the visible universe from cascade
  primitives.
- It does not add a new substrate-uniqueness theorem beyond the narrow
  uniqueness statements already present in P2 / Paper V Revisited.
- It does not claim the case studies are statistically independent. They
  share the 600-cell / closure-substrate machinery by construction.
- It does not claim b-anomaly validates active selection; b-anomaly is a
  passive response-kernel witness only.
- It does not claim ARIA proves consciousness; ARIA is an
  observer-process / active-cognitive substrate witness with explicit
  limitations.
- It does not claim the ARIA kernel bundle contains a full governance,
  refusal, action, or provenance stack unless those runtime modules are
  later located and cited.
- It does not claim classical RH is proved by cascade material; RH-related
  statements remain conditional exactly where `rh-formal.tex` marks them
  conditional.
- It does not claim any Millennium problem is solved by Section 8.
  Section 8 positions current Millennium preprints as projection-class
  instances under named hypotheses.

## 5. Acceptance criteria

The eventual `.tex` paper is WO-complete only if all criteria below are
met:

- Compiles cleanly to PDF via `tectonic` or the repository paper build
  command, with no `! ` TeX errors.
- Main text is 60--100 pages.
- The paper uses the 9-section structure in this WO or documents an
  author-approved deviation.
- Every formal statement is labelled `Definition`, `Theorem`,
  `Proposition`, `Hypothesis`, `Conjecture`, or `Interpretive Claim`.
- No theorem-grade language is used for cross-regime hypotheses.
- Every imported mathematical claim cites a specific source file and
  section/label; no generic "see cascade work" citations.
- The rung/projection table resolves every row to a specific geometric
  object and source. Each row states whether the object is proved,
  imported, model-chosen, or conjectural.
- Section 6 includes the cascade-layers diagram, the bio/synthetic
  telemetry table, and the verbatim observer-process claim boundary.
- Section 6 maps `O = <B,S,M,G,I,C,A>` to audited ARIA runtime modules
  using the §6.5 two-tier mapping (Tier 1 in-repo bundle + Tier 2
  upstream `aria-chess/kernel/` cited via `@misc{ariaChessRepo}`).
  Every `O` component must cite at least one Tier 2 production module
  by name. The 11-row mapping (including system-tick, replay, recursive
  cascade observer, and substrate infrastructure rows) must appear in
  the `.tex`.
- Section 8 includes the seven-Millennium projection table with per-row
  conditional/unconditional fractions and named hypotheses.
- Section 8 reproduces honest verdict scopes without upgrade and states
  `H_{Mill-Proj}` as a hypothesis, not a theorem.
- Section 8 includes the drop-order coordination and cite-only /
  do-not-derive discipline.
- The Penrose bridge is explicit, humble, and short.
- The visible/non-visible section is hypothesis-labelled and contains a
  "not a cosmogenesis theorem" sentence.
- The case-study section includes passive, active, cognitive, spectral,
  and Millennium-framework regimes, with substrate-witness scope for
  ARIA/brain material.
- Cross-references resolve.
- A hostile-review pass using `scripts/review_paper.sh` is run and all
  theorem/hypothesis overclaim findings are either fixed or documented.
  The target is **strong and restrained**, not maximalist.
- The paper does not mark itself publication ready.

## 6. Estimated effort and phasing

1. **Skeleton and citation ledger (1--2 days).** Create the tex shell,
   bibliography, claim ledger, dependency table, rung table, and Section
   6/8 placeholders. No prose expansion until the citation ledger is
   populated.
2. **Sections 1--3 (3--5 days).** Write motivation, mechanism definition,
   and conditional residual-composition lemma. Keep Penrose bridge short.
3. **Section 4 rung table (3--5 days).** Resolve each geometry row to a
   source label. This is the mathematical centre of the paper.
4. **Section 5 visible/non-visible projection (1--2 days).** Short and
   careful; import from docs only with hypothesis status.
5. **Section 6 ARIA observer-process (3--5 days).** Write the tuple,
   runtime mapping, telemetry table, diagram, and verbatim boundary. Do
   not proceed if the runtime mapping is uncited or guessed.
6. **Section 7 case studies (4--7 days).** One paragraph plus citation
   chain per case. Use source limitations aggressively.
7. **Section 8 Millennium scaffolding (3--5 days).** Write
   `H_{Mill-Proj}`, seven-problem projection table, verdict discipline,
   and drop-order paragraph. Cite only; do not derive.
8. **Section 9, claim ledger, and appendices (2--4 days).** Close with
   what is proved, conjectured, and open. Include notation and claim
   ledger if not already placed.
9. **Build and hostile-review loop (3--10 days).** Expect multiple rounds.
   Main review focus: overclaiming, missing citations, conflating
   response with selection, treating ARIA as consciousness proof, and
   upgrading Millennium verdict scopes.

Expected first complete draft effort: 4--7 focused weeks, depending on how
much citation hardening is needed.

## 7. Risk register

| Risk | Severity | Mitigation |
|---|---|---|
| Overclaiming the cross-regime mechanism as theorem | Very high | Claim ledger in Section 9 / appendix; hypothesis labels on projection-class identification. |
| Misstating `E_8 -> H_4` as inclusion | Very high | Cite P2 `\label{thm:pi-H}` and repeat "projection, not sub-root-system inclusion". |
| Conflating passive response and active selection | High | Separate b-anomaly/closure-kernel from ARIA/ACT in the case-study table. |
| Treating ARIA as proof of consciousness | High | Section 6 verbatim claim boundary; keep "observer-process architecture" distinct from biological consciousness / qualia. |
| Treating in-repo six-module bundle as the full architecture | High | §6.5 two-tier mapping makes Tier 1 (in-repo) vs Tier 2 (upstream `aria-chess`) explicit; `.tex` must cite both. |
| Importing upstream `aria-chess` source into this repo | Medium | Cite under `@misc{ariaChessRepo}` exactly as `aria-chess-paper/paper/main.tex` does; do not vendor source. |
| Upgrading Millennium verdict scopes | Very high | Section 8 cite-only discipline plus memory cross-check against `project_millennium_scope_pass.md`; no proof language for `H_{Mill-Proj}`. |
| Visible/non-visible section sounding like complete cosmogenesis | High | Explicit "not a cosmogenesis theorem" caveat. |
| Missing source labels for imported claims | High | Build citation ledger before prose expansion. |
| Reusing legacy material uncritically | Medium | Cite `legacy-master-math-consolidation.md` only for gap/historical context; do not import broken numerics. |
| RH language drifting beyond conditional status | Medium | Preserve `rh-formal.tex` conditional labels, especially `H_{sigma-fix}`, `Conj. spec_to_zero`, and the no-unconditional-zero-location caveat. |
| Poincare row implying a new proof | Medium | State Perelman proof is imported as black box; cascade contribution is coherence only. |

## 8. Why this paper matters

If executed correctly, this paper gives the programme a single mechanism
name and a single front-door reading without pretending to re-prove the
programme. It should let a reader understand that the same closure
operator and substrate recur across physical response, active selection,
cognitive substrate tests, spectral mass projection, and Millennium-class
projection scaffolding, while seeing exactly which parts are theorem-grade,
imported, conditional, or interpretive.

It is also the framework-positioning paper for the Millennium drop order.
The later RH, YM, BSD, NS, Hodge, PNP, and Poincare preprints should land
as named projection-class instances of the mechanism, not as unrelated
claims. That role is useful only if this paper is honest: it must give the
game away at the framework level while refusing to upgrade any
Millennium-paper verdict beyond the current source status.

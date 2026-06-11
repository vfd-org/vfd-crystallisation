# WO-ARIA-VFD-EXPLORER-001: Research Log

## VFD Explorer — a unified computational library for deriving, validating, and showcasing the VFD framework

**Status:** Active planning
**Date opened:** 2026-04-16
**Classification:** Software infrastructure + validation + showcase
**Priority:** Foundational — predecessor to CCRO and to any future physics-facing paper

---

## 1. Executive Summary

The VFD framework currently comprises ~33 papers, 47 paper-specific
verification scripts, and ~3,100 lines of `src/vfd/crystallisation/`
code focused on the *crystallisation operator* (the flagship
collapse-replacement machinery). Particle-physics derivations — the
600-cell geometry, H₄/E₈ structure, shell assignments, masses, radii,
couplings — are scattered across per-paper scripts that each rebuild
the same primitives from scratch.

**The Explorer** is the missing unified layer. It is a single library
(`src/vfd_core/` plus a thin CLI and a dashboard) that:

1. **Encodes every recurring primitive once** — 600-cell geometry, H₄
   Coxeter system, E₈ root system, representation theory, shell
   assignment machinery, closure functionals, spectral operators.

2. **Exposes every numerical claim in every paper as a callable
   function** that returns `(predicted, measured, uncertainty,
   relative_error, method_reference)` so any claim can be re-derived
   and re-checked on demand.

3. **Runs a full validation suite** — one command re-derives every
   published prediction, reports pass/fail against experiment with
   statistical margins, and generates a one-page credibility report.

4. **Surfaces consistency** — change a shell assignment, an integer, or
   a representation choice, and the library reports every downstream
   prediction that breaks. Inconsistencies become visible, not hidden.

5. **Generates new predictions** — once primitives are factored, new
   shell combinations / representation choices can be swept
   systematically. Hypotheses become runnable experiments.

6. **Showcases credibly** — notebooks, a dashboard, and a public
   prediction registry with experimental comparisons make the
   framework browsable by a physicist who has never seen it before.

**Why this is worth building before anything else:** every future
paper, every reviewer response, every external collaborator
conversation will need the question "does this actually reproduce?"
answered in seconds. Right now the answer is "let me find the script"
across 47 folders. After the Explorer, the answer is one command.

---

## 2. The Gap This Closes

From the framework inventory (2026-04-16):

| Asset | State | Gap |
|---|---|---|
| 600-cell geometry | Built 3× (scripts/, paper-v, paper-xxii) | No single source of truth |
| H₄ Coxeter system | Implicit in scripts | No reusable module |
| E₈ roots and projection | Paper XXII scripts only | Not exposed as a library |
| Representation theory | Manual per paper | No irrep / branching library |
| Shell assignments | Reinvented per paper | No canonical registry |
| Mass predictions | 13 masses verified in one place | Not tied to paper claims individually |
| Hadron radii | Verified for p/n/π/K | No neutron charge-radius², no deuteron yet |
| α⁻¹ = 137 + π/87 | Verified | Not linked to 084473 chain |
| 084473 = 137(7×87+8)−56 | Verified | Numerics only, no structural claim check |
| Generations Z₃, sin²θ_W | Verified in paper-xxii | Not exposed as queryable prediction |
| Spacetime emergence (XXIII–XXVIII) | Analytical only | No numerical verification at all |
| Measurement (XXXIII) | Recent, conceptual | No runnable claim yet |
| Consistency across papers | Nothing enforces it | Silent divergence risk |
| External showcase | `docs/` overview only | No interactive demonstration |

The Explorer is the single artefact that closes every row.

---

## 3. Target Architecture

```
src/vfd_core/
    __init__.py
    constants.py            # α⁻¹, φ, 137, 87, 50, 94, 084473, etc.
    geometry/
        sixhundred_cell.py  # vertices, adjacency, Laplacian, Hopf
        h4.py               # H₄ Coxeter group and its exponents
        e8.py               # E₈ root system and E₈→H₄ projection
        polytope_checks.py  # uniqueness / regularity theorems
    algebra/
        coxeter.py          # exponents, eigenvalues exp(2πim/h)
        representations.py  # irreps, branching rules
        spectrum.py         # Laplacian spectrum, eigenvalue algebra
    shells/
        assignment.py       # canonical shell→particle registry
        distance.py         # graph distance, shell membership
        invariants.py       # NN/NNN eigenvalues, shell identities
    closure/
        functional.py       # F = αR + βE − γQ (already in vfd/crystallisation)
        residual.py         # Ξ(state) — structural admissibility
        operators.py        # G, K, coherence, resonance
    predictions/
        masses.py           # 13+ particle masses → predict_mass(symbol)
        radii.py            # charge radii → predict_charge_radius(symbol)
        couplings.py        # α, α_s, sin²θ_W, CKM angles
        constants.py        # 084473, π/87, φ-relations
        generations.py      # Z₃ structure, generation count
        hadrons.py          # form factors, coherence lengths
        leptons.py          # lepton masses and no-go results
        gravity.py          # (stub) curvature predictions from XXIII–XXVIII
    registry/
        predictions.yaml    # canonical list: every claim with paper ref
        experiments.yaml    # experimental values + uncertainties + sources
        dependencies.yaml   # DAG: which predictions depend on which
    validation/
        verify.py           # re-derive every registered prediction
        compare.py          # predicted vs measured with sigma margins
        consistency.py      # DAG check — change X, see what breaks
        report.py           # one-page credibility PDF/MD
    sweep/
        parameter_sensitivity.py  # sweep integers / shell choices
        hypothesis_runner.py      # run a new prediction end-to-end
    data/
        600cell.npz         # canonical precomputed geometry
        e8_roots.npz
        experimental.csv    # PDG/NIST values with uncertainties
    cli.py                  # `vfd verify`, `vfd predict <symbol>`, `vfd sweep`

src/vfd/crystallisation/     # existing — NOT touched, imports into vfd_core
tests/vfd_core/              # one test per registered prediction
notebooks/explorer/
    01_geometry_tour.ipynb
    02_mass_spectrum.ipynb
    03_hadron_radii.ipynb
    04_couplings_and_constants.ipynb
    05_consistency_dashboard.ipynb
benchmarks/explorer/
    full_framework_report.py  # produces credibility report
papers/vfd-explorer/
    WO-VFD-EXPLORER.md        # this document
    v1-coverage-matrix.md     # which paper claims are covered by v1
    v1-report.md              # generated by benchmarks/explorer
```

Key design choices:

- **`vfd_core` is new; `vfd/crystallisation/` stays untouched.** The
  existing operator/estimation/falsifiability code is already solid
  and tested — the Explorer imports it, does not replace it.
- **Registry-driven.** `registry/*.yaml` is the single source of
  truth. Every prediction has an entry; every entry maps to a
  function; every entry maps to an experimental value.
- **Pure functions where possible.** Geometry and algebra modules are
  stateless. Predictions are pure functions of the registry + data.
  Stateful workflow (sweeps, hypothesis runs) lives in `sweep/`.
- **One test per prediction.** `tests/vfd_core/` has one pytest per
  registry entry; the CI matrix is the validation matrix.

---

## 4. Module Specifications

### 4.1 `geometry/` — the unified geometric ground truth

**`sixhundred_cell.py`**
- `build()` returns a `SixHundredCell` dataclass: vertices (120×4),
  edges, adjacency matrix, Laplacian, eigenvalues, eigenvectors, Hopf
  fibration (12×10), shell partition by graph distance.
- Result cached on disk (`data/600cell.npz`); rebuild only on version
  bump.
- Replaces the three independent implementations currently scattered
  across `scripts/`, `paper-v/`, `paper-xxii/`.

**`h4.py`**
- `H4Coxeter` dataclass: generators, Coxeter number h=30, exponents
  {1, 11, 19, 29}, eigenvalues exp(2πi·m/30), upper exponents
  {17, 19, 23, 29}.
- Exposes `sum_upper_exponents() == 88`, `sum_upper_minus_one() == 87`.

**`e8.py`**
- Full E₈ root system (240 roots), Gosset polytope vertex structure.
- `project_to_h4()` — deterministic 2:1 projection E₈ → 600-cell;
  verifies exactly 2 roots per vertex.
- Exposes the identity "2 × 600-cell vertices within one E₈" as a
  testable property.

**`polytope_checks.py`**
- Uniqueness proofs: there are exactly six regular polytopes in 4D,
  the 600-cell is the unique one with 120 vertices and icosahedral
  face structure. Machine-checkable where feasible.

### 4.2 `algebra/` — representation-theoretic primitives

**`coxeter.py`**
- Coxeter exponent lists for A, D, E, H series; projection
  eigenvalues; phase accumulators used in α⁻¹ = 137 + π/87.

**`representations.py`**
- Irreps of the binary icosahedral group 2I (what carries the 600-cell
  structure).
- SU(5) branching rules used in Paper XXII.
- `rho_{4'}` and friends from the proton-radius WO.

**`spectrum.py`**
- The 9 non-trivial Laplacian eigenvalues {9, 12, 14, 15, 27, 28, 40,
  42, 48}.
- The mass eigenvalue sector {9, 12, 14, 15}, trace 50, and the three
  independent routes to 87.
- NN and NNN eigenvalues per irrep.

### 4.3 `shells/` — the canonical particle / shell registry

**`assignment.py`**
- Canonical map particle → shell set. Proton = {2,3,4}, electron =
  {1}, etc. Pulled from Papers I, IV, VIII, and the proton-radius WO.
- Single source of truth. No paper re-invents assignments.

**`distance.py`**
- Graph distance on the 600-cell. Shell = level-set of distance from
  origin vertex.

**`invariants.py`**
- `max_shell(particle)`, `shell_dimension(particle)`, NN/NNN
  eigenvalue sums — all the integer invariants that show up in mass
  and radius formulae.

### 4.4 `closure/` — the VFD operator layer

Thin imports of the existing `vfd/crystallisation/operator.py`, plus:

- `residual.Ξ(state, invariants)` — returns the closure residual used
  in the formal admissibility statements.
- `operators.coherence_metric`, `resonance_metric` — the Q and R terms
  used by later predictions and, eventually, by CCRO.

### 4.5 `predictions/` — the heart of the Explorer

Every numerical claim in the papers becomes a function. Uniform
signature:

```python
def predict_proton_radius() -> Prediction:
    r = n_max(proton) * hbar / (m_p * c)
    return Prediction(
        name="proton_charge_radius",
        value=r,
        unit="fm",
        method="n_max × lambdabar_p (triply determined factor 4)",
        paper_ref="WO-PROTON-RADIUS",
        experimental=ExperimentalValue(0.8409, 0.0004, "PDG 2022"),
    )
```

`Prediction` dataclass tracks: name, value, unit, method, paper ref,
uncertainty (if any), and the experimental value to compare against.

Modules inside `predictions/`:

- `masses.py` — 13 particle masses from Paper V, proton/electron
  ratio from master-mass, φ-scaling relations.
- `radii.py` — proton, neutron <r²>, pion, kaon, deuteron from
  Paper XXXII + proton-radius WO.
- `couplings.py` — α⁻¹ = 137 + π/87 (Paper XXII / master-mass);
  sin²θ_W = 3/8; α_s structure.
- `constants.py` — 084473 universal activation code; π/87 structural
  origin; φ-mass relations.
- `generations.py` — Z₃ generation structure; no-go for 4th
  generation from shell extension (Paper F / lepton-generations).
- `hadrons.py` — form factors G_E(Q²), coherence lengths, F_int
  decomposition.
- `leptons.py` — lepton mass spectrum, conditional π/87 via spectral
  dimension.
- `gravity.py` — **STUB** for Papers XXIII–XXVIII. These are
  currently analytical only; v1 registers them as "not yet
  numerically verified" and v2 implements curvature-from-event-order
  numerics.

### 4.6 `registry/` — the source of truth

**`predictions.yaml`** (illustrative fragment)
```yaml
- id: proton_charge_radius
  paper: proton-radius
  module: vfd_core.predictions.radii
  function: predict_proton_radius
  unit: fm
  experimental:
    value: 0.8409
    uncertainty: 0.0004
    source: PDG 2022
  depends_on:
    - proton_shell_assignment
    - proton_mass
- id: alpha_inverse
  paper: master-mass
  module: vfd_core.predictions.couplings
  function: predict_alpha_inverse
  unit: dimensionless
  experimental:
    value: 137.035999084
    uncertainty: 0.000000021
    source: CODATA 2022
  depends_on:
    - coxeter_upper_exponents_sum
    - mass_eigenvalue_trace
```

**`experiments.yaml`** — ledger of PDG/CODATA/NIST values with
citations and measurement methods. Updated when PDG releases new
averages.

**`dependencies.yaml`** — the derivation DAG. Primitives at the root;
predictions at the leaves; intermediate quantities in between.

### 4.7 `validation/` — the credibility engine

- `verify.py` — iterate registry, call every function, collect
  `Prediction` results, compare to experimental.
- `compare.py` — report relative error, σ-margin, pass/fail per
  prediction.
- `consistency.py` — DAG walker: "if I change primitive X, which
  registry entries become stale?" Flags silent divergence across
  papers.
- `report.py` — produces `v1-report.md` (and optionally PDF): a
  one-page table of every VFD prediction vs experiment, with
  uncertainties, σ-margins, and paper references. This is the
  credibility artefact.

### 4.8 `sweep/` — hypothesis discovery

- `parameter_sensitivity.py` — sweep the integer parameters (shell
  assignments, representation choices, exponent sums); report which
  predictions remain within experimental uncertainty and which fail.
  This is what tells you "the factor 4 is triply determined" as a
  quantitative stability result rather than an analytical assertion.
- `hypothesis_runner.py` — given a proposed new shell assignment /
  rep / identity, run the full prediction pipeline and report
  pass/fail against experiment. Turns "what if we assigned the
  neutrino to shell 0" into a one-liner.

### 4.9 `cli.py` — the user-facing surface

```
vfd verify                     # run full validation suite, print report
vfd verify --paper XXXII       # run only predictions from paper XXXII
vfd predict proton_radius      # print a single prediction + comparison
vfd predict --list             # list every registered prediction
vfd sweep shell proton         # sweep proton shell assignments
vfd consistency                # DAG health check
vfd report --format md         # generate credibility report
```

### 4.10 Notebooks — the showcase layer

Five notebooks mirroring the library modules. Each is both a
pedagogical walkthrough and a live demonstration. They import from
`vfd_core` — no copy-pasted math. If the library changes, the
notebooks update on re-run.

---

## 5. Paper Coverage Matrix (v1 target)

Abbreviated; the full matrix goes in `v1-coverage-matrix.md`.

| Paper / WO | Predictions registered | V1 covered? |
|---|---|---|
| Master-Mass (E) | 13 masses, α⁻¹ = 137+π/87, mp/me ratio | **Yes** |
| Paper V | Spectrum {9,12,14,15,27,28,40,42,48}, 13 masses | **Yes** |
| Paper VIII | Proton shell {2,3,4}, confinement invariants | **Yes** |
| Paper XXII | α⁻¹, sin²θ_W=3/8, Z₃ generations, 94 modes, E₈→H₄ 2:1 | **Yes** |
| Paper XXXII | Hadron charge radii (p, n, π, K) + F, F_int decomp | **Yes** |
| Proton-radius WO | r_p = 4λ̄_p, triply determined factor 4 | **Yes** |
| God Prime WO | 084473 = 137(7·87+8)−56 | **Yes** |
| Lepton-generations (F) | No-go for 4th generation, conditional π/87 | **Yes** |
| Papers VI, VII, IX, X, XI | Structural correspondences | **Partial** (structural checks, not numerical) |
| Papers XII–XXI | Dynamics, quantisation, interference | **Partial** (imports from vfd/crystallisation) |
| Papers XXIII–XXVIII | Spacetime / metric / curvature emergence | **No** (v2; currently analytical only) |
| Paper XXXIII | Measurement as closure projection | **Structural** (no numerical claim yet) |
| Bridge / Composition / Shell-Link | Technical companions | **Yes** (primitives) |
| Main-preprint / Formalism / Experimental / Mechanism / Inevitability | Crystallisation operator | **Yes** (via existing vfd/crystallisation) |

**V1 target: ≥ 90% of numerical claims registered, callable, and
compared to experiment.** Analytical-only papers (XXIII–XXVIII) are
honestly marked as such in the registry.

---

## 6. Verification Strategy

Three layers:

1. **Unit tests per prediction.** `tests/vfd_core/test_predictions.py`
   iterates the registry and asserts each prediction lies within
   stated tolerance of experiment. Tolerance is per-entry — tight
   (0.1%) where the derivation claims to be tight, looser where the
   paper says "order of magnitude."

2. **Structural tests.** Geometry and algebra modules get dedicated
   unit tests: the 600-cell has exactly 120 vertices, the E₈→H₄
   projection covers each H₄ vertex exactly twice, the Coxeter upper
   exponent sum is 88, etc.

3. **Consistency tests.** `test_consistency.py` walks the DAG and
   verifies that primitives are consistent with claimed downstream
   values (e.g. Σ mass-eigenvalue-trace = 50 agrees with the 87
   derivation in three independent ways).

CI runs all three on every commit. Any new paper requires a registry
entry; the registry lint refuses merges that leave claims
unregistered.

---

## 7. Phasing and Milestones

### Phase 1 — foundation (target: 2–3 weeks)
- Scaffold `vfd_core` package.
- Migrate `build_600cell.py` to `geometry/sixhundred_cell.py`.
- Build `h4.py`, `e8.py`, `spectrum.py`, `shells/assignment.py`.
- Stand up the registry (`predictions.yaml`, `experiments.yaml`).
- Smoke-test: registry loads, geometry builds, one prediction
  (proton radius) returns correct value.

### Phase 2 — prediction coverage (target: 3–4 weeks)
- Implement `predictions/masses.py` — all 13 masses from Paper V.
- Implement `predictions/radii.py` — proton, neutron², pion, kaon.
- Implement `predictions/couplings.py` — α⁻¹, sin²θ_W.
- Implement `predictions/constants.py` — 084473 and π/87.
- Implement `predictions/generations.py` — Z₃ structure.
- Tests: one per prediction, all green.

### Phase 3 — validation and reporting (target: 1–2 weeks)
- `validation/verify.py`, `compare.py`, `report.py`.
- Produce first `v1-report.md` — a single page with every VFD
  prediction vs experiment.
- CLI: `vfd verify`, `vfd predict`, `vfd report`.

### Phase 4 — consistency and sweeps (target: 2–3 weeks)
- `validation/consistency.py` — DAG walker.
- `sweep/parameter_sensitivity.py` — integer-sweep framework.
- Demonstrate: "the factor 4 in r_p is triply determined" as a
  quantitative sensitivity result, not an analytical assertion.

### Phase 5 — showcase (target: 2 weeks)
- Five notebooks in `notebooks/explorer/`.
- Optional: Streamlit or Observable dashboard reading the registry.
- Public README for `vfd_core` suitable for external physicists.

### Phase 6 — gravity stub and v2 planning
- Register XXIII–XXVIII predictions as "analytical only, not yet
  verified."
- Scope v2: numerical curvature from event-order geometry.

Total v1 scope: ~10–14 weeks elapsed calendar, assuming part-time
cadence. Claude agents can execute most of phases 1–3 in days if
given the WO as a spec.

---

## 8. Success Criteria

V1 ships when:

1. `vfd verify` runs end-to-end and prints a pass/fail table for
   every registered prediction.
2. ≥ 90% of numerical claims across the 33-paper body are registered
   and within claimed tolerance of experiment.
3. All structural tests green (geometry, algebra, DAG).
4. `v1-report.md` exists and reads cleanly as a credibility document
   — a physicist unfamiliar with the framework can scan it in 5
   minutes and see the evidence.
5. Five notebooks render without errors and tell the framework story.
6. Every paper's numerical claims have a direct `module.function`
   reference in the registry — no "the script is somewhere in
   papers/" answers.
7. Changing a primitive (e.g. altering a shell assignment) is
   detected by the consistency checker and surfaces every affected
   prediction within seconds.

---

## 9. Risks and Mitigations

**Risk 1: scope explosion.** 33 papers × multiple claims each is a
lot. **Mitigation:** phase-gate by paper, not by feature. Phase 2
ships whatever predictions are ready; the registry makes partial
coverage honest and visible.

**Risk 2: silent divergence between `vfd_core` reimplementations and
legacy per-paper scripts.** **Mitigation:** every migration step adds
a test that compares the new `vfd_core` output to the legacy script
output byte-for-byte before retiring the legacy script.

**Risk 3: analytical-only papers (XXIII–XXVIII) resist numerical
verification.** **Mitigation:** register them honestly as "structural
claim, no numerical test yet." Do not fake coverage. Push
quantitative versions to v2.

**Risk 4: registry maintenance overhead.** **Mitigation:** lint on CI
— new predictions require a registry entry; unregistered public
functions in `predictions/` fail the lint.

**Risk 5: external dependencies creep.** **Mitigation:** `vfd_core`
depends only on numpy, scipy, and (optional) sympy. No deep-learning
libraries. CCRO's later dependency on torch stays isolated to
`src/vfd_optim/`.

**Risk 6: performance.** E₈ roots and full Laplacian are not tiny
but are not huge either. **Mitigation:** everything caches to disk
under `data/`; rebuilds are opt-in.

---

## 10. Relationship to Other Efforts

- **`vfd/crystallisation/`** (existing): left alone. `vfd_core`
  imports it for closure operators. No duplication.
- **Paper-specific scripts**: become thin wrappers over `vfd_core`
  over time. Migration is gradual; legacy scripts stay functional
  until their paper is registered and green.
- **CCRO (vfd-optimiser)**: resumes after Explorer v1 ships. CCRO's
  coherence / closure functionals are thin adapters over
  `closure/operators.py`. The Explorer is the substrate CCRO sits on.
- **Future papers**: new claims must register. This turns the
  registry into a living contract. The next VFD paper is not
  submittable until its claims are callable and green.

---

## 11. Next Steps

1. ✅ ~~User sign-off on architecture (§3) and phasing (§7).~~
2. ✅ ~~Phase 1 kickoff: scaffold `vfd_core`, migrate 600-cell, set up
   registry skeleton.~~ (shipped 2026-04-16 as v1)
3. ✅ ~~First deliverable: `vfd predict proton_radius` works end-to-end.~~
4. **v1.1 in progress** — see `v1.1-scope.md` in this folder. Goal:
   lift coverage from 11 to ~25 predictions by adding Paper V's
   full mass spectrum, electric charge assignments, proton magnetic
   radius, magnetic moments (or honest gap entries), generation
   count, and sampled form-factor points.
5. v1.2+ adds hadronic resonances, bosons beyond tree-level, and
   the CKM/PMNS/neutrino claims if the framework derives them.

---

## Appendix A: What makes this "credible" rather than "another project folder"

A physicist opening this repo today sees 33 papers and 47 scripts.
Credibility requires three things the current state lacks:

1. **One command reproduces every claim.** `vfd verify` is that
   command. Without it, every external reviewer has to trust or
   spot-check. With it, reproducibility is a yes/no fact.

2. **Every claim has a σ-margin against experiment.** The registry
   forces every prediction to carry an experimental comparison with
   a cited source. Analytical hand-waves are not registrable.

3. **Inconsistency is visible, not hidden.** The DAG walker means
   "if I change X, does Y still hold?" is a machine-answerable
   question. A framework that cannot answer this is a collection of
   stories; one that can, is a theory.

The Explorer is the machine that makes VFD a theory by the standards
a reviewer uses, not just by internal consistency.

---

## Appendix B: Open questions surfaced during planning

- **Gravity numerics.** Papers XXIII–XXVIII derive spacetime /
  metric / curvature from event-order geometry analytically. What is
  the first numerical claim we can extract and register?
- **Neutron charge radius squared.** Sign and magnitude of
  ⟨r²⟩ ≈ −0.1161 fm² is a stringent test. Does Paper XXXII's
  machinery reproduce the sign?
- **Deuteron (6+α) fit.** Paper XXXII claims 0.02σ. Which specific
  integer invariants enter? Register them as primitives, not buried
  constants.
- **Baryon asymmetry.** Listed as an open problem in the inventory.
  Not a v1 target but worth a registry entry marked "open."
- **Higgs mass / W / Z.** Are these in Paper V's 13 masses, or
  separate? Coverage matrix needs to be explicit.

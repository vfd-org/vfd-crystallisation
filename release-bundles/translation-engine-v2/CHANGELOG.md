# Changelog

## [0.3.0-prototype] — 2026-05-29

**SAGE integration working with real Hecke data.**

### Added

- `sage_scripts/compute_brandt_level31.sage` — SAGE script
  computing Brandt module + Hecke matrices over Q, plus prime
  structure of Q(√5). Verified on SAGE 9.0 (Ubuntu 20.04 apt).
- `data/brandt_level31.json` — 15 genuine Hecke matrices for
  primes p ∈ {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
  43, 47} from BrandtModule(31, 1).
- `examples/run_v600_real_hecke.py` — engine v0.3 runner that
  ingests SAGE data, verifies Hecke commutativity, extends
  Dirichlet coefficients by multiplicativity, locates
  candidate L-function zeros, applies calibrated deep checks.

### Verified

- Real Hecke commutativity: max ||[T_p, T_q]|| < 1e-12 across
  105 prime pairs. EXACT verdict.
- Multiplicativity extension: 78 coefficients to n ≤ 200 from
  15 prime Hecke traces.
- Engine pipeline runs end-to-end on real SAGE data.

### Known scope

- BrandtModule(31, 1) is over Q, not the icosian quaternion
  algebra over Q(√5). SAGE 9.0 doesn't implement number-field
  BrandtModule.
- A near-coincidence appeared: Brandt L-zero at γ ≈ 32.963 vs
  Riemann zero #5 at 32.935 (Δ = 0.028). Probably a truncation
  artefact; needs higher-precision Mellin to confirm.
- The icosian-specific computation requires SAGE 10+ which
  supports `BrandtModule` over number fields.

### Next milestone (v0.4)

Upgrade to SAGE 10+ via conda-forge or build-from-source, run
the same pipeline with `BrandtModule` over Q(√5) and the
icosian quaternion algebra. This is a 1-day SAGE exercise once
the version is in place.

## [0.2.0-prototype] — 2026-05-29

**Deep admissibility + calibrated checks.**

### Added

- `code/deep_admissibility.py`: four deep classes —
  FUNCTIONAL_EQUATION_RESPECTED, DENSITY_CONSISTENT,
  GUE_DISTRIBUTED, HECKE_MULTIPLICATIVE.
- `code/deep_admissibility_calibrated.py`: N-aware versions
  with KS tests against tabulated γ_n and GUE CDF.
- `code/dictionary.py`: 12 typed dictionary entries (4
  substrate + 8 analytic — completed_L, zero_count_N_T,
  pair_correlation, explicit_formula, selberg_class_S,
  hecke_T_p, brandt_matrix, sato_tate_measure,
  U_symmetry_class).
- `examples/run_v600_deep_diagnostic.py`: original deep check
  diagnostic.
- `examples/run_v600_calibrated_diagnostic.py`: calibrated
  version. Correctly identifies γ_n itself as
  HILBERT_POLYA_STRONG.
- `docs/grammar_dictionary_complete.md`: full grammar /
  dictionary reference.
- `docs/sage_integration_spec.md`: precise spec for v0.3
  (later realised below at v0.3.0).

## [0.1.0-prototype] — 2026-05-29

Initial prototype release.

### New transformation kinds (5)

- `HECKE_LIFT`: prototype Hecke operator T_p constructed with
  Eichler–Brandt target eigenvalues for split / inert / ramified
  primes of Z[φ].
- `MODULAR_EMBED`: records the Hilbert modular surface context
  (H × H) / SL₂(O_K) for K = Q(√5).
- `ANALYTIC_EXTEND`: numerical Mellin/Dirichlet candidate analytic
  continuation with zero-line scanning.
- `SPECTRAL_LIFT_INFINITE`: direct-sum prototype of infinite-dim
  spectral extension via 1/k scaling.
- `TRACE_FORMULA_CLOSE`: Selberg-style spectral-geometric trace
  identity check on first 3 power traces.

### New admissibility classes (4)

- `SPECTRAL_MATCH`: RMSE-based verdict comparing operator eigenvalues
  to γ_n target.
- `ZERO_LINE_FORCED`: zero-spacing coefficient-of-variation check on
  candidate analytic continuation.
- `HECKE_COMPATIBLE`: pairwise commutator norm against Hecke
  operators.
- `MODULAR_INVARIANT`: invariance check under substrate action
  generators.

### Search infrastructure

- `code/search.py`: composition search over base operator + Hecke
  pool, with ranked candidate output.

### V_600 example

- `examples/run_v600_search.py`: applies the extended engine to
  V_600's 26-dim Galois-paired block.
- Best current result: CANDIDATE verdict at RMSE 7.97 with 14-feature
  least-squares fit.

### Scope discipline

- Prototype implementations of Hecke / Modular / Analytic-Extend are
  structural scaffolds, not full mathematical implementations.
- The bundle demonstrates the **architecture** works; the
  **mathematics inside the kinds** is the next research work.
- No claim of constructing the Hilbert–Pólya operator T.

### Next milestones

- 0.2.0: replace prototype Hecke matrix construction with genuine
  Hecke action on a small space of Hilbert modular forms over Q(√5)
  (via SAGE / Pari interface).
- 0.3.0: implement verifiable analytic continuation with
  functional-equation symmetry checks.
- 0.4.0: full SELBERG_TRACE admissibility class with explicit
  geometric-side prime-ideal sums.
- 1.0.0: production release with all prototype kinds replaced by
  mathematically verified implementations.

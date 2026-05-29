# Changelog

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

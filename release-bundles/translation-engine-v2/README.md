# Translation Engine v2

**Bridging the finite algebraic substrate (V₆₀₀, icosian triad,
closure operator) to the infinite-dimensional analytic side
(Hilbert modular forms, Hecke operators, analytic continuation).**

Current version: **v0.3-prototype** (working with real SAGE Hecke data)

## Quick status

- **v0.1** — engine architecture (5 new transformation kinds, 4 new
  admissibility classes, composition search). Architectural validity
  demonstrated.
- **v0.2** — deep admissibility (FE / DN / GUE / Hecke
  multiplicativity) + N-aware calibrated checks. Engine correctly
  identifies γ_n itself as HILBERT_POLYA_STRONG.
- **v0.3** — SAGE integration. Real Hecke matrices from
  BrandtModule(31, 1) computed by SAGE 9.0 and fed to the engine.
  Hybrid probe combining SAGE Hecke + V₆₀₀'s 26-dim block reaches
  **HILBERT_POLYA_PARTIAL** (passes FE + GUE at CANDIDATE).
- **v0.4** (next) — SAGE 10+ upgrade for icosian-specific BrandtModule
  over Q(√5).

## What this bundle adds to the existing engine

The original closure transformation engine has:
- 12 finite transformation kinds (DUAL, SHELL_PROJECTION, etc.)
- 5 admissibility classes (EXACT, CANDIDATE, APPROXIMATE, BROKEN,
  DEGENERATE)

This bundle adds:

### Five new transformation kinds

| Kind | Input | Output | Status |
|---|---|---|---|
| `HECKE_LIFT` | substrate + prime p | candidate T_p operator | prototype (uses Eichler–Brandt target eigenvalues) |
| `MODULAR_EMBED` | substrate | Hilbert modular surface context | metadata-level, full |
| `ANALYTIC_EXTEND` | finite spectrum | Mellin/Dirichlet analytic continuation | numerical proxy |
| `SPECTRAL_LIFT_INFINITE` | finite operator | N-truncated infinite-dim extension | direct-sum prototype |
| `TRACE_FORMULA_CLOSE` | operator + geometric data | Selberg-style spectral-geometric balance check | first 3 power-traces |

### Four new admissibility classes

| Class | Test |
|---|---|
| `SPECTRAL_MATCH` | Eigenvalues approximate γ_n target (RMSE-based verdict) |
| `ZERO_LINE_FORCED` | Candidate analytic continuation has zeros on Re(s) = 1/2 |
| `HECKE_COMPATIBLE` | Operator commutes with Hecke operators (pairwise commutator norm) |
| `MODULAR_INVARIANT` | Invariance under given substrate action generators |

### Composition search infrastructure

`code/search.py` provides systematic search over compositions of
transformations, scoring each candidate against admissibility classes.

## Bundle structure

```
translation-engine-v2/
  code/
    __init__.py
    transformation_kinds.py     # five new transformation kinds
    admissibility.py            # four new admissibility classes
    search.py                   # composition-search engine
  examples/
    run_v600_search.py          # apply to V_600's 26-dim block
  outputs/
    search_results.txt          # ranked search candidates
  docs/                         # design notes
  tests/                        # unit tests (skeleton)
  README.md
  CHANGELOG.md
  LICENSE
```

## What the v600 search shows

Running `examples/run_v600_search.py` produces ranked candidates for
the search:

> Find a composition of base-operator powers and prototype Hecke
> operators whose spectrum on V₆₀₀'s 26-dim Galois-paired block
> matches the first 26 Riemann γ_n.

Sample output (current prototype):

| Rank | Composition | RMSE | Verdict |
|---|---|---|---|
| 1 | LS-fit(base, base², T₂...T₃₇) | 7.97 | CANDIDATE |
| 2 | T₂₃ + T₃₇ | 20.9 | WEAK |
| 3 | T₁₇ + T₃₇ | 23.5 | WEAK |
| ... | ... | ... | ... |

The CANDIDATE verdict at RMSE ~8 reflects that a 14-feature
least-squares fit can approximate γ_n to ~10% relative error using
our prototype Hecke operators. An EXACT verdict (RMSE → 0 without
free parameters) would require:

1. Real Hecke operators on Hilbert modular forms over Q(√5), not
   prototype eigenvalues.
2. Verifiable Hecke commutation relations on the 26-dim block.
3. Analytic continuation verification through the critical strip.

These extensions are well-scoped research work; the architecture
supports adding each piece without redesigning the framework.

## What "extending to a full translation tool" means

The framework's design lets you add new transformation kinds and
admissibility classes incrementally, each as a typed module with a
verdict function. The composition search engine then automatically
incorporates them. This means future research can proceed as:

1. Identify a new transformation kind needed (e.g., specific Hecke
   matrix elements from Pari/GP or Sage).
2. Implement it as a new entry in `transformation_kinds.py` with
   typed input/output.
3. Add any new admissibility checks to `admissibility.py`.
4. Re-run `search.py` with the extended grammar.
5. Examine the ranked candidates for EXACT-verdict matches.

Each iteration is small and testable. The architecture is right; the
content needs the mathematics filled in.

## Honest scope statement

The current prototype's Hecke implementations are **structural
placeholders** using Eichler–Brandt-derived target eigenvalues, not
genuine Hecke matrix elements on Hilbert modular forms. The
`HECKE_LIFT` outcome returns a Hermitian matrix with the right
eigenvalue magnitude but the wrong eigenvectors (orthonormal random
basis). This is sufficient to demonstrate that the **architecture
works**; it is not sufficient to test whether a real T exists.

The next step — replacing prototype Hecke operators with genuine
Hilbert modular Hecke action computed against the substrate's irrep
decomposition — is the real research work the architecture enables.

## Status

Pre-peer-review open research prototype. The architecture is real and
runnable. The mathematics inside the transformation kinds is
intentionally minimal — enough to demonstrate the framework, not
enough to settle anything about γ_n.

## Companion bundles

- `vfd-org/icosian-triad-v600` — the math anchor.
- `vfd-org/closure-picture` — the programme-wide synthesis.
- `release-bundles/translation-layer` — the original dictionary/
  grammar/translation paper this engine is the operational version of.
- `release-bundles/critical-line-pullback` — the 8 findings + 10 sims
  that established the substrate-side picture; this engine is the
  next direction.

## Licence

CC BY 4.0 (prose) / Apache 2.0 (code). See `LICENSE`.

# Complete Grammar and Dictionary (engine v0.2)

This document lists every transformation kind, admissibility class,
and dictionary entry currently in the engine. Use it as the
authoritative reference for what the engine can and cannot reason
about.

## Layer 1: Vocabulary (substrate primitives)

| Entry ID | Substrate object | Math referent |
|---|---|---|
| V_600 | 120 unit icosian quaternions | Vertex set of 600-cell; 2I as binary icosahedral group |
| V_24 | 2T = 24 sigma-fixed vertices | 24-cell vertex set; fundamental coset block in Schlaefli |
| A_1 | Edge-adjacency operator on V_600 | 120x120 graph operator; defines L = 12 I − A_1 |
| 9 A_1 eigenvalues | {12, 6φ, 4φ, 3, 0, −2, 4−4φ, −3, 6−6φ} | mults (1,4,9,16,25,36,9,16,4) summing to 120 |
| Z[phi] | Ring of integers of Q(sqrt 5) | Where C_phi spectrum and Hecke eigenvalues live |

## Layer 2: Grammar (substrate side)

| Entry ID | Object | Role in grammar |
|---|---|---|
| C_phi | Closure operator L + φ⁻²·I | Self-adjoint; induces 94+13+13 split; positive |
| N_H | Generation operator I → Z[φ] | Quaternary norm form; universal for tot.-pos. primes |
| tau_galois | Galois sigma: φ → 1−φ on spectrum | The "repetition" that gives 94+13+13 |
| Schlaefli_5_cosets | V_600 = 5 × 24-cell cosets | First grammar primitive |
| lambda_12_lift | per-coset λ=12 eigvec lift to V_600 | Positive grammar rule |
| lambda_12_uniqueness | only (2T, 12) opens full lift channel | Negative grammar rule |
| Galois pairs (3,3') | A_5 irrep pair, 3D level | Source of the 13+13 |
| Spin (2,2') | 2I-only irrep pair, 4D-new | Adds 4+4 to each "13" |

## Layer 2: Grammar (analytic side, v0.2 additions)

| Entry ID | Object | Role in grammar |
|---|---|---|
| completed_L | Lambda(s) = π^(−s/2) Γ(s/2) ζ(s) | Functional equation s ↔ 1−s |
| zero_count_N_T | N(T) ~ (T/2π)log(T/2π) − T/(2π) | Spectral density target |
| pair_correlation | Montgomery's R(α) ~ 1 − (sin πα/πα)² | GUE pair correlation |
| explicit_formula | Sum over zeros = sum over primes | Weil identity (strongest constraint) |
| selberg_class_S | Axiomatic class of L-functions | L_sub belongs to S |
| hecke_T_p | Hecke operator at prime p of Z[φ] | The missing transformation kind |
| brandt_matrix | Finite-dim Hecke action from ideal classes | Computable in SAGE |
| sato_tate_measure | Semicircular Hecke distribution | Secondary test |
| U_symmetry_class | Random-matrix unitary class | ζ belongs to U |

## Transformation kinds (full list)

### Original 12 (engine v0.1, from closure_transform_engine)

| Kind | Input | Output |
|---|---|---|
| DUAL | closed graph | dual graph |
| SHELL_PROJECTION | decorated graph | sub at shell |
| BOUNDARY_PROJECTION | decorated graph | boundary subgraph |
| SPECTRAL_PROJECTION | decorated graph | eigenspace projection |
| CYCLE_PROJECTION | decorated graph | cycle subgraph |
| QUOTIENT | graph + equivalence | quotient graph |
| SUBGROUP_RESTRICTION | graph + subgroup | invariant subgraph |
| EDGE_CONTRACTION | graph + edge | contracted graph |
| VERTEX_DELETION | graph + vertex | deleted graph |
| EDGE_DELETION | graph + edge | deleted graph |
| DIMENSIONAL_LIFT | low-dim closed | higher-dim candidate |
| DIMENSIONAL_PROJECTION | high-dim closed | lower-dim candidate |

### Translation-engine v0.1 additions (analytic bridge)

| Kind | Status |
|---|---|
| HECKE_LIFT | Prototype (Eichler–Brandt target eigvals + random eigenvecs); needs SAGE backend |
| MODULAR_EMBED | Metadata-level only (records Hilbert modular surface context) |
| ANALYTIC_EXTEND | Numerical proxy via Mellin/Dirichlet truncated series |
| SPECTRAL_LIFT_INFINITE | Direct-sum prototype via 1/k scaling |
| TRACE_FORMULA_CLOSE | First 3 power-trace comparison; full Selberg trace is next |

### Coming in v0.3 (per SAGE spec)

| Kind | Source |
|---|---|
| HECKE_LIFT_FROM_BRANDT | SAGE Brandt matrices for Q(√5) |
| EXPLICIT_FORMULA_VERIFY | Weil identity check with explicit test functions |
| GUE_NORMALISE | Rescale spectrum to GUE convention |

## Admissibility classes (full list)

### Original 5 (engine v0.1)

EXACT, CANDIDATE, APPROXIMATE, BROKEN, DEGENERATE

### Translation-engine v0.1 additions (basic analytic)

| Class | Check |
|---|---|
| SPECTRAL_MATCH | RMSE of eigenvalues vs γ_n |
| ZERO_LINE_FORCED | Spacing coefficient of variation |
| HECKE_COMPATIBLE | Pairwise Hecke commutator Frobenius norm |
| MODULAR_INVARIANT | Action invariance under given generators |

### v0.2 additions (deep / calibrated)

| Class | Check |
|---|---|
| FUNCTIONAL_EQUATION_RESPECTED | Sign-symmetric spectrum, or positive-half FE-compatible (calibrated) |
| DENSITY_CONSISTENT | KS test against tabulated γ_n with N-adaptive threshold |
| GUE_DISTRIBUTED | KS test against GUE CDF with N-adaptive threshold |
| HECKE_MULTIPLICATIVE | λ(mn) = λ(m)λ(n) for coprime m,n |

### Coming in v0.3

| Class | Source |
|---|---|
| SELBERG_CLASS_S_VERIFIED | Axiomatic check against the four Selberg axioms |
| EXPLICIT_FORMULA_RESPECTED | Weil identity within tolerance over test functions |
| HILBERT_POLYA_STRONG | Composite: pass FE+DN+GUE at STRONG+ |
| HILBERT_POLYA_CANDIDATE | Composite: pass FE+DN+GUE at CANDIDATE+ |

## Search strategies (current)

The engine's search engine (`code/search.py`) enumerates:

1. Base operator and its powers (k=1..6)
2. Each Hecke operator alone
3. Pairwise sums: base + T_p
4. Pairwise Hecke sums: T_p + T_q
5. Least-squares fit over all features

Each candidate is scored on SPECTRAL_MATCH. v0.2 adds scoring on
FE, DN, GUE via the calibrated deep checks. v0.3 will add
explicit_formula verification and goal-directed proposals.

## What this grammar lets the engine REJECT

Before v0.2: anything that didn't have approximately the right
eigenvalue magnitudes was rejected. But that's almost no signal —
random Hermitians easily pass.

After v0.2 (calibrated): rejection is much sharper. Operators are
rejected if any of:
- Spectrum not sign-symmetric (FE BROKEN)
- Density not following Riemann-Hardy-Littlewood (DN BROKEN)
- Spacings not GUE-distributed (GUE BROKEN)

This means the search effectively prunes to a far smaller subset.

## What this grammar STILL cannot do

- Compute genuine Hecke matrix elements (needs SAGE — v0.3)
- Verify explicit formula identities (needs test function table — v0.4)
- Drive goal-directed search (needs closure_ai integration — v0.5)
- Handle truly infinite-dim spaces (always a truncation; needs
  asymptotic analysis — research-grade work)

## The bottom line

Engine v0.2 has all the grammar AND admissibility infrastructure
needed for a serious Hilbert–Pólya search. The remaining piece —
v0.3 — is wiring in SAGE so the search uses genuine Hecke
operators rather than prototype scaffolds.

Once 0.3 is done, the search either finds a candidate (publish
immediately) or fails systematically (publish the specific
obstruction). Either is a real result.

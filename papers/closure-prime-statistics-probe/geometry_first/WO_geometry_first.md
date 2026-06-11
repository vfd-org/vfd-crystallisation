# WO_geometry_first — eigenspace fingerprinting of A_{V_600}

**Goal.** Produce a data table that uniquely fingerprints each of the 9 eigenspaces of the standard adjacency matrix `A_{V_600}` by `(dimension, trace-vector under a fixed list of W(H_4) generators)`. No interpretation. No framework narrative.

## 1. Construction (numpy only; no group-theoretic libraries)

Let `phi = (1 + sqrt(5)) / 2`.

**1.1 Build V_600 as 120 unit quaternions** (the icosian group `2I`):
- 8 quaternions: `(+/-1, 0, 0, 0)` and permutations.
- 16 quaternions: `(+/- 1/2, +/- 1/2, +/- 1/2, +/- 1/2)` (all sign combos).
- 96 quaternions: even permutations of `(0, +/- 1/2, +/- phi/2, +/- 1/(2*phi))` with all sign combos.

Verify `|V_600| = 120` and every vertex has norm 1 (tolerance `1e-10`).

**1.2 Build the adjacency matrix `A` (120 x 120)**:
- Compute all pairwise Euclidean distances.
- The minimum positive distance `d_min` is the edge length.
- `A[i,j] = 1` if `||v_i - v_j|| < d_min + 1e-8`, else 0; zero the diagonal.
- Verify `A` is symmetric, row-sums are all 12.

**1.3 Diagonalise `A`**:
- Use `numpy.linalg.eigh`.
- Cluster eigenvalues with tolerance `1e-6`; expect 9 clusters with the multiplicities listed in the WO context.
- For each cluster `k`, store `lambda_k`, `dim_k`, and an orthonormal basis `B_k` (a `120 x dim_k` matrix) of the eigenspace.

**1.4 Build W(H_4) generators acting on V_600 by permutation.** Construct the following five 120x120 permutation matrices `P_g` where `P_g[i,j] = 1` iff `g(v_j) = v_i` (matched by Euclidean distance < `1e-8`). Each `g` must map `V_600` to itself; assert that the matching is a bijection.

- `g1` = left quaternion multiplication by `q1 = (1/2, 1/2, 1/2, 1/2)` (order 6, in `2I`).
- `g2` = left quaternion multiplication by `q2 = (1/2, 1/2, phi/2, 1/(2*phi))` after verifying `q2 in V_600` (order-10 element of `2I`).
- `g3` = right quaternion multiplication by `q1`.
- `g4` = the reflection `v -> v - 2 (v . r) r` where `r = (1, -1, 0, 0)/sqrt(2)` (an H_4 simple-root reflection; verify it maps V_600 to itself).
- `g5` = coordinate permutation `(x1, x2, x3, x4) -> (x2, x3, x4, x1)` (a 4-cycle, in W(H_4) as the symmetry permuting the 8 "axis" quaternions).

These five generators, taken together, generate W(H_4) of order 14400 — this is a known fact (left-and-right multiplication by `2I` gives `2I x 2I / {+/-1}` of order 14400, which is exactly W(H_4); g4 and g5 are added as sanity checks and to populate distinct conjugacy classes).

**Note.** We do NOT need to verify that `<g1,...,g5> = W(H_4)` inside the sim — that is a known group-theory fact (Conway-Smith, *On Quaternions and Octonions*, Ch. 4). The sim only needs each `P_g` to be a genuine permutation matrix and to commute with `A` (`P_g A = A P_g`); both are machine-verifiable.

## 2. Required outputs

For `g in {g1, g2, g3, g4, g5}`:
- `cycle_structure_g`: partition of 120 from the cycles of `P_g` (e.g. `[10, 10, 10, ..., 1, 1]`).
- For each eigenspace `k`: `trace_k_g = trace( B_k^T P_g B_k )`.

**Pretty-printed stdout table:**
```
eigenvalue   dim   tr(g1)  tr(g2)  tr(g3)  tr(g4)  tr(g5)
-3.708         4    ...
-3.000        16    ...
... (9 rows total) ...
```

**JSON at `output/geom_first_results.json`** with schema:
```
{
  "vertices_count": 120,
  "edge_degree": 12,
  "eigenvalues": [...],          // 9 floats, sorted
  "eigenspace_dims": [...],      // 9 ints
  "generators": ["g1","g2","g3","g4","g5"],
  "cycle_structures": {"g1":[...], ...},
  "full_traces": {"g1": int, ...},   // trace of P_g on R^120
  "eigenspace_traces": [
    {"eigenvalue": ..., "dim": ..., "traces": {"g1": ..., ...}},
    ...
  ],
  "checks": {
    "eigenspace_dim_sum_equals_120": true/false,
    "trace_sum_matches_full_per_generator": {"g1": true/false, ...},
    "all_generators_commute_with_A": {"g1": true/false, ...},
    "fingerprints_distinct": true/false
  }
}
```

**Forbidden output text:** no mention of `sigma`, "closure", "cascade", "paired", `{1,1,5,5}`, primes, `zeta`, `E_8`, "Galois". The output is a pure linear-algebra table.

## 3. Verification criterion

The sim PASSES iff all four `checks` entries are `true`. "Fingerprints distinct" means the 9 tuples `(dim_k, tr_k_g1, tr_k_g2, tr_k_g3, tr_k_g4, tr_k_g5)` (rounded to nearest int; integrality must itself be verified to tolerance `1e-6`) are all pairwise distinct.

## 4. Next sim (if this passes — out of scope here)

A follow-up WO will: (a) tabulate the 34 W(H_4) irreducible characters from Geck-Pfeiffer App. C piecewise, (b) compute `chi_irrep(g_i)` for each chosen generator, (c) label each eigenspace with its W(H_4)-irrep name by matching fingerprints. That is a SEPARATE work order.

## 5. Out of scope (do NOT do in this WO)

- No `sigma`-Galois action.
- No icosian-ring construction beyond V_600 itself.
- No claim about `{1, 1, 5, 5}`.
- No "closure operator", no cascade reference.
- No E_8 embedding.
- No `zeta_K`, `zeta`, prime counting.
- No interpretation of which eigenspace "means" what.

## 6. Flagged under-specifications

- **(F1)** The claim that `<g1,g2,g3,g4,g5> = W(H_4)` is taken from the literature, not verified inside the sim. If the implementer wants in-sim verification, they would need to enumerate the orbit of the identity under the generated group and check it has size 14400 — feasible but expensive (~10^4 matrices). We do NOT require this; we only require each `P_g` to commute with `A`.
- **(F2)** Whether 5 generators give 9 distinct fingerprints is an empirical question. If they don't, the implementer should add a sixth generator `g6` = left multiplication by `q3 = (phi/2, 1/(2*phi), 1/2, 0)` (verify `q3 in V_600`) and re-run. The acceptance check "fingerprints_distinct: true" must hold for the final generator list, which must be recorded in the JSON.

## Acceptance checklist (machine-verifiable)

The sim's output JSON at `output/geom_first_results.json` MUST satisfy:

- [ ] `vertices_count == 120`
- [ ] `edge_degree == 12`
- [ ] `len(eigenvalues) == 9` and `len(eigenspace_dims) == 9`
- [ ] `sum(eigenspace_dims) == 120`
- [ ] `checks.eigenspace_dim_sum_equals_120 == true`
- [ ] For every `g` in `generators`: `checks.all_generators_commute_with_A[g] == true`
- [ ] For every `g` in `generators`: `checks.trace_sum_matches_full_per_generator[g] == true` (i.e. `sum_k tr_k_g == full_traces[g]`, to integer match after rounding within `1e-6`)
- [ ] Every `trace` value in `eigenspace_traces` is an integer to tolerance `1e-6`
- [ ] `checks.fingerprints_distinct == true`
- [ ] The stdout table has exactly 9 data rows, sorted by eigenvalue ascending
- [ ] The output text contains none of the forbidden tokens: `sigma`, `closure`, `cascade`, `paired`, `prime`, `zeta`, `E_8`, `E8`, `Galois`, `{1,1,5,5}` (case-insensitive search)
- [ ] `cycle_structures[g]` for each `g` is a list of positive ints summing to 120

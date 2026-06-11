# WO_irrep_identification

## Context

`output/geom_first_results.json` (from `WO_geometry_first.md`) gives a
distinct-fingerprint table for the nine eigenspaces of the V_600
adjacency operator A under generators g1..g5 of W(H_4). Dimensions are
(1, 4, 4, 9, 9, 16, 16, 25, 36) summing to 120. All five generators
commute with A (verified), so eigenspaces are W(H_4)-submodules.

This WO identifies each eigenspace with a W(H_4) irrep **without** the
Geck-Pfeiffer character table.

## Inputs

- `output/geom_first_results.json` (read-only).

## Tasks

### 1. Multiplicity-free verification

Compute `⟨χ_perm, χ_perm⟩` = number of W(H_4)-orbits on V_600 × V_600.
Use vertex-transitivity: orbit count equals the number of distinct
squared Euclidean distances from a fixed unit-norm vertex to all 120
vertices. Expected: 9. If different, report the value and the
distance multiset; mark `multiplicity_free=false` and proceed with the
fallback labeling.

### 2. Structural identifications from internal data

Use only the trace table in the JSON.

- **Trivial irrep** (dim 1, traces (+1,+1,+1,+1,+1)). The +12 eigenvalue
  row matches exactly. Label `trivial`.
- **Reflection irrep** (dim 4, natural W(H_4) action on R^4). A
  reflection has character `dim − 2 = +2`; both dim-4 eigenspaces show
  tr(g5)=+2, so g5 alone does not separate them. Apply the secondary
  test on g2 (order 10): in the natural reflection rep g2 acts as a
  pair of planar rotations with character `2cos(2πa/10)+2cos(2πb/10)`
  for the H_4-Coxeter exponent pair. Identify the dim-4 eigenspace
  whose tr(g2) matches this value; the other dim-4 is its outer-tensor
  partner. Report both candidates' tr(g2) and the chosen identification.
- **Same-dim partners.** Label the two dim-9 eigenspaces `irrep_a`,
  `irrep_a'`; the two dim-16 as `irrep_b`, `irrep_b'`; the dim-25 as
  `irrep_c`; the dim-36 as `irrep_d`. No Geck-Pfeiffer names.

### 3. Pair-twist verification

For each same-dim pair output a table
`(generator, tr_E+, tr_E−, sum, diff)`. The classical sign-twist
criterion expects `tr(reflection on E_+) = −tr(reflection on E_−)`. The
data show **all** V_600 eigenspaces have positive tr(g5), so the
1-dimensional sign rep is absent from V_600's permutation rep and the
twin pairs are related by a different automorphism. Accept the pair as
a "twist pair" if **at least one** generator yields opposite signs.
Record the differentiating generator per pair.

## Outputs

1. `output/irrep_identification.md` — markdown table:

   | eigenvalue | dim | fingerprint (tr g1..g5) | irrep_label | structural_id |

2. `output/irrep_identification.json` — per eigenspace: eigenvalue,
   dim, fingerprint, irrep_label, structural_id; plus
   `pair_twist_verification` (the three same-dim pair tables) and
   `inner_product_chi_perm`.

3. Stdout: pretty-printed labeled table.

## Acceptance criteria

- `inner_product_chi_perm` reported; pass if = 9.
- `trivial` placed at eigenvalue +12 with tr=(1,1,1,1,1).
- `reflection` placed at exactly one dim-4 eigenspace by the g2
  secondary test (both candidates shown).
- Each same-dim pair has at least one generator with opposite-sign
  traces; the generator is recorded.
- All 9 eigenspaces carry a non-empty `irrep_label`.
- File contains none of the tokens: `sigma`, `closure`, `cascade`,
  `paired`, `prime`, `zeta`, `E_8`, `E8`, `Galois`, `{1,1,5,5}`
  (outside the acceptance/out-of-scope listings).

## Out of scope

- Geck-Pfeiffer table lookups; named-irrep imports.
- Claims about ẑ poles, primes, zeta-function structure, or
  cascade-narrative content.
- Generators beyond g1..g5.

## Fallback

If `⟨χ_perm, χ_perm⟩ ≠ 9`, mark `multiplicity_free=false`, record the
actual value and distance multiset, and label eigenspaces by
(dim, fingerprint) only.

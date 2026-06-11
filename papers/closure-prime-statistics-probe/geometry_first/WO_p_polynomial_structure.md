# WO #5: P-Polynomial Structure of V_600 and Intersection Array

## Context

Step 4 established V_600 as a symmetric association scheme on 9
classes with palindromic valencies (1, 12, 20, 12, 30, 12, 20, 12, 1)
and multiplicities (1, 4, 9, 16, 25, 36, 9, 16, 4), all intersection
numbers p_{ij}^k integer non-negative, all Krein parameters q_{ij}^k
non-negative real. The codex review of step 4 surfaced two structural
features: (i) V_600 is **P-polynomial in A_1**, since A_1 has 9
distinct eigenvalues, so every shell operator A_i is uniquely
expressible as a polynomial p_i(A_1) of degree exactly i; and (ii)
the central character P[8, ·] = (+1, −1, +1, −1, +1, −1, +1, +1, −1)
pairs each same-dim eigenspace pair by a sign-flip pattern, consistent
with χ ↔ χ · sign on the eigenspace level.

This WO computes the explicit polynomial reduction A_i = p_i(A_1),
extracts the classical intersection array {b_0, ..., b_{d−1};
c_1, ..., c_d}, and tabulates the antipodal-pairing signs.

## Task

Build `sim_p_polynomial_structure.py` performing the following.

### 1. Re-derive spectral data of A_1

- Reload V_600, the 9 shell operators A_0 = I, A_1, ..., A_8, the
  P-eigenmatrix (9×9), the valencies k_i, and the multiplicities f_j
  from the step-4 outputs.
- Extract the 9 distinct eigenvalues (λ_0, λ_1, ..., λ_8) of A_1 in
  the canonical row-order of the P-matrix (so P[1, j] = λ_j).
- Confirm |{λ_j}| = 9 (all distinct), and λ_0 = k_1 = 12.

### 2. Polynomial reduction A_i = p_i(A_1)

For each i ∈ {0, 1, ..., 8}:

- Construct the 9-point Lagrange interpolant p_i(x) of degree ≤ 8
  satisfying p_i(λ_j) = P[i, j] for j = 0, ..., 8.
- Equivalently, solve the 9×9 Vandermonde system V · c_i = P[i, :]
  with V[j, k] = λ_j^k, recovering the monomial-basis coefficient
  vector c_i ∈ R^9.
- Compute the matrix polynomial Ã_i := Σ_k c_i[k] · A_1^k and check
  max |Ã_i − A_i| < 1e-8.
- Verify deg(p_i) = i, i.e. c_i[k] ≈ 0 for k > i (tol 1e-8) and
  c_i[i] is non-zero.
- Attempt rational/Z[φ] recognition of each c_i[k]: write
  c_i[k] = a + b · φ with φ = (1 + √5)/2 and report (a, b) when
  both are within 1e-10 of rationals with small denominator
  (≤ 10^6). Otherwise record the float and flag.

### 3. Intersection array {b_i, c_i}

For a P-polynomial scheme of diameter d = 8, the three-term recurrence
on the polynomials is

    x · p_i(x) = c_{i+1} · p_{i+1}(x) + a_i · p_i(x) + b_{i−1} · p_{i−1}(x)

with a_i + b_i + c_i = k_1 = 12 and the boundary conditions
b_{−1} = c_0 = 0, c_{d+1} undefined. Read these constants directly
from the intersection numbers computed in step 4:

- b_i := p_{1, i+1}^i  for i = 0, ..., 7  (forward step)
- c_i := p_{1, i−1}^i  for i = 1, ..., 8  (backward step)
- a_i := p_{1, i}^i = 12 − b_i − c_i      (loop term)

Record b_0, b_1, ..., b_7 and c_1, c_2, ..., c_8 as integer arrays.
Verify k_i = (b_0 · b_1 · ... · b_{i−1}) / (c_1 · c_2 · ... · c_i)
(standard valency recursion) for all i to tol 1e-8.

### 4. Three-term recurrence verification

For each i ∈ {0, ..., 7} and each eigenvalue λ_j:

    R[i, j] := λ_j · p_i(λ_j) − c_{i+1} · p_{i+1}(λ_j)
                              − a_i · p_i(λ_j)
                              − b_{i−1} · p_{i−1}(λ_j)

with p_{−1} := 0, p_9 := 0 at the boundary. Acceptance: max |R| < 1e-8
across the full 8 × 9 grid.

### 5. Central-character pairing

The antipodal map is A_8 (single antipode per vertex; k_8 = 1). Its
eigenvalues P[8, j] ∈ {+1, −1} partition the 9 eigenspaces into a
+1 set and a −1 set. For each same-dim pair identified in step 2:

- dim-4 pair (j_a, j_b): record (P[8, j_a], P[8, j_b])
- dim-9 pair (j_a, j_b): same
- dim-16 pair (j_a, j_b): same
- dim-25 singleton, dim-36 singleton, dim-1 singleton: record sign
  alone.

Check whether each same-dim pair has opposite P[8, ·] signs (the
"χ ↔ χ · sign" pattern). Report the 9-vector P[8, :] and the
pairing table.

### 6. Acceptance criteria (all must be machine-true)

1. A_1 has 9 distinct eigenvalues.
2. For each i ∈ {0, ..., 8}: max |p_i(A_1) − A_i| < 1e-8 and
   deg(p_i) = i.
3. Every monomial-basis coefficient c_i[k] of every p_i is either
   rational or in Z[φ] to within 1e-10; flag otherwise.
4. b_0, ..., b_7 and c_1, ..., c_8 are non-negative integers.
5. Valency recursion k_i = (∏ b_<i) / (∏ c_≤i) holds to tol 1e-8.
6. Three-term recurrence residual max |R[i, j]| < 1e-8.
7. P[8, j] ∈ {+1, −1} for all j, and each same-dim pair (dim-4,
   dim-9, dim-16) carries opposite signs.

### 7. Output

- `output/p_polynomial_results.md`: human-readable tables of
  (a) the 9 polynomials p_0, ..., p_8 in monomial basis with rational
  or Z[φ] coefficients, (b) the intersection array
  {b_0, ..., b_7; c_1, ..., c_8} plus the a_i column, (c) the 8 × 9
  recurrence-residual matrix (should be uniformly < 1e-8), (d) the
  central-character pairing table with P[8, :] and the same-dim
  sign-flip check.
- `output/p_polynomial_results.json`: same content machine-readable,
  plus the seven acceptance booleans.
- Stdout: pretty-print the intersection array, the polynomial degree
  certificate, and the acceptance booleans.

### 8. Out of scope

- No interpretation tokens.
- No appeal to the BCN classification that the intersection array
  uniquely determines V_600.
- No naming of W(H_4) irreps beyond the trivial (E_0) and 4-dim
  reflection (E_1) already identified in steps 1–2.
- No claim that the antipodal sign pattern *is* the sign character
  of any specific W(H_4) irrep; only that the pairs invert sign.

### 9. Flag under-specifications

- If any p_i has an irrational coefficient not in Z[φ] (residual to
  rational + φ-rational > 1e-10), record the float and continue.
- If the intersection array depends on shell ordering: V_600 has 9
  distinct A_1-eigenvalues and palindromic valencies, so the
  diameter-8 ordering by increasing squared distance is unique;
  verify against the step-4 shell indexing.
- If the same-dim sign-flip fails for any pair, record which pair
  and report the actual sign tuple — this would mean the antipodal
  map does *not* pair those two eigenspaces by χ · sign.

---

## Summary

WO #5 upgrades V_600 from an association scheme to an explicit
P-polynomial scheme by Lagrange-interpolating each shell operator
A_i as a degree-i polynomial p_i(A_1) over the 9 distinct
eigenvalues of A_1, then extracting the diameter-8 intersection
array {b_0, ..., b_7; c_1, ..., c_8} (with loop terms a_i = 12 − b_i
− c_i) directly from the intersection numbers p_{1, i±1}^i computed
in step 4. Acceptance is (i) exact matrix polynomial reduction
A_i = p_i(A_1) to tolerance 1e-8 for all i, (ii) rational or Z[φ]
coefficients on every p_i, (iii) non-negative-integer intersection
array satisfying the valency recursion and the three-term recurrence
at all 9 spectral points, and (iv) the antipodal P[8, ·] vector
landing in {±1}^9 with each same-dim pair (dim-4, dim-9, dim-16)
carrying opposite signs, confirming the χ ↔ χ · sign pattern flagged
by codex review of step 4. Output is one markdown table file, one
JSON, and stdout summary; flags reserved for irrational coefficients
or sign-pairing failures.

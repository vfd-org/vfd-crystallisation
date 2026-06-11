# WO #3: Second-Shell Adjacency Operator and Joint Diagonalisation

## Context

Steps 1 and 2 produced 9 distinct A-eigenspaces of V_600 under the
shortest-shell adjacency operator A, with the trivial (+12) and the natural
4-dim reflection irrep (+6φ) identified by structural witness. Three
same-dim pairs remain (dim 4, 9, 16), distinguished only by g_i-character
fingerprints — not by an operator-level witness.

This WO builds a second commuting operator A_2 and verifies that
joint (A, A_2) diagonalisation lifts the residual degeneracy.

## Task

Build `sim_second_shell_operator.py` performing the following.

### 1. Construction of A_2

- Load the 120 V_600 vertices V and the operator A from step 1.
- Compute pairwise squared distances d²(i, j) = ||V[i] - V[j]||².
- Verify the distinct non-zero d² values match
  {0.382..., 1.0, 1.382..., 2.0, 2.618..., 3.0, 3.618..., 4.0}
  (tolerance 1e-8).
- Define A_2 ∈ {0,1}^{120×120} with A_2[i,j] = 1 iff d²(i,j) is within
  1e-8 of the **second-smallest** non-zero value (i.e. 1.0).
- A_2 must be symmetric; row sums must be constant (vertex-transitivity).

### 2. Commutation checks

Machine-verify:

- max |A · A_2 - A_2 · A| < 1e-8
- For each of the 5 W(H_4) generators g_1..g_5 (permutation matrices P_g
  reused from step 1): max |A_2 · P_g - P_g · A_2| < 1e-8

If any check fails, halt and report — A_2 is then not in the centraliser
and the WO cannot proceed.

### 3. Joint diagonalisation

For each of the 9 A-eigenspaces E_λ from step 1, with orthonormal basis
B_λ (dim_λ × 120):

- Form the restriction B_λ := B_λ · A_2 · B_λᵀ (a dim_λ × dim_λ matrix).
- Compute eigenvalues of B_λ (symmetric, so use `eigh`).
- Round to 8 decimals and group by multiplicity to get the A_2-spectrum
  on E_λ.

### 4. Acceptance criteria (all must be machine-true)

1. A_2 commutes with A.
2. A_2 commutes with each P_{g_i}, i = 1..5.
3. For each same-dim A-eigenspace pair (dim 4 pair, dim 9 pair, dim 16
   pair): the two members carry **distinct** A_2-eigenvalue multisets
   (compared as sorted tuples, 8-decimal rounding).
4. Each of the 9 A-eigenspaces is itself an A_2-eigenspace (B_λ is a
   scalar multiple of the identity to tol 1e-8) — i.e. joint
   diagonalisation is complete and (A, A_2) is a CSCO on V_600.

### 5. Output

- `output/second_shell_results.md`: table with columns
  (index, eigenvalue_A, eigenvalue_A_2, dim, A_2_spectrum_on_E_λ).
- `output/second_shell_results.json`: same content, machine-readable,
  plus the four acceptance booleans.
- Stdout: pretty-print the table and the acceptance booleans.

### 6. Out of scope

No Geck–Pfeiffer character tables. No interpretation tokens. No claim
about what any irrep "means" — only that it is now uniquely labelled by
the ordered pair (eigenvalue_A, eigenvalue_A_2).

### 7. Fallback if criterion 4 fails

If some B_λ has a non-trivial A_2-spectrum (i.e. A_2 splits E_λ into
strictly smaller joint pieces but does not fully resolve to dimension 1
labels), document the residual degeneracy and define A_3 as the 0/1
adjacency at the **third**-smallest non-zero squared distance (1.382...).
Re-run commutation and joint-spectrum checks for the triple (A, A_2, A_3).
If still incomplete, escalate shell-by-shell up to A_8 (the 8 non-zero
shells); record the smallest k for which (A, A_2, ..., A_k) is a CSCO.

---

## Summary

WO #3 constructs the second-shell adjacency operator A_2 on V_600 — the 0/1 matrix marking pairs at the second-smallest non-zero squared distance (= 1.0) — verifies it commutes with both the first-shell operator A and the five W(H_4) generators g_1..g_5, then restricts A_2 to each of A's nine eigenspaces and reads off its eigenvalues. The success criterion is that the three residual same-dim pairs (dim 4, 9, 16) acquire distinct A_2-eigenvalues, upgrading the dimension-plus-fingerprint label of step 2 into a structural ordered pair (eigenvalue_A, eigenvalue_A_2) that uniquely tags each of the nine joint eigenspaces. A fallback ladder to A_3..A_8 is specified in case A_2 alone is insufficient to make (A, A_2) a complete set of commuting observables.

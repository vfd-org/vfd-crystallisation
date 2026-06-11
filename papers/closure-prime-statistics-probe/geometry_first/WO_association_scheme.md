# WO #4: Association Scheme Structure of V_600

## Context

Steps 1-3 established that V_600 is a distance-regular graph on 120
vertices with 9 distance classes (squared distances {0, 0.382, 1,
1.382, 2, 2.618, 3, 3.618, 4}), with shell adjacency operators
A_0 = I, A_1 = A, A_2, ..., A_8 all mutually commuting and in the
centraliser of W(H_4). The first-shell operator A has 9 distinct
eigenvalues with eigenspaces of dimensions {1, 4, 4, 9, 9, 16, 16,
25, 36}. The triple (A, A_2, A_3) was shown to be a CSCO: each
A-eigenspace carries a unique (A, A_2, A_3)-eigenvalue triple.

This WO completes the characterisation by computing all classical
association-scheme invariants: the P- and Q-eigenmatrices, the
intersection numbers p_{ij}^k, the Krein parameters q_{ij}^k, the
valencies k_i, and the multiplicities f_j. The success criterion is
that V_600 satisfies the defining axioms of a symmetric association
scheme (Bannai-Ito; Brouwer-Cohen-Neumaier) on the nose.

## Task

Build `sim_association_scheme.py` performing the following.

### 1. Load shell operators and spectral data

- Reuse the 120 V_600 vertices V and the 9 shell operators
  A_0 = I, A_1, ..., A_8 from steps 1-3 (regenerate from V if not
  serialised; squared-distance buckets are deterministic).
- Reuse the 9 A-eigenspaces E_0, ..., E_8 (orthonormal bases B_j)
  and their dimensions f_j ∈ {1, 4, 4, 9, 9, 16, 16, 25, 36}.

### 2. Valencies

- Compute k_i := row-sum of A_i (must be constant across rows by
  vertex-transitivity; verify with tolerance 0).
- Record (k_0, k_1, ..., k_8); confirm k_0 = 1, k_1 = 12, Σ k_i = 120.

### 3. P-matrix (first eigenmatrix)

- For each (i, j) with i, j ∈ {0, ..., 8}: compute
  P[i, j] := scalar eigenvalue of A_i on E_j (verify B_jᵀ A_i B_j is
  a scalar multiple of identity to tol 1e-8; report otherwise).
- Verify P[0, j] = 1 for all j (since A_0 = I).
- Verify P[i, 0] = k_i for all i (trivial eigenspace).

### 4. Q-matrix (second eigenmatrix) and orthogonality

- Compute Q via the classical relation Q = 120 · P^{-1} (standard
  convention with n = |V| = 120).
- Verify P · Q = 120 · I and Q · P = 120 · I to tol 1e-8.
- Verify Q[j, 0] = f_j for all j (trivial-shell dual).
- Verify Q[0, j] = 1 for all j.

### 5. Intersection numbers p_{ij}^k

- For each ordered pair (i, j) compute the matrix product A_i · A_j.
- Express A_i · A_j = Σ_k p_{ij}^k · A_k by solving the linear system
  in the 9-dim Bose-Mesner basis (A_0, ..., A_8 are linearly
  independent since pairwise disjoint as 0/1 supports plus I).
- The constants p_{ij}^k must be **non-negative integers** (classical
  association-scheme axiom). Verify and report.
- Verify the standard identity Σ_k p_{ij}^k = k_i · k_j / k_0 = k_i · k_j
  ... wait, the correct identity is Σ_k p_{ij}^k · k_k = k_i · k_j;
  also p_{ij}^0 = k_i · δ_{ij} and p_{0j}^k = δ_{jk}. Verify all three.

### 6. Krein parameters q_{ij}^k

- From the Q-matrix, compute the Krein parameters via
  q_{ij}^k = (f_i · f_j / n) · Σ_l (Q[l, i] · Q[l, j] · Q[l, k]) / (f_l · ??)
  using the standard formula
  q_{ij}^k = (1/n) · Σ_l (P[l, i] · P[l, j] · conj(P[l, k])) · f_k / (k_l · ??)
  — implement via the textbook identity
  q_{ij}^k = (f_k / n) · Σ_l (Q[l, i] Q[l, j] Q[l, k]) / f_l^2 · f_l
  or equivalently from the dual Bose-Mesner idempotents E*_i ∘ E*_j
  = (1/n) Σ_k q_{ij}^k E*_k where ∘ is entrywise Hadamard product on
  the primitive idempotents E*_i := (1/n) Σ_l Q[l, i] · A_l.
- Compute E*_0, ..., E*_8 as 120×120 matrices.
- Verify entrywise (Hadamard) products E*_i ∘ E*_j expand in the
  E*-basis with coefficients (1/n) q_{ij}^k.
- The constants q_{ij}^k must be **non-negative reals** (Krein
  condition; Scott 1973). Verify and report.

### 7. Acceptance criteria (all must be machine-true)

1. k_i row-sums constant for all i = 0, ..., 8.
2. P · Q = 120 · I and Q · P = 120 · I to tol 1e-8.
3. All p_{ij}^k are non-negative integers (round to nearest integer;
   max |p - round(p)| < 1e-8).
4. Σ_k p_{ij}^k · k_k = k_i · k_j for all (i, j) to tol 1e-8.
5. All q_{ij}^k are non-negative reals to tol 1e-8 (the Krein
   condition).
6. Σ_k q_{ij}^k · f_k = f_i · f_j for all (i, j) to tol 1e-8 (Krein
   dual of valency identity).

### 8. Output

- `output/association_scheme.md`: human-readable tables of (k_i),
  (f_j), the 9×9 P matrix, the 9×9 Q matrix, the six 9×9 slices of
  p_{·,·}^k for k = 0..8, and the six 9×9 slices of q_{·,·}^k.
- `output/association_scheme.json`: machine-readable arrays
  k_i, f_j, P, Q, p[i][j][k], q[i][j][k], plus the six acceptance
  booleans.
- Stdout: pretty-print (k_i), (f_j), P, Q, and the acceptance
  booleans.

### 9. Out of scope

- No interpretation tokens. The numbers are structural invariants of
  V_600's distance-regular graph.
- No comparison with the Geck-Pfeiffer character table of W(H_4).
- No claim about what any p_{ij}^k or q_{ij}^k "means" beyond the
  axioms it satisfies.

### 10. Flag under-specifications

- If any p_{ij}^k is non-integer (max |p - round(p)| ≥ 1e-8), report
  it: V_600 would then not be a *pure* symmetric association scheme
  but a generalisation (e.g. a coherent configuration with fractional
  structure constants).
- If any q_{ij}^k is strictly negative beyond tolerance, report it
  as a classical Krein-condition violation. This would constrain the
  scheme's combinatorial type sharply (Krein violation rules out
  most known infinite families).
- If P · Q deviates from 120 · I, the eigenspace bases are
  ill-conditioned; halt.

---

## Summary

WO #4 promotes V_600 from "distance-regular graph with a CSCO" to
the full classical structure of a symmetric **association scheme** on
9 classes. It computes the P-eigenmatrix (eigenvalues of each shell
operator A_i on each A-eigenspace E_j), the dual Q-eigenmatrix
(verified by P·Q = 120·I), the 729 intersection numbers p_{ij}^k as
structure constants of the 9-dimensional Bose-Mesner algebra
spanned by (A_0, ..., A_8), and the 729 Krein parameters q_{ij}^k as
their dual obtained via the primitive idempotents. Acceptance is
non-negative-integer p_{ij}^k, non-negative-real q_{ij}^k (the Krein
condition), and the two scalar identities Σ_k p_{ij}^k k_k = k_i k_j
and Σ_k q_{ij}^k f_k = f_i f_j. Output is one human-readable
markdown table file and one machine-readable JSON, with under-
specification flags reserved for the cases of non-integer
intersection numbers (coherent-configuration generalisation) or
Krein violation (classical anomaly).

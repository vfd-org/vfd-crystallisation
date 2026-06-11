# Irrep identification of V_600 eigenspaces

Multiplicity-free check: ⟨χ_perm, χ_perm⟩ = 9
  (multiplicity-free iff = 9: **True**)

λ_reflection (from coordinate functionals A·u_a = λ·u_a) = 9.708204
  Equals 6φ = 9.708204: **True**

## Labeled eigenspace table

| eigenvalue | dim | fingerprint (tr g1..g5) | label | structural id |
|---|---|---|---|---|
| -3.7082 | 4 | (+2, +3, +2, +0, +2) | `unidentified_dim4_eig-3.708` | dim-4 W(H_4) irrep at eigenvalue -3.7082 (not yet identified with named irrep) |
| -3.0000 | 16 | (+4, -4, +4, +0, +4) | `unidentified_dim16_eig-3.000` | dim-16 W(H_4) irrep at eigenvalue -3.0000 (not yet identified with named irrep) |
| -2.4721 | 9 | (+0, +5, +0, -3, +3) | `unidentified_dim9_eig-2.472` | dim-9 W(H_4) irrep at eigenvalue -2.4721 (not yet identified with named irrep) |
| -2.0000 | 36 | (+0, -6, +0, +0, +6) | `unidentified_dim36_eig-2.000` | dim-36 W(H_4) irrep at eigenvalue -2.0000 (not yet identified with named irrep) |
| -0.0000 | 25 | (-5, +0, -5, +5, +5) | `unidentified_dim25_eig-0.000` | dim-25 W(H_4) irrep at eigenvalue -0.0000 (not yet identified with named irrep) |
| +3.0000 | 16 | (-4, +4, -4, +0, +4) | `unidentified_dim16_eig+3.000` | dim-16 W(H_4) irrep at eigenvalue +3.0000 (not yet identified with named irrep) |
| +6.4721 | 9 | (+0, -2, +0, -3, +3) | `unidentified_dim9_eig+6.472` | dim-9 W(H_4) irrep at eigenvalue +6.4721 (not yet identified with named irrep) |
| +9.7082 | 4 | (+2, -1, +2, +0, +2) | `reflection` | natural W(H_4) rep on R^4; eigenvalue 6φ from coord functionals |
| +12.0000 | 1 | (+1, +1, +1, +1, +1) | `trivial` | 1-dim trivial rep (all traces +1) |

## Pair-twist verification

### dim-4 pair
- Eigenvalues: [-3.708203932499371, 9.708203932499357]
- Generators with opposite-sign traces: ['g2']
- Twist verified: **True**

### dim-16 pair
- Eigenvalues: [-3.0000000000000027, 2.999999999999995]
- Generators with opposite-sign traces: ['g1', 'g2', 'g3']
- Twist verified: **True**

### dim-9 pair
- Eigenvalues: [-2.4721359549995823, 6.472135954999577]
- Generators with opposite-sign traces: ['g2']
- Twist verified: **True**

# V_600 P-polynomial structure

- A_1 has 9 distinct eigenvalues; V_600 is P-polynomial in A_1.
- Eigenvalues (E_0..E_8 descending): +12.0000, +9.7082, +6.4721, +3.0000, -0.0000, -2.0000, -2.4721, -3.0000, -3.7082

## Polynomials p_i(x)

Each shell operator A_i = p_i(A_1).

| i | degree | p_i(x) coefficients (constant..x^i) |
|---|---|---|
| 0 | 0 | 1 |
| 1 | 1 | 0.0000, 1 |
| 2 | 8 | -4, -16.4875, -6.3945, 3.0454, 1.0538, -0.2186, -0.0298, 0.0070, -0.0003 |
| 3 | 8 | -0.0000, 44.4626, 20.1836, -9.1363, -3.1613, 0.6558, 0.0895, -0.0211, 0.0009 |
| 4 | 8 | 6, -71.5353, -32.9527, 14.5368, 4.9839, -1.0316, -0.1419, 0.0333, -0.0015 |
| 5 | 8 | -0.0000, 75.1939, 32.6020, -14.7947, -5.0973, 1.0388, 0.1501, -0.0345, 0.0015 |
| 6 | 8 | -4, -24.3188, -10.4557, 4.7718, 1.8737, -0.3487, -0.0616, 0.0132, -0.0006 |
| 7 | 8 | 0.0000, -18.4797, -6.0873, 3.6282, 0.8224, -0.2244, -0.0181, 0.0055, -0.0003 |
| 8 | 8 | 1, 10.1458, 3.0871, -2.0522, -0.4724, 0.1291, 0.0116, -0.0034, 0.0002 |

## Intersection array

{b_0..b_7; c_1..c_8} = {12, 5, 3, 5, 2, 5, 3, 1; 1, 3, 5, 2, 5, 3, 5, 12}

## Central-character pairing

| pair_dim | j0 | j1 | P[8, j0] | P[8, j1] | opposite_sign |
|---|---|---|---|---|---|
| dim_4 | 1 | 8 | -1 | -1 | False |
| dim_9 | 2 | 6 | +1 | +1 | False |
| dim_16 | 3 | 7 | -1 | +1 | True |

## Acceptance
- `A_1_has_9_distinct_eigenvalues`: **True**
- `all_p_i_evaluate_to_A_i`: **True**
- `intersection_array_nonneg_integer`: **True**
- `valency_recursion_holds`: **True**
- `central_character_pairing_present`: **True**
- `valency_recursion_holds_BCN`: **True**
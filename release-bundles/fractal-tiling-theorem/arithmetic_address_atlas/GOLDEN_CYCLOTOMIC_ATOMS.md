# Golden Cyclotomic Atoms (family B2)

**Definition.** A *golden atom* is `Φ_d(2)` with `5 ∣ d`. By Theorem 2 its
primitive prime factors are forced into the **split locus of `Q(√5)`**.

| d | `Φ_d(2)` | factors (type) | grade | icosian hit |
|---|---|---|---|---|
| 5 | 31 | 31 (split) | **D** | **level** |
| 10 | 11 | 11 (split) | **D** | **Hecke prime** |
| 15 | 151 | 151 (split) | **D** | **level (dim table)** |
| 20 | 205 | 5 (ramified), 41 (split) | **D** | **41 = level** |
| 25 | 1082401 | 601 (split), 1801 (split) | C | — |
| 30 | 331 | 331 (split) | **D** | **dim-table prime** |
| 40 | 61681 | 61681 (split) | C | (large) |
| 50 | 1016801 | 251 (split), 4051 (split) | C | — |
| 60 | 80581 | 61 (split), 1321 (split) | C | — |

**Split-fraction across golden sectors = 1.000** (vs 0.30 control). The first
golden atoms `31, 11, 41, 151, 331` are exactly the levels / Hecke primes of the
icosian construction — the genuine `address → coordinate` content.

## Boundary (honest)
- **Sufficient, not bijective.** `5∣d` guarantees split factors, but split primes
  also arise from non-golden sectors (e.g. `Φ₁₃(2)=8191` is split). Golden atoms
  do not generate *all* levels (e.g. 59, 61, 71, 79 are not small golden atoms).
- **Reaches Grade D at most** (level/Hecke-prime). It does **not** reach E/F: the
  order-sector is decoupled from the Hecke value (see `HECKE_RESPONSE_BOUNDARY.md`).

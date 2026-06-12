# Address Atlas Schema

Each atlas entry (`atlas_entries.json`) records how far an object penetrates the stack.

## Fields
| field | meaning |
|---|---|
| `name` | human label |
| `expr` | integer or expression (e.g. `2^136279840+1`, `Phi_5(2)`, `prime 31`) |
| `value` / `value_digits` | the value, or digit-count for mega-numbers |
| `family` | seed family (B1…B5) |
| `factor` / `n_factor` | factorisation (of the value, or of the exponent) |
| `active_sectors` / `small_sectors` | cyclotomic `d`-sectors of `a^n±1` |
| `forced_divisor` | algebraic factor proving compositeness (Grade A) |
| `q_mod5` / `field_type` | splitting in `Q(√5)`: split / inert / ramified (Grade C) |
| `ideal` | prime-ideal refinement in `Z[φ]` (Grade D) |
| `is_level` / `is_hecke_prime` | enters the icosian Brandt/Hecke construction (Grade D) |
| `is_L_function` | a coherent global L-function (Grade E) |
| `boundary_test` | order-sector vs Hecke decoupling result |
| `grade` | **A–F**, the deepest demonstrated layer |
| `grade_reason` | one-line justification |
| `note` | claim boundary / caveats |

## Grading rule
`grade(entry)` returns the deepest layer with a *demonstrated* pass condition:
`E` if `is_L_function`; else `D` if `is_level`/`is_hecke_prime`; else `C` if
`routes_to_field`; else `B` if `is_cyclotomic_address`; else `A`. **`F` is never
auto-assigned** — a positivity/RH claim would require an explicit proof artifact,
which this atlas does not contain.

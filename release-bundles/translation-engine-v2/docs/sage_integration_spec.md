# SAGE Integration Specification — Engine v0.3 Milestone

This document specifies exactly what's needed to wire genuine
Hecke / Brandt matrix data from SAGE into the translation engine's
`HECKE_LIFT` transformation kind, replacing the v0.2 prototype.

## Why SAGE specifically

SAGE is the canonical open-source mathematical computing system
for number theory. It has built-in support for:
- Hilbert modular forms over Q(√d) for small d
- Brandt matrices for quaternion algebras over number fields
- Hecke operators on automorphic representations
- Quaternion algebras and their maximal orders
- Class groups and ideal class representatives

Magma and Pari/GP have overlapping capability but SAGE is freely
available and has Python interop, which matches our engine's
language.

## What we need from SAGE

### Required SAGE version and modules

- SAGE ≥ 9.5 (10.x preferred)
- Modules: `sage.modular.hilbert_modular_forms`,
  `sage.algebras.quatalg.quaternion_algebra`,
  `sage.modular.brandt`,
  `sage.rings.number_field`

### Specific SAGE objects we need to construct

```python
# In a SAGE session (or via SAGE's Python interpreter):

# 1. Number field K = Q(sqrt 5) with golden ratio generator
K.<phi> = NumberField(x^2 - x - 1)
OK = K.maximal_order()

# 2. The icosian quaternion algebra over K
# (the totally definite quaternion algebra ramified at the
# infinite places, or its closest tractable analog)
B.<i, j, k> = QuaternionAlgebra(K, -1, -1)
I_max = B.maximal_order()  # the maximal icosian order

# 3. The Brandt module
# (This is the finite-dim space carrying the Hecke action.)
BM = BrandtModule(I_max, level=1)
dim_BM = BM.dimension()  # finite, computable

# 4. For each prime p of OK, compute the Brandt matrix B_p
# This is the Hecke operator T_p on BM.
for p in OK.primes_below_bound(50):
    B_p = BM.hecke_matrix(p)  # finite-dim matrix
    # save B_p for the engine
```

### Required output format for the engine

The engine consumes Brandt matrices as a JSON or pickle file with
schema:

```json
{
  "field": "Q(sqrt 5)",
  "field_generator": "phi (golden ratio)",
  "field_minimal_polynomial": "x^2 - x - 1",
  "quaternion_algebra": {
    "ramified_primes": [...],
    "discriminant": "..."
  },
  "maximal_order": "I_max (the icosian maximal order)",
  "brandt_module": {
    "level": 1,
    "dimension": N,
    "ideal_class_representatives": [...]
  },
  "hecke_operators": [
    {
      "prime": {"norm": p, "representative": "..."},
      "kind": "split | inert | ramified",
      "matrix": [[...], [...], ...]
    },
    ...
  ]
}
```

The matrices are integer-valued (the entries of Brandt matrices are
representation counts of one ideal class by another, mod the prime
p), so the JSON is lossless.

## Where this slots into the engine

### File: `code/transformation_kinds.py`

Replace the `hecke_lift` function with `hecke_lift_from_brandt`:

```python
def hecke_lift_from_brandt(brandt_data: Dict,
                            prime_norm: int
                            ) -> TransformationOutcome:
    """Construct the genuine Hecke operator T_p from SAGE-computed
    Brandt matrix data."""
    # Look up the specific T_p in brandt_data["hecke_operators"]
    op = next((h for h in brandt_data["hecke_operators"]
               if h["prime"]["norm"] == prime_norm), None)
    if op is None:
        return TransformationOutcome(
            kind=TransformationKind.HECKE_LIFT,
            input_summary=f"prime norm {prime_norm}",
            output_summary="prime not found in Brandt data",
            admissibility=Admissibility.DEGENERATE,
        )
    T_p = np.array(op["matrix"], dtype=int)
    # T_p eigenvalues are the actual Hecke eigenvalues
    eigs = np.linalg.eigvalsh(0.5 * (T_p + T_p.T))
    return TransformationOutcome(
        kind=TransformationKind.HECKE_LIFT,
        input_summary=f"Brandt module + prime norm {prime_norm}",
        output_summary=f"genuine T_p ({T_p.shape[0]}x{T_p.shape[1]})",
        output_data=T_p,
        admissibility=Admissibility.EXACT,
        notes=[f"prime norm = {prime_norm}",
               f"split / inert / ramified: {op['kind']}",
               "matrix elements from SAGE Brandt module"],
    )
```

### File: `code/search.py`

Update `search_compositions` to load Brandt data and use the new
function:

```python
def search_compositions(base_operator, brandt_data_path: str,
                        primes_to_try, max_compositions=4,
                        target_eigs=adm.GAMMAS, report_top_k=10):
    import json
    with open(brandt_data_path) as f:
        brandt_data = json.load(f)
    # ... use hecke_lift_from_brandt for each prime
```

### File: `examples/run_v600_real_search.py` (NEW)

```python
# After running SAGE to produce brandt_data.json:
candidates = srch.search_compositions(
    base_operator=A1_block,
    brandt_data_path="data/brandt_q_sqrt5_level_1.json",
    primes_to_try=[2, 3, 5, 7, 11, 13, ...],
    target_eigs=adm.GAMMAS,
)
```

## Implementation steps and success criteria

### Step 1 — Install SAGE
```bash
# Option A: package manager (Ubuntu)
sudo apt install sagemath
# Option B: Conda
conda install -c conda-forge sage
# Option C: build from source (~1 hour)
```

**Success criterion**: `sage -c "K.<phi> = NumberField(x^2 - x - 1); print(K)"`
returns the field.

### Step 2 — Compute Brandt matrices for Q(√5) at level 1

Write `sage_scripts/compute_brandt.sage`:

```python
K.<phi> = NumberField(x^2 - x - 1)
B.<i, j, k> = QuaternionAlgebra(K, -1, -1)
I_max = B.maximal_order()
BM = BrandtModule(I_max, level=1)

import json
output = {
    "field": "Q(sqrt 5)",
    "field_generator": "phi",
    "brandt_module": {"level": 1, "dimension": BM.dimension()},
    "hecke_operators": []
}

for p in K.primes_below_bound(100):
    B_p = BM.hecke_matrix(p)
    p_norm = p.norm()
    output["hecke_operators"].append({
        "prime": {"norm": int(p_norm), "representative": str(p)},
        "matrix": [[int(B_p[i,j]) for j in range(B_p.ncols())]
                   for i in range(B_p.nrows())]
    })

with open("data/brandt_q_sqrt5_level_1.json", "w") as f:
    json.dump(output, f, indent=2)
```

Run: `sage compute_brandt.sage`

**Success criterion**: `data/brandt_q_sqrt5_level_1.json` exists
with at least 10 Hecke operators tabulated. Brandt module dimension
is reported (typically small for level 1; non-trivial structure
appears at higher levels).

### Step 3 — Wire into engine

Apply the file changes above. Run
`examples/run_v600_real_search.py`.

**Success criterion**: search returns at least one candidate with
HECKE_MULTIPLICATIVE = EXACT (since real Hecke operators DO satisfy
multiplicativity).

### Step 4 — Test against deep admissibility

For each candidate operator from the search, run
`deepc.evaluate_calibrated`. Report which operators pass FE / DN /
GUE.

**Success criterion**: at least one operator passes all four deep
checks (FE / DN / GUE / HK_MULT) at CANDIDATE level or better. This
would be a candidate Hilbert–Pólya construction.

(Note: passing all four at CANDIDATE is NOT a proof. It's evidence
that the construction is structurally consistent. Verifying it
analytically requires further work.)

### Step 5 — Scale up to higher levels and weights

If level 1 doesn't yield candidates, repeat at level N = 5, 11, 31
(primes inert in Z[φ]) and weight (2, 2), (4, 4), etc.

**Success criterion**: a documented attempt at multiple levels
showing the search either succeeds or fails systematically.

## Roadmap milestones

| Milestone | Content | Status |
|---|---|---|
| 0.1 | Prototype engine (current) | DONE |
| 0.2 | Deep admissibility classes + calibrated diagnostic | DONE |
| **0.3** | **SAGE Brandt integration (this doc)** | **NEXT** |
| 0.4 | Explicit formula verification (Weil identity) | future |
| 0.5 | Goal-directed search via closure_ai | future |
| 1.0 | Production release — prototype kinds fully replaced | future |

## What 0.3 would tell us

The engine v0.3 with real Brandt data will tell us one of three
things:

1. **Some real Hecke combination passes all deep checks at
   CANDIDATE+ level.** This would be a concrete Hilbert–Pólya
   candidate. Worth publishing immediately as a probe result;
   analytical verification would be the next work.

2. **No combination passes; a specific deep check is the wall.**
   This narrows the open problem: we'd know exactly which property
   (e.g. "Hecke operators don't give the right density") is the
   obstruction. Publishable as a precise structural result.

3. **The Brandt module is too small at level 1.** Class number 1
   for our setup means low-level Brandt modules are 1-dimensional.
   Then 0.3 is the work of computing at higher levels and weights,
   which is SAGE-side work but well-scoped.

Any of the three is a real research outcome.

## Time estimate

- SAGE install: 1–3 hours
- Brandt computation script: 1–2 hours
- Engine integration: 1–2 hours
- Diagnostic runs and analysis: 2–4 hours

**Total: 1 working day**, assuming SAGE has the Brandt module
functionality for Q(√5) (it does as of SAGE 10+).

This is the next concrete milestone. The engine's architecture
supports it without redesign. The mathematics inside is the
research content; the engine handles the bookkeeping and
admissibility verification.

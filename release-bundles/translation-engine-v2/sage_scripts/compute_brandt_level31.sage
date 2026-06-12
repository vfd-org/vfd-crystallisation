"""Compute REAL Brandt matrices for level 31 over Q, and harvest
Hecke eigenvalues for primes up to bound, plus prime structure of
Q(sqrt 5) for cross-reference.

Outputs:
  data/brandt_level31.json -- the Brandt module data + Hecke matrices

Why level 31:
  - 31 is the smallest prime where the icosian programme's chain
    naturally lives (V_600 spectrum has 31-related structure;
    level-31 modular forms over Q(sqrt 5) are conjecturally related
    to icosian theta).
  - BrandtModule(31, 1) has dim 3 in SAGE 9.0, giving a 3x3 Hecke
    matrix action, NON-TRIVIAL Brandt structure.
  - SAGE 9.0 supports this case natively (number field BrandtModule
    is not implemented in 9.0).

Caveat:
  This is BrandtModule over Q at level 31, not the icosian Brandt
  module over Q(sqrt 5). It's a proxy: real Hecke action with the
  right multiplicativity and analytic structure, used here to
  demonstrate the engine v0.3 pipeline with genuine number theory
  inputs.

Run:
  sage compute_brandt_level31.sage
"""
import json
from pathlib import Path

# Number field Q(sqrt 5) for cross-reference
K.<phi> = NumberField(x^2 - x - 1)

# Prime structure in Q(sqrt 5) (split / inert / ramified)
prime_structure_K = {}
for p_rat in primes(50):
    factors = K.ideal(p_rat).factor()
    if len(factors) == 1 and factors[0][1] == 1:
        kind = "inert"
    elif len(factors) > 1:
        kind = "split"
    else:
        kind = "ramified"
    prime_structure_K[int(p_rat)] = {
        "kind": kind,
        "ideals": [{"norm": int(P.norm()), "exp": int(e)}
                   for P, e in factors]
    }

# Brandt module at level 31 over Q (proxy for icosian Hecke action)
BM = BrandtModule(31, 1)
dim_BM = int(BM.dimension())

# Compute Hecke matrices T_p for primes up to bound
primes_to_compute = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                      37, 41, 43, 47]
hecke_data = []
for p in primes_to_compute:
    try:
        T_p = BM.hecke_matrix(p)
        matrix_list = [[int(T_p[i, j]) for j in range(dim_BM)]
                       for i in range(dim_BM)]
        # Hecke eigenvalues (real, since Hecke matrices on Brandt
        # modules are symmetric / can be made so via Petersson)
        eigvals = T_p.eigenvalues()
        kind_K = prime_structure_K.get(p, {}).get("kind", "unknown")
        hecke_data.append({
            "prime": int(p),
            "kind_in_Q_sqrt_5": kind_K,
            "matrix": matrix_list,
            "trace": int(T_p.trace()),
            "det": int(T_p.det()),
            "eigvals_string": str(eigvals)[:200],
        })
        print(f"T_{p}: trace = {T_p.trace()}, det = {T_p.det()}, "
              f"K-kind = {kind_K}")
    except Exception as e:
        print(f"T_{p}: error {repr(e)[:100]}")

# Helper to recursively convert SAGE Integers to Python ints
def to_py(obj):
    if isinstance(obj, dict):
        return {to_py(k): to_py(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_py(x) for x in obj]
    try:
        return int(obj)
    except (TypeError, ValueError):
        try:
            return float(obj)
        except (TypeError, ValueError):
            return str(obj)

output = to_py({
    "field": "Q(sqrt 5)",
    "field_generator": "phi",
    "field_minimal_polynomial": "x^2 - x - 1",
    "field_class_number": K.class_number(),
    "prime_structure_K": prime_structure_K,
    "brandt_module_proxy": {
        "level": 31,
        "weight": 2,
        "dimension": dim_BM,
        "comment": "BrandtModule(31, 1) over Q -- proxy for icosian "
                   "Hecke action; SAGE 9.0 does not implement "
                   "BrandtModule over Q(sqrt 5)",
    },
    "hecke_operators": hecke_data,
    "sage_version": "9.0",
})

# Save
out_path = Path("data/brandt_level31.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print()
print(f"Saved Brandt data with {len(hecke_data)} Hecke matrices to "
      f"{out_path}")
print(f"Brandt module dimension: {dim_BM}")

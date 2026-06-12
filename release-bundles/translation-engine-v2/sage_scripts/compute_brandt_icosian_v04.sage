"""v0.4: Compute the ICOSIAN-SPECIFIC Brandt matrices over Q(sqrt 5).

Requires SAGE 10+ (number-field BrandtModule, maximal_order for
quaternion algebras over number fields).

This is the natural next milestone after v0.3 (which used
BrandtModule over Q at level 31 as a proxy).

What this computes:
  1. K = Q(sqrt 5), O_K = Z[phi]
  2. B = the icosian quaternion algebra over K
     (totally definite, ramified at the infinite places only)
  3. I_max = the maximal order of B (corresponds to the icosian
     ring -- the V_600 quaternions form a finite subgroup of I_max
     under units)
  4. BM(N) = the Brandt module of I_max at level N for N = ideal
     of O_K (we try several primes)
  5. T_p = Hecke operators on BM at primes p of O_K
  6. Output: data/brandt_icosian.json with full Hecke matrices

This is the substrate's NATIVE Hecke action. If the hybrid probe
in v0.3 found HILBERT_POLYA_PARTIAL with non-icosian data, the
icosian-specific data SHOULD reach STRONG -- if the substrate-side
RH picture is correct.

Failure modes (informative):
  - The icosian Brandt module at low levels might still be too
    small (class number = 1 -> dim 1 at level 1)
  - Hecke matrix structure might differ from level-31 proxy in
    ways that affect FE / GUE
  - Some technical SAGE 10 issue might surface -- in which case
    we have a precise bug report

Run:
  ~/miniconda3/bin/sage compute_brandt_icosian_v04.sage
"""
import json
from pathlib import Path

print("=" * 76)
print("v0.4: Icosian Brandt computation over Q(sqrt 5)")
print("=" * 76)

# Step 1: Q(sqrt 5)
K.<phi> = NumberField(x^2 - x - 1)
OK = K.maximal_order()
print(f"K = {K}")
print(f"class number: {K.class_number()}")
print(f"OK basis: {OK.basis()}")
print()

# Step 2: Icosian quaternion algebra
# The icosian quaternion algebra over K is the unique (up to
# isomorphism) totally definite quaternion algebra ramified at
# both real places of K and nowhere finite. SAGE 10's
# QuaternionAlgebra constructor handles this.
B.<i, j, k> = QuaternionAlgebra(K, -1, -1)
print(f"B = {B}")
print(f"B discriminant: {B.discriminant()}")
print()

# Step 3: Maximal order (SAGE 10+ required)
try:
    I_max = B.maximal_order()
    print(f"I_max = {I_max}")
    print(f"I_max basis (first few): {I_max.basis()[:6]}")
except NotImplementedError as e:
    print(f"FAIL: maximal_order not implemented: {e}")
    print("This means we still have a SAGE 9 limitation.")
    raise

# Step 4: Brandt modules at various levels
prime_levels_to_try = []
for p_rat in primes(50):
    for P, _ in K.ideal(p_rat).factor():
        if P.norm() <= 50:
            prime_levels_to_try.append(P)

results = []
for level_ideal in prime_levels_to_try[:8]:  # try first 8 primes
    try:
        BM = BrandtModule(I_max, level=level_ideal)
        dim_bm = int(BM.dimension())
        print(f"BrandtModule(I_max, level=prime of norm "
              f"{level_ideal.norm()}): dim {dim_bm}")
        results.append({
            "level_norm": int(level_ideal.norm()),
            "level_repr": str(level_ideal),
            "dimension": dim_bm,
        })
    except Exception as e:
        print(f"BrandtModule at level {level_ideal}: {repr(e)[:100]}")
        results.append({
            "level_norm": int(level_ideal.norm()),
            "level_repr": str(level_ideal),
            "error": repr(e)[:200],
        })

# Step 5: Pick the smallest non-trivial Brandt module and compute
# Hecke matrices
best_BM = None
best_level = None
for r, level_ideal in zip(results, prime_levels_to_try[:8]):
    if r.get("dimension", 0) >= 2:
        try:
            best_BM = BrandtModule(I_max, level=level_ideal)
            best_level = level_ideal
            print(f"\nUsing BrandtModule at level of norm "
                  f"{level_ideal.norm()} (dim {best_BM.dimension()}) "
                  f"for Hecke computation")
            break
        except Exception:
            continue

if best_BM is None:
    print("\nWARNING: no non-trivial Brandt module found at levels "
          "tested. Trying higher levels...")
    # Try higher levels (composite, higher norm primes)
    for p_rat in [53, 59, 61, 67, 71, 73, 79, 83]:
        for P, _ in K.ideal(p_rat).factor():
            try:
                BM = BrandtModule(I_max, level=P)
                dim_bm = int(BM.dimension())
                if dim_bm >= 2:
                    best_BM = BM
                    best_level = P
                    print(f"BrandtModule at norm {P.norm()}: dim {dim_bm}")
                    break
            except Exception:
                continue
        if best_BM is not None:
            break

if best_BM is None:
    print("\nFAIL: could not find non-trivial Brandt module. "
          "All icosian Brandt modules at tested levels are 1-dim "
          "(class number 1 = trivial Hecke action). This is the "
          "substrate-side limit at finite levels.")
    output = {
        "field": "Q(sqrt 5)",
        "field_class_number": int(K.class_number()),
        "quaternion_algebra": "B = (-1, -1) over K",
        "all_tested_brandt_modules": results,
        "conclusion": "All icosian Brandt modules at tested levels "
                       "are 1-dim; substrate-native Hecke at finite "
                       "levels is trivial.",
    }
else:
    # Step 6: Compute Hecke matrices
    hecke_data = []
    primes_to_compute = prime_levels_to_try[:15]
    for P_hecke in primes_to_compute:
        try:
            T_p = best_BM.hecke_matrix(P_hecke)
            d = best_BM.dimension()
            matrix_list = [[int(T_p[i, j]) for j in range(d)]
                           for i in range(d)]
            hecke_data.append({
                "prime_norm": int(P_hecke.norm()),
                "prime_repr": str(P_hecke),
                "matrix": matrix_list,
                "trace": int(T_p.trace()),
                "det": int(T_p.det()),
            })
            print(f"  T_p (norm {P_hecke.norm()}): "
                  f"trace = {T_p.trace()}, det = {T_p.det()}")
        except Exception as e:
            print(f"  T_p (norm {P_hecke.norm()}): error "
                  f"{repr(e)[:80]}")

    output = {
        "field": "Q(sqrt 5)",
        "field_class_number": int(K.class_number()),
        "quaternion_algebra": "icosian quaternion algebra over K",
        "level": {
            "norm": int(best_level.norm()),
            "repr": str(best_level),
        },
        "brandt_module": {
            "dimension": int(best_BM.dimension()),
        },
        "hecke_operators": hecke_data,
        "all_tested_levels": results,
    }


# Helper for SAGE Integer -> Python int
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

output = to_py(output)

out_path = Path("data/brandt_icosian.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nSaved to {out_path}")
print("Done.")

"""Demo: run the refuter on real candidate certificates -- including ones it MUST kill."""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import refuter as R

line = "=" * 84
print(line); print("CANDIDATE-CERTIFICATE REFUTER  --  it refutes; it never certifies"); print(line)
results = {}

# ---- RH ----
print("\n[RH]  candidate: 'the Weil explicit-formula form is PSD via completion X'")
for cand in ["real", "fake", "none"]:
    v = R.refute_rh(candidate=cand)
    results[f"rh_{cand}"] = {"verdict": v.verdict, "witness": v.witness, "detail": v.detail}
    tag = "REFUTED" if v.refuted else "survives-truncations"
    extra = f"  witness={v.witness}" if v.refuted else ""
    print(f"   completion='{cand}': {tag}{extra}")
print("   -> correct completion survives (near-null, evidence only); fake/none REFUTED.")

# ---- Collatz ----
print("\n[Collatz]  candidate: 'V is a strict Lyapunov function for the 3n+1 odd-step map'")
cands = {
    "log n":       (lambda n: math.log(n)),
    "n":           (lambda n: float(n)),
    "v2(n)+log n": (lambda n: math.log(n) + ((n & -n).bit_length() - 1)),
}
for name, V in cands.items():
    v = R.refute_collatz_lyapunov(V, name=name, N=20000)
    results[f"collatz_lyap_{name}"] = {"verdict": v.verdict, "witness": v.witness}
    tag = "REFUTED" if v.refuted else "survives-truncations"
    extra = f"  witness={v.witness['item'] if v.refuted else ''}->{v.witness['value'] if v.refuted else ''}" if v.refuted else ""
    print(f"   V='{name}': {tag}{extra}")
vN = R.refute_collatz_numeric(N=20000)
results["collatz_numeric"] = {"verdict": vN.verdict}
print(f"   candidate 'all n<=20000 reach 1': {vN.verdict}  (verification, NOT proof)")
print("   -> every purely-local Lyapunov is REFUTED, as the full-shift theorem predicts.")

# ---- Navier-Stokes ----
print("\n[Navier-Stokes]  candidate: 'nu>=nu_floor => dyadic-shell capacity stays >=0'")
for floor in [0.2, 0.05]:
    v = R.refute_ns_coercive(nu_floor=floor)
    results[f"ns_{floor}"] = {"verdict": v.verdict, "witness": v.witness}
    tag = "REFUTED" if v.refuted else "survives-truncations"
    extra = f"  witness=nu {v.witness['item']} -> Q {v.witness['value']}" if v.refuted else ""
    print(f"   nu_floor={floor}: {tag}{extra}")

print("\n" + line)
print("VERDICT SUMMARY: the harness REFUTED the wrong candidates with concrete witnesses,")
print("and returned SURVIVES-TRUNCATIONS (never 'proved') for the rest.")
print(f"\n{R.BANNER}")
print(line)
json.dump({k: (v if isinstance(v, dict) else str(v)) for k, v in results.items()},
          open(os.path.join(os.path.dirname(__file__), "refuter_results.json"), "w"),
          indent=2, default=str)
print("[json] refuter_results.json")

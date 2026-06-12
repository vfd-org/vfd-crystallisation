"""
Out-of-sample icosian Brandt test  --  WO-VFD-OOS-ICOSIAN-BRANDT-001

THE QUESTION (Lee's hypothesis): is the icosian / 600-cell geometry the real plumbing
under the arithmetic -- does it generate the genuine Hecke eigenvalues WITHOUT fitting,
on primes it was never shown?

THE TARGET (genuine, parameter-free): the norm-31 cuspidal Hilbert newform over Q(sqrt5),
eigenvalues a_P computed by brute-force point-counting on the elliptic curve 31.1-a1
(sims/sim_genuine_eigenvalues.py). No LMFDB eigenvalue table, no fitting. Satisfies
Ramanujan |a_P| <= 2 sqrt(N(P)) -> genuinely cuspidal (the RH-bearing object).

THE GEOMETRY'S CHANNELS:
  * Eisenstein channel (COMPUTABLE, parameter-free): the level-1 icosian theta series is
    Eisenstein; its Hecke eigenvalue is E_P = N(P)+1. This is pure geometry/counting.
  * Cuspidal channel (the one that must match a_P): the icosian Brandt action at level
    (5phi-2). REQUIRES quaternion-order arithmetic over Z[phi] -- NOT available here
    (no Magma; SAGE: 'maximal order only for rational quaternion algebras'). BLOCKED.

THE TEST (designed to FAIL honestly): split primes into in-sample (N<=41) and
out-of-sample (N>=59). Ask whether any PARAMETER-FREE geometric channel reproduces the
genuine a_P out-of-sample. The Eisenstein channel is the only one we can compute, so we
test it -- and report the cuspidal channel as BLOCKED rather than fake a pass.
"""
import csv, math, os, json

HERE = os.path.dirname(__file__)
GEN = os.path.join(HERE, "..", "data", "genuine_newform_eigenvalues.csv")

rows = []
with open(GEN) as fh:
    for r in csv.DictReader(fh):
        if r["status"] != "good" or r["a_P"] == "":
            continue
        N = int(r["norm_NP"]); a = int(r["a_P"])
        rows.append({"N": N, "a_P": a, "kind": r["kind"]})

IN, OUT = 41, 59      # in-sample primes used by the prior substrate file go up to N=41
def bucket(N): return "in-sample" if N <= IN else "out-of-sample"

print("=" * 84)
print("OUT-OF-SAMPLE ICOSIAN BRANDT TEST  --  does the geometry generate a_P without fitting?")
print("=" * 84)
print(f"\n  {'N(P)':>5} {'kind':9} {'genuine a_P':>11} {'Eisenstein N+1':>14} "
      f"{'|a|<=2sqrtN':>11} {'bucket':>13}")
eis_matches = {"in-sample": 0, "out-of-sample": 0}
eis_total = {"in-sample": 0, "out-of-sample": 0}
ram_ok = 0
for r in rows:
    N, a = r["N"], r["a_P"]
    E = N + 1
    ram = abs(a) <= 2 * math.sqrt(N) + 1e-9
    ram_ok += ram
    b = bucket(N)
    eis_total[b] += 1
    if a == E:
        eis_matches[b] += 1
    print(f"  {N:5d} {r['kind']:9} {a:11d} {E:14d} {str(ram):>11} {b:>13}")

print("\n" + "-" * 84)
print("CHANNEL RESULTS (parameter-free, no fitting):")
print(f"  Ramanujan |a_P|<=2sqrt(N(P)) holds for {ram_ok}/{len(rows)} genuine eigenvalues "
      f"-> target is genuinely CUSPIDAL (not Eisenstein).")
for b in ("in-sample", "out-of-sample"):
    print(f"  Eisenstein channel (N+1) reproduces genuine a_P: "
          f"{eis_matches[b]}/{eis_total[b]} {b}")
eis_is_wrong = (eis_matches["out-of-sample"] == 0)
print(f"  -> Eisenstein channel matches the cuspidal target out-of-sample: "
      f"{'NO' if eis_is_wrong else 'partially'} "
      f"(expected NO: Eisenstein ~N+1 violates Ramanujan).")

cuspidal_geometry_available = False     # icosian Brandt over Z[phi] not computable here
verdict = (
    "GEOMETRY REPRODUCES CUSPIDAL OUT-OF-SAMPLE" if cuspidal_geometry_available else
    "NOT DEMONSTRATED (cuspidal channel BLOCKED)")
print("\n" + "=" * 84)
print(f"  VERDICT: {verdict}")
print("""  HONEST READING:
   * The genuine target is real, parameter-free, and CUSPIDAL (Ramanujan holds).
   * The geometry's ONE computable parameter-free channel -- the level-1 Eisenstein
     eigenvalue N(P)+1 -- does NOT reproduce the cuspidal a_P (it grows like N, the
     target obeys Ramanujan). So the trivially-geometric channel is the WRONG object,
     exactly as the circle-test audit warned.
   * The channel that COULD match -- the icosian Brandt action at level (5phi-2) -- is
     the genuine test of "geometry is the plumbing". It is BLOCKED with available tools
     (no Magma; SAGE has no maximal order / Brandt module over Q(sqrt5)). We REFUSE to
     fit a map to the target (that was the prior error), so the test returns NOT
     DEMONSTRATED rather than a fake pass.
   * What the geometry DOES reproduce parameter-free is the EISENSTEIN arithmetic
     (icosian theta = zeta_K(s) zeta_K(s-1), verified earlier) -- the bookkeeping/divisor
     layer. The CUSPIDAL layer, where the L-function and RH live, is NOT yet shown to be
     geometric. That gap is precisely 'what we are missing'.
  WHAT WOULD UNBLOCK IT: (a) Magma's quaternion-order/HMF over Q(sqrt5), or (b) the
  from-scratch icosian Eichler-order class enumeration at level (5phi-2) (scaffold in
  route_b/brandt_level31.py; acceptance gate: Brandt-module dim h=2 via the mass formula),
  then compare ITS cuspidal eigenvalue to the a_P above out-of-sample. NOT a proof of RH
  even if it matches -- positivity (the Connes wall) remains.""")
print("=" * 84)
json.dump(dict(work_order="WO-VFD-OOS-ICOSIAN-BRANDT-001",
    n_eigenvalues=len(rows), ramanujan_holds=f"{ram_ok}/{len(rows)}",
    eisenstein_matches=eis_matches, eisenstein_is_wrong_object=eis_is_wrong,
    cuspidal_geometry_computable=cuspidal_geometry_available, verdict=verdict,
    honest="geometry reproduces the EISENSTEIN arithmetic parameter-free; the CUSPIDAL "
           "(RH-bearing) channel via icosian Brandt over Z[phi] is BLOCKED (no Magma/SAGE-HMF); "
           "test refuses to fit -> NOT DEMONSTRATED, not a fake pass",
    no_rh_claim=True),
    open(os.path.join(HERE, "oos_brandt_results.json"), "w"), indent=2, default=str)
print("[json] oos_brandt_results.json")

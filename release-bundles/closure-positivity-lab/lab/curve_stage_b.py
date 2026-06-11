"""Stage B via the MODULARITY shortcut -- the icosian L's zeros, today, on a laptop.

The icosian Brandt eigenvalues were established (13/13 out-of-sample, level-31
cuspidal-geometry work) to equal the Frobenius traces of the elliptic curve

    E = 31.1-a1 / Q(sqrt5):  [a1..a6] = [1, phi+1, phi, phi, 0],  conductor (5phi-2).

So the degree-4 L-function's Dirichlet coefficients do NOT require Brandt enumeration
(cost ~hours/prime at large norm): they come from point counts of E over residue
fields via quadratic-character sums -- O(p) per split prime, O(p^2) per inert prime,
and Dirichlet coverage to n only needs inert p <= sqrt(n).  Coverage to n ~ 5000 costs
seconds.  PARI then finds the zeros (lfuncheckfeq self-validates), and the Li
certificates lambda_n fire.

PROVENANCE (honest): these zeros come via the modularity identification (curve side),
point-counted from five field elements -- no LMFDB eigenvalue tables.  The Brandt run
on the big machine is the GEOMETRIC out-of-sample certification of the same local
data at ~600 primes; this script cross-checks every available geometric eigenvalue
against the curve (must match exactly) before building anything.
"""
from __future__ import annotations
import json, math, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
LEVEL_NORM = 31
# a-invariants as (a, b) = a + b*phi
AINV = [(1, 0), (1, 1), (0, 1), (0, 1), (0, 0)]


# ----------------------------------------------------------- residue fields
def _primes_up_to(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = b"\x00" * len(s[i * i::i])
    return [i for i in range(2, n + 1) if s[i]]


def _phi_roots(p):
    """roots of r^2 = r + 1 mod p (split/ramified detection)."""
    return [r for r in range(p) if (r * r - r - 1) % p == 0]


def _count_Fp(p, phi_r):
    """#E(F_p) by character sum: #E = p + 1 + sum_x chi(D(x)),
    D(x) = (a1 x + a3)^2 + 4(x^3 + a2 x^2 + a4 x + a6)."""
    a1, a2, a3, a4, a6 = [(a + b * phi_r) % p for (a, b) in AINV]
    if p == 2:
        n = 1
        for x in range(2):
            for y in range(2):
                if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % 2 == 0:
                    n += 1
        return n
    sq = bytearray(p)
    for t in range((p + 1) // 2 + 1):
        sq[(t * t) % p] = 1
    s = 0
    for x in range(p):
        D = ((a1 * x + a3) ** 2 + 4 * (x ** 3 + a2 * x * x + a4 * x + a6)) % p
        s += 0 if D == 0 else (1 if sq[D] else -1)
    return p + 1 + s


def _count_Fp2(p):
    """#E(F_{p^2}) for inert p: F_p2 = F_p[phi], phi^2 = phi + 1.
    Elements (a,b); chi via the set of squares (O(p^2) precompute)."""
    q = p * p
    def mul(u, v):
        a, b = u; c, d = v
        return ((a * c + b * d) % p, (a * d + b * c + b * d) % p)
    def add(u, v):
        return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)
    def smul(k, u):
        return ((k * u[0]) % p, (k * u[1]) % p)
    A = [( (a) % p, (b) % p ) for (a, b) in AINV]
    a1, a2, a3, a4, a6 = A
    els = [(a, b) for a in range(p) for b in range(p)]
    if p == 2:
        n = 1
        for x in els:
            for y in els:
                lhs = add(add(mul(y, y), mul(mul(a1, x), y)), mul(a3, y))
                x2 = mul(x, x); x3 = mul(x2, x)
                rhs = add(add(x3, mul(a2, x2)), add(mul(a4, x), a6))
                if (lhs[0] - rhs[0]) % p == 0 and (lhs[1] - rhs[1]) % p == 0:
                    n += 1
        return n
    sq = set()
    for u in els:
        sq.add(mul(u, u))
    s = 0
    for x in els:
        x2 = mul(x, x); x3 = mul(x2, x)
        t = add(mul(a1, x), a3)
        f = add(add(x3, mul(a2, x2)), add(mul(a4, x), a6))
        D = add(mul(t, t), smul(4, f))
        s += 0 if D == (0, 0) else (1 if D in sq else -1)
    return q + 1 + s


def curve_ap_table(nmax):
    """a_P for every prime ideal needed for Dirichlet coverage to nmax.
    Split/ramified p <= nmax (each root of phi); inert p <= sqrt(nmax).
    Bad prime above 31 = (5 phi - 2): phi |-> 19; a = -1 (nonsplit mult., matches
    the Brandt Steinberg eigenvalue).  Good prime above 31: phi |-> 13."""
    rows = []
    for p in _primes_up_to(nmax):
        roots = _phi_roots(p)
        if p == 5:                                       # ramified
            r = roots[0]
            rows.append({"p": p, "kind": "ramified", "norm": 5, "phi": r,
                         "a_P": 5 + 1 - _count_Fp(5, r)})
        elif roots:                                      # split
            for r in roots:
                if p == LEVEL_NORM and (5 * r - 2) % p == 0:
                    rows.append({"p": p, "kind": "bad", "norm": p, "phi": r,
                                 "a_P": -1})             # nonsplit multiplicative
                else:
                    rows.append({"p": p, "kind": "split", "norm": p, "phi": r,
                                 "a_P": p + 1 - _count_Fp(p, r)})
        elif p * p <= nmax:                              # inert, needed at n = p^2
            rows.append({"p": p, "kind": "inert", "norm": p * p, "phi": None,
                         "a_P": p * p + 1 - _count_Fp2(p)})
    return rows


# ----------------------------------------------------------- cross-checks
def crosscheck_geometric(rows):
    """Every available geometric Brandt eigenvalue must equal the curve a_P."""
    paths = [os.path.join(HERE, "..", "..", "frontier-run", "out", "a_q_extended.json"),
             os.path.join(HERE, "..", "..", "icosian-rh-geometric", "repro", "data",
                          "geometric_aP.json")]
    geo = []
    for pth in paths:
        if os.path.exists(pth):
            geo = json.load(open(pth))["rows"]; src = os.path.basename(pth); break
    if not geo:
        return {"checked": 0, "mismatches": -1, "source": None}
    by = {}
    for r in rows:
        by.setdefault((r["p"], r["norm"]), []).append(r["a_P"])
    n_ok = n_chk = 0; bad = []
    for g in geo:
        key = (g["rational_prime"], g["norm"])
        if key not in by:
            continue
        n_chk += 1
        if g["a_q_geometric"] in by[key]:
            n_ok += 1
        else:
            bad.append({"key": key, "geometric": g["a_q_geometric"], "curve": by[key]})
    return {"checked": n_chk, "matched": n_ok, "mismatches": len(bad),
            "bad": bad[:10], "source": src}


# ----------------------------------------------------------- Dirichlet + PARI
def _polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def _series_inverse(poly, kmax):
    inv = [0.0] * (kmax + 1); inv[0] = 1.0
    for k in range(1, kmax + 1):
        s = 0.0
        for j in range(1, min(k, len(poly) - 1) + 1):
            s += poly[j] * inv[k - j]
        inv[k] = -s
    return inv


def dirichlet_coeffs(rows, nmax):
    lam = [0.0] * (nmax + 1); lam[1] = 1.0
    by_p = {}
    for r in rows:
        by_p.setdefault(r["p"], []).append(r)
    for p in _primes_up_to(nmax):
        evs = by_p.get(p, [])
        if p == LEVEL_NORM:
            bad = [x for x in evs if x["kind"] == "bad"]
            good = [x for x in evs if x["kind"] == "split"]
            if not bad or not good:
                return None, p
            poly = _polymul([1, -bad[0]["a_P"]], [1, -good[0]["a_P"], p])
        elif p == 5:
            if not evs:
                return None, p
            poly = [1, -evs[0]["a_P"], 5]
        elif evs and evs[0]["kind"] == "split":
            if len(evs) < 2:
                return None, p
            poly = _polymul([1, -evs[0]["a_P"], p], [1, -evs[1]["a_P"], p])
        elif evs and evs[0]["kind"] == "inert":
            poly = [1, 0, -evs[0]["a_P"], 0, p * p]
        else:
            if p * p <= nmax:                            # inert but missing
                return None, p
            continue                                     # inert, irrelevant below nmax
        kmax = int(math.log(nmax, p)) + 1
        inv = _series_inverse(poly, kmax)
        new = lam[:]
        for k in range(1, kmax + 1):
            pk = p ** k
            if pk > nmax:
                break
            for m in range(1, nmax // pk + 1):
                if m % p != 0:
                    new[m * pk] += lam[m] * inv[k]
        lam = new
    return lam, None


def run_pari(avec, gp="gp", height=25.0):
    os.makedirs(OUT, exist_ok=True)
    gpf = os.path.join(OUT, "_curve_zeros.gp")
    with open(gpf, "w") as f:
        f.write("default(parisize, 2^30);\n")
        f.write("av=[" + ",".join(str(int(round(x))) for x in avec) + "];\n")
        f.write("bestf=10^9; beste=0; bestL=0;\n")
        f.write("for(e=-1,1, if(e!=0,"
                " L=lfuncreate([av,0,[0,0,1,1],2,775,e]);"
                " ff=lfuncheckfeq(L);"
                " if(ff<bestf, bestf=ff; beste=e; bestL=L)));\n")
        f.write('print("EPS=",beste);\nprint("FEQ=",bestf);\n')
        f.write('print("ZEROS=",lfunzeros(bestL,%g));\n' % height)
    res = subprocess.run([gp, "-q", gpf], capture_output=True, text=True, timeout=14400)
    out = res.stdout + res.stderr
    eps = re.search(r"EPS=(-?\d+)", out)
    feq = re.search(r"FEQ=([-0-9.eE]+)", out)
    zm = re.search(r"ZEROS=\[([^\]]*)\]", out)
    zeros = ([float(x) for x in zm.group(1).split(",") if x.strip()]
             if zm and zm.group(1).strip() else [])
    return {"eps": int(eps.group(1)) if eps else None,
            "lfuncheckfeq_log2": float(feq.group(1)) if feq else None,
            "zeros": zeros, "raw_tail": out[-300:]}


def main(nmax=3000, height=25.0):
    import time
    t0 = time.time()
    rows = curve_ap_table(nmax)
    ram = all(abs(r["a_P"]) <= 2 * math.sqrt(r["norm"]) + 1e-9
              for r in rows if r["kind"] != "bad")
    print(f"[curve] {len(rows)} prime ideals point-counted to coverage n<={nmax} "
          f"({time.time()-t0:.1f}s); all Ramanujan: {ram}")
    chk = crosscheck_geometric(rows)
    print(f"[curve] geometric cross-check ({chk.get('source')}): "
          f"{chk.get('matched')}/{chk.get('checked')} match, "
          f"mismatches={chk.get('mismatches')}  <-- must be 0")
    if chk.get("mismatches"):
        print("[curve] MISMATCH vs geometric eigenvalues -- stopping, no L built.")
        print(chk["bad"]); return
    lam, miss = dirichlet_coeffs(rows, nmax)
    if lam is None:
        print(f"[curve] coverage broken at prime {miss}"); return
    print(f"[curve] {nmax} Dirichlet coefficients built "
          f"(a_2={lam[4]:.0f}@4? sample: {[int(lam[i]) for i in range(1,13)]})")
    print(f"[curve] -> PARI (lfuncheckfeq + lfunzeros to height {height})...", flush=True)
    pr = run_pari(lam[1:], height=height)
    print(f"[curve] eps={pr['eps']}  lfuncheckfeq(log2)={pr['lfuncheckfeq_log2']} "
          f"(very negative => L-data consistent)")
    print(f"[curve] zeros: {[round(z,4) for z in pr['zeros']]}")
    res = {"provenance": "modularity shortcut: curve 31.1-a1 point counts "
                         "(cross-checked vs ALL available geometric Brandt "
                         "eigenvalues, 0 mismatches); zeros from PARI lfun",
           "nmax": nmax, "n_prime_ideals": len(rows), "all_ramanujan": ram,
           "geometric_crosscheck": chk, **pr}
    res["L_zeros"] = res.pop("zeros")
    json.dump(res, open(os.path.join(OUT, "curve_zeros.json"), "w"), indent=1)
    print(f"[curve] wrote out/curve_zeros.json")
    if pr["zeros"]:
        from . import li_certificate as li
        print()
        li_res = li.icosian_li(nmax=8,
                               zeros_path=os.path.join(OUT, "curve_zeros.json"))
        if li_res:
            json.dump(li_res, open(os.path.join(OUT, "curve_li.json"), "w"), indent=1)
            print("[curve] wrote out/curve_li.json")


if __name__ == "__main__":
    import sys
    main(nmax=int(sys.argv[1]) if len(sys.argv) > 1 else 3000,
         height=float(sys.argv[2]) if len(sys.argv) > 2 else 25.0)

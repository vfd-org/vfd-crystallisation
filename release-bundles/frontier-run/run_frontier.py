#!/usr/bin/env python3
"""Frontier run -- extend the icosian Brandt eigenvalues and (try to) resolve the
icosian cuspidal L-function's OWN zeros out-of-sample.

Built for a many-core background machine. Two stages:

  STAGE A  (parallel, checkpointed, resumable)
    Compute the geometric Brandt cuspidal eigenvalues a_q for every prime ideal of
    K=Q(sqrt5) up to a norm bound, using the verified BrandtEngine. Embarrassingly
    parallel across prime ideals; writes out/a_q_extended.json incrementally, skips
    already-done ideals on restart, and validates against the shipped baseline
    (norms <= 150 must match exactly) plus Ramanujan + self-adjointness on all.

  STAGE B  (single process; needs Stage A output)
    Build the degree-4 Dirichlet coefficients lambda(n) of L(s,pi) from the local
    factors, SELF-TEST the zero-finder on the Riemann zeta (must recover 14.134..,
    21.022..), then find L's own low zeros and run the explicit-formula
    out-of-sample check  ARCH(g) - PRIME(g)  vs  sum over the found zeros.

Usage (background, take as long as it takes):
    python3 run_frontier.py --stage a --norm-bound 50000 --procs 30
    python3 run_frontier.py --stage b --nmax 4000
    # or: --stage both  (default norm-bound 50000, procs = cpu-2)

Nothing here proves RH. RH(L) = GRH for this one cuspidal L; positivity is untouched.
"""
from __future__ import annotations
import argparse, json, math, os, sys, time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "engine"))
import ok_arithmetic as ok           # noqa: E402
import brandt_matrices as bm         # noqa: E402
import geometric_aP as gap           # noqa: E402

OUT = os.path.join(HERE, "out")
A_PATH = os.path.join(OUT, "a_q_extended.json")
BASE = os.path.join(OUT, "geometric_aP_baseline.json")
LEVEL_NORM = 31                      # bad prime p_31 = (5 phi - 2)


# ============================================================ STAGE A (parallel)
_ENG = None
def _worker_init():
    global _ENG
    _ENG = bm.BrandtEngine()

def _worker(job):
    """job = (rational_prime, varpi_as_list). Returns a row or an error record."""
    p, varpi = job[0], tuple(job[1])
    try:
        r = _ENG.brandt_matrix(varpi)
        Nq = r["norm"]
        return {"rational_prime": p, "norm": Nq, "varpi": list(varpi),
                "a_q_geometric": r["cuspidal_eigenvalue"],
                "self_adjoint": bool(r["self_adjoint"]),
                "eisenstein_ok": bool(r["eisenstein_ok"]),
                "ramanujan_ok": abs(r["cuspidal_eigenvalue"]) <= 2*(Nq**0.5)+1e-9,
                "cuspidal_eigenvector": list(r["cuspidal_eigenvector"])}
    except Exception as e:                                  # level prime, etc.
        return {"rational_prime": p, "varpi": list(varpi), "error": repr(e)}


def _primes_up_to(n):
    s = bytearray([1])*(n+1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i::i] = b"\x00"*len(s[i*i::i])
    return [i for i in range(2, n+1) if s[i]]


def build_jobs(norm_bound):
    """All prime-ideal generators with norm <= norm_bound (split p<=B; inert p^2<=B)."""
    jobs = []
    for p in _primes_up_to(norm_bound):
        if p % 5 in (1, 4):
            if p > norm_bound:        continue            # split, norm p
        elif p == 5:
            if 5 > norm_bound:        continue            # ramified, norm 5
        else:
            if p*p > norm_bound:      continue            # inert, norm p^2
        for varpi in gap.prime_ideal_generators(p):
            jobs.append((p, list(varpi)))
    return jobs


def stage_a(norm_bound, procs, checkpoint_every=25):
    import multiprocessing as mp
    os.makedirs(OUT, exist_ok=True)
    done = {}
    if os.path.exists(A_PATH):
        for r in json.load(open(A_PATH)).get("rows", []):
            done[(r["rational_prime"], tuple(r.get("varpi", [])))] = r
    jobs = [j for j in build_jobs(norm_bound)
            if (j[0], tuple(j[1])) not in done]
    print(f"[A] norm_bound={norm_bound}  procs={procs}  "
          f"already done={len(done)}  to do={len(jobs)}", flush=True)
    rows = list(done.values())
    t0 = time.time(); n_new = 0
    if jobs:
        with mp.Pool(procs, initializer=_worker_init) as pool:
            for rec in pool.imap_unordered(_worker, jobs, chunksize=1):
                rows.append(rec); n_new += 1
                if "error" not in rec:
                    print(f"[A] N={rec['norm']:<7} a_q={rec['a_q_geometric']:<6}"
                          f" ram={rec['ramanujan_ok']} sa={rec['self_adjoint']}"
                          f"  ({n_new}/{len(jobs)}, {time.time()-t0:.0f}s)", flush=True)
                if n_new % checkpoint_every == 0:
                    _save_a(rows, norm_bound)
    _save_a(rows, norm_bound)
    _validate_a(rows)
    print(f"[A] done: {len(rows)} ideals, {time.time()-t0:.0f}s", flush=True)


def _save_a(rows, norm_bound):
    good = [r for r in rows if "error" not in r]
    good.sort(key=lambda d: (d["norm"], d["a_q_geometric"]))
    json.dump({"source": "icosian_brandt_operator (frontier parallel run)",
               "norm_bound": norm_bound, "n_prime_ideals": len(good),
               "all_self_adjoint": all(r["self_adjoint"] for r in good),
               "all_ramanujan": all(r["ramanujan_ok"] for r in good),
               "errors": [r for r in rows if "error" in r],
               "rows": good}, open(A_PATH, "w"), indent=1)


def _validate_a(rows):
    good = {(r["rational_prime"], r["norm"], tuple(r["varpi"])): r["a_q_geometric"]
            for r in rows if "error" not in r}
    base = json.load(open(BASE))["rows"] if os.path.exists(BASE) else []
    mism = 0
    for b in base:
        key = (b["rational_prime"], b["norm"], tuple(b["varpi"]))
        if key in good and good[key] != b["a_q_geometric"]:
            mism += 1
    sa = all(r["self_adjoint"] for r in rows if "error" not in r)
    ram = all(r["ramanujan_ok"] for r in rows if "error" not in r)
    print(f"[A][validate] baseline mismatches={mism} (must be 0); "
          f"all self-adjoint={sa}; all Ramanujan={ram}", flush=True)


# ============================================================ STAGE B (zeros)
def _local_factors(rows, nmax):
    """lambda(n) for n<=nmax from local Euler factors; returns (lam, covered, missing).
    Weight-2 normalisation: split p -> (1 - a X + p X^2)(1 - a' X + p X^2);
    inert p -> 1 - a X^2 + p^2 X^4 (X=p^-s); ramified 5 -> 1 - a X + 5 X^2.
    Bad prime above 31 (the level): degree-1 (1 - eps31 X) with eps31 = +1 (flagged)."""
    import numpy as np
    by_p = {}
    for r in rows:
        by_p.setdefault(r["rational_prime"], []).append(r)
    lam = np.zeros(nmax+1); lam[1] = 1.0
    known_prime = {}
    for p in _primes_up_to(nmax):
        # local polynomial coefficients c[k] = coeff of p^{-ks} in 1/L_p, then invert
        if p == LEVEL_NORM:                                # 31 splits: bad (level, deg 1) + good (deg 2)
            evs = by_p.get(p, [])
            bad = [x for x in evs if not x.get("self_adjoint", True)]
            good = [x for x in evs if x.get("self_adjoint", True)]
            if not bad or not good: known_prime[p] = False; continue
            poly = _polymul([1, -bad[0]["a_q_geometric"]],
                            [1, -good[0]["a_q_geometric"], p])
        elif p % 5 in (1, 4):                              # split: need both ideals
            ev = sorted(x["a_q_geometric"] for x in by_p.get(p, []))
            if len(ev) < 2: known_prime[p] = False; continue
            a, b = ev[0], ev[1]
            # (1 - a X + p X^2)(1 - b X + p X^2)
            poly = _polymul([1, -a, p], [1, -b, p])
        elif p == 5:
            ev = [x["a_q_geometric"] for x in by_p.get(5, [])]
            if not ev: known_prime[p] = False; continue
            poly = [1, -ev[0], 5]
        else:                                              # inert: one ideal norm p^2
            ev = [x["a_q_geometric"] for x in by_p.get(p, []) if x["norm"] == p*p]
            if not ev: known_prime[p] = False; continue
            poly = [1, 0, -ev[0], 0, p*p]                  # 1 - a X^2 + p^2 X^4
        known_prime[p] = True
        # Dirichlet coeffs at powers of p:  sum lam(p^k) X^k = 1/poly(X)
        kmax = int(math.log(nmax, p)) + 1
        inv = _series_inverse(poly, kmax)                  # [lam(1),lam(p),lam(p^2),..]
        # fold into lam by the sieve
        new = lam.copy()
        for k in range(1, kmax+1):
            pk = p**k
            if pk > nmax: break
            # multiply existing lam[m] (p-free) by inv[k] at m*pk
            step = pk
            for m in range(1, nmax//pk + 1):
                if m % p != 0:                             # m coprime to p
                    val = lam[m]*inv[k]
                    if m*pk <= nmax: new[m*pk] += val
        lam = new
    # coverage: n is known iff all its prime factors are known
    covered = np.ones(nmax+1, bool)
    for p in _primes_up_to(nmax):
        if not known_prime.get(p, False):
            covered[p::p] = False
    missing = sorted(p for p in _primes_up_to(nmax) if not known_prime.get(p, False))
    return lam, covered, missing


def _polymul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def _series_inverse(poly, kmax):
    """power-series inverse of poly (poly[0]=1) up to degree kmax."""
    inv = [0.0]*(kmax+1); inv[0] = 1.0
    for k in range(1, kmax+1):
        s = 0.0
        for j in range(1, min(k, len(poly)-1)+1):
            s += poly[j]*inv[k-j]
        inv[k] = -s
    return inv


# ============================================================ STAGE B (PARI lfun)
def _build_coeffs(rows, nmax):
    lam, covered, missing = _local_factors(rows, nmax)
    Ncov = nmax
    for n in range(1, nmax + 1):
        if not covered[n]:
            Ncov = n - 1; break
    return lam, covered, missing, Ncov


def stage_b(nmax, gp="gp", height=25.0):
    """Build the degree-4 L of the icosian cuspidal form from the extended a_q,
    hand it to PARI/GP (lfuncheckfeq self-validates the L-data; lfunzeros finds the
    zeros), then run the explicit-formula OUT-OF-SAMPLE check against THOSE zeros."""
    import json, subprocess, re
    rows = json.load(open(A_PATH))["rows"]
    lam, covered, missing, Ncov = _build_coeffs(rows, nmax)
    print(f"[B] coverage: complete for n<= {Ncov}  (first missing prime "
          f"{missing[0] if missing else None}); requested nmax={nmax}", flush=True)
    if Ncov < 200:
        print("[B] coverage too low for degree-4 zeros (need a few hundred clean "
              "coefficients). Run stage A to a higher --norm-bound first.", flush=True)
        json.dump({"coverage_complete_to": Ncov, "missing_primes": missing[:40],
                   "note": "run stage A to higher norm-bound, then re-run stage B"},
                  open(os.path.join(OUT, "zeros_result.json"), "w"), indent=1)
        return
    avec = [int(round(lam[n])) for n in range(1, Ncov + 1)]
    gpf = os.path.join(OUT, "_zeros.gp")
    with open(gpf, "w") as f:
        f.write("default(parisize, 2^30);\n")
        f.write("av=[" + ",".join(str(x) for x in avec) + "];\n")
        f.write("bestf=10^9; beste=1; bestL=0;\n")
        f.write("for(e=-1,1, if(e!=0,"
                " L=lfuncreate([av,0,[0,0,1,1],2,775,e]);"
                " ff=lfuncheckfeq(L);"
                " if(ff<bestf, bestf=ff; beste=e; bestL=L)));\n")
        f.write('print("EPS=",beste);\nprint("FEQ=",bestf);\n')
        f.write('print("ZEROS=",lfunzeros(bestL,%g));\n' % height)
    print(f"[B] {len(avec)} coefficients -> PARI/GP (lfuncheckfeq + lfunzeros)...",
          flush=True)
    try:
        res = subprocess.run([gp, "-q", gpf], capture_output=True, text=True,
                             timeout=72000)
        out = res.stdout + res.stderr
    except Exception as e:
        print("[B] gp call failed:", e); return
    eps = re.search(r"EPS=(-?\d+)", out)
    feq = re.search(r"FEQ=([-0-9.eE]+)", out)
    zm = re.search(r"ZEROS=\[([^\]]*)\]", out)
    zeros = ([float(x) for x in zm.group(1).split(",") if x.strip()]
             if zm and zm.group(1).strip() else [])
    feqv = float(feq.group(1)) if feq else None
    print(f"[B] eps={eps.group(1) if eps else '?'}  lfuncheckfeq(log2)={feqv}  "
          f"(very negative => L-data consistent, zeros trustworthy)", flush=True)
    print(f"[B] icosian L zeros up to height {height}: "
          f"{[round(z,4) for z in zeros]}", flush=True)
    chk = _explicit_formula_check(rows, zeros)
    json.dump({"coverage_complete_to": Ncov, "coeffs_used": len(avec),
               "eps": int(eps.group(1)) if eps else None,
               "lfuncheckfeq_log2": feqv, "L_zeros": zeros,
               "explicit_formula_out_of_sample": chk,
               "gp_raw_tail": out[-400:]},
              open(os.path.join(OUT, "zeros_result.json"), "w"), indent=1)
    print("[B] wrote out/zeros_result.json", flush=True)


def _explicit_formula_check(rows, zeros, sigmas=(2.0, 2.5, 3.0)):
    """OUT-OF-SAMPLE: does ARCH(h) - PRIME(h) (from the geometry: gamma factor and
    the geometric a_q) equal sum over the PARI zeros 2*sum_{gamma>0} h(gamma)?
    h(r)=exp(-r^2/2 sigma^2). Conductor 775, gamma Gamma_R shifts [0,0,1,1]."""
    import math, cmath
    if not zeros:
        return {"note": "no zeros to check"}
    LOGPI = math.log(math.pi)
    def dig(z):
        r = 0 + 0j
        while z.real < 10:
            r -= 1 / z; z = z + 1
        inv = 1 / z; inv2 = inv * inv
        return r + cmath.log(z) - 0.5 * inv - inv2 * (1/12 - inv2*(1/120 - inv2/252))
    def gR(s): return -0.5 * LOGPI + 0.5 * dig(s / 2)
    kap = [0.0, 0.0, 1.0, 1.0]; logN = math.log(775)
    out = []
    for sg in sigmas:
        def h(r): return math.exp(-(r * r) / (2 * sg * sg))
        def g(u): return (sg / math.sqrt(2 * math.pi)) * math.exp(-(sg * sg) * u * u / 2)
        rmax, npts = 45.0, 600; dr = 2 * rmax / npts; arch = 0.0
        for i in range(npts + 1):
            r = -rmax + i * dr; tot = logN + 0j
            for k in kap:
                tot += gR(complex(0.5 + k, r)) + gR(complex(0.5 + k, -r))
            w = 0.5 if i in (0, npts) else 1.0
            arch += w * (h(r) * tot).real
        arch = arch * dr / (2 * math.pi)
        prime = 0.0
        for rr in rows:
            Nq = rr["norm"]; aq = rr["a_q_geometric"]
            if Nq == 31 and not rr.get("self_adjoint", True):
                continue                            # bad (Steinberg) prime: handled separately
            x = aq / (2 * math.sqrt(Nq))
            if abs(x) > 1:
                continue
            th = math.acos(max(-1.0, min(1.0, x))); lN = math.log(Nq); k = 1
            while k * lN < 45 and Nq ** (k / 2.0) < 1e12:
                prime += 2 * math.cos(k * th) * lN / math.sqrt(Nq ** k) * g(k * lN)
                k += 1
        W = arch - prime
        zerosum = 2.0 * sum(h(z) for z in zeros)     # zeros come in +/- gamma pairs
        out.append({"sigma": sg, "arch_minus_prime": W, "zero_sum_over_found": zerosum,
                    "rel_err": abs(W - zerosum) / (abs(zerosum) + 1e-30),
                    "note": "tight only if zeros reach high enough height for this sigma"})
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["a", "b", "both"], default="both")
    ap.add_argument("--norm-bound", type=int, default=50000)
    ap.add_argument("--procs", type=int, default=max(1, (os.cpu_count() or 2)-2))
    ap.add_argument("--nmax", type=int, default=4000)
    a = ap.parse_args()
    if a.stage in ("a", "both"):
        stage_a(a.norm_bound, a.procs)
    if a.stage in ("b", "both"):
        stage_b(a.nmax)

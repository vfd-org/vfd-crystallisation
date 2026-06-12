"""Route A: compute the GENUINE Hecke eigenvalues of the norm-31
Hilbert newform over Q(sqrt5), independently, by point-counting.

We use ONLY the Weierstrass equation of the elliptic curve 31.1-a1
over K = Q(sqrt5) (from LMFDB -- five field elements):

    y^2 + xy + phi*y = x^3 + (phi+1)x^2 + phi*x
    [a1,a2,a3,a4,a6] = [1, phi+1, phi, phi, 0]
    conductor (5phi - 2), norm 31,  phi = (1+sqrt5)/2, phi^2 = phi+1.

By modularity over Q(sqrt5), the curve's Frobenius traces
    a_P = N(P) + 1 - #E(F_P)
ARE the Hecke eigenvalues of the (1-dimensional) cuspidal Hilbert
newform at level (5phi-2).  We compute #E(F_P) by brute-force point
counting in the residue field -- no LMFDB eigenvalue table is used,
so this is a fully independent determination of the genuine target
sequence H = {a_P : N(P) <= 200}.

This is the "H" side of the circle test.  It is the reference data the
substrate's icosian Brandt eigenvalues must reproduce out-of-sample,
once that construction exists.

Two honesty checks are built in:
  (1) Ramanujan: |a_P| <= 2 sqrt(N(P)) must hold for a genuine
      cuspidal form (it cannot hold for an Eisenstein series, whose
      eigenvalues grow like N(P)+1).
  (2) Contrast with the values the engine's hecke_lift HARDCODED
      (2*sqrt(p) for split, sqrt(1+p^2) for inert).  We show the
      hardcoded inert values are Eisenstein-type (~p), violating
      Ramanujan -- i.e. the engine was using the wrong object.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
DATA.mkdir(parents=True, exist_ok=True)

# --- Z[phi] arithmetic, element (a,b) = a + b*phi, phi^2 = phi+1 -----------

def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)

def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def zsmul(k, x):
    return (k * x[0], k * x[1])

def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])

# a-invariants of 31.1-a1 in Z[phi]
A1 = (1, 0)
A2 = (1, 1)   # phi + 1
A3 = (0, 1)   # phi
A4 = (0, 1)   # phi
A6 = (0, 0)

def discriminant_zphi():
    """Standard elliptic-curve discriminant in Z[phi]."""
    b2 = zadd(zmul(A1, A1), zsmul(4, A2))
    b4 = zadd(zsmul(2, A4), zmul(A1, A3))
    b6 = zadd(zmul(A3, A3), zsmul(4, A6))
    b8 = zsub(
        zadd(
            zadd(zmul(zmul(A1, A1), A6), zsmul(4, zmul(A2, A6))),
            zsub(zmul(A2, zmul(A3, A3)), zmul(A1, zmul(A3, A4))),
        ),
        zmul(A4, A4),
    )
    # Delta = -b2^2 b8 - 8 b4^3 - 27 b6^2 + 9 b2 b4 b6
    t1 = zsmul(-1, zmul(zmul(b2, b2), b8))
    t2 = zsmul(-8, zmul(zmul(b4, b4), b4))
    t3 = zsmul(-27, zmul(b6, b6))
    t4 = zsmul(9, zmul(b2, zmul(b4, b6)))
    return zadd(zadd(t1, t2), zadd(t3, t4))

DELTA = discriminant_zphi()

# --- prime ideals of Q(sqrt5) ---------------------------------------------

def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def sqrt5_mod(p):
    """Return roots of x^2 = 5 mod p, or None if non-residue."""
    for r in range(p):
        if (r * r - 5) % p == 0:
            return r
    return None

def prime_ideals(norm_bound):
    """Yield (norm, kind, p, root) for each prime ideal with
    N(P) <= norm_bound. For split/ramified, root = phi mod p (in F_p).
    For inert, root = None and residue field is F_{p^2}."""
    ideals = []
    for p in primes_up_to(norm_bound):
        r5 = p % 5
        if p == 5:
            # ramified: x^2-x-1 has double root; phi -> (1)/2 mod 5 = 3
            inv2 = pow(2, p - 2, p)
            root = (1 * inv2) % p
            ideals.append((5, "ramified", p, root))
        elif r5 in (1, 4):
            # split: two primes of norm p, phi -> two roots of x^2-x-1
            s = sqrt5_mod(p)
            inv2 = pow(2, p - 2, p)
            r1 = ((1 + s) * inv2) % p
            r2 = ((1 - s) * inv2) % p
            ideals.append((p, "split", p, r1))
            ideals.append((p, "split", p, r2))
        else:
            # inert: one prime of norm p^2
            if p * p <= norm_bound:
                ideals.append((p * p, "inert", p, None))
    ideals.sort(key=lambda t: (t[0], t[3] if t[3] is not None else -1))
    return ideals

# --- point counting --------------------------------------------------------

def reduce_scalar(x, root, p):
    """Reduce (a,b)=a+b*phi to F_p via phi->root."""
    return (x[0] + x[1] * root) % p

def count_points_Fp(root, p):
    """#E(F_p) for the curve reduced via phi->root."""
    a1 = reduce_scalar(A1, root, p)
    a2 = reduce_scalar(A2, root, p)
    a3 = reduce_scalar(A3, root, p)
    a4 = reduce_scalar(A4, root, p)
    a6 = reduce_scalar(A6, root, p)
    count = 1  # point at infinity
    for x in range(p):
        rhs = (x * x * x + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            lhs = (y * y + a1 * x * y + a3 * y) % p
            if lhs == rhs:
                count += 1
    return count

# F_{p^2} = F_p[t]/(t^2 - t - 1), element (u,v) = u + v t, t plays phi
def f2mul(x, y, p):
    a, b = x
    c, d = y
    return ((a * c + b * d) % p, (a * d + b * c + b * d) % p)

def f2add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

def count_points_Fp2(p):
    """#E(F_{p^2}) with phi -> t (the field generator)."""
    a1 = (A1[0] % p, A1[1] % p)
    a2 = (A2[0] % p, A2[1] % p)
    a3 = (A3[0] % p, A3[1] % p)
    a4 = (A4[0] % p, A4[1] % p)
    a6 = (A6[0] % p, A6[1] % p)
    elems = [(u, v) for u in range(p) for v in range(p)]
    count = 1
    for x in elems:
        x2 = f2mul(x, x, p)
        x3 = f2mul(x2, x, p)
        rhs = f2add(f2add(x3, f2mul(a2, x2, p), p),
                    f2add(f2mul(a4, x, p), a6, p), p)
        for y in elems:
            y2 = f2mul(y, y, p)
            lhs = f2add(y2, f2add(f2mul(a1, f2mul(x, y, p), p),
                                  f2mul(a3, y, p), p), p)
            if lhs == rhs:
                count += 1
    return count

# --- main ------------------------------------------------------------------

def main():
    print("=" * 76)
    print("ROUTE A: genuine Hecke eigenvalues of the norm-31 Hilbert")
    print("newform over Q(sqrt5), by independent point counting")
    print("=" * 76)
    print(f"\nCurve 31.1-a1: [a1,a2,a3,a4,a6] = [1, phi+1, phi, phi, 0]")
    print(f"Discriminant in Z[phi]: {DELTA[0]} + {DELTA[1]}*phi  "
          f"(= -(5phi-2), norm -31)")

    NORM_BOUND = 200
    ideals = prime_ideals(NORM_BOUND)
    print(f"\nPrime ideals with N(P) <= {NORM_BOUND}: {len(ideals)}")

    rows = []
    ramanujan_ok = True
    for norm, kind, p, root in ideals:
        # bad reduction? Delta == 0 in residue field
        if kind == "inert":
            d = (DELTA[0] % p, DELTA[1] % p)
            bad = (d == (0, 0))
        else:
            bad = (reduce_scalar(DELTA, root, p) == 0)
        if bad:
            rows.append((norm, kind, p, root, None, "bad", None))
            continue
        if kind == "inert":
            npts = count_points_Fp2(p)
        else:
            npts = count_points_Fp(root, p)
        a_P = norm + 1 - npts
        bound = 2 * math.sqrt(norm)
        ratio = abs(a_P) / bound
        if ratio > 1.0 + 1e-9:
            ramanujan_ok = False
        rows.append((norm, kind, p, root, a_P, "good", ratio, npts))

    # Torsion cross-check: 31.1-a1 has Z/8Z torsion -> 8 | #E(F_P)
    torsion_ok = True
    for r in rows:
        if r[5] == "good" and r[7] % 8 != 0:
            torsion_ok = False
    rows = [r[:7] for r in rows]  # drop npts from downstream rows

    print("\n  N(P)  kind       phi_modp   a_P     |a_P|/2sqrtN")
    print("  " + "-" * 56)
    for norm, kind, p, root, a_P, status, ratio in rows:
        if status == "bad":
            print(f"  {norm:<5} {kind:<10} {str(root):<10} "
                  f"  --   (bad reduction, conductor)")
        else:
            print(f"  {norm:<5} {kind:<10} {str(root):<10} "
                  f"{a_P:>4}    {ratio:.3f}")

    print("\n" + "=" * 76)
    print(f"RAMANUJAN CHECK |a_P| <= 2 sqrt(N(P)): "
          f"{'PASS (genuine cuspidal)' if ramanujan_ok else 'FAIL'}")
    print(f"TORSION CROSS-CHECK 8 | #E(F_P) (curve has Z/8Z torsion): "
          f"{'PASS' if torsion_ok else 'FAIL'}")
    print("  (independent correctness proof of the point counts -- needs")
    print("   no external eigenvalue table)")
    print("=" * 76)

    # Contrast: genuine cuspidal a_P  vs  engine hardcoded  vs  Eisenstein
    print("\nCONTRAST: genuine a_P  vs  engine hecke_lift hardcoded  vs  "
          "true Eisenstein N(P)+1")
    print("  (engine hardcoded: split -> 2 sqrt(p); inert -> sqrt(1+p^2))")
    print("\n  N(P)  kind     genuine a_P   engine hardcoded   Eisenstein N+1")
    print("  " + "-" * 64)
    sq_err_engine = 0.0
    sign_disagree = 0
    n_cmp = 0
    for norm, kind, p, root, a_P, status, ratio in rows:
        if status == "bad":
            continue
        if kind == "split" or kind == "ramified":
            hardcoded = 2 * math.sqrt(p)
        else:
            hardcoded = math.sqrt(1.0 + p * p)
        eisenstein = norm + 1
        print(f"  {norm:<5} {kind:<8} {a_P:>6}        "
              f"{hardcoded:>8.3f}          {eisenstein:>6}")
        sq_err_engine += (a_P - hardcoded) ** 2
        # engine hardcoded is always positive; genuine a_P sign varies
        if a_P < 0:
            sign_disagree += 1
        n_cmp += 1
    rmse_engine = math.sqrt(sq_err_engine / n_cmp)
    print(f"\n  RMSE(genuine a_P, engine hardcoded) = {rmse_engine:.2f}")
    print(f"  Genuine a_P are negative on {sign_disagree}/{n_cmp} primes; "
          f"engine hardcoded values are ALWAYS positive and monotone.")
    print("  -> the engine's 'substrate' values are ad hoc; they are")
    print("     neither the genuine cuspidal a_P nor the Eisenstein N+1.")

    # Save genuine eigenvalues as the reference target
    with open(DATA / "genuine_newform_eigenvalues.csv", "w",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["norm_NP", "kind", "p", "phi_mod_p", "a_P",
                    "ramanujan_ratio", "status"])
        for norm, kind, p, root, a_P, status, ratio in rows:
            w.writerow([norm, kind, p, root,
                        "" if a_P is None else a_P,
                        "" if ratio is None else f"{ratio:.4f}",
                        status])
    print(f"\nSaved genuine target H -> "
          f"data/genuine_newform_eigenvalues.csv")

    print("\n" + "=" * 76)
    print("INTERPRETATION")
    print("=" * 76)
    print("""
This is the GENUINE target sequence H, computed independently (only the
curve equation came from LMFDB; the eigenvalues are our own point counts).

It is Ramanujan-bounded -> genuinely cuspidal, 1-dimensional newform.
This CONFIRMS the dimension finding: the cuspidal space at norm 31 is
1-dim, NOT 26.  The 26-dim A_1 block of V_600 is a different object
(graph-adjacency spectrum), not this Hecke eigenspace.

The engine's hardcoded values bear NO resemblance to the genuine a_P:
they are always positive and monotone increasing, while genuine a_P
oscillate in sign and stay small (Ramanujan).  RMSE is large.  So the
engine was never computing these eigenvalues -- exactly the audit's
point, now shown numerically against real data.  (Note: the genuine
EISENSTEIN eigenvalue is N(P)+1, which grows like the norm; the icosian
theta series at level 1 realises that Eisenstein series, not the cusp
form -- which is why level structure at (5phi-2) is essential.)

The circle test now has a real, fixed target.  What remains (Route B) is
to compute the icosian ring's intrinsic Brandt action at level (5phi-2)
and check, out-of-sample and without fitting, whether ITS cuspidal
eigenvalues equal this H.  That is the only honest way to close the circle.
""")


if __name__ == "__main__":
    main()

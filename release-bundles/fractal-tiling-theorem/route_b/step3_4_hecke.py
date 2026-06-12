"""Route B, steps 3-4: Hecke eigenvalues at level (5phi-2), and the
circle test against the genuine target H.

Model (class number 1, Voight Ch. 41 / Dembele): the level-(5phi-2)
modular space is C[O^x \\ P^1(F_31)] = the 2 orbits found in step2
(sizes 12 and 20).  For a prime q (q != p, q split in B), the Hecke
operator T_q acts by summing the action of the norm-q quaternions:

   (T_q f)(L_i) = (1/|O^x|) * sum_{x: nrd(x)=nu_q} f( rho(x) . L_i )

where nu_q is a totally-positive generator of q, rho is the local
splitting B (x) F_31 ~ M_2(F_31) (step2), and the sum over all 120*(q+1)
norm-nu elements equals (q+1) coset reps after dividing by |O^x|=120.

T_q is a 2x2 matrix on the 2 orbits.  The all-ones vector is the
Eisenstein eigenvector with eigenvalue N(q)+1 (row sums); the OTHER
eigenvalue is the cuspidal a_q.  For a 2x2 with one eigenvalue N(q)+1,
   a_q = trace(T_q) - (N(q)+1).

Self-checks: (i) row sums == N(q)+1 (Eisenstein), (ii) |a_q| <= 2 sqrt(N(q))
(Ramanujan / cusp form).  THE test: a_q == genuine H from Route A.
"""
from __future__ import annotations

import csv
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import icosian as ico
import short_vectors as sv
import step2_eichler as st2

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"


def reconstruct_quaternion(c, basis):
    x = [(Fraction(0), Fraction(0)) for _ in range(4)]
    for i in range(8):
        if c[i] == 0:
            continue
        bi = basis[i]
        for k in range(4):
            x[k] = (x[k][0] + c[i] * bi[k][0], x[k][1] + c[i] * bi[k][1])
    return tuple(x)


def field_norm(nu):
    a, b = nu
    return int(a * a + a * b - b * b)


def load_target():
    H = {}
    with open(DATA / "genuine_newform_eigenvalues.csv") as f:
        for row in csv.DictReader(f):
            if row["status"] == "good":
                H.setdefault(int(row["norm_NP"]), []).append(int(row["a_P"]))
    return H


def main():
    print("=" * 74)
    print("ROUTE B steps 3-4: Hecke eigenvalues at level (5phi-2)")
    print("=" * 74)

    # 1) lattice + all norm-nu elements up to trace bound
    basis, GL, GLf = sv.build_lattice()
    M = 13                     # covers reduced norms up to N=41
    vecs = sv.enumerate_short(GL, GLf, M)
    by_nu = defaultdict(list)
    for c in vecs:
        nu = sv.reduced_norm_of_combo(c, basis)
        by_nu[(nu[0], nu[1])].append(reconstruct_quaternion(c, basis))
    print(f"\nEnumerated {len(vecs)} icosians (Q<= {M}); "
          f"{len(by_nu)} distinct reduced norms.")

    # 2) orbits on P^1(F_31) from step2
    units = ico.unit_icosians()
    mats = [st2.quat_to_matrix(q) for q in units]
    pts = st2.p1_points()
    idx = {pt: n for n, pt in enumerate(pts)}
    parent = list(range(len(pts)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb
    for Mt in mats:
        for pt in pts:
            union(idx[pt], idx[st2.act(Mt, pt)])
    orbit_id = {}
    reps = {}
    for i in range(len(pts)):
        r = find(i)
        if r not in reps:
            reps[r] = i
        orbit_id[i] = r
    orbit_roots = sorted(set(orbit_id.values()),
                         key=lambda r: -sum(1 for i in orbit_id
                                            if orbit_id[i] == r))
    # orbit index 0 = larger orbit, 1 = smaller (consistent labels)
    oindex = {r: k for k, r in enumerate(orbit_roots)}
    rep_pts = [pts[reps[r]] for r in orbit_roots]
    print(f"Orbits: sizes "
          f"{[sum(1 for i in orbit_id if orbit_id[i]==r) for r in orbit_roots]}")

    # 3) totally-positive prime generators (pick one generator per prime)
    targets = [
        ("(2)",      (Fraction(2), Fraction(0)),  4),    # inert 2
        ("(sqrt5)",  (Fraction(2), Fraction(1)),  5),    # ramified
        ("(3)",      (Fraction(3), Fraction(0)),  9),    # inert 3
        ("(11)a",    (Fraction(3), Fraction(2)),  11),   # split 11
        ("(11)b",    (Fraction(5), Fraction(-2)), 11),   # split 11 conj
        ("(19)a",    (Fraction(5), Fraction(-1)), 19),   # split 19  (OUT OF SAMPLE)
        ("(19)b",    (Fraction(4), Fraction(1)),  19),
        ("(29)a",    (Fraction(6), Fraction(-1)), 29),   # split 29
        ("(29)b",    (Fraction(5), Fraction(1)),  29),
        ("(41)a",    (Fraction(6), Fraction(1)),  41),   # split 41
        ("(41)b",    (Fraction(7), Fraction(-1)), 41),
    ]

    H = load_target()
    print("\n  prime      N(q)  #norm-nu  q+1  rowsum  T_q       a_q  "
          "Raman?  H(N(q))")
    print("  " + "-" * 70)
    results = {}
    for label, nu, q in targets:
        xs = by_nu.get(nu, [])
        if not xs:
            print(f"  {label:<10} {q:<5} (no elements of reduced norm "
                  f"{nu} within Q<= {M})")
            continue
        # build 2x2 Hecke matrix Tm[i][j]: from orbit i rep, count
        # x with rho(x).L_i in orbit j, divided by |O^x|=120
        Tm = [[0, 0], [0, 0]]
        for k, root in enumerate(orbit_roots):
            Li = rep_pts[k]
            for x in xs:
                Mx = st2.quat_to_matrix(x)
                dest = st2.act(Mx, Li)
                j = oindex[orbit_id[idx[dest]]]
                Tm[k][j] += 1
        Tm = [[v // 120 for v in row] for row in Tm]
        rowsums = [sum(r) for r in Tm]
        trace = Tm[0][0] + Tm[1][1]
        a_q = trace - (q + 1)
        raman = abs(a_q) <= 2 * math.sqrt(q) + 1e-9
        Hvals = H.get(q, [])
        results.setdefault(q, []).append(a_q)
        print(f"  {label:<10} {q:<5} {len(xs):<9} {q+1:<4} {rowsums} "
              f"{Tm}   {a_q:>3}  {'yes' if raman else 'NO '}   {Hvals}")

    # circle test: do the substrate a_q match H (as multisets per norm)?
    print("\n" + "=" * 74)
    print("CIRCLE TEST (steps so far): substrate a_q vs genuine H")
    print("=" * 74)
    ok = True
    for q in sorted(results):
        sub = sorted(results[q])
        gen = sorted(H.get(q, []))
        # compare as multisets where both available (split primes give 2)
        match = all(s in gen for s in sub)
        ok = ok and match
        print(f"  N(q)={q:<4} substrate {sub}   genuine {gen}   "
              f"{'MATCH' if match else 'mismatch'}")
    print("\n  " + ("ALL TESTED PRIMES MATCH -> substrate reproduces the "
                    "genuine newform" if ok else
                    "mismatch -> investigate Hecke normalisation or "
                    "generator/labelling"))

    # save substrate eigenvalues
    with open(DATA / "substrate_hecke_eigenvalues.csv", "w",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["N_q", "substrate_a_q", "genuine_H", "match"])
        for q in sorted(results):
            sub = sorted(results[q]); gen = sorted(H.get(q, []))
            w.writerow([q, sub, gen, all(s in gen for s in sub)])
    print(f"\n  Saved -> data/substrate_hecke_eigenvalues.csv")


if __name__ == "__main__":
    main()

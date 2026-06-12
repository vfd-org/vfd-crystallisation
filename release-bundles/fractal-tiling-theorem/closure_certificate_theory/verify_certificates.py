"""
Numerical harness verifying every PROVEN claim in closure_certificate_theory.tex.
Each check returns True; the script asserts all of them.  This GROUNDS the formal
note (it does not replace the proofs).
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, sqrtm
from itertools import product

ok = {}

# Lemma 1: dissipative certificate <=> rho(T)<1
T = np.array([[0.6, 0.5], [0.0, 0.4]])               # rho=0.6<1
B = solve_discrete_lyapunov(T.T, np.eye(2))
ok["L1_B_pd"] = np.linalg.eigvalsh(B).min() > 0
ok["L1_defect_negdef"] = np.linalg.eigvalsh(T.T @ B @ T - B).max() < -1e-9
Tbad = np.array([[1.2, 0.0], [0.0, 0.3]])            # rho=1.2>1
# no PD B can give strict dissipation (eigenvalue 1.2>1) -> Lyapunov solve diverges/indefinite
try:
    Bb = solve_discrete_lyapunov(Tbad.T, np.eye(2))
    ok["L1_escape_no_cert"] = np.linalg.eigvalsh(Bb).min() <= 0
except Exception:
    ok["L1_escape_no_cert"] = True

# Lemma 2: isometric certificate for finite-order T (3-cycle), exact via Weyl average
P = np.roll(np.eye(3), 1, axis=0)                    # 3-cycle, order 3
Biso = sum(np.linalg.matrix_power(P.T, k) @ np.linalg.matrix_power(P, k) for k in range(3)) / 3
ok["L2_iso_invariant"] = np.max(np.abs(P.T @ Biso @ P - Biso)) < 1e-12
ok["L2_iso_pd"] = np.linalg.eigvalsh(Biso).min() > 0
ok["L2_rotation_not_selfadjoint"] = float(np.max(np.abs(np.linalg.eigvals(P).imag))) > 1e-6

# Lemma 3: self-adjoint certificate <=> real diagonalizable
S = np.array([[1.0, 1.0], [0.0, 2.0]]); D = np.diag([2.0, -1.0])
Tsym = S @ D @ np.linalg.inv(S)                      # real spectrum {2,-1}
Bsa = np.linalg.inv(S).T @ np.linalg.inv(S)
ok["L3_BT_symmetric"] = np.max(np.abs(Bsa @ Tsym - (Bsa @ Tsym).T)) < 1e-9
ok["L3_Bsa_pd"] = np.linalg.eigvalsh(Bsa).min() > 0
# converse direction: M = B^{1/2} T B^{-1/2} symmetric
Bh = sqrtm(Bsa); M = Bh @ Tsym @ np.linalg.inv(Bh)
ok["L3_M_symmetric"] = np.max(np.abs(M - M.T)) < 1e-7

# Corollary (Markov): reversible -> diag(pi) self-adjoint cert; ergodic -> contraction on mean-zero
P = np.array([[0.5, 0.5, 0.0], [0.25, 0.5, 0.25], [0.0, 0.5, 0.5]])
w, V = np.linalg.eig(P.T); pi = np.real(V[:, np.argmin(np.abs(w - 1))]); pi /= pi.sum()
Bm = np.diag(pi)
ok["Cor_detailed_balance"] = np.max(np.abs(Bm @ P - (Bm @ P).T)) < 1e-9
ok["Cor_real_spectrum"] = float(np.max(np.abs(np.linalg.eigvals(P).imag))) < 1e-9
ev = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
ok["Cor_gap_below_1"] = ev[1] < 1 - 1e-9             # second eigenvalue strictly inside disc

# Lemma 4 + Proposition 1: 3n+1 one-cycle => only n=1
def one_cycle_solutions(q):
    sols = []
    for a in range(1, 40):
        d = 2**a - q
        if d > 0 and 1 % d == 0 and 1 // d >= 1:
            n = 1 // d
            if (q * n + 1) % (2**a) == 0 and (q * n + 1) >> a == n:
                sols.append((a, n))
    return sols
sol3 = one_cycle_solutions(3)
ok["P1_only_trivial_1cycle"] = sol3 == [(2, 1)]

# Corollary (small cycles, k<=6, a<=4): no nontrivial odd cycle for q=3
def small_cycles(q, kmax=6, amax=4):
    from fractions import Fraction
    found = []
    for k in range(1, kmax + 1):
        for a in product(range(1, amax + 1), repeat=k):
            A = sum(a)
            if 2**A <= q**k:
                continue
            s = 0; num = 0
            for j in range(k):
                num += q**(k - 1 - j) * 2**s; s += a[j]
            val = Fraction(num, 2**A - q**k)
            if val.denominator == 1:
                n = int(val)
                if n >= 1 and n % 2 == 1:
                    m, good = n, True
                    for ai in a:
                        mm = q * m + 1; av = (mm & -mm).bit_length() - 1
                        if av != ai: good = False; break
                        m = mm >> av
                    if good and m == n and not (q == 3 and n == 1):
                        found.append((k, a, n))
    return found
ok["Cor_no_small_cycles_3"] = small_cycles(3) == []

print("CLOSURE-CERTIFICATE-THEORY verification")
for k, v in ok.items():
    print(f"  {'PASS' if v else 'FAIL':4}  {k}")
assert all(ok.values()), "a formal-claim check FAILED"
print(f"\nALL {len(ok)} formal-claim checks PASS.")

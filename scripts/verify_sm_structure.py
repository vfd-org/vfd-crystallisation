#!/usr/bin/env python3
"""
Verify the two newly-closeable Standard-Model structure items
(docs/sm-closeability-audit.md; Paper LVIII):

  CH (chirality is structural):
      The arena's 4D rotation group is Spin(4) = SU(2)_left x SU(2)_right
      (left and right unit-quaternion multiplication). The rendered frame
      split (Papers LIII/LVI: right factor = spatial rotations of the
      scene, left factor = internal) then has a representation-theoretic
      consequence: fixing the complex structure J = right multiplication
      by i, the quaternions become the 2-complex-dimensional WEYL MODULE
      on which the LEFT factor acts complex-linearly as SU(2), while the
      RIGHT factor (the spatial one) is NOT complex-linear on it - it
      moves between chirality sectors. An internal SU(2) inherited from
      the left factor therefore acts on one chirality only.
      CH1  J^2 = -1; every left multiplication commutes with J (C-linear).
      CH2  in the complex basis {1, j}, left multiplication by each of
           the 120 substrate units is an SU(2) matrix, and the map is a
           group homomorphism (the standard 2I -> SU(2) inclusion).
      CH3  right multiplication is C-linear ONLY for the four units in
           the i-line {+-1, +-i}: the spatial factor does not act on the
           chiral module; generically [R_q, J] != 0.
      CH4  the left action leaves no real 1-dim invariant subspace of the
           module (it is the irreducible 2-dim complex rep, not a sum of
           characters).

  Q (electric charge is quantized in thirds, with the lepton/quark
     multiplet pattern):
      On the complexified octonions O (x) C with the SAME clock unit e1
      and complex structure J = L_{e1} used in Paper LVI, build three
      fermionic ladder operators from the three J-complex lines of the
      transverse space W = span(e2..e7). The number operator
      N = sum_k a_k! a_k has spectrum {0,1,2,3} with multiplicities
      {1,3,3,1}, and Q = N/3 gives charges {0, 1/3, 2/3, 1}: the
      magnitudes of (nu, anti-down, up, positron) - charge quantization
      in thirds with the correct multiplet sizes (Gunaydin-Gursey 1973;
      Furey 2016; re-derived here on the substrate's own octonions).
      Q1  the three ladder operators obey the fermionic algebra
          {a_i, a_j!} = delta_ij, {a_i, a_j} = 0 on the module.
      Q2  N has eigenvalues {0,1,2,3} with multiplicities {1,3,3,1}.
      Q3  the su(3) clock-stabiliser of Paper LVI commutes with N and
          acts irreducibly on each 3-dim eigenspace, trivially on the
          1-dim ones: the {1,3,3,1} are su(3) multiplets (lepton,
          quark-type triplets, lepton).
      Q4  null: building the ladder from a NON-J-compatible pairing
          destroys the integer spectrum.

Usage:
    python scripts/verify_sm_structure.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

rng = np.random.default_rng(20260614)

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def qmul(q1, q2):
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([a*e - b*f - c*g - d*h,
                     a*f + b*e + c*h - d*g,
                     a*g - b*h + c*e + d*f,
                     a*h + b*g - c*f + d*e])


def Lmat_q(q):
    return np.column_stack([qmul(q, e) for e in np.eye(4)])


def Rmat_q(q):
    return np.column_stack([qmul(e, q) for e in np.eye(4)])


# ======================================================================
# CH: chirality is structural
# ======================================================================

def ch_chirality():
    print("CH: the internal (left) factor is chiral")
    verts = np.load(DATA_PATH)["vertices"]
    J = Rmat_q(np.array([0.0, 1.0, 0.0, 0.0]))      # right mult by i
    check("CH1a J = R_i is a complex structure (J^2 = -1)",
          np.allclose(J @ J, -np.eye(4)))
    worst = max(np.max(np.abs(Lmat_q(v) @ J - J @ Lmat_q(v))) for v in verts)
    check("CH1b every left multiplication is C-linear ([L_q, J] = 0, "
          "all 120 units)", worst < 1e-12, f"max commutator {worst:.2e}")

    # complex basis {1, j} for H as a right-C module: x = 1 z1 + j z2
    def to_complex_matrix(M):
        """2x2 complex matrix of a J-commuting real 4x4 matrix in basis {1, j}."""
        e1 = np.array([1.0, 0, 0, 0])
        ej = np.array([0.0, 0, 1.0, 0])

        def coords(x):
            # x = 1*(a+bi) + j*(c-di)  for x = (a,b,c,d)
            return np.array([x[0] + 1j * x[1], x[2] - 1j * x[3]])
        return np.column_stack([coords(M @ e1), coords(M @ ej)])

    keys = {tuple(np.round(v, 8)): i for i, v in enumerate(verts)}
    mats = {}
    ok_su2 = True
    for i, v in enumerate(verts):
        U = to_complex_matrix(Lmat_q(v))
        mats[i] = U
        ok_su2 = ok_su2 and np.allclose(U.conj().T @ U, np.eye(2), atol=1e-10) \
            and abs(np.linalg.det(U) - 1) < 1e-10
    check("CH2a left multiplication acts as SU(2) on the Weyl module "
          "(unitary, det 1, all 120)", ok_su2)
    ok_hom = True
    for _ in range(60):
        i, j = rng.integers(len(verts), size=2)
        k = keys[tuple(np.round(qmul(verts[i], verts[j]), 8))]
        ok_hom = ok_hom and np.allclose(mats[i] @ mats[j], mats[k], atol=1e-9)
    check("CH2b the assignment is a group homomorphism (2I -> SU(2) "
          "inclusion)", ok_hom)

    clin = [i for i, v in enumerate(verts)
            if np.max(np.abs(Rmat_q(v) @ J - J @ Rmat_q(v))) < 1e-12]
    inline = sorted(tuple(np.round(verts[i], 4)) for i in clin)
    expected = sorted([(-1.0, -0.0, -0.0, -0.0), (-0.0, -1.0, -0.0, -0.0),
                       (0.0, 1.0, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0)])
    ok_right = len(clin) == 4 and all(
        abs(verts[i][2]) < 1e-9 and abs(verts[i][3]) < 1e-9 for i in clin)
    check("CH3 right (spatial) multiplication is C-linear only on the "
          "i-line {+-1, +-i}: the spatial factor is NOT an operator on "
          "the chiral module", ok_right,
          f"C-linear right units: {len(clin)}/120")
    _ = (inline, expected)

    # CH4: irreducibility. For a UNITARY 2-dim rep, reducible means a sum
    # of two characters, hence abelian image; so a non-abelian image is an
    # exact certificate of irreducibility.
    M1 = mats[rng.integers(len(verts))]
    found = None
    for i in range(len(verts)):
        if not np.allclose(mats[i] @ M1, M1 @ mats[i], atol=1e-9):
            found = mats[i]
            break
    check("CH4 the left action is irreducible (unitary 2-dim with "
          "non-abelian image: reducible would force abelian)",
          found is not None)

    # CH5: the mirror (conjugate) Weyl module. With the LEFT complex
    # structure J_L = L_i, the roles swap exactly: every RIGHT
    # multiplication is C-linear, and LEFT multiplication is C-linear only
    # on the i-line. The two factors each own one module.
    JL = Lmat_q(np.array([0.0, 1.0, 0.0, 0.0]))
    worstR = max(np.max(np.abs(Rmat_q(v) @ JL - JL @ Rmat_q(v))) for v in verts)
    clinL = [i for i, v in enumerate(verts)
             if np.max(np.abs(Lmat_q(v) @ JL - JL @ Lmat_q(v))) < 1e-12]
    check("CH5 mirror module (J_L = L_i): every right multiplication is "
          "C-linear; left only on the i-line - each factor owns exactly "
          "one Weyl module", worstR < 1e-12 and len(clinL) == 4,
          f"right worst {worstR:.1e}; C-linear left units {len(clinL)}/120")


# ======================================================================
# Q: charge quantization in thirds from the octonions
# ======================================================================

def cayley_dickson(mult):
    n = mult.shape[0]

    def conj_vec(v):
        w = v.copy()
        w[1:] *= -1
        return w

    big = np.zeros((2 * n, 2 * n, 2 * n))
    for i in range(2 * n):
        for j in range(2 * n):
            a = np.zeros(n); b = np.zeros(n)
            c = np.zeros(n); dd = np.zeros(n)
            (a if i < n else b)[i % n] = 1.0
            (c if j < n else dd)[j % n] = 1.0
            ac = np.einsum("i,j,ijk->k", a, c, mult)
            db = np.einsum("i,j,ijk->k", conj_vec(dd), b, mult)
            da = np.einsum("i,j,ijk->k", dd, a, mult)
            bc = np.einsum("i,j,ijk->k", b, conj_vec(c), mult)
            big[i, j, :n] = ac - db
            big[i, j, n:] = da + bc
    return big


def q_charges():
    print("Q: charge quantization in thirds (octonion ladder operators)")
    m1 = np.ones((1, 1, 1))
    m8 = cayley_dickson(cayley_dickson(cayley_dickson(m1)))

    def Lmat(x):
        return np.einsum("i,ijk->kj", x, m8)  # (L_x)_{kj} = (x e_j)_k

    e = np.eye(8)
    Jfull = Lmat(e[1])                          # L_{e1}, the clock unit
    # three J-complex lines in W = span(e2..e7): pair f with J f
    pairs = []
    used = set()
    for a in range(2, 8):
        if a in used:
            continue
        Jf = Jfull @ e[a]
        b = int(np.argmax(np.abs(Jf)))
        sgn = np.sign(Jf[b])
        pairs.append((a, b, sgn))
        used.update({a, b})
    check("Q0 the transverse space splits into exactly 3 J-complex lines",
          len(pairs) == 3, f"pairs {[(a,b) for a,b,_ in pairs]}")

    # fermionic ladder operators a_k = 1/2 (L_f - i L_{Jf}) on O (x) C
    A = [0.5 * (Lmat(e[a]) - 1j * sgn * Lmat(e[b])) for a, b, sgn in pairs]

    ok_acr = True
    ok_ann = True
    for i in range(3):
        for j in range(3):
            acr = A[i] @ A[j].conj().T + A[j].conj().T @ A[i]
            ann = A[i] @ A[j] + A[j] @ A[i]
            ok_acr = ok_acr and np.allclose(acr, np.eye(8) * (i == j), atol=1e-9)
            ok_ann = ok_ann and np.allclose(ann, 0, atol=1e-9)
    check("Q1 fermionic algebra: {a_i, a_j!} = delta_ij, {a_i, a_j} = 0",
          ok_acr and ok_ann)

    N = sum(a.conj().T @ a for a in A)
    evals = np.linalg.eigvalsh(N)
    evals_r = np.round(np.real(evals), 8)
    from collections import Counter
    spec = Counter(np.round(evals_r).astype(int))
    ok_spec = (np.max(np.abs(evals_r - np.round(evals_r))) < 1e-9
               and dict(spec) == {0: 1, 1: 3, 2: 3, 3: 1})
    check("Q2 number operator spectrum {0,1,2,3} with multiplicities "
          "{1,3,3,1}: Q = N/3 in {0, 1/3, 2/3, 1} - thirds quantization, "
          "lepton/quark pattern", ok_spec,
          f"spectrum {dict(sorted(spec.items()))}")

    # Q3: the su(3) clock-stabiliser commutes with N; 3-dim eigenspaces
    # are irreducible su(3) triplets, 1-dim ones trivial
    rows = []
    for i in range(8):
        for j in range(8):
            for mcomp in range(8):
                row = np.zeros((8, 8))
                row[mcomp, :] += m8[i, j, :]
                for a in range(8):
                    row[a, i] -= m8[a, j, mcomp]
                for b in range(8):
                    row[b, j] -= m8[i, b, mcomp]
                rows.append(row.ravel())
    Msys = np.array(rows)
    _, sv, vt = np.linalg.svd(Msys)
    nullity = int(np.sum(sv < 1e-9 * sv[0]))
    Dbasis = [vt[-(k + 1)].reshape(8, 8) for k in range(nullity)]
    Aim = np.array([D[:, 1] for D in Dbasis])
    rk = np.linalg.matrix_rank(Aim, tol=1e-9)
    _, _, vN = np.linalg.svd(Aim.T, full_matrices=True)
    stab = [sum(c * D for c, D in zip(co, Dbasis)) for co in vN[rk:]]
    ok_comm = all(np.max(np.abs(D.astype(complex) @ N - N @ D)) < 1e-8
                  for D in stab)
    lam, vec = np.linalg.eigh(N)
    # Irreducibility certificate: su(3) is simple (Paper LVI item SM4), so
    # a nonzero action on a 3-dim space is FAITHFUL (kernel is an ideal),
    # and the only nontrivial su(3) reps of dim <= 3 are the triplets.
    # Certificate: the restricted images span an 8-dimensional algebra.
    ok_irr = True
    dims = {}
    for target in (1, 2):
        Vs = vec[:, np.abs(lam - target) < 1e-8]
        Ms = [(Vs.conj().T @ D.astype(complex) @ Vs).ravel() for D in stab]
        dims[target] = np.linalg.matrix_rank(np.array(Ms), tol=1e-8)
        ok_irr = ok_irr and dims[target] == 8
    for target in (0, 3):
        Vs = vec[:, np.abs(lam - target) < 1e-8]
        Ms = [Vs.conj().T @ D.astype(complex) @ Vs for D in stab]
        ok_irr = ok_irr and all(np.max(np.abs(M)) < 1e-8 for M in Ms)
    check("Q3 su(3) commutes with N; restricted image is the FULL "
          "8-dim algebra on each 3-dim eigenspace (faithful => triplet, "
          "by simplicity) and zero on the 1-dim ones",
          ok_comm and ok_irr,
          f"image dims on N=1,2 eigenspaces: {dims[1]}, {dims[2]}")

    # Q4 null: a non-J-compatible pairing destroys the integer spectrum
    Abad = [0.5 * (Lmat(e[a]) - 1j * Lmat(e[(a % 6) + 2])) for a in (2, 4, 6)]
    Nbad = sum(a.conj().T @ a for a in Abad)
    ebad = np.linalg.eigvalsh(Nbad)
    ok_null = np.max(np.abs(ebad - np.round(ebad))) > 1e-3
    check("Q4 null: a non-J-compatible pairing has no integer charge "
          "spectrum", ok_null,
          f"max deviation from integers {np.max(np.abs(ebad - np.round(ebad))):.3f}")


def main():
    print("=" * 70)
    print("SM structure verification — chirality + charge quantization")
    print("=" * 70)
    ch_chirality()
    q_charges()
    print("=" * 70)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())

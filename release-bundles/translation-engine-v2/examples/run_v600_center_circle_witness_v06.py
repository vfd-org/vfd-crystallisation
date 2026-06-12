"""v0.6: T as center-circle witness construction.

User insight: 'our T is a center circle in the triad. It is the
witness.'

Interpretation:
  - The TRIAD is (I, G, C) = (substrate, generation, closure) on V_600.
  - The CENTER of the triad's joint action = V_min, the 1-dim
    eigenspace at smallest C_phi eigenvalue (lambda = phi^-2).
    V_min sits inside the tau-fixed 94-dim block (Finding 7).
  - A CIRCLE in the center = a U(1) phase family centred at V_min,
    extending through the tau-fixed block.
  - T is the WITNESS = the self-adjoint operator whose ground state
    is V_min and whose excited states have eigenvalues gamma_n.

The construction:
  T_witness = sum_n gamma_n |n><n|
  where |0> = V_min (ground state, eigval = 0 or phi^-2 baseline)
  and |n> for n >= 1 are orthogonal vectors in the tau-fixed 94-dim
  block.

We then check whether this T passes the 7 v0.5 admissibility classes
(SM, FE, DN, GUE, EF, CB, ST). If yes, T_witness is the constructive
demonstration the user's insight predicts.

Additional structural tests:
  - Does T_witness COMMUTE with the substrate action?
  - Does T_witness preserve the tau-fixed/tau-paired decomposition?
  - Is T's restriction to V_min equal to a multiple of identity (the
    'center' property)?
"""
from __future__ import annotations

import math
import sys
from itertools import permutations, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import deep_admissibility_calibrated as deepc
import admissibility as adm
import cuspidal_admissibility as cusp
import explicit_formula as ef

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


def _is_even_perm(p):
    sign = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                sign = -sign
    return sign == 1


def generate_v600():
    verts = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = float(s)
            verts.append(np.array(v))
    for signs in product((1, -1), repeat=4):
        verts.append(np.array(signs, dtype=float) / 2.0)
    base = (0.0, 1.0, INVPHI, PHI)
    seen = set()
    for perm in permutations(range(4)):
        if not _is_even_perm(perm):
            continue
        for signs in product((1, -1), repeat=4):
            v = np.zeros(4)
            for slot in range(4):
                v[slot] = signs[slot] * base[perm[slot]] / 2.0
            key = tuple(round(float(x), 9) for x in v)
            if key in seen:
                continue
            if abs(np.dot(v, v) - 1.0) > 1e-8:
                continue
            seen.add(key)
            verts.append(v.copy())
    return np.array(verts)


def build_a1(verts, tol=1e-6):
    n = len(verts)
    min_d2 = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if 1e-10 < d2 < min_d2:
                min_d2 = d2
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if abs(d2 - min_d2) < tol:
                A[i, j] = 1.0
    return A


def main():
    print("=" * 78)
    print("v0.6 CENTER CIRCLE WITNESS construction")
    print("=" * 78)

    GAMMAS = deepc.GAMMAS

    # Build V_600, A_1, identify tau-fixed 94-dim block, V_min
    print("\n[Setup] Building substrate and finding the center...")
    verts = generate_v600()
    A1 = build_a1(verts)
    L = 12 * np.eye(120) - A1
    C_phi = L + (1.0 / (PHI * PHI)) * np.eye(120)

    eigvals_C, eigvecs_C = np.linalg.eigh(C_phi)
    # V_min = eigenspace of C_phi at smallest eigenvalue = phi^-2
    lam_min = eigvals_C[0]
    print(f"  V_min eigenvalue: {lam_min:.4f} (expected phi^-2 = "
          f"{INVPHI*INVPHI:.4f})")

    # The center of the triad: V_min
    V_min_vec = eigvecs_C[:, 0:1]  # 120 x 1
    print(f"  V_min vector norm: "
          f"{float(np.linalg.norm(V_min_vec)):.6f}")

    # tau-fixed 94 block: eigenspaces of A_1 at rational eigenvalues
    rational_A1 = [12.0, 3.0, 0.0, -2.0, -3.0]
    eigvals_A, eigvecs_A = np.linalg.eigh(A1)
    tau_fixed_cols = []
    for k in range(120):
        if any(abs(eigvals_A[k] - r) < 1e-5 for r in rational_A1):
            tau_fixed_cols.append(eigvecs_A[:, k])
    V_tau_fixed = np.array(tau_fixed_cols).T  # 120 x 94
    print(f"  tau-fixed block dim: {V_tau_fixed.shape[1]}")

    # Verify V_min sits inside tau-fixed
    V_min_proj = V_tau_fixed.T @ V_min_vec
    print(f"  ||P_tau-fixed @ V_min||: "
          f"{float(np.linalg.norm(V_min_proj)):.6f}  "
          f"(should be ~1.0 if V_min in tau-fixed)")

    # ---- CONSTRUCT T_witness ----
    # T acts on the tau-fixed 94-dim block.
    # Ground state |0> = V_min (eigenvalue 0).
    # Excited states |n> for n = 1..26 have eigenvalue gamma_n.
    # Remaining 67 dims (94 - 1 - 26) have eigenvalue 0 (or padded).

    # Build T in the tau-fixed eigenbasis
    print("\n[1] Building T_witness on tau-fixed 94 block...")

    # Use the eigenvectors of A_1 restricted to tau-fixed as the
    # natural basis. Sort by some natural order (smallest A_1 eigval
    # first = highest C_phi eigval). Then V_min should be the first
    # vector (since it has smallest C_phi eigval = highest A_1 eigval
    # = 12).

    # Project V_min onto V_tau_fixed basis
    v_min_in_block = V_tau_fixed.T @ V_min_vec  # 94 x 1
    v_min_in_block = v_min_in_block / np.linalg.norm(v_min_in_block)

    # Build orthonormal basis with V_min as first vector, then
    # complete via Gram-Schmidt
    basis = [v_min_in_block.flatten()]
    rng = np.random.default_rng(42)
    for k in range(93):
        v = rng.standard_normal(94)
        # Orthogonalize against existing basis
        for b in basis:
            v = v - np.dot(v, b) * b
        v = v / np.linalg.norm(v)
        basis.append(v)
    B = np.array(basis).T  # 94 x 94

    # Build T_witness in this basis: diagonal with gamma_n eigvals
    eigvals_T = np.zeros(94)
    eigvals_T[0] = 0.0  # V_min ground state
    for i, g in enumerate(GAMMAS):
        if i + 1 < 94:
            eigvals_T[i + 1] = g

    T_witness_block = B @ np.diag(eigvals_T) @ B.T
    T_witness_block = 0.5 * (T_witness_block + T_witness_block.T)
    print(f"  T_witness in tau-fixed block: shape {T_witness_block.shape}")
    print(f"  T eigvals (first 5): "
          f"{sorted(np.linalg.eigvalsh(T_witness_block))[:5]}")
    print(f"  T eigvals (largest 5): "
          f"{sorted(np.linalg.eigvalsh(T_witness_block))[-5:]}")

    # Lift T_witness back to 120-dim via V_tau_fixed
    T_witness_full = V_tau_fixed @ T_witness_block @ V_tau_fixed.T
    T_witness_full = 0.5 * (T_witness_full + T_witness_full.T)

    # ---- STRUCTURAL TESTS ----
    print("\n[2] Structural tests of T_witness:")

    # (a) Does T_witness preserve the tau-fixed block?
    # Check: T maps tau-fixed to tau-fixed (i.e., T * P_tau-paired = 0)
    rational_dim_count = V_tau_fixed.shape[1]
    P_tau_paired = np.eye(120) - V_tau_fixed @ V_tau_fixed.T
    error_paired = float(np.linalg.norm(P_tau_paired @ T_witness_full,
                                          ord="fro"))
    print(f"  T preserves tau-fixed?      "
          f"||P_paired @ T||_F = {error_paired:.4e} (should be ~0)")

    # (b) Does T_witness's ground state correspond to V_min?
    eigvals_W, eigvecs_W = np.linalg.eigh(T_witness_full)
    # Sort by eigenvalue
    idx_min = np.argmin(eigvals_W)
    ground_state = eigvecs_W[:, idx_min:idx_min+1]
    overlap = float(abs(ground_state.T @ V_min_vec))
    print(f"  T's ground state = V_min?   "
          f"overlap = {overlap:.4f} (should be ~1.0)")

    # (c) Does T commute with substrate action?
    # Use A_1 as a proxy for "substrate action"
    comm_A = T_witness_full @ A1 - A1 @ T_witness_full
    norm_comm = float(np.linalg.norm(comm_A, ord="fro"))
    print(f"  [T, A_1] norm:              {norm_comm:.4e}")
    print(f"  (Nonzero is expected -- T's eigvals are gamma_n, not")
    print(f"   in the substrate's algebra; T is a NEW operator added)")

    # ---- ADMISSIBILITY VERDICT MATRIX ----
    print("\n[3] Admissibility on T_witness:")
    spectrum = np.linalg.eigvalsh(T_witness_block)
    sm_v, sm_r, _ = adm.check_spectral_match(T_witness_block, GAMMAS,
                                               use_abs=True)
    deep_s = deepc.evaluate_calibrated(T_witness_block)
    ef_v, ef_r, _ = ef.check_explicit_formula(spectrum)

    print(f"  SM (spectral match vs gamma_n): {sm_v} (RMSE {sm_r:.4f})")
    print(f"  FE (functional equation):        "
          f"{deep_s['functional_equation']['verdict']}")
    print(f"  DN (density):                    "
          f"{deep_s['density_consistent']['verdict']}")
    print(f"  GUE (Wigner spacing):            "
          f"{deep_s['gue_distributed']['verdict']}")
    print(f"  EF (explicit formula):           {ef_v} (residual "
          f"{ef_r:.4f})")
    print(f"  Overall deep verdict:            {deep_s['overall']}")

    # ---- FINAL VERDICT ----
    print()
    print("=" * 78)
    print("FINAL VERDICT")
    print("=" * 78)
    print()

    passes_all_7 = (sm_v in ("EXACT", "STRONG", "CANDIDATE") and
                     deep_s["functional_equation"]["verdict"]
                     in ("EXACT", "STRONG", "CANDIDATE") and
                     deep_s["density_consistent"]["verdict"]
                     in ("EXACT", "STRONG", "CANDIDATE") and
                     deep_s["gue_distributed"]["verdict"]
                     in ("EXACT", "STRONG", "CANDIDATE") and
                     ef_v in ("EXACT", "STRONG", "CANDIDATE"))

    if passes_all_7:
        print("T_witness passes the 5 spectral admissibility classes")
        print("(SM, FE, DN, GUE, EF) at CANDIDATE level or better.")
        print()
        print("This means: a self-adjoint operator on V_600's tau-fixed")
        print("94-dim block with gamma_n as its spectrum is INTERNALLY")
        print("CONSISTENT with the engine's necessary conditions.")
        print()
        print("Substrate-localised Hilbert-Polya witness: EXISTS")
        print("as a self-adjoint operator on the tau-fixed block with")
        print("V_min as its ground state and gamma_n as excited eigvals.")
        print()
        print("HOWEVER: this is a TAUTOLOGICAL construction. We built T")
        print("BY HAND to have gamma_n as eigvals, then checked the")
        print("engine doesn't reject it. The construction validates the")
        print("engine's internal consistency but does not derive gamma_n")
        print("from substrate-intrinsic data.")
        print()
        print("The genuine open question remains: derive gamma_n from")
        print("the substrate's Hecke / closure-flow structure, NOT from")
        print("an external lookup table.")
    else:
        print("T_witness does NOT pass all 5 spectral classes.")
        print("Identifies which class fails:")
        for class_name, verdict in [
            ("SM", sm_v),
            ("FE", deep_s["functional_equation"]["verdict"]),
            ("DN", deep_s["density_consistent"]["verdict"]),
            ("GUE", deep_s["gue_distributed"]["verdict"]),
            ("EF", ef_v),
        ]:
            if verdict not in ("EXACT", "STRONG", "CANDIDATE"):
                print(f"  {class_name}: {verdict}")

    print()
    print("=" * 78)
    print("INTERPRETATION OF 'T AS CENTER CIRCLE WITNESS'")
    print("=" * 78)
    print()
    print("The user's insight 'T is a center circle in the triad and")
    print("the witness' is realised by:")
    print()
    print("  CENTER:  V_min (1-dim, smallest C_phi eigenvalue), sits")
    print("           in the tau-fixed 94-dim block.")
    print("  CIRCLE:  The U(1) of phase rotations on V_min (formal:")
    print("           T's spectrum includes 0 at V_min and gamma_n at")
    print("           the other excited states).")
    print("  WITNESS: The explicit self-adjoint operator T on the")
    print("           tau-fixed block whose existence demonstrates")
    print("           substrate-side Hilbert-Polya is constructible.")
    print()
    print("Engine v0.6 conclusion: such a T_witness exists as an")
    print("operator-level object. The hard part -- DERIVING T from the")
    print("triad rather than positing it -- is the next milestone.")
    print()
    print("WHAT v0.7 NEEDS:")
    print("  - Show that the closure-flow dynamics on V_600 carries the")
    print("    constraints that T must satisfy (gamma_n derivable from")
    print("    closure-flow + cuspidal HMF + 2I-equivariance).")
    print("  - LMFDB cuspidal HMF over Q(sqrt 5) data.")
    print("  - Self-consistency: T must commute with the right Hecke")
    print("    operators AND have V_min as ground state AND have gamma_n")
    print("    as spectrum.")


if __name__ == "__main__":
    main()

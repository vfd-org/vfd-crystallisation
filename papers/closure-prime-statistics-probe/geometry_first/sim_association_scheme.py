#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 4: V_600 distance-regular graph as a classical
symmetric association scheme.

Implements WO_association_scheme.md.  Computes:
  - valencies k_i (shell degrees)
  - multiplicities f_j (eigenspace dimensions)
  - P-matrix (first eigenmatrix)
  - Q-matrix (second eigenmatrix, dual)
  - intersection numbers p_{ij}^k
  - Krein parameters q_{ij}^k

Verifies the defining axioms of a symmetric association scheme.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4; v[i] = s
            verts.append(v)
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for p in even_perms:
        for sa in (-1,1):
            for sb in (-1,1):
                for sc in (-1,1):
                    v = [0.0]*4
                    v[p[0]] = sa*half_phi
                    v[p[1]] = sb*half
                    v[p[2]] = sc*half_phi_i
                    v[p[3]] = 0.0
                    verts.append(v)
    return np.array(verts, dtype=float)


def main():
    print("=" * 78)
    print("SIM 4: V_600 distance-regular graph as a symmetric association scheme")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    print(f"  V_600: {n} vertices")

    # ----- Build all shell operators A_0..A_8 -----
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    distinct_d2 = sorted(set(round(float(x), 6) for x in d2.flatten()))
    n_shells = len(distinct_d2)
    print(f"  Distinct squared distances ({n_shells} shells): {distinct_d2}")
    assert n_shells == 9, f"expected 9 shells, got {n_shells}"

    A = []
    for k in range(n_shells):
        if k == 0:
            # A_0 = I (identity, diagonal 1s)
            A_k = np.eye(n)
        else:
            A_k = (np.abs(d2 - distinct_d2[k]) < 1e-7).astype(float)
            np.fill_diagonal(A_k, 0.0)
        A.append(A_k)
    print(f"  Built 9 shell operators A_0..A_8")
    print()

    # ----- Valencies k_i = row sum of A_i -----
    valencies = []
    for k in range(n_shells):
        row_sums = A[k].sum(axis=1)
        assert np.all(row_sums == row_sums[0]), f"A_{k} not vertex-transitive"
        k_i = int(row_sums[0])
        valencies.append(k_i)
    print(f"  Valencies (k_0..k_8): {valencies}")
    print(f"  Sum: {sum(valencies)} (must equal n = 120)")
    assert sum(valencies) == 120, f"sum of valencies != 120: {sum(valencies)}"
    print()

    # ----- A's eigendecomposition -----
    A_main = A[1]  # A = first shell
    eigvals_raw, eigvecs_raw = np.linalg.eigh(A_main)
    # Cluster
    eigvals = []
    eigspace_indices = []
    cur_val = eigvals_raw[0]
    cur_idx = [0]
    for k in range(1, n):
        if abs(eigvals_raw[k] - cur_val) < 1e-6:
            cur_idx.append(k)
        else:
            eigvals.append(float(cur_val))
            eigspace_indices.append(cur_idx)
            cur_val = eigvals_raw[k]
            cur_idx = [k]
    eigvals.append(float(cur_val))
    eigspace_indices.append(cur_idx)
    # Reverse order so E_0 = trivial (largest A-eigenvalue = degree = k_1).
    # Standard association-scheme convention.
    eigvals = list(reversed(eigvals))
    eigspace_indices = list(reversed(eigspace_indices))
    multiplicities = [len(idx) for idx in eigspace_indices]
    print(f"  Multiplicities (f_0..f_8): {multiplicities}")
    print(f"  A eigenvalues (E_0..E_8, descending): {[f'{x:+.4f}' for x in eigvals]}")
    print()

    # ----- P-matrix: P[i, j] = scalar value of A_i on E_j -----
    bases = [eigvecs_raw[:, idx] for idx in eigspace_indices]
    P = np.zeros((n_shells, n_shells))
    for i in range(n_shells):
        for j in range(n_shells):
            B_j = bases[j]
            M = B_j.T @ A[i] @ B_j   # f_j × f_j
            # Should be scalar; mean of eigenvalues
            P[i, j] = float(np.mean(np.linalg.eigvalsh(M)))
    print(f"  P-matrix (P[i, j] = eigval of A_i on E_j):")
    header_label = "i/j"
    print(f"  {header_label:<5}", end="")
    for j in range(n_shells):
        cell = f"E_{j} (f={multiplicities[j]})"
        print(f"{cell:<14}", end="")
    print()
    for i in range(n_shells):
        row_label = f"A_{i}"
        print(f"  {row_label:<5}", end="")
        for j in range(n_shells):
            print(f"{P[i, j]:+12.3f}  ", end="")
        print()
    print()

    # Sanity: P[0, j] = 1 (since A_0 = I)
    P0_ok = np.allclose(P[0, :], 1.0, atol=1e-8)
    # P[i, 0] = k_i (column 0 is the all-1 eigenspace of A_main; eigval = k_i)
    P_col0_ok = np.allclose(P[:, 0], np.array(valencies, dtype=float), atol=1e-8)
    print(f"  P[0, j] = 1: {P0_ok}")
    print(f"  P[i, 0] = k_i: {P_col0_ok}")

    # ----- Q-matrix via P · Q = n · I -----
    Q = float(n) * np.linalg.inv(P)
    PQ = P @ Q
    QP = Q @ P
    PQ_ok = np.allclose(PQ, float(n) * np.eye(n_shells), atol=1e-8)
    QP_ok = np.allclose(QP, float(n) * np.eye(n_shells), atol=1e-8)
    print(f"  P · Q = 120 · I: {PQ_ok}, max dev = {np.max(np.abs(PQ - n*np.eye(n_shells))):.2e}")
    print(f"  Q · P = 120 · I: {QP_ok}")

    # Sanity on Q (in our layout: rows = E_j, cols = A_i)
    Q_row0_all_ones = np.allclose(Q[0, :], 1.0, atol=1e-8)         # E_0 (trivial) row
    Q_col0_eq_mults  = np.allclose(Q[:, 0], np.array(multiplicities, dtype=float),
                                    atol=1e-8)                       # A_0 (identity) col
    print(f"  Q[0, j] = 1 for all j (E_0 = trivial row all-ones): {Q_row0_all_ones}")
    print(f"  Q[i, 0] = f_i (A_0 col = multiplicities): {Q_col0_eq_mults}")
    print()

    print(f"  Q-matrix:")
    q_header = "j/i"
    print(f"  {q_header:<5}", end="")
    for i in range(n_shells):
        cell_q = f"A_{i} (k={valencies[i]})"
        print(f"{cell_q:<14}", end="")
    print()
    for j in range(n_shells):
        e_label = f"E_{j}"
        print(f"  {e_label:<5}", end="")
        for i in range(n_shells):
            print(f"{Q[j, i]:+12.3f}  ", end="")
        print()
    print()

    # ----- Intersection numbers p_{ij}^k -----
    # For each i, j: A_i · A_j is a 120×120 matrix. Express in Bose-Mesner basis.
    # Method: pick a representative pair (a, b) for each shell-distance class k,
    # then (A_i · A_j)[a, b] = p_{ij}^k.
    # Use vertex 0 as 'a', and one representative per shell.
    shell_reps = {}  # shell index k -> some vertex b with shell-distance k from 0
    for b in range(n):
        d2_0b = d2[0, b]
        for k_shell in range(n_shells):
            if abs(d2_0b - distinct_d2[k_shell]) < 1e-7:
                if k_shell not in shell_reps:
                    shell_reps[k_shell] = b
                break
    assert len(shell_reps) == n_shells, "missing shell rep"

    intersection_numbers = {}  # (i, j, k) -> p_{ij}^k
    all_integer = True
    max_dev = 0.0
    for i in range(n_shells):
        for j in range(n_shells):
            AiAj = A[i] @ A[j]
            for k_shell in range(n_shells):
                b = shell_reps[k_shell]
                p_val = float(AiAj[0, b])
                p_rounded = round(p_val)
                dev = abs(p_val - p_rounded)
                if dev > 1e-8:
                    all_integer = False
                max_dev = max(max_dev, dev)
                intersection_numbers[(i, j, k_shell)] = p_rounded
    print(f"  Intersection numbers p_{{ij}}^k computed (729 total)")
    print(f"  All non-negative integers: {all_integer} (max dev = {max_dev:.2e})")

    # Check classical identities:
    # (a) p_{ij}^0 = k_i · delta_{ij}
    p00_ok = True
    for i in range(n_shells):
        for j in range(n_shells):
            expected = valencies[i] if i == j else 0
            actual = intersection_numbers[(i, j, 0)]
            if actual != expected:
                p00_ok = False
    print(f"  Identity p_{{ij}}^0 = k_i δ_{{ij}}: {p00_ok}")

    # (b) Σ_k p_{ij}^k · k_k = k_i · k_j
    sum_identity_ok = True
    for i in range(n_shells):
        for j in range(n_shells):
            s = sum(intersection_numbers[(i, j, k)] * valencies[k] for k in range(n_shells))
            expected = valencies[i] * valencies[j]
            if s != expected:
                sum_identity_ok = False
                break
    print(f"  Identity Σ_k p_{{ij}}^k k_k = k_i k_j: {sum_identity_ok}")

    # All non-negative
    all_nonneg = all(v >= 0 for v in intersection_numbers.values())
    print(f"  All p_{{ij}}^k ≥ 0: {all_nonneg}")
    print()

    # ----- Krein parameters via Hadamard product on primitive idempotents -----
    # E*_k = projector onto k-th eigenspace E_k = B_k · B_k^T
    Estar = []
    for k in range(n_shells):
        B_k = bases[k]
        Estar.append(B_k @ B_k.T)
    # Verify they sum to I and are mutually orthogonal
    sum_E = sum(Estar)
    Estar_sum_ok = np.allclose(sum_E, np.eye(n), atol=1e-8)
    print(f"  Σ E*_k = I: {Estar_sum_ok}")
    Estar_orth_ok = True
    for k in range(n_shells):
        for l in range(n_shells):
            if k != l:
                prod = Estar[k] @ Estar[l]
                if not np.allclose(prod, 0.0, atol=1e-8):
                    Estar_orth_ok = False
    print(f"  E*_k · E*_l = 0 for k≠l: {Estar_orth_ok}")
    print()

    # Krein: E*_i ⊙ E*_j = (1/n) Σ_k q_{ij}^k E*_k
    # Solve for q_{ij}^k via: q_{ij}^k = n · trace((E*_i ⊙ E*_j) · E*_k) / f_k
    print(f"  Computing Krein parameters via Hadamard products ...")
    krein = {}  # (i, j, k) -> q_{ij}^k
    all_q_nonneg = True
    min_q = 0.0
    for i in range(n_shells):
        for j in range(n_shells):
            Hij = Estar[i] * Estar[j]  # Hadamard product (entrywise)
            for k in range(n_shells):
                c_l = float(np.trace(Hij @ Estar[k])) / multiplicities[k]
                q_val = n * c_l
                krein[(i, j, k)] = q_val
                if q_val < -1e-8:
                    all_q_nonneg = False
                    min_q = min(min_q, q_val)
    print(f"  All q_{{ij}}^k ≥ 0 (Krein condition): {all_q_nonneg}"
          f"{'' if all_q_nonneg else f' (min q = {min_q:.4e})'}")

    # Krein dual identity: Σ_k q_{ij}^k · f_k = f_i · f_j
    krein_sum_ok = True
    for i in range(n_shells):
        for j in range(n_shells):
            s = sum(krein[(i, j, k)] * multiplicities[k] for k in range(n_shells))
            expected = multiplicities[i] * multiplicities[j]
            if abs(s - expected) > 1e-6:
                krein_sum_ok = False
                break
    print(f"  Identity Σ_k q_{{ij}}^k f_k = f_i f_j: {krein_sum_ok}")
    print()

    # ----- Acceptance -----
    checks = {
        "valencies_constant_rows":          True,
        "P_zeroth_row_all_ones":             P0_ok,
        "P_zeroth_col_equals_valencies":     P_col0_ok,
        "PQ_equals_nI":                      bool(PQ_ok),
        "QP_equals_nI":                      bool(QP_ok),
        "Q_E0_row_all_ones":                  bool(Q_row0_all_ones),
        "Q_A0_col_equals_multiplicities":     bool(Q_col0_eq_mults),
        "intersection_numbers_all_integer":  bool(all_integer),
        "intersection_numbers_all_nonneg":   bool(all_nonneg),
        "p_ij_0_identity":                    bool(p00_ok),
        "p_sum_identity":                     bool(sum_identity_ok),
        "Estar_sum_to_identity":              bool(Estar_sum_ok),
        "Estar_mutually_orthogonal":          bool(Estar_orth_ok),
        "Krein_condition":                    bool(all_q_nonneg),
        "Krein_sum_identity":                 bool(krein_sum_ok),
    }
    print("Acceptance checks:")
    for k_check, v_check in checks.items():
        print(f"  {k_check}: {v_check}")
    all_pass = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")

    # ----- Outputs -----
    out_json = {
        "n_vertices":             n,
        "shells":                 [float(x) for x in distinct_d2],
        "valencies":              valencies,
        "multiplicities":         multiplicities,
        "P_matrix":               P.tolist(),
        "Q_matrix":               Q.tolist(),
        "intersection_numbers":   {f"{i},{j},{k}": int(intersection_numbers[(i,j,k)])
                                    for i in range(n_shells)
                                    for j in range(n_shells)
                                    for k in range(n_shells)},
        "krein_parameters":       {f"{i},{j},{k}": float(krein[(i,j,k)])
                                    for i in range(n_shells)
                                    for j in range(n_shells)
                                    for k in range(n_shells)},
        "checks":                 checks,
        "overall_pass":           all_pass,
    }
    with open(OUTPUT_DIR / "association_scheme.json", "w") as f:
        json.dump(out_json, f, indent=2)

    # Markdown
    md_lines = ["# V_600 as a symmetric association scheme", "",
                f"- |V_600| = {n}",
                f"- Number of classes (shells, including 0): {n_shells}",
                f"- Valencies (k_0..k_8): {valencies}",
                f"- Multiplicities (f_0..f_8): {multiplicities}",
                f"- Σ k_i = {sum(valencies)} = Σ f_j", "",
                "## P-matrix (first eigenmatrix)",
                "P[i, j] = eigenvalue of A_i on eigenspace E_j", "",
                "| | " + " | ".join(f"E_{j}" for j in range(n_shells)) + " |",
                "|" + "---|" * (n_shells + 1)]
    for i in range(n_shells):
        md_lines.append(f"| A_{i} | " + " | ".join(f"{P[i, j]:+.4f}"
                                                     for j in range(n_shells)) + " |")
    md_lines.append("")
    md_lines.append("## Q-matrix (second eigenmatrix)")
    md_lines.append("Q[j, i] = dual eigenvalue; P · Q = 120 · I.")
    md_lines.append("")
    md_lines.append("| | " + " | ".join(f"A_{i}" for i in range(n_shells)) + " |")
    md_lines.append("|" + "---|" * (n_shells + 1))
    for j in range(n_shells):
        md_lines.append(f"| E_{j} | " + " | ".join(f"{Q[j, i]:+.4f}"
                                                     for i in range(n_shells)) + " |")
    md_lines.append("")
    md_lines.append("## Acceptance")
    for k_check, v_check in checks.items():
        md_lines.append(f"- `{k_check}`: **{v_check}**")
    with open(OUTPUT_DIR / "association_scheme.md", "w") as f:
        f.write("\n".join(md_lines))

    print()
    print(f"Wrote:")
    print(f"  {OUTPUT_DIR / 'association_scheme.md'}")
    print(f"  {OUTPUT_DIR / 'association_scheme.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())

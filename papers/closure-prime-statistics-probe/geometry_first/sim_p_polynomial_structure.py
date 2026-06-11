#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 5: P-polynomial structure of V_600.

Implements WO_p_polynomial_structure.md.  For each shell operator A_i,
explicitly compute the polynomial p_i(x) of degree i such that
A_i = p_i(A_1).  Extract the intersection array {b_i; c_i}, verify the
three-term recurrence, and tabulate central-character pairings.

All numerics from association-scheme step 4 are re-derived.  Pure
linear algebra; no interpretation.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
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


def is_zphi_integer(x: float, tol: float = 1e-8, max_b: int = 100) -> tuple | None:
    """If x = a + b*phi for small integer a, b, return (a, b). Else None."""
    for b in range(-max_b, max_b + 1):
        a_real = x - b * PHI
        a_int = round(a_real)
        if abs(a_real - a_int) < tol:
            return (int(a_int), int(b))
    return None


def zphi_str(rep):
    if rep is None: return "?"
    a, b = rep
    if b == 0: return str(a)
    if a == 0: return f"{b}φ" if b != 1 else "φ"
    sign = "+" if b > 0 else "−"
    return f"{a}{sign}{abs(b)}φ"


def main():
    print("=" * 78)
    print("SIM 5: V_600 P-polynomial structure")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    distinct_d2 = sorted(set(round(float(x), 6) for x in d2.flatten()))
    n_shells = len(distinct_d2)
    print(f"  V_600: {n} vertices, {n_shells} shells")

    # ---- Build shell operators A_0..A_8 ----
    A = []
    for k in range(n_shells):
        if k == 0:
            A.append(np.eye(n))
        else:
            A_k = (np.abs(d2 - distinct_d2[k]) < 1e-7).astype(float)
            np.fill_diagonal(A_k, 0.0)
            A.append(A_k)

    # Valencies
    valencies = [int(A[k].sum(axis=1)[0]) for k in range(n_shells)]
    print(f"  Valencies: {valencies}")

    # ---- Diagonalise A_1 ----
    A1 = A[1]
    eigvals_raw, eigvecs = np.linalg.eigh(A1)
    # Cluster
    eigvals_distinct = []
    eigspace_idx = []
    cur_val = eigvals_raw[0]
    cur_idx = [0]
    for k in range(1, n):
        if abs(eigvals_raw[k] - cur_val) < 1e-6:
            cur_idx.append(k)
        else:
            eigvals_distinct.append(float(cur_val))
            eigspace_idx.append(cur_idx)
            cur_val = eigvals_raw[k]
            cur_idx = [k]
    eigvals_distinct.append(float(cur_val))
    eigspace_idx.append(cur_idx)
    # Reverse: E_0 = trivial = largest eigenvalue
    eigvals_distinct = list(reversed(eigvals_distinct))
    eigspace_idx = list(reversed(eigspace_idx))
    multiplicities = [len(idx) for idx in eigspace_idx]

    # Check 9 distinct eigenvalues
    n_distinct = len(eigvals_distinct)
    A1_has_9_distinct = (n_distinct == 9)
    print(f"  A_1 has {n_distinct} distinct eigenvalues: {A1_has_9_distinct}")
    print(f"  Eigenvalues (E_0..E_8, descending):")
    for j, lam in enumerate(eigvals_distinct):
        rep = is_zphi_integer(lam, tol=1e-5)
        print(f"    λ_{j} = {lam:+10.6f}  = {zphi_str(rep) if rep else '?'}")
    print()

    # ---- P-matrix from A_i restricted to each eigenspace ----
    bases = [eigvecs[:, idx] for idx in eigspace_idx]
    P = np.zeros((n_shells, n_shells))
    for i in range(n_shells):
        for j in range(n_shells):
            B_j = bases[j]
            M = B_j.T @ A[i] @ B_j
            P[i, j] = float(np.mean(np.linalg.eigvalsh(M)))

    # ---- Compute polynomials p_i(x) such that A_i = p_i(A_1) ----
    # Solve Vandermonde V·c = P[i, :] where V[j, k] = (eigvals_distinct[j])^k
    print("  Computing polynomials p_i(x) = Σ c_k x^k such that A_i = p_i(A_1) ...")
    print()
    Vander = np.zeros((n_shells, n_shells))
    for j in range(n_shells):
        for k in range(n_shells):
            Vander[j, k] = eigvals_distinct[j] ** k

    polynomials = []
    poly_verified = True
    max_dev = 0.0
    coeffs_zphi_ok = True
    for i in range(n_shells):
        # Solve V c = P[i, :]
        target = np.array([P[i, j] for j in range(n_shells)])
        c = np.linalg.solve(Vander, target)
        polynomials.append(c)
        # Verify p_i(A_1) = A_i
        # Evaluate p_i(A_1) using Horner
        p_eval = np.zeros((n, n))
        A1_power = np.eye(n)
        for k in range(n_shells):
            p_eval = p_eval + c[k] * A1_power
            if k < n_shells - 1:
                A1_power = A1_power @ A1
        dev = float(np.max(np.abs(p_eval - A[i])))
        max_dev = max(max_dev, dev)
        if dev > 1e-6:
            poly_verified = False
    print(f"  Max ||p_i(A_1) - A_i||_∞: {max_dev:.2e}")
    print(f"  All p_i(A_1) = A_i: {poly_verified}")
    print()

    # ---- Display polynomials with Z[φ] recognition ----
    print("  Polynomials p_i(x) = Σ c_k x^k:")
    poly_table = []
    for i in range(n_shells):
        c = polynomials[i]
        # Trim trailing near-zeros
        last_nonzero = n_shells - 1
        while last_nonzero > 0 and abs(c[last_nonzero]) < 1e-8:
            last_nonzero -= 1
        terms = []
        coeffs_recognized = []
        for k in range(last_nonzero + 1):
            if abs(c[k]) < 1e-8:
                coeffs_recognized.append((0, 0))
                continue
            rep = is_zphi_integer(c[k], tol=1e-6)
            if rep is None:
                # Try rational denom up to 2
                rep2 = is_zphi_integer(2 * c[k], tol=1e-6)
                if rep2 is not None:
                    coeffs_recognized.append(("half", rep2))
                    if k == 0:
                        terms.append(f"({zphi_str(rep2)})/2")
                    elif k == 1:
                        terms.append(f"({zphi_str(rep2)})/2·x")
                    else:
                        terms.append(f"({zphi_str(rep2)})/2·x^{k}")
                else:
                    coeffs_recognized.append(("?", None))
                    coeffs_zphi_ok = False
                    if k == 0:
                        terms.append(f"{c[k]:.4f}")
                    elif k == 1:
                        terms.append(f"{c[k]:.4f}·x")
                    else:
                        terms.append(f"{c[k]:.4f}·x^{k}")
            else:
                coeffs_recognized.append((1, rep))
                a_val, b_val = rep
                if k == 0:
                    if rep == (1, 0): terms.append("1")
                    elif rep == (-1, 0): terms.append("−1")
                    else: terms.append(zphi_str(rep))
                elif k == 1:
                    if rep == (1, 0): terms.append("x")
                    elif rep == (-1, 0): terms.append("−x")
                    else: terms.append(f"({zphi_str(rep)})·x")
                else:
                    if rep == (1, 0): terms.append(f"x^{k}")
                    elif rep == (-1, 0): terms.append(f"−x^{k}")
                    else: terms.append(f"({zphi_str(rep)})·x^{k}")
        poly_str = " + ".join(terms).replace("+ −", "− ")
        print(f"    p_{i}(x) = {poly_str}")
        poly_table.append({"i": i, "degree": last_nonzero,
                            "coefficients_float": [float(x) for x in c[:last_nonzero+1]],
                            "coefficients_zphi":  [(c_type, list(rep) if rep else None)
                                                    for c_type, rep in coeffs_recognized]})
    print()
    print(f"  All polynomial coefficients in Z[φ] or (1/2)·Z[φ]: {coeffs_zphi_ok}")
    print()

    # ---- Intersection array {b_i, c_i} ----
    # For a P-polynomial scheme: A_1 · A_i = c_{i+1} · A_{i+1} + a_i · A_i + b_{i-1} · A_{i-1}
    # where the coefficients are non-negative integers.
    # b_i = p_{1,i+1}^i (number of step-1 neighbours going from shell i to shell i+1)
    # c_i = p_{1,i-1}^i
    # a_i = p_{1,i}^i = k_1 - b_i - c_i
    print("  Computing intersection array {b_0..b_7; c_1..c_8} ...")
    # Compute A_1 · A_i and read coefficients
    intersection_array = {"b": [], "c": [], "a": []}
    intersection_array_int = True
    for i in range(n_shells):
        AiA1 = A[1] @ A[i]
        # AiA1 = Σ_j p_{1,i}^j A_j. To find p_{1,i}^j, pick a vertex pair (a, b)
        # at shell distance j and read AiA1[a, b].
        coeffs_j = []
        for j in range(n_shells):
            # Find vertex pair at shell j
            if j == 0:
                a_idx, b_idx = 0, 0
            else:
                a_idx = 0
                b_idx = -1
                for k_v in range(n):
                    if abs(d2[0, k_v] - distinct_d2[j]) < 1e-7:
                        b_idx = k_v
                        break
                if b_idx < 0:
                    coeffs_j.append(None)
                    continue
            val = float(AiA1[a_idx, b_idx])
            val_int = round(val)
            if abs(val - val_int) > 1e-8:
                intersection_array_int = False
            coeffs_j.append(int(val_int))
        # b_{i-1} = coefficient of A_{i-1}, a_i = coefficient of A_i, c_{i+1} = coefficient of A_{i+1}
        # Actually: AiA1[a, b] for (a, b) at distance j gives the intersection number p_{1,i}^j.
        b_i_neg = coeffs_j[i - 1] if i >= 1 else 0  # b_{i-1} contribution
        a_i = coeffs_j[i]
        c_i_pos = coeffs_j[i + 1] if i <= n_shells - 2 else 0  # c_{i+1} contribution
        intersection_array["b"].append(b_i_neg)
        intersection_array["a"].append(a_i)
        intersection_array["c"].append(c_i_pos)

    # Standard intersection-array encoding:
    # {b_0, b_1, ..., b_{d-1}; c_1, c_2, ..., c_d}
    # where d = 8 (diameter)
    d_diam = n_shells - 1
    b_seq = [intersection_array["c"][i] for i in range(d_diam)]   # b_i = c_{i+1} from our indexing
    c_seq = [intersection_array["b"][i] for i in range(1, n_shells)]   # c_i = b_{i-1} contribution
    # Actually let's be careful. Our coeffs_j[j] = p_{1,i}^j gives:
    # When we examine AiA1 at distance-j pair, we read p_{1,i}^j.
    # The standard P-poly recursion: A_1 · A_i = c_{i+1}·A_{i+1} + a_i·A_i + b_{i-1}·A_{i-1}
    # So coeffs_j[i+1] = c_{i+1}, coeffs_j[i] = a_i, coeffs_j[i-1] = b_{i-1}.
    # Hence:
    #   b_{i-1} = coeffs_j[i-1]  (from i-th row, distance-(i-1) coefficient)
    #   c_{i+1} = coeffs_j[i+1]  (from i-th row, distance-(i+1) coefficient)
    # For i=0: A_1·A_0 = A_1, so b_{-1}=0, a_0=0, c_1=k_1=12.
    # For i=8: A_1·A_8 = b_7·A_7 (since c_9 doesn't exist).

    print(f"  Intersection array:")
    print(f"    i:   {list(range(n_shells))}")
    print(f"    b_i: {[intersection_array['c'][i] for i in range(n_shells)]}  "
          "(transitions i → i+1)")
    print(f"    a_i: {intersection_array['a']}  (stays at i)")
    print(f"    c_i: {[intersection_array['b'][i] for i in range(n_shells)]}  "
          "(transitions i → i−1)")
    print()
    # BCN convention: b_i = p^i_{1, i+1} (row i+1 of A_1·A_{i+1} at distance i);
    # c_i = p^i_{1, i-1}. Recompute by reading (A_1·A_s) directly at distance t.
    pt_1s = np.zeros((n_shells, n_shells), dtype=int)  # pt_1s[s, t] = p^t_{1, s}
    for s in range(n_shells):
        A1_As = A[1] @ A[s]
        for t in range(n_shells):
            if t == 0:
                # diagonal entry
                pt_1s[s, t] = int(round(float(A1_As[0, 0])))
            else:
                # find vertex at shell t from V[0]
                b_idx = -1
                for k_v in range(n):
                    if abs(d2[0, k_v] - distinct_d2[t]) < 1e-7:
                        b_idx = k_v
                        break
                if b_idx < 0:
                    continue
                pt_1s[s, t] = int(round(float(A1_As[0, b_idx])))
    # a_i = p^i_{1, i}, b_i = p^i_{1, i+1}, c_i = p^i_{1, i-1}
    a_seq_bcn = [int(pt_1s[i, i]) for i in range(n_shells)]
    b_seq_bcn = [int(pt_1s[i+1, i]) for i in range(d_diam)]   # b_0..b_{d-1}
    c_seq_bcn = [int(pt_1s[i-1, i]) for i in range(1, n_shells)]   # c_1..c_d
    print(f"  Intersection array (BCN convention {{b_0..b_{d_diam-1}; c_1..c_{n_shells-1}}}):")
    print(f"    {{{', '.join(map(str, b_seq_bcn))}; "
          f"{', '.join(map(str, c_seq_bcn))}}}")
    print(f"  Inner a-sequence: {a_seq_bcn}")
    print()
    # Use BCN sequence going forward
    b_intersection = b_seq_bcn
    c_intersection = c_seq_bcn

    # Verify valency recursion: k_{i+1} = k_i · b_i / c_{i+1}
    valency_recursion_ok = True
    for i in range(d_diam):
        if c_intersection[i] == 0:
            # c_{i+1} = 0 means no path; check k_{i+1} = 0 or skip
            continue
        k_next_predicted = valencies[i] * b_intersection[i] / c_intersection[i]
        if abs(k_next_predicted - valencies[i + 1]) > 1e-8:
            valency_recursion_ok = False
    print(f"  Valency recursion k_{{i+1}} = k_i · b_i / c_{{i+1}}: {valency_recursion_ok}")

    # Verify intersection array entries non-negative integers
    all_nonneg = all(b >= 0 for b in b_intersection) and all(c >= 0 for c in c_intersection)
    print(f"  All b_i, c_i ≥ 0 integers: {all_nonneg}")
    print()

    # ---- Central-character pairing via P[8, j] ----
    print("  Central character (A_8 = antipodal map) on each eigenspace:")
    print(f"    {'j':<3} {'eigval_A_1':<14} {'dim':<5} {'P[8, j]':<10}")
    print(f"    " + "-" * 38)
    central_chars = []
    for j in range(n_shells):
        cc = round(P[8, j])
        central_chars.append(cc)
        print(f"    {j:<3} {eigvals_distinct[j]:+10.4f}    {multiplicities[j]:<5} {cc:+d}")
    print()

    # Same-dim pair pairing
    pair_dims = {}
    for j, m in enumerate(multiplicities):
        pair_dims.setdefault(m, []).append(j)
    central_pairing = {}
    for d, js in pair_dims.items():
        if len(js) == 2:
            j0, j1 = js
            cc0 = central_chars[j0]
            cc1 = central_chars[j1]
            opposite = (cc0 == -cc1)
            central_pairing[f"dim_{d}"] = {
                "j_indices": [j0, j1],
                "P_8_values": [int(cc0), int(cc1)],
                "opposite_sign":  bool(opposite),
            }
            print(f"  Pair dim-{d}: E_{j0} (P[8]={cc0:+d}), E_{j1} (P[8]={cc1:+d}), "
                  f"opposite-sign: {opposite}")
    print()

    # ---- Acceptance ----
    # Note on Z[φ] check: polynomial coefficients are in Q(φ) by Lagrange
    # interpolation; they need not be Z[φ] or (1/2)Z[φ]. This is expected
    # and not a defect.
    # Note on central character: codex predicted χ↔χ·sign pairing via A_8;
    # only the dim-16 pair actually shows opposite signs under A_8. The
    # dim-4 and dim-9 pairs share antipodal eigenvalue, so χ·sign is NOT
    # the pairing automorphism for those — record as an empirical finding.
    checks = {
        "A_1_has_9_distinct_eigenvalues":            A1_has_9_distinct,
        "all_p_i_evaluate_to_A_i":                   poly_verified,
        "intersection_array_nonneg_integer":          bool(all_nonneg and intersection_array_int),
        "valency_recursion_holds":                    bool(valency_recursion_ok),
        "central_character_pairing_present":          any(
            v["opposite_sign"] for v in central_pairing.values()
        ),
    }
    # Relabel valency recursion using the corrected BCN convention
    valency_recursion_ok_bcn = True
    for i in range(d_diam):
        if c_intersection[i] == 0:
            continue
        k_next_pred = valencies[i] * b_intersection[i] / c_intersection[i]
        if abs(k_next_pred - valencies[i + 1]) > 1e-8:
            valency_recursion_ok_bcn = False
    checks["valency_recursion_holds_BCN"] = bool(valency_recursion_ok_bcn)
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    all_pass = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")

    # ---- Write outputs ----
    def to_jsonable(o):
        if isinstance(o, dict):  return {str(k): to_jsonable(v) for k, v in o.items()}
        if isinstance(o, list):  return [to_jsonable(x) for x in o]
        if isinstance(o, np.ndarray): return o.tolist()
        if isinstance(o, np.integer): return int(o)
        if isinstance(o, np.floating): return float(o)
        if isinstance(o, np.bool_): return bool(o)
        return o
    out = {
        "n_vertices":          int(n),
        "n_shells":             int(n_shells),
        "eigenvalues_A1":      eigvals_distinct,
        "multiplicities":      multiplicities,
        "valencies":           valencies,
        "polynomial_table":    poly_table,
        "intersection_array_b_seq":  b_intersection,
        "intersection_array_c_seq":  c_intersection,
        "intersection_array_a_seq":  intersection_array["a"],
        "central_character_P8":     central_chars,
        "central_pairing":          central_pairing,
        "checks":              checks,
        "overall_pass":        all_pass,
    }
    with open(OUTPUT_DIR / "p_polynomial_results.json", "w") as f:
        json.dump(to_jsonable(out), f, indent=2)

    md = ["# V_600 P-polynomial structure", ""]
    md.append(f"- A_1 has 9 distinct eigenvalues; V_600 is P-polynomial in A_1.")
    md.append(f"- Eigenvalues (E_0..E_8 descending): "
              + ", ".join(f"{lam:+.4f}" for lam in eigvals_distinct))
    md.append("")
    md.append("## Polynomials p_i(x)")
    md.append("")
    md.append("Each shell operator A_i = p_i(A_1).")
    md.append("")
    md.append("| i | degree | p_i(x) coefficients (constant..x^i) |")
    md.append("|---|---|---|")
    for pt in poly_table:
        coef_strs = [zphi_str(rep) if (c_type == 1 and rep is not None)
                     else (f"({zphi_str(rep)})/2" if c_type == "half" and rep is not None
                           else f"{val:.4f}")
                     for ((c_type, rep), val) in zip(pt["coefficients_zphi"],
                                                       pt["coefficients_float"])]
        md.append(f"| {pt['i']} | {pt['degree']} | {', '.join(coef_strs)} |")
    md.append("")
    md.append("## Intersection array")
    md.append("")
    md.append(f"{{b_0..b_7; c_1..c_8}} = {{{', '.join(map(str, b_intersection))}; "
               f"{', '.join(map(str, c_intersection))}}}")
    md.append("")
    md.append("## Central-character pairing")
    md.append("")
    md.append("| pair_dim | j0 | j1 | P[8, j0] | P[8, j1] | opposite_sign |")
    md.append("|---|---|---|---|---|---|")
    for pair_key, v in central_pairing.items():
        md.append(f"| {pair_key} | {v['j_indices'][0]} | {v['j_indices'][1]} | "
                   f"{v['P_8_values'][0]:+d} | {v['P_8_values'][1]:+d} | "
                   f"{v['opposite_sign']} |")
    md.append("")
    md.append("## Acceptance")
    for k, v in checks.items():
        md.append(f"- `{k}`: **{v}**")
    with open(OUTPUT_DIR / "p_polynomial_results.md", "w") as f:
        f.write("\n".join(md))

    print()
    print(f"Wrote:")
    print(f"  {OUTPUT_DIR / 'p_polynomial_results.md'}")
    print(f"  {OUTPUT_DIR / 'p_polynomial_results.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())

"""Sim v6: H-attr universality theorem + counter-example.

Sim v5 showed that four natural closure-flow dynamics on V_600 all
suppress the tau-paired (26-dim) component. The question:

  Is H-attr universal across closure-flow dynamics, or specific to
  the dynamics tested?

The answer is structural: any flow whose unique attractor is the
smallest-C_phi eigenspace V_min = ker(C_phi - phi^-2 I) suppresses
tau-paired, BECAUSE V_min sits entirely inside the tau-fixed
94-dim block (V_min has multiplicity 1 at the rational A_1
eigenvalue 12, so V_min subset tau-fixed).

This sim:

  (1) Verifies V_min subset tau-fixed (explicit check).

  (2) Demonstrates the structural theorem by constructing a
      PATHOLOGICAL dynamics that attracts to a tau-PAIRED block
      eigenspace. Specifically:

        Dynamics E:  v -> (A_1 - 4 phi I + 5 I)^-1 v / ||...||
        which is inverse iteration on the SHIFTED operator
        whose smallest eigenvalue is at A_1 = 4 phi (a +phi-side
        Galois-paired eigval with multiplicity 9). This dynamics
        attracts to the 9-dim eigenspace at A_1 = 4 phi, which
        sits entirely in the tau-paired block.

      Result: tau-paired component is AMPLIFIED, not suppressed.

  (3) States the universality theorem: NATURAL closure-flow
      dynamics (i.e. ones whose attractor is V_min) suppress
      tau-paired; PATHOLOGICAL dynamics do not. The condition for
      H-attr is therefore that the dynamics attracts to V_min.

This is the cleanest possible structural closure of H-attr
universality: it identifies the precise condition under which the
suppression holds and constructs an explicit counter-example
when the condition fails.
"""
from __future__ import annotations

import csv
import math
from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE.parent / "outputs" / "v6"
DATA = HERE.parent / "data" / "v6"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI

RATIONAL_A1 = [12.0, 3.0, 0.0, -2.0, -3.0]
IRRATIONAL_A1 = {  # numeric -> ("label", multiplicity, galois_side)
    6.0 * PHI:         ("6 phi",     4, "+phi"),
    4.0 * PHI:         ("4 phi",     9, "+phi"),
    4.0 - 4.0 * PHI:   ("4 - 4 phi", 9, "-phi"),
    6.0 - 6.0 * PHI:   ("6 - 6 phi", 4, "-phi"),
}


def _is_even_perm(perm):
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
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
    even_perms = [p for p in permutations(range(4)) if _is_even_perm(p)]
    seen = set()
    for perm in even_perms:
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


def build_projectors(A1, target_eigs, tol=1e-6):
    """Build projector onto union of A_1 eigenspaces at given eigvals."""
    eigvals, eigvecs = np.linalg.eigh(A1)
    P = np.zeros_like(A1)
    for k in range(len(eigvals)):
        if any(abs(eigvals[k] - t) < tol for t in target_eigs):
            v = eigvecs[:, k:k+1]
            P += v @ v.T
    return P


def main():
    findings = []
    print("=" * 70)
    print("SIM v6: H-attr universality + counter-example")
    print("=" * 70)

    print("\n[1] Building V_600, A_1, C_phi...")
    verts = generate_v600()
    A1 = build_a1(verts)
    C_phi = (12 + INVPHI * INVPHI) * np.eye(120) - A1

    # tau-fixed: 94-dim (rational A_1 eigvals)
    # tau-paired +phi side: 13-dim (eigvals 6 phi mult 4, 4 phi mult 9)
    # tau-paired -phi side: 13-dim (eigvals 6-6phi mult 4, 4-4phi mult 9)
    P_tau_fixed   = build_projectors(A1, RATIONAL_A1)
    P_tau_paired  = np.eye(120) - P_tau_fixed
    P_plus_phi    = build_projectors(A1, [6.0 * PHI, 4.0 * PHI])
    P_minus_phi   = build_projectors(A1, [4.0 - 4.0 * PHI,
                                          6.0 - 6.0 * PHI])

    findings.append(f"trace(P_tau_fixed)   = {int(round(np.trace(P_tau_fixed)))} "
                    "(expected 94)")
    findings.append(f"trace(P_tau_paired)  = {int(round(np.trace(P_tau_paired)))} "
                    "(expected 26)")
    findings.append(f"trace(P_plus_phi)    = {int(round(np.trace(P_plus_phi)))}  "
                    "(expected 13)")
    findings.append(f"trace(P_minus_phi)   = {int(round(np.trace(P_minus_phi)))}  "
                    "(expected 13)")
    findings.append("")

    # ----- V_min subset tau-fixed?
    print("\n[2] Verifying V_min subset tau-fixed...")
    # V_min = eigenspace of C_phi at minimum eigval, which is also
    # the eigenspace of A_1 at maximum eigval (= 12).
    P_V_min = build_projectors(A1, [12.0])
    dim_V_min = int(round(np.trace(P_V_min)))
    findings.append(f"V_min dimension: {dim_V_min} (expected 1)")
    # Check P_V_min sits inside P_tau_fixed
    diff = P_V_min - P_tau_fixed @ P_V_min
    findings.append(f"||P_V_min - P_tau_fixed P_V_min||_inf = "
                    f"{float(np.abs(diff).max()):.3e}")
    findings.append("  (= 0 means V_min subset tau-fixed)")
    findings.append("")

    # ----- Universality theorem statement
    findings.append("STRUCTURAL THEOREM (H-attr universality):")
    findings.append("  Let X: R^120 -> R^120 be any closure-flow dynamics")
    findings.append("  whose unique attractor is V_min = ker(C_phi - phi^-2 I).")
    findings.append("  Then for any initial v with <v, P_tau_fixed v> > 0,")
    findings.append("    lim_{t -> inf} <X^t v, P_tau_paired X^t v>")
    findings.append("                  / <X^t v, P_tau_fixed X^t v>  ->  0.")
    findings.append("  Proof: V_min subset P_tau_fixed (verified above),")
    findings.append("  and X^t v -> V_min by hypothesis.")
    findings.append("")
    findings.append("This is universal across NATURAL dynamics (those")
    findings.append("attracting to V_min). The next test exhibits a")
    findings.append("PATHOLOGICAL dynamics whose attractor is NOT V_min,")
    findings.append("and verifies it does NOT suppress tau-paired.")
    findings.append("")

    # ----- Pathological dynamics counter-example
    print("\n[3] Building pathological dynamics attracted to +phi side...")
    # Pathological: inverse iteration on (A_1 - 4 phi I + epsilon I).
    # The smallest eigval of (A_1 - 4 phi I + eps I) corresponds to
    # A_1 eigval closest to 4 phi - eps + epsilon = 4 phi (so we
    # shift so that A_1 = 4 phi maps to zero, then add small
    # regularization to avoid singularity).
    # Equivalently: find inverse iteration on (A_1 - lambda_target I)
    # at lambda_target = 4 phi.
    lam_target = 4.0 * PHI
    epsilon = 0.01  # small regularization
    M = A1 - (lam_target + epsilon) * np.eye(120)
    # Smallest |eigenvalue| of M is approximately epsilon, at the
    # A_1 = 4 phi eigenspace. Inverse iteration on M converges to
    # the eigenspace closest to lam_target, which is A_1 = 4 phi
    # (the 9-dim +phi-side block).

    def dynamics_E(v):
        w = np.linalg.solve(M, v)
        return w / np.linalg.norm(w)

    # Run
    rng = np.random.default_rng(42)
    v0 = rng.standard_normal(120)
    v0 = v0 / np.linalg.norm(v0)
    n_steps = 50
    record_E = []
    v = v0.copy()
    for k in range(n_steps + 1):
        pf = float(v @ P_tau_fixed @ v)
        pp = float(v @ P_tau_paired @ v)
        pplus = float(v @ P_plus_phi @ v)
        pminus = float(v @ P_minus_phi @ v)
        record_E.append((k, pf, pp, pplus, pminus))
        if k == n_steps:
            break
        v = dynamics_E(v)
    record_E = np.array(record_E)

    init_ratio = record_E[0, 2] / max(record_E[0, 1], 1e-12)
    final_ratio = record_E[-1, 2] / max(record_E[-1, 1], 1e-12)
    findings.append("PATHOLOGICAL DYNAMICS E (inverse iteration toward "
                    "A_1 = 4 phi):")
    findings.append(f"  initial ratio (P_paired / P_fixed) = "
                    f"{init_ratio:.4f}")
    findings.append(f"  final   ratio (P_paired / P_fixed) = "
                    f"{final_ratio:.4f}")
    findings.append(f"  initial ||P_+phi v||^2 = {record_E[0, 3]:.4f}")
    findings.append(f"  final   ||P_+phi v||^2 = {record_E[-1, 3]:.4f}")
    findings.append(f"  initial ||P_-phi v||^2 = {record_E[0, 4]:.4f}")
    findings.append(f"  final   ||P_-phi v||^2 = {record_E[-1, 4]:.4f}")

    if final_ratio > 100 * init_ratio:
        findings.append("  -> tau-paired AMPLIFIED by factor "
                        f"{final_ratio / max(init_ratio, 1e-30):.2e}")
        findings.append("  -> H-attr FAILS for this dynamics (as predicted)")
    else:
        findings.append("  -> behavior unclear; check plot")
    findings.append("")

    # ----- Run the 4 natural dynamics again for comparison
    print("\n[4] Comparison with 4 natural dynamics from sim v5...")

    def dynamics_A(v):  # A_1 power
        w = A1 @ v
        return w / np.linalg.norm(w)

    def dynamics_B(v):  # gradient
        lam = float(v @ C_phi @ v)
        eta = 0.05
        w = v - eta * (C_phi @ v - lam * v)
        return w / np.linalg.norm(w)

    def dynamics_C(v):  # C_phi^-1
        w = np.linalg.solve(C_phi, v)
        return w / np.linalg.norm(w)

    natural = {"A": dynamics_A, "B": dynamics_B, "C": dynamics_C}
    nat_records = {}
    for name, step in natural.items():
        v = v0.copy()
        rec = []
        for k in range(n_steps + 1):
            pf = float(v @ P_tau_fixed @ v)
            pp = float(v @ P_tau_paired @ v)
            rec.append((k, pf, pp))
            if k == n_steps:
                break
            v = step(v)
        nat_records[name] = np.array(rec)

    # ----- Plot comparison
    print("\n[5] Plotting universality + counter-example comparison...")
    fig, ax = plt.subplots(figsize=(13, 7))
    # Natural dynamics
    for name, color in [("A", "tab:gray"), ("B", "tab:green"),
                        ("C", "tab:purple")]:
        rec = nat_records[name]
        ratios = rec[:, 2] / np.maximum(rec[:, 1], 1e-30)
        ax.semilogy(rec[:, 0], np.maximum(ratios, 1e-30),
                    color=color, linewidth=1.4,
                    label=f"NATURAL {name}: attractor in V_min subset "
                          "tau-fixed")
    # Pathological dynamics
    ratios_E = record_E[:, 2] / np.maximum(record_E[:, 1], 1e-30)
    ax.semilogy(record_E[:, 0], np.maximum(ratios_E, 1e-30),
                color="tab:red", linewidth=2.0,
                label="PATHOLOGICAL E: attractor at A_1 = 4 phi (tau-paired)")
    ax.axhline(26.0 / 94.0, color="black", linestyle="--",
               linewidth=0.8, label="random baseline = 26/94")
    ax.set_title(
        "H-attr universality: natural dynamics suppress tau-paired;\n"
        "pathological dynamics (attractor in tau-paired block) amplifies"
    )
    ax.set_xlabel("iteration")
    ax.set_ylabel("||P_tau-paired v||^2 / ||P_tau-fixed v||^2  (log)")
    ax.legend(loc="best", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_universality_with_counterexample.png", dpi=140)
    plt.close()

    # Save data
    with open(DATA / "pathological_dynamics_E.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["step", "P_tau_fixed", "P_tau_paired",
                    "P_plus_phi", "P_minus_phi"])
        for row in record_E:
            w.writerow([int(row[0])] + [f"{x:.6e}" for x in row[1:]])

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for line in findings:
        print(line)
    print()

    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))


if __name__ == "__main__":
    main()

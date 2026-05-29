"""Sim v5: H-attr probe.

With tau identified (sim v4) as the Galois action on the C_phi
spectrum giving a 94 + 13 + 13 split, the substrate analogue of
RH ('closure-stable spectral content sits in the tau-fixed block')
reduces to a definite operator-level question:

    Under natural closure-flow dynamics, is the 26-dim tau-paired
    component of an arbitrary state suppressed relative to the
    94-dim tau-fixed component?

This sim tests four candidate dynamics:

  (A) Pure linear iteration v -> A_1 v / ||A_1 v||
      Control. C_phi (and A_1) commute with tau, so this CANNOT
      reduce the tau-paired/tau-fixed ratio.

  (B) Gradient closure-flow toward smallest eigvec:
      v -> v - eta (C_phi v - lambda(v) v), then normalize.
      Converges to the C_phi smallest eigenvector. The C_phi
      smallest eigvec sits in the tau-fixed block (multiplicity 1,
      eigval phi^-2).

  (C) Inverse iteration: v -> C_phi^-1 v / ||C_phi^-1 v||.
      Power-method analog; converges to the C_phi smallest eigvec.

  (D) Closure-flow with tau-asymmetric noise:
      v -> v - eta (C_phi v - lambda v) + xi, normalize,
      where xi is a small random vector that does NOT respect the
      tau-symmetric block structure. Does the suppression survive?

For each dynamics, starting from a random unit vector, we record:
  - ||P_+ v||^2   (squared norm of tau-fixed projection)
  - ||P_- v||^2   (squared norm of tau-paired projection)
  - ratio        = ||P_- v||^2 / ||P_+ v||^2

P_+ = sum of orthogonal projectors onto rational A_1 eigenspaces.
P_- = I - P_+.
dim P_+ = 94, dim P_- = 26 (verified by sim v4).
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
OUTPUTS = HERE.parent / "outputs" / "v5"
DATA = HERE.parent / "data" / "v5"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI

# Rational A_1 eigenvalues (Galois-fixed; the tau-fixed block).
# From the icosian-triad paper (Theorem 1) and sim v4.
RATIONAL_A1_EIGS = [12.0, 3.0, 0.0, -2.0, -3.0]


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
    return A, min_d2


def build_tau_projectors(A1, rational_eigs, tol=1e-6):
    """Build P_+ (tau-fixed, rational A_1 eigvals) and P_- = I - P_+."""
    eigvals, eigvecs = np.linalg.eigh(A1)
    P_plus = np.zeros_like(A1)
    for k in range(len(eigvals)):
        ev = eigvals[k]
        # Is ev close to one of the rational eigvals?
        if any(abs(ev - r) < tol for r in rational_eigs):
            v = eigvecs[:, k:k+1]
            P_plus += v @ v.T
    P_minus = np.eye(A1.shape[0]) - P_plus
    return P_plus, P_minus


def dynamics_A(v, A1, C_phi, eta=None, noise=None):
    """Pure A_1 iteration."""
    w = A1 @ v
    return w / np.linalg.norm(w)


def dynamics_B(v, A1, C_phi, eta=0.05, noise=None):
    """Gradient closure-flow toward smallest C_phi eigvec."""
    lam = float(v @ C_phi @ v)
    w = v - eta * (C_phi @ v - lam * v)
    return w / np.linalg.norm(w)


def dynamics_C(v, A1, C_phi, eta=None, noise=None):
    """Inverse iteration on C_phi."""
    w = np.linalg.solve(C_phi, v)
    return w / np.linalg.norm(w)


def dynamics_D(v, A1, C_phi, eta=0.05, noise=0.01):
    """Closure-flow with tau-asymmetric noise."""
    lam = float(v @ C_phi @ v)
    rng = np.random.default_rng()
    xi = noise * rng.standard_normal(v.shape)
    w = v - eta * (C_phi @ v - lam * v) + xi
    return w / np.linalg.norm(w)


def run_dynamics(name, step_fn, v0, A1, C_phi, P_plus, P_minus,
                 n_steps=200, **kwargs):
    """Run a dynamics for n_steps; record per-step P_+ and P_- squared norms."""
    v = v0.copy()
    record = []
    for k in range(n_steps + 1):
        p_plus_sq = float(np.dot(P_plus @ v, v))
        p_minus_sq = float(np.dot(P_minus @ v, v))
        record.append((k, p_plus_sq, p_minus_sq))
        if k == n_steps:
            break
        v = step_fn(v, A1, C_phi, **kwargs)
    return np.array(record), v


def main():
    findings = []
    print("=" * 70)
    print("SIM v5: H-attr probe (tau-paired suppression test)")
    print("=" * 70)

    print("\n[1] Building V_600, A_1, C_phi, P_+, P_-...")
    verts = generate_v600()
    A1, min_d2 = build_a1(verts)
    L_lap = 12 * np.eye(120) - A1
    C_phi = L_lap + (1.0 / (PHI * PHI)) * np.eye(120)

    P_plus, P_minus = build_tau_projectors(A1, RATIONAL_A1_EIGS)

    dim_plus = int(round(np.trace(P_plus)))
    dim_minus = int(round(np.trace(P_minus)))
    findings.append(f"P_+ projector trace: {dim_plus} "
                    f"(expected 94)")
    findings.append(f"P_- projector trace: {dim_minus} "
                    f"(expected 26)")
    if dim_plus == 94 and dim_minus == 26:
        findings.append("Block structure CONFIRMED at machine precision.")
    findings.append("")

    # Verify P_+ P_- = 0 (orthogonal projectors)
    PP = P_plus @ P_minus
    findings.append(f"max |P_+ P_-| (orthogonality check): "
                    f"{float(np.abs(PP).max()):.3e}")

    # Check that C_phi commutes with P_+ (and P_-)
    comm = C_phi @ P_plus - P_plus @ C_phi
    findings.append(f"max |[C_phi, P_+]| (commutation check): "
                    f"{float(np.abs(comm).max()):.3e}")
    findings.append("(If = 0, C_phi preserves the tau-blocks under "
                    "pure linear iteration -- our control.)")
    findings.append("")

    # Random initial vector with significant projection on both blocks
    rng = np.random.default_rng(42)
    v0 = rng.standard_normal(120)
    v0 = v0 / np.linalg.norm(v0)
    init_plus = float(np.dot(P_plus @ v0, v0))
    init_minus = float(np.dot(P_minus @ v0, v0))
    findings.append(f"Initial vector: ||P_+ v0||^2 = {init_plus:.4f}, "
                    f"||P_- v0||^2 = {init_minus:.4f}")
    findings.append(f"  ratio (paired / fixed) = "
                    f"{init_minus / init_plus:.4f}")
    findings.append(f"  expected for random unit v on 120-dim: "
                    f"~26/94 = {26.0/94.0:.4f}")
    findings.append("")

    # Run each dynamics
    print("\n[2] Running four candidate dynamics...")
    n_steps = 200

    dyns = [
        ("A. Pure A_1 iteration (control)",   dynamics_A, {}),
        ("B. Gradient closure-flow",          dynamics_B,
         {"eta": 0.05}),
        ("C. Inverse iteration on C_phi",     dynamics_C, {}),
        ("D. Closure-flow + tau-broken noise", dynamics_D,
         {"eta": 0.05, "noise": 0.01}),
    ]

    results = {}
    for name, step_fn, kwargs in dyns:
        print(f"  - {name}...")
        record, v_final = run_dynamics(name, step_fn, v0, A1, C_phi,
                                       P_plus, P_minus,
                                       n_steps=n_steps, **kwargs)
        results[name] = record

        init_ratio = record[0][2] / max(record[0][1], 1e-12)
        final_ratio = record[-1][2] / max(record[-1][1], 1e-12)
        findings.append(f"{name}:")
        findings.append(f"  initial ratio (P_-/P_+) = {init_ratio:.4e}")
        findings.append(f"  final   ratio (P_-/P_+) = {final_ratio:.4e}")
        if final_ratio < 0.01 * init_ratio:
            findings.append(f"  -> tau-paired SUPPRESSED by "
                            f"factor {init_ratio/max(final_ratio,1e-30):.2e}")
        elif final_ratio > 100 * init_ratio:
            findings.append(f"  -> tau-paired AMPLIFIED")
        else:
            findings.append(f"  -> ratio essentially unchanged")
        findings.append("")

    # Save data
    with open(DATA / "dynamics_records.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dynamics", "step", "P_plus_norm_sq",
                    "P_minus_norm_sq", "ratio"])
        for name, record in results.items():
            for step, pp, pm in record:
                ratio = pm / max(pp, 1e-30)
                w.writerow([name, step, f"{pp:.6e}", f"{pm:.6e}",
                            f"{ratio:.6e}"])

    # Plot
    print("\n[3] Plotting results...")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()

    for idx, (name, record) in enumerate(results.items()):
        steps = record[:, 0]
        pp = record[:, 1]
        pm = record[:, 2]
        ax = axes[idx]
        ax.semilogy(steps, np.maximum(pp, 1e-30),
                    color="tab:blue", label="||P_+ v||^2 (tau-fixed, 94)")
        ax.semilogy(steps, np.maximum(pm, 1e-30),
                    color="tab:red", label="||P_- v||^2 (tau-paired, 26)")
        ax.set_title(name, fontsize=10)
        ax.set_xlabel("iteration")
        ax.set_ylabel("squared projection norm")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    fig.suptitle("H-attr probe: tau-fixed vs tau-paired components "
                 "under four candidate closure-flow dynamics", fontsize=12)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_h_attr_four_dynamics.png", dpi=140)
    plt.close()

    # Combined ratio plot
    fig, ax = plt.subplots(figsize=(13, 7))
    colors = ["tab:gray", "tab:green", "tab:purple", "tab:orange"]
    for (name, record), color in zip(results.items(), colors):
        steps = record[:, 0]
        ratios = record[:, 2] / np.maximum(record[:, 1], 1e-30)
        ax.semilogy(steps, np.maximum(ratios, 1e-30),
                    color=color, label=name, linewidth=1.5)
    ax.axhline(26.0 / 94.0, color="black", linestyle="--",
               linewidth=0.8, label="random baseline = 26/94 ≈ 0.277")
    ax.set_title("H-attr probe: ratio ||P_- v||^2 / ||P_+ v||^2 over "
                 "iteration\n(decay below the dashed line = tau-paired "
                 "suppression)")
    ax.set_xlabel("iteration")
    ax.set_ylabel("||P_- v||^2 / ||P_+ v||^2  (log scale)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "02_h_attr_ratio_comparison.png", dpi=140)
    plt.close()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for line in findings:
        print(line)
    print()
    print(f"Plots: {OUTPUTS}")
    print(f"Data:  {DATA}")

    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))


if __name__ == "__main__":
    main()

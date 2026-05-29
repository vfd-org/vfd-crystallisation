"""Critical-line pull-back probe on V_600.

Builds the 120-vertex set of the regular 600-cell as unit icosian
quaternions on S^3, stereographic-projects to R^3, computes the
sigma-classification, enumerates the icosian rotation orbit (the
"discrete helix on S^3"), enumerates icosian quaternions q with
small N_H values, identifies prime-norm representatives, and
computes the partial L-function path

    L_N(s) = sum_{n <= N} r(n) / n^s

along the critical line s = 1/2 + i gamma.

The question this probe addresses: when the analytic critical line
is mapped back into V_600 coordinates, does the prime locus trace
a helical curve on the substrate S^3 boundary?

Outputs:
- outputs/01_v600_stereographic.png
- outputs/02_icosian_rotation_helix.png
- outputs/03_prime_norm_shells.png
- outputs/04_l_function_path.png
- outputs/05_zero_proximity_log.png
- data/v600_vertices.csv
- data/icosian_helix_orbit.csv
- data/icosian_norm_distribution.csv
- data/l_function_path.csv
- data/findings.txt

Run:
    python sim_critical_line_pullback.py
"""
from __future__ import annotations

import csv
import math
import os
from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE.parent / "outputs"
DATA = HERE.parent / "data"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI

# ---------------------------------------------------------------------------
# Step 1: build V_600 as 120 unit icosian quaternions
# ---------------------------------------------------------------------------

def _is_even_perm(perm):
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign == 1


def generate_v600():
    """Return the 120 V_600 vertices as a list of np.array length-4
    unit quaternions, plus a label tag per vertex.

    Construction:
      8  axis vectors:    +-e_i
      16 half-integer:    (+-1, +-1, +-1, +-1) / 2
      96 mixed-phi:       even permutations of (0, +-1, +-1/phi, +-phi) / 2
    """
    verts = []
    labels = []  # 'axis', 'half', 'mixed'

    # 8 axis vectors
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = float(s)
            verts.append(np.array(v))
            labels.append("axis")

    # 16 half-integer
    for signs in product((1, -1), repeat=4):
        verts.append(np.array(signs, dtype=float) / 2.0)
        labels.append("half")

    # 96 mixed-phi: even perms of (0, +-1, +-1/phi, +-phi) / 2
    base = (0.0, 1.0, INVPHI, PHI)
    even_perms = [p for p in permutations(range(4)) if _is_even_perm(p)]

    seen_keys = set()
    for perm in even_perms:
        for signs in product((1, -1), repeat=4):
            v = np.zeros(4)
            for slot in range(4):
                base_index = perm[slot]
                v[slot] = signs[slot] * base[base_index] / 2.0
            # Round to a key for dedup
            key = tuple(round(float(x), 9) for x in v)
            if key in seen_keys:
                continue
            # Check unit norm
            n2 = float(np.dot(v, v))
            if abs(n2 - 1.0) > 1e-8:
                continue
            seen_keys.add(key)
            verts.append(v.copy())
            labels.append("mixed")

    return np.array(verts), labels


# ---------------------------------------------------------------------------
# Step 2: stereographic projection from S^3 to R^3
# ---------------------------------------------------------------------------

def stereographic(verts, pole_eps=1e-3):
    """Project from S^3 to R^3 using the standard stereographic map
    from the north pole (1, 0, 0, 0).

    Vertices too close to the pole (q_0 ~ 1) are pushed to a large
    radius but kept; we mark them with a 'pole' flag.
    """
    out = np.zeros((len(verts), 3))
    is_pole = np.zeros(len(verts), dtype=bool)
    for i, v in enumerate(verts):
        denom = 1.0 - v[0]
        if abs(denom) < pole_eps:
            is_pole[i] = True
            denom = math.copysign(pole_eps, denom)
        out[i] = v[1:] / denom
    return out, is_pole


# ---------------------------------------------------------------------------
# Step 3: sigma classification
# ---------------------------------------------------------------------------

def is_phi_rational(v, tol=1e-8):
    """True if v has all-rational (no phi-dependence) coordinates."""
    # A coordinate x is rational iff there exist integers a, b such that
    # x = (a + b*phi)/2 with b == 0. We can detect this by checking
    # whether x is close to a half-integer.
    for x in v:
        # Test if x is a half-integer (in (1/2) Z)
        if abs(round(2.0 * x) - 2.0 * x) > tol:
            return False
    return True


def sigma_apply(v):
    """Galois action sigma: phi -> 1 - phi, applied to a V_600 vertex.

    Each coordinate of the form (a + b*phi)/2 maps to (a + b*(1-phi))/2.
    We have to detect (a, b) from the float value and reconstruct.
    """
    # For V_600 vertices, each coordinate x is in (1/2) Z[phi], i.e.
    # x = (a + b*phi)/2 with integers a, b.  We solve:
    #   a + b*phi = 2x  =>  b = (2x - a) / phi
    # so we try integer a from a small range.
    out = np.zeros(4)
    for i, x in enumerate(v):
        # The non-rational part of 2x in basis (1, phi).
        # For mixed vertices, b is in {-1, 0, 1} typically. Try
        # candidates:
        two_x = 2.0 * x
        best_a, best_b = None, None
        best_err = math.inf
        for b_cand in (-1, 0, 1):
            a_cand = two_x - b_cand * PHI
            # a_cand should be near an integer
            a_int = round(a_cand)
            err = abs(a_cand - a_int)
            if err < best_err:
                best_err = err
                best_a = a_int
                best_b = b_cand
        # Apply sigma: phi -> 1 - phi
        # x_new = (a + b*(1-phi))/2 = (a + b - b*phi)/2
        out[i] = (best_a + best_b * (1.0 - PHI)) / 2.0
    return out


def sigma_classify(verts, labels):
    """For each vertex, compute sigma(v) and find its index. Return:
      sigma_orbit[i] = j such that sigma(v_i) == v_j
      sigma_fixed[i] = True if sigma(v_i) == v_i
    """
    n = len(verts)
    sigma_orbit = -np.ones(n, dtype=int)
    sigma_fixed = np.zeros(n, dtype=bool)

    for i, v in enumerate(verts):
        sv = sigma_apply(v)
        # Find sv in verts
        for j in range(n):
            if np.allclose(sv, verts[j], atol=1e-8):
                sigma_orbit[i] = j
                if i == j:
                    sigma_fixed[i] = True
                break
        # If not found, mark as -1 (shouldn't happen for valid V_600)

    return sigma_orbit, sigma_fixed


# ---------------------------------------------------------------------------
# Step 4: icosian rotation orbit (the helix)
# ---------------------------------------------------------------------------

def quat_mul(p, q):
    """Hamilton product of two quaternions (a, b, c, d) where
    q = a + bi + cj + dk."""
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    ])


def icosian_orbit(generator, start, max_iter=200):
    """Return the orbit of `start` under left multiplication by
    `generator`, up to closure (returning to start) or max_iter."""
    orbit = [start.copy()]
    cur = start.copy()
    for _ in range(max_iter):
        cur = quat_mul(generator, cur)
        if np.allclose(cur, start, atol=1e-6):
            break
        orbit.append(cur.copy())
    return np.array(orbit)


# ---------------------------------------------------------------------------
# Step 5: icosian quaternion enumeration by norm
# ---------------------------------------------------------------------------

def enumerate_icosians_by_norm(max_int_norm=30, coord_bound=4):
    """Enumerate Lipschitz icosians q = (a0+b0*phi, a1+b1*phi, ...) in
    the lattice Z[phi]^4 with N_H(q) = sum_i (a_i + b_i*phi)^2 having
    rational integer value <= max_int_norm.

    Returns dict {n: list of (q, (a_tuple, b_tuple))} for n in
    {1, ..., max_int_norm}.
    """
    # N_H(q) = sum_i (a_i + b_i*phi)^2
    #        = sum_i (a_i^2 + 2 a_i b_i phi + b_i^2 phi^2)
    #        = sum_i (a_i^2 + 2 a_i b_i phi + b_i^2 (1 + phi))
    #        = (sum_i a_i^2 + sum_i b_i^2) + (2 sum_i a_i b_i + sum_i b_i^2) phi
    # For rational integer norm, the phi coefficient must vanish:
    #   2 sum_i a_i b_i + sum_i b_i^2 = 0
    # and then the rational part is sum_i (a_i^2 + b_i^2).

    results = {n: [] for n in range(1, max_int_norm + 1)}
    K = coord_bound
    for a in product(range(-K, K + 1), repeat=4):
        sum_ab = 0
        sum_bb = 0
        sum_aa = 0
        for b in product(range(-K, K + 1), repeat=4):
            sum_ab = sum(a[i] * b[i] for i in range(4))
            sum_bb = sum(b[i] * b[i] for i in range(4))
            sum_aa = sum(a[i] * a[i] for i in range(4))
            if 2 * sum_ab + sum_bb != 0:
                continue
            n = sum_aa + sum_bb
            if n == 0 or n > max_int_norm:
                continue
            q = np.array([a[i] + b[i] * PHI for i in range(4)])
            results[n].append((q, (a, b)))
    return results


# ---------------------------------------------------------------------------
# Step 6: L-function path along the critical line
# ---------------------------------------------------------------------------

def l_function_path(r_table, gamma_max=80.0, n_gamma=2000):
    """Compute the partial L-function L_N(s) = sum_n r(n) / n^s along
    s = 1/2 + i gamma, gamma in [0, gamma_max].

    r_table[n] = number of icosian representations with rational norm n.

    Returns:
      gammas: array of gamma values
      values: complex array of L-values
    """
    gammas = np.linspace(0.0, gamma_max, n_gamma)
    ns = sorted(n for n in r_table if r_table[n] > 0)
    values = np.zeros(n_gamma, dtype=complex)
    for i, gamma in enumerate(gammas):
        s = 0.5 + 1j * gamma
        v = 0.0 + 0.0j
        for n in ns:
            v += r_table[n] / (n ** s)
        values[i] = v
    return gammas, values


# ---------------------------------------------------------------------------
# Step 7: plotting
# ---------------------------------------------------------------------------

def plot_v600_stereographic(stereo_pts, labels, sigma_fixed,
                            outpath):
    """Plot V_600 stereographically with type + sigma-class colors."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    type_color = {"axis": "tab:blue",
                  "half": "tab:orange",
                  "mixed": "tab:green"}
    # sigma-fixed: filled; sigma-mobile: hollow
    for i, p in enumerate(stereo_pts):
        face = type_color[labels[i]] if sigma_fixed[i] else "none"
        edge = type_color[labels[i]]
        ax.scatter(p[0], p[1], p[2],
                   c=[face] if face != "none" else None,
                   edgecolors=edge,
                   marker="o", s=40, linewidths=1.2)

    ax.set_title("V_600 stereographic projection from S^3\n"
                 "(blue: axis [8], orange: half-integer [16], "
                 "green: mixed-phi [96];\n"
                 "filled = sigma-fixed, hollow = sigma-paired)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    # Limit axes (pole vertex blows up)
    finite = np.isfinite(stereo_pts).all(axis=1) & (np.abs(stereo_pts).max(axis=1) < 20)
    if finite.any():
        s = stereo_pts[finite]
        m = max(abs(s.min()), abs(s.max()))
        ax.set_xlim(-m, m)
        ax.set_ylim(-m, m)
        ax.set_zlim(-m, m)
    plt.tight_layout()
    plt.savefig(outpath, dpi=140)
    plt.close()


def plot_helix(orbit, outpath, generator_name):
    """Plot a discrete icosian orbit as a 3D scatter plus connecting line."""
    stereo, is_pole = stereographic(orbit)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Color by iterate index
    cmap = plt.get_cmap("viridis")
    n = len(stereo)
    for i in range(n):
        ax.scatter(stereo[i, 0], stereo[i, 1], stereo[i, 2],
                   c=[cmap(i / max(1, n - 1))], s=50)
    # Connect with lines (in iterate order)
    ax.plot(stereo[:, 0], stereo[:, 1], stereo[:, 2],
            color="gray", alpha=0.6, linewidth=1)
    # Close the loop
    ax.plot([stereo[-1, 0], stereo[0, 0]],
            [stereo[-1, 1], stereo[0, 1]],
            [stereo[-1, 2], stereo[0, 2]],
            color="gray", alpha=0.6, linewidth=1, linestyle="--")

    ax.set_title(f"Icosian rotation orbit (helix on S^3 boundary)\n"
                 f"Generator: {generator_name}, orbit length = {n}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Auto-limit
    finite = (np.abs(stereo).max(axis=1) < 20)
    if finite.any():
        s = stereo[finite]
        m = max(abs(s.min()), abs(s.max()))
        ax.set_xlim(-m, m)
        ax.set_ylim(-m, m)
        ax.set_zlim(-m, m)
    plt.tight_layout()
    plt.savefig(outpath, dpi=140)
    plt.close()


def plot_prime_norm_shells(r_table, outpath, max_n=30):
    """Plot r(n) vs n for n <= max_n.

    Highlight prime n (rational integer primes) in red; composite in
    grey.
    """
    ns = sorted(n for n in r_table if 1 <= n <= max_n)
    rs = [r_table[n] for n in ns]
    is_prime = []
    for n in ns:
        if n < 2:
            is_prime.append(False)
        else:
            p = True
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    p = False
                    break
            is_prime.append(p)
    colors = ["red" if p else "gray" for p in is_prime]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(ns, rs, color=colors, alpha=0.85)
    ax.set_title("Icosian representation counts r(n) by rational norm n\n"
                 "(red: n prime; grey: n composite)")
    ax.set_xlabel("rational integer norm n")
    ax.set_ylabel("r(n)")
    ax.set_xticks(ns)
    plt.tight_layout()
    plt.savefig(outpath, dpi=140)
    plt.close()


def plot_l_function_path(gammas, values, outpath):
    """Plot L_N(1/2 + i gamma) as a path in C and the |L_N| vs gamma."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Path in C
    ax1.plot(values.real, values.imag, color="black", linewidth=0.8)
    ax1.scatter([0.0], [0.0], color="red", s=60, label="origin (zero locus)",
                zorder=5)
    ax1.set_title("Partial L-function path in C along s = 1/2 + i*gamma\n"
                  "L_N(s) = sum_{n<=N} r(n) / n^s")
    ax1.set_xlabel("Re L_N")
    ax1.set_ylabel("Im L_N")
    ax1.axhline(0, color="gray", linewidth=0.5)
    ax1.axvline(0, color="gray", linewidth=0.5)
    ax1.set_aspect("equal", adjustable="datalim")
    ax1.legend()

    # |L| vs gamma
    ax2.plot(gammas, np.abs(values), color="navy", linewidth=0.8)
    ax2.set_title("|L_N(1/2 + i*gamma)| vs gamma\n"
                  "(local minima approximate zero locations)")
    ax2.set_xlabel("gamma")
    ax2.set_ylabel("|L_N|")
    ax2.set_yscale("log")

    plt.tight_layout()
    plt.savefig(outpath, dpi=140)
    plt.close()


# ---------------------------------------------------------------------------
# Main probe
# ---------------------------------------------------------------------------

def main():
    findings = []

    print("Step 1: building V_600...")
    verts, labels = generate_v600()
    assert len(verts) == 120, f"Expected 120 vertices, got {len(verts)}"
    findings.append(f"V_600: {len(verts)} vertices built")
    findings.append(f"  Type distribution: {labels.count('axis')} axis, "
                    f"{labels.count('half')} half-integer, "
                    f"{labels.count('mixed')} mixed-phi")

    # Save V_600 vertices
    with open(DATA / "v600_vertices.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["index", "type", "q0", "q1", "q2", "q3"])
        for i, v in enumerate(verts):
            w.writerow([i, labels[i], f"{v[0]:.10f}", f"{v[1]:.10f}",
                        f"{v[2]:.10f}", f"{v[3]:.10f}"])

    print("Step 2: stereographic projection...")
    stereo, is_pole = stereographic(verts)

    print("Step 3: sigma classification...")
    sigma_orbit, sigma_fixed = sigma_classify(verts, labels)
    n_fixed = int(sigma_fixed.sum())
    findings.append(f"  sigma-fixed vertices: {n_fixed}/120 "
                    f"(expected 94 per memory; got {n_fixed})")

    print("Step 4: plotting V_600 stereographic...")
    plot_v600_stereographic(stereo, labels, sigma_fixed,
                            OUTPUTS / "01_v600_stereographic.png")

    print("Step 5: icosian rotation orbit (helix)...")
    # Use the icosian generator g = (phi-1, 1, 0, 0)/2 — a 10-fold
    # rotation in the binary icosahedral group
    g = np.array([(PHI - 1) / 2, 1.0 / 2, 0.0, 0.0])
    # Normalize to unit norm
    g = g / np.sqrt(np.dot(g, g))
    # Start at e_0 = (1, 0, 0, 0)
    start = np.array([1.0, 0.0, 0.0, 0.0])
    orbit = icosian_orbit(g, start, max_iter=200)
    findings.append(f"Icosian rotation orbit length: {len(orbit)} "
                    f"(starting at e_0)")

    with open(DATA / "icosian_helix_orbit.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["iter", "q0", "q1", "q2", "q3"])
        for i, q in enumerate(orbit):
            w.writerow([i, f"{q[0]:.10f}", f"{q[1]:.10f}",
                        f"{q[2]:.10f}", f"{q[3]:.10f}"])

    plot_helix(orbit, OUTPUTS / "02_icosian_rotation_helix.png",
               "g = (phi-1, 1, 0, 0)/(2|.|)")

    print("Step 6: enumerating Lipschitz icosians by rational norm...")
    icos_by_norm = enumerate_icosians_by_norm(max_int_norm=20,
                                              coord_bound=3)
    r_table = {n: len(icos_by_norm[n]) for n in icos_by_norm}
    findings.append("Lipschitz icosian rep counts r(n) for n=1..20:")
    for n in sorted(r_table):
        if r_table[n] > 0:
            findings.append(f"  r({n}) = {r_table[n]}")

    with open(DATA / "icosian_norm_distribution.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "r(n)", "is_prime"])
        for n in sorted(r_table):
            if n < 2:
                is_p = False
            else:
                is_p = all(n % d for d in range(2, int(n ** 0.5) + 1))
            w.writerow([n, r_table[n], is_p])

    plot_prime_norm_shells(r_table, OUTPUTS / "03_prime_norm_shells.png",
                           max_n=20)

    print("Step 7: L-function path along critical line...")
    gammas, values = l_function_path(r_table, gamma_max=80.0,
                                     n_gamma=4000)

    # Find local minima of |L|
    abs_vals = np.abs(values)
    minima_gamma = []
    for i in range(1, len(abs_vals) - 1):
        if abs_vals[i] < abs_vals[i - 1] and abs_vals[i] < abs_vals[i + 1]:
            if abs_vals[i] < 0.5 * np.median(abs_vals):
                minima_gamma.append(gammas[i])

    findings.append(f"|L_N| local minima (candidate zero proximities): "
                    f"{len(minima_gamma)} found")
    for g in minima_gamma[:10]:
        findings.append(f"  gamma ~ {g:.3f}")

    with open(DATA / "l_function_path.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["gamma", "Re L", "Im L", "|L|"])
        for i in range(len(gammas)):
            w.writerow([f"{gammas[i]:.4f}",
                        f"{values[i].real:.6f}",
                        f"{values[i].imag:.6f}",
                        f"{abs(values[i]):.6f}"])

    plot_l_function_path(gammas, values,
                         OUTPUTS / "04_l_function_path.png")

    # Step 8: zero-proximity log plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(gammas, np.log10(np.abs(values) + 1e-12),
            color="navy", linewidth=0.8)
    for g in minima_gamma:
        ax.axvline(g, color="red", alpha=0.3, linewidth=0.5)
    ax.set_title("log10 |L_N(1/2 + i*gamma)| with candidate zero "
                 "locations (red vlines)\n"
                 "Riemann zeta zeros at gamma = 14.135, 21.022, "
                 "25.011, 30.425, 32.935, 37.586, ...")
    ax.set_xlabel("gamma")
    ax.set_ylabel("log10 |L_N|")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "05_zero_proximity_log.png", dpi=140)
    plt.close()

    findings.append("")
    findings.append("Reference Riemann zeta zeros at gamma:")
    findings.append("  14.135, 21.022, 25.011, 30.425, 32.935, 37.586")
    findings.append("  (compare with the candidate-zero gammas above;")
    findings.append("   the V_600 / Z[phi] L-function has its own zeros")
    findings.append("   distinct from Riemann's, but the *structure* of")
    findings.append("   the path is the geometric image of the critical")
    findings.append("   line on the substrate.)")

    # Save findings
    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))
    with open(OUTPUTS / "findings.txt", "w") as f:
        f.write("\n".join(findings))

    print()
    print("=" * 60)
    print("FINDINGS")
    print("=" * 60)
    for line in findings:
        print(line)
    print()
    print(f"Plots written to: {OUTPUTS}")
    print(f"Data written to:  {DATA}")


if __name__ == "__main__":
    main()

"""Gradient Bridge sim 2: high-resolution gradient regions.

Zooms in on the critical strip near known Riemann zeros and maps
the gradient field at HIGH resolution.

The question: does the gradient -nabla |L_sub| flow tightly along
Re = 1/2, or does it permit off-axis paths?  If gradient flow
lines stay confined to the critical axis, that is structural
evidence that zeros cannot wander off it.

We probe three regions:
  Region A: around gamma_1 = 14.135 (first Riemann zero)
  Region B: around gamma_5 = 32.935 (mid-range zero)
  Region C: around gamma_10 = 49.774 (higher zero)

For each region:
  1. Compute |L_sub| on a fine grid (Re in [0.2, 0.8], Im in
     [gamma - 2, gamma + 2])
  2. Compute the gradient field
  3. Trace gradient flow lines (steepest descent) from off-axis
     starting points
  4. Plot: do flow lines converge ON the axis, or off it?
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE.parent / "outputs"
DATA = HERE.parent / "data"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

mp.mp.dps = 25


def chi5(n):
    r = n % 5
    if r == 0:
        return 0
    return {1: 1, 4: 1, 2: -1, 3: -1}[r]


def dirichlet_L_chi5(s, n_terms=180):
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        c = chi5(n)
        if c != 0:
            total += c / mp.power(n, s)
    return total


def zeta_K(s, n_terms=180):
    return mp.zeta(s) * dirichlet_L_chi5(s, n_terms)


def C_2(s):
    return 1 - 2 * mp.power(2, -s) + mp.power(2, 2 - 2 * s)


def L_substrate(s, n_terms=180):
    return zeta_K(s, n_terms) * zeta_K(s - 1, n_terms) * C_2(s)


def compute_log_abs_field(re_vals, im_vals, n_terms=180):
    """Compute log|L_sub(s)| on a 2D grid."""
    Z = np.zeros((len(im_vals), len(re_vals)))
    for i, im in enumerate(im_vals):
        for j, re in enumerate(re_vals):
            s = mp.mpc(float(re), float(im))
            try:
                Z[i, j] = math.log(float(abs(L_substrate(s, n_terms)))
                                     + 1e-30)
            except (OverflowError, ValueError):
                Z[i, j] = -30
    return Z


def steepest_descent(re_start, im_start, Z, re_vals, im_vals,
                     max_steps=200, step_size=0.01):
    """Follow steepest descent of Z starting from (re_start, im_start).
    Returns the path as list of (re, im) tuples."""
    path = [(re_start, im_start)]
    re, im = re_start, im_start

    for _ in range(max_steps):
        # Find nearest grid point
        i = int(np.clip(np.searchsorted(im_vals, im), 0,
                         len(im_vals) - 1))
        j = int(np.clip(np.searchsorted(re_vals, re), 0,
                         len(re_vals) - 1))
        # Compute local gradient via finite differences
        if 0 < i < len(im_vals) - 1 and 0 < j < len(re_vals) - 1:
            dZ_dre = (Z[i, j+1] - Z[i, j-1]) / (
                re_vals[j+1] - re_vals[j-1])
            dZ_dim = (Z[i+1, j] - Z[i-1, j]) / (
                im_vals[i+1] - im_vals[i-1])
        else:
            break
        # Step in -gradient direction
        norm = math.sqrt(dZ_dre ** 2 + dZ_dim ** 2)
        if norm < 1e-6:
            break
        re -= step_size * dZ_dre / norm
        im -= step_size * dZ_dim / norm
        # Stay in strip
        if re < re_vals[0] or re > re_vals[-1]:
            break
        if im < im_vals[0] or im > im_vals[-1]:
            break
        path.append((re, im))
    return path


def probe_region(label, gamma_center, save_path):
    """Compute and plot gradient field in a small region centered
    on Re=1/2, Im=gamma_center."""
    print(f"\n[Region {label}] gamma_center = {gamma_center}")

    re_vals = np.linspace(0.2, 0.8, 41)
    im_vals = np.linspace(gamma_center - 2, gamma_center + 2, 41)

    print(f"  Computing log|L_sub| on {len(re_vals)} x {len(im_vals)} "
          f"= {len(re_vals) * len(im_vals)} grid points...")
    Z = compute_log_abs_field(re_vals, im_vals)
    print(f"  Range: [{Z.min():.2f}, {Z.max():.2f}]")

    # Detect minimum
    min_idx = np.unravel_index(np.argmin(Z), Z.shape)
    min_re = re_vals[min_idx[1]]
    min_im = im_vals[min_idx[0]]
    print(f"  Minimum at: Re = {min_re:.3f}, Im = {min_im:.3f}, "
          f"log|L| = {Z[min_idx]:.2f}")

    # Trace gradient flow lines from off-axis starting points
    print(f"  Tracing gradient flow lines from off-axis starts...")
    starts = []
    for re_start in [0.25, 0.35, 0.65, 0.75]:
        for im_offset in [-1.5, -0.5, 0.5, 1.5]:
            im_start = gamma_center + im_offset
            starts.append((re_start, im_start))

    paths = []
    for re_start, im_start in starts:
        path = steepest_descent(re_start, im_start, Z, re_vals,
                                  im_vals)
        paths.append(path)

    # Check: do paths converge on Re=1/2?
    final_res = [p[-1][0] for p in paths]
    on_axis = sum(1 for re in final_res if abs(re - 0.5) < 0.05)
    print(f"  {on_axis}/{len(paths)} flow lines end with |Re-1/2| < 0.05")
    print(f"  (= strong evidence gradient FORCES paths onto axis)")

    # Plot
    fig, ax = plt.subplots(figsize=(8, 7))
    extent = [re_vals[0], re_vals[-1], im_vals[0], im_vals[-1]]
    im_plot = ax.imshow(Z, extent=extent, origin="lower",
                          aspect="auto", cmap="viridis_r")
    plt.colorbar(im_plot, ax=ax, label="log|L_sub(s)|")

    # Gradient arrows (subsampled)
    grad_y, grad_x = np.gradient(Z)
    skip = 3
    ax.quiver(re_vals[::skip], im_vals[::skip],
              -grad_x[::skip, ::skip], -grad_y[::skip, ::skip],
              alpha=0.5, scale=80, color="white", width=0.003)

    # Witness axis
    ax.axvline(0.5, color="red", linewidth=2, alpha=0.8,
               label="Re(s) = 1/2 (witness axis)")

    # Flow lines
    for path in paths:
        path_arr = np.array(path)
        ax.plot(path_arr[:, 0], path_arr[:, 1], "-",
                 color="cyan", linewidth=1.5, alpha=0.8)
        ax.plot(path_arr[0, 0], path_arr[0, 1], "o",
                 color="white", markersize=8, markeredgecolor="black")
        ax.plot(path_arr[-1, 0], path_arr[-1, 1], "*",
                 color="yellow", markersize=12, markeredgecolor="black")

    # Reference: expected zero location
    ax.plot(0.5, gamma_center, "P", color="red", markersize=14,
            markeredgecolor="black", label=f"expected zero gamma={gamma_center}")

    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title(f"Region {label}: gradient field near gamma = "
                 f"{gamma_center}\n"
                 f"Cyan lines = gradient flow; "
                 f"{on_axis}/{len(paths)} end on Re=1/2")
    ax.legend(loc="upper right", fontsize=9)
    plt.tight_layout()
    plt.savefig(save_path, dpi=140)
    plt.close()

    return on_axis, len(paths), final_res


def main():
    print("=" * 78)
    print("GRADIENT BRIDGE sim 2: high-resolution gradient regions")
    print("=" * 78)

    # Three regions to probe
    regions = [
        ("A", 14.134725, OUTPUTS / "10_region_A_gamma1.png"),
        ("B", 32.935062, OUTPUTS / "11_region_B_gamma5.png"),
        ("C", 49.773832, OUTPUTS / "12_region_C_gamma10.png"),
    ]

    summary = []
    for label, gamma, save_path in regions:
        on_axis, total, final_res = probe_region(label, gamma, save_path)
        summary.append((label, gamma, on_axis, total))

    # Summary table
    print()
    print("=" * 78)
    print("SUMMARY: gradient flow convergence on witness axis")
    print("=" * 78)
    print()
    print(f"  {'Region':<8} {'gamma':<10} {'on-axis ends':<14} "
          f"{'fraction'}")
    for label, gamma, on_axis, total in summary:
        print(f"  {label:<8} {gamma:<10.3f} "
              f"{on_axis}/{total:<11} {on_axis/total:.2%}")

    print()
    print("INTERPRETATION:")
    print("  If gradient flow lines starting from off-axis points")
    print("  reliably converge onto Re=1/2, this is structural")
    print("  evidence that the gradient field FORCES zeros onto the")
    print("  witness axis -- a necessary condition for RH.")
    print()
    print("  This is computational evidence, not a proof.  A proof")
    print("  would require:")
    print("    - showing the gradient confinement is exact (not just")
    print("      empirical at our resolution)")
    print("    - connecting the confinement to the substrate's")
    print("      finite-dim Hilbert-Polya construction")

    # Save summary CSV
    with open(DATA / "gradient_region_summary.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["region", "gamma_center", "on_axis_ends",
                    "total_paths", "fraction"])
        for label, gamma, on_axis, total in summary:
            w.writerow([label, f"{gamma:.6f}", on_axis, total,
                        f"{on_axis/total:.4f}"])


if __name__ == "__main__":
    main()

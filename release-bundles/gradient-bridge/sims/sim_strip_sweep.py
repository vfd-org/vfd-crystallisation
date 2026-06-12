"""Gradient Bridge sim 1: sweep L_sub across the critical strip.

Maps |L_sub(s)| over a grid covering the entire critical strip
0 < Re(s) < 1, |Im(s)| <= 50.  Identifies zeros (where |L_sub|
locally minimises near zero) and computes the gradient
field nabla|L_sub| at each grid point.

This is the FIRST step toward the gradient bridge: see what the
gradient structure actually looks like in the critical strip,
not just on the centerline.

The substrate framework only natively covers Re(s) = 1/2.  This
sim asks: what does the analytical landscape look like in the
2D region surrounding the centerline?  Answers we want:
  - How sharp is the gradient toward zeros?
  - Are zeros confined to Re = 1/2 in our scan?
  - What is the structure of |L_sub| just off the centerline?

Outputs:
  outputs/01_strip_heatmap.png    -- |L_sub| heatmap over strip
  outputs/02_gradient_field.png   -- arrow field of nabla|L_sub|
  outputs/03_zero_locations.png   -- detected zeros + critical line
  data/strip_values.csv           -- raw |L_sub| values
  data/detected_zeros.csv         -- found zeros (Re, Im, |L_sub|)
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

mp.mp.dps = 20


def chi5(n):
    r = n % 5
    if r == 0:
        return 0
    return {1: 1, 4: 1, 2: -1, 3: -1}[r]


def dirichlet_L_chi5(s, n_terms=150):
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        c = chi5(n)
        if c != 0:
            total += c / mp.power(n, s)
    return total


def zeta_K(s, n_terms=150):
    return mp.zeta(s) * dirichlet_L_chi5(s, n_terms)


def C_2(s):
    return 1 - 2 * mp.power(2, -s) + mp.power(2, 2 - 2 * s)


def L_substrate(s, n_terms=150):
    return zeta_K(s, n_terms) * zeta_K(s - 1, n_terms) * C_2(s)


def main():
    print("=" * 76)
    print("GRADIENT BRIDGE sim 1: strip sweep")
    print("=" * 76)

    # Grid over critical strip
    print("\n[1] Building grid over critical strip...")
    n_re = 41   # Re values from 0.05 to 0.95
    n_im = 81   # Im values from -50 to +50 (skip Im=0 region near pole)
    re_vals = np.linspace(0.05, 0.95, n_re)
    im_vals = np.linspace(-50.0, 50.0, n_im)

    # Compute |L_sub| at each grid point
    print(f"\n[2] Computing |L_sub(s)| on {n_re} x {n_im} grid...")
    print("    (~ {:.0f} evaluations; mpmath, this will take a moment)"
          .format(n_re * n_im))

    Z = np.zeros((n_im, n_re))
    for i, im in enumerate(im_vals):
        if i % 10 == 0:
            print(f"    progress: row {i}/{n_im}")
        for j, re in enumerate(re_vals):
            s = mp.mpc(float(re), float(im))
            try:
                val = abs(L_substrate(s))
                Z[i, j] = float(val)
            except (OverflowError, ValueError):
                Z[i, j] = float("nan")

    # Save raw values
    with open(DATA / "strip_values.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Re", "Im", "abs_L_sub"])
        for i, im in enumerate(im_vals):
            for j, re in enumerate(re_vals):
                w.writerow([f"{re:.4f}", f"{im:.4f}", f"{Z[i,j]:.6e}"])

    # Detect local minima below threshold (candidate zeros)
    print("\n[3] Detecting candidate zeros (local minima of |L_sub|)...")
    log_Z = np.log10(Z + 1e-30)
    median_log = float(np.median(log_Z))
    threshold = median_log - 2.0  # 100x smaller than median

    zeros = []
    for i in range(1, n_im - 1):
        for j in range(1, n_re - 1):
            local_min = (log_Z[i, j] < log_Z[i-1, j] and
                          log_Z[i, j] < log_Z[i+1, j] and
                          log_Z[i, j] < log_Z[i, j-1] and
                          log_Z[i, j] < log_Z[i, j+1])
            if local_min and log_Z[i, j] < threshold:
                zeros.append((re_vals[j], im_vals[i], Z[i, j]))
    print(f"    Found {len(zeros)} candidate zeros below threshold")

    with open(DATA / "detected_zeros.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Re", "Im", "abs_L_sub"])
        for re, im, val in zeros:
            w.writerow([f"{re:.4f}", f"{im:.4f}", f"{val:.6e}"])

    # Analyze: which are on Re=1/2?
    on_axis = [z for z in zeros if abs(z[0] - 0.5) < 0.025]
    off_axis = [z for z in zeros if abs(z[0] - 0.5) >= 0.025]
    print(f"    On critical line (|Re-1/2| < 0.025): {len(on_axis)}")
    print(f"    Off critical line:                    {len(off_axis)}")

    if off_axis:
        print("\n    OFF-AXIS ZEROS FOUND (worth investigating):")
        for re, im, val in off_axis[:10]:
            print(f"      Re = {re:.3f}, Im = {im:.3f}, |L| = {val:.2e}")
    else:
        print("\n    NO off-axis zeros detected.  Consistent with RH "
              "in scan range.")

    # ---- Plot heatmap
    print("\n[4] Plotting heatmap...")
    fig, ax = plt.subplots(figsize=(8, 10))
    # log scale for visibility
    plot_Z = log_Z.copy()
    plot_Z = np.clip(plot_Z, -20, 5)
    im = ax.imshow(plot_Z, extent=[re_vals[0], re_vals[-1],
                                     im_vals[0], im_vals[-1]],
                    origin="lower", aspect="auto", cmap="viridis_r")
    plt.colorbar(im, ax=ax, label="log_10 |L_sub(s)|")
    ax.axvline(0.5, color="red", linewidth=1.5,
               label="Re(s) = 1/2 (witness axis)")
    # Mark detected zeros
    for re, im_val, _ in zeros:
        ax.plot(re, im_val, "rx", markersize=8)
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title("|L_sub(s)| over the critical strip\n"
                 "(red x = detected zero; red line = witness axis)")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_strip_heatmap.png", dpi=140)
    plt.close()

    # ---- Gradient field
    print("\n[5] Plotting gradient field...")
    fig, ax = plt.subplots(figsize=(9, 11))
    grad_y, grad_x = np.gradient(log_Z)
    # Subsample for visibility
    skip = 4
    ax.quiver(re_vals[::skip], im_vals[::skip],
              -grad_x[::skip, ::skip], -grad_y[::skip, ::skip],
              alpha=0.6, scale=80, color="navy")
    ax.axvline(0.5, color="red", linewidth=1.5,
               label="Re(s) = 1/2 (witness axis)")
    for re, im_val, _ in zeros:
        ax.plot(re, im_val, "ro", markersize=10, markerfacecolor="none")
    ax.set_xlim(re_vals[0], re_vals[-1])
    ax.set_ylim(im_vals[0], im_vals[-1])
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title("Gradient field -nabla(log|L_sub|) "
                 "(arrows point toward zeros)\n"
                 "Red circles = detected zeros; red line = witness axis")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "02_gradient_field.png", dpi=140)
    plt.close()

    # ---- Zero locations
    print("\n[6] Plotting zero locations...")
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.axvline(0.5, color="red", linewidth=1.5,
               label="Re(s) = 1/2 (witness axis)")
    if on_axis:
        ax.scatter([z[0] for z in on_axis], [z[1] for z in on_axis],
                    s=80, c="blue", marker="x",
                    label=f"on axis ({len(on_axis)})")
    if off_axis:
        ax.scatter([z[0] for z in off_axis], [z[1] for z in off_axis],
                    s=80, c="orange", marker="+",
                    label=f"OFF axis ({len(off_axis)})")
    ax.set_xlim(0, 1)
    ax.set_ylim(im_vals[0], im_vals[-1])
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title("Detected L_sub zeros in critical strip "
                 "(grid resolution ~0.02)")
    ax.legend(loc="lower right")
    ax.axvspan(0, 0.5, alpha=0.05, color="gray")
    ax.axvspan(0.5, 1, alpha=0.05, color="gray")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "03_zero_locations.png", dpi=140)
    plt.close()

    print("\nDone.")
    print(f"  Plots: {OUTPUTS}")
    print(f"  Data:  {DATA}")


if __name__ == "__main__":
    main()

"""Sim v7: reverse-direction zero correspondence.

Sim v4 showed that Riemann zeros of zeta(s) pull back to substrate
L_sub candidate minima attributed (scalar-factor level) to the zeta
factor. This sim asks the
reverse:

  Where do the OTHER L_sub zeros (the ones NOT at Riemann gammas)
  come from?

Factorisation: L_sub(s) = zeta_K(s) * zeta_K(s-1) * C_2(s)
              = zeta(s) * L(s, chi_5) * zeta(s-1) * L(s-1, chi_5) * C_2(s).

On the critical line Re(s) = 1/2, the factors evaluate at:
  zeta(s)         at Re = 1/2    -> Riemann zeros
  L(s, chi_5)     at Re = 1/2    -> Dirichlet L mod 5 critical zeros
  zeta(s-1)       at Re = -1/2   -> NO non-trivial zeros (functional eq.)
  L(s-1, chi_5)   at Re = -1/2   -> NO non-trivial zeros (functional eq.)
  C_2(s)          at Re = 1/2    -> NO zeros (C_2 zeros are at Re = 1)

So on Re(s) = 1/2:
  L_sub vanishes iff zeta(s) = 0 OR L(s, chi_5) = 0.

This sim:
  (1) Sweeps gamma in [0.1, 60], computes L_sub(1/2 + i gamma)
      analytically via mpmath.
  (2) Identifies all local minima of |L_sub| below a threshold
      (candidate zeros).
  (3) For each candidate, attributes the zero to ZETA, CHI_5, or
      both.
  (4) Heuristic sweep (NOT root certification): finds candidate local
      minima of |L_sub|; the tabulated Riemann zeros appear among them
      as zeta-attributed candidates; further minima are smallest where
      the chi_5 factor is smallest. Several candidates carry |L_sub|
      values far from zero and are locations, not certified zeros.
  (5) Records the factor-wise reading of the published Dedekind
      factorisation (orientation only; adds no mathematical content
      and does not restate or approach RH).

This is a heuristic reverse-direction scan, not a closure of any
zero correspondence.
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
OUTPUTS = HERE.parent / "outputs" / "v7"
DATA = HERE.parent / "data" / "v7"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

mp.mp.dps = 30


def chi5(n):
    r = n % 5
    if r == 0:
        return 0
    return {1: 1, 4: 1, 2: -1, 3: -1}[r]


def dirichlet_L_chi5(s, n_terms=300):
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        c = chi5(n)
        if c != 0:
            total += c / mp.power(n, s)
    return total


def zeta_K(s, n_terms=300):
    return mp.zeta(s) * dirichlet_L_chi5(s, n_terms)


def C_2(s):
    return 1 - 2 * mp.power(2, -s) + mp.power(2, 2 - 2 * s)


def L_substrate(s, n_terms=300):
    return zeta_K(s, n_terms) * zeta_K(s - 1, n_terms) * C_2(s)


# Reference Riemann zeros (first 15) - imaginary parts.
RIEMANN_ZEROS = [
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063246,
    59.347044002602353,
]

# First few Dirichlet L(s, chi_5) zeros (imaginary parts).
# These are NOT widely tabulated; we'll compute them by searching
# along Re(s) = 1/2 in the same sweep.


def find_zeros_by_sweep(f, gamma_min, gamma_max, n_grid=4000,
                        local_min_threshold=0.5):
    """Find local minima of |f(1/2 + i gamma)| over [gamma_min, gamma_max].

    Returns list of gamma values where |f| is locally minimal and
    below local_min_threshold * (median of values).
    """
    gammas = np.linspace(gamma_min, gamma_max, n_grid)
    vals = np.zeros(n_grid)
    for i, gamma in enumerate(gammas):
        s = mp.mpc(0.5, gamma)
        try:
            v = abs(f(s))
        except Exception:
            v = mp.mpf(0)
        vals[i] = float(v)
    median_val = float(np.median(vals))
    threshold = max(local_min_threshold * median_val, 1e-8)

    minima = []
    for i in range(2, n_grid - 2):
        # local-min over 5-point neighborhood
        if (vals[i] < vals[i - 1] and vals[i] < vals[i + 1]
                and vals[i] < vals[i - 2] and vals[i] < vals[i + 2]):
            if vals[i] < threshold:
                # refine via golden section in a tight window
                refined_gamma = refine_minimum(f, gammas[i - 1],
                                               gammas[i + 1])
                refined_val = float(abs(f(mp.mpc(0.5, refined_gamma))))
                minima.append((refined_gamma, refined_val))
    return gammas, vals, minima


def refine_minimum(f, a, b, n_iter=30):
    """Golden-section search for the minimum of |f(1/2 + i*gamma)|."""
    phi_g = (math.sqrt(5) - 1) / 2  # 1/phi
    c = b - phi_g * (b - a)
    d = a + phi_g * (b - a)
    fc = float(abs(f(mp.mpc(0.5, c))))
    fd = float(abs(f(mp.mpc(0.5, d))))
    for _ in range(n_iter):
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = b - phi_g * (b - a)
            fc = float(abs(f(mp.mpc(0.5, c))))
        else:
            a = c
            c = d
            fc = fd
            d = a + phi_g * (b - a)
            fd = float(abs(f(mp.mpc(0.5, d))))
    return (a + b) / 2


def attribute_zero(gamma, threshold=1e-3):
    """Given gamma such that L_sub(1/2 + i gamma) ~ 0, attribute to
    one or both of: zeta(s), L(s, chi_5).

    Returns dict with keys: zeta_val, chi5_val, attribution.
    """
    s = mp.mpc(0.5, gamma)
    z = float(abs(mp.zeta(s)))
    L = float(abs(dirichlet_L_chi5(s)))

    contribs = []
    if z < threshold:
        contribs.append("ZETA (sigma-fixed, Riemann zero)")
    if L < threshold:
        contribs.append("CHI_5 (sigma-paired, Dirichlet L_5 zero)")
    if not contribs:
        attribution = "neither factor vanishes -- numerical artefact?"
    else:
        attribution = " + ".join(contribs)
    return {"gamma": gamma, "zeta_val": z, "chi5_val": L,
            "attribution": attribution}


def main():
    findings = []
    print("=" * 70)
    print("SIM v7: reverse-direction zero correspondence")
    print("=" * 70)

    print("\n[1] Sweeping L_sub along Re(s) = 1/2, gamma in [0.1, 60]...")
    gammas, vals, minima = find_zeros_by_sweep(
        L_substrate, gamma_min=0.1, gamma_max=60.0,
        n_grid=2400, local_min_threshold=0.01
    )
    findings.append(f"Found {len(minima)} candidate L_sub zeros in "
                    f"gamma in [0.1, 60].")
    findings.append("")

    # Attribute each
    print("\n[2] Attributing each candidate zero to a factor...")
    attributions = []
    for gamma, val in minima:
        a = attribute_zero(gamma, threshold=1e-2)
        a["L_sub_val"] = val
        attributions.append(a)

    # Match to Riemann zeros
    matched_riemann = set()
    chi5_zeros = []
    findings.append(f"  {'gamma':<11} {'|L_sub|':<11} {'|zeta|':<11} "
                    f"{'|L(s,chi_5)|':<12} {'attribution'}")
    for a in attributions:
        # Match to nearest Riemann zero
        nearest_R = None
        for k, rz in enumerate(RIEMANN_ZEROS):
            if abs(rz - a["gamma"]) < 0.1:
                nearest_R = (k + 1, rz)
                matched_riemann.add(k + 1)
                break
        if nearest_R:
            tag = f" (== Riemann zero #{nearest_R[0]})"
        elif "CHI_5" in a["attribution"]:
            chi5_zeros.append(a)
            tag = " (chi_5 zero)"
        else:
            tag = ""
        findings.append(
            f"  {a['gamma']:<11.5f} {a['L_sub_val']:<11.2e} "
            f"{a['zeta_val']:<11.2e} {a['chi5_val']:<12.2e} "
            f"{a['attribution']}{tag}"
        )

    findings.append("")
    findings.append(f"Riemann zeros matched (out of first 13 listed): "
                    f"{len(matched_riemann)} / "
                    f"{sum(1 for r in RIEMANN_ZEROS if r <= 60)}")
    findings.append(f"chi_5 zeros found (NEW): {len(chi5_zeros)}")

    findings.append("")
    findings.append("HEURISTIC ATTRIBUTION (candidate minima on Re(s) = 1/2; not certified zeros):")
    findings.append("  Every L_sub zero on the critical line is")
    findings.append("  attributable to a vanishing factor:")
    findings.append("    zeta(s) = 0    => tau-fixed (substrate-94 block)")
    findings.append("    L(s, chi_5) = 0 => tau-paired (substrate-26 block)")
    findings.append("    no other factor of L_sub vanishes on Re(s)=1/2.")
    findings.append("")
    findings.append("FACTOR-WISE READING (orientation only; adds no mathematical content):")
    findings.append("  Factor-wise reading of the published factorisation:")
    findings.append("  zeta(s) is the sigma-fixed Dedekind factor and")
    findings.append("  L(s, chi_5) the sigma-paired one; the 94 + (13 + 13)")
    findings.append("  split is spectral bookkeeping (candidate tau only).")
    findings.append("  This bookkeeping does not restate RH and resolves")
    findings.append("  nothing; attributions here are scalar-factor level;")
    findings.append("  the classical conjectures are untouched.")

    # Save data
    with open(DATA / "l_sub_zeros_attribution.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["gamma", "L_sub_val", "zeta_val", "chi5_val",
                    "attribution"])
        for a in attributions:
            w.writerow([f"{a['gamma']:.8f}",
                        f"{a['L_sub_val']:.6e}",
                        f"{a['zeta_val']:.6e}",
                        f"{a['chi5_val']:.6e}",
                        a['attribution']])

    # Plot
    print("\n[3] Plotting zero attribution along critical line...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 9),
                                    sharex=True)

    # Top: |L_sub|, |zeta|, |L(s, chi_5)|
    zeta_vals = []
    chi5_vals = []
    for gamma in gammas:
        s = mp.mpc(0.5, gamma)
        zeta_vals.append(float(abs(mp.zeta(s))))
        chi5_vals.append(float(abs(dirichlet_L_chi5(s, n_terms=200))))
    zeta_vals = np.array(zeta_vals)
    chi5_vals = np.array(chi5_vals)
    vals_arr = np.array(vals)
    ax1.semilogy(gammas, np.maximum(vals_arr, 1e-30),
                 color="black", linewidth=0.7, label="|L_sub|", alpha=0.7)
    ax1.semilogy(gammas, np.maximum(zeta_vals, 1e-30),
                 color="tab:blue", linewidth=0.6, label="|zeta(s)|",
                 alpha=0.7)
    ax1.semilogy(gammas, np.maximum(chi5_vals, 1e-30),
                 color="tab:orange", linewidth=0.6,
                 label="|L(s, chi_5)|", alpha=0.7)
    # Mark candidate zeros
    for a in attributions:
        if "ZETA" in a["attribution"]:
            ax1.axvline(a["gamma"], color="tab:blue", linestyle=":",
                        alpha=0.4, linewidth=0.5)
        if "CHI_5" in a["attribution"]:
            ax1.axvline(a["gamma"], color="tab:orange", linestyle=":",
                        alpha=0.4, linewidth=0.5)
    ax1.set_ylabel("|.| (log scale)")
    ax1.legend(loc="best")
    ax1.set_title(
        "Critical-line factor decomposition of L_sub(1/2 + i gamma)\n"
        "Blue dotted = zeta-attributed zero (tau-fixed); "
        "orange dotted = chi_5-attributed (tau-paired)"
    )
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(bottom=1e-16)

    # Bottom: classification scatter
    zeta_class = [a for a in attributions if "ZETA" in a["attribution"]]
    chi5_class = [a for a in attributions if "CHI_5" in a["attribution"]
                  and "ZETA" not in a["attribution"]]
    other_class = [a for a in attributions
                   if "ZETA" not in a["attribution"]
                   and "CHI_5" not in a["attribution"]]
    if zeta_class:
        ax2.scatter([a["gamma"] for a in zeta_class],
                    [1.0] * len(zeta_class), color="tab:blue", s=120,
                    edgecolors="black", label=f"zeta-zero (tau-fixed): "
                    f"{len(zeta_class)}", marker="^")
    if chi5_class:
        ax2.scatter([a["gamma"] for a in chi5_class],
                    [2.0] * len(chi5_class), color="tab:orange", s=120,
                    edgecolors="black",
                    label=f"chi_5-zero (tau-paired): {len(chi5_class)}",
                    marker="v")
    if other_class:
        ax2.scatter([a["gamma"] for a in other_class],
                    [3.0] * len(other_class), color="tab:red", s=80,
                    edgecolors="black",
                    label=f"unclassified: {len(other_class)}", marker="x")
    ax2.set_yticks([1.0, 2.0, 3.0])
    ax2.set_yticklabels(["zeta (tau-fixed)", "chi_5 (tau-paired)",
                         "other"])
    ax2.set_xlabel("gamma  (imaginary part of s on Re(s) = 1/2)")
    ax2.set_title("Substrate decomposition of all L_sub zeros found in "
                  "[0, 60]")
    ax2.legend(loc="best")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_zero_decomposition.png", dpi=140)
    plt.close()

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

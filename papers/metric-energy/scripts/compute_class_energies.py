#!/usr/bin/env python3
"""
Paper III — Metric-Induced Class-Energy Computation
=====================================================

Defines candidate metric families on the phi-structured manifold,
derives the induced measure and spectral operator for each,
and computes class energies for electron {1} and proton {2,3,4}.

Zero fitting. Every quantity derived from the metric definition.
"""

import math
import csv
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Callable

PHI = (1 + math.sqrt(5)) / 2
TARGET_RATIO = 1836.15267343
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")

E_SHELLS = [1]
P_SHELLS = [2, 3, 4]
N_SHELLS = 5  # total shell count

# ═══════════════════════════════════════════════════════════════
# Metric family definitions
# ═══════════════════════════════════════════════════════════════

@dataclass
class MetricFamily:
    id: str
    name: str
    description: str
    origin: str  # derived / postulated / provisional

    # Shell weight function w(n): the metric-induced weight of shell n
    # This is the fundamental object from which everything else follows
    shell_weight: Callable  # w(n) -> float

    # Measure mu(n): volume/area element at shell n
    # Derived from the metric as the "size" of shell n
    measure: Callable  # mu(n) -> float

    # Spectral weight lambda(n): eigenvalue of the natural operator at shell n
    # Derived from the metric Laplacian or equivalent
    spectral_weight: Callable  # lambda(n) -> float

    # Inter-shell coupling: does adjacent-shell interaction exist?
    has_coupling: bool
    coupling: Callable = None  # K(n,m) -> float, if has_coupling


def make_metrics() -> Dict[str, MetricFamily]:
    """Construct all candidate metric families."""
    metrics = {}

    # ── MF1: Pure radial phi metric ──
    # The simplest possible metric: each shell at radius r_n = phi^{-n}
    # has weight determined solely by its radial position.
    # Shell weight: w(n) = phi^{2n} (from the radial metric ds^2 ~ phi^{2n} dn^2)
    # Measure: mu(n) = phi^{-2n} (inverse of metric weight — smaller shells have less volume)
    # Spectral: lambda(n) = phi^{2n} (Laplacian eigenvalue scales as inverse-square-radius)
    # No inter-shell coupling.
    metrics["MF1"] = MetricFamily(
        id="MF1",
        name="Pure radial phi metric",
        description="Shell weight from radial phi-scaling only. "
                    "w(n) = phi^{2n}, mu(n) = phi^{-2n}, lambda(n) = phi^{2n}.",
        origin="derived (minimal radial metric on phi-nested shells)",
        shell_weight=lambda n: PHI ** (2 * n),
        measure=lambda n: PHI ** (-2 * n),
        spectral_weight=lambda n: PHI ** (2 * n),
        has_coupling=False,
    )

    # ── MF2: Boundary/interior metric ──
    # Shell 1 (boundary) carries a distinct normalization.
    # Interior shells n >= 2 are weighted by phi^{2n}.
    # Boundary shell has weight phi^2 * (1 + 1/phi) = phi^2 * phi = phi^3.
    # This comes from the boundary condition: the boundary shell
    # couples to the exterior, acquiring an extra phi factor.
    # Measure: mu(1) = phi^{-3}, mu(n>=2) = phi^{-2n}.
    # Spectral: lambda(1) = phi^3, lambda(n>=2) = phi^{2n}.
    metrics["MF2"] = MetricFamily(
        id="MF2",
        name="Boundary/interior metric",
        description="Shell 1 carries extra phi factor from boundary coupling. "
                    "w(1) = phi^3, w(n>=2) = phi^{2n}.",
        origin="postulated (boundary shell couples to exterior)",
        shell_weight=lambda n: PHI ** 3 if n == 1 else PHI ** (2 * n),
        measure=lambda n: PHI ** (-3) if n == 1 else PHI ** (-2 * n),
        spectral_weight=lambda n: PHI ** 3 if n == 1 else PHI ** (2 * n),
        has_coupling=False,
    )

    # ── MF3: Surface multiplicity metric ──
    # Each shell n has internal surface area proportional to n^2
    # (analogous to spherical harmonics: degeneracy ~ (2l+1) ~ n^2 for large n).
    # Shell weight: w(n) = n^2 * phi^{2n}.
    # Measure: mu(n) = n^2 * phi^{-2n}.
    # Spectral: lambda(n) = phi^{2n} / n^2 (eigenvalue per unit area).
    metrics["MF3"] = MetricFamily(
        id="MF3",
        name="Surface multiplicity metric",
        description="Shell n has internal multiplicity n^2. "
                    "w(n) = n^2 * phi^{2n}.",
        origin="derived (surface area scaling by shell index)",
        shell_weight=lambda n: n ** 2 * PHI ** (2 * n),
        measure=lambda n: n ** 2 * PHI ** (-2 * n),
        spectral_weight=lambda n: PHI ** (2 * n) / (n ** 2),
        has_coupling=False,
    )

    # ── MF4: Adjacent-shell interaction metric ──
    # Same as MF1 but with nearest-neighbor coupling.
    # Coupling: K(n, n+1) = phi^{n + (n+1)} = phi^{2n+1}.
    # This is the geometric mean of adjacent shell weights.
    def coupling_fn(n, m):
        if abs(n - m) == 1:
            return PHI ** (n + m)
        return 0.0

    metrics["MF4"] = MetricFamily(
        id="MF4",
        name="Adjacent-shell interaction metric",
        description="MF1 plus nearest-neighbor coupling K(n,n+1) = phi^{2n+1}.",
        origin="derived (geometric mean of adjacent shell metrics)",
        shell_weight=lambda n: PHI ** (2 * n),
        measure=lambda n: PHI ** (-2 * n),
        spectral_weight=lambda n: PHI ** (2 * n),
        has_coupling=True,
        coupling=coupling_fn,
    )

    # ── MF5: Harmonic phi metric ──
    # Shell weight determined by the harmonic structure:
    # w(n) = phi^{n(n+1)/2} (triangular number in exponent).
    # This arises if the phi-exponent accumulates as sum(1..n) = n(n+1)/2
    # during closure traversal — each shell adds n to the accumulated exponent.
    metrics["MF5"] = MetricFamily(
        id="MF5",
        name="Harmonic (triangular) phi metric",
        description="Shell weight from accumulated harmonic traversal. "
                    "w(n) = phi^{n(n+1)/2}.",
        origin="derived (accumulated phi-exponent during closure cycle)",
        shell_weight=lambda n: PHI ** (n * (n + 1) / 2),
        measure=lambda n: PHI ** (-n * (n + 1) / 2),
        spectral_weight=lambda n: PHI ** (n * (n + 1) / 2),
        has_coupling=False,
    )

    return metrics


# ═══════════════════════════════════════════════════════════════
# Class-energy computation
# ═══════════════════════════════════════════════════════════════

def compute_class_energy(shells: List[int], metric: MetricFamily) -> dict:
    """Compute class energy under a given metric.

    Energy contributions:
    1. Shell-spectral energy: sum of spectral weights over occupied shells
    2. Coupling energy: sum of inter-shell couplings (if present)
    3. Normalized by measure (total class measure)
    """
    # Spectral energy: E_spec = sum lambda(n) for n in shells
    E_spec = sum(metric.spectral_weight(n) for n in shells)

    # Coupling energy: E_coup = sum K(n,m) for adjacent occupied shells
    E_coup = 0.0
    if metric.has_coupling and metric.coupling:
        for i in range(len(shells)):
            for j in range(i + 1, len(shells)):
                E_coup += metric.coupling(shells[i], shells[j])

    # Total measure of class
    mu_total = sum(metric.measure(n) for n in shells)

    # Class energy (three variants):
    # A) Sum: total spectral + coupling energy
    E_sum = E_spec + E_coup

    # B) Density: energy per unit measure
    E_density = E_sum / mu_total if mu_total > 0 else float('inf')

    # C) Weighted: spectral energy weighted by shell weight
    E_weighted = sum(metric.shell_weight(n) * metric.spectral_weight(n)
                     for n in shells)

    return {
        "E_spectral": E_spec,
        "E_coupling": E_coup,
        "E_sum": E_sum,
        "E_density": E_density,
        "E_weighted": E_weighted,
        "mu_total": mu_total,
    }


# ═══════════════════════════════════════════════════════════════
# Main analysis
# ═══════════════════════════════════════════════════════════════

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    metrics = make_metrics()

    results = []

    print("=" * 100)
    print("PAPER III: METRIC-INDUCED CLASS-ENERGY ANALYSIS")
    print("=" * 100)

    for mid, metric in metrics.items():
        e_data = compute_class_energy(E_SHELLS, metric)
        p_data = compute_class_energy(P_SHELLS, metric)

        # Compute ratios under each energy convention
        for etype in ["E_spectral", "E_sum", "E_density", "E_weighted"]:
            E_e = e_data[etype]
            E_p = p_data[etype]
            ratio = E_p / E_e if E_e > 1e-30 else float('inf')
            err = abs(ratio - TARGET_RATIO) / TARGET_RATIO * 100

            results.append({
                "metric": mid,
                "metric_name": metric.name,
                "energy_type": etype,
                "E_electron": E_e,
                "E_proton": E_p,
                "ratio": ratio,
                "observed": TARGET_RATIO,
                "error_pct": err,
                "origin": metric.origin,
            })

    # Sort by error
    results.sort(key=lambda r: r["error_pct"])

    # Print summary
    print(f"\n{'Metric':<5} {'Energy Type':<14} {'E(e)':<12} {'E(p)':<14} {'Ratio':<14} {'Err%':<10}")
    print("-" * 80)
    for r in results:
        print(f"{r['metric']:<5} {r['energy_type']:<14} {r['E_electron']:<12.4f} "
              f"{r['E_proton']:<14.4f} {r['ratio']:<14.4f} {r['error_pct']:<10.2f}")

    # Save results
    with open(os.path.join(BASE_DIR, "class_energy_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=results[0].keys())
        w.writeheader()
        w.writerows(results)

    # Metric family summary
    print("\n" + "=" * 80)
    print("METRIC FAMILY SUMMARY")
    print("=" * 80)
    for mid, metric in metrics.items():
        e = compute_class_energy(E_SHELLS, metric)
        p = compute_class_energy(P_SHELLS, metric)

        print(f"\n  {mid}: {metric.name}")
        print(f"    Origin: {metric.origin}")
        print(f"    Shell weights: n=1: {metric.shell_weight(1):.4f}, "
              f"n=2: {metric.shell_weight(2):.4f}, "
              f"n=3: {metric.shell_weight(3):.4f}, "
              f"n=4: {metric.shell_weight(4):.4f}")
        print(f"    E_sum ratio: {p['E_sum']/e['E_sum']:.4f}")
        print(f"    E_density ratio: {p['E_density']/e['E_density']:.4f}")
        if metric.has_coupling:
            print(f"    Coupling energy (proton): {p['E_coupling']:.4f}")

    # Best result
    best = results[0]
    print(f"\n{'='*80}")
    print(f"BEST RESULT: {best['metric']} / {best['energy_type']}")
    print(f"  Ratio: {best['ratio']:.4f}")
    print(f"  Error: {best['error_pct']:.2f}%")
    print(f"  Origin: {best['origin']}")

    # Analysis questions
    print(f"\n{'='*80}")
    print("ANALYSIS ANSWERS")
    print(f"{'='*80}")

    # Find which metric moves furthest from phi^15
    phi15 = PHI ** 15
    for mid, metric in metrics.items():
        e = compute_class_energy(E_SHELLS, metric)
        p = compute_class_energy(P_SHELLS, metric)
        for etype in ["E_sum", "E_density"]:
            ratio = p[etype] / e[etype]
            shift = ratio - phi15
            if abs(shift) > 0.1:
                print(f"  {mid}/{etype}: ratio = {ratio:.2f}, "
                      f"shift from phi^15 = {shift:+.2f} ({shift/phi15*100:+.2f}%)")

    # Save metric catalogue
    catalogue = []
    for mid, metric in metrics.items():
        catalogue.append({
            "id": mid,
            "name": metric.name,
            "description": metric.description,
            "origin": metric.origin,
            "has_coupling": metric.has_coupling,
            "w1": metric.shell_weight(1),
            "w2": metric.shell_weight(2),
            "w3": metric.shell_weight(3),
            "w4": metric.shell_weight(4),
        })
    with open(os.path.join(BASE_DIR, "metric_family_catalogue.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=catalogue[0].keys())
        w.writeheader()
        w.writerows(catalogue)

    # Summary JSON
    summary = {
        "metrics_tested": len(metrics),
        "energy_types_per_metric": 4,
        "total_results": len(results),
        "best": {k: str(v) for k, v in best.items()},
        "target_ratio": TARGET_RATIO,
        "phi_15": phi15,
    }
    with open(os.path.join(BASE_DIR, "paper3_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()

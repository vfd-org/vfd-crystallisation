#!/usr/bin/env python3
"""
Paper II — Minimal Deterministic Mass-Ratio Model
===================================================
Stage 3: Compute mass ratios and compare against observed values.

For each (freq_law, amp_law, phase_law) combination, takes the
stable representatives for electron/proton/neutron classes and
computes predicted mass ratios.

All computation is deterministic.
"""

import csv
import json
import math
import os

# ═══════════════════════════════════════════════════════════════
# Observed values (PDG 2022)
# ═══════════════════════════════════════════════════════════════

OBSERVED_MP_ME = 1836.15267343   # proton/electron mass ratio
OBSERVED_MN_MP = 1.00137841898   # neutron/proton mass ratio
OBSERVED_MN_ME_DIFF = 1.29333236  # (mn - mp) in MeV/c^2


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts")

    # Load stable states
    stable_path = os.path.join(base_dir, "stable_states.csv")
    with open(stable_path, "r") as f:
        reader = csv.DictReader(f)
        stable = list(reader)

    # Group by model combination (including energy law)
    models = {}
    for s in stable:
        key = (s["freq_law"], s["amp_law"], s["phase_law"], s.get("energy_law", "default"))
        if key not in models:
            models[key] = {}
        models[key][s["symmetry"]] = s

    # Compute ratios
    results = []
    for key, states in sorted(models.items()):
        freq, amp, phase = key[0], key[1], key[2]
        electron = states.get("charged_lepton")
        proton = states.get("baryon")
        neutron = states.get("baryon_neutral")

        if not (electron and proton):
            continue

        E_e = float(electron["energy"])
        E_p = float(proton["energy"])
        E_n = float(neutron["energy"]) if neutron else None

        if E_e < 1e-30:
            continue

        ratio_pe = E_p / E_e
        ratio_ne = E_n / E_e if E_n else None
        ratio_np = E_n / E_p if (E_n and E_p > 1e-30) else None

        pct_err_pe = abs(ratio_pe - OBSERVED_MP_ME) / OBSERVED_MP_ME * 100
        pct_err_np = abs(ratio_np - OBSERVED_MN_MP) / OBSERVED_MN_MP * 100 if ratio_np else None

        hierarchy_correct = ratio_pe > 1 and (ratio_np is None or ratio_np > 1)

        energy_law = key[3] if len(key) > 3 else "default"
        results.append({
            "freq_law": freq,
            "amp_law": amp,
            "phase_law": phase,
            "energy_law": energy_law,
            "E_electron": f"{E_e:.12e}",
            "E_proton": f"{E_p:.12e}",
            "E_neutron": f"{E_n:.12e}" if E_n else "N/A",
            "predicted_mp_me": f"{ratio_pe:.6f}",
            "observed_mp_me": f"{OBSERVED_MP_ME:.6f}",
            "pct_error_mp_me": f"{pct_err_pe:.4f}",
            "predicted_mn_mp": f"{ratio_np:.8f}" if ratio_np else "N/A",
            "observed_mn_mp": f"{OBSERVED_MN_MP:.8f}",
            "pct_error_mn_mp": f"{pct_err_np:.4f}" if pct_err_np else "N/A",
            "hierarchy_correct": str(hierarchy_correct),
            "e_shells": electron["shells"],
            "p_shells": proton["shells"],
            "n_shells": neutron["shells"] if neutron else "N/A",
        })

    # Sort by mp/me error (best first)
    results.sort(key=lambda r: float(r["pct_error_mp_me"]))

    # Write ratio results
    out_path = os.path.join(base_dir, "ratio_results.csv")
    if results:
        with open(out_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

    # Print summary
    print(f"=== Mass Ratio Analysis ({len(results)} model combinations) ===\n")
    print(f"{'Freq Law':<20} {'Amp Law':<16} {'Phase Law':<18} {'mp/me':>12} {'err%':>8} {'mn/mp':>12} {'Hierarchy':>10}")
    print("-" * 100)
    for r in results[:15]:  # top 15
        print(f"{r['freq_law']:<20} {r['amp_law']:<16} {r['phase_law']:<18} "
              f"{r['predicted_mp_me']:>12} {r['pct_error_mp_me']:>8} "
              f"{r['predicted_mn_mp']:>12} {r['hierarchy_correct']:>10}")

    # Best result
    if results:
        best = results[0]
        print(f"\n=== Best Model ===")
        print(f"  Freq: {best['freq_law']}, Amp: {best['amp_law']}, Phase: {best['phase_law']}")
        print(f"  Predicted mp/me: {best['predicted_mp_me']}")
        print(f"  Observed mp/me:  {best['observed_mp_me']}")
        print(f"  Error: {best['pct_error_mp_me']}%")
        print(f"  Predicted mn/mp: {best['predicted_mn_mp']}")
        print(f"  Hierarchy correct: {best['hierarchy_correct']}")
        print(f"  Electron shells: {best['e_shells']}")
        print(f"  Proton shells:   {best['p_shells']}")

    # Model summary JSON
    summary = {
        "total_model_combinations": len(results),
        "observed_mp_me": OBSERVED_MP_ME,
        "observed_mn_mp": OBSERVED_MN_MP,
        "best_model": results[0] if results else None,
        "top_5": results[:5],
        "all_hierarchy_correct": sum(1 for r in results if r["hierarchy_correct"] == "True"),
        "assessment": "",
    }

    if results:
        best_err = float(results[0]["pct_error_mp_me"])
        if best_err < 1:
            summary["assessment"] = "Excellent: best model within 1% of observed mp/me"
        elif best_err < 10:
            summary["assessment"] = "Promising: best model within 10% of observed mp/me"
        elif best_err < 50:
            summary["assessment"] = "Structural hierarchy reproduced but quantitative fit needs work"
        else:
            summary["assessment"] = "Hierarchy may not be reproduced; model revision needed"

    json_path = os.path.join(base_dir, "model_summary.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    print(f"\n  Assessment: {summary['assessment']}")


if __name__ == "__main__":
    main()

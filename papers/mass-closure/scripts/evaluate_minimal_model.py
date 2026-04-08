#!/usr/bin/env python3
"""
Paper II — Minimal Deterministic Mass-Ratio Model (Final)
==========================================================
Evaluates the stability functional on all candidate states under
the selected energy laws. Selects stable representatives per class.

Energy convention: E ~ a^2 * phi^{k*n} * omega_n
where k is the energy-scale exponent. Higher shells carry more energy.

The structural value k = phi^2 + 3 (= phi + 4 ≈ 5.618) is tested as
the primary model, with k_opt ≈ 5.73 noted as the numerical optimum.

All computation is deterministic.
"""

import csv
import json
import math
import os

PHI = (1 + math.sqrt(5)) / 2

# Stability functional weights
ALPHA = 1.0   # closure defect
BETA = 0.5    # spectral variance
GAMMA = 0.3   # torsion penalty
DELTA = 0.0   # boundary (zero in minimal truncation)

# Energy-scale exponents
K_STRUCTURAL = PHI ** 2 + 3   # = phi + 4 ≈ 5.618 (clean phi-derived)
K_OPTIMAL = 5.73              # numerical best-fit for mp/me

ENERGY_LAWS = {
    "structural_k": lambda a, omega, n: a ** 2 * PHI ** (K_STRUCTURAL * n) * omega,
    "optimal_k": lambda a, omega, n: a ** 2 * PHI ** (K_OPTIMAL * n) * omega,
    "phi_growing_2": lambda a, omega, n: a ** 2 * PHI ** (2 * n) * omega,
}


def parse_floats(s):
    return [float(x) for x in s.split(",")]


def compute_energy(amps, freqs, shells, law_fn):
    return sum(law_fn(a, w, n) for a, w, n in zip(amps, freqs, shells))


def compute_closure_defect(amps, phases, shells):
    return sum(a**2 * PHI**(-2*n) * (2 - 2*math.cos(th))
               for a, th, n in zip(amps, phases, shells))


def compute_spectral_variance(amps, freqs, shells):
    vals = [a * PHI**n * w for a, w, n in zip(amps, freqs, shells)]
    if len(vals) < 2:
        return 0.0
    mean = sum(vals) / len(vals)
    return sum((v - mean)**2 for v in vals) / len(vals)


def compute_torsion(amps, phases, shells):
    wraw = [a**2 * PHI**(-2*n) for a, n in zip(amps, shells)]
    tw = sum(wraw)
    if tw < 1e-30:
        return 0.0
    w = [x/tw for x in wraw]
    re_s = sum(wi * math.cos(th) for wi, th in zip(w, phases))
    im_s = sum(wi * math.sin(th) for wi, th in zip(w, phases))
    return (re_s - 1)**2 + im_s**2


def compute_stability(D, V, T):
    return ALPHA*D + BETA*V + GAMMA*T


def evaluate_candidates(candidates):
    results = []
    for c in candidates:
        shells = [int(x) for x in c["shells"].split(",")]
        amps = parse_floats(c["amplitudes"])
        phases = parse_floats(c["phases"])
        freqs = parse_floats(c["frequencies"])

        D = compute_closure_defect(amps, phases, shells)
        V = compute_spectral_variance(amps, freqs, shells)
        T = compute_torsion(amps, phases, shells)
        S = compute_stability(D, V, T)

        for ename, efn in ENERGY_LAWS.items():
            E = compute_energy(amps, freqs, shells, efn)
            results.append({
                **c,
                "energy_law": ename,
                "energy": f"{E:.12e}",
                "closure_defect": f"{D:.12e}",
                "spectral_variance": f"{V:.12e}",
                "torsion_penalty": f"{T:.12e}",
                "boundary_penalty": "0.000000000000e+00",
                "stability_score": f"{S:.12e}",
            })
    return results


def select_stable(results):
    groups = {}
    for r in results:
        key = (r["symmetry"], r["freq_law"], r["amp_law"], r["phase_law"], r["energy_law"])
        S = float(r["stability_score"])
        E = float(r["energy"])
        cur = groups.get(key)
        if cur is None or S < float(cur["stability_score"]) or \
           (S == float(cur["stability_score"]) and E > float(cur["energy"])):
            groups[key] = r
    return list(groups.values())


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "artifacts")
    with open(os.path.join(base, "candidate_states.csv")) as f:
        candidates = list(csv.DictReader(f))

    print(f"Evaluating {len(candidates)} candidates x {len(ENERGY_LAWS)} energy laws...")
    results = evaluate_candidates(candidates)
    stable = select_stable(results)

    fields = list(results[0].keys())
    with open(os.path.join(base, "evaluated_states.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(results)
    with open(os.path.join(base, "stable_states.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(stable)

    print(f"Selected {len(stable)} stable representatives")
    for elaw in ENERGY_LAWS:
        print(f"\n  --- {elaw} ---")
        for sym in ["charged_lepton", "baryon", "baryon_neutral"]:
            ss = [s for s in stable if s["symmetry"] == sym and s["energy_law"] == elaw]
            if ss:
                best = min(ss, key=lambda x: float(x["stability_score"]))
                print(f"    {sym}: shells={best['shells']}, E={float(best['energy']):.4e}, S={float(best['stability_score']):.4e}")

    json.dump({
        "alpha": ALPHA, "beta": BETA, "gamma": GAMMA, "delta": DELTA,
        "phi": PHI, "k_structural": K_STRUCTURAL, "k_optimal": K_OPTIMAL,
        "energy_laws": list(ENERGY_LAWS.keys()),
        "note": "Minimal truncation. B=0. Primary model: structural_k = phi^2+3."
    }, open(os.path.join(base, "model_parameters.json"), "w"), indent=2)


if __name__ == "__main__":
    main()

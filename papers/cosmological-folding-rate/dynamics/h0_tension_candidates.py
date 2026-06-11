"""H0-tension candidate-ratio screen.

Take the Planck (early-universe-inferred) H0 as anchor and SH0ES (local
distance-ladder) H0 as target. Enumerate candidate rate corrections
derived purely from V_600 / L_12 / cascade-fan substrate combinatorics
(no fitting, no free parameters) and score each against the data.

Published values used:
  Planck 2018 TT,TE,EE+lowE+lensing  H0 = 67.36 ± 0.54 km/s/Mpc
  SH0ES Riess+ 2022                   H0 = 73.04 ± 1.04 km/s/Mpc
  TRGB Freedman+ 2021                 H0 = 69.80 ± 1.70 km/s/Mpc

Sources:
  Planck Collaboration 2020 A&A 641, A6 (arXiv:1807.06209)
  Riess et al. 2022 ApJL 934, L7 (arXiv:2112.04510)
  Freedman 2021 ApJ 919, 16 (arXiv:2106.15656)

Candidate ratios are listed BEFORE comparing to data, then ranked by
|predicted − observed| / σ.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, List

import numpy as np

# Substrate combinatorics (immutable structural numbers, not fit parameters).
N_V600 = 120                # vertices of the 600-cell
N_BULK = 20                 # σ-fixed bulk vertices  (K=72 ∪ K=0 cycles)
N_BDRY = 100                # σ-paired boundary vertices
N_CYCLES = 12               # pentagonal-clock cycles in V_600
N_BULK_CYCLES = 2
N_BDRY_CYCLES = 10
K_TOTAL = 432               # 72 + 0 + 5*52 + 5*20
K_BULK = 72                 # 72 + 0
K_BDRY = 360                # 5*52 + 5*20
N_RUNGS = 7                 # cascade fan rungs (E8→...→0)
N_FRAMES = 8                # frame ladder
DIM_L12 = 12                # L_12 substrate dimensionality
PHI = (1.0 + math.sqrt(5.0)) / 2.0
LN_PHI = math.log(PHI)


# Published measurements --------------------------------------------------
@dataclass(frozen=True)
class Measurement:
    name: str
    value: float
    sigma: float
    note: str = ""


PLANCK = Measurement("Planck18 TT,TE,EE+lowE+lensing", 67.36, 0.54,
                    "early-universe-inferred via ΛCDM extrapolation")
SH0ES = Measurement("Riess+2022 SH0ES Cepheid+SNeIa", 73.04, 1.04,
                    "local distance ladder, z<0.15")
TRGB = Measurement("Freedman+2021 CCHP TRGB+SNeIa", 69.80, 1.70,
                    "TRGB-anchored, intermediate")
TENSION = SH0ES.value - PLANCK.value
TENSION_SIGMA = math.hypot(SH0ES.sigma, PLANCK.sigma)
TENSION_RATIO = SH0ES.value / PLANCK.value


# Candidate corrections ----------------------------------------------------
# Multiplier f such that  H_local_predicted = f · H_early_anchor.
# All come from substrate / cascade structure with NO fit parameters.
@dataclass(frozen=True)
class Candidate:
    name: str
    multiplier: float
    rationale: str


def _candidates() -> List[Candidate]:
    cands: List[Candidate] = []

    # Cycle-count corrections
    cands.append(Candidate("1 + 1/N_cycles",          1 + 1/N_CYCLES,
                           "1/12: extra mode from 12-cycle pentagonal clock"))
    cands.append(Candidate("1 + 1/(N_cycles-1)",      1 + 1/(N_CYCLES-1),
                           "1/11: cycles minus one σ-fixed anchor"))
    cands.append(Candidate("(N_cycles+1)/N_cycles",   (N_CYCLES+1)/N_CYCLES,
                           "13/12 — same number, different rationale (cycles+anchor)"))

    # Bulk/boundary vertex ratios
    cands.append(Candidate("|B|/|V|",                 1 + N_BULK/N_V600,
                           "20/120 = 1/6: bulk vertex fraction"))
    cands.append(Candidate("|B|/|∂|",                 1 + N_BULK/N_BDRY,
                           "20/100 = 1/5"))
    cands.append(Candidate("|∂|/(|V|·something)",     1 + N_BDRY/(N_V600*N_CYCLES),
                           "100/(120·12) — boundary normalised by cycles"))

    # K-spectral weights
    cands.append(Candidate("1 + K_bulk/K_total",      1 + K_BULK/K_TOTAL,
                           "72/432 = 1/6: bulk K-weight share"))
    cands.append(Candidate("1 + (K_bdry-K_bulk)/(N_V600·something)",
                           1 + (K_BDRY-K_BULK)/(N_V600*N_RUNGS),
                           "K-weight contrast / 120·7"))

    # L_12 / dimensional
    cands.append(Candidate("1 + 1/D_L12",             1 + 1/DIM_L12,
                           "1/12: L_12 dimensional inverse — same number as cycles"))
    cands.append(Candidate("1 + 1/(D_L12·N_rungs)·N_cycles",
                           1 + N_CYCLES/(DIM_L12*N_RUNGS),
                           "12/(12·7): cycle count over cascade·dim"))

    # Cascade fan
    cands.append(Candidate("1 + 1/N_rungs",           1 + 1/N_RUNGS,
                           "1/7: cascade-fan rung inverse"))
    cands.append(Candidate("1 + 1/N_frames",          1 + 1/N_FRAMES,
                           "1/8: frame-ladder inverse"))

    # φ-based
    cands.append(Candidate("φ^(1/N_cycles)",          PHI**(1/N_CYCLES),
                           "φ^(1/12): φ-cascade root"))
    cands.append(Candidate("1 + ln(φ)/(2π)",          1 + LN_PHI/(2*math.pi),
                           "log-period / cycle"))
    cands.append(Candidate("1 + ln(φ)/N_rungs",       1 + LN_PHI/N_RUNGS,
                           "log-period / rungs"))
    cands.append(Candidate("1 + 1/(2φ²)",             1 + 1/(2*PHI**2),
                           "1/(2φ²) ≈ 0.191"))

    # Null candidates (expected to FAIL — sanity)
    cands.append(Candidate("1 + 1/π",                 1 + 1/math.pi,
                           "[null] π is not in substrate algebra"))
    cands.append(Candidate("1 + 1/e",                 1 + 1/math.e,
                           "[null] e is not in substrate algebra"))
    cands.append(Candidate("ratio_random_0.05",       1.05,
                           "[null] arbitrary 5% offset"))
    cands.append(Candidate("ratio_random_0.10",       1.10,
                           "[null] arbitrary 10% offset"))

    # Identity (ΛCDM null)
    cands.append(Candidate("1.0",                     1.0,
                           "[null] no correction — pure ΛCDM"))

    return cands


def score(c: Candidate, anchor: Measurement, target: Measurement) -> dict:
    predicted = c.multiplier * anchor.value
    sigma_pred = c.multiplier * anchor.sigma  # propagate anchor uncertainty
    delta = predicted - target.value
    sigma_total = math.hypot(sigma_pred, target.sigma)
    z = delta / sigma_total
    return {
        "candidate": c.name,
        "rationale": c.rationale,
        "multiplier": c.multiplier,
        "predicted": predicted,
        "anchor": anchor.value,
        "target": target.value,
        "delta": delta,
        "z_score": z,
        "abs_z": abs(z),
    }


def main() -> None:
    print("=" * 70)
    print("H0 tension candidate-ratio screen")
    print("=" * 70)
    print(f"  Planck18:  H0 = {PLANCK.value} ± {PLANCK.sigma}")
    print(f"  SH0ES22:   H0 = {SH0ES.value} ± {SH0ES.sigma}")
    print(f"  TRGB21:    H0 = {TRGB.value} ± {TRGB.sigma}")
    print(f"  Tension:   {TENSION:+.2f} ± {TENSION_SIGMA:.2f} km/s/Mpc"
          f"  ({TENSION/TENSION_SIGMA:.1f}σ)")
    print(f"  Ratio SH0ES/Planck:  {TENSION_RATIO:.5f}")
    print()

    cands = _candidates()
    rows = [score(c, PLANCK, SH0ES) for c in cands]
    rows.sort(key=lambda r: r["abs_z"])

    print(f"{'#':>2}  {'candidate':<42} {'pred':>7} {'Δ':>7} {'|z|':>5}  rationale")
    print("-" * 110)
    for i, r in enumerate(rows, 1):
        print(
            f"{i:>2}  {r['candidate']:<42} "
            f"{r['predicted']:>7.2f} {r['delta']:>+7.2f} {r['abs_z']:>5.2f}  "
            f"{r['rationale']}"
        )

    print()
    print("Best candidate (closest to SH0ES under Planck anchor):")
    best = rows[0]
    print(f"  {best['candidate']}  →  predicted H0_local = {best['predicted']:.2f} km/s/Mpc")
    print(f"  observed SH0ES H0      = {SH0ES.value:.2f} ± {SH0ES.sigma}")
    print(f"  |z| against SH0ES      = {best['abs_z']:.2f}")
    print(f"  rationale: {best['rationale']}")

    # Export
    import csv
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "h0_tension_candidates.csv")
    with open(out, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nFull table → {out}")


if __name__ == "__main__":
    main()

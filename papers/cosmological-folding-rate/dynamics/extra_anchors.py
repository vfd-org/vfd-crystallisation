"""Pre-registered tests of the 1/12 prediction against additional anchors.

Anchors tested:
  (a) DESI 2024 BAO H₀ — should land near Planck (no local boundary coupling).
  (b) Cosmic dipole anomaly — radio + quasar dipoles vs CMB dipole.
  (c) JWST-recalibrated SH0ES (Riess+2024) — should still land at +1/12.

Each test was specified BEFORE looking at the data:
  - BAO: predict H_BAO ≈ H_early = 67.36 (no boundary contribution).
  - Dipole: predict ratio = 1 + 1/12 = 1.083.
  - JWST: predict same +1/12 as Cepheid SH0ES.

Sources used:
  DESI 2024 VI       arXiv:2404.03002 (DESI Collaboration; H_0 = 67.97 ± 0.38 with CMB)
  DESI Newest        arXiv:2412.13045 (Hu+ data-driven; H_0 = 68.4 +1.0/-0.8)
  Quasar dipole      Secrest+2021 ApJL 908, L51 (arXiv:2009.14826) — 4.9σ excess
  Quaia dipole       Mittal+2024 (~5σ; 1700 km/s vs CMB 370 km/s)
  Radio dipole       Singal 2023 / Wagenveld+2023 (3× CMB amplitude)
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List

# Locked prediction from derivation
EPS = 1.0 / 12.0  # = 1/12, derived in derivation.md

# Anchor for early-universe rate
PLANCK_H0, PLANCK_H0_S = 67.36, 0.54


@dataclass(frozen=True)
class AnchorTest:
    name: str
    observable: float
    sigma: float
    predicted: float
    rationale: str
    note: str = ""


def score(t: AnchorTest) -> dict:
    delta = t.predicted - t.observable
    z = abs(delta) / t.sigma
    return {"name": t.name, "predicted": t.predicted, "observed": t.observable,
            "sigma": t.sigma, "delta": delta, "abs_z": z}


def main() -> None:
    tests: List[AnchorTest] = []

    # (a) BAO — H_BAO should land near H_early because BAO does not couple
    #     to per-galaxy boundary fluctuations.
    bao_pred = PLANCK_H0  # = H_early; +0/12 boundary content
    tests.append(AnchorTest(
        "DESI 2024 BAO+CMB",   67.97, 0.38,
        bao_pred,
        "BAO uses sound horizon — no local boundary; expect H_early = 67.36.",
        "consistency, not headline test (BAO is anchored on Planck)",
    ))
    tests.append(AnchorTest(
        "DESI 2024 data-driven", 68.4, 0.9,
        bao_pred,
        "Data-driven (no sound-horizon calibration); same prediction.",
        "weakly Planck-anchored, more independent",
    ))

    # (b) Cosmic dipole anomaly — predicted excess = 1 + 1/12 = 1.0833.
    #     CMB dipole velocity = 370 km/s.
    cmb_dipole_v = 370.0
    cmb_dipole_v_sigma = 0.5  # very precise
    dipole_pred_v = cmb_dipole_v * (1 + EPS)
    tests.append(AnchorTest(
        "Quasar (Quaia) dipole velocity", 1700.0, 100.0,
        dipole_pred_v,
        "Predicted excess = +1/12 ≈ 8%.  Observed excess = 360%.",
        "CRITICAL FAIL: predicted ~401, observed ~1700.",
    ))
    radio_dipole_amp_ratio = 3.0
    radio_dipole_amp_ratio_sigma = 0.5
    tests.append(AnchorTest(
        "Radio dipole amplitude ratio", radio_dipole_amp_ratio, radio_dipole_amp_ratio_sigma,
        1.0 + EPS,
        "Predicted ratio = 1.083.  Observed ratio = 3.0.",
        "FAIL: 1/12 too small to explain dipole anomaly.",
    ))

    # (c) JWST recalibration of SH0ES.  Riess+2024 confirms H_0 ≈ 73.
    sh0es_jwst = 72.6  # Riess+2024 JWST redo, rounded
    sh0es_jwst_s = 1.04
    tests.append(AnchorTest(
        "JWST-Cepheid SH0ES (Riess+2024)", sh0es_jwst, sh0es_jwst_s,
        PLANCK_H0 * (1 + EPS),
        "Same +1/12 prediction as Cepheid SH0ES.",
        "consistency check on the H₀ anchor.",
    ))

    print("=" * 80)
    print(f"Pre-registered tests of locked prediction: ε = 1/12 = {EPS:.5f}")
    print(f"H_early anchor: Planck = {PLANCK_H0} ± {PLANCK_H0_S}")
    print("=" * 80)
    print()
    for t in tests:
        r = score(t)
        verdict = "PASS" if r["abs_z"] < 1.0 else ("MARGINAL" if r["abs_z"] < 2.0 else "FAIL")
        print(f"[{verdict:<8}] {t.name}")
        print(f"           predicted = {r['predicted']:.3f}, observed = {r['observed']:.3f} ± {r['sigma']:.3f}")
        print(f"           |z| = {r['abs_z']:.2f}")
        print(f"           rationale: {t.rationale}")
        if t.note:
            print(f"           note: {t.note}")
        print()


if __name__ == "__main__":
    main()

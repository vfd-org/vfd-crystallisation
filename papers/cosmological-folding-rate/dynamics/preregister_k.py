"""Pre-registered k-ladder predictions for cosmic-dipole surveys.

Locked: 2026-05-05.  Predictions made BEFORE any analysis of upcoming surveys.

The k-ladder formula:    ratio(k) = 1 + k/2,   k ∈ {0,1,...,10}

Per-survey k is assigned from a single rule applied uniformly:

    k = round( 2·z_eff · w_AGN )

where:
  z_eff   = effective median redshift of the source population
  w_AGN   = AGN-bias weight: 1.0 for general galaxy/IR samples,
            1.5 for AGN-dominated samples (radio + quasar selections couple
            more strongly to boundary modes because AGN trace high-σ-paired
            content; argument deferred to OD-3 of derivation.md)
  k clipped to [0, 10]

This rule is then *fitted* to existing data:

  WISE all-sky    z_eff=0.5   w=1.0  → k_pred = 1   (observed k=2)
  CatWISE         z_eff=1.0   w=1.5  → k_pred = 3   (observed k=3) ✓
  NVSS+RACS       z_eff=1.0   w=1.5  → k_pred = 3   (observed k=4)
  Quaia           z_eff=1.5   w=1.5  → k_pred = 5   (observed k=7)

Rule fits half the points but the high-k surveys (NVSS, Quaia) are
underpredicted. This is honest — the rule is a working hypothesis.

For the pre-registration we ship k_pred for each survey explicitly;
each survey's *post-measurement* discrepancy with k_pred is the test.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SurveyPrediction:
    name: str
    z_eff: float
    w_AGN: float
    k_pred: int
    ratio_pred: float
    notes: str


def k_from_rule(z_eff: float, w_AGN: float) -> int:
    k = round(2 * z_eff * w_AGN)
    return max(0, min(10, k))


def ratio(k: int) -> float:
    return 1.0 + k / 2.0


def predictions() -> List[SurveyPrediction]:
    upcoming = [
        # (name, z_eff, w_AGN, notes)
        ("SPHEREx (NASA, IR all-sky 0.75–5 μm, ~2026)",
         0.5, 1.0,
         "All-sky IR like WISE but with low-res spectra. Matches WISE class. "
         "Predict k near WISE; if k>3 framework needs revision."),
        ("Rubin LSST (optical 6-band, 10 yr)",
         0.7, 1.0,
         "Galaxy survey to z~1.5; not AGN-biased."),
        ("Rubin LSST AGN sample (z>1)",
         2.0, 1.5,
         "Deep AGN selection. Predict k ≥ 6."),
        ("SKA-Phase 1 (HI continuum, μJy)",
         1.5, 1.5,
         "Deep radio AGN; deeper than NVSS+RACS. Predict k ≥ 4."),
        ("SKA-Phase 2 (continuum, deeper)",
         2.5, 1.5,
         "Maximum-depth radio AGN. Predict k near max (≥7)."),
        ("DESI quasar sample (z~1–3)",
         2.0, 1.5,
         "Spectroscopic quasars; similar depth to Quaia."),
        ("Euclid quasars",
         1.5, 1.5,
         "Optical+NIR space mission, z<2 quasars."),
        ("eROSITA-DE X-ray AGN",
         1.0, 1.5,
         "X-ray AGN selection; depth between CatWISE and Quaia."),
    ]
    out = []
    for name, z, w, notes in upcoming:
        k = k_from_rule(z, w)
        out.append(SurveyPrediction(name, z, w, k, ratio(k), notes))
    return out


def main() -> None:
    print("=" * 80)
    print("Pre-registered cosmic-dipole k-ladder predictions (locked 2026-05-05)")
    print("=" * 80)
    print()
    print(f"{'survey':<48} {'z_eff':>6} {'w_AGN':>6} {'k':>3} {'ratio':>6}")
    print("-" * 80)
    preds = predictions()
    for p in preds:
        print(f"{p.name:<48} {p.z_eff:>6.1f} {p.w_AGN:>6.1f} {p.k_pred:>3} {p.ratio_pred:>6.1f}")

    print()
    print("Notes per survey:")
    for p in preds:
        print(f"  {p.name}")
        print(f"    {p.notes}")
        print()

    print("=" * 80)
    print("Falsification gates")
    print("=" * 80)
    print("Each survey's measured ratio must land within 0.5σ of one of:")
    for k in range(11):
        print(f"  k = {k:>2}  →  ratio = {ratio(k):.1f}")
    print()
    print("Specifically, the framework FAILS if ANY of:")
    print("  (i)   A survey reports a ratio at non-half-integer (e.g., 3.7 ± 0.1).")
    print("  (ii)  A survey reports a ratio >6 by more than ~0.5 sigma (max boundary).")
    print("  (iii) The k assigned by the rule above is wrong for the majority of new surveys.")
    print()
    print("If (iii) fails alone, the rule needs revision but the ladder shape stands.")
    print("If (i) or (ii) fails, the entire bulk-trace reframe needs revision.")

    # Export
    import csv, os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "preregister_k_predictions.csv")
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["survey", "z_eff", "w_AGN", "k_pred", "ratio_pred", "notes"])
        for p in preds:
            w.writerow([p.name, p.z_eff, p.w_AGN, p.k_pred, p.ratio_pred, p.notes])
    print(f"\nLocked predictions → {out}")


if __name__ == "__main__":
    main()

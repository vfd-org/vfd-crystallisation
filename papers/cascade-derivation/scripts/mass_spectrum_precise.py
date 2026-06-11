#!/usr/bin/env python3
"""
Precise cascade mass spectrum: integer shell depths to high precision.

Uses high-precision Planck mass and PDG 2024 fermion masses.
"""

from mpmath import mp, mpf, log, sqrt, power

mp.dps = 30  # 30 decimal digits


PHI = (1 + sqrt(5)) / 2
LOG_PHI = log(PHI)
M_P_GeV = mpf("1.22089e19")   # reduced Planck scale (non-reduced convention)


# PDG 2024 fermion masses (GeV), most-precise values
FERMIONS = [
    ("electron",  mpf("5.1099895e-4")),
    ("muon",      mpf("0.10565837")),
    ("tau",       mpf("1.77686")),
    ("up",        mpf("2.16e-3")),
    ("down",      mpf("4.67e-3")),
    ("strange",   mpf("9.34e-2")),
    ("charm",     mpf("1.273")),
    ("bottom",    mpf("4.18")),
    ("top",       mpf("172.76")),
    ("proton",    mpf("0.9382720813")),
    ("neutron",   mpf("0.9395654205")),
    ("W",         mpf("80.377")),
    ("Z",         mpf("91.1876")),
    ("Higgs",     mpf("125.25")),
]


def N_shell(m):
    return log(M_P_GeV/m)/LOG_PHI


def predicted_mass(N):
    return M_P_GeV * power(PHI, -N)


def main():
    print("=" * 72)
    print("PRECISE MASS SPECTRUM — shell depths and integer fits")
    print("=" * 72)
    print()
    print(f"  {'Particle':<12}  {'m [GeV]':>14}  {'N_shell':>14}  "
          f"{'N_int':>5}  {'frac':>9}")
    print(f"  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*5}  {'-'*9}")
    for name, m in FERMIONS:
        N = N_shell(m)
        N_int = int(mp.nint(N))
        frac = N - N_int
        mark = ""
        if abs(frac) < 0.1:
            mark = "  ⭐ INTEGER"
        elif abs(frac) < 0.2:
            mark = "  ✓ near"
        print(f"  {name:<12}  {float(m):>14.7e}  {float(N):>14.6f}  "
              f"{N_int:>5}  {float(frac):>+9.6f}{mark}")
    print()

    # High-precision muon check
    print("-" * 72)
    print("MUON AT SHELL 96 — high precision check")
    print("-" * 72)
    muon_mass = mpf("0.10565837")
    N_muon = N_shell(muon_mass)
    m_pred = predicted_mass(96)
    print(f"  Observed muon mass:    {float(muon_mass):.10e} GeV")
    print(f"  Cascade shell 96:      m_P · φ^(-96) = {float(m_pred):.10e} GeV")
    ratio = muon_mass/m_pred
    gap = (muon_mass - m_pred)/m_pred * 100
    print(f"  Ratio obs/pred:        {float(ratio):.6f}")
    print(f"  Gap:                   {float(gap):+.4f}%")
    print()

    # Electron
    print("-" * 72)
    print("ELECTRON AT SHELL 107 — check")
    print("-" * 72)
    e_mass = mpf("5.1099895e-4")
    m_pred_107 = predicted_mass(107)
    m_pred_108 = predicted_mass(108)
    print(f"  Observed electron:     {float(e_mass):.10e} GeV")
    print(f"  Cascade shell 107:     {float(m_pred_107):.10e} GeV  ratio {float(e_mass/m_pred_107):.3f}")
    print(f"  Cascade shell 108:     {float(m_pred_108):.10e} GeV  ratio {float(e_mass/m_pred_108):.3f}")
    print(f"  Neither is exact; electron at shell 107.08 (non-integer).")
    print()

    # Ratios between generations (cascade structural?)
    print("-" * 72)
    print("GENERATION SHELL-GAPS — testing cascade integer structure")
    print("-" * 72)
    print()
    particles = {name: N_shell(m) for name, m in FERMIONS}
    gaps = [
        ("μ/e shell gap",   particles["electron"] - particles["muon"],   "11"),
        ("τ/μ shell gap",   particles["muon"] - particles["tau"],         "6"),
        ("τ/e shell gap",   particles["electron"] - particles["tau"],     "17"),
        ("c/u shell gap",   particles["up"] - particles["charm"],         "13"),
        ("t/c shell gap",   particles["charm"] - particles["top"],        "10"),
        ("s/d shell gap",   particles["down"] - particles["strange"],     "6"),
        ("b/s shell gap",   particles["strange"] - particles["bottom"],   "8"),
        ("p/e shell gap",   particles["electron"] - particles["proton"],  "16"),
    ]
    for name, gap, candidate in gaps:
        print(f"  {name:<25}  actual gap = {float(gap):>7.3f}  "
              f"vs integer {candidate} (diff {float(gap) - int(candidate):+.3f})")
    print()

    # Boson shell-depth check
    print("-" * 72)
    print("BOSONS — shell depths of W, Z, Higgs")
    print("-" * 72)
    for name, m in [(p[0], p[1]) for p in FERMIONS if p[0] in ["W", "Z", "Higgs"]]:
        N = N_shell(m)
        print(f"  {name:<10}  m = {float(m):>8.3f} GeV   N = {float(N):.3f}")
    # electroweak scale
    ew_scale = mpf("246")  # Higgs VEV
    N_ew = N_shell(ew_scale)
    print(f"  Higgs VEV (246 GeV)   N = {float(N_ew):.3f}")
    print()

    # Ratio W/Z relates to sin²θ_W = 3/8 at GUT
    print("  W/Z mass ratio check:")
    W = mpf("80.377"); Z = mpf("91.1876")
    cos_sq_W = (W/Z)**2
    sin_sq_W = 1 - cos_sq_W
    print(f"    cos²θ_W = (M_W/M_Z)² = {float(cos_sq_W):.4f}")
    print(f"    sin²θ_W_obs(EW)      = {float(sin_sq_W):.4f}")
    print(f"    sin²θ_W_cascade(GUT) = 0.375 (= 3/8)")
    print(f"    Note: GUT value runs to ~0.231 at EW scale (standard RG).")
    print()


if __name__ == "__main__":
    main()

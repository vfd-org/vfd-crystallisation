#!/usr/bin/env python3
"""
Cascade mass spectrum scan — shell depths of SM fermions.

For each particle: N = log_φ(m_P / m).
Look for cascade-structural integers and ratios.
"""

import numpy as np
from math import log, sqrt

PHI = (1 + sqrt(5)) / 2
LOG_PHI = log(PHI)
M_P_GeV = 1.22089e19


FERMIONS = [
    # (name, mass GeV, type)
    ("electron",       5.109989e-4,   "lepton",   1),
    ("muon",           0.1056584,     "lepton",   2),
    ("tau",            1.77686,       "lepton",   3),
    ("up",             2.16e-3,       "quark",    1),
    ("down",           4.67e-3,       "quark",    1),
    ("strange",        93.4e-3,       "quark",    2),
    ("charm",          1.273,         "quark",    2),
    ("bottom",         4.18,          "quark",    3),
    ("top",            172.76,        "quark",    3),
    # neutrino upper bounds
    ("neutrino (upper)", 1e-9,        "lepton",   1),
]


def shell_depth(m):
    return log(M_P_GeV / m) / LOG_PHI


def main():
    print("=" * 72)
    print("CASCADE MASS SPECTRUM — shell depths N = log_φ(m_P/m)")
    print("=" * 72)
    print()
    print(f"  Planck mass m_P = {M_P_GeV:.5e} GeV")
    print()
    print(f"  {'Fermion':<20}  {'m [GeV]':>12}  {'N = log_φ':>10}  {'gen':>4}  {'type':<8}")
    print(f"  {'-'*20}  {'-'*12}  {'-'*10}  {'-'*4}  {'-'*8}")
    data = []
    for name, m, typ, gen in FERMIONS:
        N = shell_depth(m)
        data.append((name, m, N, gen, typ))
        print(f"  {name:<20}  {m:>12.4e}  {N:>10.2f}  {gen:>4}  {typ:<8}")
    print()

    # Charged-lepton ratio analysis
    print("=" * 72)
    print("CHARGED LEPTON MASS RATIOS vs φ-POWERS")
    print("=" * 72)
    print()
    e = 5.109989e-4
    mu = 0.1056584
    tau = 1.77686
    r_mu_e = mu / e
    r_tau_mu = tau / mu
    r_tau_e = tau / e
    print(f"  m_μ / m_e   =  {r_mu_e:.3f}")
    print(f"  m_τ / m_μ   =  {r_tau_mu:.3f}")
    print(f"  m_τ / m_e   =  {r_tau_e:.3f}")
    print()
    print(f"  Shell-depth gaps:")
    print(f"    e → μ  :  ΔN = {shell_depth(e) - shell_depth(mu):+.3f}")
    print(f"    μ → τ  :  ΔN = {shell_depth(mu) - shell_depth(tau):+.3f}")
    print(f"    e → τ  :  ΔN = {shell_depth(e) - shell_depth(tau):+.3f}")
    print()
    print(f"  φ-power candidates for these gaps:")
    for gap_name, gap in [("μ/e", shell_depth(e) - shell_depth(mu)),
                           ("τ/μ", shell_depth(mu) - shell_depth(tau)),
                           ("τ/e", shell_depth(e) - shell_depth(tau))]:
        n = round(gap)
        pred = PHI**n
        actual = PHI**gap
        err = (pred - actual) / actual * 100
        print(f"    {gap_name}  gap ≈ φ^{n}:  φ^{n} = {pred:.3f}  "
              f"(actual φ^{gap:.2f} = {actual:.3f})  gap from integer: {err:+.1f}%")
    print()

    # Quark masses
    print("=" * 72)
    print("QUARK MASS RATIOS")
    print("=" * 72)
    print()
    quarks = [(n, m, g) for n, m, t, g in FERMIONS if t == "quark"]
    for n, m, g in quarks:
        print(f"  {n:<12}  m = {m:>10.4e} GeV   N_shell = {shell_depth(m):.2f}   gen {g}")
    print()

    # Generation structure
    print(f"  Generation structure (shell depth averages):")
    for gen_num in [1, 2, 3]:
        in_gen = [(n, m, t) for n, m, t, g in FERMIONS if g == gen_num
                   and t != "lepton" or "neutrino" not in n]
        leptons = [m for n, m, t, g in FERMIONS if g == gen_num and t == "lepton"
                    and "neutrino" not in n]
        quarks_g = [m for n, m, t, g in FERMIONS if g == gen_num and t == "quark"]
        if leptons:
            avg_lep_N = np.mean([shell_depth(m) for m in leptons])
            print(f"    Gen {gen_num} charged lepton shell depth:  {avg_lep_N:.2f}")
        if quarks_g:
            avg_qk_N = np.mean([shell_depth(m) for m in quarks_g])
            print(f"    Gen {gen_num} quark shell depth (avg):      {avg_qk_N:.2f}")
    print()

    # Look for Fibonacci/cascade integer matches
    print("=" * 72)
    print("CASCADE INTEGER MATCHES")
    print("=" * 72)
    print()
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    cascade_ints = [2, 3, 5, 7, 8, 12, 14, 15, 16, 21, 24, 34, 40, 55, 89,
                    120, 144, 240]
    print(f"  For each fermion's shell depth N, find closest cascade integer:")
    print(f"  {'Fermion':<12}  {'N':>8}  {'nearest':>8}  {'gap':>6}")
    print(f"  {'-'*12}  {'-'*8}  {'-'*8}  {'-'*6}")
    for name, m, typ, gen in FERMIONS[:-1]:   # skip neutrino bound
        N = shell_depth(m)
        nearest = min(range(60, 130), key=lambda x: abs(x - N))
        gap = N - nearest
        print(f"  {name:<12}  {N:>8.2f}  {nearest:>8}  {gap:>+6.2f}")
    print()

    # Proton mass check (known cascade result: r_p = 4 λ̄_p, but also mass?)
    print("=" * 72)
    print("PROTON MASS (cascade cross-check)")
    print("=" * 72)
    print()
    m_proton = 0.9382721  # GeV
    N_proton = shell_depth(m_proton)
    print(f"  m_proton = {m_proton} GeV")
    print(f"  Shell depth = {N_proton:.3f}")
    # VFD master math claim: m_P × φ^(-k*8); try k=11.5
    print(f"  VFD master math claim: m ∝ m_P × φ^(-k·8) with k ≈ {N_proton/8:.2f}")
    print(f"    (non-integer k — ansatz doesn't fit cleanly)")
    print()
    # Cascade reading: m_proton = 4λ̄_p from proton-radius WO
    # Note: r_p and m_p are related by Compton λ̄_p = ℏ/(m_p c)
    # So m_p = ℏc/λ̄_p, and r_p = 4 λ̄_p gives r_p × m_p × c / ℏ = 4
    # which is the dimensionless cascade factor.
    hbar_c_fm_GeV = 0.1973
    r_p_fm = 0.8414   # experimental proton charge radius
    lambda_bar = hbar_c_fm_GeV / m_proton
    print(f"  λ̄_p = ℏ/(m_p c) = {lambda_bar:.4f} fm")
    print(f"  r_p (observed) = {r_p_fm} fm")
    print(f"  r_p / λ̄_p = {r_p_fm/lambda_bar:.3f}  (cascade predicts 4)")
    print(f"  Gap: {(r_p_fm/lambda_bar - 4)/4*100:+.2f}%")
    print()


if __name__ == "__main__":
    main()

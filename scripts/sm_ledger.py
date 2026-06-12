#!/usr/bin/env python3
"""
sm_ledger.py — the Standard-Model ledger simulator.

Models everything the VFD framework currently determines about the
Standard Model, with HONESTY GRADES, and is precise about both the
predictions and their current errors. This is deliberately not a fit:
nothing here has an adjustable parameter. Grades:

  STRUCTURAL   derived from the framework's verified structure
               (sims cited; see verify_sm_structure.py, verify_residual_closure.py)
  CONDITIONAL  derived under one named open hypothesis
  PLACED       the framework assigns a slot whose integer/offset is
               read from data, not derived (postdiction, recorded)
  CONJECTURE   a named candidate mechanism, untested
  OPEN         not derived; no candidate mechanism in hand

Anchor mode (default): the muon mass plus the structural shell
N_mu = 96 = 24 x 4 (Paper LII; Hypothesis H-shell-96) fix the Planck
mass; every other particle's mass at ITS integer shell is then a
parameter-free number m = m_mu * phi^(96 - N). The deviation column is
the framework's current, honest error at each slot.

Usage:
    python scripts/sm_ledger.py
"""
from __future__ import annotations

import numpy as np

PHI = (1 + np.sqrt(5)) / 2
LN_PHI = np.log(PHI)

# PDG 2024 central values (GeV); shell integers from
# papers/cascade-derivation/cascade-masses.md §E3.1
PARTICLES = [
    # name, PDG mass GeV, shell N, grade of the shell assignment
    ("electron", 5.1099895e-4, 107, "PLACED"),
    ("muon",     0.1056583755,  96, "CONDITIONAL (H-shell-96; ppm offset; Paper LII prior)"),
    ("tau",      1.77686,       90, "PLACED"),
    ("up",       2.16e-3,      104, "PLACED"),
    ("down",     4.67e-3,      102, "PLACED (worst offset +0.48)"),
    ("strange",  0.0934,        96, "PLACED"),
    ("charm",    1.273,         91, "PLACED"),
    ("bottom",   4.18,          88, "PLACED"),
    ("top",      172.76,        81, "PLACED"),
    ("proton",   0.93827209,    91, "PLACED (offset +0.46)"),
    ("W",        80.377,        82, "PLACED"),
    ("Z",        91.1876,       82, "PLACED (offset -0.049)"),
    ("Higgs",    125.25,        81, "PLACED"),
]

M_MU = 0.1056583755
N_MU = 96


def mass_table():
    print("=" * 78)
    print("MASS SECTOR — anchor: m_mu + H-shell-96  =>  m_P = m_mu phi^96 "
          f"= {M_MU * PHI**96:.4e} GeV")
    print("every entry below is then the parameter-free number "
          "m = m_mu phi^(96 - N)")
    print("=" * 78)
    print(f"{'particle':<10} {'shell':>5} {'m_pred [GeV]':>14} "
          f"{'m_PDG [GeV]':>14} {'dev':>8}  grade")
    print("-" * 78)
    for name, m_pdg, N, grade in PARTICLES:
        m_pred = M_MU * PHI ** (N_MU - N)
        dev = m_pred / m_pdg - 1
        print(f"{name:<10} {N:>5} {m_pred:>14.6g} {m_pdg:>14.6g} "
              f"{dev:>+8.1%}  {grade}")
    print("-" * 78)
    print("Reading: the LADDER is the framework's (one golden-ratio step per")
    print("shell); the INTEGERS are currently read from data except the muon's")
    print("(structural claim, Paper LII); the OFFSETS (up to half a shell, i.e.")
    print("up to ~25% in mass) are the open dynamical content - the framework's")
    print("analogue of radiative corrections. Deriving integers + offsets is")
    print("the named open item; nothing here is fitted.")
    print()
    print("Not placed at all: NEUTRINO MASSES - OPEN.")
    print()


def charge_table():
    print("=" * 78)
    print("CHARGE / QUANTUM-NUMBER SECTOR — STRUCTURAL "
          "(verify_sm_structure.py, 11/11)")
    print("=" * 78)
    rows = [
        ("electric charge lattice", "quantized in 1/3 units: Q = N/3, "
         "N the octonion number operator", "STRUCTURAL (Q1-Q2)"),
        ("multiplet pattern", "{1, 3, 3, 1} = (nu, d-type, u-type, e-type); "
         "3-dim spaces are su(3) triplets", "STRUCTURAL (Q2-Q3)"),
        ("colour group", "su(3) = clock-unit stabiliser in Der(O)",
         "STRUCTURAL (Paper LVI, SM1-SM4)"),
        ("weak group", "internal SU(2) = left quaternion factor",
         "STRUCTURAL (Paper LVI, A2/T14)"),
        ("chirality", "the internal SU(2) is the LEFT Spin(4) factor and "
         "acts C-linearly on one Weyl module only; the spatial (right) "
         "factor cannot act on it", "STRUCTURAL (CH1-CH4)"),
        ("hypercharge as bookkeeping", "given doublet assignments, "
         "Y = 2(Q - T3) is fixed by the derived Q lattice",
         "STRUCTURAL arithmetic, but:"),
        ("hypercharge as INDEPENDENT gauge factor", "U(1)_Y not inside "
         "SU(2); requires the embedding/mixing", "OPEN"),
        ("Weinberg angle", "no derivation; geometric candidates "
         "scheme-dependent", "OPEN"),
        ("generations = 3", "candidate: D4-rung triality S3 permuting "
         "three 8-dim representations (cascade-gr C1)", "CONJECTURE, untested"),
        ("anomaly cancellation", "follows arithmetically IF the standard "
         "assignments are adopted; not derived from the substrate", "OPEN"),
    ]
    for a, b, c in rows:
        print(f"  {a:<38} {c}")
        print(f"      {b}")
    print()


def coupling_table():
    print("=" * 78)
    print("COUPLING / CONSTANT SECTOR")
    print("=" * 78)
    alpha_inv_pred = 137 + np.pi / 87
    alpha_inv_meas = 137.035999084
    G_pred = 1.054571817e-34 * 299792458.0 / (1.883531627e-28 * PHI**96) ** 2
    rows = [
        ("form of gravity (Einstein eqs)", "DERIVED-EFF (Papers LIII/LVII, 39+24 checks)", ""),
        ("form of electromagnetism (Maxwell)", "STRUCTURAL (uniqueness scan, T13)", ""),
        ("non-abelian form (Yang-Mills/Lie)", "cited theorem + machine null (YM1-YM2)", ""),
        ("G (Newton)", f"CONDITIONAL anchor: {G_pred:.5e} vs 6.67430e-11 "
         f"({G_pred/6.6743e-11-1:+.1e})", "H-shell-96"),
        ("alpha^-1", f"CONDITIONAL chain: 137 + pi/87 = {alpha_inv_pred:.7f} vs "
         f"{alpha_inv_meas:.7f} ({alpha_inv_pred/alpha_inv_meas-1:+.1e})",
         "6-hypothesis stack (alpha-chain docs)"),
        ("g_2, g_3, running couplings", "OPEN", ""),
        ("Lambda (cosmological)", "fixed by cosmology branch "
         "(hypersphere-cosmology v1.1.0: -0.083% on Omega_Lambda)", ""),
    ]
    for a, b, c in rows:
        suffix = f"   [{c}]" if c else ""
        print(f"  {a:<38} {b}{suffix}")
    print()


def atoms_table():
    print("=" * 78)
    print("ATOMS SECTOR — standard quantum mechanics on the DERIVED equations")
    print("(Schrodinger: Paper LIII T11; Coulomb/Maxwell: LIII T13; charges:")
    print(" Paper LVIII). Inputs: alpha (CONDITIONAL chain), m_e (PLACED).")
    print("=" * 78)
    alpha = 1 / (137 + np.pi / 87)
    me_GeV = M_MU * PHI ** (96 - 107)      # electron at its integer shell
    me_meas = 5.1099895e-4
    for label, me in (("with PLACED m_e (shell 107)", me_GeV),
                      ("with measured m_e (for reference)", me_meas)):
        E1 = -0.5 * alpha**2 * me * 1e9    # eV
        a0 = 1.0 / (alpha * me)            # 1/GeV
        a0_m = a0 * 1.9733e-16             # GeV^-1 -> m
        print(f"  hydrogen ground state {label}: "
              f"E1 = {E1:8.3f} eV   (Rydberg reference -13.6057)")
        print(f"  Bohr radius            {label}: "
              f"a0 = {a0_m:.3e} m (reference 5.292e-11)")
    # first correction beyond the Coulomb model, same equations: reduced mass
    mu_red = me_meas / (1 + me_meas / 0.93827209)
    E1r = -0.5 * alpha**2 * mu_red * 1e9
    print(f"  first higher-order correction (reduced mass, same equations):")
    print(f"    E1 = {E1r:8.4f} eV vs measured ionization -13.5984 eV")
    print(f"    (residual falls 7.3 -> 0.13 meV, a factor ~55, no new input)")
    print("  Reading: once a mode has mass + charge + Schrodinger + Coulomb,")
    print("  the nonrelativistic Coulomb atom is a THEOREM of the derived")
    print("  layer; the residual error is, to leading order, the mass-input")
    print("  error (electron shell +3.9%). Reduced-mass/fine-structure are")
    print("  higher-order corrections of the same equations, not re-derived.")
    print()


def main():
    print()
    print("THE STANDARD-MODEL LEDGER — what the framework determines today,")
    print("with grades, and no adjustable parameters anywhere below.")
    print()
    charge_table()
    mass_table()
    coupling_table()
    atoms_table()
    print("=" * 78)
    print("BOTTOM LINE")
    print("=" * 78)
    print("STRUCTURAL today : gauge inventory, chirality, charge lattice,")
    print("                   multiplet pattern, force-law forms.")
    print("CONDITIONAL today: G and alpha^-1 (named hypothesis stacks).")
    print("GRADED today     : the mass ladder (muon ppm; Z 2.3%; others up to")
    print("                   ~25% at their integer shells).")
    print("OPEN, named      : independent hypercharge + Weinberg angle, shell")
    print("                   integers + offsets (= all precise masses),")
    print("                   3 generations (triality conjecture), neutrino")
    print("                   sector, anomaly assignments, running couplings.")
    print()
    print("Every STRUCTURAL line has a falsifiable verification item; run")
    print("  python3 scripts/verify_sm_structure.py   (11 checks)")
    print("  python3 scripts/verify_residual_closure.py (24 checks)")


if __name__ == "__main__":
    main()

# Papers

The VFD corpus currently spans ~33 papers. The Explorer v1 surfaces
numerical claims from the subset below; later releases will expand
coverage.

## Papers with live predictions in the registry

| Paper / WO | Predictions registered |
|---|---|
| **proton-radius WO** | `proton_charge_radius`, `proton_magnetic_radius` |
| **paper-xxxii** (hadron charge radii + form factor) | `neutron_charge_radius_squared`, `pion_charge_radius`, `kaon_charge_radius`, `deuteron_charge_radius`, `proton_magnetic_radius`, `G_E_proton_at_Q2_zero`, `G_E_proton_at_Q2_0p05`, `G_E_proton_at_Q2_0p1`, `G_E_slope_radius_consistency`, `G_E_proton_asymptote` |
| **paper-xxii** (Standard Model from 600-cell) | `alpha_inverse`, `sin2_theta_w_tree`, `integer_mode_count_94`, `upper_coxeter_sum_88`, `generation_count_z3` |
| **paper-v** (spectral-geometric mass model) | `proton_electron_mass_ratio`, `integer_mode_count_94` |
| **master-mass** (zero-parameter mass law) | `alpha_inverse`, `proton_electron_mass_ratio`, `muon_electron_mass_ratio`, `tau_electron_mass_ratio` |
| **lepton-generations (Paper F)** | `muon_electron_mass_ratio`, `tau_electron_mass_ratio`, `generation_count_z3` |
| **god-prime-084473-derivation** | `god_prime_activation_084473` |

## Not yet in the registry — see [coverage gaps](gaps.md)

See the dedicated [coverage gaps](gaps.md) page for the explicit,
audited list of claims that are **not** yet runnable, including:

- Electric charge assignments (±1, ±1/3, ±2/3) — representation-theoretic only
- Magnetic moments μ_p, μ_n, electron g-factor — lattice computed, continuum map incomplete
- Quark masses (u, d, s, c, b, t) — no derivation script yet
- W, Z, Higgs masses — no derivation script yet
- Running sin²θ_W to the Z pole — RG open problem
- Papers XXIII–XXVIII gravity numerics — analytical only

## Source

All papers are in the [`papers/` directory](https://github.com/VFD-org/vfd-crystalisation-paper/tree/main/papers)
of the repository. Each paper folder contains the LaTeX source, its
own verification scripts, and (where applicable) the derivations that
back the registered predictions.

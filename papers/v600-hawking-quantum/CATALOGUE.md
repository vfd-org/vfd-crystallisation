# Paper 2 — Math Catalogue (D/L/T/N entries)

Cross-references use stable LaTeX labels. Every entry below is
established by the certificate `verify.py` and/or the shared pytest
suite at `papers/v600-programme/tests/` (currently 39 tests).

## Definitions

- **D1.** σ-pair excitation E(v) := |v − σ(v)|²_Euclidean
  (label `def:Eobs`, §3). Exact rational value computed in Q(√5).
  *Status:* explicit in `vfd_v600.sigma.sigma_pair_energy`.

- **D2.** Coset thermodynamic content S(C), A(C), E(C), T_H(C)
  (label `def:coset_thermo`, §5).
  *Status:* definitions; values verified.

## Lemmas

- **L1.** *E(v) = 0 iff v ∈ V_24.* Label `lem:vanish` (§3).
  *Status:* Verified — `verify.py` checks all 24 fixed and 96 mobile.

- **L2.** *Coordinate identity: v − σ(v) has exactly two nonzero
  coordinates of value ±√5/2 for every σ-mobile v.*
  Label `lem:coord` (§3).
  *Status:* Verified — coordinate-by-coordinate check on all 96 mobile
  vertices.

## Theorems

- **T1.** *Hawking quantum:* spectrum is 24·δ_0 + 96·δ_{5/2}.
  Label `thm:Eq` (§4). *Status:* Verified (energy values on all 120
  vertices) and supported by symmetry orbit certificate.

- **T2.** *Discrete first law:* per coset (left or right, bulk or
  non-bulk), A=16, S=4, E=40, T_H=5/2; T_H·S = E/4. Bulk coset has
  the same incidence because |H ∩ V_24| = 4 (Paper 1). Label
  `thm:firstlaw` (§5).
  *Status:* Verified — all 6 left + all 6 right cosets exhibited;
  non-bulk aggregate also verified.

## Numerical results

- **N1.** Per-coset first-law values (printed by `verify.py`):
  for each of all 6 left + all 6 right cosets (bulk + non-bulk),
  A=16, S=4, E=40, T_H=5/2, T_H·S=10.  *Status:* Verified.

- **N2.** Aggregate boundary: A=80, S=20, E=200, T_H·S=50.
  *Status:* Verified.

- **N3.** Bilateral V_24 orbit certificate: bilateral action g·v·h with
  g, h ∈ V_24 commutes with σ (verified for all 24×24 = 576 (g,h)
  pairs scanning all 120 v) and partitions V_600 into exactly two
  orbits of sizes 24 (= V_24) and 96 (= σ-mobile sector).
  *Status:* Verified — `verify.py` and shared
  `tests/test_symmetry.py`.

## Remarks (interpretive, not theorems)

- **R1.** Bekenstein–Hawking analogy (label `rem:BH`, §5).
  Three formal relations within the finite model that echo S=A/4.
  Marked in the manuscript as interpretive; the present work does
  NOT establish the standard physical first law dE = T·dS.

- **R2.** §6 calibration discussion. Lists three open requirements
  (cascade-unit ↔ physical-unit map; semiclassical continuum
  recovery; observational model) for any quantitative observational
  claim. Marked Tier-2; no physics prediction is made in this paper.

## Verification entry points

- `papers/v600-hawking-quantum/verify.py` — primary certificate.
- `papers/v600-programme/tests/test_operator_traces.py` — energy/first-law tests.
- `papers/v600-programme/tests/test_symmetry.py` — bilateral V_24 orbit certificate.

## Out-of-scope (reserved for companion papers)

- Cascade-unit calibration to physical T_H = ℏc³/(8πGM k_B) (Tier-2).
- Semiclassical Planck-spectrum recovery from discrete gap (Tier-2).
- Quantitative PBH evaporation cutoff (Tier-2).
- Canonical involution τ_σ (Paper 3).
- Operator-trace cosmology (Paper 4).
- Unified V_600 framework (Paper 5).

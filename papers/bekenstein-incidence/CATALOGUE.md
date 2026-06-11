# Paper 1 — Math Catalogue (D/L/T/N entries)

Cross-references use **stable LaTeX labels** (e.g. `lem:basics`).
Every entry below is established by exact finite-arithmetic verification
in `verify.py` (and in the shared pytest suite at
`papers/v600-programme/tests/`, currently 35 tests).

## Definitions

- **D1.** Icosian quaternions and V_600
  (label `def:icosian`, §2). Explicit 8+16+96 vertex orbits.
  *Status:* explicit construction in `vfd_v600/icosian.build_vertices`.

- **D2.** T_τ-cycles for τ ∈ G of order 10
  (label `def:Ttau`, §3).
  *Status:* explicit in `vfd_v600/group.build_state`.

- **D3.** K-classes K(C) for cycles
  (label `def:Kclass`, §3).
  *Status:* exact rational arithmetic; verified.

- **D4.** Bulk subgroup H = (K=72) ∪ (K=0)
  (label `def:bulk`, §3).
  *Status:* explicit construction; verified.

- **D5.** Galois twist σ on icosians
  (label `def:galois`, §4). Component-wise √5 ↦ −√5.
  *Status:* foundational.

- **D6.** σ-fixed sublattice V_24
  (label `def:V24`, §4).
  *Status:* coordinate-rationality test; verified.

- **D7.** Anchor count S(C), channel count A(C)
  (label `def:SAcount`, §6).
  *Status:* definitions only.

## Lemmas

- **L1.** *|V_600| = 120, unit-norm, group closure.*
  Label `lem:basics` (§2). *Status:* Verified — `verify.py` checks all
  120 unit norms and all 14400 products.

- **L2.** *K-multiset = {72:1, 0:1, 52:5, 20:5}.*
  Label `lem:kmulti` (§3). *Status:* Verified.

- **L3.** *H ≅ Dic_5 with explicit (a, b) presentation.*
  Label `lem:h_is_dic5` (§3). *Status:* Verified — closure (400 H×H
  pairs), explicit generator pair, ⟨a,b⟩ = H by enumeration.

- **L4.** *Coset cycle composition.* Right cosets: each non-bulk Hg
  is one whole K=52 cycle plus one whole K=20 cycle. Left cosets:
  each non-bulk gH contains 2 vertices from each of the 10 non-bulk
  cycles. Label `lem:cosetkpair` (§3). *Status:* Verified — pytest
  `test_non_bulk_left_cosets_2_per_cycle` and
  `test_non_bulk_right_cosets_pair_K52_K20` distinguish the two cases;
  `verify.py` additionally certifies `g⁻¹τg ∉ H` for all g ∉ H.

- **L5.** *H is self-normalizing in G (N_G(H) = H).*
  Label `lem:nonnormal` (§3). *Status:* Verified — all 100 g ∉ H
  satisfy gH ≠ Hg.

- **L6.** *|V_24| = 24; 8 axis + 16 half-type vertices; V_24 = V_600 ∩
  σ(V_600).* Label `lem:24cell` (§4). *Status:* Verified — explicit
  24-vertex enumeration; intersection identity certified by `verify.py`.

## Theorems

- **T1.** *Coset incidence:* |gH ∩ V_24| = |Hg ∩ V_24| = 4 for all
  cosets. Label `thm:main` (§5). *Status:* Verified — 6 left + 6 right
  cosets, each with explicit 4-element σ-fixed intersection printed.

- **T2.** *τ-independence:* every order-10 τ ∈ G yields the same 4/16
  incidence, with 6 distinct H_τ all G-conjugate. Label
  `thm:taunoindep` (§5). *Status:* Verified — 24 τ-choices, |H_τ|=20,
  closure, presentation, left/right coset partitions, 4/16 on both
  sides, exactly 6 distinct H_τ, conjugacy to canonical H.

- **T3.** *S/A = 1/4 per coset and aggregate.* Label `thm:onequarter`
  (§6). *Status:* Direct corollary of T1 + T2.

## Numerical results

- **N1.** Per-coset table (Table 1 in §5).
  Reproduced exactly by `verify.py`.

- **N2.** Aggregate boundary: S = 20, A = 80, S/A = 1/4 (§6).
  *Status:* Verified.

## Verification entry points

- `papers/bekenstein-incidence/verify.py` — primary certificate
  (every `assert_log(...)` corresponds to one entry above).
- `papers/v600-programme/tests/` — shared pytest suite (35 tests).

## Out-of-scope (reserved for companion papers)

- Hawking spectrum / σ-pair excitation (Paper 2).
- Canonical involution τ_σ (Paper 3).
- Operator-trace cosmology (Paper 4).
- Unified V_600 framework (Paper 5).
- Cascade-unit calibration to physical Planck scale (Tier-2).

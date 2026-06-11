# Discrete Hawking quantum on V_600 — paper scope

**Working title:** *A monochromatic Hawking spectrum from σ-pair excitations on the binary icosahedral group.*

**One-sentence pitch:** The σ-Galois pair-excitation energy E(v) := |v − σ(v)|²_Euclidean takes a single value E_q = 5/2 across all 96 σ-mobile vertices of V_600 (the bilateral V_24 action on V_600 is transitive on the σ-mobile sector and commutes with σ), giving a discrete monochromatic finite-arithmetic spectrum that echoes the structural shape of Hawking radiation; semiclassical Planck-continuum recovery and any quantitative observational claim require future cascade-unit calibration and are not asserted in this paper.

## Why this paper, why now

Lands second in the V_600 programme. Inherits the V_600 + Dic_5 + V₂₄ setup from Paper 1 (Bekenstein 1/4) and adds *one* dynamical observable: the σ-pair excitation. The result is a clean, narrow, falsifiable claim about the deepest-discrete limit of Hawking radiation.

## What's IN scope

1. **Setup recap (cite Paper 1).** V_600 = 2I, σ-Galois twist, 24-cell as σ-fixed sublattice, Dic_5 bulk subgroup.
2. **σ-pair excitation observable.** E(v) := |v − σ(v)|²_Euclidean, computed exactly in Q(√5).
3. **Main theorem.** σ-fixed: E = 0 (no emission). σ-mobile: E = 5/2 exactly. Single delta-function spectrum.
4. **Why monochromatic.** The bilateral V_24 action Γ = {v ↦ g·v·h : g, h ∈ V_24} acts transitively on the σ-mobile sector and commutes with σ (because every g ∈ V_24 has σ(g) = g). Each generator is an isometry of the Euclidean norm on the icosian quaternion algebra, so |v − σ(v)|² is Γ-invariant; the certificate verify.py exhibits Γ explicitly via 24 left and 24 right multiplication permutations.
5. **First-law identity.** Per Dic_5-coset: E_per_coset = T_H · A, S = A/4, T_H · S = E/4. Exact arithmetic.
6. **T_H interpretation.** Cascade Hawking temperature T_H = E_q (single-line spectrum forces T = quantum gap).
7. **Semiclassical recovery sketch.** Brief argument that summing over many cosets / cascade resolutions broadens the delta into a Planck continuum.
8. **Falsifiable PBH prediction.** Primordial black holes near evaporation should exhibit a discrete spectral cutoff at the cascade gap, not a smooth thermal tail.

## What's explicitly OUT of scope

1. **Quantitative T_H ↔ ℏc³/(8πGM) calibration** (cascade-unit ↔ Planck-unit). Tier-2.
2. **Full semiclassical Planck-spectrum derivation** (only sketched, not computed).
3. **All cosmology** (H_0, σ_8, CMB).
4. **τ_σ involution.** Paper 3 territory; not needed here.
5. **Theory of QG.** No claim of one.
6. **PBH abundance constraints.** Beyond scope; cite if relevant.

## Section structure (target ~10 pages)

1. **Introduction** (1pp). Hawking radiation, the discreteness question, what this paper does.
2. **V_600 and the σ-Galois twist** (1.5pp). Recap from Paper 1.
3. **The σ-pair excitation** (1.5pp). Definition + W(H₄)-invariance argument.
4. **Main theorem and proof** (2pp). E_q = 5/2 across all 96 σ-mobile vertices. Computational verification appended.
5. **First-law structure** (1.5pp). T_H · S = E/4 exact per coset.
6. **Semiclassical recovery** (1pp). Heuristic sketch of how Planck continuum emerges.
7. **PBH prediction and scope** (1pp). Falsifiable cutoff. What is and isn't claimed.
8. **Conclusion** (0.5pp).
9. **Appendix.** Verification script (`hawking_radiation_derivation.py`).

## The undismissable spine

> We define the σ-Galois pair-excitation E(v) := |v − σ(v)|²_Euclidean on the binary icosahedral group V_600 ⊂ Sp(1) ⊗ ℚ(√5), where σ acts by √5 ↦ −√5 on the icosian quaternion components. We prove that E(v) = 0 for the 24 σ-fixed vertices (the 24-cell sublattice) and E(v) = 5/2 exactly for the remaining 96 σ-mobile vertices. The numerical value follows from a direct coordinate computation; constancy of E on the σ-mobile sector additionally follows from the transitive bilateral V_24 action g·v·h, which commutes with σ and forms a subgroup of W(H₄). Interpreted as a Hawking-pair excitation channel, this gives a monochromatic finite-arithmetic spectrum whose per-coset identity T_H · S = E/4 holds exactly for every non-bulk Dic_5-coset.

The reviewer sees: finite-group fact, named symmetry argument, exact identity. No theory of quantum gravity is being claimed.

## Risk register

| Hook | Mitigation |
|---|---|
| "A single delta function isn't Hawking radiation." | §6 sketches semiclassical recovery; §7 frames result as the deepest-discrete limit, not the full Hawking spectrum. |
| "Why interpret σ-pair as Hawking?" | §3 motivates: σ takes V_600 to σ(V_600), giving a "twin-universe" exit channel — direct analog of Hawking pair production at the horizon. State as definition with motivation. |
| "PBH cutoff prediction lacks numerical anchor." | §7 acknowledges; flags as Tier-2 quantitative work. The *qualitative* cutoff (discrete vs continuous) is testable. |
| "Why W(H₄) symmetry matters." | §3 explains: V_600 is the W(H₄)-orbit of (1,0,0,0); σ-mobile vertices form one orbit under W(H₄) intersected with the σ-mobile sector. |
| "This is just one number." | True. The paper claims one identity. The narrowness is the strength. |

## Files inherited

- `papers/cosmological-folding-rate/dynamics/hawking_radiation_derivation.py` — verification script. Move/copy.
- `papers/cosmological-folding-rate/dynamics/HAWKING_RESULT.md` — convert to draft text for §4–§5.
- `papers/paper-xxii/scripts/run_icosian_exact.py` — exact icosian arithmetic.

## Open scoping questions

1. Is the **PBH cutoff prediction** strong enough to anchor §7, or should §7 be deflated to "scope" only?
2. Should the **first-law identity** (§5) be its own §, or folded into §4?
3. Should we cite **Strominger–Vafa** for context, or keep this paper free of QG-derivation comparisons?
4. Length: 10pp tight or 14pp with more semiclassical-recovery discussion?

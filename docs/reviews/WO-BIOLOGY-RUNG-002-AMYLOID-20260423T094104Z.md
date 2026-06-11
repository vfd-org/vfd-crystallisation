**1. Claim Audit**
- `[L.1] “The preimage … is cyclic of order 10 … angles … {0°,36°,…,324°}”` is now materially established in the derivation. The Schur-Zassenhaus/copime-order split plus the `\exp(i(\alpha/2)\hat n\cdot \hat\sigma)` convention fixes the earlier ambiguity. No substantive defect in the derivation proof remains here. `papers/biology-rung/derivation-amyloid.md:111-134`
- `[C.1 of L.1] “The smallest nonzero angle … is 36°”` follows from `[L.1]`. Fine. `papers/biology-rung/derivation-amyloid.md:136-137`
- `[D.2]` is coherent as a definition, and the reduction to the `36°/N · Z` ladder is correct. `papers/biology-rung/derivation-amyloid.md:168-198`
- `[L.2] “dense in R/2π by Weyl’s equidistribution theorem (since 36°/(2π) is rational)”` is not clean. The density conclusion is true, but the stated reason is wrong: Weyl is irrelevant here, and “since rational” points the wrong way. The elementary density of rationals `m/N` is enough. The catalogue version is worse: it invokes continued fractions / best approximants to a rational number. This needs correction. `papers/biology-rung/derivation-amyloid.md:200-212`, `papers/biology-rung/math-catalogue.md:564-570`
- `[D.3]` is explicit, but it bakes in a hidden extra hypothesis: exact full return `Mθ=360°`. Earlier the derivation defines crossover modulo the fibril’s own point-group symmetry; `D.3` drops that and imposes the stricter single-full-turn condition. That changes the admissible window. As a modelling definition it is clear; as “amyloid-scale compatibility” it is stronger than the setup justifies. `papers/biology-rung/derivation-amyloid.md:50-53`, `papers/biology-rung/derivation-amyloid.md:218-240`
- `[L.3]` is established computationally for the current `D.3` filter and `N ≤ 20`. The sim/CSV support a 24-element admissible set, not 49. The derivation itself only lists representatives and relies on the sim. `papers/biology-rung/derivation-amyloid.md:242-262`, `papers/biology-rung/data/wo2_prediction.csv:2-25`
- `[C.1]` is correctly left conjectural, but it inherits the unqualified `D.3` filter. As written it overstates how biologically compelled that filter is. `papers/biology-rung/derivation-amyloid.md:264-280`
- `[C.2]` is properly conjectural, but the “consistent with the L-amino-acid world” phrasing is stronger than the cited upstream source, which supports intrinsic chirality, not a derived bias direction. `papers/biology-rung/derivation-amyloid.md:307-320`
- `[C.3]`, `[C.4]`, `[C.5]`, `[C.6]` are all presented as conjectural/open. No over-claim beyond the usual speculative tone. `papers/biology-rung/derivation-amyloid.md:322-393`

**2. WO Acceptance Audit**
- `AC1` “Publication ready: yes”: not met. There are still substantive math/consistency issues. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:181-183`
- `AC2` “Math-catalogue updated with every new D/L/T/C/N entry”: not met. The catalogue is out of sync and internally wrong in multiple WO-2 entries. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:184`
- `AC3` “Sim enumerates admissible pitches end-to-end”: met for the current `D.3` model. The rewrite enforces exact integer `M` and the CSV matches the computation. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:185`
- `AC4` “Empirical comparison … performed”: not touched. No comparison script/result exists. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:186-187`
- `AC5` “Clear statement of whether (a), (b), or (c) from §1 holds”: only partial. The derivation explicitly takes `(a)` as primary, but does not settle `(a)` vs `(b)` vs `(c)`. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:188`, `papers/biology-rung/derivation-amyloid.md:165-166`
- Open item `(a)`: partially resolved; this is the working model. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:42-46`, `papers/biology-rung/derivation-amyloid.md:149-156`
- Open item `(b)`: not resolved; only sketched. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:42-49`, `papers/biology-rung/derivation-amyloid.md:156-159`
- Open item `(c)`: not resolved; only sketched. `papers/biology-rung/WO-BIOLOGY-RUNG-002-AMYLOID.md:47-49`, `papers/biology-rung/derivation-amyloid.md:160-166`

**3. Catalogue Audit**
- The derivation introduces a corollary label `[C.1 of L.1]`, but the catalogue has no corollary namespace and already uses `C.1` for the amyloid-selection conjecture. That is a numbering collision and audit defect. `papers/biology-rung/derivation-amyloid.md:136-137`, `papers/biology-rung/derivation-amyloid.md:264-280`, `papers/biology-rung/math-catalogue.md:606-613`
- `L.2 (WO-2)` in the catalogue is not backed by the derivation and is mathematically misdescribed. `papers/biology-rung/math-catalogue.md:564-570`
- `L.3 (WO-2)` in the catalogue says “49 distinct θ values”; the actual CSV has 24. `papers/biology-rung/math-catalogue.md:600-602`, `papers/biology-rung/data/wo2_prediction.csv:2-25`
- `C.1 (WO-2)` in the catalogue still uses the stale `[3.4°, 17.1°]` window. `papers/biology-rung/math-catalogue.md:606-613`
- `N.1 (WO-2)` says output/status are pending, but the sim and CSV exist. `papers/biology-rung/math-catalogue.md:681-688`
- The derivation says “Sim N.1 below,” but there is no `N.1` object in the derivation itself. Dead internal reference. `papers/biology-rung/derivation-amyloid.md:261-262`

**4. Attribution / External Consistency**
- The citation to `cascade-bio.md §5.1` for the decagram/36°/10-per-turn substrate is locally supported. `papers/cascade-derivation/cascade-bio.md:559-566`
- The citation to `cascade-bio.md §2.7 / §B5` supports intrinsic chirality of `2I` and a qualitative enantiomer-selection programme, but not a derived handedness bias direction. The amyloid text is stronger than the cited source. `papers/cascade-derivation/cascade-bio.md:162-181`, `papers/cascade-derivation/cascade-bio.md:605-627`
- The citation to the Hopf `15 × 40` cell structure is stale in the opposite direction: the derivation still talks as if this dependency is conjectural, while the current repo also contains a local closure document treating it as closed. `papers/biology-rung/derivation-amyloid.md:376-378`, `papers/cascade-derivation/cascade-phase-l1-closure.md:20-24`, `papers/cascade-derivation/cascade-phase-l1-closure.md:106-116`
- The reference to the WO-1 chirality thread is locally consistent as a qualitative conjectural analogue. `papers/biology-rung/derivation-amyloid.md:312-315`, `papers/biology-rung/derivation-capsid.md:464-480`

**5. Sim Correctness**
- The sim does implement the current `D.3` exactly. It reduces `θ = 36° s / N`, enforces exact integrality via `M = 10N/s`, rejects non-divisors, and imposes `22 ≤ M ≤ 106`. `papers/biology-rung/scripts/wo2_helical_orbits.py:17-23`, `papers/biology-rung/scripts/wo2_helical_orbits.py:55-74`
- The emitted CSV is the 24-element admissible set for `N_max = 20`. I verified the script’s `enumerate_admissible(20)` reproduces the CSV row-for-row, and every row satisfies exact `Mθ = 360°`. `papers/biology-rung/data/wo2_prediction.csv:2-25`
- The round-2 target “all spot-checks `36°/N` for `N=3..10` pass” is correct under current `D.3`. `papers/biology-rung/scripts/wo2_helical_orbits.py:149-162`
- Two non-correctness defects remain in the sim text: the docstring says one row per distinct `(θ,s,N)` triple, but the code dedupes by `θ` only; and the summary formatter has a literal formatting bug. Neither affects the CSV set. `papers/biology-rung/scripts/wo2_helical_orbits.py:59-60`, `papers/biology-rung/scripts/wo2_helical_orbits.py:106-112`, `papers/biology-rung/scripts/wo2_helical_orbits.py:142-147`

**6. Tightness**
- `“cryo-EM surveys find specific discrete clusters”` is too strong without in-repo evidence. Better: `“reported structures include recurring cluster values.”` `papers/biology-rung/derivation-amyloid.md:58-63`
- `“Amyloid-scale compatible”` should say `“amyloid-scale compatible under the exact full-360 crossover filter”`. `papers/biology-rung/derivation-amyloid.md:218-235`
- `“should empirically show a handedness bias consistent with the L-amino-acid world”` should be weakened to `“may show a handedness bias; upstream work only supports intrinsic chirality, not the direction.”` `papers/biology-rung/derivation-amyloid.md:311-319`

**7. Top Three Fixes**
1. Repair `[L.2]` in both derivation and catalogue. Remove the bogus Weyl / continued-fraction language and give the elementary density argument actually available. `papers/biology-rung/derivation-amyloid.md:200-212`, `papers/biology-rung/math-catalogue.md:564-570`
2. Resolve the `D.3` scope contradiction: either justify why crossover must be exact `360°` rather than modulo protofilament symmetry, or restate the filter honestly as a stronger modelling assumption. `papers/biology-rung/derivation-amyloid.md:50-53`, `papers/biology-rung/derivation-amyloid.md:218-235`
3. Clean the WO-2 ledger/debris: fix stale `17.1°`, stale `49 distinct θ values`, stale `N.1 pending`, the dead `Sim N.1 below` reference, the `C.1` numbering collision, and the stale round-0 status line. `papers/biology-rung/math-catalogue.md:600-613`, `papers/biology-rung/math-catalogue.md:681-688`, `papers/biology-rung/derivation-amyloid.md:5`, `papers/biology-rung/derivation-amyloid.md:136-137`, `papers/biology-rung/derivation-amyloid.md:261-262`

**8. Verdict**
Publication ready: no.

**1. Claim audit**

- **D.1** “A helical closure orbit of pitch `(α,h)` is the orbit of `⟨R_α·T_h⟩` … closure-compatible iff `α` is a rational multiple of `2π`” (`derivation-amyloid.md:83-104`).
  Assessment: underdefined. The “infinite stack of 600-cell copies glued along the axis” is not constructed anywhere, and the closure criterion ignores `h` and `x_0`. As a definition this is survivable, but it is not yet a usable mathematical object.

- **L.1** “`Stab_2I(A) = {k·36°}`” (`derivation-amyloid.md:106-127`).
  Assessment: the stated proof does not prove the claim. It assumes the conclusion by invoking `|C_10|=10` before establishing that the stabiliser is `C_10`. It also blurs three different notions: `2I ⊂ SU(2)`, physical rotations about a 5-fold axis, and the decagram phase seen in `cascade-bio.md §5.1`. The conclusion is plausible, but the proof is circular. There is also a geometric gap around the `180°` entry: in `2I`, the order-2 element is central, not obviously a rotation “about axis `A`” in the same sense as the others.

- **Corollary from L.1** “The `2I` group itself does not contain rotations with angle less than 36° about a 5-fold axis” (`derivation-amyloid.md:124-127`).
  Assessment: only as strong as L.1. Not established by the present argument.

- **R.1** “This forces the small-angle twist to emerge between `2I`-elements” (`derivation-amyloid.md:129-154`).
  Assessment: over-strong. At most, conditional on the fixed 5-fold-axis single-element model, small angles are not realised by one such element. That does not “force” the three listed mechanisms.

- **D.2** “`θ(α;p,q):=(pα-q2π)/N`, where `N` is the smallest integer such that `Nθ ≡ 0 mod 2π`” (`derivation-amyloid.md:156-176`).
  Assessment: not well-defined. `θ` is defined using `N`, and `N` is defined using `θ`. Worse, `Nθ = pα-q2π`, so the minimality condition is either independent of `N` or impossible; it does not pick out a unique `N`. This is the central defect in the derivation.

- **L.2** “`Θ_adm(A)` is countable … for each `α` there is an infinite sequence of best rational approximations with `θ→0`” (`derivation-amyloid.md:178-191`).
  Assessment: proof invalid. Here `α/2π = k/10` is rational, so its continued fraction terminates; the quoted “infinite sequence of convergents” argument is wrong. Countability/zero-accumulation may still be salvageable after fixing D.2, but not by this proof.

- **D.3** “`21 ≤ M ≤ 106`, hence `θ ∈ [3.4°,17.1°]`” (`derivation-amyloid.md:197-215`).
  Assessment: numerically wrong at the upper end. From `M·4.7 ∈ [100,500]`, one gets `M ≥ ceil(100/4.7)=22`, not `21`. So the correct upper bound is `360/22 ≈ 16.36°`, not `17.1°`.

- **L.3** “Computing `Θ_adm(A) ∩ [3.4°,17.1°]` … representative values include `36°/N` for `N=3..11`, i.e. … `3.27°`” (`derivation-amyloid.md:217-231`).
  Assessment: self-contradictory and not backed by the sim as described. `36/11 = 3.27°` is outside `[3.4°,17.1°]`, and outside the sim’s actual strict filter `[3.396°,16.364°]`. Also, the derivation says “other values arise from `α ∈ {72°,108°,144°,180°}`”, but the emitted CSV contains only `alpha_deg = 36.000` (`data/wo2_prediction.csv:2-50`).

- **C.1** “Observed twists cluster on `Θ_adm(A) ∩ [3.4°,17.1°]`” (`derivation-amyloid.md:233-249`).
  Assessment: correctly marked as conjecture here, but over-claimed elsewhere. The opening paragraph says the document “derives” the discrete-set statement (`derivation-amyloid.md:7-14`), which it does not.

- **R.2** ultra-slow polymorphs (`derivation-amyloid.md:251-270`).
  Assessment: properly open in tone, but explanation (i) relies on `N>106`, and `N` is not yet a coherent parameter under D.2.

- **C.2** chirality bias (`derivation-amyloid.md:276-289`).
  Assessment: conjectural and explicitly qualitative. Fine as conjecture; not derived.

- **C.3** protofilament count from `2I` subgroups (`derivation-amyloid.md:291-309`).
  Assessment: pure conjecture. No mathematical argument connects subgroup structure to observed protofilament counts.

- **C.4/C.5/C.6** (`derivation-amyloid.md:335-362`).
  Assessment: these are honestly flagged as open.

**2. WO acceptance audit**

Acceptance criteria in `WO-BIOLOGY-RUNG-002-AMYLOID.md:179-188`:

1. **Publication ready yes**: **Not resolved.** Substantive math defects remain.
2. **Catalogue updated with every new D/L/T/C/N**: **Partially resolved.** Main WO-2 entries exist, but there are catalogue defects; see section 3.
3. **Sim enumerates admissible pitches end-to-end**: **Partially resolved.** A sim and CSV exist, but the sim does not implement D.2 as stated and its output contradicts L.3’s prose.
4. **Empirical comparison against at least one amyloid species**: **Not touched.**
5. **Clear statement of whether (a), (b), or (c) holds**: **Not resolved.** The derivation says “We take (a) as the primary hypothesis” (`derivation-amyloid.md:153-154`), not that (a) has been established.

Open items from the WO executive summary (`WO-BIOLOGY-RUNG-002-AMYLOID.md:39-49`):

- **(a) finer / commensurable orbit class yields slower pitches**: **Partially resolved at best.** This is the intended route, but D.2/L.2 are broken.
- **(b) cell-level orbit class admits slower pitches**: **Not touched substantively.** Only deferred to open item C.4.
- **(c) entirely different cascade orbit class**: **Not touched substantively.** Mentioned as a possibility, not analysed.

**3. Catalogue audit**

- Coverage is mostly present: D.1, L.1, R.1, D.2, L.2, D.3, L.3, C.1, R.2, C.2, C.3, C.4, C.5, C.6, N.1 all appear in `math-catalogue.md:488-660`.
- Defect: the derivation contains a labelled corollary, “**Corollary [C.1 of L.1]**” (`derivation-amyloid.md:124-127`), but the catalogue has no corresponding entry, and the label collides with the distinct WO-2 conjecture **C.1**.
- Defect: catalogue **D.2** improperly includes the L.2 claim inside the definition: “`Θ_adm(A)` is countable with zero-accumulation” (`math-catalogue.md:538-543`). That is not a definition.
- Defect: catalogue **L.1** and **L.2** are marked “Proved” (`math-catalogue.md:518,557`) when the derivation does not prove them.
- Defect: catalogue **L.3** repeats the bad filtered list including `3.27°` in `[3.4°,17.1°]` (`math-catalogue.md:573-580`).
- Defect: catalogue **N.1** says output is “Pending” (`math-catalogue.md:659-...`), but `data/wo2_prediction.csv` exists in-repo.

**4. Attribution / external consistency**

- **`cascade-bio.md §5.1` decagram / 10 vertices per turn**: accurate. The source explicitly says adjacent pentagons are rotated by `36°` and the combined orbit is a regular decagram with 10 vertices per `2π` turn (`cascade-bio.md:559-566`).
- **`cascade-bio.md §2.6 / §3.2` Hopf 15×40 cell fibration is conjectural**: accurate. The source calls it a “structural candidate” (`cascade-bio.md:149-160`).
- **`cascade-bio.md §2.7` / B5 for chirality**: mostly accurate but sloppy. `§2.7` supports “2I is intrinsically chiral” and says which enantiomer is selected is a B5 question (`cascade-bio.md:162-181`). The stronger “god-prime selects one enantiomer” language appears in `§5.3` (`cascade-bio.md:595-625`), not in `§2.7` alone.
- **WO-1 chirality thread [C.3]**: only partially supportive. WO-1 C.3 is a capsid-level qualitative asymmetry conjecture (`derivation-capsid.md:464-480`). It does not establish fibril handedness; it provides an analogy, not a proof.
- I found no evidence that the amyloid derivation misquotes the B2 decagram result. The main attribution problems are inflation, not fabrication.

**5. Sim correctness**

- The sim does **not** implement D.2 as written. D.2 defines `N` by a minimality condition; the code simply loops over arbitrary `N` and sets `θ = (pα - q·2π)/N` (`wo2_helical_orbits.py:70-85, 87-126`).
- The sim’s actual D.3 filter is `[360/106, 360/22] = [3.396°, 16.364°]` (`wo2_helical_orbits.py:47-56`), not the derivation’s `[3.4°,17.1°]`.
- The derivation’s prose about extra branches from `α = 72°,108°,144°,180°` is not reflected in the published output. `data/wo2_prediction.csv` contains only `alpha_deg = 36.000` (`data/wo2_prediction.csv:2-50`).
- That is not accidental. Algebraically the code computes
  `θ = 360*(p*k/10 - q)/N = 36*(kp - 10q)/N`,
  so after deduplication every value is just an integer multiple of `36°/N`. Larger `α` do not generate new angles; they only duplicate the same ladder.
- `dedupe_by_theta` throws away branch provenance and keeps only the smallest-`N` representative (`wo2_helical_orbits.py:129-138`). That is fatal if the claim is about distinct orbit classes rather than merely distinct numeric angles.
- `M = round(360/theta)` (`wo2_helical_orbits.py:116-117`) is a heuristic post-processing step, not a demonstrated closure witness.

**6. Tightness**

- `derivation-amyloid.md:7-14`: replace “This document derives the cascade-level statement…” with “This document explores the hypothesis that…”.
- `derivation-amyloid.md:133-135`: replace “This forces” with “Under the fixed 5-fold-axis single-element model, this suggests”.
- `derivation-amyloid.md:211`: replace `[3.4°, 17.1°]` with `[3.396°, 16.364°]` or round honestly to `[3.4°, 16.4°]`.
- `derivation-amyloid.md:228-229`: delete “Other values arise from `α ∈ {72°, 108°, 144°, 180°}`” unless you preserve branch provenance and show genuinely new values.

**7. Top three fixes**

1. **Rebuild D.2/L.2 from scratch** (`derivation-amyloid.md:156-191`, `wo2_helical_orbits.py:60-126`).
   Make `N` an explicit parameter of the definition, or eliminate it entirely. Right now the central object is circular.

2. **Fix the amyloid-scale window and recompute all downstream claims** (`derivation-amyloid.md:197-231`, `math-catalogue.md:561-580`, `wo2_helical_orbits.py:47-56`, `data/wo2_prediction.csv:2-50`).
   The upper bound is `16.36°`, not `17.1°`, and `36°/11` does not belong to the filtered set.

3. **Replace L.1’s proof with an actual group-theoretic argument** (`derivation-amyloid.md:106-127`).
   Prove that the preimage in `2I` of a 5-fold `I ≅ A_5` stabiliser is cyclic of order 10, then explain what “angle” means in this SU(2)/600-cell setting.

**8. Verdict**

Publication ready: **no**.

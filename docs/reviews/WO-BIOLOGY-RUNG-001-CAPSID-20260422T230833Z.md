**1. Claim Audit**

- **[D.1] “`𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)`”** and “the six units realise the `C_6` action at each face center, which is the stabiliser of a face under `I_h`” are not well-defined as stated. You never construct the WO-promised `2I`-invariant sublattice, only a facewise Eisenstein lattice plus an `A_5` action on faces. Worse, the face stabiliser in the icosahedral symmetry is `C_3` rotationally (or `D_3` including reflections), not `C_6`. The local hexagonal `C_6` is lattice symmetry, not icosahedral-face stabiliser symmetry. [derivation-capsid.md:77](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:77)

- **[L.0] “`π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓`”** is standard and consistent with the stated character values. No defect here. [derivation-capsid.md:101](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:101)

- **[D.2] “`𝒯_casc : ℤ[ω] → ℤ_{≥0}`, `𝒯_casc(z)=z\bar z`”** is well-defined on `ℤ[ω]`. But the added sentence that it is “`A_5`-equivariant” on the substrate is not formalised: no `A_5` action on the domain is defined, and the map is scalar-valued anyway. This is sloppy but repairable. [derivation-capsid.md:126](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:126)

- **[L.1] “`spec(𝒯_casc)=Loeschian numbers`”** is established, but only as the classical image of the Eisenstein norm on `ℤ[ω]`. That part is fine. [derivation-capsid.md:147](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:147)

- **[L.3] “Any positive-definite `C_6`-invariant quadratic form on `ℤ[ω]` is `c·𝒯_casc`”** is only half-shown. The real-linear statement on `ℝ²` is plausible; the proof sketch is missing the actual matrix argument. More importantly, the document repeatedly sells this as forced by the *substrate’s own symmetry*, but the only symmetry used is the extra hexagonal-lattice `C_6`, not the icosahedral face stabiliser. So the abstract uniqueness claim is probably true; the advertised geometric meaning is overstated. [derivation-capsid.md:156](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:156)

- **[T.1] “single operator on the cell-level icosahedral substrate, uniquely determined up to scale by the substrate’s local `C_6` symmetry”** is over-claimed. What you actually have is the classical norm on `ℤ[ω]`, plus a sketch that `C_6`-invariant quadratic forms on a planar hexagonal lattice are scalar multiples. You do **not** have a cell-level `600`-cell operator or a defined `2I`-invariant sublattice. Existence of a face-level norm is shown; the stronger substrate-level uniqueness claim is not. [derivation-capsid.md:176](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:176)

- **[R.1] “the current doc’s T=5 entry is misleading”** is a fair rereading of the existing document. The old file explicitly lists `T=5` as a T-number while also correctly listing the Loeschian sequence without `5`. The extra sentence “no `T=5` capsids are observed” is not sourced anywhere in-repo. [derivation-capsid.md:193](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:193)

- **[L.2] “`{irrep-dims} ∩ {Loeschians ≤ 5} = {1,3,4}`”** is correct. The prose immediately after it is not: “three of the five distinct `A_5` irrep dimensions” is false. `A_5` has five irreps but only **four distinct dimension values**: `1,3,4,5`. [derivation-capsid.md:216](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:216)

- **[D.3] `μ(T)` via `D_6`-orbits** is the worst mathematical defect in the draft. If you mod out by `D_6`, you have already included conjugation, so laevo/dextro are identified. Then `μ(T)=2` for chiral cases is false as stated. To count chirality pairs you need `C_6`-orbits first, not `D_6`-orbits. [derivation-capsid.md:247](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:247)

- **[C.1] weighting by `μ(T)`** is conjectural, which is fine, but it rests on the broken `μ(T)` definition. As written it is not yet mathematically coherent. [derivation-capsid.md:272](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:272)

- **[C.3] chirality asymmetry** is admissible as a conjecture, but again its formal basis is corrupted by [D.3]. [derivation-capsid.md:291](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:291)

- **[C.2] restriction of Paper XXXII `F`** is not posed tightly enough to be worked out next round. `π`, `(600-cell)^{2I}`, “face-level residue”, and `F | (π-fibre-average)` are undefined. The claimed upstream theorem is also misidentified. This is not a worked conjecture; it is a sketchy aspiration. [derivation-capsid.md:317](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:317)

- **[C.4]** is clearly labelled speculative. No objection beyond that. [derivation-capsid.md:352](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:352)

- **[N.1]/[N.2]** are placeholders, not results. No sim artefacts or scripts were supplied, so nothing is established here. [derivation-capsid.md:389](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:389)

**2. WO Acceptance Audit**

- **AC1** “passes codex review: publication ready yes”: **not resolved**.
- **AC2** “catalogue lists every D/L/T/C/N with provenance and status”: **partially resolved**. Coverage is mostly complete, but some entries are wrong in content/status.
- **AC3** “sim runs end-to-end”: **not touched**. The promised scripts/data are absent from the repo. [WO-BIOLOGY-RUNG-001-CAPSID.md:119](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:119)
- **AC4** “comparison result recorded honestly”: **not touched**.
- **AC5** “T=5 question is settled explicitly”: **resolved mathematically**, via [L.1]/[L.2]/[R.1], though not propagated back into `cascade-bio.md`.

- **O1** restriction of `F` vs new object: **not resolved**. Still conjectural, and presently misattributed/undefined. [WO...:106](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:106)
- **O2** T=5: **resolved** as option (a): the honest overlap is `{1,3,4}`.
- **O3** `2I` vs `A_5`: **partially resolved**. The draft chooses `A_5` for face-level action, `2I` for chirality, but the promised justification from the existing doc is thinner than claimed.
- **O4** chirality weighting: **partially resolved** as conjecture only.
- **O5** VIPERdb bias: **not touched**.

**3. Catalogue Audit**

- Coverage is broadly complete: every derivation `D/L/T/C/N` object has a catalogue entry, and there are no obvious extra catalogue `D/L/T/C/N` entries absent from the derivation.
- The defects are substantive:
- **D.3** in the catalogue repeats the false `D_6`-orbit/chirality statement. [math-catalogue.md:78](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:78)
- **L.2** repeats the false phrase “five distinct `A_5` irrep dimensions.” [math-catalogue.md:139](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:139)
- **L.3** is marked “proved” although the derivation only gives a sketch and overstates the geometric source of the `C_6` symmetry. [math-catalogue.md:159](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:159)
- **T.1** is marked “proved” in the stronger substrate-level form, which the derivation does not establish. [math-catalogue.md:180](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:180)
- **N.1/N.2** describe scripts that are not present in the repo. As pending computational placeholders they match the derivation, but they are not backed by supplied artefacts. [math-catalogue.md:317](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:317)

**4. Attribution / External Consistency**

- **`cascade-bio.md §3.1` for “biology lives at the cell level”**: supported. [cascade-bio.md:198](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:198)
- **`cascade-bio.md §2.1–2.3` for `2I`, quotient to `A_5`**: supported. [cascade-bio.md:43](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:43)
- **`cascade-bio.md §B3.1` for `T=h²+hk+k²` / Loeschian numbers**: supported. [cascade-bio.md:257](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:257)
- **`cascade-bio.md §B3.2` re-read in [R.1]/[L.2]**: fair. The source explicitly overclaims `T=5` as a T-number. [cascade-bio.md:274](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:274)
- **`cascade-bio.md §2.7` for chirality**: supports only a qualitative chirality story, not the stronger capsid-level asymmetry machinery. [cascade-bio.md:162](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:162)
- **`paper-xxxii` “Theorem F: uniqueness under locality / compact `S^3` / finite-subgroup-closure / maximal vertex-transitivity axioms”**: false attribution. The `compact S^3` / finite-subgroup / maximality assumptions belong to the 600-cell-selection theorem, not Theorem F. Theorem F itself is the log-sum-exp uniqueness theorem under A1–A3 in a soft-min class. [paper-xxxii.tex:237](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:237), [paper-xxxii.tex:363](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:363)
- **WO citation to `paper-xxxii.tex §2` for “general form of closure operator, uniqueness theorem, spectral structure”**: not verified at the cited location. The closure-functional theorem is later in the paper, not in “§2” as cited. [WO...:81](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:81)
- **WO citation to `foundations.tex §F2` for “locality, invariance, scalar-valued, order ≤ 2”**: not verified. The local source I found supports the closure form `αR+βE−γQ` and quadratic finite-level energies, not those axioms. [WO...:82](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:82), [foundations.tex:1100](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-correspondence-foundations/foundations.tex:1100)
- **Catalogue provenance for `R.2` from an “implicit ... 3/3' irrep pair” in `cascade-bio.md §B3.2`**: not found. The source mentions only the 3-dimensional standard irrep, not a `3/3'` pair. [math-catalogue.md:229](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:229), [cascade-bio.md:280](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:280)

**5. Sim Correctness**

- No sim artefact was supplied. The WO promises `scripts/wo1_capsid_predict.py`, `scripts/wo1_viperdb_fetch.py`, `scripts/wo1_compare.py`, and generated `data/` outputs, but none are present, so there is nothing to audit for correctness. [WO...:119](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:119)

**6. Tightness**

- [derivation-capsid.md:7](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:7): replace “uniquely picked out by the 2I / A5 symmetry” with “realised by the classical Eisenstein norm on face data; uniqueness under added local `C_6` lattice symmetry is argued separately.”
- [derivation-capsid.md:170](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:170): replace “substrate-determined” with “determined once one imposes local hexagonal-lattice `C_6` symmetry.”
- [derivation-capsid.md:185](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:185): replace “Theorem [T.1] closes this item” with “This gives a face-level candidate operator matching the CK spectrum; the relation to the full 600-cell closure machinery remains open.”
- [derivation-capsid.md:262](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:262): replace the `D_6` sentence with “under `C_6` there are two chirality classes when `h,k` are nonzero and distinct; adjoining conjugation collapses them into one `D_6`-orbit.”

**7. Top Three Fixes**

- **1. Repair [D.3]/[C.1]/[C.3].** The current `D_6`-orbit definition destroys the chirality split it claims to count. Start at [derivation-capsid.md:247](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:247) and [math-catalogue.md:78](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:78).
- **2. Rewrite [C.2] and its provenance.** Define the projection, the domain, and the restriction map, or stop pretending this is a mathematically posed conjecture. Also stop attributing the wrong theorem to `paper-xxxii`. Start at [derivation-capsid.md:317](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:317), [WO...:81](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:81), [WO...:82](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:82).
- **3. Downgrade or restate [D.1]/[L.3]/[T.1].** As written they overclaim a cell-level `2I` substrate result when the actual derivation is a face-level Eisenstein norm result with an extra local lattice symmetry. Start at [derivation-capsid.md:77](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:77), [derivation-capsid.md:156](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:156), [derivation-capsid.md:176](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:176).

**8. Verdict**

Publication ready: **no**.

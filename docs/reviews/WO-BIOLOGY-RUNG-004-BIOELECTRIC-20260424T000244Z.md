**1. Claim Audit**

- “`G/2I` has exactly 5 orbits of size 120 each” — `biology-rung-bioelectric.tex:132-139`. Established by `wo4_sim_close_orbits.py`; I reproduced 5 orbits of size 120. Caveat: the sim is floating-point, despite the docstring implying exact arithmetic.
- “No eigenmode computation is performed/run here” — `biology-rung-bioelectric.tex:68-70`, `156-163`, `469-472`. False/stale. The derivation now cites `wo4_sim_close_laplacian.py` output at `324-330` and `431-435`.
- “5 vertex orbits … see WO-1 catalogue R.0” — `biology-rung-bioelectric.tex:211-214`. False attribution. R.0 only says `2I` vs `A_5` substrate, not the WO-4 cell-orbit count.
- “`A_5` has five irreducible complex representations…” — `biology-rung-bioelectric.tex:219-226`. Correct standard representation theory.
- Definition of `L_casc` as a graph Laplacian “conjecturally obtained by restriction…” — `biology-rung-bioelectric.tex:237-250`. Not constructed. The PSD/symmetric/commuting conclusions are conditional, not established.
- Conj. C1, “admissible prepatterns are low-lying eigenmodes … classified by `A_5` irrep content” — `253-278`. Not established. Worse: the text later admits the quotient graph alone cannot carry non-trivial `A_5` labels (`331-335`).
- Conj. C2, “double-head and no-head … sign-inversions / squared `3` mode” — `280-288`. Not mathematically defined. Squaring an eigenmode is generally not an eigenmode; “sign inversion” does not produce a double-pole state without a nonlinear model.
- Conj. C3, “patterns with `A_6` or `A_7` symmetry content” falsify — `290-300`. Ill-posed on a `2I/A_5` cell substrate unless an embedding/projection/norm is specified.
- B_laplacian claim: “first six low-lying eigenvalues have multiplicities `1,4,9,16,25,36`” — `324-330`. Reproducible. I reran the script and got those multiplicities.
- “confirming isotypic structure on low modes” — `431-435`. Over-claim for the supplied artefact. The script prints multiplicities, but does not classify each eigenspace by restricted `2I` character.

**2. WO Acceptance Audit**

- Goal 1, define `Δ_casc` — partially resolved. A conjectural placeholder exists; no operator is constructed.
- Goal 2, compute eigenspectrum — partially resolved. Standard full `600 x 600` cell-graph Laplacian computed; not `Δ_casc`, not quotient `Δ_casc`.
- Goal 3, classify eigenmodes by `2I` irrep — partially resolved at best. Multiplicities are suggestive; script’s `A_5` decomposition is invalid and no per-eigenspace `2I` classification is reported.
- Goal 4, map modes to morphologies — not resolved. Only conjectural assignments.
- Goal 5, compare to Levin data — not resolved.
- Goal 6, forbidden morphology — partially resolved. C3 names a possible falsifier, but it is not mathematically or experimentally specified enough.
- Goal 7, φ-scaling check — not touched.
- §4 anticipated entries: `G_600` partially defined; `Δ_casc` not constructed; first nontrivial `4`-dim `A_5` mode not shown; morphology correspondence not shown.

**3. Catalogue Audit**

The supplied catalogue has no WO-4 section. Defects:

- Missing D entry for cell graph / quotient: `biology-rung-bioelectric.tex:206-215`.
- Missing D entry for conjectural `L_casc`: `237-250`.
- Missing C entries for C1/C2/C3: `253-301`.
- Missing N entry for B_orbits: `132-139`, `426-430`.
- Missing N entry for B_laplacian multiplicities: `324-330`, `431-435`.
- Existing R.0 does not support the five-orbit claim; it only states `2I`/`A_5` substrate status (`math-catalogue.md:266-276`).

**4. Attribution / External Consistency**

- `CascadeBio §2.1-2.3, §3.1` supports `2I`, `A_5`, and cell-level biology: yes (`cascade-bio.md:43-70`, `189-201`).
- `CascadeBio §2.6/§3.2` supports 600 cells and candidate `15 x 40` Hopf fibre arithmetic: yes (`cascade-bio.md:143-160`, `203-214`). It does not support a 5-orbit WO-4 cell quotient.
- WO-1 / SmartCapsid Lemma L.0 supports the face permutation decomposition only: yes (`biology-rung-capsid.tex:196-227`). It does not classify WO-4 cell eigenmodes.
- Paper XXXII §4 supports a pointwise soft-min closure functional, not a graph Laplacian: `paper-xxxii.tex:363-389`.
- CascadeFoundations §F2 supports density form `F = ∫(αR + βE - γQ)dV`, not a cell graph Laplacian: `cascade-foundations.md:91-155`.
- WO-6 cross-reference is accurate: `WO-BIOLOGY-RUNG-006-DMN-BRIDGE.md:79-85`.
- Xenopus citation fix is incomplete. Intro cites Vandenberg primary (`biology-rung-bioelectric.tex:105-110`), but the abstract still omits it (`47-49`) and §3.2 still attributes pre-gene voltage maps to Pietak (`348-350`).

**5. Sim Correctness**

- `wo4_sim_close_orbits.py` does implement the B1 orbit-count claim and reproduces 5 orbits of size 120. B1 is computationally closed, modulo floating-point tolerance and no saved output artefact.
- `wo4_sim_close_laplacian.py` computes the standard face-sharing cell-graph Laplacian correctly enough for the reported spectrum. B2 multiplicities are verifiable.
- Major bug: `decompose_character_A5()` assumes the cell action factors through `A_5` (`wo4_sim_close_laplacian.py:184-188`). It does not. The central element `-e` acts nontrivially on cells. The printed `A_5` decomposition is therefore not a valid representation-theoretic result.
- The script does not classify each eigenspace by `2I` irrep; it decomposes the full permutation representation after computing eigenvalues. No χ²/KL/statistical comparison is present.

**6. Tightness**

- Replace “computed fact” at `biology-rung-bioelectric.tex:139-140` with “verified for this 600-cell coordinate/action implementation.”
- Replace “confirming isotypic structure” at `431-435` with “matching the expected squared-dimension multiplicity pattern; irrep classification still requires eigenspace character projections.”
- Delete stale “No computational artefact is supplied” at `469-472`.
- Replace “at most 5” at `275-277` with “candidate grouping into five `A_5` labels, if a valid descent is constructed.”

**7. Top Three Fixes**

1. Fix `wo4_sim_close_laplacian.py:170-273`: remove invalid `A_5` descent; compute restricted `2I` class characters per eigenvalue eigenspace and assert the claimed irrep labels.
2. Purge false R.0 attribution at `WO-BIOLOGY-RUNG-004-BIOELECTRIC.md:68-70` and `biology-rung-bioelectric.tex:211-214`; cite B_orbits instead.
3. Add WO-4 catalogue entries for D1, C1-C3, B_orbits, and B_laplacian; currently `math-catalogue.md` has no WO-4 ledger at all.

**8. Verdict**

Publication ready: no. B1 is basically closed; B2’s multiplicities are reproducible, but the representation classification and `A_5` descent are not correct as artefacts, the false R.0 attribution persists, and the catalogue is missing every WO-4 object.

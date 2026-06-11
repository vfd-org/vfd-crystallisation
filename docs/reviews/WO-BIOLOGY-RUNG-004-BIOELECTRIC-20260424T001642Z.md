**1. Claim Audit**
- `papers/biology-rung-bioelectric/biology-rung-bioelectric.tex:55-66`, `145-153`, `253-278`: the central “`A_5` quotient / five attractor families” claim is not established and is now the wrong level. The supplied sim verifies that `-e` acts nontrivially on cells, so the full action does not factor through `A_5`. At most, central-even eigenspaces can descend after a separate quotient construction.
- `biology-rung-bioelectric.tex:131-140`, `417-424`: the 5 orbits of size 120 are sim-verified. I ran `wo4_sim_close_orbits.py`; it reports 5 orbits, all size 120. This claim is clean.
- `biology-rung-bioelectric.tex:211-215`: “see WO-1 catalogue R.0” does not support the 5-cell-orbit statement. R.0 only distinguishes `2I` vs `A_5`; cite `B_orbits` / catalogue `N.1` instead.
- `biology-rung-bioelectric.tex:237-250`: the definition of `\Lcasc` is only a placeholder. The argument does not construct a closure-Laplacian. Also “its eigenspectrum would descend to `G/2I`” is false as stated; only invariant/central-even scalar sectors descend.
- `biology-rung-bioelectric.tex:280-288`: double-head/no-head as “sign inversions” or “squared `3` mode” is not derived. Squaring an eigenmode is generally not an eigenmode, and no nonlinear closure algebra is specified.
- `biology-rung-bioelectric.tex:290-301`: the forbidden-pattern falsifier is not 2I-clean. “`A_6` or `A_7` symmetry content” is not defined on the `2I` cell graph.
- `biology-rung-bioelectric.tex:324-335`, `425-434`: the sim does establish the standard cell-graph Laplacian spectrum facts: 4-regular graph, 1200 edges, 27 eigenvalues, low multiplicities `(1,4,9,16,25,36)`, and central parity. It does not establish labelled low-mode irreps.
- `biology-rung-bioelectric.tex:428-430` and catalogue `N.2`: “first six 2I irreps `{1,2,3,4,5,6}`” is imprecise. These are six distinct dimensions, not six irreps; `2I` has duplicate 2-, 3-, and 4-dimensional irreps.
- `biology-rung-bioelectric.tex:451-454`: “confirming isotypic structure” overclaims. The script explicitly says full per-eigenspace decomposition is not attempted (`wo4_sim_close_laplacian.py:395-398`).
- `biology-rung-bioelectric.tex:68-70`, `156-157`, `488-491`: stale. A standard graph-Laplacian computation and CSV artefact now exist. What remains uncomputed is `\Lcasc`.

**2. WO Acceptance Audit**
- Criterion 1, define `Δ_casc` (`WO...:68-70`): partially resolved. A conjectural name exists; no construction.
- Criterion 2, compute eigenspectrum (`WO...:71-72`): partially resolved for the standard graph Laplacian, not for `Δ_casc`.
- Criterion 3, classify eigenmodes by `2I` irrep (`WO...:73`): partially resolved only by central parity. Full irrep labels unresolved.
- Criterion 4, map modes to morphology (`WO...:74-76`): not resolved.
- Criterion 5, compare to Levin data (`WO...:77-80`): not touched.
- Criterion 6, forbidden morphology (`WO...:84-87`): partially sketched, not operational and not 2I-clean.
- Criterion 7, φ-scaling (`WO...:88-89`): not touched.
- §4 anticipated math: `G_600` is resolved; `Δ_casc` is unresolved; the expected first nontrivial `A_5` 4-irrep is not resolved and is likely contradicted by `χ(-e)=-4` for the first nonzero mode; morphology correspondence remains conjectural.

**3. Catalogue Audit**
- Catalogue `D.1` is the cell graph (`math-catalogue.md:901-909`), but manuscript `def:D1` is the conjectural closure-Laplacian (`biology-rung-bioelectric.tex:237-251`). Missing catalogue entry for `\Lcasc`, or labels need renaming.
- Catalogue `C.1` says 2I-level, no global descent to `A_5`, at most 9 irreps (`math-catalogue.md:957-965`). Manuscript `C1` says `A_5`, quotient graph, at most 5 (`biology-rung-bioelectric.tex:253-278`). Direct conflict.
- Catalogue `C.2` says concrete phenotype assignments are deferred (`math-catalogue.md:971-980`). Manuscript `C2` makes a concrete double-head/no-head assignment (`biology-rung-bioelectric.tex:280-288`). Direct conflict.
- Catalogue `C.3` is 2I-overlap based (`math-catalogue.md:984-991`). Manuscript `C3` is non-`A_5` / `A_6` / `A_7` based. Direct conflict.
- Full permutation decomposition at `biology-rung-bioelectric.tex:435-440` is a new computational result but is not separately catalogued unless folded explicitly into `N.1` or `N.2`.

**4. Attribution / External Consistency**
- `cascade-bio.md` supports `2I` as 600-cell vertices and `A_5` quotient (`cascade-bio.md:43-68`), the 600 tetrahedral cells and 15×40 Hopf candidate (`cascade-bio.md:143-160`), and biology at cell level (`cascade-bio.md:189-206`).
- `cascade-bio.md` does not supply the 5 cell-orbit result; that is from `B_orbits`.
- Paper XXXII §4 supports a pointwise soft-min closure functional (`paper-xxxii.tex:363-389`), not a cell-graph Laplacian restriction.
- `cascade-foundations.md §F2` supports the density form `F[Φ]=∫(αR+βE−γQ)dV` (`cascade-foundations.md:137-144`), not a graph projection.
- WO-1 / capsid Lemma L.0 does support the `A_5` face representation decomposition (`biology-rung-capsid.tex:196-202`), but that is face-level, not WO-4 cell-mode classification.

**5. Sim Correctness**
- `B_orbits` is clean: direct run returns 5 orbits of size 120.
- `B_laplacian` matches the supplied CSV for the reported modes. I reproduced: 600 cells, degree min/max 4/4, 1200 edges, 27 distinct eigenvalues, low multiplicities as stated.
- Full permutation representation decomposition is correct and forced by freeness: `χ_perm(e)=600`, all nonidentity classes `0`, hence `5` regular representations.
- Full low-eigenspace irrep decomposition is not correct/complete. Using the script’s own character table, projections for several first eigenspaces are non-integral; the script rightly declines to use them.
- Minor sim bug: `wo4_sim_close_laplacian.py:304` checks `degrees.mean() == 4.0`; it should assert `np.all(degrees == 4)`.
- No χ²/KL/null-hypothesis comparison is implemented. That is acceptable only if the paper keeps empirical comparison explicitly future-work.

**6. Tightness**
- Replace “classified by `A_5` irreps” with “classified first by `2I` irreps; central-even sectors may later descend to `A_5`.”
- Replace “eigenspectrum would descend to `G/2I`” with “the invariant sector descends; nontrivial 2I eigenspaces live on the full cell graph.”
- Replace “first six 2I irreps” with “first six distinct 2I irrep dimensions.”
- Replace “confirming isotypic structure” with “consistent with an isotypic interpretation, pending full character projection.”
- Replace “No computational artefact is supplied” with “A standard graph-Laplacian artefact is supplied; `\Lcasc` remains unconstructed.”

**7. Top Three Fixes**
1. `biology-rung-bioelectric.tex:55-66`, `145-153`, `253-278`: rewrite the core conjecture from `A_5` quotient/five-family language to 2I-first language, with `A_5` descent only as a separate open projection.
2. `biology-rung-bioelectric.tex:237-250`, `321-335`, `451-454`: fix quotient/descent and irrep-classification overclaims. The sim proves multiplicity/parity, not labelled irreps.
3. `math-catalogue.md:901-991` and manuscript labels: align `D.1`, `C.1`, `C.2`, `C.3`; add or fold in the full-permutation-rep computational result.

**8. Verdict**
Publication ready: no.

The 2I-level free-action and full-permutation-representation pieces are clean. The low-mode analysis is not yet mathematically clean beyond multiplicity and central parity, and the manuscript still carries an incompatible `A_5` quotient/five-attractor framework.

Publication ready: **no**.

Reviewed file: [biology-rung-bioelectric.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-bioelectric/biology-rung-bioelectric.tex:1>)

**1. Claim audit**
- **Definition D.1** (`lines 227-240`): acceptable as an explicitly conjectural definition. It does not overclaim a construction. The problem is downstream use: the paper never specifies a coherent representation-theoretic setting in which `\mathcal G/2I` can still carry nontrivial `A_5`-irrep content.
- **Conjecture C.1** (`lines 243-268`): not established, and more seriously not even well-posed as written. You place the operator on the **quotient graph** `\mathcal G/2I` (`lines 246-247`), but then classify eigenmodes by `A_5` irreps. After quotienting by the full `2I` action, there is no nontrivial `2I`/`A_5` action left to classify. This is a structural defect, not merely “open work.”
- **C.1 again** (`lines 265-267`): “The morphological attractor count is at most 5 (the `A_5` irrep count)” does not follow. Irrep count does not bound attractor count without a precise rule identifying one attractor family per isotypic sector and excluding multiplicities, mixed modes, nonlinear selection, etc.
- **C.1 itemisation** (`lines 249-263`): the assignments `3 -> AP axis`, `3' -> heterospecific head`, `4 -> electric face`, `5 -> axolotl/echinoderm-like contexts` are naked conjectural matches. That is fine in principle, but the text should say “candidate match” uniformly. As written, some bullets read closer to asserted identifications than to hypotheses.
- **Conjecture C.2** (`lines 270-278`): not established; also mathematically muddled. A sign flip of a single `3`-mode gives `f -> -f`; it does not by itself produce both “double-head” and “no-head.” The phrase “squared `\mathbf 3` mode” is introduced ad hoc and never defined.
- **Conjecture C.3** (`lines 280-291`): not established and poorly specified. “A pattern with `A_6` or `A_7` symmetry content” is undefined in this graph setting, especially after collapsing to a 5-vertex quotient. If the intended falsifier is “a viable morphology induced by a voltage pattern not approximable by the low eigenspaces,” say that.
- There are **no proved theorems/propositions/corollaries/numerical results in this paper itself**. On point (a): the manuscript mostly does keep the “framework conjecture note” framing, but several sentences overstep by talking as if the mathematical architecture were already coherent when it is not.

**2. Internal consistency**
- The central inconsistency is between `lines 201-205`, `243-247`, and `314-318`. A `5`-vertex quotient graph and a `5 x 5` matrix in an orbit basis cannot simultaneously realise the full `A_5` irrep list `1,3,3',4,5`. The natural 5-letter permutation representation is `1 ⊕ 4`, not the full irrep spectrum.
- Relatedly, `lines 58-60`, `138-143`, and `239-240` conflate three different spaces: the full cell graph, the quotient graph, and an `A_5` representation space. The paper needs to choose one.
- `lines 61-66` and `209-216` mishandle the “full `A_5` irrep spectrum.” `lines 62-63` say dimensions `1,3,4,5` are “the full spectrum,” omitting the second 3-dimensional irrep; later the paper correctly lists five irreps.
- `lines 63-66` also miscount the morphologies. The prose says “five bulk attractor morphologies” but then folds in the `3/3'` pair as a “polymorphic variant.” The counting is unstable throughout.
- Cross-references within the LaTeX source itself are fine: all `\ref{...}` labels used in the file resolve to existing labels. There are no internal broken `\ref`/`\eqref` calls visible in source.

**3. External consistency**
- **WO-1 / R.0 attribution is wrong.** The paper claims the “5 vertex orbits” come from “R.0 of WO-1’s catalogue” (`lines 129-130`, `201-205`, `409-410`). In [math-catalogue.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:266>), `R.0` says only that the substrate admits both `2I` and `A_5`; it does **not** state a 5-orbit decomposition of the cell graph.
- The local source that does mention “5 vertex orbits” is the WO-4 stub [WO-BIOLOGY-RUNG-004-BIOELECTRIC.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/WO-BIOLOGY-RUNG-004-BIOELECTRIC.md:121>), where it appears as an anticipated object, not a derived fact.
- **WO-1 / Lemma L.0 attribution is fine but limited.** [biology-rung-capsid.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:196>) proves the decomposition of the **20-face permutation representation**. That supports the imported `A_5` irrep table, not the bioelectric paper’s cell-graph quotient claims.
- **`cascade-bio.md` supports the conjectural Hopf-cell-fibration framing**: `§2.6` explicitly calls the `15 x 40` cell fibration a “structural candidate” / conjectural (`cascade-bio.md lines 149-160`). On point (a), the present paper is consistent with that.
- **`cascade-bio.md` does not support the paper’s cell-orbit claim cleanly.** It supports the five disjoint `24`-cell / coset picture (`paper-xxxv.tex` lines 55-57 also do), i.e. a five-letter `A_5` action on Schläfli frames, not “five vertex orbits of the 600-cell cell graph.”
- **Levin citations**
  - Beane 2011 supports voltage control of head-versus-tail identity in planaria, including headless/double-headed outcomes. It does support the general bioelectric-prepattern story. Source: PubMed/PMC abstract and review discussion. Links: https://pubmed.ncbi.nlm.nih.gov/21276941/ , https://pmc.ncbi.nlm.nih.gov/articles/PMC3278711/
  - Durant 2017 supports stable rewriting of planarian AP pattern and double-headed outcomes. It does **not** appear to be the primary source for heterospecific-head morphology. Link: https://www.sciencedirect.com/science/article/pii/S0006349517304277
  - The heterospecific-head claim at `lines 101-104`, `254-257`, `326-330` should cite Emmons-Bell et al. 2015 instead. Link: https://www.mdpi.com/1422-0067/16/11/27865
  - Pietak and Levin 2016 is a **BETSE/simulation** paper, not the primary experimental “electric face” paper. It discusses instructive prepatterns and cites the frog-face work, but the direct experimental support is Vandenberg et al. 2011, not Pietak 2016. Links: https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2016.00055/full , https://pubmed.ncbi.nlm.nih.gov/21761475/
  - Levin 2021 supports the high-level review claims about bioelectric networks controlling large-scale morphogenesis and cancer-related dysregulation. It does **not**, from the abstract at least, support the specific wording that Levin “posed explicitly” the paper’s discrete-attractor question at `lines 113-117`. Link: https://www.sciencedirect.com/science/article/pii/S0092867421002233
- On point (d): I see **no false claim that computation has already been done**. The paper repeatedly says no eigenmode computation is run here (`lines 68-71`, `146-153`, `302-319`, `344-345`, `428-434`).

**4. Tightness**
- `lines 129-130`: replace “has 5 vertex orbits per our survey of the substrate” with “is hypothesised in the programme stub to admit a 5-orbit quotient; this has not been derived here.”
- `lines 135-143`: replace “correspond to five morphological attractor families” with “are conjectured to organise at most five candidate attractor families, pending a coherent operator construction on the full cell graph.”
- `lines 314-316`: replace “straightforward once `\mathcal G/2I` is constructed” with “formal only; the representation space must first be specified consistently.”
- `lines 371-372`: replace “(15/18 preregistered hits)” with “reported elsewhere as a sibling-programme result” unless you are willing to cite the sibling source more carefully.
- `lines 389-391`: replace “would interpret tumour `V_mem` patterns as ‘forbidden’ modes” with “suggests a possible interpretation of tumour-associated `V_mem` disruption as occupancy outside the conjectured admissible mode family.”

**5. Surface issues**
- The abstract’s “full `A_5` irrep spectrum” wording (`lines 62-63`) is mathematically sloppy.
- `PietakLevin2016` is the wrong primary citation for the experimental “electric face” claim.
- `DurantLevin2017` is the wrong primary citation for heterospecific-head morphology.
- `LevinBeane2011` bibliography key is backwards relative to author order in the actual paper, though that is cosmetic.
- “A successful induction of a viable morphology from a non-`A_5`-irrep-classifiable `V_mem` pattern” (`lines 288-290`) is not a well-defined criterion as written.
- No obvious undefined macros or broken internal `\ref`s in source.

**6. Top three fixes**
1. **Repair the mathematical object.** The paper cannot keep claiming both “operator on `\mathcal G/2I`” and “classification by full `A_5` irrep content.” This affects the abstract, Introduction, Definition D.1, Conjecture C.1, and the computational prerequisite (`lines 58-60`, `129-130`, `201-205`, `243-247`, `314-318`).
2. **Remove or explicitly downgrade the unsupported “five cell-graph orbits” claim.** It is not in WO-1 `R.0`; the current attribution is false (`lines 129-130`, `201-205`, `409-410`).
3. **Fix the biological citations.** Heterospecific heads need Emmons-Bell 2015, and the Xenopus “electric face” needs the direct experimental frog-face paper, not Pietak 2016 (`lines 101-108`, `254-260`, `326-334`).

On your specific checks:
- **(a) Conjectural framing:** mostly yes, but with substantive mathematical overreach in the formulation itself.
- **(b) 5-orbit structure via WO-1 R.0:** no.
- **(c) Levin references say what is claimed:** only partly; two important attributions are wrong or non-primary.
- **(d) Over-claim that computation has been done:** no.

Substantive verdict: **not publication-ready**. The problem is not lack of computation; it is that the central conjecture is presently formulated on the wrong space and cited to the wrong internal source.

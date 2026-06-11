I stayed read-only and did not create `docs/codex-derive/...` because the sandbox is read-only.

**SECTION A. Insight / External Relevance**
Already in cascade papers:
- The biology substrate is explicitly cell-level: 600 tetrahedral cells, with the `15 x 40` Hopf cell-fibration still a candidate, not a proved partition: `cascade-bio.md:143-160`, `cascade-bio.md:449-451`.
- The B2 decagram result is upstream and usable for WO-2/WO-5 helical arguments: 10 vertices per turn, 36 degree offset: `cascade-bio.md:535-567`.
- WO-5’s own source already says the golden angle is classical Coxeter/Vogel, while the cascade adds substrate placement: `cascade-bio.md:402-437`.
- `T_PH_1` has changed: it is now `T_meta ~= Z[phi]^2`, rank 2 over `Z[phi]`, not a 13-adjacency object: `cascade-photon-microtubule-alpha-programme.md:103-115`; `cascade-meta-layer-theorem.md:136-161`.
- Local T-MT-1 work says `T_meta` does not carry 13; the viable 13 route is `12 + 1`, the closed 1-neighborhood of a 600-cell vertex: `cascade-phase-tmt1-closure.md:1-8`, `:81-88`, `:126-130`.
- WO-1 does not support WO-4’s “5 cell-graph orbits” attribution. R.0 only supplies the shared `2I/A_5` substrate: `math-catalogue.md:266-274`. WO-1 is face-level and explicitly avoids a cell-level 600-cell closure claim: `biology-rung-capsid.tex:161-167`, `math-catalogue.md:244-255`.

Only in `insight.md` or newer side notes:
- `insight.md` upgrades the alpha story through the `E8 -> 600-cell` 2:1 projection: `insight.md:47-64`, and interprets two conjugate 600-cells as paired sectors: `insight.md:178-190`, `:204-230`. Relevant to narrative, not directly needed to close WO-2/3/4/5.
- God-prime / QMS-3 content is relevant as a future apex consistency check, not as a biology-rung closure input: `insight.md:670-717`.
- Pentagonal holonomy is the strongest new derivation route for “missing dynamics”: define a `Z[phi]^x` 1-cocycle on the 600-cell graph: `insight.md:835-890`. Note the line `insight.md:837` says “120 cells”; cascade source says 600 tetrahedral cells, so Claude should not import that count literally.
- Repo side note already sharpens this into a clock/holonomy build: `docs/pentagonal-torsion-derivation.md:198-220`, `:255-280`.

External literature directly relevant:
- Xenopus electric-face attribution should cite Vandenberg/Morrie/Adams 2011, not BETSE as the primary map source. PubMed/PMC: https://pubmed.ncbi.nlm.nih.gov/21761475/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC10277013/
- Prota 2014 is laulimalide/peloruside at a non-taxane site, not direct taxane-pocket support: https://www.dora.lib4ri.ch/psi/islandora/object/psi:9134
- Taxol/tubulin pocket support should instead use Nogales et al. 1995 and Löwe/Li/Downing/Nogales 2001; Taxol conformation support: Snyder et al. 2001. Search anchors: https://www.nature.com/articles/375424a0 and https://go.drugbank.com/articles/A11194
- Microtubule counts: Tilney et al. 1973 supports 13 protofilaments in surveyed cellular microtubules; Chrétien/Wade 1991 supports in-vitro 12-17 variation. Links: https://rupress.org/jcb/article/59/2/267/18231/MICROTUBULES-EVIDENCE-FOR-13-PROTOFILAMENTS and https://pubmed.ncbi.nlm.nih.gov/1912942/
- Amyloid cross-beta 4.7-4.8 A repeat and twist/crossover measurements are literature-backed: https://pmc.ncbi.nlm.nih.gov/articles/PMC7617691/ and tau cryo-EM twist/crossover example https://pmc.ncbi.nlm.nih.gov/articles/PMC5552202/

**SECTION B. Priority Gaps / Builds**
B1. `B_orbits`: cell-orbit certificate for WO-4  
Object: action map `2I x C_600 -> C_600`, where `C_600` is the set of tetrahedral 4-cliques in the 600-cell vertex graph. Codomain: orbit partition plus weighted quotient graph. Bridges WO-4 `biology-rung-bioelectric.tex:205-209`, `:413-416`. Route: SIM. First step: extend `build_2I_and_icosahedral.py:202-234` to left-multiply each cell and count orbits. Acceptance: exactly 5 orbits, preferably all size 120; otherwise current WO-4 orbit count must be rebuilt around the actual partition.

B2. `B_modes_full`: actual bioelectric eigenmode build  
Object: `L_cell: l^2(C_600) -> l^2(C_600)`, plus `2I/A_5` character projectors. Bridges WO-4 morphology-to-irrep claims at `bioelectric.tex:247-272`, `:274-295`. Route: SIM + representation derivation. First step: construct face-sharing cell Laplacian and decompose low eigenspaces under `2I` and then `A_5`. Important correction: a quotient graph `G/2I` alone cannot carry nontrivial `A_5` irrep labels; the full 600-cell cell graph is needed.

B3. `B_bioelectric_dataset`: Levin-pattern comparison  
Object: map `observed V_mem pattern -> fitted eigenspace / residual`. Domain: Vandenberg/planaria image-derived voltage maps. Codomain: irrep/eigenmode label plus residual score. Bridges WO-4 phenotype assignments. Route: empirical dataset + image registration. First step: pin primary image sources and define a five-pattern template set.

B4. `B_crossover`: amyloid modulo-bundle closure  
Object: predicate `Close_n(theta) := exists M with M theta in (360/n) Z` and `M d_beta in [100,500]`, for `n in {1,2,3,4,5}`. Domain: `theta = 36*s/N`. Codomain: admissible table by bundle symmetry. Bridges D.3 exact-360 condition at `biology-rung-amyloid.tex:255-274` and the physical “modulo point-group” interpretation in `derivation-amyloid.md:50-56`. Route: SIM. First step: add `bundle_n` column and prove `n=1` recovers current 24-row table.

B5. `B_wo2_review`: WO-2 paper audit build  
Object: review checklist from derivation claims to LaTeX claims. Bridges task R2-G3 and current paper summary `biology-rung-amyloid.tex:397-439`. Route: code-review pass. First step: check D.3/D.2/L.2 wording and stale “exact 360” fallout after `B_crossover`.

B6. `B_selector_formal`: tubulin selector theorem repair  
Object: exact selector datum `eta: A_13 -> \hat C_n`, with bijection/minimality and primitive non-uniform characters. Domain: 13 adjacency addresses. Codomain: cyclic characters. Bridges `biology-rung-tubulin.tex:168-189`, `:191-214`, `:216-249`. Route: new derivation. First step: replace D.1c with “primitive non-uniform modes”; prove for `C_13` via `gcd(k,13)=1`.

B7. `B_tmt13_routeK`: 13-source import repair  
Object: `N[v] = {v} union N(v)` in the 600-cell graph, `|N[v]|=13`. Bridges the broken upstream import at `tubulin.tex:149-162` and local T-MT source mismatch. Route: alternative route K, already locally sketched in `cascade-phase-tmt1-closure.md:96-111`. First step: import as conditional biological-instantiation hypothesis `(H-MT)`, not as `T_meta`.

B8. `B_tmeta_routeQ`: optional `T_meta -> 13` bridge  
Object: functor/descent `Z[phi]^2 -> closed H4-neighborhood selector`. Bridges the task’s requested `B_tmeta`. Route: new derivation; no current route in local sources. First step: define a descent map from upper phason flips to H4 vertex-neighborhood adjacency. If no canonical map exists, use Route K instead.

B9. `B_taxane_sources`: tubulin bibliography correction  
Object: citation contract for taxane pocket vs non-taxane MSA sites. Bridges `tubulin.tex:297-300`, `:496-503`. Route: literature lookup. First step: move Prota2014 to “laulimalide/peloruside non-taxane site”; add Nogales1995 / Lowe2001 / Snyder2001 for Taxol site/conformation.

B10. `B_mt_lit_audit`: microtubule empirical summary support  
Object: literature table `(source, organism/condition, protofilament count, in vivo/in vitro) -> claim support`. Bridges `tubulin.tex:372-397`, `:403-415`. Route: literature lookup. First step: extract Tilney1973 and ChretienWade1991 into a small evidence table before retaining any “satisfied by existing literature” sentence.

B11. `B_phyllo_extremality`: classical theorem import/proof  
Object: theorem stack: three-gap theorem + continued-fraction extremality + golden-angle phyllotaxis convention. Bridges `phyllotaxis.tex:256-309`, `:318-364`. Route: classical literature or direct proof, choose one. First step: cite Sós/Świerczkowski for three-gap only; cite Hurwitz/Khinchin/Markov-Lagrange or give a direct continued-fraction lemma for “all partial quotients 1 is extremal.”

B12. `B_cross_ref_wo1_wo5`: WO-1/WO-5 reconciliation  
Object: citation-contract map `WO-1 face-level CK` versus `WO-5 cell-level phyllotaxis framing`. Bridges `phyllotaxis.tex:159-161`, `:591-595`. Route: source audit. First step: replace “same way as Caspar-Klug” with “same biology-rung substrate family, different derivational level.”

**SECTION C. Surgical Replacements**
- At `biology-rung-bioelectric.tex:205` replace the paragraph beginning `The $2I$-orbit structure of $\mathcal{G}$ has five vertex orbits` through line 209 with:  
  `Build B_orbits enumerates the induced left-$2I$ action on the 600 tetrahedral cells of $\mathcal{G}$ and supplies the orbit partition used below. Conditional on the B_orbits certificate (five orbits of size $120$ and an equivariant face-sharing quotient), the quotient graph $\mathcal{G}/2I$ has five vertices with edge weights determined by $2I$-equivariant cell adjacencies.`
- At `biology-rung-bioelectric.tex:318` replace `Explicit diagonalisation (~$5 \times 5$ matrix in the orbit basis; straightforward once $\mathcal{G}/2I$ is constructed).` with:  
  `Build B_modes diagonalises the certified operator: first the B_orbits weighted quotient for orbit-constant modes, and then the full $600\times600$ cell Laplacian with $2I/A_5$ character projectors for nontrivial irrep content.`
- At `biology-rung-bioelectric.tex:335` replace `\cite{PietakLevin2016} reports the pre-gene-expression voltage maps.` with:  
  `\cite{VandenbergLevin2011} reports the pre-gene-expression Xenopus voltage/pH regionalisation; \cite{PietakLevin2016} supplies the BETSE simulation framework for downstream modelling.`
- At `biology-rung-bioelectric.tex:372` replace `\cite[WO-BIOLOGY-RUNG-006-DMN-BRIDGE]{CascadeBio}` with `\texttt{papers/biology-rung/WO-BIOLOGY-RUNG-006-DMN-BRIDGE.md}`.
- At `biology-rung-bioelectric.tex:413` replace the bullet claiming the 5-orbit decomposition is imported from WO-1 R.0 with:  
  `Build B_orbits supplies the cell-orbit certificate; WO-1 catalogue R.0 supplies only the shared $2I/A_5$ substrate and face-representation convention.`
- At `biology-rung-tubulin.tex:151` replace the `13-dimensional adjacency structure ... T_PH_1` paragraph with a paragraph importing `T_meta ~= Z[phi]^2` and naming `B_tmt13_routeK/B_tmeta_routeQ` as the required 13-selector build.
- At `biology-rung-tubulin.tex:182` replace D.1c with primitive non-uniform character language; current “no proper subgroup acts trivially on any non-zero subspace” conflicts with the trivial character.
- At `biology-rung-tubulin.tex:205` replace the primality proof sentence with:  
  `For $k=1,\ldots,12$, $\gcd(k,13)=1$, so $\chi_k(g)=e^{2\pi i k/13}$ has kernel $\{e\}$ and order $13$ in $\widehat C_{13}$.`
- At `biology-rung-tubulin.tex:299` replace `subsequently refined by cryo-EM~\cite{Prota2014}` with taxane-site citations, e.g. `located/refined in taxol-bound electron-crystallographic models~\cite{NogalesWolfDowning1995,LoweNogalesDowning2001,Snyder2001}`.
- At `biology-rung-tubulin.tex:496` keep Prota only if the parenthetical says: `Laulimalide/peloruside A bind a unique non-taxane MSA site on beta-tubulin; not direct taxane-site-pocket support.`
- At `biology-rung-amyloid.tex:259` after `M \cdot \theta = 360^{\circ}` add the `B_crossover` generalized condition for `C_n`: `M\theta \in (360^{\circ}/n)\mathbb Z`, with current D.3 explicitly the `n=1` full-orientation case.
- At `biology-rung-phyllotaxis.tex:159` replace “in the same substrate level as Caspar--Klug triangulation” with:  
  `in the same biology-rung programme family as Caspar--Klug triangulation, while differing in derivational level: WO-1 is face-level Eisenstein arithmetic, whereas WO-5 is cell/helix-level substrate framing.`
- At `biology-rung-phyllotaxis.tex:591` replace the bullet comparing phyllotaxis to CK/DNA with the same distinction: WO-1 face-level, WO-5 decagram/cell-level framing, B2 DNA vertex-decagram.

**SECTION D. Route Q vs Route K**
Route Q: `T_meta -> 13 selector`. Current sources do not supply this. `T_meta = Z[phi]^2` is rank-2 phason/matching data, and local meta-layer text explicitly says reduction to photon/gauge/polarisation requires further descent: `cascade-meta-layer-theorem.md:202-210`. A new descent functor is required.

Route K: `13 = closed H4 vertex neighborhood = 12 + 1`. This is locally available and sim-closeable from the 600-cell degree-12 graph: `src/vfd_core/geometry/sixhundred_cell.py:34-43`, `:137-144`; `cascade-phase-tmt1-closure.md:96-111`. This is the best WO-3 closure path.

**SECTION F. Top 3 Next Builds**
1. `B_orbits + B_modes_full` at `bioelectric.tex:205-209`, `:318-322`, `:413-416`. This closes the largest WO-4 gap and decides whether the 5-attractor story has a real spectral object.
2. `B_crossover` at `amyloid.tex:255-274` plus `derivation-amyloid.md:50-56`. This resolves the exact-360 versus modulo-`C_n` contradiction with a finite enumeration.
3. `B_tmt13_routeK + B_selector_formal` at `tubulin.tex:149-186`, `:191-249`. This repairs WO-3’s main theorem by replacing the stale T_PH_1 import with a concrete 13-selector source and a correct character-theoretic selector definition.

**SECTION G. Field-Aligned Next-Domain Candidates**
1. Flagellar / basal-body `C_11` and symmetry mismatch. Strong fit: recent cryo-EM reports FliF MS ring 34 subunits with 23-fold and 11-fold subsymmetries: https://pmc.ncbi.nlm.nih.gov/articles/PMC8270960/. Sim: cyclic selector comparison `C_11` vs `C_13`.
2. Collagen triple helix. Strong biological fit and clean `C_3` route through 2I’s 3-fold stabilisers. Literature anchor: collagen triple helix is three PPII strands in a right-handed superhelix with 10/3 symmetry: https://pmc.ncbi.nlm.nih.gov/articles/PMC2846778/
3. Centriole 9-fold / SAS-6 cartwheel. Excellent data and falsifiability; weaker cascade fit because 9 is not a native 2I count except via `3^2` representation multiplicity. Anchor: https://pmc.ncbi.nlm.nih.gov/articles/PMC3089914/
4. Chlorophyll / porphyrin tetrapyrrole. Clean `C_4` chemistry target, strong data, but more chemistry-rung than biology-rung. Anchor: https://pmc.ncbi.nlm.nih.gov/articles/PMC9919320/
5. Ribosomal small subunit domains. Data-rich but symmetry is less clean; better as a later “domain-radiation” build than immediate sim-close target. Anchor: https://www.nature.com/articles/srep20885

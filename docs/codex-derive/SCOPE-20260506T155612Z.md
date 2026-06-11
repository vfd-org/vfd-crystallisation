No files edited.

**SECTION A. Insight / External Content Relevance**
Already in cascade papers / repo:
- Paper 1 supplies the setup Paper 3 should cite: \(V_{600}=2I\) coordinates and closure [bekenstein-incidence.tex:119], \(G=2I\) [bekenstein-incidence.tex:158], \(T_\tau\)-cycles [bekenstein-incidence.tex:162], K-multiset [bekenstein-incidence.tex:182], \(H=\Dic_5\) [bekenstein-incidence.tex:193], and \(V_{24}\) as the \(\sigma\)-fixed sublattice [bekenstein-incidence.tex:278].
- Paper 1 is also the correction anchor: non-bulk **right** cosets \(Hg\) are whole \(T_\tau\)-cycle pairs \(K=52+K=20\), while non-bulk left cosets \(gH\) contain two vertices from each non-bulk cycle [bekenstein-incidence.tex:218]. \(H\) is self-normalizing and non-normal [bekenstein-incidence.tex:257].
- Shared code agrees: `left_cosets` says non-bulk left cosets are not whole cycle unions and \(H\) is non-normal [group.py:137]; `right_cosets` is the whole-cycle carrier [group.py:170]; `dic5_is_normal` returns false [group.py:200].
- Current τ infrastructure only loads a static map [tau_sigma.py:1] and verifies P1-P4 only [tau_sigma.py:40]. Tests mirror that limited scope [test_tau_sigma.py:12]. Data claims phase `(0,0,0,0,0)` and antipodal compatibility [tau_sigma_canonical.txt:1].
- Block notes give the lineage: E8/icosian lattice setup [block3a_e8_icosian_lattice.py:1], parity-flip route [block3b_parity_flip_tau_sigma.py:1], reflection obstruction [block3c_e8_reflection_obstruction.py:1], 100K phase search [block3d_coset_swap_search.py:7], σ-projection refinements [block3e_sigma_projection_canonical.py:1], [block3f_sigma_projection_coset_constrained.py:1], [block3g_VFD_canonical_tau_sigma.py:1], and symmetric phase filter [block3h_VFD_canonical_filter.py:1].
- Classical references already available: Conway-Sloane/Coxeter/Humphreys/Moody-Patera in Paper 1 bib [references.bib:43]; Conway-Sloane/Elkies/Humphreys in shared bib [references-shared.bib:125].

Only in `insight.md` or external/prior-session material:
- E8 double-cover context: \(240/120=2\) and two 600-cell copies [insight.md:47], [insight.md:176]. Useful only as background for §3, not needed for the pure τ theorem.
- Pentagonal-holonomy idea is a separate possible dynamical object, not a Paper 3 dependency [insight.md:830], with proposed \(Z[\phi]^\times\)-valued cocycle [insight.md:878].
- QMS-3 / god-prime material [insight.md:664] is out of scope for Paper 3.

**SECTION B. Priority Gaps To Close The Task**
B1. Right-coset carrier lemma  
Object: \(\rho_R:G\to H\backslash G\), \(v\mapsto Hv\), with \(G=2I\), \(H=\Dic_5\).  
Bridges: Paper 1 setup to Paper 3 construction.  
Route: already in Paper 1 + shared code.  
First step: state lemma: every non-bulk right coset \(Hg\) is one \(K=52\) \(T_\tau\)-cycle plus one \(K=20\) cycle; left cosets are not the carrier.

B2. Trace metric normalization  
Object: \(b_{\mathrm{tr}}:\mathbb H_K\times\mathbb H_K\to\mathbb Q\), \(b_{\mathrm{tr}}(x,y)=\operatorname{Tr}_{K/\mathbb Q}\operatorname{Re}(x\bar y)\).  
Bridges: σ-projection wording to exact verification.  
Route: classical icosian/E8 lattice literature + Block 3a.  
First step: define one `trace_score` in `verify.py`; do not rely directly on `vfd_v600.icosian.trace_inner`, which returns a \(Q(\sqrt5)\) pair [icosian.py:94].

B3. Literal per-vertex σ-projection theorem  
Object: \(M_v=\arg\max_{u\in Hg(v)\cap C_{\mathrm{opp}}(v)} b_{\mathrm{tr}}(\sigma v,u)\).  
Bridges: §4 definition to §5 theorem.  
Route: new derivation.  
First step: build exact max tables for all 100 boundary vertices. Diagnostic: with current right-coset carrier and trace score, the loaded canonical map misses the literal forward max for 80/100 boundary vertices, so this theorem needs a corrected score, candidate pool, or gauge argument before being used.

B4. Safer Route K: cycle-phase σ-projection filter  
Object: for a right coset pair \(C_{52}=(v_k)\), \(C_{20}=(w_k)\), phases \(j\in\mathbb Z/10\), define the \(T_\tau\)-equivariant swap \(v_k\leftrightarrow w_{j+k}\).  
Bridges: Block 3h to the canonical loaded map.  
Route: alternative route, strongly aligned with existing data.  
First step: prove/verify per coset that phases \(j=0,5\) are exactly the symmetric maximin σ-projection phases; phase \(5\) is the antipodal shift. This yields \(2^5=32\) lifts and the zero-phase canonical representative.

B5. Verification rebuild  
Object: `rebuild_tau_sigma(state) -> list[int]`.  
Bridges: static data to reproducible theorem.  
Route: implementation/verification build.  
First step: enumerate right-coset cycle pairs, compute allowed phases by Route Q if B3 closes or Route K if selected, choose zero phase, compare exactly to `load_tau_sigma()`.

**SECTION C. Reversals / Corrections**
- at `papers/tau-sigma-construction/SCOPE.md:16` replace “unique normal subgroup of order 20” with “self-normalizing, non-normal binary-dihedral subgroup of order 20”.
- at `papers/tau-sigma-construction/SCOPE.md:17` replace “five non-trivial boundary cosets each containing one K=52 cycle and one K=20 cycle” with “five non-trivial right cosets \(Hg\), each containing one whole \(K=52\) cycle and one whole \(K=20\) cycle; left cosets are recorded separately and are not whole-cycle carriers”.
- at `papers/tau-sigma-construction/SCOPE.md:19` replace “v's left coset” with “v's right coset \(Hg\)”.
- at `papers/cosmological-folding-rate/dynamics/TAU_SIGMA_RESULT.md:22` replace “left cosets” with “right cosets”.
- at `papers/cosmological-folding-rate/dynamics/TAU_SIGMA_RESULT.md:12` replace `c \cdot \mathrm{Dic}_5` with `\mathrm{Dic}_5 \cdot c`.

**SECTION D. Route Choice**
Route Q: keep the scoped per-vertex argmax. This needs B3 before drafting §4/§5.  
Route K: define τ by \(T_\tau\)-equivariant right-coset phases selected by symmetric σ-projection/maximin tables. This matches the current canonical map, \(Z_2^5\), and verifier target. Recommended for Claude unless B3 is closed first.  
Route H: pentagonal holonomy from `insight.md` is future/outlook only, not part of Paper 3.

**SECTION E. Acceptance Criteria**
`paper.tex`:
1. Pure math only; no cosmology/BH/Hawking interpretation.
2. Cites Paper 1 for \(V_{600},\Dic_5,V_{24}\), K-classes, and right/left coset distinction.
3. §3 proves/refers to W(H4)/E8 failure: non-isometric vertex permutation required.
4. §4 gives exact construction, pseudocode, and worked example using cycles 2 and 3: cycle 2 `[4,119,81,80,118,5,112,86,87,113]`, cycle 3 `[6,93,59,58,92,7,90,60,61,91]`.
5. §5 theorem proves/verifies involution, fixes \(H\), swaps \(K=52\leftrightarrow20\) inside right cosets, \(T_\tau\)-equivariance, antipodal compatibility.
6. §6 proves/verifies \(Z_2^5\): independent phase \(0\) or \(5\) per non-bulk right coset.

`verify.py`:
1. Builds state from `vfd_v600`, no static-only proof.
2. Rebuilds τ from scratch by selected σ-projection algorithm.
3. Asserts rebuilt map equals `data/tau_sigma_canonical.txt`.
4. Verifies P1-P4 plus right-coset preservation, antipodal compatibility, and \(32=2^5\) phase count.
5. Adds regression check that left cosets are not the whole-cycle carrier.

**SECTION F. Top 3 Next Builds**
1. Coset convention fix: anchors [SCOPE.md:16], [bekenstein-incidence.tex:218], [group.py:137], [group.py:170]. Content: right-coset carrier lemma.
2. Rebuild verifier: anchors [tau_sigma.py:40], [test_tau_sigma.py:12], [block3h_VFD_canonical_filter.py:115]. Content: exact reconstruction and static-map equality.
3. §4/§5 derivation: anchors [block3g_VFD_canonical_tau_sigma.py:3], [block3h_VFD_canonical_filter.py:61], [TAU_SIGMA_RESULT.md:28]. Content: construction, worked example, theorem, \(Z_2^5\).

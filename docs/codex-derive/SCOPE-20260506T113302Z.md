Read-only status: I did not edit or commit files. I read the requested files and inspected the shared tests. Current shared test baseline: `28 passed` with `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 ... -s -p no:cacheprovider`.

**SECTION A. Insight / External Content Relevance**

Already in cascade/programme files:

- Paper 1 is scoped as the lead finite identity: `4 σ-fixed / 16 σ-mobile per Dic_5-coset = 1/4` at [NARRATIVE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/NARRATIVE.md:68>) and as “Paper 1 needs only group theory” at [NARRATIVE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/NARRATIVE.md:60>).
- The intended theorem spine is in [SCOPE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/SCOPE.md:20>): `2I=V_600`, `Dic_5`, `σ`, `V_24`, per-coset `4+16=20`, and dimensionless `1/4`.
- Shared notation already defines `2I`, `V_600`, `Dic_5`, `V_24`, `σ`, and `1/4` at [NOTATION.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/NOTATION.tex:7>).
- Exact arithmetic support exists: `Q(sqrt(5))` Fractions, no floating point in core arithmetic at [icosian.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/icosian.py:1>), and the 120 vertices are built explicitly at [icosian.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/icosian.py:112>).
- Existing tests already cover the main incidence facts at [test_24cell_incidence.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_24cell_incidence.py:25>) and the subgroup/coset facts at [test_dic5_subgroup.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_dic5_subgroup.py:10>).

Only in `insight.md` or external literature:

- `insight.md` contains E8/two-600-cell/fine-structure material at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:47>) and [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:178>). This is not needed for Paper 1.
- God-prime/RH/QMS-3 material at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:592>) and [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:670>) is out of scope.
- Pentagonal holonomy at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:830>) is useful only as a future dynamics route, not Paper 1.
- External citations needed: Bekenstein/Hawking/String/LQG comparison entries are already in [references-shared.bib](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/references-shared.bib:74>); Coxeter/Conway-Sloane/Moody-Patera anchors for 600-cell/24-cell/icosians are at [cascade-algebraic-substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:2247>).

**SECTION B. Priority Gaps To Close**

B1. Coset-side/normality correction.  
Object: subgroup `H=Dic_5 <= G=2I`; left cosets `gH`, right cosets `Hg`. Bridges SCOPE wording to true finite theorem. Route: new exact diagnostic. First step: state no normality is used; verify both sides. Diagnostic found both sides have sigma counts `[4,4,4,4,4,4]`, but `H` is not normal.

B2. `Dic_5` presentation certificate.  
Object: generators `a,b in H` with `a^10=1`, `b^2=a^5=-1`, `bab^{-1}=a^{-1}`. Bridges “bulk subgroup” to actual binary dihedral group. Route: finite derivation plus classical presentation. First step: add this generator search/assertion to `verify.py`.

B3. Exact shell ordering without floats.  
Object: exact comparator on `Q(sqrt(5))` distances. Bridges K-class construction to hostile-review-grade exact arithmetic. Route: new derivation. First step: replace Paper 1 verification’s shell ranking with rational sign comparison for `a+b sqrt(5)`; do not rely on float keys in [group.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/group.py:65>).

B4. `V_24 = Fix(σ)` proof.  
Object: `σ: Q(sqrt(5))^4 -> Q(sqrt(5))^4`, fixed set `F={v in V_600: σ(v)=v}`. Bridges coordinate arithmetic to the 24-cell. Route: classical coordinate proof plus exact enumeration. First step: prove the fixed vertices are the 8 axis points plus 16 half-type points, then cite Coxeter coordinates.

B5. Incidence theorem certificate.  
Object: incidence map `I(C)=|C ∩ F|` on all one-sided cosets. Bridges subgroup/cosets to `4/16`. Route: new exact enumeration. First step: `verify.py` prints a six-row table for `gH` and `Hg`: `size=20`, `fixed=4`, `mobile=16`.

B6. Interpretation firewall.  
Object: definitions `S(C)=|C∩F|`, `A(C)=|C\F|`, coefficient `κ(C)=S(C)/A(C)`. Bridges arithmetic to Bekenstein coefficient without overclaiming physics. Route: alternative structural route. First step: a marked scope box: exact ratio proved; Planck/horizon-radius calibration not proved here, matching [SCOPE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/SCOPE.md:26>).

B7. Reproducibility harness.  
Object: `papers/bekenstein-incidence/verify.py -> exit code 0`. Bridges manuscript to tests. Route: existing shared suite. First step: import `vfd_v600`, run Paper 1 assertions, and document the test command using the shared tests.

**SECTION C. Reversals / Corrections**

- At `papers/bekenstein-incidence/SCOPE.md:21` replace `unique normal subgroup of index 6` with `distinguished index-six binary dihedral subgroup`.
- At `papers/bekenstein-incidence/SCOPE.md:22` replace the current coset theorem sentence with: `For every left coset gDic_5 and every right coset Dic_5g in 2I, the intersection with V_24 has exactly 4 vertices; hence each coset has 4 σ-fixed and 16 σ-mobile vertices. No normality assumption is used.`
- At `papers/bekenstein-incidence/SCOPE.md:42` replace `Proof from |2I| = 120, |Dic_5| = 20, |V₂₄| = 24, transitivity of 2I on V_600` with `Proof by exact Q(sqrt(5)) finite enumeration plus a subgroup/presentation certificate for Dic_5; cardinalities alone do not imply uniform incidence.`
- At `papers/bekenstein-incidence/SCOPE.md:45` replace the PBH corollary section with `Reproducibility and audit: exact verification script, coset incidence table, and shared-test baseline.`
- At `papers/v600-programme/lib/vfd_v600/group.py:94`, if Claude touches infrastructure, replace the docstring claim `left Dic_5-cosets` with `cosets H*g generated by left multiplication by Dic_5; historically named left_cosets`.

**SECTION D. Numbered Work Order For `paper.tex` + `verify.py`**

1. Create `papers/bekenstein-incidence/paper.tex` with title, abstract, and one claim: finite incidence gives `4/16=1/4`.
   Acceptance: abstract contains no cosmology, Hawking spectrum, `τ_σ`, E8 double-cover, god-prime, RH, or ontology claim.

2. Section 1, Introduction.
   Acceptance: cites Bekenstein/Hawking for the coefficient, Strominger-Vafa/LQG only as comparison genre; states this paper proves a finite arithmetic identity.

3. Section 2, Exact Model.
   Definitions: `K=Q(sqrt(5))`, `σ(a+b√5)=a-b√5`, icosian quaternions, `V_600`, Hamilton product, `G=2I`.
   Lemmas: 120 vertices, unit norm, closure under multiplication.
   Acceptance: all definitions match `NOTATION.tex`; no floating approximations appear.

4. Section 3, The Bulk Subgroup.
   Definitions: `T_tau`, 12 cycles, shell index, `K(C)`, `H=(K=72)∪(K=0)`.
   Lemmas: cycles are 12 of length 10; K-multiset `{72:1,0:1,52:5,20:5}`; `|H|=20`; `H` is a subgroup; `H ≅ Dic_5`.
   Acceptance: includes explicit Dic5 presentation certificate or generator lemma.

5. Section 4, Sigma Fixed 24-Cell.
   Definitions: `F=Fix(σ)∩V_600`, `V_24=F`.
   Lemmas: `|F|=24`; fixed set is 8 axis + 16 half-type points; `V_24` is a regular 24-cell.
   Acceptance: cites Coxeter/Conway-Sloane/Moody-Patera via existing bibliography.

6. Section 5, Main Incidence Theorem.
   Theorem: for every left coset `gH`, `|gH∩F|=4`, `|gH\F|=16`; same verified for right cosets `Hg`.
   Lemmas: six cosets partition `G`; non-bulk cosets have one `K=52` and one `K=20` cycle.
   Acceptance: theorem proof uses explicit finite enumeration/certificate, not transitivity/cardinality alone.

7. Section 6, Structural Coefficient.
   Definition: `S(C)=|C∩F|`, `A(C)=|C\F|`.
   Theorem: `S(C)/A(C)=4/16=1/4` for each coset and aggregate boundary `20/80=1/4`.
   Acceptance: clearly marks this as structural coefficient; calibration to physical Planck units remains outside Paper 1.

8. Section 7, Scope.
   Acceptance: marked scope box says exact/unconditional: incidence and ratio; interpretive: entropy/area naming; out of scope: dynamics, Hawking quantum, cosmology, `τ_σ`, physical ontology.

9. Section 8, Comparison.
   Acceptance: one compact comparison table: this paper = finite rational incidence; string theory = brane microstate counting; LQG = spin-network horizon counting. No superiority claim.

10. Appendix A, Verification.
   Acceptance: describes `verify.py`, exact arithmetic, commands, and expected certificate table.

11. Create `papers/bekenstein-incidence/verify.py`.
   Must assert: `|V_600|=120`; closure; `|F|=24`; `|H|=20`; subgroup; Dic5 presentation; six `gH`; six `Hg`; all cosets size 20; all fixed counts 4; all mobile counts 16; ratios `Fraction(1,4)`; aggregate boundary `20/80`.

12. Verification commands.
   Acceptance:
   `PYTHONDONTWRITEBYTECODE=1 python3 papers/bekenstein-incidence/verify.py`
   and
   `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=papers/v600-programme/lib python3 -m pytest -q -s -p no:cacheprovider papers/v600-programme/tests`
   both exit 0.

**SECTION E. Routes**

Route K, recommended: build `H` from `T_tau` cycles and K-classes, then prove incidence. This matches the programme and tests.

Route Q, fallback: define an explicit quaternionic Dic5 subgroup by generators and enumerate cosets directly, bypassing K. This is cleaner if a reader distrusts K as programme-specific.

Route E8/τ_sigma: do not use in Paper 1. It adds surface area and is assigned to later papers.

Route 2T/Schläfli: do not use as theorem support. Existing substrate text warns the `2I/2T` 24-cell coset language is related but not needed for the theorem at [cascade-algebraic-substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:918>).

**SECTION F. Top 3 Next Builds**

1. `paper.tex` math spine at [SCOPE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/SCOPE.md:37>): implement Sections 2-6 as definitions/lemmas/theorems above.

2. `verify.py` at [ORCHESTRATION.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/ORCHESTRATION.md:79>): exact finite certificate, including both coset sides and Dic5 presentation.

3. Surgical wording fixes at [SCOPE.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/SCOPE.md:21>) and [group.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/group.py:94>): remove normality/left-right ambiguity before drafting.

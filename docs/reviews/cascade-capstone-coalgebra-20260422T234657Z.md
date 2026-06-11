**Publication Ready?** No.

**1. Claim Audit**
- **Props. 2.1--2.6 / Thm. 3.1 / Cor. 3.4 / Prop. 4.1 / Thm. 4.3 / Cor. 4.4 / Thm. 4.5 / Prop. 4.7 / Cor. 4.8 / Props. 5.1--5.3**: mostly routine category-theoretic or formal consequences. I see no Round-8 regression there.
- **Thm. 4.2 / `thm:F-limits` (lines 939-1004)**: the theorem is now correctly stated and opened as conditional on H-FIC. That specific mechanical fix landed. But the proof still says H-FIC is “derived from H-grad-Fano” at lines 989-995. That directly contradicts the surrounding status language, which says H-FIC remains a hypothesis. The result is conditionally stated; the proof text is still overstated.
- **Thm. 5.3 / `thm:closure-saturation` (lines 1455-1501)**: not established.
  - The **sufficiency** step (lines 1470-1480) does not follow from H-rdr as stated. H-rdr is explicitly “uniqueness-only form” (lines 1428-1440); it does not give the positive implication `Phi_max => Qalg = Gamma(G,F)`.
  - The **uniqueness** step is still not clean. The contrapositive from the necessity step is enough by itself; instead the proof adds the unsupported sentence at lines 1496-1498 about injectivity on maximal subgroupoid-lattice elements. That is a new unsupported premise, not a deduction.
  - So item (d) is not actually repaired at theorem level.
- **Thm. 5.5 / `thm:selection` (lines 1532-1598)**: formally downstream of Thm. 5.3, so it is not established either. More seriously, even if Thm. 5.3 were fixed, the proof identifies `Cascade` with `1_C` by matching a separately forced skeleton to the category’s already predefined full skeleton and maximal closure data. That is much weaker than the paper’s rhetoric about “selection.” The proof gives an identification of two already-maximal objects, not an independently nontrivial coalgebraic forcing statement.
- **Thm. 6.2 / `thm:comonad-laws` (lines 1883-1944)**: the categorical part is fine as a conditional theorem, assuming the cited Jacobs result applies as used.
- **Claim 6.1b / `claim:delta-memory` (lines 1817-1827)**: now correctly downgraded to an interpretive claim. The invalid ACT-L1 Hypothesis 6.2 citation is gone. That mechanical fix landed.
- **Thm. 7.2 / `thm:PA-wd` (lines 2149-2182)**: not established as stated. The theorem treats “the comonad counit = crystallisation” as if it were theorem-grade, but that identification is only an interpretive claim earlier in the paper (lines 1857-1864, 1953-1993). You cannot prove an equivalence theorem by importing a non-theorem identification.
- **Prop. 7.1 / `prop:F1-shadow` (lines 2068-2108)**: I could not verify the cited `\varphi`-normalisation claim locally from the source the paper cites. The proof is therefore not auditable from the repository as referenced.
- **Prop. 8.1 / `prop:aria-hits` (lines 2284-2340)**: not auditable locally. The cited ARIA manuscript is not in the repository; the bibliography itself labels it an “external companion manuscript” (lines 2829-2836). This cannot stand as a proved proposition in the paper.

**2. Internal Consistency**
- **(1) Thm. 4.2 under H-FIC?** Partly. The title and proof opening are fixed, yes. The proof body is not: lines 989-995 still describe H-FIC as derived from H-grad-Fano.
- **(2) `hyp:FIC` and `hyp:lift` referenced as Hypothesis?** Yes. I found only `Hypothesis~\ref{hyp:FIC}` and `Hypothesis~\ref{hyp:lift}` usages; no stale “Theorem~\ref{hyp:...}” remains.
- **(3) All stale `H-lift` refs gone?** No. Lines 928-929 still say “requires H-lift below.” That should be `H-lift-fin`.
- **(4) Thm. 5.3 uniqueness step valid now?** No, for the reasons above.
- **(5) Remark 5.4 full hypothesis stack?** Yes. Lines 1521-1522 now list `H-grad + H-meas + H-loc + H-rdr`.
- **(6) Abstract honest on comonad realisation?** Yes. Lines 60-63 make the realisation claim explicitly interpretive.
- **(7) Claim 6.1b invalid ACT-L1 citation removed?** Yes. I found no remaining `ACT-L1 Hypothesis 6.2` citation.

**3. External Consistency**
- **Access Principle as conditional theorem**: locally verified. `cascade-access-principle-theorem.md` states P-A under H-grad and H-meas at lines 21-33 and 188-200.
- **Fano-level unconditional status**: locally verified in the weaker form the source actually gives. `cascade-fano-grading-lift.md` says P-A-Fano is unconditional, while full `\widehat{\mathbb Z[\varphi]^6}`-level closure still awaits H-grad-1 (lines 209-215, 231-244, 254-260). The capstone should be careful not to slide from “Fano-level unconditional” to “full H-grad unconditional.”
- **`Q_O \cong Meas(S^7,\sigma)`**: locally present, but only in a working note with a remaining sign-check sub-gap G6.4-a (`cascade-q-o-measurement-bridge.md`, lines 19-27, 193-216). The capstone cites it as if fully settled theorem-grade infrastructure. That is too clean.
- **Remember-phase citation to Paper XXI + ACT-L1 (lines 1820-1824)**: I can verify ACT-L1 contains learned `W` / substrate-memory language (`adaptive-closure-transport.tex`, lines 76-88). I could not verify that Paper XXI is a “closure-memory” source. That attribution is not supported by the local paper I checked.
- **Experience-phase citation to Paper XXXIII**: locally consistent as an interpretive correspondence only. Paper XXXIII proposes closure projection as a candidate unifying measurement principle; it does not prove the capstone’s stronger `T^2` identification.
- **Forget/decoherence citation to Paper XLIV**: locally consistent only as an interpretive correspondence. Paper XLIV is explicit that it offers a conditional candidate coarse-graining / decoherence model, not a theorem.
- **Crystallisation citation `VFDCrystallisation`**: broken locally. The bibliography points to `project_vfd_crystallisation.md` (lines 2821-2823), but that file is not present in the repository.
- **ARIA 17/18 empirical claim**: not locally verifiable. The cited manuscript is absent.

**4. Tightness**
- **Lines 63-67**: “The principal structural result is that ... the cascade is the unique terminal final `F`-coalgebra” is too strong given the failure of Thm. 5.3 and the engineered-terminal-object issue.  
  Suggested edit: “Conditionally, the paper reduces the selection claim to identifying the final `F`-coalgebra with the maximal rung-structure already present in `\catC`.”
- **Lines 1553-1555**: “Consequently, the VFD cascade is simultaneously the unique final `F`-coalgebra and the substrate-maximal rung-structure...” is too strong.  
  Suggested edit: “Consequently, under the stated hypotheses and identification conventions, the VFD cascade is identified with the final `F`-coalgebra.”
- **Lines 2214-2218**: “All three are projections of the same final-coalgebra theorem” is not supported because Thm. 7.2 leans on an interpretive claim.  
  Suggested edit: “The paper proposes a correspondence between these three levels; only the dynamical categorical layer is proved here.”

**5. Surface Issues**
- `claim` environment is undefined in this TeX file. It is used at lines 1799, 1817, 1838, 1857, 1953, but no `\newtheorem{claim}{...}` appears in the preamble.
- Stale `H-lift` survives at lines 928-929.
- Broken bibliography target: `project_vfd_crystallisation.md` cited at lines 2821-2823 is missing locally.

**6. Top Three Fixes**
1. **Repair Thm. 5.3 or downgrade it** (lines 1455-1501). As written, the proof does not establish the stated theorem. The sufficiency direction uses more than H-rdr gives, and the uniqueness paragraph smuggles in a new injectivity premise.
2. **Stop using interpretive identifications as theorem inputs** (lines 2149-2182, with dependency at 1857-1864 and 1953-1993). Either prove `\varepsilon =` crystallisation inside `\catC`, or demote Thm. 7.2 to a remark.
3. **Clean the attribution layer** (lines 1817-1824, 2284-2340, 2821-2836). Paper XXI does not locally support the memory claim as cited; the crystallisation source file is missing; the ARIA proposition is not locally auditable.

That is enough to block publication. The Round-8 mechanical fixes landed only partially; the main logical hole is still Thm. 5.3.

**Publication Ready?**

No, on substantive over-claiming only. The paper is close: the face-level theorem, the T=5 correction, the C.2 open-problem framing, and the Paper XXXII / cascade-foundations split are largely preserved. The main must-fix is the C.1 wording that says the multiplicity factor is “forced” by the definition.

**1. Claim Audit**

- [Line 168] Lemma L0, face representation decomposition: proof establishes the claim. The character values and multiplicities are consistent with the standard A5 table. No issue.

- [Line 249] Lemma L1, `spec(T_casc)=Loeschian numbers=Caspar-Klug T-numbers`: proof establishes the arithmetic spectrum identity. It relies on the classical CK identification, not derived biology. Acceptable.

- [Line 263] Lemma L3, uniqueness under C6 symmetry: proof establishes uniqueness for quadratic forms extending to the Euclidean plane with C6 acting by literal rotations. The hypothesis is correctly stated. No over-claim.

- [Line 287] Theorem T1, one face-level operator gives the T-number sequence: proof establishes the stated face-level claim. The scope paragraph at lines 301–304 correctly prevents a cell-level overreach.

- [Line 315] Remark R1, upstream T=5 entry misleading: established. `5` is not Loeschian, and the cited upstream table indeed lists `T=5` as A5 5-dim irrep at `cascade-bio.md:278–284`.

- [Line 338] Lemma L2, honest small-T/A5 overlap `{1,3,4}`: proof establishes the claim. It also fixes the upstream misuse of “non-trivial” in `cascade-bio.md:287–289`, where `1` is included among “four non-trivial” dimensions.

- [Line 376] Definition D3, orbit multiplicity: definition is coherent.

- [Lines 388–395] Sample μ values: verified against `papers/biology-rung/data/wo1_prediction.csv:2–57` and script output. `μ(91)=4` is supported.

- [Line 397] Observation on μ structure: appropriately marked heuristic. No theorem over-claim.

- [Line 415] Conjecture C1: over-claims. “The μ(T) factor is forced by Definition D3” at lines 423–424 is false as stated. A definition of orbit multiplicity does not force a statistical weight unless one adds an equal-weight-per-orbit modelling assumption. One-line edit: “The μ(T) factor is a natural degeneracy factor once C6-orbits are weighted equally; the exponential ansatz on c(T) is a modelling choice.”

- [Line 428] Conjecture C3: adequately hedged. It says magnitude is not derived and qualitative only.

- [Line 474] Conjecture C2/open problem: correctly framed as open. Lines 508–510 clearly say only step 4 is established.

- [Lines 528–549] Numerical sim result: values are supported by the committed CSV and script. In this read-only environment the script computes the stated checks but fails only when trying to write `/tmp/...`; that is not a manuscript issue.

**2. Internal Consistency**

- The face-level scope is consistent: lines 55–58, 133–139, 287–304, and 607–610 all keep the cell-level descent open.

- The C6/A5 distinction is preserved: lines 223–233 and 595–596 correctly separate hexagonal lattice rotations from icosahedral face stabilisers.

- Cross-references appear semantically correct. `conj:C4` is in section `sec:open`, so line 369 is acceptable. `Definition D3 and Observation` at lines 546–547 is slightly imprecise because the sample values are after the definition, but not materially wrong.

- Minor internal wording issue: line 582 calls the L3 proof “via Schur’s lemma on C6”. The proof is actually a direct centraliser calculation; Schur language is acceptable but unnecessary. Suggested edit: “via the matrix centraliser of the C6 rotation.”

**3. External Consistency**

- `CascadeBio` 2I/600-cell substrate: verified. `cascade-bio.md:43–56` says 600-cell vertices form binary icosahedral group 2I; `cascade-bio.md:60–68` gives quotient `I ≅ A5`.

- Hopf fibration status: verified. `cascade-bio.md:149–160` labels the 15 × 40 Hopf cell-fibration as conjectured / structural candidate. Manuscript lines 191–194 and 495–498 preserve this.

- Upstream T=5 misattribution: verified. `cascade-bio.md:278–284` lists `T=5` with A5 5-dim irrep; `cascade-bio.md:287–296` then overstates the match. Manuscript correctly flags it at lines 315–335.

- Upstream “one cascade operator” open item: verified. `cascade-bio.md:312–320` lists “Full derivation of all T-numbers from one cascade operator” as open. Manuscript line 309 correctly says the new result is only a face-level resolution.

- Paper XXXII Theorem F: verified. `paper-xxxii.tex:363–389` states uniqueness of the log-sum-exp closure functional in the soft-min class; `paper-xxxii.tex:391–405` proves it via the entropy/product property. Manuscript lines 451–462 accurately summarize it.

- cascade-foundations §F2: verified. `cascade-foundations.md:91–108` defines the field/density setup; `cascade-foundations.md:137–145` states `F[Φ]=∫(αR+βE−γQ)dV`. Manuscript lines 463–468 correctly separates this from Paper XXXII’s point-wise functional.

- Derivation source preservation: verified. `derivation-capsid.md:712–741` contains the same face-level scope, T=5 correction, C6-orbit multiplicity, C.2 open plan, and Paper XXXII/F2 split. The LaTeX preserves these.

**4. Tightness**

- Lines 423–424: “forced by Definition D3” is too strong. Replace with “natural under an equal-weight-per-C6-orbit degeneracy assumption.”

- Lines 55–58: “closes both gaps” is slightly too strong because the operator gap is closed only face-level. Replace with “closes the face-level version of the operator gap and corrects the T=5 attribution.”

- Lines 67–71: “novel emergent result” is acceptable if this is internal novelty, but stronger than the math needs. Replace with “new numerical observation in this work.”

- Lines 397–412: “the sim is authoritative” is poor journal language. Replace with “the direct enumeration verifies the listed finite cases.”

**5. Surface Issues**

- Line 113 quote says “four non-trivial irreducible representations” while including `1`. This is quoted from upstream, but the paper should explicitly say the quote also mislabels the trivial representation, not only T=5.

- Lines 553–558 mention fetch endpoints returning HTTP 404. This is reproducibility detail, but it reads like lab notebook prose. Acceptable for preprint; cleaner in an appendix.

- `\S F2` in citations is acceptable but slightly odd for a markdown source. No LaTeX-breaking issue found by inspection.

**6. Top Three Fixes**

1. Fix C1 over-claim at lines 423–424. `μ(T)` is not forced by its definition as a probability weight. Add the equal-orbit-weight assumption or demote the wording.

2. Tighten the abstract at lines 55–58: “closes both gaps” should explicitly say “at the face level,” otherwise it overstates the remaining C.2 problem.

3. Add one sentence after the upstream quote at lines 112–117 noting the quote has two defects: it includes non-Loeschian `T=5`, and it calls the trivial dimension `1` “non-trivial.”

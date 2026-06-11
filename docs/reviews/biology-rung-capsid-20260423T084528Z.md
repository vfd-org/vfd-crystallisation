**Publication-Ready?**

Yes, on substantive math/attribution must-fix items only. Round 7’s remaining abstract-level overclaim has been fixed, the Theorem T.1 scope restriction is now restored where it needed to be, and I do not see a remaining proof-level or attribution-level blocker.

**1. Claim Audit**

- Lines 196-202, Lemma L0: “The \(A_5\) permutation representation on the twenty faces decomposes as \(\mathbf{1}\oplus\mathbf{3}\oplus\mathbf{3}'\oplus\mathbf{4}^{\oplus2}\oplus\mathbf{5}\).” The proof at lines 205-215 does establish the claim, albeit in compressed form: it gives the character-theoretic method and the resulting multiplicities. This is acceptable, though the arithmetic is omitted rather than shown.

- Lines 282-287, Lemma L1: “\(\mathrm{spec}(\Tcasc)=\{\text{positive Loeschian numbers}\}=\) Caspar–Klug \(T\)-values.” The proof at lines 290-322 establishes exactly this, conditional only on standard Eisenstein-integer arithmetic, which is properly cited. No hidden hypothesis is missing.

- Lines 324-329, Lemma L3: uniqueness of \(Q\) among positive-definite quadratic forms on \(\mathbb Z[\omega]\) extending to \(C_6\)-invariant forms on \(\mathbb R^2\). The proof at lines 332-346 establishes exactly that claim. The crucial hypothesis is the extension to a \(C_6\)-invariant form on \(\mathbb R^2\); the paper now states it clearly.

- Lines 348-354, Theorem T1: existence and uniqueness-up-to-scale of the face-level quadratic form whose spectrum is the Caspar–Klug sequence. The proof at lines 357-360 is valid by direct appeal to Definitions D1–D2 and Lemmas L1 and L3. This theorem no longer overclaims: the summary paragraph at lines 371-376 now correctly re-inserts the Lemma L3 hypothesis.

- Lines 382-400, Remark R1: the upstream “\(T=5\leftrightarrow A_5\) 5-dim irrep” entry “is misleading” and “yields no face-level \(T=5\) value in the present model.” This is established. The paper now correctly confines the negation to the present face-level model and does not slide into an empirical “no \(T=5\) capsid exists” claim.

- Lines 406-418, Lemma L2: “\(\{ \text{distinct }A_5\text{ irrep dims}\}\cap\{\text{Loeschians}\le5\}=\{1,3,4\}\).” The proof at lines 421-430 establishes the claim cleanly.

- Lines 468-475, sample values for \(\mu(T)\). These are numerical claims, not proved in-text, but they are properly labelled as directly enumerated. I independently checked the local script/data: \(\mu(49)=3\), \(\mu(91)=4\), and the listed representatives match.

- Lines 625-639, numerical summary: “36 distinct Loeschian \(T\)-values \(\le100\),” “61 distinct \(C_6\)-orbits,” and “\(\mu(91)=4\), the first Loeschian value up to \(T\le100\) with four \(C_6\)-orbits.” All of these check out against the local data/script.

- Lines 477-492, Observation \(\mu\)-structure. This is explicitly marked heuristic and not sold as a theorem. That is the correct status. No proof gap matters because no proof claim is being made.

**2. Internal Consistency**

- The abstract fix is in place. Lines 70-73 now say the \(5\)-dimensional irrep “yields no face-level \(T=5\) value in the present model,” which is consistent with the body at lines 397-403.

- The Theorem T1 scope is now internally consistent. Lines 371-373 explicitly say the theorem isolates the unique face-level quadratic form “among those extending to \(C_6\)-invariant forms on \(\mathbb R^2\).” That restores the Lemma L3 hypothesis instead of pretending to a larger uniqueness statement.

- “Positive Loeschian numbers” is now used consistently where the paper means admissible capsid \(T\)-values: abstract lines 44, 62-69 and intro lines 105-115.

- The paper keeps the two symmetry groups distinct without contradiction: \(A_5\) on faces (lines 256-262) and \(C_6\) on the Eisenstein lattice (lines 263-266). That distinction is maintained thereafter.

- Cross-references are internally coherent. The labels cited in the prose all exist in the file, and the surrounding text matches the referenced content. I do not see a misleading \(\ref\) or \(\eqref\) use.

- Minor non-substantive inconsistency: the paper source lives in `papers/biology-rung-capsid/`, while the reproducibility artefacts are correctly listed under `papers/biology-rung/` at lines 729-746. That is not mathematically inconsistent, but it is a layout mismatch worth clarifying.

**3. External Consistency**

- Lines 46-53 and 130-144 attribute to `CascadeBio` the small-\(T\)/\(A_5\)-irrep observation including \(T=5\). Verified locally at `papers/cascade-derivation/cascade-bio.md`, lines 274-320, especially 287-290 and 316-320. The attribution is accurate.

- Line 174 cites `CascadeBio` \S B3.1 for the alternative \(\omega=e^{2\pi i/3}\) convention. Verified locally at `cascade-bio.md`, lines 257-263. Accurate.

- Lines 219-229 cite `CascadeBio` on the 15-fibre / 40-cell discussion and its conjectural status. Verified locally at `cascade-bio.md`, lines 143-160 and 203-214. Accurate.

- Lines 231-233 cite `CascadeBio` \S 2.1–2.3 for \(2I\) order \(120\) and \(I\cong A_5\) order \(60\). Verified locally at `cascade-bio.md`, lines 43-67. Accurate.

- Lines 368-370 cite `CascadeBio` \S B3.4 for the status-table row “Full derivation of all \(T\)-numbers from one cascade operator” being open. Verified locally at `cascade-bio.md`, lines 316-320. Accurate.

- Lines 519-522 cite `CascadeBio` \S 2.7 for the handedness/chirality thread. Verified locally at `cascade-bio.md`, lines 162-175. Accurate as a citation to a qualitative thread.

- Lines 535-549 summarise Paper XXXII as proving uniqueness of the regularised soft-min closure functional under A1–A3. Verified locally at `papers/paper-xxxii/paper-xxxii.tex`, lines 340-405. The summary is materially accurate.

- Lines 550-556 summarise `CascadeFoundations` F2 as giving \(F[\Phi]=\int(\alpha R+\beta E-\gamma Q)\,dV\), unique up to coefficients under the stated invariances. Verified locally at `papers/cascade-derivation/cascade-foundations.md`, lines 99-160. Accurate.

- The only slight citation imprecision is line 535 calling this “Paper XXXII, \S 4, Theorem F.” The source paper’s theorem is titled “Uniqueness of the closure functional” at lines 363-389; “Theorem F” is an informal label, not the displayed theorem name. That is cosmetic, not substantive.

**4. Tightness**

- Lines 55-57: “isolates the classical Eisenstein norm as the canonical face-level quadratic form…” This is now mostly fine, but “canonical” is still a shade too broad unless the class restriction is kept close by. One-line edit: replace “canonical face-level quadratic form” with “canonical face-level quadratic form within the stated \(C_6\)-invariant class”.

- Lines 75-79 and 631-633: the \(91=7\cdot13\) explanation is correctly labelled “consistent with” and “heuristic reading, not a proved classification theorem.” That is the right level. No tightening needed.

- Lines 293-296 of the cited upstream source are much stronger than warranted; this paper now avoids inheriting that overstatement. Good.

**5. Surface Issues**

- Lines 617-623 and 729-746: the paper should explicitly say that the manuscript source is in `papers/biology-rung-capsid/` but the computational artefacts live in `papers/biology-rung/`. As written, the split is inferable, but needlessly untidy.

- Line 535: “Theorem F” is not the displayed theorem title in Paper XXXII. Use the actual theorem name or just cite the section and theorem statement.

- Lines 205-215: Lemma L0 proof is very compressed. Not wrong, but one displayed inner-product computation would make the paper feel less hand-waved at exactly the point where the upstream \(T=5\) correction relies on representation theory.

**6. Top Three Fixes**

1. Lines 617-623 and 729-746: clarify the repository split between `papers/biology-rung-capsid/` (paper) and `papers/biology-rung/` (artefacts). This is the main remaining editorial ambiguity.

2. Line 535: replace “Theorem F” with the actual source-paper wording, e.g. “the theorem ‘Uniqueness of the closure functional’ in Paper XXXII, §4”. This removes a small attribution sloppiness.

3. Lines 205-215: expand Lemma L0’s proof by one explicit character-inner-product line. The result is correct, but the current proof is thinner than the rest of the paper and invites avoidable skepticism.

On the criterion you asked for, the answer is still: yes. No substantive math or attribution must-fix remains.

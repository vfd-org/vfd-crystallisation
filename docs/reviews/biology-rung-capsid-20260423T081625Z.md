**1. Claim audit**

- `"The $A_5$ permutation representation on the twenty faces decomposes as ... \mathbf{1}\oplus\mathbf{3}\oplus\mathbf{3}'\oplus\mathbf{4}^{\oplus2}\oplus\mathbf{5}"` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:185)). The proof at lines 194-202 is adequate, modulo the standard character table citation. No substantive gap.

- `"\mathrm{spec}(\Tcasc)=\{\text{Loeschian numbers}\}=\text{Caspar--Klug }T\text{-numbers}"` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:266)). Not literally established as written, because the paper earlier defines Loeschian numbers as non-negative integers ([lines 100-103]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:100)), while the spectrum excludes `0` by definition ([line 268]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:268)). The claim becomes correct if you say “positive Loeschian numbers” or “non-zero Eisenstein norms.” As written, it is false on its own definitions.

- `"Let Q ... be any positive-definite quadratic form ... $C_6$-invariant ... Then $Q=c\cdot \Tcasc$"` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:289)). The proof at lines 297-311 establishes exactly that. This is the cleanest argument in the paper.

- `"There exists a face-level quadratic form $\Tcasc$ ... unique up to positive scale ... whose spectrum is exactly the Caspar--Klug $T$-number sequence"` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:313)). Formally this follows from Definition D2 plus Lemmas L1 and L3. The only real issue is inherited from Lemma L1: the “Loeschian”/`0` mismatch. Apart from that, the theorem says what the proof proves.

- `"The upstream $T=5$ entry is misleading"` with the specific reasons at lines 350-360 ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:342)). Supported. `5` is excluded arithmetically, and the identification of the `5`-dimensional irrep as a summand of `\pi_{20}` follows from Lemma L0.

- `"$A_5$ has five irreducible representations with four distinct dimensions ... The Loeschian numbers $\le 5$ are \{1,3,4\}"` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:365)). Same defect as Lemma L1: under the paper’s own definition, `0` is Loeschian. You mean positive Loeschian numbers / admissible positive `T`-values. Fix the wording.

- Numerical claim: sample values `\mu(1)=...=1`, `\mu(7)=...=2`, `\mu(49)=3`, `\mu(91)=4` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:415)). These are not proved in the paper, but they are supported by the local artefact `papers/biology-rung/data/wo1_prediction.csv`, which contains the stated rows for `T=49` and `T=91`, and by `wo1_capsid_predict.py`.

- Numerical claim: `36 distinct Loeschian T-values ≤100`, `61 distinct C_6-orbits`, `\mu(91)=4`, `18` spot checks pass, `11` forbidden-`T` checks pass ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:571)). These are supported by the repository artefacts. They are computational claims, not mathematical proofs, but they are at least reproducible from what is present.

**2. Internal consistency**

- The paper is inconsistent about whether “Loeschian numbers” includes `0`. You define them as non-negative at lines 100-103 and again invoke non-negative integers at lines 277-280, but later identify them with the spectrum on `\Zom\setminus\{0\}` at lines 266-269 and with the small set `\{1,3,4\}` at lines 370-372. This is the main internal mathematical defect.

- The cross-reference structure is otherwise fine. I found no undefined `\ref`/`\eqref`, and the local references point where the prose suggests.

- The distinction between face-level `C_6` and icosahedral face stabiliser `C_3` is now stated consistently ([lines 240-250]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:240)). Round 2’s old confusion is gone.

**3. External consistency**

- `CascadeBio` B3.2 quotation about `"The four smallest viral capsid T-numbers (1,3,4,5)..."` is accurately represented. The offending table entry is at `papers/cascade-derivation/cascade-bio.md` lines 278-291, with `T=5` explicitly listed at line 283.

- `CascadeBio` B3.4 attribution that `"Full derivation of all T-numbers from one cascade operator"` was open is accurate. Verified at `cascade-bio.md` lines 314-320.

- `CascadeBio` B3.1 attribution about the third-root convention is accurate. Verified at `cascade-bio.md` lines 257-263.

- `Paper XXXII, §4, Theorem F` is described accurately. Verified at `papers/paper-xxxii/paper-xxxii.tex` lines 363-405.

- `CascadeFoundations §F2` is described accurately as uniqueness up to coefficients under locality/invariance/minimal-order/scalar-valuedness. Verified at `cascade-foundations.md` lines 137-160.

- The Hopf-fibration citation is sloppier. At lines 209-210 and 530-533 of the preprint you cite `CascadeBio §3.2` as though that section is where the `"structural candidate"/"conjectured"` status is attached. The explicit conjectural language is in `cascade-bio.md` §2.6, lines 149-160. §3.2 discusses why `40` is the fibre size, not the conjectural status. This is an attribution precision error.

**4. Tightness**

- Lines 55-57: `"This paper closes the face-level version of the operator gap"` is too strong. Suggested edit: `This paper identifies a canonical face-level quadratic operator with the Caspar--Klug spectrum; no cell-level descent is proved.`

- Lines 333-336: `"Theorem T1 provides a face-level resolution"` oversells what is actually a normal-form statement plus a classical norm identification. Suggested edit: `Theorem T1 isolates the unique face-level $C_6$-invariant quadratic form with the Caspar--Klug spectrum.`

- Lines 73-74 and 577-579: `"chiral Loeschian prime"` is stronger than your definitions support because that term is nowhere defined. Suggested edit: `where both prime factors admit chiral representatives in the wedge picture`.

**5. Surface issues**

- The `0`/Loeschian ambiguity is not cosmetic; it appears repeatedly and needs a global cleanup.
- `sim` at lines 69 and 563 is journal-hostile diction. Use `script` or `simulation`.
- `\Lcal` is defined at line 23 and never used.
- The paper has no broken internal labels as far as local inspection goes.
- The repo paths cited in the reproducibility section do exist.

**6. Top three fixes**

1. Fix the literal falsehood around Loeschian numbers and `0`.  
   Affects [lines 100-103]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:100), [266-286]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:266), and [365-372]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:365). Write “positive Loeschian numbers” or “non-zero Eisenstein norms” wherever you identify them with admissible `T`-values.

2. Repair the Hopf-fibration attribution.  
   The citations at [lines 209-210]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:209) and [530-533]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:530) point to `CascadeBio §3.2` for a status judgment that actually appears in §2.6.

3. Stop overselling Theorem T1 as if it derived a cascade operator from the 600-cell machinery.  
   The overstatement is concentrated at [lines 55-57]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:55), [141-147]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:141), and [333-336]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:333). What you have shown is a face-level canonical form, not a descent from the cell-level theory.

Publication-ready on substantive math/attribution must-fix items only: **no**. The remaining defects are smaller than the Round 2 blockers, but the `0`/Loeschian mismatch is a literal mathematical error as written, and the Hopf-fibration citation is still not clean.

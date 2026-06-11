Publication-ready on substantive math/attribution only: **yes**. I do **not** see a remaining math/attribution blocker. What remains is tightening and cleanup.

**1. Claim Audit**
- **Lemma L0** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:195)): “The `A_5` permutation representation on the twenty faces decomposes as `1 ⊕ 3 ⊕ 3' ⊕ 4^{⊕2} ⊕ 5`.”  
  The proof at lines 204–212 does establish the claim, albeit tersely. It appeals to the standard `A_5` character table and the stated permutation character. No hidden hypothesis is missing.

- **Lemma L1** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:279)): “`spec(T_casc)` = positive Loeschian numbers = Caspar–Klug `T`-values.”  
  This is now actually proved. The converse direction, previously the soft spot, is written out at lines 309–316: split primes, even powers of inert primes, and powers of the ramified prime `3` are all exhibited as norms. That is enough. The proof is citation-dependent, not self-contained, but that is acceptable here.

- **Lemma L3** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:321)): “Any positive-definite quadratic form on `Z[ω]` extending to a `C_6`-invariant form on `R^2` is a positive scalar multiple of `T_casc`.”  
  Established. The important hypothesis is the extension to a `C_6`-invariant form on `R^2`; without that, uniqueness on the lattice alone would be false. The paper states the hypothesis, so no over-claim.

- **Theorem T1** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:345)): existence/uniqueness of the face-level quadratic form with Caspar–Klug spectrum.  
  Established by L1 + L3. The repeated “face-level only” caveat prevents the usual overreach into cell-level descent.

- **Remark R1** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:379)): upstream `T=5` entry is misleading.  
  Correct. The paper shows both that `5` is not Loeschian and that the `5`-dimensional irrep exists only as a representation-theoretic summand, not as a norm value. This is the right correction.

- **Lemma L2** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:402)): honest overlap is `{1,3,4}`.  
  Established.

- **Numerical claims** ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:617)): “36 distinct Loeschian `T`-values `≤100`,” “61 distinct `C_6`-orbits,” and “`μ(91)=4`, first up to `T≤100`.”  
  Supported by the local CSV/script artefact. I verified the file on disk gives exactly `36`, `61`, `μ(91)=4`, and that `91` is the first value in the computed range with multiplicity `4`. The manuscript now scopes this correctly to the finite computation.

**2. Internal Consistency**
- The `ω = e^{iπ/3}` convention is handled cleanly at lines 168–176, including the reconciliation with the upstream third-root convention. No notation drift later.
- The face-level/cell-level distinction is now consistent throughout: lines 160–166, 360–373, and 521–552 all say the same thing.
- The `A_5`/`C_3` versus lattice-`C_6` distinction is also consistent; the old confusion is gone.
- Static scan found **no unresolved `\ref`/`\eqref` labels**.
- Minor presentational wobble only: the reproducibility artefacts live in `papers/biology-rung/` while the manuscript lives in `papers/biology-rung-capsid/`. That is not inconsistent, but it deserves one explicit sentence.

**3. External Consistency**
- Lines 45–52, 124–157, 379–385, 424–427 cite the upstream small-`T` / `A_5` match in `papers/cascade-derivation/cascade-bio.md`. Verified locally at `B3.2` and `B3.4` ([cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:274), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:312)). The source really does make the incorrect `T=5` claim; this paper is not inventing a straw man.
- Lines 216–230 and 576–579 cite `cascade-bio` for the cell-level biology reading, Hopf-fibre arithmetic `40=8·5`, and the conjectural status of the `15×40` partition. Verified locally ([cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:143), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:203)). The manuscript reports the conjectural status correctly.
- Lines 527–541 attribute the pointwise closure-functional theorem to Paper XXXII. Verified locally ([paper-xxxii.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:363)). The summary is materially accurate.
- Lines 542–548 attribute the field-level `F2` form to `cascade-foundations.md`. Verified locally ([cascade-foundations.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-foundations.md:135)). Again materially accurate.
- Lines 513–514 cite `cascade-bio` §2.7 for the chirality thread. Verified locally ([cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:162)). That source is speculative; this paper correctly keeps the extension as a conjecture.
- I did **not** find an in-repo attribution used by this manuscript that is absent from the cited local source.

**4. Tightness**
- Lines 54–57 are still slightly too self-advertising: “identifies a canonical face-level quadratic form” sounds newer than the math is.  
  One-line edit: “This paper isolates the classical Eisenstein norm as the canonical face-level quadratic form under the stated `C_6`-invariance hypothesis.”
- Lines 394–399 overstate slightly on the empirical side: “does not predict a `T=5` capsid.” The math only rules out `T=5` in this model/classification.  
  One-line edit: “and yields no face-level `T=5` value in the present model.”
- Lines 417–421 are weaker than the paper’s actual support: “Second claim: direct enumeration.” You do not need enumeration there.  
  One-line edit: “Second claim follows from the Loeschian criterion: among positive integers `≤5`, only `1,3,4` avoid an inert prime `p≡2 mod 3` with odd exponent.”

**5. Surface Issues**
- Lines 205–208: the Frobenius inner product is written without complex conjugation. For `A_5` this is harmless because the characters are real, but formally it should be conjugated or the real-valuedness should be stated.
- Lines 540–552 use `point-wise`; standard mathematical English is `pointwise`.
- Line 546: `order-$\le 2$` is ugly prose. Write “order at most `2`.”
- No broken cross-references found.
- No obvious undefined macros found from a static scan.

**6. Top Three Fixes**
1. **Tone down the abstract’s novelty wording** at lines 54–57. The paper is isolating a classical object under a clean hypothesis, not inventing a new quadratic form from whole cloth.
2. **Limit the `T=5` negative claim to the model/math** at lines 394–399. Do not let a referee say you slid from “not a Loeschian value” to an empirical impossibility claim.
3. **Clean the formal sloppiness in the character-inner-product proof** at lines 205–208. It is minor, but it is the one place a hostile algebraist can score an easy point.

On the narrow question you asked: **yes**, this clears the substantive math/attribution bar. I do not see a must-fix blocker on that axis.

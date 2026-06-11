Publication-ready on substantive math/attribution must-fix items only: `yes`.

**1. Claim Audit**
- `Lemma L0` ([lines 194-211]): established. The proof is a standard character-inner-product computation and the stated conclusion matches what the proof claims to do. It would be cleaner to display the actual inner-product values, but there is no obvious over-claim.
- `Lemma L1` ([lines 278-300]): essentially established, but by appeal to classical arithmetic rather than by an internal proof. The statement is correct; the weak point is the citation style at [lines 295-298], especially “the argument is identical.” That is not false, but it is not referee-grade justification unless you give a direct Eisenstein-integer citation or a short proof.
- `Lemma L3` ([lines 302-324]): established. The proof does show that a positive-definite quadratic form on `R^2` invariant under rotation by `π/3` must be a scalar multiple of `|x|^2`. No hidden hypothesis beyond the stated extension to a `C_6`-invariant form on `R^2`.
- `Theorem T1` ([lines 326-339]): established as stated. The proof is just “Definition D2 + Lemmas L1 and L3,” and that is sufficient. The trimmed scope language at [lines 341-354] prevents the previous over-claim.
- `Remark R1` / the `T=5` correction ([lines 360-381]): established. The paper’s argument is enough: `5` is not Loeschian, hence not in `spec(T_casc)`, hence not a Caspar-Klug `T`-value.
- `Lemma L2` ([lines 383-403]): established. The overlap computation is trivial once `L0` and the non-Loeschian status of `2,5` are in place.
- Numerical claims on `μ(T)` ([lines 71-77], [433-440], [591-604]): established as numerical enumeration claims, not as theorems. I verified them against the local CSV/script: `36` Loeschian values `<=100`, `61` total `C_6`-orbits, `μ(49)=3`, `μ(91)=4`, and the listed representatives for `49` and `91` match the local data.
- `Observation` on multiplicity structure ([lines 442-457]): correctly not established as a theorem. The text marks it as heuristic. No over-claim remains there.

**2. Internal Consistency**
- The “positive Loeschian numbers” repair is now consistent across abstract, introduction, `L1`, and `T1` ([lines 54-61], [103-112], [278-283], [326-332]).
- The sixth-root vs third-root convention is handled consistently and explicitly ([lines 167-175]); no notation conflict there.
- The face-level/cell-level distinction is now internally consistent. The paper does not silently smuggle a descent theorem back in after disclaiming it.
- The point-wise `Paper XXXII` object and the field-level `F2` object are kept distinct in §6 ([lines 498-525]); that fixes the older conflation.
- Source-level cross-references appear coherent by inspection: the references to `sec:t5`, `sec:operator`, `sec:open`, `sec:num`, and the lemma/theorem labels point to the intended objects. I did not compile the file, so this is a source audit, not a PDF audit.
- Residual minor mismatch: the heading `Sim output (present)` at [line 580] is out of register with the rest of the paper and with the claimed prose cleanup.

**3. External Consistency**
- `CascadeBio` small-`T` quote and `T=5` misattribution ([lines 128-149], [360-366], [405-408], [650-652]): verified locally against [cascade-bio.md lines 280-296]. The paper quotes the offending claim accurately.
- `CascadeBio` status table / “Full derivation of all T-numbers from one cascade operator = open” ([lines 346-354]): verified against [cascade-bio.md lines 312-324].
- `CascadeBio` §2.6 + §3.2 Hopf-fibration attribution ([lines 217-225], [548-552]): verified. The “structural candidate / conjectured” status is in [cascade-bio.md lines 149-160], and the `40 = 8 × 5` arithmetic is in [lines 203-214]. This paper now cites the right places.
- `CascadeBio` §2.1-2.3 on `2I`, `I=2I/{±1}`, and the 600-cell substrate ([lines 227-229]): verified against [cascade-bio.md lines 43-67].
- `CascadeBio` §2.7 chirality thread ([lines 484-487]): verified as an attribution to an upstream qualitative thread, not as a proved fact, against [cascade-bio.md lines 172-179].
- `CascadeFoundations` `F2` claim ([lines 515-520], [536-540], [669-671]): verified against [cascade-foundations.md lines 102-145, 159-176]. The paper reports it correctly as “unique up to coefficients.”
- `Paper XXXII` Theorem `F` claim ([lines 500-514]): verified against [paper-xxxii.tex lines 363-405]. The summary here is faithful.
- I did not find a local attribution that is invented or materially misquoted.

**4. Tightness**
- [lines 54-56] is still slightly too strong. Edit to: “identifies, within the class of positive-definite quadratic forms extending to `C_6`-invariant forms on `R^2`, a canonical face-level quadratic form”.
- [lines 73-75] overstates the search domain. Edit to: “direct enumeration up to `T<=100` gives `μ(91)=4`, the first value in that enumeration admitting four distinct `C_6`-orbits”.
- [lines 421-430] is too categorical about chirality. Edit to: “We do not quotient by reflection; this treats mirror-related wedge representatives as distinct oriented face-level classes.”
- [lines 494-496] is weaker than the actual analysis in `C2(a)`. Edit to: “The point-wise route via Paper XXXII is ill-posed without an additional lift; the serious open problem is the field-level route.”

**5. Surface Issues**
- [line 580] `Sim output` should go. Use `Enumeration Output` or `Numerical Output`.
- [lines 295-298] needs a direct citation for representability by `h^2+hk+k^2`; the current “parallel Gaussian case” wording is too informal for a paper.
- `laevo/dextro` is nonstandard journal English. Either define it once or replace with `left-handed/right-handed`.
- No obvious undefined macros or broken labels from source inspection. The old unused `\Lcal` issue is gone.

**6. Top Three Fixes**
1. Strengthen `Lemma L1`’s support at [lines 286-299] and the introductory characterisation at [lines 109-112] with a direct Eisenstein-norm theorem citation or a short self-contained proof. The mathematics is standard; the present justification is not.
2. Clarify the status of the reflection/chirality choice in `Definition D3` at [lines 421-430] and in the chirality conjecture at [lines 477-487]. Right now a modelling convention is written too much like a structural consequence.
3. Tighten the numerical prose around `μ(91)` at [lines 71-77] and [593-599], and remove the leftover `Sim` heading at [line 580]. The math is fine; the wording is sloppier than the rest of the draft.

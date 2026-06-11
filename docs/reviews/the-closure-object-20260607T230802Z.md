**1. Claim Audit**

- `Lemma [class number one]` at `:87-95`: acceptable. The cited invariant `(n,d_F,D,N)=(2,5,1,1)` is the standard icosian class-number-one case. No blocker, though the paper relies on an external table rather than proving it.

- `Proposition [recalled from IcosianTriad]` at `:103-115`: partially supported, but not cleanly enough. The target identity now includes `C_2(s)` at `:107-110`, which fixes the prior clean-product overclaim. However `:114` still says the finite checks matched coefficients of the clean product `ζ_K(s)ζ_K(s-1)`, not the corrected product. Also the main paper never states the explicit `C_2(s)` or that it has no critical-line zeros, which is needed later when counting on-line zeros.

- `Result` at `:118-122` for the 24-cell: not established here. “Tested to finite precision” is acceptable language, but putting it in a `Certified Result` theorem environment overstates it. The cited icosian paper does not prove this sub-object claim in the form used here.

- `Proposition` at `:124-133`: established. The proof correctly shows `ζ(s-1)` contributes no zeros on `Re(s)=1/2`. No RH claim is made.

- `Result` at `:134-137` for the `96`-vertex shell: not established here. The local engine simply returns precomputed `L(χ_5)` zeros for this builder; that is a consistency test, not an independent geometric derivation.

- `Result [ζ-boundary]` at `:157-164`: supported as a gate result for this declared candidate. The numerical values match the saved atlas. The scope restriction at `:210-211` is now honest.

- `Result [counting route]` at `:165-172`: mostly fixed. The irrelevant `s-1` shift language is gone and the asymptotic is no longer certified. The ratios `4.7, 3.7, 3.1` are reproducible from the engine zero lists. But `:167-168` should say “in the computed on-line lists” rather than presenting strict excess as a theorem.

- `fitted-map control` at `:175-180`: supported, with the caveat already stated at `:148-150`: provenance is declaration-based, not program analysis.

- `GUE control` at `:181-189`: fixed. This is now one seeded control instance, not a theorem about GUE operators.

**2. Internal Consistency**

- The target file now states the local-2 factor honestly in the abstract, claim paragraph, proposition, boundary section, table, scope, and bibliography: `:34-35`, `:62-63`, `:107-110`, `:141-142`, `:197`, `:210-211`, `:253-254`.

- Remaining inconsistency: `:114` still describes finite checks against the clean product, while the claimed identity is product times `C_2(s)`.

- `:117` says “The two Galois components ... carry the two factors” of Dedekind factorisation. That is stronger than the definitions establish. The paper has a 24-cell subset and a 96-vertex shell, but no theorem here decomposes the theta/L-function by those subsets.

- Cross-references resolve coherently. I found no broken `\ref`/`\eqref`.

- The physics wall is clear: `:54-59`, `:213-214`, `:227-232`, and `:237-245` keep it interpretive and non-load-bearing.

**3. External Consistency**

- `IcosianTriad`: verified locally in `release-bundles/icosian-triad-v600/papers/01-icosian-triad/icosian-triad.tex`. The theorem at lines `713-724` states  
  `L(Θ_I,s)=ζ_K(s)ζ_K(s-1)C_2(s)`, and the README/CHANGELOG also include `C_2(s)`. Fixed.

- But the same bundle still has stale/inconsistent supporting text: `docs/FINDINGS.md:193-196` and `:227` omit `C_2(s)` before later adding it at `:209-210`. The sim output compares against the clean product, not the corrected product. This is a documentation/support mismatch.

- The 24-cell and `φ`-shell positive rows are not verified in `IcosianTriad` as theorem-grade claims. In `vfd_math_engine/run_programme.py`, the builders are literal zero-list returns: `E.RIEMANN`, `sorted(E.RIEMANN+E.LCHI5)`, and `E.LCHI5` at lines `16-18`. That is not independent certification.

- `CIRCLE_TEST.md` supports the fitted-map audit: the least-squares fitting trap is explicitly identified at lines `59-66`.

- `grow_atlas.py` supports the GUE control as a single seeded matrix: seed at line `6`, one Hermitian draw at `8-15`. The current paper’s wording is now appropriately limited.

- `vfd-rh-reformulation.md` supports the physics caveats: status lines `4-11`, construction target `94-102`, falsifiable test `112-123`. This matches Section 5.

**4. Tightness**

- Fixed: local-2 factor is now stated in the target paper and bibliography.

- Fixed: positive table rows now say `consistent`, not `verified/realizes`, at `:196-198`.

- Remaining over-tight wording:
  - `:118` and `:134`: replace `Certified Result` environment for these with `Numerical check` or `Recorded consistency check`.
  - `:117`: replace “carry the two factors” with “are tested against the two factors.”
  - `:167-168`: replace “its on-line zero count strictly exceeds” with “in the computed windows, the combined on-line list exceeds.”
  - `:111-114`: add explicit `C_2(s)` handling and do not say the checks match the clean product without qualification.

**5. Surface Issues**

- `:80-81`: “the ring of Hurwitz units” is wrong wording. Units form a group; Hurwitz quaternions form the order/ring. Suggested: “the Hurwitz unit group.”

- `:19`: `\renewcommand{\Theta}{\vartheta}` is unusual and can confuse readers expecting uppercase theta notation. Not broken, but unnecessary.

- `:109`: “prime `2`” should be “the prime ideal above `2`” or “the inert prime `(2)`.”

- The theoremstyle ordering makes `definition` and `remark` use the default theorem style because `\theoremstyle{definition}` comes after their declarations. Not fatal.

**6. Top Three Fixes**

1. Demote or prove the positive sub-object claims at `:117-137` and table rows `:196-198`. The atlas currently hardcodes target zero lists; it does not certify the 24-cell or `φ`-shell geometry.

2. Repair the local-2 support chain at `:103-115`: state explicit `C_2(s)`, note it contributes no critical-line zeros, and change `:114` so it no longer says the numerical checks match the clean product unqualified.

3. Tighten the counting route at `:165-172`: make it explicitly finite-window/computed-list evidence, not a general theorem about on-line zero density.

**Verdict**

No, this version is not free of publication-blocking errors. The prior wording fixes are mostly in place, and there is no RH claim. But the positive “Certified Result” rows are still stronger than the available support, and the local-2 correction is not consistently reflected in the proof/numerical-support chain.

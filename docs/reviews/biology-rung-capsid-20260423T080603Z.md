**Publication Readiness**

No, but not because of the three round-0 substantive fixes. Those are materially fixed. The remaining must-fix is a smaller but still publication-relevant overstatement/inconsistency around the numerical and reproducibility claims.

**1. Claim Audit**

- Lemma L0, lines 178-184: “The \(A_5\) permutation representation on the twenty faces decomposes as …”  
  Established. The face character values at lines 171-176 are correct for the \(A_5\) action on 20 faces, and the Frobenius calculation supports the stated multiplicities.

- Lemma L1, lines 259-263: “\(\mathrm{spec}(\Tcasc)=\) Loeschian numbers \(=\) Caspar--Klug \(T\)-numbers.”  
  Established, provided “Caspar--Klug \(T\)-numbers” means the arithmetic CK triangulation values \(h^2+hk+k^2\), not empirically observed capsid values. The proof at lines 266-270 is sufficient.

- Lemma L3, lines 273-278: uniqueness under \(C_6\).  
  Established under the stated hypothesis that \(Q\) extends to a real \(C_6\)-invariant quadratic form on \(\mathbb R^2\). The hidden assumption is exactly that extension and full \(C_6\) invariance, but both are stated. No overclaim.

- Theorem T1, lines 297-302: “There exists a face-level operator … uniquely determined up to positive scale … whose spectrum is exactly the CK \(T\)-number sequence.”  
  Established by L1 and L3. The “face-level” qualification is essential and is consistently retained.

- Remark R1, lines 325-345: upstream \(T=5\) entry is misleading.  
  Established. \(5\equiv2\pmod3\) is inert and not Loeschian; L1 excludes it from \(\mathrm{spec}(\Tcasc)\). The correction is sound.

- Lemma L2, lines 348-360: honest overlap is \(\{1,3,4\}\).  
  Established. The proof is brief but adequate.

- Definition D3 and sample values, lines 386-405: \(\mu(T)\) orbit multiplicities.  
  Definition is clear. The listed values agree with the local enumerator and CSV.

- Observation, lines 407-422: heuristic structure for \(\mu(T)\).  
  Acceptable as heuristic. However, the title still says “the sim is authoritative” at line 407, contradicting the stated round-0 tightening. Change it.

- Conjecture C1, lines 425-439: closure-preference weighting.  
  Properly labelled conjectural. The round-0 defect is fixed: the \(\mu(T)\) factor is now explicitly a modelling assumption, not forced by D3.

- Conjecture C3, lines 442-452: chirality asymmetry.  
  Properly labelled qualitative/conjectural. No proof claimed.

- Conjecture C2, lines 488-524: face-level residue from 600-cell closure machinery.  
  Properly open. The paper no longer pretends to prove cell-level descent.

- Numerical claim, lines 551-557: “36 distinct Loeschian \(T\)-values \(\le100\), 61 distinct \(C_6\)-orbits, \(\mu(91)=4\), first Loeschian \(T\) with four orbits.”  
  Verified by the local script output up to \(T\le100\). Since “first” only requires checking \(T<91\), the finite enumeration suffices if the enumeration logic is accepted. But the paper should say “direct enumeration up to \(T=100\)” rather than letting “first” read as a theorem independent of the enumerator.

**2. Internal Consistency**

- Lines 55-57, 75-79, 143-149, 311-314, 488-524: face-level/cell-level distinction is now consistent.

- Lines 120-127 correctly annotate both upstream defects: \(T=5\) is not Loeschian, and dimension \(1\) is trivial. This fixes the round-0 attribution problem.

- Line 407 still says “the sim is authoritative.” This conflicts with the intended tightened language and with lines 420-422, which correctly say direct enumeration verifies listed finite cases.

- Lines 560-561 say spot checks are against “Definition D3 and Observation.” Definition D3 defines \(\mu\) but states no sample values. The values are in the paragraph after D3. Edit to “the sample values following Definition D3 and Observation…”

- Lines 567-573 say the comparison script is not present in-repo. This is false: `papers/biology-rung/scripts/wo1_compare.py` exists, and `papers/biology-rung/data/wo1_comparison.md` exists with `WAITING_FOR_DATA`. The absent object is the observed dataset `wo1_viperdb_observed.csv`, not the comparison script.

- Cross-references appear internally coherent by inspection. I did not find a mismatched `\ref` target.

**3. External Consistency**

- Lines 46-53, 108-127 cite `papers/cascade-derivation/cascade-bio.md`. Verified. The upstream note contains the erroneous B3.2 table at cascade-bio.md lines 274-284 and the “four non-trivial irreducible representations” sentence at lines 287-289.

- Lines 199-206 cite CascadeBio §§3.1-3.2 for 600-cell biology and conjectural Hopf fibration. Verified in substance: cascade-bio.md lines 143-160 label the 15 × 40 Hopf cell-fibration as a structural candidate.

- Lines 208-210 cite CascadeBio §§2.1-2.3 for \(2I\), order 120, and \(A_5\) quotient. Verified at cascade-bio.md lines 43-68.

- Lines 316-320 cite CascadeBio B3.4 for “Full derivation of all T-numbers from one cascade operator” open. Verified at cascade-bio.md line 320.

- Lines 451-452 cite CascadeBio §2.7 for \(2I\) handedness / L-amino-acid thread. Verified at cascade-bio.md lines 162-178. The source itself is speculative/structural, and this paper labels the capsid extension qualitative, which is appropriate.

- Lines 465-476 cite Paper XXXII Theorem F. Verified at `paper-xxxii.tex` lines 363-389. Minor caveat: the capsid summary omits some hypotheses from the theorem class, especially \(R(\delta_i)=0\), `opt in {min,max}`, and additive constants/reparametrisation. Not fatal, but add “with the normalisation and opt convention of Paper XXXII.”

- Lines 477-482 cite CascadeFoundations §F2. Verified at cascade-foundations.md lines 91-155. The statement is accurate if “unique form” is understood as “unique form up to coefficients”; the source explicitly does not fix \(\alpha,\beta,\gamma\).

**4. Tightness**

- Line 407: “Heuristic structure; the sim is authoritative”  
  Replace with: “Heuristic structure; direct enumeration verifies the listed finite cases.”

- Lines 553-555: “The emergent result \(\mu(91)=4\)… This is the first…”  
  Replace with: “Direct enumeration up to \(T\le100\) gives \(\mu(91)=4\), the first listed Loeschian value with four \(C_6\)-orbits.”

- Lines 615-616: “Novel numerical emergence…”  
  Replace with: “New numerical observation in this work…”

- Lines 584-585: “No empirical claim is made…”  
  Good. This is the right strength.

**5. Surface Issues**

- Line 407 still contains the disallowed/tightened phrase “sim is authoritative.”

- Lines 567-573 are factually stale: `wo1_compare.py` is present. Rewrite to say the observed VIPERdb CSV is absent and the comparison report is currently `WAITING_FOR_DATA`.

- Lines 542-547 use correct script/data paths.

- Line 560: “Definition D3” should not be cited as the source of sample-value assertions.

- No obvious undefined macros in the TeX body. `\blacktriangleright` should be covered by `amssymb`.

**6. Top Three Fixes**

1. Fix the stale reproducibility claim at lines 567-573. The comparison script is present; only the observed dataset is absent. This is the most concrete false statement in the paper.

2. Remove “the sim is authoritative” at line 407. It is exactly the kind of overclaim the round-0 pass was supposed to eliminate.

3. Tighten the \(\mu(91)\) wording at lines 553-557 and 615-616 to “direct enumeration up to \(T\le100\)” / “new numerical observation.” The finite check supports the claim, but the current prose still leans too hard rhetorically.

On the substantive math and attribution items from round 0: yes, those are fixed. On publication readiness as a preprint: no, not until the stale script-presence claim and remaining numerical-tone overclaims are corrected.

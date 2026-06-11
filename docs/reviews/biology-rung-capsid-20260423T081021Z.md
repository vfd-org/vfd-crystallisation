Publication-ready on substantive math/attribution must-fix items only: **No**.

**1. Claim Audit**

1. `Lemma ... Decomposition of the face representation` ([biology-rung-capsid.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:179), lines 179-185).  
Claim: the 20-face permutation representation decomposes as `1 ⊕ 3 ⊕ 3' ⊕ 4^{⊕2} ⊕ 5`.  
Assessment: **probably correct, but the proof is only a citation plus “direct computation.”** The statement is standard and I can believe it, but the paper does not actually show the inner-product computation. Not a fatal gap, but it is not proved in a referee-grade self-contained way.

2. `Lemma ... Spectrum of Tcasc = Loeschian numbers` ([...:260]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:260), lines 260-271).  
Claim: `spec(Tcasc)=` the Loeschian numbers.  
Assessment: **established only by appeal to an external arithmetic fact.** The proof is just “this is the Eisenstein norm image.” That is fine if properly sourced, but citing OEIS for a theorem-level equivalence is weak. The claim itself is fine; the proof is not really a proof.

3. `Lemma ... Uniqueness under C6 symmetry` ([...:274]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:274), lines 274-295).  
Claim: every positive-definite quadratic form on `Z[ω]` extending to a `C6`-invariant quadratic form on `R^2` is a positive scalar multiple of `Tcasc`.  
Assessment: **proved as stated.** This is the cleanest argument in the paper.

4. `Theorem ... Face-level T-number sequence from one operator` ([...:298]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:298), lines 298-303).  
Claim: there is an operator `Tcasc`, “uniquely determined up to positive scale by local hexagonal-lattice `C6` symmetry,” whose spectrum is exactly the CK `T`-sequence.  
Assessment: **over-claimed.** The uniqueness proved in Lemma L3 is uniqueness only within the class of positive-definite quadratic forms. The theorem drops that hypothesis and upgrades “quadratic form” to “operator.” That is not what was proved.

5. `Lemma ... Honest small-T / A5 match` ([...:349]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:349), lines 349-368).  
Claim: distinct `A5` irrep dimensions intersect Loeschians `≤5` in `{1,3,4}`.  
Assessment: **established.** This is fine.

6. Numerical claims in `Sample values` ([...:399]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:399), lines 399-405) and `Sim output` ([...:555]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:555), lines 555-568).  
Assessment: **supported by the local CSV/script artefacts.** I verified the present `wo1_prediction.csv` has 36 distinct `T` values, 61 orbit rows, `μ(49)=3`, `μ(91)=4`.  
Caveat: the explanatory language “arising from `91=7·13` where both factors are chiral Loeschian primes” (lines 560-562) is **heuristic**, not a proved classification theorem.

7. `Observation ... direct enumeration verifies the listed finite cases` ([...:408]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:408), lines 408-423).  
Assessment: **now properly labelled heuristic.** This was fixed correctly.

**2. Internal Consistency**

1. The paper still contradicts itself about `wo1_compare.py`.  
Present section: script is “present and operational” and emits `WAITING_FOR_DATA` ([...:578]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:578), lines 578-581).  
Summary section: empirical work is pending “completion of `wo1_compare.py`” ([...:642]( /mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:642), lines 642-644).  
That is stale and wrong.

2. The uniqueness claim is narrower in the formal lemma than in the abstract/introduction/summary.  
Abstract lines 57-62 are careful; introduction lines 136-138 and theorem lines 299-303 are less careful; summary lines 604-606 again overstate. This is a real convergence failure in the paper’s own logical chain.

3. Cross-references: I do not see broken `\ref`s from source inspection. The references used match existing labels. No `\eqref` issues because there are effectively none.

**3. External Consistency**

1. `CascadeBio` B3.2 misstates the small-`T` match, including `T=5`.  
Your citation is accurate. Verified in [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:274), lines 274-291.

2. `CascadeBio` B3.4 says full derivation from one cascade operator is open.  
Your citation is accurate. Verified at [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:312), lines 312-320.

3. `CascadeBio` §§3.1-3.2 / conjectured Hopf fibre structure.  
Your summary that this is conjectural/structural-candidate rather than proved is accurate. Verified at [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:158) and [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:189).

4. `CascadeBio` §2.7 chirality thread.  
Your citation is accurate as attribution. Verified at [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:162).  
But note: the source is itself speculative. You are citing it correctly, not converting it into evidence.

5. `Paper XXXII` Theorem F summary.  
Your expanded hypothesis summary is accurate. Verified at [paper-xxxii.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:363), lines 363-389.

6. `CascadeFoundations` F2 summary.  
Your “unique form up to coefficients” summary is accurate. Verified at [cascade-foundations.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-foundations.md:137), lines 137-159.

I did not find a local attribution claim in this draft that flatly misquotes the cited in-repo source. The attribution problem is not mis-citation now; it is theorem-strength inflation in your own prose.

**4. Tightness**

1. Over-strong: lines 299-303.  
Replace with: “There exists a face-level quadratic form `Tcasc` on `Z[ω]`, unique up to positive scale among positive-definite `C6`-invariant quadratic forms, whose spectrum is exactly the Caspar–Klug `T`-sequence.”

2. Over-strong: lines 604-606.  
Replace with: “Theorem T1: `Tcasc` is the unique positive-definite quadratic form, up to positive scale, with the stated `C6` invariance and Loeschian spectrum.”

3. Slightly too strong: lines 560-562.  
Replace “arising from” with “consistent with the factorisation pattern”.

**5. Surface Issues**

1. Stale internal statement: “completion of `wo1_compare.py`” at lines 642-644 is false.  
2. “sim” in abstract/§6 is too informal for journal prose. Use “enumeration script” or “numerical enumeration.”  
3. OEIS is not an adequate sole citation for the arithmetic characterization in lines 105-107 / Lemma L1. Use a real number-theory source.

**6. Top Three Fixes**

1. **Restrict the uniqueness claim everywhere to the class actually proved.**  
Abstract lines 57-62 are mostly fine; introduction lines 136-138, theorem lines 299-303, and summary lines 604-606 are not. This is the main substantive math issue.

2. **Replace the OEIS-only support for the Loeschian characterization with a proper source, or prove the needed fact.**  
Lines 105-107 and 267-271 are carrying too much weight on too little citation.

3. **Remove the stale claim that empirical work awaits “completion of `wo1_compare.py`.”**  
Lines 642-644 directly contradict lines 578-581. This is not deep mathematics, but it is an obvious credibility wound in a convergence-check draft.

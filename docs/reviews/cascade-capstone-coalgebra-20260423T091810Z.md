**Publication Ready?** No.

**1. Claim Audit**
I am only listing substantive claim failures or over-claims.

- **Theorem 5.3 overclaims relative to the cited H-loc reduction.**  
  Quote: “`The full-access rung-structure ... is the unique rung-structure ... whose query algebra coincides with the full meta-layer section algebra`” ([cascade-capstone-coalgebra.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1498)).  
  Problem: the proof of necessity at lines 1515–1521 uses H-loc as if every strict deficiency `Φ ≠ Φ_max` yields a witness section. But the cited reduction note for H-loc explicitly leaves an unresolved **E8-only deficiency corner case**. So the proof does **not** presently establish the stated biconditional in full generality. Either exclude that case in the theorem statement or prove it.

- **Theorem 5.6 still carries the old H-FIC hypothesis instead of the residual sub-gaps.**  
  Quote: “`Assume Hypothesis~\ref{hyp:FIC} (H-FIC)`” ([...tex:1565](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1565)).  
  Problem: Round 16 says H-FIC has been reduced to `G-FIC-a + G-FIC-b`. The theorem statement, and therefore the paper’s actual main claim, still assumes raw H-FIC. The proof does not use the reduction; it just imports H-FIC. This is not a cosmetic issue. Your status prose and your theorem stack now disagree.

- **Theorem 4.3 / Corollary 4.4 remain stated under H-FIC rather than `G-FIC-a + G-FIC-b`.**  
  Quotes:  
  “`F preserves ω^op-limits, under H-FIC`” ([...tex:962](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:962))  
  “`F satisfies the Adámek hypotheses, under H-FIC`” ([...tex:1029](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1029))  
  Problem: same defect. The reduction is only in remarks. The theorem-grade statement is not updated.

- **Proposition 3.1 is stated at theorem grade, but its proof still contains stale pre-closure caveats.**  
  Quote: “`Observer-rung necessity ... at theorem-grade after G6.4-a closure`” ([...tex:602](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:602)).  
  But the proof still says: “`closing G6.4-a would lift the argument to theorem grade`” ([...tex:636](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:636)).  
  That is an unresolved contradiction inside the proof of the claim itself.

- **The source-audit claim about what the headline theorems require is false as written.**  
  Quote: “`the paper's headline theorems do not require the full P-A to be proved in its strongest form, only the Fano-level version which is unconditional`” ([...tex:256](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:256)).  
  This is contradicted by your own net remark at lines 301–304, which correctly says Theorems 5.3/5.6 inherit full `\widehat{\Z[\varphi]^6}`-level conditionality through P-A. The stronger line at 256–261 is an over-claim.

**2. Internal Consistency**
- **The hidden-hypothesis problem is not consistently acknowledged.**  
  Lines 301–304 correctly say Theorems 5.3 and 5.6 inherit full `\widehat{\Z[\varphi]^6}` conditionality from P-A. Lines 256–261 say the opposite. One of these must go. As written, the paper gives both answers.

- **Round-16 status is not integrated into §3 and §9.**  
  Line 1112 still lists the operative stack as raw `H-FIC, H-lift-fin, H-loc, H-rdr` ([...tex:1112](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1112)). That is stale: H-rdr is closed; H-loc/H-FIC are reduced.  
  Lines 2453–2463 still describe H-FIC via the **old graded-groupoid route** ([...tex:2453](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2453)), contradicting the new support-projection reduction in lines 939–959.

- **Your prose says H-lift-fin is the only remaining capstone-introduced hypothesis; your theorem statements say otherwise.**  
  The table/net remark/conclusion say that. Theorems 4.3, 4.4, and 5.6 still assume H-FIC directly. So the answer is not yet consistently “yes”.

- I found no unresolved `\ref`/`\eqref` labels by grep-level inspection.

**3. External Consistency**
Central repository attributions:

- **Verified:** `CascadeHrdrClosure` supports “H-rdr reduced to P-A” and explicitly says the reduction inherits P-A’s `{H-grad, H-meas}` conditionality. Good attribution.  
  Problem is not the citation; problem is that the capstone still understates the inherited full-`\widehat{\Z[\varphi]^6}` dependency elsewhere.

- **Verified with caveat:** `CascadeG64aClosure` supports “386 cases, all pass” and upgrades the multiplicative-compatibility step behind `Q_O ≅ Meas(S^7,\sigma)`. Good.

- **Not fully verified as used:** `CascadeHlocClosure` does reduce H-loc to `G-loc-a`, but it also explicitly leaves the **E8-only deficiency** case unresolved. The capstone uses it as if Theorem 5.3 necessity were fully covered. That attribution is too strong.

- **Verified as reduction, not closure:** `CascadeHFICClosure` supports “reduced to G-FIC-a + G-FIC-b” and explicitly says both are still lemma-grade residuals. Good attribution.  
  But the capstone’s theorem statements still behave as though H-FIC itself is the active assumption. The attribution and theorem stack are out of sync.

- **Verified:** `CascadeAccessPrinciple` states Theorem P-A conditional on H-grad and H-meas. It does **not** support any suggestion that the capstone’s headline theorems only need Fano-level unconditionality.

- **Verified:** `CascadeCompletenessAudit` / `cascade-foundations.md` support the 7-rung FAN and F3/F4 forcing.

- **Appropriately weakened:** the XXI/XXXI/XXXIII/XLIV/ACT/crystallisation correspondences are not proved by those papers as categorical identifications. The capstone’s present “interpretive claim” framing is the correct one.

**4. Tightness**
One-line edits:

- Replace lines 256–261 with:  
  “Theorem 5.3 and Theorem 5.6 still inherit full `\widehat{\Z[\varphi]^6}`-level conditionality through P-A; Fano-level unconditionality suffices only for the observer-rung measurement statements.”

- Replace theorems at lines 962 and 1565 with assumptions on `G-FIC-a + G-FIC-b`, or explicitly state “by Remark 4.x, H-FIC is reduced to G-FIC-a + G-FIC-b, which are the actual residual assumptions.”

- Replace lines 1488–1504 with either a theorem conditional on `G-loc-a` **plus** an explicit exclusion/proof of the E8-only deficiency case, or weaken the necessity claim.

- Remove or rewrite lines 636–637; they are stale.

**5. Surface Issues**
- `\Phi_{\min}` appears in examples ([...tex:774](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:774), [...tex:1056](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1056)) without being defined.
- §9 H-FIC item is stale and cites the wrong derivation route.
- Proof of Proposition 3.1 still contains pre-closure language inconsistent with its updated theorem-grade status.

**6. Top Three Fixes**
1. **Fix Theorem 5.3’s necessity claim** ([...tex:1488](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1488)).  
   Either prove the E8-only deficiency case or narrow the theorem. As written, the cited H-loc reduction does not establish the full biconditional.

2. **Resolve the full-`\widehat{\Z[\varphi]^6}` conditionality contradiction** ([...tex:256](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:256) vs [...tex:301](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:301)).  
   Right now the paper simultaneously says the headline theorems do and do not inherit the full P-A conditionality.

3. **Actually integrate the H-FIC reduction into theorem-grade statements and §9** ([...tex:962](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:962), [...tex:1565](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1565), [...tex:2453](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2453)).  
   Until you do that, “H-lift-fin is the only unreduced capstone-introduced hypothesis” is not true in the paper’s operative theorem stack.

**Direct answers to your five checks**
1. All four closure integrations consistent across abstract/§1.8/§3/§5/§9/conclusion? **No.**
2. H-lift-fin correctly remaining as the single capstone-introduced hypothesis not reduced? **No, not consistently; theorem statements still carry H-FIC.**
3. Residual sub-gap list accurate? **Yes in prose: `G-loc-a`, `G-FIC-a`, `G-FIC-b`. No in theorem integration.**
4. Hidden-hypothesis problem now acknowledged correctly? **No; one passage still denies it.**
5. Remaining stale pre-closure language? **Yes: Proposition 3.1 proof, §3 technical-scope stack, and §9 H-FIC item.**

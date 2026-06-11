**Publication Ready?**

No.

**1. Claim Audit**

Within the Round-9 target zone:

- **Fail.** “`\begin{theorem}[$F$ preserves \omega^{\mathrm{op}}-limits, under H-FIC]`” at [cascade-capstone-coalgebra.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:941).  
  The proof body still says at lines [991-998](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:991) that H-FIC-O and H-FIC-\(E_8\) are “derived from H-grad-Fano.” That is exactly the unsupported derivation the revision was supposed to remove. If H-FIC is a named hypothesis, the proof may use it; it may not quietly re-upgrade it to a derived consequence.

- **Pass, with over-assumption.** “`\begin{theorem}[Closure-data saturation; conditional on H-grad, H-meas, H-loc, H-rdr]`” at [1456-1468](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1456).  
  The rewritten proof now does what it says: sufficiency from H-rdr at [1471-1473](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1471), necessity from Lemma 5.2 / H-loc at [1475-1481](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1475), uniqueness from the biconditional at [1483-1488](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1483).  
  But H-grad and H-meas are not used in the proof. Either explain where they enter, or remove them from the theorem statement.

- **Pass mathematically; fail in surrounding metadata.** H-rdr is stated as sufficiency-only at [1430-1441](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1430), and Theorem 5.3 uses it that way. That fix is real. The inconsistency is elsewhere.

- **Fail.** “`\begin{remark}[P-A as comonad counit well-definedness ...]`” at [2137-2155](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2137).  
  The demotion from theorem to remark is not clean, because later text still cites it as a theorem at [2163](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2163) and [2176](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2176). That is not a cosmetic issue; it re-inflates a non-theorem into theorem-grade support.

- **Fail by source-grade inflation.** “Observer-rung necessity; \(\Qalg_O \cong \mathrm{Meas}(S^7,\sigma)\)” at [582-612](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:582).  
  The proof says the bridge is “established as a theorem” in `CascadeQOBridge` at [598-600](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:598). The cited local source explicitly labels itself “WORKING NOTE, lemma-grade” and leaves sub-gap G6.4-a open. The stated proof therefore overstates the imported support.

**2. Internal Consistency**

- H-rdr is still described as “uniqueness-only form” in the status table at [269](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:269), in the main theorem hypotheses at [1526](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1526), and in open items at [2688](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2688). The hypothesis itself is sufficiency-only. This is a genuine contradiction.

- The demoted P-A/counit statement is a `remark` with label `thm:PA-wd` at [2140](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2140), then cited as “Theorem” at [2163](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2163) and [2176](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2176). The demotion is therefore not internally complete.

- The H-FIC remark at [913-939](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:913) correctly says the earlier derivation claim was premature; the theorem proof at [991-998](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:991) contradicts that.

**3. External Consistency**

Checked against local sources:

- **Not verified; contradicted by source.** At [2159-2164](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2159), the paper says the headline theorems use only the sufficiency direction of P-A, “which is unconditional” from `cascade-observer-query-algebra.md` §4.2.  
  The cited source does not establish that as a theorem. It explicitly keeps P-A as a conjecture and labels §4.2 as a “direct sketch of sufficiency”; see `cascade-observer-query-algebra.md` lines 188 and 202.

- **Not verified at theorem grade.** At [598-600](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:598), the paper treats `cascade-q-o-measurement-bridge.md` as theorem-grade closure.  
  The local file says “WORKING NOTE, lemma-grade” and leaves G6.4-a open; see lines 1-3 and 193-195 of that source. You may cite it as supporting infrastructure, not as a clean closed theorem.

- **Mis-cited source.** “Skeleton forcing; inherited from `CascadeCompletenessAudit`” at [1340-1351](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1340).  
  The cited audit itself says it is “not a new theorem” and that F3/F4 live in `cascade-foundations.md`; see `cascade-completeness-audit.md` lines 31-50 and 381. The attribution is sloppy at best.

- **Verified.** The `VFDCrystallisation` bibliography entry at [2794-2798](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2794) points to files that exist locally, and the crystallisation papers do contain the relevant operator/functional material.

**4. Tightness**

- [991-998](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:991): replace “derived from H-grad-Fano” with “assumed as part of Hypothesis H-FIC.”

- [2159-2164](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2159): replace “the sufficiency direction of P-A, which is unconditional” with “the sufficiency sketch motivating H-rdr; no unconditional theorem is claimed here.”

- [1340-1341](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1340): replace “inherited from `CascadeCompletenessAudit`” with “recorded in `CascadeCompletenessAudit`, with theorem source `cascade-foundations.md`.”

**5. Surface Issues**

- `claim` environment is now defined at [17](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:17). That fix is fine.

- No stale `H-lift` references remain. The remaining instances are `H-lift-fin`.

- The `thm:PA-wd` label on a `remark` is bad hygiene and currently causes downstream theorem mis-citations.

**6. Top Three Fixes**

1. **Purge the reintroduced fake derivation in Theorem 4.2’s proof** at [991-998](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:991).  
   As written, the proof still claims H-FIC is derived from H-grad-Fano.

2. **Stop claiming unconditional P-A sufficiency and finish the Theorem→Remark demotion cleanly** at [2159-2176](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2159).  
   The local source does not give an unconditional theorem there, and the paper still cites the demoted remark as a theorem.

3. **Fix source-grade inflation in imported theorem claims** at [582-600](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:582) and [1340-1351](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1340).  
   `CascadeQOBridge` is not closed theorem-grade, and `CascadeCompletenessAudit` is not the primary theorem source for F3/F4.

**Round-9 verification summary**

1. Thm 4.2 proof body consistent, no “derived” language? **No.**
2. H-rdr now sufficiency-only? **In the hypothesis and Thm 5.3 proof, yes; elsewhere, no.**
3. Thm 5.3 proof now valid on its own stated route? **Yes, essentially.**
4. Thm 7.2 → Remark demotion clean? **No.**
5. No stale `H-lift` refs remaining? **Yes.**
6. `claim` environment now defined? **Yes.**
7. `VFDCrystallisation` bib valid? **Yes.**

Publication ready: **no**.

All capstone line numbers below refer to [cascade-capstone-coalgebra.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1>).

**1. Claim audit**
- **Lines 42-69, 125-155, 2455-2488:** “the VFD cascade is mathematically necessary,” “closes the selection-principle problem,” and the abstract/conclusion-level empirical/comonad claims are overstated. The body still leaves load-bearing assumptions open or mis-propagated.
- **Propositions 2.1–2.6 (lines 345-480):** routine category-structure claims are broadly fine. The product/limit computations by inclusion/intersection are coherent in this concrete category.
- **Theorem 3.1 / Observer-rung necessity (lines 514-544):** only as strong as the bridge note. Acceptable as an imported conditional input; not independently established here.
- **Lemma 3.3 / “$S^7$-coverage at the terminal” (lines 625-662): not established.** The proof uses a stronger statement than the cited source gives: it needs “every morphism in `\Gcal_O` comes from a measurement event and lifts back as that morphism.” The source note proves an algebra isomorphism, not this morphism-level surjectivity.
- **Corollary 3.5 / terminal idempotence (lines 784-800): not established.** It depends on Lemma 3.3.
- **Theorem 4.1 / `F` preserves `\omega^{op}`-limits (lines 863-933): conditionally fine.** The concrete `A ∩ (∩ B_n) = ∩(A ∩ B_n)` argument in lines 1744-1776 is the right repair for the `X × -` step. No objection there. The issue is assumption propagation, not that calculation.
- **Corollary 4.2 and Existence section (lines 935-1178): overclaimed.** `F` preserves `\omega^{op}`-limits only under H-FIC (lines 863-866). But Proposition 4.4 (lines 1079-1087), Theorem 4.7 (lines 1133-1146), and everything downstream are stated unconditionally.
- **Lemma 5.1 / section deficiency from closure-data restriction (lines 1284-1315): not established.** The new retreat in the statement is honest; the proof is not. Minimality and unique ergodicity from M3 do not imply existence of a sheaf section supported on a chosen morphism `\gamma` and nowhere outside `\Gcal_r`.
- **Theorem 5.3 / closure-saturation (lines 1329-1370): not established.** Its necessity step depends on invalid Lemma 5.1 and then quietly strengthens “some section is lost” to “there is a character `\chi` with `\Fcal(\chi)` lost” at lines 1360-1362. That stronger claim is exactly what Remark 5.2 says is *not* being claimed.
- **Theorem 5.6 / selection principle (lines 1399-1445): not established as stated.** It inherits both defects above: hidden H-FIC dependence from Sections 4–5 and the broken necessity argument in Theorem 5.3.
- **Corollaries 5.7–5.10 (lines 1470-1524): not established.** They are downstream of Theorem 5.6.
- **Theorem 6.3 / comonad laws (lines 1729-1790): conditionally fine.** The categorical part is now appropriately separated from the interpretive identification. The repaired product-limit argument is tight enough in this specific `\catC`.
- **Claims 6.1–6.5 (lines 1646-1710, 1799-1815): acceptable only as interpretive claims.** They are not source-level theorems, and the capstone should not speak as if Paper XXXIII or the others already prove those identifications.
- **Theorem 7.2 / `P-A` as counit well-definedness (lines 1995-2028): overclaimed.** It leans on Claim 6.4 (`\varepsilon` as crystallisation), which is explicitly interpretive. So the “equivalent to the statement that the comonad’s observer-localised counit is well-defined” part is not a theorem-grade deduction.
- **Proposition 8.1 / ARIA 17/18 (lines 2130-2186): unverifiable locally.** The cited manuscript is not present in the repository.

**2. Internal consistency**
- **H-FIC is not propagated.** Section 4 correctly states `F` preserves limits only under H-FIC (lines 863-866). Section 5 then uses existence/finality without carrying that assumption (lines 1079-1178, 1399-1412). Open item 5 (lines 2287-2294) even admits the `E_8` commutation lemma is still missing.
- **You simultaneously treat H-FIC as hypothesis and theorem.** Lines 814-832 define it as a hypothesis; lines 858-860 say it is “therefore a theorem under H-grad”; lines 2287-2294 say the `E_8` piece still needs an explicit lemma. Those cannot all stand.
- **G6.1/G6.4 status drifts.** Remark 3.2 says Definition 3.3 removes dependence on G6.1 (lines 615-622). Section 3 discussion calls G6.1 and G6.4 “conjectural” (lines 1015-1018). Open items then say G6.1 is still a prerequisite for Definition 3.3 well-definedness and G6.4 is closed except for G6.4-a (lines 2251-2271). This is internally inconsistent.
- **The abstract/introduction are not honest about conditionality.** The conditional statements only appear later; the front matter still reads as if selection, comonad realisation, and empirical observability are established outright.
- **The theorem/claim boundary is still blurred.** Section 6 correctly separates theorem from interpretation, but Theorem 7.2 re-imports Claim 6.4 as if it were theorem-grade.

**3. External consistency**
- **`CascadeQOBridge`: verified only up to algebra-isomorphism, not your stronger use.** In [cascade-q-o-measurement-bridge.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-q-o-measurement-bridge.md:19>) and [same file](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-q-o-measurement-bridge.md:112>), the note states `Q_O ≅ Meas(S^7,σ)` as an `R`-algebra with involution. It does **not** state the morphism-level groupoid generation claim used in capstone lines 637-652. Also, its own status line calls it a “WORKING NOTE, lemma-grade” at line 3.
- **`CascadeMetaLayer`: verified, but does not support Lemma 5.1’s proof move.** [cascade-meta-layer-theorem.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-meta-layer-theorem.md:175>) gives M3a/b/c/d: minimality, unique ergodicity, linear repetitivity, local-to-global extension of finite-patch assignments. It does **not** give existence of a sheaf section with support concentrated on a chosen morphism.
- **`CascadeAccessPrinciple`: verified as conditional, but not as an H-FIC theorem.** [cascade-access-principle-theorem.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-access-principle-theorem.md:21>) and [same file](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-access-principle-theorem.md:188>) do give Theorem P-A under H-grad and H-meas. They do **not** prove H-FIC-O or H-FIC-`E_8`. In fact line 233 still says the full `\widehat{\mathbb Z[\varphi]^6}`-level form remains conditional on an H-grad sub-gap.
- **`CascadeCompletenessAudit`: verified for the skeleton only.** [cascade-completeness-audit.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-completeness-audit.md:33>) gives the 7-rung forcing and [same file](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-completeness-audit.md:50>) gives the 583 budget. It explicitly says at lines 63-65 that F3+F4 do **not** force the full algebraic/dynamical content. Your skeleton-only use is fine.
- **Paper XXXIII is weaker than your prose suggests.** [paper-xxxiii.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxiii/paper-xxxiii.tex:45>) frames closure projection as a proposed unifying principle, and [same file](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxiii/paper-xxxiii.tex:356>) explicitly says the identifications are “structural, not rigorously derived.” So lines 1679-1692 should remain plainly interpretive.
- **ARIA source not locally verifiable.** The bibliography points to external companion files, but those files are not present in the repo.

**4. Tightness**
- **Abstract, lines 42-58:** too strong.  
  Edit: “We formulate a conditional coalgebraic selection principle for the VFD cascade, with categorical parts proved under H-FIC and identification steps conditional on H-grad/H-meas.”
- **Lemma 3.3 proof, lines 637-642:** too strong.  
  Edit: “The bridge gives an algebra-level correspondence; to conclude morphism-level coverage one needs an explicit lift/surjectivity lemma, which we isolate as an additional assumption.”
- **Theorem 5.3 necessity, lines 1360-1362:** stronger than the math supports.  
  Edit: replace “there is a character `\chi` with `\Fcal(\chi)` …” by “there is a section `s \in \Gamma(\Gcal,\Fcal)` …”.
- **Section 6 measurement identification, lines 1679-1692:** too strong for the source.  
  Edit: “This matches the intended structural role of measurement in Paper XXXIII.”
- **Introduction, lines 176-185:** too strong.  
  Edit: “We discuss ARIA as a candidate non-biological substrate on which the four-phase cycle may be instantiated.”

**5. Surface issues**
- `\Phi_{\min}` appears at lines 668 and 960 with no definition.
- `\mathcal O(g)` / `\Gcal_O^{(g)}` are only described informally (lines 603-612); they are load-bearing and need a precise definition if Lemma 3.3 is to be more than handwaving.
- Lines 1015-1018 still call G6.4 “conjectural,” which conflicts with the bibliography/open-items status.
- Lines 2525-2528 still list G6.3 and G6.4 generically as inherited dependencies; that is stale after the later refinements.
- Line 2416 reverts to “15-of-18 hits” in the non-claims section, while the paper’s main empirical statement is now 17/18 under the reset protocol.

**6. Top three fixes**
1. **Fix the hidden H-FIC dependency before claiming existence/selection.**  
   Lines 834-860, 1079-1178, 1399-1412, 2287-2294. Either prove H-FIC-`E_8` and propagate it cleanly, or state existence/selection only under H-FIC. As written, the main theorem chain is missing a load-bearing hypothesis.
2. **Repair Lemma 3.3 at the actual morphism level.**  
   Lines 635-659. The current proof does not show every morphism in `\Gcal_O` lies in some `\Gcal_O^{(g)}`. Supply a genuine bridge lemma from the source note, or retreat to the weaker algebra-level statement.
3. **Repair Lemma 5.1 and the necessity half of Theorem 5.3.**  
   Lines 1298-1314 and 1360-1362. M3 does not produce the localized section you need, and the theorem then illicitly reintroduces the discarded character-class claim. This is still the main mathematical defect in the closure-saturation argument.

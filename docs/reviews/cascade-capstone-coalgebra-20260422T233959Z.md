Publication ready: **no**.

**1. Claim Audit**
I will only list the non-trivial claims that matter to publishability. The routine category-setup propositions at [cascade-capstone-coalgebra.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:409)–[523] and the formal corollaries depending on them are not where this draft currently fails.

- “**H-lift-fin: finite-cover morphism bridge**” at [689](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:689): correctly relabelled as a **hypothesis**. The derivation-route remark at [696-718](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:696) is honest.
- “**Idempotence on \mathbf{1}_\catC, under H-lift-fin**” at [860-865](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:860): statement now correctly says **under H-lift-fin**. This specific Round-7 fix is in place.
- “**H-FIC: Filtered-Intersection-Commutation**” at [892-907](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:892): correctly relabelled as a **hypothesis**. The derivation-route remark at [909-933](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:909) is honest.
- “**\(F\) preserves \(\omega^{\mathrm{op}}\)-limits, unconditional at Fano level**” at [936-949](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:936): **fails as written**. The opening sentence “By Theorem~\ref{hyp:FIC} (H-FIC, derived from H-grad-Fano)” at [939] and the proof lines [986-993] still treat H-FIC as derived. That directly contradicts the new status.
- “**Existence of \(\Omegacap\), under H-FIC and H-lift-fin**” at [1206-1220](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1206): the **statement** is now correctly conditional. The proof is only acceptable once Theorem [936] is rewritten to assume H-FIC rather than claim it is derived.
- “**H-loc: witness-separation, weakened form**” at [1360-1370](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1360): yes, the displayed statement is now the weaker witness-separation form.
- “**H-rdr: ... uniqueness-only form**” at [1425-1437](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1425): yes, the strict-monotonicity clause is gone.
- “**Closure-data saturation**” at [1452-1463](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1452): **not established by the proof**. H-rdr at [1431-1433] already states essentially the target biconditional. The proof’s “Uniqueness” step at [1487-1490] is invalid: maximality of subgroupoids does not imply equality from equality of query algebras.
- “**Selection principle**” at [1520-1543](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1520): the local circularity issue is improved; \(\iota\) is set up before coalgebra data at [1547-1560]. But the theorem still leans on the failed closure-saturation theorem, so it is not publication-safe.
- “**\( \mathbf{P\text{-}A}\) as comonad counit well-definedness**” at [2136-2148](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2136): **not proved**. It depends on Claim \ref{claim:epsilon-crystallisation}, which Section 6 itself treats as interpretive, not theorem-grade.
- “**ARIA pre-registration hits as coalgebra corroboration**” at [2271-2280](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2271): **cannot be verified locally**. The cited manuscript is not present in the repository.

**2. Internal Consistency**
- The old status of H-FIC is still embedded in Theorem [936] and proof lines [986-993] via “derived from H-grad-Fano.” This is the main stale regression.
- The old name **H-lift** survives at [151](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:151), [925](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:925), and [2623](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2623). Those should all read `H-lift-fin`.
- Theorem [1452] says closure saturation is conditional on H-grad, H-meas, H-loc, H-rdr. But Remark [1508-1511](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1508) says “H-grad, H-meas force \(\Phi_{\max}\),” silently dropping H-loc and H-rdr.
- `\ref{hyp:FIC}` is repeatedly cited as a **theorem** although it is a hypothesis.

**3. External Consistency**
- `CascadeAccessPrinciple`: verified locally. It does state Theorem P-A conditional on H-grad and H-meas at [188-200](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-access-principle-theorem.md:188).
- `CascadeFanoLift`: verified locally. It explicitly gives the two-tier status: Fano-level unconditional, full \( \widehat{\Z[\varphi]^6}\)-level still conditional on H-grad-1 at [223-244](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-fano-grading-lift.md:223).
- `CascadeQOBridge`: verified locally, but the note is marked “WORKING NOTE, lemma-grade” at [1-3](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-q-o-measurement-bridge.md:1) and still leaves G6.4-a open at [193-195](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-q-o-measurement-bridge.md:193).
- `CascadeCompletenessAudit`: verified locally, but it is a meta-audit quoting `cascade-foundations.md`, not the primary derivation.
- `PaperXXXIII`: verified locally. It presents closure projection as a **proposal/candidate principle**, not a closed theorem; see [44-52](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxxiii/paper-xxxiii.tex:44) and [315-356](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxxiii/paper-xxxiii.tex:315).
- `ACT-L1`: I cannot verify the citation “Hypothesis 6.2” at [1809](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1809). That string does not occur in the local file.
- `AriaBrainMapping`: not found locally. The ARIA statistics and null-model claim are uncheckable from this repo.

**4. Tightness**
- Abstract [58-60](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:58): “realises the cofree comonad” is too strong. Edit to: “is proposed to realise the cofree comonad”.
- Introduction [148-151](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:148): replace `H-lift` with `H-lift-fin`.
- Theorem title [936-937](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:936): delete “unconditional at Fano level”.
- Conclusion [2621-2624](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2621): replace `H-lift` with `H-lift-fin`; otherwise the advertised retreat is false on the last page.

**5. Surface Issues**
- Stale nomenclature: `H-lift` at [151], [925], [2623].
- Stale status language: `Theorem~\ref{hyp:FIC}` and “derived from H-grad-Fano” at [939], [986-993].
- Invalid local citation: `ACT-L1 (Hypothesis 6.2)` at [1809].
- Unverifiable local citation: `AriaBrainMapping` throughout Section 8.

**6. Top Three Fixes**
1. Rewrite Theorem [936-1001](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:936) so H-FIC is assumed, not “derived.” Until that is fixed, the Round-7 retreat is not honest.
2. Demote or rewrite Theorem [1452-1491](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1452). As written it does not prove its claim, and Theorem [1520-1560](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1520) inherits that defect.
3. Remove theorem-grade status from the counit/P-A equivalence at [2136-2169](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:2136) and fix the comonad-identification rhetoric in the abstract/introduction. The paper itself says these are interpretive claims, not proved identifications.

**Requested checks**
- 1. Thm 3.7 now a hypothesis: **yes locally, but contradicted later by stale text**.
- 2. Thm 3.10 now a hypothesis: **yes**.
- 3. Cor 3.8 under H-lift-fin: **yes**.
- 4. H-loc witness-separation form: **yes**.
- 5. H-rdr uniqueness-only: **yes**.
- 6. Thm 5.6 non-circular: **locally improved, yes; globally still unsupported because 4.2 fails**.
- 7. Abstract honest about conditional structure: **partly; not honest enough about the four-phase/comonad identification**.
- 8. §9 accurate: **mostly yes**.
- 9. Remaining stale references to old theorem status: **yes, several, listed above**.

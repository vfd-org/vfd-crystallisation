Publication-ready: **No**.

**1. Claim Audit**
- **[lines 250-258](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:250>)**: “Then for every \(N\ge1\), the set \(S_N\) partitions the circle into arcs of at most three distinct lengths. The pitch \(\theta\) is ‘most uniform’ ... exactly when \(\theta/360^\circ\) is badly approximable by rationals.”  
  The first sentence is the classical three-distance theorem. The second sentence is not stated precisely enough to be a theorem here: “most uniform” and “three-distance metric” are undefined, and the proof is only “Classical. See ...”. As written, the proposition overstates what is established.

- **[lines 265-289](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:265>)**: “\(\theta_{\mathrm{full}}=360^\circ/\varphi\) is the unique aperiodic pitch whose rational approximants \(p_n/q_n\) converge most slowly in the three-distance metric.”  
  The proof establishes the all-1 continued fraction and the supplement identity. It does **not** establish the stated uniqueness claim in any precise theorem-grade sense, because the relevant metric is never defined and no extremal theorem is actually proved. The algebraic part is fine; the optimisation claim is not.

- **[lines 312-328](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:312>)**: “Then the selected smaller divergence angle is \(\theta_{\mathrm{phyllo}}=360^\circ/\varphi^2\).”  
  This is only conditionally true because the proof simply assumes the classical selection rule on the chosen helix model at **[lines 341-344](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:341>)**. The paper does **not** prove that the B2 decagram substrate itself forces that rule, nor that “Fibonacci-parastichy closure across iterated \(2I\) actions” has any formal content beyond rhetoric. The theorem is materially weaker than its title suggests.

- **[lines 399-422](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:399>)** and **[467-489](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:467>)**: “The two quantities do share a real cascade signature at the integer level...” / “The integer 137 ... is a programme-internal structural overlap...”  
  Not established. What is actually shown is: in **degrees**, \(\lfloor 137+\pi/87\rfloor=\lfloor 360/\varphi^2\rfloor=137\), and no clean fractional relation was found. That is a numerically true observation. It does **not** prove a structural invariant shared by the two constructions.

- **[lines 426-435](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:426>)**: “No candidate combines a clean cascade origin with a sub-\(\sim0.5\%\) match.”  
  Fine as a report on the tested table, assuming the script is authoritative. This is a negative computational observation, not a theorem. It should be labelled that way.

- **Major hidden assumption not confronted anywhere in §4**: the whole “137 overlap” compares a **dimensionless constant** \(\alpha^{-1}\) with an **angle in degrees**. The coincidence disappears in radians or turns. Unless the paper proves that the factor \(360\) is structurally canonical rather than a human unit convention, the integer-floor discussion is unit-dependent numerology, not mathematics.

**2. Internal Consistency**
- The paper’s toned-down abstract is better than prior rounds, but the body backslides. The abstract says “suggestive structural overlap” and “not as a theorem-level fractional relation” at **[lines 83-85](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:83>)**; §4 then says “real cascade signature” at **[lines 399-402](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:399>)** and “identifies 137 itself as a cascade signature” at **[lines 482-485](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:482>)**. That is a re-escalation of the claim.

- The summary strengthens Theorem T1 beyond the theorem statement: **[lines 560-565](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:560>)** says the angle “compatible with Fibonacci-parastichy closure is uniquely” \(360^\circ/\varphi^2\). The actual theorem proves only a conditional import of the classical criterion.

- **[line 354](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:354>)** cites “Theorem F1-unique”. The local source has **Theorem F1**, not that label.

- Internal `\ref` usage looks syntactically coherent. I do not see a missing local label from the source text.

**3. External Consistency**
- **CascadeBio §5.1 / §3.1**: verified locally in [cascade-bio.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:189>) and [cascade-bio.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:535>). The manuscript’s basic B2 substrate description is faithful.

- **CascadeFoundations F1**: verified locally in [cascade-foundations.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-foundations.md:47>). The source proves a unique positive solution \(r=\varphi\). The manuscript’s theorem-label citation is wrong.

- **CascadeBio §B6.1-B6.2**: verified locally in [cascade-bio.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:362>). The source does indeed say “integer shared, fractional parts not”. So the manuscript is faithful to that source. The problem is that this is not upgraded to a proof here.

- **CascadeAlphaChain**: verified locally in [cascade-alpha-chain-complete-theorem.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-alpha-chain-complete-theorem.md:21>). That source explicitly claims theorem status for \(\alpha^{-1}=137+\pi/87\).

- **Paper XXII**: verified locally in [paper-xxii.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:46>) and [paper-xxii.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:297>). That source explicitly demotes the same formula to a numerical/structural correspondence, not a derivation. The manuscript cites both statuses without resolving the contradiction.

- **WO-1 / SmartCapsid**: the manuscript says phyllotaxis is “native to the VFD programme in the same way” as Caspar–Klug at **[lines 575-579](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:575>)**. The local source [biology-rung-capsid.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-capsid/biology-rung-capsid.tex:375>) says the capsid result is face-level and explicitly **not** a proved cell-level descent. Your sentence overreads the source.

- I could not find any local source that justifies comparing \(\alpha^{-1}\) to \(\theta_{\mathrm{phyllo}}\) specifically in **degrees** as a canonical, programme-internal normalisation. That missing justification is fatal to the 137 section.

**4. Tightness**
- **[lines 52-53](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:52>)**: “This short paper formalises two results.”  
  Edit: “This short paper states one conditional placement result and one negative numerical comparison.”

- **[lines 159-162](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:159>)**: “This makes the phyllotaxis angle native to the VFD programme...”  
  Edit: “This places the classical phyllotaxis angle on a VFD-selected substrate; no substrate-to-angle derivation is proved here.”

- **[lines 399-402](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:399>)**: “do share a real cascade signature”  
  Edit: “share a programme-internal overlap claim, contingent on the chosen normalisation and upstream \(\alpha\)-chain interpretation.”

- **[lines 482-485](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:482>)**: “It identifies 137 itself as a cascade signature...”  
  Edit: “It records a shared integer floor in the current degree-based comparison; no invariant structural identity is proved.”

- **[lines 560-565](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:560>)**: “compatible with Fibonacci-parastichy closure is uniquely ...”  
  Edit: “conditional on the imported classical criterion, the selected smaller angle is \(360^\circ/\varphi^2\).”

**5. Surface Issues**
- **Wrong source label**: “Theorem F1-unique” at **[line 354](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:354>)** does not exist in the cited file.

- **Repository-wide numerical inconsistency**: this paper uses `137.0361103`; `cascade-bio.md` still has `137.0361102`; `cascade-alpha-chain-complete-theorem.md` has `137.036104...`. Your manuscript and script agree; the local source tree does not.

- **Unit problem left implicit**: \(\Delta=\theta_{\mathrm{phyllo}}-\alpha^{-1}\) at **[lines 426-430](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:426>)** subtracts an angle in degrees from a dimensionless constant. If you insist on keeping §4, you need an explicit statement that this is a comparison of bare numerals under a chosen normalisation, not a unit-consistent physical relation.

- **Insider terminology persists**: “Coxeter / phason degree-of-freedom count (programme-internal)” at **[lines 406-408](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:406>)** is still opaque in this paper. Replacing one piece of jargon with another did not solve the readability problem.

**6. Top Three Fixes**
1. **Either justify the degree normalisation or delete the entire integer-137 overlap section.**  
   The comparison at **[lines 388-489](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:388>)** is unit-dependent. Without a proof that `360` is structurally canonical here, the “shared 137” claim is not publication-grade.

2. **Downgrade Proposition `three-dist`, Proposition `coxeter-vogel`, and Theorem T1 to match what is actually proved.**  
   The problems are at **[lines 250-303](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:250>)** and **[312-357](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:312>)**. Right now the theorem package is still rhetorically stronger than the argument.

3. **Resolve the \(\alpha^{-1}\) status conflict across your own sources.**  
   The manuscript cites theorem status at **[lines 166-168](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:166>)** and correspondence status at **[lines 168-174](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex:168>)**, while local sources flatly disagree. Until you choose one status and rewrite accordingly, the paper is not internally or externally stable.

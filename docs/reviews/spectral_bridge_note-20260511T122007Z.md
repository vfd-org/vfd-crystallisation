Publication ready: **no**.

All line numbers below refer to [spectral_bridge_note.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:1>).

**1. Claim Audit**

- Lines 31-35: “Inside \(2I\), \(2T\) has index 5; its left cosets partition the 600-cell into five disjoint copies of the 24-cell.”  
  Not established in the note. Worse, the later action uses right multiplication, so the cosets must be right cosets \(2T\backslash 2I\), not left cosets, unless a different action convention is stated. Since \(2T\) is not normal in \(2I\), this is not cosmetic.

- Lines 38-43 and 141-148: “\(\mathrm{lift}_i(E_{C_i}(12))\subset E_{600}(12)\)” with residual \(6\times 10^{-15}\).  
  The proof establishes only a floating-point observation. For publication, this needs an exact argument: e.g. identify the inter-coset boundary operator and prove it annihilates the local \(\lambda=12\) eigenspace, or give exact rational/\(\mathbb Q(\sqrt5)\) linear-algebra certificates. The current “subset” notation is theorem-level, but the evidence is numerical.

- Lines 42-43, 67-71, 176-177: “Negative controls … all fail”; “No other eigenvalue … survives”; “fails at every other local-Laplacian eigenvalue.”  
  Over-claim. The \(\lambda=0\) span across the five cosets contains the global constant eigenvector; lines 172-174 admit this. Also, the reported statistic is a maximum residual on a basis, which does not prove the lifted subspace has zero intersection with the global eigenspace. Use intersection dimensions or minimum singular values.

- Lines 63-65: “classical fact” that the five \(2T\) cosets form five inscribed 24-cells.  
  No citation and no proof. Hostile referee will not accept this as load-bearing background without Coxeter/Conway-Sloane or a short finite-group/coordinate proof.

- Lines 91-94: “\(\sigma\)-fixed sublattice … exactly \(2T\).”  
  Asserted, not proved. This is finite set equality, not a “sublattice” statement as written. Needs coordinate proof or citation.

- Lines 98-106 and 194-196: right multiplication permutes the cosets and descends to faithful \(A_5\).  
  Missing hypotheses/proof. You must say explicitly that \(-1\in 2T\), so \(\{\pm1\}\) acts trivially on right cosets, and prove the kernel is exactly \(\{\pm1\}\). Faithfulness is not automatic.

- Lines 121-129: spectra of local and global Laplacians.  
  Numerical diagonalisation supports the displayed values, but exact spectra are being used downstream. The global spectrum is available as an exact \(2I\)-character-table computation in the repo; the note should cite or reproduce that. The local 24-cell spectrum also needs an exact source.

- Lines 181-190: direct-sum decomposition and “inter-coset operator subspace.”  
  The orthogonal complement is tautological once the lift is proved. But “operator subspace” is undefined; \(\Eres\) is a vector subspace of functions/eigenvectors, not an operator space.

- Lines 192-235: \(A_5\) character table and \(\Elift\cong 2Y_5\), etc.  
  Currently numerical, but displayed as exact representation theory. Need proof that the subspaces are invariant under the \(A_5\) action and state that the class characters are rounded numerical traces unless exact traces are certified.

**2. Internal Consistency**

- Left/right cosets conflict: lines 32 and 63 say left cosets; lines 98-106 and 194-196 use right multiplication, which acts naturally on right cosets \(2T\backslash 2I\). Fix globally.

- “\(d=1\)” is overloaded. The global nearest-neighbour shell has squared distance \((3-\sqrt5)/2\), while the internal coset/24-cell edge shell has squared distance \(1\). These are not the same shell. The note risks conflating global 600-cell edges with local 24-cell edges.

- “Exact” language conflicts with numerical evidence: lines 50, 68-71, 144-148, 245-249 use exact/inclusion language where only floating-point residuals are supplied.

- There are no `\ref`, `\eqref`, or `\cite` commands in the note, so there are no broken cross-references; the problem is absence of citations.

**3. External Consistency**

- The note contains no explicit attributions to “Paper XVIII/XXIX/etc.” It therefore fails to attribute several imported facts.

- Verified locally: \(V_{600}\cong 2I\) is proved/computer-certified in `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:964-994`. The global \(\lambda=12\) multiplicity \(25\) is in `:1116-1161`.

- Partly verified locally: the five \(2T\)-coset 24-cells appear in `papers/paper-xxxv/paper-xxxv.tex:284-303`, and the \(A_5\) action/kernel claim in `:416-432`. But that source uses a left-coset/left-action convention; this note uses right multiplication. The note must reconcile the convention.

- I found no paper-level proof in the repo of the \(\lambda=12\) zero-extension lift identity. I found code/tests/artifacts only.

- Local repo inconsistency to resolve before citing: `cascade-algebraic-substrate.tex:1566-1567` lists a 24-cell spectrum \(\{0,6,8,12\}\), while this note uses \(\{0,4,8,10,12\}\). Other repo files match the note. Do not leave two incompatible “24-cell spectrum” claims unqualified.

**4. Tightness**

- Line 50: replace “lifting exactly” with “observed to lift to numerical precision” unless an exact proof is added.

- Lines 67-71: replace with “The computations find a single-coset lift at \(\lambda=12\); among nonzero local eigenvalues, the tested alternatives fail.”

- Line 106: add “because \(-1\in 2T\)” and a kernel/core argument.

- Lines 205-207: caption the table as “rounded numerical class characters.”

- Lines 243-249: replace “shows that … exists” with “provides numerical evidence for” unless Section 3 is upgraded to a proof.

**5. Surface Issues**

- No bibliography or citations despite imported classical and repo-local results.

- “\(\sigma\)-fixed sublattice in \(V_{600}\)” is imprecise; \(V_{600}\) is a finite vertex set.

- “basis” in the character table should be “subspace.”

- “inter-coset operator subspace” is undefined and misleading.

**6. Top Three Fixes**

1. Fix the coset convention and \(A_5\) descent: lines 31-32, 63-65, 98-106, 194-196. Use right cosets consistently or change the action.

2. Replace the numerical \(\lambda=12\) lift claim with an exact proof/certificate: lines 38-43, 141-148, 243-249.

3. Correct the selectivity claim: lines 42-43, 67-71, 172-177. The \(\lambda=0\) global constant survives as a combination, and max residual is not a no-intersection proof.

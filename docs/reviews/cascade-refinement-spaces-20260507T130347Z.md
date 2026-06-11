All line numbers refer to `papers/cascade-refinement-spaces/cascade-refinement-spaces.tex`.

**1. Claim Audit**

- “$V_{600}$ ... standard $120$-vertex set” and “$V_{24}$ ... $24$-vertex subset” (lines 252-258): established by local P2 labels; verified.
- “Refinement properties” (lines 446-458): mostly established from the definitions, but only if vertices/edges/centroids are treated as formal labelled objects. If they are geometric points/edges, the proof does not rule out coincidences or duplicate generated edges.
- “Each level-$n$ oriented edge has exactly two ... preimages” (lines 456-458): established under the formal edge-parent convention.
- “$F^0$ ... dimension $32$” and “$F^1$ ... dimension $7$” (lines 551-557): arithmetic correct.
- “$X_n^{0,\bullet}$ and $X_n^{1,\bullet}$ are finite-dimensional real Hilbert spaces” (lines 603-614): not fully established as written. The Clifford-sector form at lines 535-542 is not defined precisely enough to be known positive-definite. If $a^\dagger$ means reversion, the form is indefinite in signature $(1,3)$.
- “Bonding contractions” (lines 676-685): established. The edge proof is non-sharp but sufficient.
- “Adjoint relation” (lines 759-773): established, including the $p^1j^1=\tfrac12\id$ half-section.
- “$X_\cyl^{0,\bullet}\cong c_{00}$” (lines 873-884) and compatibility lemma (lines 942-947): established.
- “Limits exist” (lines 978-983): established.
- “$X_\inv^{0,\bullet}\cong\ell^2(V_\infty^\bullet;F^0)$” (lines 999-1015): essentially established; add one sentence justifying the inner-product limit by absolute convergence/Cauchy-Schwarz in line 1043’s passage.
- “$X_\cyl^0$ is dense in $X_\inv^0$” (lines 1057-1066): established.
- “Coxeter action ... is unitary” (lines 1130-1134): reflection-representation part is adequately cited to Humphreys, but the statement cites only Definition 4.2/`def:Xn-0` even for the edge space. It also inherits the Clifford-form problem above.
- “mixed $\Q(\varphi)/\Q$-form ... $\Q$-dimension $36$” (lines 1184-1205): arithmetic correct. Source naming is loose; P2’s `def:Q-forms` uses `U_Q`, `Cl_Q`, `O_Q`, not the exact names `V_{D_4,Q}`, `V_{16,Q}`, `V_{8,Q}`.
- “$\sigma_n$ is a $\Q$-linear involution ... does not extend $\R$-linearly” (lines 1235-1244): established.
- “Intertwining identities” (lines 1255-1320):  
  - Vertex Coxeter $p^0$: established.  
  - Vertex Coxeter $j^0$: adjunction argument is acceptable but terse; it should explicitly use unitarity and level subscripts.  
  - Edge Coxeter $p^1,j^1$: established; the $j^1$ adjunction step at lines 1403-1420 is now adequate.  
  - Refinement-$\sigma$ on both $p^0$ and $j^0$: established by direct fibrewise inspection, including zero-extension.  
  - Coxeter-$\sigma$: correctly restricted; no full $W(H_4)$-$\sigma$ commutation is claimed.
- The summary phrase “and analogously for $\sigma$ from P1” (line 108) is too broad. The actual theorem gives only mixed-form vertex-sector $p^0/j^0$ refinement-$\sigma$, not edge or real-Hilbert $\sigma$.

**2. Internal Consistency**

- The graph-plus-faces convention is explicit at lines 282-305 and 339-358. Good. But “edge set of a graph” conflicts with “disjoint union” construction if generated unordered pairs ever coincide. State explicitly whether this is a simple graph, multigraph, or labelled-edge graph.
- Remark lines 373-378 says the bonding/intertwining constructions depend only on edge classes (a) and (b). For $p^1$ they depend on class (a) only at the current step; $X_{n+1}^1$ still contains all edge classes. Rephrase.
- Line 1132 cites `def:Xn-0` for unitarity on both vertex and edge spaces. It should cite `def:Xn-0` and `def:Xn-1`.
- Lines 1266-1267 say the $p^1$ and $j^1$ identities hold “on $X_{n+1}^{1,\bullet}$.” The $j^1$ identity is on $X_n^{1,\bullet}$.
- Lines 1459-1462 say “each action” descends to $X_\cyl$ and $X_\inv`; this conflicts with lines 1315-1320, which correctly deny a real-Hilbert $\sigma$ action. Say “the vertex Coxeter action.”
- I found no unresolved `\ref`, `\eqref`, or bibliography keys.

**3. External Consistency**

- P1 `def:sigma`: verified locally; it defines $\sigma(\varphi)=1-\varphi`.
- P1 `def:sigmaV`: verified locally; coefficientwise $\sigma_V=\id_V\otimes\sigma`.
- P1 `thm:pisigma-functorial`: verified locally; it proves functoriality for scalar extensions of $\Q$-linear maps. P3’s refusal to use it for full $W(H_4)$-$\sigma$ commutation is correct.
- P2 `def:V600`, `def:V24`, `prop:24-in-600`: verified locally.
- P2 `def:icosian-ring`, `thm:icosian-closure`, `def:Cl-basis`, `def:octonions`: labels exist and support the cited substrate objects.
- P2 `def:Q-forms`: exists, but the correspondence to P3’s names should be spelled out. It does not literally define `V_{D_4,Q}`, `V_{16,Q}`, `V_{8,Q}` under those names.
- P3’s claim that $W(H_4)$ reflection matrices have $\Q(\varphi)$ entries is correctly marked as an inference, not a P2 theorem (lines 1605-1611).
- The citation to `CascadeRefinementCompat` section `sec:scope-and-gap` is verified: that paper explicitly uses an abstract scalar pure-midpoint model and names the full P3/P4 lift hypotheses.
- `CascadeMechanism` does define the O0-O3 consumer API and records O3 as discharged only in the abstract pure-midpoint companion setting.

**4. Tightness**

- Line 108: replace “and analogously for $\sigma$ from P1” with “and the mixed-form vertex-sector $p^0/j^0$ refinement-$\sigma$ identities.”
- Lines 535-542: replace the Clifford-form sentence with a precise adjoint convention and a basis check of positivity.
- Lines 373-378: replace “only on edge classes (a) and (b)” with “the parent-fibre averaging uses the class-(a) subdividing edges; the remaining edge classes enter only as finite-level domain components ignored by $p^1$ at that step.”
- Lines 1383-1385: add the explicit adjoint calculation with $U_n(g)p=pU_{n+1}(g)$ and unitarity.
- Lines 1459-1462: replace “each action” with “the vertex Coxeter action.”

**5. Surface Issues**

- “principal involution (anti-automorphism reversing Clifford generators)” (lines 537-538) is not standard enough and likely wrong for positivity.
- Duplicate bibliography entries `Humphreys` and `HumphreysReflectionGroups` cite the same book. Consolidate unless different uses genuinely require separate keys.
- “Coxeter-$\sigma$ intertwining” is sometimes used where the theorem proves restricted commutation. Use “commutation” for line 1497 and nearby prose.
- `\ell^2_{\rm fin}` (line 1210) is nonstandard notation; define it or use “all functions on the finite set.”
- The P2 `def:Q-forms` support is only in the bibliography, not cited inline in Definition `def:Xn-Q-form`.

**6. Top Three Fixes**

1. Fix the Clifford-sector inner product at lines 535-542. Without a precise positive-definite form, Proposition `prop:Xn-Hilbert` and every later Hilbert-space claim rest on an unproved assumption.

2. Tighten Theorem `thm:commute` wording at lines 1266-1267 and 1459-1462. The $j^1$ domain is misstated, and the descent sentence over-includes $\sigma$ despite the paper correctly excluding real-Hilbert $\sigma$ actions.

3. Make the refinement datum formally unambiguous at lines 282-358. State whether generated edges are labelled edge instances or ordinary unordered pairs, and adjust Remark lines 373-378 so the role of class-(a), class-(b), and class-(c) edges is exactly true.

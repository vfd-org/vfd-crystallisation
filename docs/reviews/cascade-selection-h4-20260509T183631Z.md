Publication ready: no.

**1. Claim Audit**

- [lines 392-403](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:392), Proposition `prop:psd`: established. The tensor form `L_N^{block}=L_N^{cl}\otimes id_{F^0}` is now explicit, and the operator-norm argument is clean.

- [lines 446-449](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:446), Lemma `lem:connected`: established, modulo the classical base connectivity of the 600-cell graph. The induction from P3 refinement is valid.

- [lines 492-502](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:492), Theorem `thm:kernel`: established. The proof correctly uses  
  `ker L_N^{block} = (ker L_N^{cl}) \otimes F^0`.

- [lines 550-571](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:550), Theorem `thm:convergence`: essentially established, but the theorem statement omits the quantifier “for every `N >= 0`.” Also, `lambda_+ > 0` should explicitly invoke connectedness plus nontriviality of `G_N^{H_4}`.

- [lines 620-625](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:620), Lemma `lem:H4-fixed`: established from irreducibility/nontriviality of the standard `H_4` representation.

- [lines 643-654](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:643), Theorem `thm:fixed-dim`: established, and verified against P3 `def:coxeter`.

- [lines 685-727](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:685), Proposition `prop:o0`: over-claims. It says “standing analytic preconditions `(O0)` ... hold for the five-tuple,” but CascadeMechanism `(O0)` is rung-sequence data: all `Phi_k`, all `R_k`, all flows, and each adjacent pushforward. The proof verifies top-rung analytic pieces and records availability of P3 bonding maps. That is not the same claim.

- [lines 735-781](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:735), Theorem `thm:main`: establishes the stated `(O1)` witness for a chosen `xi^*` and the trivial chosen initial datum `phi_N^(0)=phi_N^*`. It does not overclaim uniqueness or `(O2)/(O3)`.

- [lines 843-894](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:843), `N=0` numerics: spectrum, norm, kernel dimension, and gap match P2. But [lines 882-883](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:882) incorrectly use `\Psi_0` for the embedding; this must be `\iota_0`.

**2. Internal Consistency**

- Cross-references resolve locally; no `\eqref` references are present.
- [lines 711-715](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:711) say “clauses (1)--(3) of `(O1)` are top-rung statements.” False as written. CascadeMechanism `(O1)` is one API item, and Definition clauses `(1)--(3)` include terminal projection compatibility, which is not top-rung-only.
- [lines 145-152](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:145) correctly say full `(O0)` is not built here. [lines 685-689](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:685) then weaken that discipline by calling the proposition “`(O0)` verification.”
- [lines 882-883](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:882): `\Psi_0` conflicts with the paper’s own notation; `\Psi_N^t` is the flow, `\iota_N` is the embedding.

**3. External Consistency**

Verified locally:

- CascadeMechanism: `(O0)--(O3)` are indeed at lines 594-627; `(O1)` is lines 609-617; “successor paper’s own task” is lines 637-639. The paper’s `(O1)` usage is valid. Its formal `(O0)` proposition remains too strong.
- RefinementSpaces/P3: `def:Xn-0`, `prop:Xn-Hilbert`, `def:refinement`, `def:base-graphs`, `not:fibres`, `def:coxeter`, `def:p0`, `thm:bonding`, and `def:sigma` all exist and support the stated uses.
- ClosureDynamics/P4: `def:coboundary` projects `F^0` to `Im(O)`; `def:An` has top-left block `d_n^*d_n` acting trivially outside the imaginary octonion direction; `def:Fn` and `thm:flow-exists` support the cited uses.
- RefinementCompat: `def:abstract-model`, `def:Atilde`, `prop:strict-fails`, `thm:O3-discharge`, and `sec:scope-and-gap` exist. The revised `(L1)/(L3)` descriptions now match the source.
- AlgebraicSubstrate/P2: `def:V600` gives `|V_600|=120`; `tab:P2-spectrum` gives eigenvalues including `9-3 sqrt(5)` and `9+3 sqrt(5)` with the stated multiplicities.

**4. Tightness**

- [line 685](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:685): change “`(O0) verification`” to “Top-rung analytic preconditions and recorded bonding map.”
- [lines 687-689](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:687): replace “`(O0) ... hold for the five-tuple`” with “the top-rung analytic components of `(O0)` hold for the five-tuple; the rung-sequence bonding map is recorded separately.”
- [lines 711-715](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:711): replace with “The `(O1)` witness below uses only top-rung residual-zero and convergence data; no inter-rung pushforward is used.”

**5. Surface Issues**

- [lines 882-883](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:882): `\Psi_0` should be `\iota_0`.
- [line 552](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:552): add explicit `N >= 0` quantification to `thm:convergence`.
- I could not run `pdflatex`; the sandbox filesystem is read-only and could not create an output directory.

**6. Top Three Fixes**

1. Fix the formal `(O0)` overclaim at [lines 685-689](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:685). This is the only publication-blocking mathematical scope problem.

2. Replace the false “clauses (1)--(3) of `(O1)`” sentence at [lines 711-715](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:711). It confuses the API item with the CascadeMechanism definition clauses.

3. Correct the embedding notation regression at [lines 882-883](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:882): `\Psi_0` must be `\iota_0`.

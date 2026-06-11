Publication ready: yes.

All line numbers refer to [cascade-selection-h4.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-selection-h4/cascade-selection-h4.tex:1).

**Claim Audit**

- “`L_N^{\mathrm{block}}` is bounded, self-adjoint, and positive semi-definite...” l.398-406. Established. The proof is standard for a finite labelled multigraph and the tensor extension is valid.
- “`G_N^{H_4}` is connected” l.451-452. Established from P3’s refinement definition. No over-claim.
- “`\iota_N : F^0 \to \ker L_N^{\mathrm{block}}` is an isomorphism” l.507-514. Established, conditional on the connectivity lemma.
- “Gradient flow converges to the kernel projection...” l.565-586. Established by finite-dimensional spectral decomposition. The “nontrivial graph” assumption at l.583 is not proved in that theorem, but follows from the base 600-cell graph and class-(a) refinement.
- “Standard `H_4` reflection representation has trivial fixed subspace” l.638-640. Established by irreducibility/nontriviality.
- “`\dim_\mathbb R (F^0)^{W(H_4)} = 28`” l.660-669. Established, and externally consistent with P3’s branchwise action.
- “Top-rung analytic components of `(O0)` hold...” l.704-711. Correct only in the stated top-rung/recorded-map sense. It does not prove full rung-sequence `(O0)`, and the paper now says that explicitly.
- “The five-tuple satisfies `(O1)` in the witnessed fixed-point sense” l.781-807. Established. This is a deliberately weak fixed-point witness: choosing `\phi_N^{(0)}=\phi_N^\star` makes convergence tautological. The theorem does not over-claim basin selection.
- N=0 numerics l.875-920 and spectrum remark l.924-933. Verified against P2’s spectrum table: norm `9+3\sqrt5`, gap `9-3\sqrt5`, multiplicities, kernel dimension, and block multiplicity factor `32` are consistent.

**Internal Consistency**

No broken internal references found. The labels used by `\ref` resolve locally.

Notation is consistent after the scope edits: `A_n^{\mathrm{vertex}}` is explicitly local shorthand for P4’s top-left block, and `L_N^{\mathrm{block}}` is kept distinct from P4/compat operators.

Only minor weakness: Proposition l.701-749 has a proof at l.751-753 that says “Each item follows directly from the cited result,” but items (O0.2)-(O0.3) are partly elementary consequences for the new operator, not direct imports. This is not mathematically wrong, but the proof language is too compressed.

**External Consistency**

Verified locally:

- P3 `RefinementSpaces`: `def:base-graphs`, `def:refinement`, `not:fibres`, `def:Xn-0`, `prop:Xn-Hilbert`, `def:p0`, `thm:bonding`, `def:coxeter`, and `def:sigma` support the uses made here.
- P4 `ClosureDynamics`: `def:coboundary`, `def:An`, `def:Fn`, and `thm:flow-exists` support the claims about projection to `\Im(\mathbb O)`, the top-left block, closure functional, and finite-dimensional flow argument.
- `RefinementCompat`: `def:abstract-model`, `def:Atilde`, `prop:strict-fails`, `thm:O3-discharge`, and `sec:scope-and-gap` support the stated status of `(O2)`, `(O3)`, `(L1)`, and `(L3)`.
- `CascadeMechanism`: lines 594-627 are the `(O0)`-`(O3)` consumer API; lines 637-639 support the “selection is successor paper’s task” framing.
- P2 `AlgebraicSubstrate`: `def:V600` and `tab:P2-spectrum` support the `N=0` numerical claims.

No repository-local attributed claim failed verification.

**Tightness**

- l.704-707: “The top-rung analytic components ... hold” is acceptable, but the surrounding proposition title still sounds broader than the proof.
  Suggested edit: “The following top-rung analytic components hold, and the inter-rung bonding map is available but unused.”
- l.751-753: proof too terse.
  Suggested edit: “Items (1) and (4) are imported from P3; items (2) and (3) are elementary finite-dimensional consequences of Proposition~\ref{prop:psd}.”
- l.1066-1079: recommended citation phrasing is appropriately scoped and not over-strong.

**Surface Issues**

- l.1106: `Proposition~\ref{prop:o0}(O0.3)` will typeset cramped. Use `Proposition~\ref{prop:o0}, item~(O0.3)`.
- l.141 and l.1054 are long source lines; cosmetic only.
- No undefined macros or obvious broken LaTeX found by inspection.

**Top Three Fixes**

1. l.751-753: replace the one-sentence proof of Proposition~\ref{prop:o0}; it is the only place where the proof undersells what is actually being checked.
2. l.704-711: keep the “top-rung only” wording prominent in the proposition statement; do not let downstream readers cite it as full `(O0)`.
3. l.1106: fix the cramped cross-reference formatting in the bibliography note.

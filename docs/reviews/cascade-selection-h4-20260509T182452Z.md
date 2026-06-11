Publication ready: no.

**1. Claim Audit**
- Lines 62-75: “Five clauses constitute the named theorem.” Not true as written. The named theorem at lines 717-760 has only two enumerated O1 clauses; PSD, kernel, convergence, and fixed-dimension are separate results. This causes broken semantic references at lines 111 and 160.
- Lines 245-252: Kernel count for P4’s vertex block is correct, assuming connected graph and P4’s \(d_n\) projection to \(\mathrm{Im}(\mathbb O)\).
- Lines 374-385: PSD/self-adjoint/norm bound is established. Proof wording at lines 414-415 is imprecise: this is not four scalar copies, but \(L_N^{cl}\otimes \mathrm{id}_{F^0}\), i.e. 32 scalar coordinate copies.
- Lines 427-430: Connectivity proof is adequate given P3’s refinement definition, but it relies on nondegenerate face boundaries. If repeated/degenerate face edges are allowed upstream, the loop/multiedge convention must be stated.
- Lines 473-483: Kernel theorem is true given connectivity, but the proof at lines 496-500 is dimensionally garbled. \(\mathbb R^4\otimes F^0_{\text{summandwise}}\) would not be \(F^0\). Replace with \(\bigoplus_S(\ker L_N^{cl}\otimes V_S)\cong F^0\).
- Lines 533-553: Convergence theorem is proved for fixed \(N\). “Uniform” means uniform over initial data at fixed \(N\), not uniform in \(N\). State that.
- Lines 602-607: Fixed-subspace lemma is true. Proof has a logical typo at lines 621-622: “the fixed subspace, being non-zero” should be “if nonzero.”
- Lines 625-636: Fixed-dimension theorem is established, contingent on P3’s branchwise action being standard on \(V_{H_4}\) and trivial on the other summands. Verified locally.
- Lines 667-709: O0 proposition overclaims. Cascade-mechanism O0 is a rung-sequence condition on \(\Phi_k,R_k,\Psi_k^t,\pi^\sharp_{k+1,k}\). This paper checks the top-level Hilbert/flow data and points to \(p^0\), but does not define/check the full lower-rung tuple for all \(k\le N\).
- Lines 717-760: Main O1 theorem establishes only a weak witnessed O1 tuple, with \(\phi_N^{(0)}=\phi_N^\star\). The nontrivial convergence statement applies only to initial data whose kernel projection is already the chosen \(\phi_N^\star\). It does not establish physical selection, unique selection, or a cascade-closure event.
- Lines 823-888: \(N=0\) numerics match P2’s table, including gap \(9-3\sqrt5\) and norm \(9+3\sqrt5\). But P2 itself labels the spectrum as imported, not first-principles.

**2. Internal Consistency**
- Lines 111 and 160 cite `Theorem~\ref{thm:main}(4)` and `(3)`, but Theorem 7.2 has no such clauses.
- \(\Psi_N\) is overloaded: embedding at lines 478-480, flow family \(\Psi_N^t\) at lines 734-735, then embedding again at line 736. Rename the embedding, e.g. \(\iota_N\).
- Abstract line 57 says P4’s \(A_n\) acts only on \(\mathrm{Im}(\mathbb O)\). P4’s full \(A_n\) has vertex and edge blocks; the intended object is the vertex/top-left block \(d_n^*d_n\).
- Lines 145-149 misdescribe compat’s \((L1),(L3)\); see below.
- Line 1027: “unique up to the 28-dimensional choice” is not uniqueness. Say “leaves a 28-dimensional free choice.”

**3. External Consistency**
- P3 citations verify: base graph, refinement, fibres, \(X_n^{0,\bullet}\), Coxeter action, and bonding maps are present in `cascade-refinement-spaces.tex` lines 262-285, 320-380, 547-596, 603-654, 687-737, 1172-1226.
- P4 citations verify: \(d_n\) projects to \(\mathrm{Im}(\mathbb O)\) at lines 313-331; \(A_n\)’s vertex block is \(d_n^*d_n\) and acts trivially off the imaginary octonion direction at lines 412-425; \(F_n\) and flow existence are at lines 571-580 and 650-672.
- RefinementCompat citations mostly verify: abstract scalar model lines 175-203; \(\widetilde A_n=2^nA_n^{vertex}\) lines 279-282; O3 theorem lines 526-537; strict O2 failure lines 612-620 and 757-776.
- Not verified: lines 145-149 claim \((L1)\) is “refinement-compatibility of unscaled \(A_n\)” and \((L3)\) is “spectral-gap propagation.” Compat defines \((L1)\) as a boundary-vertex incidence/defect condition and \((L3)\) as a harmonic-extension energy lower-bound condition, lines 226-241. No spectral-gap propagation claim is there.
- CascadeMechanism citations verify: O0-O3 API lines 594-627; O1 lines 609-617; “selection is successor’s task” lines 637-639.
- P2 citations verify \(V_{600}\), \(V_{24}\), and the spectrum table at lines 778-800, 810-829, 1116-1161. Again: P2 says the spectrum is imported at lines 1125-1140.

**4. Tightness**
- Line 48: change “We discharge” to “We give a finite-level witnessed O1 tuple.”
- Lines 62-75: change “Five clauses constitute the named theorem” to “The paper proves five ingredients.”
- Lines 101-102: change “verify O0” to “verify the top-rung analytic pieces of O0, with bonding maps available from P3.”
- Lines 145-149: replace the L1/L3 description with compat’s actual definitions, or remove the claim.
- Lines 741-743: change “discharges the O1 obligation” to “satisfies O1 for the chosen \(\xi^\star\) and chosen top-rung initial datum.”
- Lines 1027-1029: replace with “The construction leaves a 28-dimensional free choice of \(\xi^\star\); single-ray selection is open.”

**5. Surface Issues**
- Undefined/incorrect proof notation: \(F^0_{\text{summandwise}}\), line 499.
- Inconsistent terminology: “positive semi-definite” vs “positive-semidefinite”; “32-dimensional” vs “32-dim.”
- Misleading upstream name: use \(A_n^{vertex}=d_n^*d_n\), not bare P4 \(A_n\), where vertex-only behavior is intended.
- Semantic broken refs: `Theorem~\ref{thm:main}(3)` and `(4)`.
- The phrase “Fiedler value” appears in the intended scope but not the draft; the draft uses \(\lambda_+\). If “Fiedler” is desired, define it explicitly.

**6. Top Three Fixes**
1. Fix theorem architecture: either make Theorem 7.2 actually contain the five advertised clauses, or stop citing `thm:main(3)/(4)` and cite the separate results. Lines 62-75, 111, 160, 717-760.
2. Repair O0/O1 scope: define the full rung-sequence data if claiming O0, or downgrade to top-rung O1 preconditions. Lines 667-709, 741-760.
3. Correct external attribution for compat \((L1),(L3)\) and upstream operators. Lines 57, 145-149, 337-358, 1000-1010.

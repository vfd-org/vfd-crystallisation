Line numbers refer to [cascade-mechanism.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-mechanism/cascade-mechanism.tex:1>). Round 4 fixes listed in the prompt have landed. The draft is still not publication-ready.

**1. Claim Audit**
- l.61-68: “prove a conditional residual-compositionality proposition” and `||C_\varphi^{-1}||=\varphi^2`. The proposition is proved as stated; the operator norm claim is supported by the shifted Laplacian spectrum. No over-claim here.
- l.201-217: imported P4/P3 infrastructure. Verified locally. P4 proves gradient operator, flow existence, dissipation, coercive contraction, and mass-only flow intertwining; P3 proves finite-level state spaces and bonding maps. The caveat “not arbitrary `R_k`” is necessary and present.
- l.237-255: Definition 3.1. Definitional, not proved. However it still has a structural gap: the initial tower is projection-compatible, but the limiting tower `\phi^\star` is not required to satisfy `\phi^\star_k=\pi^\sharp_{k+1,k}\phi^\star_{k+1}`. That is a bad omission for a “projection stack” mechanism.
- l.245-253: “converges ... to `\phi^\star_k` and `R_k(\phi^\star_k)=0`.” The later text calls this a fixed-point clause, but the definition does not explicitly require `\Psi_k^t\phi^\star_k=\phi^\star_k`. Add it or stop calling it fixed-point selection at the definition level.
- l.296-313: Hypothesis 3.2 is a hypothesis; source P4 supports only the mass-only finite-level case. The sentence l.306-310 still needs “linear gradient/vector-field operators” if it is meant to imply source-style operator intertwining, not merely vector-field intertwining.
- l.320-335: Proposition 3.4. The proof establishes residual-zero propagation and fixed-point propagation under the two hypotheses, assuming the top state is genuinely fixed for all `t`. It does not establish event existence or lower-rung convergence; Remark 3.5 correctly says this.
- l.356-378: Remark 3.5 mostly fixes the prior over-claim. But l.375-377, “external resolution either by intermediate absorption or by attractor selection,” is interpretive, not established by the proposition.
- l.394-423: 600-cell carrier facts. Vertex count, degree, shell sizes, and spectrum are locally supported. But l.413-421 slightly overstates “theorem-grade” status for the spectrum: P2 records the spectrum via the standard `2I` character table plus checks, not an independent proof from first principles.
- l.427-439: `C_\varphi` norm and correlation. Supported by `results.json`; exact norm follows from `\lambda_{\min}(L)=0` and the shift.
- l.473-485: observer-process tuple. Definition only; no proof needed.
- l.501-512: ARIA empirical anchor. Verified against the ARIA paper locally, including `18/18`, `6/6`, `-11.58\sigma`, and `+6.80\sigma`. Still imported empirical evidence, not a theorem.
- l.535-549: b-anomaly witness. Verified in `../BANOMALY-001/vfd-b-anomaly`: the sign-uniformity and AIC weights match. Properly caveated as not model preference.
- l.649-653: closing claim “residual propagates ... until a closure-compatible attractor is selected.” Still too strong unless explicitly conditioned on occurrence of a Definition 3.1 event.

**2. Internal Consistency**
- Main conflict: Definition 3.1 requires projection-compatible initial data but not a projection-compatible terminal tower, while the rest of the paper talks as if the crystallised tower is compatible.
- `\phi_k` vs `\Phi_k` is now consistent.
- “lemma” appears only in the unused theorem declaration; no prose/theorem instances remain.
- No unresolved references appear in the existing log. No `\eqref` uses are present.
- The `app:fsa-A/E/F` labels exist, but the text still references only `Appendix~\ref{app:field-signature-audit}~A/E/F`; those links go to the parent appendix, not the subsection targets.

**3. External Consistency**
- `CascadeClosureDynamics`: verified. The current paper’s mass-only caveat is accurate.
- `CascadeRefinementSpaces`: verified for finite-level spaces, bonding maps, and commuting identities. It does not supply monotonicity or flow results; current text mostly respects this.
- `CascadeAlgSubstrate`: verified for `E_8 -> H_4` projection and `V_600 ≅ 2I`. Caveat: spectrum provenance is character-table/imported-computation dependent.
- `SmartARIAChess`: verified for the empirical numbers. Runtime-level Tier 2 claims remain unpinned to a commit.
- `SmartBAnomaly`: verified locally in sibling repo. The AIC-inconclusive wording is correct.
- `SmartV`, `SmartVRev`: cited only as out-of-scope context; local sources exist.

**4. Tightness**
- l.413: replace “under which these facts are theorem-grade” with “under which the group-identification and shell-class facts are theorem-grade; the spectrum is imported from the standard `2I` character table and locally checked.”
- l.501: “Empirical anchor” -> “Empirical witness profile.”
- l.375-377: replace with “If either hypothesis fails, this proposition gives no propagation conclusion across that step.”
- l.649-653: replace with “if a cascade-closure event occurs, the stipulated resolution is selection of a closure-compatible attractor.”

**5. Surface Issues**
- `verify_kernel.py` fails in this read-only session because it writes `results.json` before printing. The existing `results.json` supports the claims, but the advertised re-run is not read-only robust.
- Existing LaTeX log shows overfull boxes in the claim ledger around l.562-618, especially l.580-581.
- Unused `lemma` and `interpretation` theorem declarations are harmless but untidy.
- `ariaChessRepo` bibliography entry still has no URL or commit hash.

**6. Top Three Fixes**
1. Fix Definition 3.1 at l.245-253: require terminal projection compatibility and explicit fixed-point invariance.
2. Pin `ariaChessRepo` with a commit hash in the bibliography and Appendix mapping, l.515 and l.730-738.
3. Remove residual over-claiming at l.375-377, l.413-421, and l.649-653; these are still stronger than the mathematics establishes.

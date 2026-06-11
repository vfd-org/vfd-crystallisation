All line references below are to [cascade-mechanism.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-mechanism/cascade-mechanism.tex:1>).

**1. Claim Audit**

- “prove a conditional residual-compositionality lemma” (l.61-63) and “We state this as a conditional lemma” (l.288-290): false label. The formal result is Proposition 3.4 (l.313). This is not mathematical damage, but Round 3’s lemma/proposition cleanup did not fully land.

- Definition “Cascade closure” (l.236-250): the quadruple rewrite landed, but the definition is still not well typed. It includes flows but no initial conditions, while occurrence depends on “the relevant initial condition” (l.246-247), never defined. It also uses `\Phi^\star_k` as a state although `\Phi_k` is the state space (l.238-245). This needs repair before publication.

- Proposition “Conditional closure-residual compositionality” (l.313-327): the proof establishes exactly residual-zero propagation and fixed-point propagation under Hypotheses 3.2 and 3.3. It does not establish existence, top-rung convergence, lower-rung convergence from specified initial data, or that a full Definition 3.1 cascade event occurs. The text mostly respects this boundary.

- “Flow intertwining implies operator intertwining” (l.302-304): overcompressed. This needs differentiability/linear-gradient assumptions and an identified generator. As written, it is not a generic consequence in the arbitrary `R_k` setting.

- “gradient operator, energy dissipation, coercive contraction … flow intertwining” imported from `CascadeClosureDynamics` (l.201-216, l.562-564): verified locally. The current caveats are correct: the source proves finite-level `F_n` results and mass-only flow intertwining, not arbitrary `R_k` dynamics.

- `V_{600}` facts: “120 vertices,” “degree 12,” shell sizes, nine eigenvalues, integer set `{0,9,12,14,15}`, and `94/26` split (l.379-407): verified locally against `CascadeAlgSubstrate` and the sigma audit script. No overclaim here.

- `\|C_\varphi^{-1}\|=\varphi^2` (l.417-421, l.577-579): established, conditional only on the stated unweighted Laplacian and its zero bottom eigenvalue. Stored `verify_kernel.py` output supports the numerical claims; I did not rerun that script because it writes `results.json`.

- ARIA empirical witness (l.486-496, l.583-585, l.676-686): verified against the ARIA paper. The caveats landed: methodology refinement, single seed, and node-count comparison. The node-count caveat is still too vague in this paper; it should say `ARIA |V|=120` vs `HCP ICA-50 |V|=50`.

- `b\to s\mu^+\mu^-` witness (l.521-539, l.586-588): verified in the sibling `../BANOMALY-001/vfd-b-anomaly` checkout, not inside this repo. The current AIC-inconclusive language is correct: `w_FREE_C9=0.652`, `w_VFD=0.348`; no VFD preference is claimed.

**2. Internal Consistency**

- The state/state-space slip is not fully fixed. `\Phi_k` is the state space at l.193-196, but `R_k(\Phi_k)>0` appears at l.254-255, and `\Phi^\star_k` is used as a state at l.245-248. Use `\phi_k`, `\phi^\star_k` for configurations.

- The status remark says “a triple” (l.268-269), but Definition 3.1 is now a quadruple (l.236-244). This is a direct leftover from the pre-fix version.

- Cross-references and bibliography keys resolve by static scan. No missing `\ref` or `\cite` keys found.

- Appendix A/E/F labels exist (l.650, l.665, l.676), but they are on starred subsections. If they are meant as hyperlink targets, add `\phantomsection` or make them numbered/custom-labelled.

**3. External Consistency**

- `CascadeClosureDynamics`: verified for gradient operator, flow existence, energy dissipation, coercive contraction, refinement-compatible operator definition, and mass-only flow intertwining. The present paper’s mass-only caveat is necessary and correct.

- `CascadeRefinementSpaces`: verified for bonding maps and intertwining identities. The paper’s l.214-216 wording attributes “state spaces” to theorem labels; those are definitions plus Theorems `thm:bonding` and `thm:commute`, not theorems alone.

- `CascadeAlgSubstrate`: verified for `E_8 -> H_4` projection, `V_{600}\cong 2I`, shell-class structure, spectrum, and `94/26` split. Spectrum values depend on imported `2I` character-table data, as the source itself says.

- `SmartARIAChess`: verified for `18/18` after methodology refinement, `6/6` on seed 42, and HCP `-11.58 sigma` with node-count caveat.

- `ariaChessRepo`: sibling checkout exists and contains the named Tier 2 modules. The paper correctly admits no commit hash (l.713-717); that is not publication-grade provenance.

- `SmartV`, `SmartVRev`: verified as out-of-scope spectral mass-projection context. The current paper makes no substantive mass claim from them, which is appropriate.

**4. Tightness**

- l.55-57: “generalises” is too strong. Edit: “is proposed as a structural generalisation of”.

- l.424-426: “through which all subsequent witnesses … are wired” is programme language. Edit: “is the operator used here to connect the substrate to the witnesses below.”

- l.486: “anchored empirically” overstates an imported witness. Edit: “illustrated by the empirical substrate-witness preprint”.

- l.612-613: “supported by an externally preregistered substrate-witness profile” is acceptable only with caveats. Edit: “accompanied by the caveated substrate-witness profile”.

- l.632-636: closing statement should remain conditional. Edit: “in systems satisfying the stated residual, projection, and intertwining hypotheses”.

**5. Surface Issues**

- Remaining “lemma” instances at l.62 and l.289 should be “proposition”.
- Remaining “triple” at l.268 should be “quadruple”.
- `R_k(\Phi_k)` at l.254-255 is type-wrong.
- Node-count caveat should be explicit, not “stated node-count comparison” (l.495, l.583-584, l.683-684).
- Static scan found no undefined custom macros, missing labels, or missing bibliography keys.
- I did not run a full LaTeX compile; the workspace is read-only and compilation would write aux/log artifacts.

**6. Top Three Fixes**

1. Fix Definition 3.1 and its remarks (l.236-280): add initial data or define “relevant initial condition”; use `\phi^\star_k` for states; change “triple” to “quadruple”; change `R_k(\Phi_k)>0` to `R_k(\phi_k)>0`.

2. Clean the proposition boundary (l.61-63, l.288-327): replace remaining “lemma” wording and state explicitly that Proposition 3.4 proves residual/fixed-point propagation only, not event existence or convergence from lower-rung initial data.

3. Make external provenance publication-grade (l.583-588, l.676-717): spell out `120` vs `50` for the HCP comparison, and pin the `ariaChessRepo` commit hash used for Tier 2 module claims.

Publication ready: no

**Claim Audit**
- Exact 600-cell claims are mostly clean. The eigenvalue proposition (`line 150`), narrow uniqueness theorem (`lines 177-183`), dual-population proposition (`lines 215-220`), `R_D(4)=15` theorem (`lines 243-264`), and Hopf-fiber proposition (`lines 273-281`) are all properly scoped as imported from P2 or conditional on classical inputs. The local scripts support the narrow claims where checked.
- The proton corollary is mathematically a direct substitution claim (`lines 318-331`) and the substitution is coherent. But the proof’s reproducibility sentence is false: `line 331` says `run_rigorous_verification.py` uses `R_D(4)=15`; the script still has `R_D = {2: 1.0, 3: 2.0, 4: 10.0}` at `scripts/run_rigorous_verification.py:53`.
- The `9 multiplicative coefficients + 1 neutron correction` framing is correct in manuscript prose (`lines 41, 77, 410, 433, 456`). But the principal verifier contradicts it: `run_chain_forward_derivations_v2.py:3-10` still says “all ten chain ratios” and `10/10 forward`, and `:217-231` still prints the old neutron mass-level formula and “10/10 forward chain entries.” Round-1 fix (a) is not complete.
- The neutron formula in the paper is now the right sign/form: `sin^2 theta_n = sin^2 theta_p - 15 alpha^2` (`lines 428, 445-449`). However `line 449` claims this is “the actual implementation in the verification scripts”; that is false for the v2 script, and only partially true for `run_exact_theta_patterns.py`, which uses `sin^2 theta_p = 15 alpha` (`scripts/run_exact_theta_patterns.py:333-340`) rather than the paper’s proton anchor `12/(26 phi^3)`. Round-1 fix (b) is therefore only fixed in prose, not in the verification trail.
- The fine-structure claim is properly weakened at `line 358` as an engineered arithmetic coincidence. But the manuscript still calls `alpha` “forward-traceable” in several places (`lines 41, 77, 82, 453, 679`). That word is too strong for a chosen arithmetic correspondence.
- The `0.014%` average mass correspondence (`lines 41, 77, 499, 679`) is presented as a numerical correspondence, not a theorem. That is acceptable as tone, but the named scripts do not currently reproduce the stated chain cleanly.
- The null-hypothesis appendix overclaims. `line 690` says random trials produced “mass predictions” evaluated against the observed spectrum. The script actually compares `sin^2 theta` proxies against the framework’s own `sin^2 theta` values (`scripts/run_null_hypothesis.py:73-88`), uses the old neutron expression (`:68`), and simplifies random neutron to proton (`:115`). This claim is not established.
- The three-witness framing is substantially repaired: `lines 109, 128, 131, 135` now avoid “same shell decomposition” and correctly say shared graph-level substrate, not identical auxiliary structure. But `lines 49, 109, 131` still say each witness is independently reproducible while also admitting the b-anomaly primary is absent and not locally audited. That should be weakened.

**Internal Consistency**
- No missing `\ref`/`\eqref` targets found in a static scan.
- The manuscript’s current epistemic status conflicts with its scripts in four places: neutron formula, `10/10` framing, `R_D(4)=15` use in `run_rigorous_verification.py`, and the null-hypothesis test.
- `run_alpha_geometric.py` also still prints overclaims: “all 13 particles exact” and “ALL masses from geometry alone. Zero observation needed” at `scripts/run_alpha_geometric.py:630,637`, contradicting the manuscript’s careful “numerical correspondence” language.
- Assignment non-uniqueness is honestly stated at `line 553`; the assignment script confirms multiple admissible choices and even shows rule-only failures for down/bottom, so the manuscript is right to call this a selection scheme, not a uniqueness theorem.

**External Consistency**
- P2 claims are locally verifiable: eigenvalues, BFS shells, dual populations, `R_D(4)=15`, narrow uniqueness, and Hopf-cycle spectrum are present in the cited P2 material.
- Papers I/IV support the closure invariant and `1265/81` proton/electron exponent attribution.
- Original Paper V does contain the old five-forward/five-reverse chain and old neutron mass-level formula, so the historical contrast is accurate.
- Paper XXX supports the Born-weight caveat: its theorem is conditional and scoped to `N >= 3`, not this `N=2` case.
- Papers XXIX/XXXIII/XXXVI support the observer/projection/F1-F8 narrative, but as interpretive and conditional infrastructure. The present paper mostly preserves that status.
- ARIA/closure-kernel facts are locally supported only through the secondary closure-kernel/ARIA materials. The b-anomaly primary repository is not present, so the b-anomaly witness remains not locally verified.

**Tightness**
- `line 41`: replace “whose two structural inputs … are themselves forward-traceable” with “whose coefficient is identified with `R_D(4)` and whose `alpha` input is the separate arithmetic correspondence.”
- `line 49`: replace “are each independently reproducible” with “are reported as independently reproducible in their respective repositories; the b-anomaly primary is not locally audited here.”
- `line 449`: delete “which is the actual implementation in the verification scripts” unless all named scripts are updated.
- `line 690`: replace the appendix paragraph with “This script tests a simplified `sin^2 theta` chain proxy, not full mass predictions against experiment.”

**Surface Issues**
- Unicode em dashes occur at `lines 438-440`; with no `inputenc` package, replace with `---` or add UTF-8 support.
- Static scan found no undefined references or missing citation keys, but I did not compile because the workspace is read-only and LaTeX would write aux files.
- The script prose is now the largest surface problem: it will mislead any reader who runs the verification commands.

**Top Three Fixes**
1. Update `run_chain_forward_derivations_v2.py` to remove all “10/10” language and the old neutron mass-level formula; this directly contradicts `paper-v-revisited.tex:41,77,410,458,626`.
2. Align neutron verification with the manuscript: either make `run_exact_theta_patterns.py` use the paper’s proton anchor `12/(26 phi^3)` and reproduce Table 1, or stop claiming it verifies the displayed neutron mass (`lines 428-449`).
3. Rewrite or remove Appendix A until `run_null_hypothesis.py` actually tests full mass predictions against observed masses with the current neutron formula (`line 690`).

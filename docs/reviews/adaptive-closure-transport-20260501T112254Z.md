**1. Claim Audit**

- `Theorem~\ref{thm:edge-decomp}` at line 289 is mostly established only for the **undirected** 600-cell edge set. The proof plus script support: 720 edges, free left `2I` action, six orbits, and the regular-representation multiplicities. It does **not** establish the advertised “explicit 6-orbit decomposition” in the strong sense: no orbit representatives, projection operators, or basis-level decomposition are given. If “explicit” means “computed multiplicities,” say that.
- The same theorem conflicts with the paper’s earlier definition of `E_M` as an “oriented edge set” at line 135. Six free orbits is correct for 720 undirected edges; for oriented edges the carrier would be 1440-dimensional. The theorem needs a separate notation such as `E_M^{und}` for conductivities and `\vec E_M` for currents.
- The representation statement at lines 295-299 is imprecise: the real edge space is written as a sum of complex irreps. State this after complexification, or give the real-type decomposition.

- `Theorem~\ref{thm:lyapunov-closure}` at line 239 is **not claim-audit clean**.
  - The domain inclusion at line 247 is false. The claim says `\{W_e>-\varphi^{-2}/d_{\max}\}` lies inside `L_W+\varphi^{-2}I>0`. For the 600-cell graph, `d_max=12` but the unweighted Laplacian has `lambda_max≈15.708`; taking uniform `W=-0.99\varphi^{-2}/12` satisfies the stated bound yet gives a negative eigenvalue for `L_W+\varphi^{-2}I`. This must be corrected.
  - Strict convexity follows on the actual positive-definite domain from the inverse quadratic term plus `\lambda I`; that part is plausible.
  - Coercivity as `||W||→∞` is not enough for global convergence on an open positive-definite domain. The proof does not rule out hitting the finite boundary where `L_W+\varphi^{-2}I` loses positivity.
  - Global convergence at line 249 is only justified if the flow is posed on a closed invariant domain, probably `W\ge0`, or if boundary repulsion/invariance is proved. The proof at lines 259-269 does neither.
  - The “hyperbolicity automatic” language at lines 66, 272, and 443 is overclaimed. A unique algebraic solution `\psi^*=(L_W+\varphi^{-2}I)^{-1}f` is not a hyperbolic fast subsystem unless the fast ODE and its linearisation are specified.
  - Calling this a closure of `Hypothesis~\ref{hyp:lyapunov}` is too strong. It closes a deliberately artificial gradient-flow example, not the original coupled transport law `G(\rho,j,W)`.

- `Fact~\ref{fact:passive}` at line 171 is fine as a conditional reduction. It correctly says that freezing `W` recovers P1, P19, P30, and P34 only after the corresponding hypotheses are imposed.
- `Hypothesis~\ref{hyp:selection}` at line 227 is correctly labelled as a hypothesis. Do not let later prose imply it has been proved generally.
- `Fact~\ref{fact:vertex-decomp}` at line 281 is consistent with P2: P2 supplies the vertex-space `2I` decomposition, not edge conductance dynamics.
- `Hypothesis~\ref{hyp:cascade-selection}` at line 313 is acceptable as a hypothesis, but line 325 says the edge decomposition is not carried out in the present paper. That is stale and contradicts Theorem 4.2.
- `Fact~\ref{fact:classification-formal}` at line 338 is definition-level and fine. `Hypothesis~\ref{hyp:classification-biological}` at line 347 is speculative but honestly labelled.
- The numerical section overclaims. Line 543 says the scripts “verify the two new theorems.” The edge script supports the finite orbit computation. The Lyapunov script demonstrates one Euler trajectory with a positivity clip; it does not verify strict convexity, coercivity, global convergence, or the Łojasiewicz exponent. Lines 597-598 should say “consistent with,” not “confirms.”

**2. Internal Consistency**

- Major notation conflict: `E_M` is oriented at line 135, but Theorem 4.2 and `verify_2I_edge_action.py` use the undirected 720-edge graph. This affects the theorem, numerical section, and any interpretation of `W_e`.
- The abstract contradicts itself. Line 58 says the edge-space decomposition remains open; lines 65 and 68 say the paper now supplies it.
- Stale “edge-space lift not supplied” language remains at lines 83, 91, 279, 325, 392, and 454. These statements must be rewritten after adding Theorem 4.2.
- ARIA status is inconsistent. Lines 92, 369, and 388 still say repository-backed ARIA verification is pending, while lines 68, 445, and 513-519 cite the `aria-chess` witness.
- The conclusion at lines 451-457 is no longer a conclusion: further substantive sections, including programme position and numerical evidence, follow it. Move the numerical and programme sections before the conclusion, or rename that section.
- I saw no obvious unresolved `\ref`/`\eqref` target from the source scan, but I did not compile the LaTeX because the sandbox is read-only and a normal build writes aux files.

**3. External Consistency**

- P1 / `transport-law.tex`: verified locally. It supports the passive transport-law reduction and presents the U(1), Schrödinger-current, and dispersion material as conditional or heuristic where appropriate.
- P2 / `cascade-algorithmic-substrate.tex`: verified locally. It establishes `V_{600}` as the binary icosahedral orbit and gives vertex-space irreducible data. I found no edge-space decomposition or adaptive `W` theorem there. The adaptive paper is right that P2 did not supply this, but wrong where it still says the present paper does not supply it.
- P19 / `SmartXIX`: verified locally. It contains a residual Schrödinger-limit construction and norm conservation, not a feedback law for `W`.
- P30 / `SmartXXX`: verified locally. Route C and Route E are conditional reconstructions, not biological slow-attractor theorems.
- P33 / `SmartXXXIII`: verified locally. The closure-projection principle is proposed and partly classified, not a completed biological selection theorem.
- P34 / `SmartXXXIV`: verified locally. The Kostant-gauge material is a convention/hypothesis, not a derivation of the adaptive closure mechanism.
- `CascadeAlphaChain`: verified locally. It supports cautious language about photon and microtubule claims; several items are explicitly marked incomplete or conditional.
- `CascadeMetaLayer`: verified locally. It supports the meta-layer structural claims, but not an identification of that layer with the present `W`-space dynamics.
- `SmartARIAClosureKernel2026`: present in the bibliography but not cited in the adaptive paper’s text. This is a citation failure. The paper instead cites `docs/aria-closure-kernel.md` around lines 473-480.
- `SmartARIAChess2026`: verified locally in the closure-kernel bundle. It supports the active-regime witness claims: six signatures at seed 42 and the 18/18 refined correspondence table. It does **not** establish a selection theorem, consciousness theorem, or uniqueness of the 600-cell substrate. Also, the source calls itself “Preprint, not peer-reviewed”; line 514 should not call it a “published preprint.”
- `SmartBAnomaly2026`: the cited source is outside the checked local paper set. I could not verify that claim from the repository material I inspected.

**4. Tightness**

Suggested one-line edits:

- Line 65: replace “explicit 6-orbit edge-space decomposition” with “computed six-orbit decomposition of the undirected 600-cell edge set,” unless orbit representatives are added.
- Line 66: replace “closes the Lyapunov selection hypothesis” with “gives a closed finite-dimensional gradient-flow example satisfying the Lyapunov selection pattern.”
- Line 247: replace the claimed `d_{\max}` lower bound with either `W\ge0` or the correct spectral condition involving `\lambda_{\max}(L_{\rm unweighted})`.
- Line 249: replace “global convergence” with “global convergence on the stated invariant positive-conductivity domain,” after proving invariance.
- Line 272: replace “hyperbolicity automatic” with “the algebraic fast equilibrium is unique; hyperbolicity follows only after specifying a stable fast relaxation equation.”
- Line 361: replace “is exactly the formal distinction between non-living and living” with “models a proposed formal distinction between passive and adaptive regimes.”
- Line 543: replace “verify the two new theorems” with “exercise the finite edge computation and one representative Lyapunov-flow instance.”
- Lines 597-598: replace “confirms the Łojasiewicz--Simon exponent” with “is consistent with exponential convergence predicted by strong convexity.”
- Line 514: replace “published preprint” with “released preprint.”

**5. Surface Issues**

- Stale text remains throughout: lines 58, 83, 91, 279, 325, 392, and 454 still describe the edge-space decomposition as open.
- `SmartARIAClosureKernel2026` is unused despite being central to the new bundle framing.
- The paper mixes ASCII LaTeX conventions with literal Unicode: especially `Łojasiewicz–Simon` and dash characters. If compiling with modern UTF-8 engines this may be fine; otherwise normalize to `{\L}ojasiewicz--Simon` and TeX dashes.
- `\textsubscript` at line 271 may be brittle depending on the LaTeX setup. `V_{600}` is safer.
- The repro scripts write JSON outputs to the current working directory, not necessarily their own `repro/` directory. The paper should either instruct `cd papers/.../repro` before running, or the scripts should write relative to `__file__`.
- `verify_2I_edge_action.py` says “100 random pairs” in its docstring but actually tests 200; the manuscript says 200. Fix the script docstring.
- The Lyapunov script clips `W` to positivity during integration. That is a projected/numerically safeguarded flow, not exactly the unconstrained gradient flow stated in the theorem.

**6. Top Three Fixes**

1. Fix Theorem 4.1 before anything else. Correct line 247, restrict the domain or prove invariance, specify the fast subsystem if claiming hyperbolicity, and weaken lines 66, 249, 272, 442, and 597-598. As written, the theorem overstates what the proof establishes.

2. Resolve the edge-space notation conflict. Decide whether `E_M` is oriented or undirected. The six-orbit theorem is for undirected conductance edges; currents need a separate oriented edge set. Repair lines 124, 135, 150-152, 203-205, and Theorem 4.2 accordingly.

3. Remove the stale programme-status contradictions. The abstract and conclusion currently say both “edge decomposition open” and “edge decomposition proved.” Update lines 58, 83, 91, 279, 325, 392, and 454, cite `SmartARIAClosureKernel2026` in the text, and stop describing ARIA verification as pending where the closure-kernel bundle is now being used.

Publication ready: yes.

Must-fixes: none. I found cleanup issues, but no remaining publication-blocking overclaim.

**1. Claim Audit**
- `Fact: passive regime` at line 172: established as a definitional reduction. The updated transport-law attribution at lines 159 and 175 is now correct for the Schrödinger-limit `H=L` theorem; the Langevin/noise case remains explicitly conditional.
- `Hypothesis: selection statement` at line 228: correctly labelled as a hypothesis, not proved. The text now carries the needed load: timescale separation, Lyapunov potential, hyperbolicity, global existence/precompactness, Lojasiewicz-Simon, Morse genericity, and no full-system convergence claim.
- `Theorem: closure-derived Lyapunov` at line 240: proof establishes strong convexity, coercivity, unique constrained minimiser, projected/subgradient flow well-posedness, contraction, explicit gradient, and fast linear hyperbolicity. Minor caveat: if `rho` is meant literally as a nonnegative density, line 241 should assume `f >= 0` or call the fast variable `psi`; otherwise arbitrary signed `f in R^{V_600}` can produce a signed field.
- `Theorem: edge-space decomposition` at line 301: proof establishes the claim, conditional on the standard icosian/quaternion realisation of `V_600`. The orbit count and isotypic dimensions match the recorded JSON witness.
- `Hypothesis: cascade-selection` at line 325: assumptions imply equivariance of the reduced `W`-flow and orbit-symmetry of the critical set. The text correctly disclaims blockwise decoupling.
- `Fact: passive/active dichotomy` at line 350: purely definitional and valid.
- `Hypothesis: long-time behaviour` at line 359: now properly scoped as conjectural and chained through the analytic hypotheses.

**2. Internal Consistency**
- All `\ref`/`\eqref` labels used in the file resolve to labels present in the file. All cited keys have matching `\bibitem`s.
- The ARIA dictionary/witness distinction at lines 381 and 400 is now internally coherent.
- One residual terminology tension: line 457 says the ARIA trajectory “empirically realises the active regime,” while lines 381 and 400 correctly say the row-by-row ACT dictionary and `G`/`V` extraction remain unverified. Prefer “is presented as an active-regime substrate witness.”
- Minor source-convention tension: ACT uses photon `W_0 > 0` uniform at lines 179 and 419; the transport-law paper says “In ARIA terms” photon corresponds to `W=0`. This is not fatal because the symbols are not clearly the same object, but line 419 should say ACT is using its conductivity convention.

**3. External Consistency**
- Transport-law paper: verified. Its Theorem `thm:u1-explicit` proves the unconditional Schrödinger-limit continuity/current/conservation claim; dispersion remains a hypothesis.
- P2: verified. P2 supplies vertex-space `2I` isotypic preservation and the `94+26` split; it does not supply edge-space decomposition, `W`-dynamics, Lyapunov potentials, or selection.
- Paper XIX: verified. It establishes a nonlinear residual and exact `L^2` conservation, but no transport-level `W` feedback law.
- Paper XXX: verified. Route C is conditional stationary-measure/Born weighting; Route E is conditional Gleason uniqueness under the `N >= 3` package.
- Paper XXXIII: verified. It labels the closure-projection measurement principle as a candidate/proposed template, not a closed theorem.
- Paper XXXIV: verified. The `88 -> 87` phason-slot count is a Kostant-gauge hypothesis/convention, not theorem-level pinning.
- Cascade alpha-chain: verified. `T_PH_2` is marked “needs polish”; `T_MT_1` is structural conjecture.
- ARIA chess: verified. Lines 526-528 now correctly include both P4 `N=20` and P13 state-reset/leave-one-out refinements.

**4. Tightness**
- Line 81: change “It is the regime of...” to “It includes regimes such as...”
- Line 259: change “sign-positive since the edge potential is convex in `W`” to “positive in the gradient flow because the inverse-response term is Loewner-decreasing in `W`.”
- Line 457: change “empirically realises the active regime” to “is presented as an active-regime substrate witness.”

**5. Surface Issues**
- Line 175: `Theorem~thm:u1-explicit` is raw label text. Use “Theorem `thm:u1-explicit` of the transport-law paper” or cite by section; do not make it look like a broken local `\ref`.
- No undefined local refs or missing bibliography keys found by text audit.
- I did not rerun the repro scripts because they write result JSON files; I inspected the scripts and recorded outputs instead.

**6. Top Three Fixes**
No publication-blocking fixes.

Highest-value cleanup before release:
1. Line 457: weaken ARIA “empirically realises active regime.”
2. Line 175: clean raw cross-paper theorem-label prose.
3. Line 241/260: either assume `f >= 0` if `rho` is a density, or call the fast variable `psi` in the worked example.

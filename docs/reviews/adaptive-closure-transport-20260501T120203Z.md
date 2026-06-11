Publication ready: no.

**1. Claim Audit**
- Fact “Passive regime reduces…” (line 173): mostly established, but only after importing a specific current choice. Eq. (2.1) itself leaves `j` unspecified, so “resulting dynamics is the setting of SmartTransportLaw” needs the extra hypothesis “with the transport-law current.”
- Theorem “Closure-derived Lyapunov…” (line 241): convexity/coercivity are essentially proved. The projected-flow part is not. Lines 250-254 write `\dot W=-P_\Omega(\nabla V)` with a nonstandard projection; line 273 claims local Lipschitzness and a projected Lojasiewicz inequality without proof. For a boundary KKT flow this should be stated as `\dot W=\Pi_{T_\Omega(W)}(-\nabla V)` or as a subgradient flow for `V+I_\Omega`, with a real convergence citation/proof.
- Theorem line 281: the numerical positivity clip `W <- max(W,10^{-3})` is not a discrete-time realisation of the KKT tangent-cone flow on `\Omega`; it is a floor on a shrunken cone. This is an overclaim.
- Theorem “Explicit 2I edge-space decomposition…” (line 302): the six free edge orbits are established modulo the standard `V600=2I` identification and the unique order-2 element fact, which should be stated. The isotypic decomposition on `\mathbb R^{E_M}` is not justified as written: the proof uses complex irrep dimensions. Either state the decomposition after complexification or prove the real-representation/Frobenius-Schur bookkeeping.
- Fact “Isotypic preservation, from P2 §6” (line 294): verified against P2; it is vertex-space only.
- Fact “Definitional passive / active dichotomy” (line 351): established; smoothness makes `G\not\equiv0` nonzero on an open set.
- Numerical results (lines 555-606): JSON artifacts match the tables. But “complete numerical verification” and “confirms” are too strong; these are numerical witnesses.

**2. Internal Consistency**
- Lines 123, 126-128, and 137-149 conflict on edge spaces: `M` is first “directed,” then `E_M` is undirected plus `\vec E_M`; currents live on oriented edges but `G` takes `j\in\mathbb R^{E_M}`. Use `\mathbb R^{\vec E_M}` for `j`.
- EdgeDec is still formally conditional at lines 326-329, despite lines 58, 65, 323, and 460 saying it is discharged. Replace the EdgeDec assumption with “by Theorem 5.2.”
- Line 405 still says the ARIA edge-space lift is open. That is stale after Theorem 5.2.
- All `\ref`/`\eqref` targets resolve by source parsing. No missing bibliography keys. I could not compile: `pdflatex` is not installed.

**3. External Consistency**
- `SmartTransportLaw`: mostly verified. It has U(1) conservation and photon-sector results, but the current transport-law draft now closes the Schrödinger-limit current more strongly than this paper says. Also note a residual conflict: transport-law still says “photons would correspond to … W=0,” while this paper insists on `W_0>0` at line 180.
- `CascadeAlgSubstrate` P2: verified. P2 supplies the vertex `2I` isotypic decomposition and `94+26` split; it does not supply edge-space decomposition.
- `SmartXIX`: verified. It proves a nonlinear residual and exact `L^2` conservation; it does not give a `W`-feedback law.
- `SmartXXX`: verified. Route C is conditional stationary-measure/Born weighting; Route E is conditional uniqueness for `N>=3`.
- `SmartXXXIII`: verified as proposal/candidate measurement principle, not closed theorem.
- `SmartXXXIV`: verified: `88 -> 87` is a Kostant-gauge convention/hypothesis, not a theorem.
- `CascadeAlphaChain`: verified mixed status; `T_PH_2` needs polish and `T_MT_1` is not rigorously closed.
- `CascadeMetaLayer`: verified: moduli/groupoid/tiling layer and `T_meta \cong Z[\varphi]^2`.
- `SmartARIAChess2026`: verified with caveat. The source says `17/18` standard, `18/18` after documented refinements; six EEG signatures are single seed 42. Lines 522-526 should not imply one seed-42 trajectory proves all eighteen preregistered correspondences.

**4. Tightness**
- Line 219: change “main conditional result” to “main conditional hypothesis.”
- Line 285: change “delivered for the `V600` substrate” to “delivered for this closure-derived gradient-flow worked example.”
- Line 319: change “complete numerical verification” to “numerical witness.”
- Line 405: remove “open edge-space lift”; cite Theorem 5.2.
- Line 605: change “confirms” to “is consistent with.”

**5. Surface Issues**
- `verify_lyapunov_selection.py` docstring is stale: it says `dt=0.01`, `n_steps=500`; code/results use `dt=0.05`, `n_steps=2000`.
- The projected-flow notation `P_\Omega` is misleading and mathematically underdefined.
- Unicode dashes/Ł characters may be fine under modern LaTeX, but compilation was not checked because `pdflatex` is unavailable.
- Label name `prop:classification` is attached to a Hypothesis; not broken, but confusing.

**6. Top Three Fixes**
1. Fix Theorem 4.1 projected-gradient mathematics: lines 250-254, 273, 281. Use standard tangent-cone projection/subgradient flow and prove/cite exponential convergence.
2. Fix edge-space theorem field-of-scalars: lines 308-317. State complexification or prove the real isotypic decomposition.
3. Remove remaining stale EdgeDec/open-lift language and repair edge-current spaces: lines 126-149, 326-329, 405.

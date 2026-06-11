Publication ready: no.

**1. Claim Audit**
- Lines 127-150, “An adaptive-closure-transport substrate is a 4-tuple … together with a learning rule …”. This is not yet well-posed as a mathematical object carrying dynamics. On the page, `L_M` and `R_{\mathrm{hom}}` never enter the evolution law, and `j_{v\to w}` is left undefined. More seriously, “finite directed graph” plus “self-adjoint operator on \(\C^{V_M}\) built from adjacency-type structure” needs an explicit symmetry/weighting hypothesis; a generic directed graph does not give a self-adjoint Laplacian.
- Lines 166-172, “the resulting dynamics is precisely the setting of SmartTransportLaw.” Over-claimed. The first bullet omits the antisymmetry assumption needed in the source for conservation; `transport-law.tex` requires both continuity and \(j_{w\to v}=-j_{v\to w}\) at lines 189-198. The second bullet is only a borrowed hypothesis in the source, not a proved consequence. The third bullet, “photon-like free-field end,” is too strong: the source treats that as a further conditional identification under the open \(T_{\mathrm{PH}}\) chain, not as part of the passive reduction (`transport-law.tex` lines 309-312).
- Lines 221-223, “the slow \(W\)-dynamics … converges … to a local minimum of \(V\). … The set of selected operating points is discrete”. As a Hypothesis, the status label is acceptable. As stated mathematical content, it is stronger than the premises given on lines 213-219. Gradient structure plus bounded-below \(V\) does not by itself yield convergence to local minima, nor discreteness of the limit set; you need additional analyticity/Morse/Łojasiewicz-type hypotheses. The remark on lines 225-226 quietly admits this.
- Lines 243-245, “selection is quantised by the cascade spectrum: only operating points respecting the \(94+26\) split can be selected”. This is not established. P2 gives an isotypic decomposition of the vertex representation \(\C^{V_{600}}\), not of the edge-conductivity space \(\R^{E_M}\). You never define a \(2I\)- or \(H_4\)-representation on \(W\), nor show that equivariance of \(G\) forces \(V(W)\) or the \(W\)-flow to decompose by those vertex blocks.
- Lines 259-269, Proposition “every stable operating point … falls into exactly one of the two regimes”. The proof sketch does not prove the stated proposition. The statement assumes only structural stability; the proof additionally uses Hypotheses 5.1 and 5.2, assumes gradient flow, assumes Morse-generic discreteness, and excludes persistent non-gradient behaviour by scope declaration rather than argument. This cannot stand as a proposition in the present form.
- Lines 280-300, ARIA dictionary. Status is honest: proposal only, pending verification.
- Lines 311-333, application catalogue. Status is mostly honest: targets, not derivations. The photon row is still mathematically incoherent with the rest of the paper; see consistency below.

**2. Internal Consistency**
- Lines 167 and 319 conflict. In the passive reduction, “\(W_0\) trivial (all edges equal)” is the transport-law specialisation. In the application table, Photon has “\(W\equiv 0\) (free)”. Those are not the same regime. Under your active ansatz \(j_{v\to w}=-W_{vw}(\rho_v-\rho_w)+\mu\rho_v(\nabla W)_{vw}\), \(W\equiv 0\) gives zero diffusive transport, not free propagation.
- Lines 118, 132, 218, 240, 244 use \(W\) as an edge-space variable but import isotypic blocks from a vertex-space decomposition. The central structural claim of Sections 5-6 is therefore not type-consistent.
- Line 135 uses an \(H_4\)-action; lines 239-245 use the left-regular \(2I\)-action. You need to say exactly which group acts on which space and how those actions are related. At present the paper slides between them.
- Line 346 reuses \(G\) for the meta-layer groupoid, conflicting with \(G(\rho,j,W)\) as the learning rule on line 121.
- Cross-reference discipline is poor. Line 200 has `\eqref{eq:continuity}` to a label in another paper, so it will not resolve locally. Lines 74, 153, 169, 170 print raw labels instead of references.

**3. External Consistency**
- `SmartTransportLaw`: verified locally. Discrete continuity is only a programme target (`transport-law.tex` lines 160-166); \(U(1)\) conservation is conditional on continuity plus antisymmetry (189-198); dispersion is explicitly a heuristic hypothesis (228-237). The present paper overstates the imported photon claim at line 171.
- `CascadeAlgSubstrate` P2: verified locally. Shell-adjacency class sums are central and act blockwise on isotypic components (P2 lines 1084-1097). The \(94+26\) split is explicitly recorded (1166-1185). What P2 does not supply is any statement about \(W\)-dynamics, Lyapunov functions, or selection.
- `SmartXIX`: verified locally. It defines and studies the nonlinear closure residual as a scalar nonlinear remainder (`paper-xix.tex` lines 77-87, 94-172, 390-402). I do not find any learning rule \(G(\rho,j,W)\), any Lyapunov potential for substrate dynamics, or any transport-level \(W\)-feedback law there.
- `SmartXXX`: verified locally. Route C is a stationary-measure/Born-weighting argument (`paper-xxx.tex` lines 282-365); Route E is a conditional uniqueness package. I do not find anything that “coincides with the existence of a slow-manifold attractor \(\rho^*(W)\)”. Line 343 is not supported by the cited source.
- `SmartXXXIV`: verified locally. It does contain the Kostant-gauge convention as an explicit hypothesis/convention for \(88\to87\) (`paper-xxxiv.tex` lines 147-160). I do not find support for the stronger statement that it “pins one specific slot structure inside the \(2I\)-isotypic decomposition”.
- `CascadeMetaLayer`: verified locally. It does establish a moduli/groupoid/sheaf layer \((\mathcal M,G,F)\) and \(T_{\text{meta}}\cong \mathbb Z[\varphi]^2\) (`cascade-meta-layer-theorem.md` lines 13-17, 132-136). It does not identify that moduli space with the present paper’s \(W\)-space. Line 346 overstates.
- ARIA repository: not verifiable from this repo. The draft is mostly honest about that.

**4. Tightness**
- Line 78, “proves a conditional selection statement”:
  Replace with: “states a conditional selection hypothesis”.
- Line 230, “it guarantees the structural form of the answer”:
  Replace with: “it suggests the structural form of the answer, contingent on additional analytic hypotheses.”
- Lines 248-249, “derived from the P2 commutant facts, and does not require any further physics input”:
  Replace with: “motivated by the P2 commutant facts, but requiring an explicit lift to the \(W\)-dynamics.”
- Line 343, “coincides with”:
  Replace with: “is at most loosely analogous to”.

**5. Surface Issues**
- Line 200: broken `\eqref{eq:continuity}` to an external-paper label.
- Lines 74, 153, 169, 170: raw labels printed instead of `\ref`/`\eqref`.
- Abstract line 50 calls \(R_{\mathrm{hom}}\) a “boundary operator”; Definition 2.1 line 133 makes it a projection. Pick one description.

**6. Top Three Fixes**
1. Lines 243-249 and line 58: rebuild or drastically weaken the cascade-selection claim. As written, the argument is not even on the right space: P2 controls \(\C^{V_{600}}\), while your selection variable is \(W\in\R^{E_M}\).
2. Lines 221-230 and 259-269: downgrade theorem-like rhetoric around selection/classification, or add the missing hypotheses and real arguments. Right now the paper states results stronger than the proof/status supports.
3. Lines 166-171, 319, 343-346: repair the imported attributions. Restore the missing antisymmetry caveat from the transport-law paper, remove the unsupported Paper XXX analogy, and fix the photon inconsistency \(W\) trivial vs \(W\equiv0\).

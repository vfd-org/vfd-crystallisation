No files edited. I read the task/context and ran the existing exact scripts read-only.

**SECTION A. Insight / External Content Relevance**
Already in cascade papers / repo:
- `F1 -> phi -> sigma` is supported in `cascade-12d-closure.tex:247-270`; `O_K=Z[phi]`, PID, and module freeness are in `:284-358`.
- Icosian/E8 substrate is in `cascade-12d-closure.tex:366-393`; the stronger icosian star/twin substrate is in `cascade-algebraic-substrate.tex:516-527` and `:600-619`.
- `V_600 = 2I`, exact closure, and shell = conjugacy class are in `cascade-algebraic-substrate.tex:964-1109` and restated in `paper-xxii.tex:200-222`.
- Paper XXII states the E8 to H4 two-to-one Galois pairing at `paper-xxii.tex:234-238`, and keeps the conjugate-pair reading structural at `:355-365`.
- B5/B6 exact sim supports order-10 classes, `tau^5=-1`, 12 cycles, and unweighted zeta: `derive_pentagonal_clock_B5_B6.py:145-158`, `:169-215`, `:223-259`.
- B7/B8 exact sim supports constant transport class, σ escaping single `2I`, and naive cocycle collapse: `derive_pentagonal_clock_B7_B8.py:215-279`, `:329-377`.

Only in `insight.md` / prior-session:
- The directly relevant missing object is the local-frame holonomy connection: `insight.md:830-851`.
- The weighted Artin-Mazur zeta and `Z[phi]^x` torsion route are prior-session only: `insight.md:855-861`.
- The key reframing “σ as local connection, not only global involution” is `insight.md:867-879`.
- God-prime/QMS-3 content is later-route constraint, not needed for B8'-B10: `insight.md:670-715`.
- Observer/RH/Mellin claims are explicitly later builds: `insight.md:771-775`, with mainstream/non-mainstream split at `:798-809`.

External literature route:
- Artin-Mazur zeta: Artin and Mazur, “On periodic points,” Ann. Math. 81 (1965), 82-99 ([MathNet](https://www.mathnet.ru/eng/mat444), [JSTOR listing](https://www.jstor.org/stable/i307331)).
- Weighted dynamical zeta: Ruelle’s AMS monograph gives the weighted fixed-point formula ([AMS](https://bookstore.ams.org/CRMM/4)).
- Quasicrystal/tiling comparison route: Bellissard/Kellendonk gap-labelling and tiling C*-algebra literature, e.g. references listed in [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0393044016302820) and [Cambridge Core](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/spectral-sequence-for-the-ktheory-of-tiling-spaces/083267F1FF42E9E9648C2C3ED251AA38).

**SECTION B. Priority Gaps To Close The Task**
B1 / B8'-C0: canonical shell-unit observable.  
Object: `q(v)=||1-v||^2 in O_K`, `u:2I -> O_K^x`, with `u(1)=1`, `u(v)=q(v)/sigma(q(v))`.  
Bridge: turns the shell/class hook into a canonical unit weight using only F1’s σ plus icosian shell data.  
Route: minimal vertex-shell route.  
First step: prove exact lemma `u(v) in {1, phi^±2, phi^±4}` using the shell table, no floats.

B2 / B8'-C1: multiplicative cocycle over the clock.  
Object: `Omega_n(v)=prod_{i=0}^{n-1} u(T_tau^i v): N x 2I -> O_K^x`.  
Bridge: converts vertex-shell weights into cycle weights.  
Route: new derivation, exact finite check.  
First step: compute all 12 `T_tau` cycles and `W_C=Omega_10(c)`. Intrinsic cycle profiles give expected weights  
`W_C = 1` with multiplicity `2`, `phi^4` with multiplicity `5`, `phi^-4` with multiplicity `5`.

B3 / B9: weighted finite Artin-Mazur zeta.  
Object: `zeta_{T,u}(z)=prod_C (1-W_C z^10)^-1`.  
Bridge: cycle weights to exact zeta.  
Route: Artin-Mazur/Ruelle finite product.  
First step: certify
`zeta = (1-z^10)^-2 (1-phi^4 z^10)^-5 (1-phi^-4 z^10)^-5`, with coefficients through degree 30:
`1 + 37 z^10 + 803 z^20 + 13364 z^30 + ...`.

B4 / B10: σ-equivariance on labelled two-copy substrate.  
Object: `X = V_+ sqcup V_-`, `V_+=2I`, `V_-=sigma(2I)`, with swap `Sigma(v,+)=(sigma(v),-)`.  
Bridge: repairs the false single-`2I` σ statement.  
Route: icosian star/twin map plus finite theorem.  
First step: prove `Sigma T_tau = T_{sigma(tau)} Sigma` on `X`, and `u(Sigma v)=sigma(u(v))=u(v)^-1`; hence `W_{Sigma C}=sigma(W_C)`.

B5 / optional holonomy build: edge/frame connection.  
Object: `omega_E:E^or(G_600)->O_K^x` via a pentagonal frame bundle.  
Bridge: matches `insight.md:878-890` directly.  
Route: deeper edge-holonomy route.  
First step: define the frame fibre and gauge action; prove cycle weights are gauge-invariant. This is not the minimal B9 path.

**SECTION C. Reversals / Corrections**
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:372` replace `σ permutes 2I` with `σ does not preserve a single 2I`.
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:373` replace `covariance on adjacency verified.` with `covariance must be formulated on 2I sqcup sigma(2I).`
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:353-356` replace representative-class weighting text with `B8' weights each cycle by the product of canonical shell units u(v)=||1-v||^2/sigma(||1-v||^2); representative classes are diagnostics unless a canonical C10-coset representative is proved.`
- at `docs/pentagonal-torsion-derivation.md:341` replace `Cocycle omega(v,w)=phi^{k(v,w)}` with `B8' vertex-shell cocycle u(v)=||1-v||^2/sigma(||1-v||^2) over T_tau; edge holonomy is a separate frame-bundle build.`
- at `docs/pentagonal-torsion-derivation.md:368` replace `Cocycle omega and weighted zeta zeta_T^omega` with `B8'/B9 construct and verify the cocycle and weighted zeta by exact shell-unit cycle products.`

**SECTION D. Route Alternatives**
Route V, chosen: vertex-shell unit `u(v)=q/sigma(q)`. Minimal, exact, nontrivial, σ-pairs cleanly.

Route H: edge-holonomy/frame bundle. Best match to insight, but needs frame uniqueness and gauge-independence first.

Route L: pure `2I sqcup sigma(2I)` lift. Required for B10, but not by itself a nontrivial cocycle.

Route R: representative-class 1/3/8. Keep only if Claude proves a canonical `C10` coset representative; otherwise use intrinsic 2/5/5 shell-unit weights.

**SECTION E. Exact Verification Targets**
- B8': exact shell map, exact `u(v)`, no float comparator.
- B8': verify 12 cycle weights are `{1:2, phi^4:5, phi^-4:5}`.
- B9: exact product zeta and coefficients to degree 30.
- B10: labelled 240-point substrate, `Sigma T = T_sigma Sigma`, and `W_{Sigma C}=sigma(W_C)`.
- Holonomy route: verify `omega(e^-1)=omega(e)^-1`, H4-equivariance, σ-covariance, and gauge-invariant cycle products.

**SECTION F. Top 3 Next Builds**
1. `derive_pentagonal_clock_B7_B8.py:353-367`: replace representative-class cycle hook with intrinsic shell-unit cycle products.

2. `derive_pentagonal_clock_B7_B8.py:248-279` plus `cascade-algebraic-substrate.tex:600-619`: state B10 on labelled `2I sqcup sigma(2I)`.

3. `docs/pentagonal-torsion-derivation.md:293-311`: insert B9 product zeta and exact degree-30 coefficients from the B8' weights.

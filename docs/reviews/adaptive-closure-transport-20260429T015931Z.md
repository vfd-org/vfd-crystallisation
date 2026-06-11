**Claim Audit**

- L166-173, “Passive regime reduces to the transport-law framework”: established as a definitional reduction when `G \equiv 0`, with the same current hypotheses imported from the transport-law paper. The caveat about continuity and antisymmetry is honest.
- L222-224, “Selection statement”: not proved, but correctly labelled as a hypothesis. If treated as a theorem it would still need analyticity/LS hypotheses for the actual `V`, slow-manifold persistence, and full-system convergence.
- L240-242, “Isotypic preservation, from P2 §6”: verified for the vertex representation. It proves nothing about edge-valued `W`, and the paper says so.
- L248-257, “Cascade-selection statement”: the equivariance conclusion follows from the assumptions. However, `EdgeDec` as mere existence of an isotypic decomposition is not really open for a finite group representation; the open item is the explicit edge decomposition and its relation to `94+26`.
- L273-280, “Definitional passive / active dichotomy”: established from Definition 2.2. But the paper’s headings and abstract repeatedly say passive/active are `\dot W=0` / `\dot W\neq0`, which conflicts with the later caveat that active equilibria have `\dot W=0`.
- L282-289, “Long-time-behaviour conjecture”: correctly not proved. The statement is only as strong as Hypothesis 4.3.
- L327-328, ARIA predictions: mostly honest and conditional. Replace “should cluster” with “would be hypothesised to cluster.”
- L353, application catalogue claim: honest conditional template; no derivation claimed.
- L356, microtubule `13` claim: verified against the local alpha-chain note; `T_MT_1` is explicitly not closed there.
- L401-415, ARIA response kernel: `C_\varphi` and the Green kernel are verified in `docs/aria-closure-kernel.md` lines 12-33. The LHCb `r=0.983` witness is only reported in a separate repo, not locally verified here.
- L417-431, “same gap” / “closing it in one frame would close it in all”: not established. Local RH and NS sources explicitly call this programme-level support, not proof.

**Internal Consistency**

All `\ref`, `\eqref`, and `\citep` keys resolve by static extraction. Only `sec:intro` and `sec:aria_home` are unused labels.

The new ARIA section is after the conclusion but absent from the structure list at L102-112. It also calls itself a “subsection” at L397 while being a `\section`.

Notation collision: `G` is the learning rule throughout, but L410 reuses `G(x)` for the Green function. Use `K_\varphi(x)` or `\mathsf G_\varphi(x)`.

The formal label `prop:classification` names a `hypothesis`, not a proposition.

Passive/active notation should be repaired globally: use `G\equiv0` / `G\not\equiv0` for regimes, reserving `\dot W=0` for states.

**External Consistency**

- Transport-law attribution verified: `transport-law.tex` lines 160-167, 189-194, 228-237 support the continuity/antisymmetry and dispersion status.
- P2 attribution verified for vertex-space shell-adjacency/isotypic structure: `cascade-algebraic-substrate.tex` lines 1086-1111, 1116-1181, 2066-2077.
- Paper XIX attribution verified: `paper-xix.tex` lines 81-87 and 153-172 give a scalar nonlinear residual with exact `L^2` conservation, not a `W`-feedback law.
- Paper XXX attribution verified: Route C and Route E are conditional; see `paper-xxx.tex` lines 323-348 and 857-861.
- Paper XXXIII attribution verified: measurement principle is proposed, not closed; see `paper-xxxiii.tex` lines 47-51 and 408-420.
- Paper XXXIV attribution verified: `88 -> 87` is a Kostant-gauge convention/hypothesis; see `paper-xxxiv.tex` lines 147-160.
- Meta-layer attribution verified: `cascade-meta-layer-theorem.md` lines 13-17 and 140-144 support `M`, matching groupoid, tiling layer, and `T_meta ≅ Z[φ]^2`.
- ARIA empirical witness not locally verified: `docs/aria-closure-kernel.md` lines 57-73 says it is in `aria/vfd-b-anomaly` as a separate repo.
- Cross-frame convergence: RH lines 2786-2793 and NS lines 809-814 support “programme-level support, not proof.” Hodge/YM/BSD/PNP programme-home sections likewise do not discharge their bridge hypotheses. The L430-431 implication is therefore false as written.

**Tightness**

- L420-431: replace with “Analogous open selection/bridge layers occur in several companion drafts; this is programme-level evidence of a shared pattern, not a proved equivalence.”
- L417-420: replace “picks one closure response” with “selects a stable `W`-operating point, after which a response field may be evaluated.”
- L411-415: replace “independent empirical witness” with “reported external, unaudited empirical witness.”
- L391: replace “supplies the mathematical substrate” with “defines a proposed mathematical substrate.”
- L296: weaken broad analogies to “has analogues in” rather than “identifies a structural boundary” across QFT/biology.

**Surface Issues**

- `sec:aria_home` unused and not in structure list.
- New section should be before the conclusion or explicitly labelled an appendix/programme note.
- `G(x)` Green function conflicts with learning rule `G`.
- “ARIA-side direct” in the application table is undefined and too strong.
- `2I` and `\twoI` are mixed.
- Could not compile in the read-only workspace; static checks found no unresolved refs/cites.

**Top Three Fixes**

1. L420-431: remove the equivalence claim “Closing it in one frame would close it in all.” No local source proves this.
2. L411-415: either include a locally auditable source for `aria/vfd-b-anomaly` or mark the LHCb witness external and non-load-bearing.
3. L417-420: repair the response-vs-selection split. The paper’s selection hypotheses select `W`/critical points, not “one closure response.”

Verdict: not publication-ready. The main ACT body is mostly honest; the new ARIA-home section reintroduces programme-level overclaiming.

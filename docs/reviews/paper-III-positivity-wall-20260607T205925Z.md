Target reviewed: [paper-III-positivity-wall.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-III-positivity-wall.tex:1>).

**1. Claim Audit**
There are no formal theorem/proposition/corollary environments. The load-bearing claims are prose/table claims.

- L25-28, “No new result on RH is claimed… Every mathematical statement below is standard and credited.” The first sentence is mostly intended, but later text violates it. L64 asserts `Λ=0` as actual; L161 and L170-171 assert `H=H^*` and `W(f)\ge0` are “the same statement.” These are not established theorems.
- L39-41, Weil positivity criterion. Basically correct, but under-specified: the test-function class and exact Weil quadratic form matter. As written it is an acceptable survey shorthand, not a proof.
- L44-57, “The following are proven equivalent.” Overstated. Weil positivity, Li positivity, and `Λ≤0` are standard equivalent criteria. Jensen-polynomial hyperbolicity is equivalent only in the “all Jensen polynomials” formulation; GORZ proves asymptotic hyperbolicity, not RH. Hilbert-Pólya is a programme, not a proven non-tautological equivalence. The function-field Frobenius/intersection-form item is a theorem over finite fields, not an equivalent RH criterion over `\mathbb Z`.
- L61-64, “verifiably… GUE” and “sit at the critical edge `Λ=0`.” Full GUE statistics are not proved; Odlyzko is numerical and Montgomery is partial/conditional evidence. `Λ=0` is equivalent to RH after Rodgers-Tao, not known unconditionally.
- L65-67, “same explicit/trace-formula identity.” Too strong. The explicit formula is unconditional; GUE statistics are not merely the same identity.
- L70-72, function-field RH via Hodge index on `C\times C`. Acceptable for Weil’s curve case, but the Deligne citation covers a broader cohomological theorem. Say “for curves, Weil’s proof…”
- L76-78, “Connes-Consani, with `F_1` modelled by the sphere spectrum and the surface by `\mathbb Z\otimes_{\mathbb S}\mathbb Z`.” This conflates Connes-Consani’s arithmetic/scaling site with sphere-spectrum/brave-new `F_1` heuristics. The “trace formula but not positivity” part is fair; the model identification is not.
- L91-96, symbol table. `F_1` as “no agreed referent” is defensible only as “no single agreed referent with the required RH intersection theory.” `Spec Z ×_{F_1} Spec Z` as “notation only” is too absolute; in particular frameworks one can define analogues, just not the needed canonical surface with positivity.
- L101-105, reciprocal mirror “is the same statement as `\xi(s)=\xi(1-s)`.” Too hard. It is a schematic model of the involution after normalization, not literally the functional equation.
- L123-129, `F_1` ledger. One-point monoid “inert” is fair. Borger “open” is fair. Connes-Consani “open” is fair if phrased as “trace-formula/positivity open.” Deitmar/Toën-Vaquié “toric factors only” needs restriction; Deitmar integral finite-type schemes are toric-like, Toën-Vaquié is broader. Deninger “wish/circ.” is unfair: it is conjectural/hypothetical, not an `F_1` candidate and not simply circular.
- L134-139, “No candidate crosses… no one has invented one that is both.” Overclaim. The defensible statement is: “None of the listed candidates is known to supply the required positivity without extra hypotheses.”
- L153-156, joint-void “shared floor.” Trace formula, density, mirror can be listed with caveats. GUE local statistics cannot be marked “reach/reach” as a theorem.
- L158-159, “Frobenius/arithmetic surface: reach” and “self-adjoint `H`: reach.” Internally and mathematically too strong. Earlier the surface is unbuilt; Berry-Keating/Connes do not give the final Hilbert-Pólya operator.
- L161, `spec(H)=zeros ∧ H=H^* iff W(f)\ge0`. Not established. At most: each side would imply RH under its own strong hypotheses; Connes relates RH to trace-pairing positivity, not to a proved literal equivalence with self-adjointness.
- L166-173, “same object… by Connes’ analysis these are the same statement… unique shape.” This is the main defect. It hardens Hilbert-Pólya philosophy into theorem. Delete or downgrade to conjectural programme language.
- L179-183, closing. “Re-expression does not prove it” is good. “The single missing step” is acceptable only as a chosen geometric programme, not as a theorem about all possible RH approaches.

**2. Internal Consistency**
- The declared expository/no-RH scope at L19-28 and L31-36 is contradicted by theorem-toned assertions at L64, L161, and L170-173.
- The paper says the arithmetic surface is “unbuilt” at L73-78 and “notation only” at L95, but the joint table marks “Frobenius / arithmetic surface” as “reach” at L158. These cannot all stand.
- The paper calls `F_1` a placeholder with no agreed referent at L96, then classifies multiple “agreed” candidates at L112-127. Fix by distinguishing “many frameworks exist” from “no agreed framework supplies the required RH object.”
- No `\label`, `\ref`, or `\eqref` occur in the file. Citation keys appearing in `\cite{...}` all have local `\bibitem`s.
- I could not run a full LaTeX compile because the filesystem is read-only and `pdflatex` could not create its `.log`. Static TeX inspection found no obvious undefined macro.

**3. External Consistency**
- Repository-paper attributions are vague. L35-36 says “companion papers” but names no claim. Local Paper I and Paper II support only verified `L`-function correspondences and an `(O2)` negative; they explicitly make no RH, positivity, self-adjointness, or arithmetic-surface claim. The bridge note likewise says the cross-role bridge is open.
- The bundle `INDEX.md` repeats the dangerous artifact claim `W(f)\ge0 \iff H=H^*`; the artifact source `aria_void_joint.py` also states this as “Connes’ theorem.” That is not verification; it is the same overclaim copied into metadata.
- Current literature spot-check: Connes-Consani-Marcolli support “RH becomes equivalent to positivity of a relevant trace pairing,” not “self-adjointness equals Weil positivity” as a theorem. See arXiv `math/0703392`, abstract lines 38-39: https://arxiv.org/abs/math/0703392.
- Connes-Consani-Moscovici’s recent spectral-triples work remains a strategy: its abstract says a rigorous convergence proof would establish RH, i.e. the proof is still open. See arXiv `2511.22755`, lines 38-41: https://arxiv.org/abs/2511.22755.
- Borger’s `\Lambda`-rings support the “Frobenius lifts/descent data” reading, not a Weil-positivity result. See arXiv `0906.3146`, lines 37-39: https://arxiv.org/abs/0906.3146.
- Deitmar supports a toric characterization only in the qualified integral finite-type setting. See arXiv `math/0608179`, lines 41-42: https://arxiv.org/abs/math/0608179.
- Deninger’s work is explicitly conjectural cohomological formalism; it is not fairly summarized as circular. See Deninger PDF lines 3-14 and 50-54: https://www.uni-muenster.de/SFB878/publications/files/php7aMxKR3029.pdf.

**4. Tightness**
- L44: replace “The following are proven equivalent” with “The following include standard equivalent criteria and standard programme templates.”
- L49-50: replace with “RH is equivalent to hyperbolicity of all Jensen polynomials; GORZ proves the fixed-degree/asymptotic part.”
- L61-64: replace with “The zeros show strong numerical and partial-theorem evidence for GUE statistics; Rodgers-Tao gives `Λ\ge0`, so RH would force `Λ=0`.”
- L76-77: replace with “Connes’ trace-formula/noncommutative-geometric programme, and related `F_1`/absolute-geometry programmes…”
- L95-96: replace “notation only” / “symbol, no agreed referent” with “no agreed construction carrying the required intersection theory.”
- L128: replace `\textsc{wish/circ.}` with `\textsc{conjectural}`.
- L161 and L170-171: replace with “would be expected to express the same RH obstruction, but no theorem identifies the two constructions.”
- L172-173: delete. “Unique shape” and “only structural lever known” are rhetoric, not mathematics.

**5. Surface Issues**
- L110: “whether one can be named” should be “whether it can be named.”
- L124: `Cohn` is cited for pointed sets, but the table also leans on Kapranov-Smirnov without bibliography.
- L125: Deitmar and Toën-Vaquié are merged under one citation and one verdict; split them or qualify the verdict.
- L128: “wish/circ.” is not journal prose.
- L153-159: table status word “reach” is undefined and too binary for partial/conjectural material.
- L161: typeset `\operatorname{spec}(H)=\text{zeros}` inside math, not with “zeros” as bare text between math fragments.
- L76-77: `\mathbb{S}` is introduced without explanation.
- Bibliography entries are too incomplete for a submission: several lack journal/volume/page or precise subsequent-work references.

**6. Top Three Fixes**
1. Fix the joint-void overclaim at L161 and L166-173. This is the publication blocker: Hilbert-Pólya self-adjointness and Weil positivity are not proved to be literally the same statement.
2. Rewrite the equivalence/verified-structure claims at L44-57 and L61-66. In particular, GUE and `Λ=0` are not unconditional verified facts, and Hilbert-Pólya is not a proven equivalence.
3. Rebuild the `F_1` symbol table and ledger at L91-139. The defensible claim is “no listed framework is known to provide the required non-circular positivity,” not “the arithmetic surface is notation only” or “all non-crossing candidates are inert/open/circular” in the strong form stated.

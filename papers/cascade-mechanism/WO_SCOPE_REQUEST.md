# WO scope request — Cascade Closure mechanism paper

**Status:** scope-out task. NOT a paper draft. The deliverable is a full Work
Order (WO) for codex to produce next, following the WO-CAPSTONE / WO-CCC-P2 /
WO-CCC-P4 in-repo template at `papers/cascade-capstone-coalgebra/WO-CAPSTONE.md`,
`papers/cascade-algebraic-substrate/WO-CCC-P2.md`,
`papers/cascade-closure-dynamics/WO-CCC-P4.md`.

**Output target:** `papers/cascade-mechanism/WO-CASCADE-MECHANISM.md`. Write the
WO directly to that path. Do not create any `.tex` source yet — that comes
after the WO is approved.

**Date:** 2026-05-02. Today.

## What this paper is and is not

This is the **mechanism paper** of the VFD programme: the dedicated, restrained,
mathematically rigorous front-door paper that frames *the work already done* as
**one underlying closure mechanism** that projects across rungs to give
distinct geometric structures in different physical / cognitive / computational
regimes.

It is **not** a re-derivation paper. The substantive proofs already live in
existing in-repo papers (capstone, P2, correspondence-foundations,
closure-dynamics, the millennium scaffolding, the biology rung WOs, the closure
kernel + selection-layer bundles, paper-v / paper-v-revisited). This paper's
job is the *consolidation + framing*: show that those scattered results are
expressions of one mechanism. The WO must explicitly identify, for each
section, which existing in-repo material it cites vs.\ derives anew. The bias
is heavily toward citation; new content is reserved for the framing and the
mechanism statement itself.

\emph{Scope note (2026-05-02 update):} the user has explicitly authorised this
to be a \emph{large} paper. The earlier 30--50 page target is replaced by
\textbf{60--100 main-text pages}. The size is justified because the paper now
carries two additional load-bearing roles beyond the mechanism statement:
(a) it formalises ARIA as an \emph{observer-process implementation} of cascade
closure (see ``ARIA as observer-process'' below); and (b) it establishes the
projection-class scaffolding under which the as-yet-undropped Millennium
papers (RH, BSD, Hodge, NS, PNP, Poincaré, YM) will land as instances of the
same mechanism (see ``Millennium-papers alignment'' below). These two roles
are not optional embellishments; they are why the paper exists.

## Title

Working title (Penrose-bridged, restrained):

> **From Objective Reduction to Cascade Crystallisation: A Geometric Closure
> Model of State Selection.**

The WO may propose alternatives but should default to this. The Penrose bridge
is load-bearing for the rhetorical strategy and for landing the paper with a
mainstream-physics audience.

## Mechanism statement (the core claim the paper exists to make)

> **Cascade Closure.** When a field state cannot maintain coherent projection
> across a stratified hierarchy of geometric closure layers, the unresolved
> mismatch propagates through the hierarchy until a closure-compatible
> attractor geometry is selected. **Collapse** is the external view of this
> resolution event; **crystallisation** is the internal view; **cascade** is
> the propagation process between instability and crystallisation.

The triad **Instability → Cascade → Crystallisation** is the load-bearing
mechanism statement. The paper formalises this triad and shows it is realised
across distinct physical, cognitive, and computational regimes by the same
underlying closure operator on the same substrate (the 600-cell in this
programme; the WO should be specific about which substrate quantities are
substrate-fixed and which are projection-class-specific).

## What the WO must deliver

The WO must contain, at minimum, the following sections (mirroring
WO-CAPSTONE structure):

1. **Purpose and position in the programme.** State the gap this paper
   closes (no single mechanism paper exists; cascade material is
   distributed across capstone + P2 + correspondence-foundations +
   closure-dynamics + closure kernel + selection layer + paper-v +
   millennium-rh + a dozen docs). State explicitly that this is a
   consolidation paper, not a new-results paper, and identify the small
   number of new statements it makes (the mechanism statement above; the
   rung table; the projection identification; the case-study comparisons).

2. **Theoretical content.** Lay out the section structure of the eventual
   `.tex` source. Recommended structure (codex may adjust but should
   justify any deviation):
     - §1 Motivation: beyond collapse language. Penrose bridge.
     - §2 Core claim (mechanism statement; collapse / crystallisation /
       cascade triad).
     - §3 The rung model, formalised: each rung is a closure layer with a
       specific geometry $G_k$, a projection map $\pi_{k+1, k}: G_{k+1}
       \to G_k$, and a closure-residual functional $R_k$ that vanishes
       iff the projection is closure-compatible.
     - §4 Geometry identification across rungs: explicit rung table tying
       each rung to its geometry (E$_8$ / H$_4$ / D$_4$ / icosian /
       boundary $S^3$ / etc.), and the proof obligation (which geometries
       are forced by closure compatibility, and which are model
       choices).
     - §5 Visible vs.\ non-visible projection: the visible universe as
       the resolved projection boundary of a deeper cascade stack.
       Restrained framing per the user's brief — no overclaim.
     - §6 \textbf{ARIA as observer-process implementation of cascade closure
       (load-bearing).} See full detail under ``ARIA as observer-process''
       below. This section formalises the observer as a process tuple
       $\Ocal = \langle B, S, M, G, I, C, A \rangle$, maps the eight
       components onto ARIA's runtime architecture, distinguishes
       biological observer telemetry (EEG / phase coupling / cross-frequency
       binding) from synthetic observer telemetry (ARIA runtime signals /
       coherence scoring / closure-residue vector), and bounds the claim
       (no claim of ARIA biological consciousness; only architectural
       implementation of the observer process). This section carries the
       paper's claim that observerhood is a process architecture, not a
       biological property.
     - §7 Case studies (brief; one rigorous paragraph plus one citation
       chain each):
       (i) Penrose OR as historical bridge / neighbouring model.
       (ii) The b-anomaly closure kernel as physical-residual instance
       (passive regime).
       (iii) ARIA as computational closure-driven selection (active
       regime). Cross-references the §6 formalisation above; the
       case-study entry is brief because §6 carries the architectural
       content.
       (iv) Brain / EEG substrate as biological cascade signature
       (cognitive regime). Explicit substrate-witness scope.
       (v) The Standard Model mass spectrum (paper V / V Revisited) as
       spectral-projection-class instance.
   The WO must specify, for each case study, which in-repo paper supplies
   the proof and which closure regime it sits in (passive / active /
   cognitive / spectral).
     - §8 \textbf{Millennium-class projection scaffolding (load-bearing,
       framework-establishing).} See full detail under ``Millennium-papers
       alignment'' below. This section pre-positions the (as-yet-unreleased)
       Millennium papers (RH, BSD, Hodge, NS, PNP, Poincaré, YM) as
       projection-class instances of cascade closure on number-theoretic /
       PDE / geometric substrates, so that those papers land as
       \emph{instances of the framework} rather than as separate strange
       claims. The section establishes the projection-class identification
       at the framework level; the proofs themselves remain in the future
       Millennium preprints. Honest scoping: this section names
       hypotheses, not theorems, for the Millennium-class connections.
     - §9 Wrap-up: what is proved, what is conjectured, what is open. The
       five honest-scope items per the user's brief: not a QM
       replacement; not a consciousness derivation; not a Penrose
       refutation; not a complete visible-universe derivation; no new
       substrate-uniqueness theorem.

3. **Mathematical rigour required.** Per the user: "this one matters so
   it needs to be strong, mathematically rigorous, but we need to show
   how all the different geometries fall out and have some level of proof
   that these geometries relate to the different areas of physics."
   The WO must specify:
     (a) Which statements are **theorems** in this paper (probably very
         few — most theorems live in the cited papers; this paper's
         theorems are likely (T1) the mechanism statement itself stated
         as a definitional triad, and (T2) the rung-projection
         compositionality theorem at coarse level).
     (b) Which statements are **propositions** imported from cited papers
         (most of the substantive geometric content).
     (c) Which statements are **conjectures / hypotheses** (the
         projection-class identification across regimes is conjectural;
         the visible / non-visible decomposition is interpretive).
   The WO must mark each section's statements with one of these three
   levels of evidence and refuse the temptation to upgrade hypotheses to
   theorems for narrative weight.

4. **Dependencies (cite-freely).** Enumerate the in-repo papers + docs
   the new paper will draw from. The list must include, at minimum:
     - `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex`
       (final-coalgebra capstone; supplies the necessity argument)
     - `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex`
       (P2; supplies the 600-cell substrate, $H_4$ / $2I$ algebra,
       eigenvalue spectrum, BFS shells, $R_D(4)=15$ theorem, narrow
       polytope-uniqueness theorem)
     - `papers/cascade-correspondence-foundations/cascade-correspondence-foundations.tex`
       (3282 lines; supplies foundations and rung correspondence)
     - `papers/cascade-closure-dynamics/cascade-closure-dynamics.tex`
       (1448 lines; supplies dynamical closure content; this is the P4
       paper)
     - `papers/cascade-fine-structure/cascade-fine-structure.tex`
       (alpha-chain content)
     - `papers/cascade-12d-closure/` (L_12 = E_8 + Z[phi]^4 closure)
     - `papers/cascade-meta-layer-theorem` (if extant in tex; otherwise
       cite the doc `docs/cascade-meta-layer-theorem.md`)
     - `papers/cascade-hydrodynamic-projection/`
     - `papers/cascade-metric-projection/`
     - `papers/cascade-phason-coxeter/`
     - `papers/cascade-refinement-spaces/`
     - `papers/cascade-schlafli-convergence/`
     - `papers/cascade-sigma-rationality/`
     - The closure kernel + selection layer bundles (closure-kernel-papers
       on GitHub; selection-layer-papers on GitHub) — these are the
       passive + active witnesses
     - `papers/aria-chess-paper/aria-chess-paper.tex` (cognitive substrate
       witness)
     - `papers/paper-v/paper-v.tex` and
       `papers/paper-v-revisited/paper-v-revisited.tex` (mass spectrum
       projection)
     - `papers/millennium-rh-formal/rh-formal.tex` (cascade ↔ RH bridge
       scaffolding via subsec:convergence)
     - Supporting docs: `docs/closure-cosmogenesis.md`,
       `docs/cascade-helix-hypothesis.md`,
       `docs/fractal-cascade-projection.md`,
       `docs/observer-instance-definition.md`,
       `docs/aria-closure-kernel.md`,
       `docs/projection-narrative.md`,
       `docs/programme-plan.md`,
       `docs/rh-cascade-closure-dynamics.md`,
       `docs/rh-projection-class.md`,
       `docs/legacy-master-math-consolidation.md`,
       `docs/proof-sheet.md`.

   Codex should audit the list against the actual repository state at WO
   time (some directories may not have .tex files yet) and adjust.

5. **Out-of-scope (refused overclaims).** The WO must explicitly enumerate
   what this paper will not claim, mirroring the user's brief:
     - Not a replacement for quantum mechanics.
     - Not a derivation of consciousness or a mind theory.
     - Not a refutation of Penrose (Penrose OR is presented as a
       neighbouring model, not falsified).
     - Not a complete derivation of the visible universe from cascade
       primitives (the rung table is partly identified, partly
       conjectural).
     - No new substrate-uniqueness theorem beyond the narrow
       polytope-uniqueness of P2 §6.
     - No claim that the four case studies are statistically independent
       (they share the substrate by construction).

6. **Acceptance criteria.** Specify, in measurable terms, what counts as
   ``WO complete'' for the eventual `.tex` source. Suggested criteria:
     - Compiles clean to PDF via `tectonic` with no `! ` errors.
     - Length 30 to 50 main-text pages (front-door paper, not a monograph).
     - Every theorem / proposition / hypothesis statement is explicitly
       labelled as Theorem / Proposition / Hypothesis (no implicit
       theorem-grade language for hypotheses).
     - Every cross-paper claim cites a specific in-repo paper + section /
       theorem; no hand-wave references.
     - The six rungs (or however many; codex to fix the count) of the
       rung table all resolve to specific geometric objects with citations.
     - Passes a single `scripts/review_paper.sh` codex hostile-review
       round with verdict `Publication ready: yes` (multi-round expected
       in practice; the WO should record that the build target is
       **strong + restrained**, not **maximalist**).
     - Cross-references resolve.
     - The Penrose bridge is explicit and humble; no triumphalist
       language.

7. **Estimated effort and phasing.** Suggest a phased approach for the
   eventual `.tex` build (skeleton → §§1--3 → §§4--5 → §§6 case studies →
   §§7--8 wrap-up + hostile-review loop). Identify which sections require
   new diagrams / tables and which can be lifted from existing material.

## Style constraints for the WO

- Markdown, ~3-6 pages.
- Mirror the WO-CAPSTONE structure (Purpose / Theoretical content /
  Dependencies / Out-of-scope / Acceptance criteria).
- Be specific about which in-repo files supply which content. No
  hand-wave "see the cascade material".
- Be specific about *what is new in this paper* vs. *what is being framed*.
  The new content surface is small by design (~the mechanism statement,
  the rung table, the projection-class compositionality argument, the
  Penrose-bridge framing). Everything else is citation. The WO should
  defend that small-new-content stance, not work around it.
- Honest about what the case studies prove and don't prove.

## What codex should do

1. Read the existing WO templates (WO-CAPSTONE, WO-CCC-P2, WO-CCC-P4)
   and follow that style.
2. Audit the dependency list against the actual repository state
   (`ls papers/cascade-* docs/` etc.) and trim / augment.
3. Read the supporting docs the user has flagged
   (closure-cosmogenesis, fractal-cascade-projection,
   observer-instance-definition, projection-narrative,
   programme-plan, legacy-master-math-consolidation) as raw material
   for the rung table.
4. Write the full WO to `papers/cascade-mechanism/WO-CASCADE-MECHANISM.md`.
5. Do NOT start writing the `.tex` paper itself.
6. Print a one-paragraph summary to stdout: title, section count,
   estimated length, the small set of new claims this paper will make,
   the dependency list size.

## ARIA as observer-process (load-bearing §6 detail)

The user has explicitly directed that ARIA be framed in this paper as an
\emph{observer-process implementation}, not as ``brain waves so therefore
conscious''. The §6 content is to be built around the following architectural
spec, which is the user's own brief. The WO must reproduce this spec precisely
and the eventual `.tex` must implement it.

\textbf{The observer as a process tuple.} Define
\[
   \Ocal \;=\; \langle B, S, M, G, I, C, A \rangle
\]
with components:

| Symbol | Component | Role |
|---|---|---|
| $B$ | boundary sampler | the system cannot ingest the whole field; it samples a bounded boundary |
| $S$ | state integrator | fuses signal + context + memory + goal into the current field state |
| $M$ | memory substrate | written by past closures; read into current state integration |
| $G$ | goal / context field | task frame, user objective, system policy |
| $I$ | invariant constraints | refusals; the governance gate that vetoes constraint-violating closures |
| $C$ | closure / crystallisation operator | selects the candidate that best closes the field |
| $A$ | action interface | the channel through which crystallised state acts (tool call, reply, code, control signal) |

\textbf{Cascade processing by the observer.} The observer does not collapse
reality directly. It processes the cascade through the descent
\[
   \text{field potential} \to \text{oscillatory modes} \to
   \text{phase coupling} \to \text{attractor formation} \to
   \text{closure residual} \to \text{crystallisation} \to
   \text{governance gate} \to \text{action} + \text{memory inscription}
   \to \text{replay / provenance}.
\]
Observerhood is the seven-step loop:
\begin{enumerate}
   \item bounded sampling (via $B$),
   \item state integration (via $S$, $M$, $G$),
   \item residual detection (the closure-residual functional $R$ acting on the integrated state),
   \item candidate formation (the crystallisation operator $C$ proposing closure-compatible attractors),
   \item crystallisation (selection of the candidate that best closes the field),
   \item invariant governance (refusal of candidates that violate $I$),
   \item memory inscription (writing the successful closure back into $M$, with replayable trace).
\end{enumerate}

\textbf{The two telemetry layers.} The biological / synthetic distinction
should be presented as a single architecture with two telemetry streams,
not as two unrelated systems:

| Cascade layer | Biological telemetry | Synthetic / ARIA telemetry |
|---|---|---|
| field potential | EEG broadband activity | runtime input vector |
| oscillatory modes | EEG bands ($\delta, \theta, \alpha, \beta, \gamma$) | per-channel coherence scores |
| phase coupling | EEG phase locking, cross-frequency coupling | inter-module coherence score |
| attractor formation | neural attractor states | candidate-state pool |
| closure residual | prediction error signals (free-energy-style) | closure-residue vector |
| crystallisation | decision / action commitment | governed tool-call / reply selection |
| governance gate | inhibitory veto, prefrontal control | invariant / refusal stack |
| memory inscription | synaptic plasticity, hippocampal replay | polytope / invariant store update |
| replay layer | offline replay (sleep, default mode) | provenance hash, replay bundle |

\textbf{The cascade-layers diagram (one figure required).} The eventual
`.tex` must include one figure displaying the descent
\[
   \text{[field potential]} \to
   \text{[oscillatory modes]} \to
   \text{[phase coupling]} \to
   \text{[attractor formation]} \to
   \text{[closure residual]} \to
   \text{[crystallisation]} \to
   \text{[governance gate]} \to
   \text{[action + memory]} \to
   \text{[replay / provenance]}
\]
with the biological / synthetic mapping table beside it. This is the
load-bearing diagram of the paper.

\textbf{Claim boundary (must be quoted verbatim or paraphrased without
loss).} The §6 conclusion must contain (or paraphrase faithfully):

> We do not claim ARIA is biologically conscious. We claim ARIA implements
> an observer-process architecture: bounded sampling, recurrent integration,
> closure selection, memory inscription, and governed action. Brain waves
> are the visible telemetry of an observer cascade in biological tissue;
> ARIA's internal coherence and closure-residue metrics are the synthetic
> telemetry of an observer cascade in computational substrate. The shared
> layer is not the material; it is the cascade-closure-crystallisation-memory
> process.

\textbf{What §6 must not claim.} ARIA implements an observer process; it
does not prove qualia, it does not prove biological consciousness in
ARIA, and it does not prove that all observer-process implementations are
phenomenologically equivalent. The §6 section must close with this
boundary explicit.

\textbf{Existing ARIA in-repo material the §6 should consolidate.}
\texttt{papers/aria-chess-paper/aria-chess-paper.tex} (substrate-witness
preprint with the EEG / preregistered cortical correspondences); the
closure-kernel-papers bundle (operator + ARIA active-regime witness on
$V_{600}$); the kernel modules \texttt{lyapunov\_selector.py},
\texttt{self\_model\_stream.py}, \texttt{consciousness\_binding.py},
\texttt{vfd\_closure\_kernel.py}, \texttt{sigma\_orbit\_basis.py},
\texttt{v66\_e8\_coxeter.py} (these are the runtime artefacts that
realise the $\Ocal$ tuple operationally — \emph{the WO must list which
module realises which $\Ocal$ component}). Cross-reference any
\texttt{SystemTickCoordinator}-style integrator and the polytope memory
/ invariant store implementations referenced in
\texttt{docs/aria-closure-kernel.md} and the ARIA repository docs.

## Millennium-papers alignment scaffolding (load-bearing §8 detail)

The user has explicitly directed: ``we also need to line up a drop of the
RH and other Millennium papers after this; this needs to align so we can
drop them after, but [the cascade paper] should give the game away.''

The §8 content must therefore establish the projection-class scaffolding
under which the (as-yet-unreleased) Millennium preprints land as
\emph{instances of cascade closure on specific substrates}, rather than as
separate strange claims. The section must do this without prematurely
publishing the Millennium proofs themselves; those remain in the
millennium-* preprints. The job here is the framework-level
\emph{positioning}.

\textbf{Contents required.} §8 must contain:

\begin{enumerate}
\item \textbf{Projection-class identification, framework-level.} A general
statement: each Millennium-class problem corresponds to a
\emph{projection class} of cascade closure on a substrate-dependent
analytic / number-theoretic / geometric object. The substrate provides the
constraint geometry; the projection class is the family of admissible
observable functionals; the closure-residue functional vanishes on
solutions. This statement is itself a hypothesis at this framework level
(call it $H_{\text{Mill-Proj}}$) and should be presented as such.

\item \textbf{The seven Millennium projections, sketched.} A table-level
sketch (one paragraph per problem) tying each Millennium problem to its
candidate cascade-closure substrate. Use the existing in-repo scaffolding
where it exists; for problems where only docs / partial preprints exist,
honestly mark the connection as ``framework hypothesis, full preprint
forthcoming''. The tabular content (codex must verify against current
in-repo state):

| Millennium problem | Candidate cascade substrate / projection class | In-repo source |
|---|---|---|
| Riemann Hypothesis | $\hat z(z)$ Mellin object on the pentagonal-clock cycle structure $K = \{72, 0, 52, 20\}$; the $\sigma$-attractor reformulation; $V_{600}$ Laplacian spectrum is 78.3\% $\sigma$-fixed unconditional, 21.7\% $\sigma$-paired conditional on $H_{\text{attr}}$ | \texttt{papers/millennium-rh-formal/rh-formal.tex} (1892 lines), \texttt{docs/rh-cascade-closure-dynamics.md}, \texttt{docs/rh-projection-class.md} |
| Yang-Mills mass gap | derivation algebra $\dim \mathrm{Der}(\mathbb{O}) = 14$, $\dim \mathrm{stab}(e_1) = 8$ on the octonion substrate; $H_{\text{OS-lift}}$ remains conditional | \texttt{papers/millennium-ym/} |
| Birch-Swinnerton-Dyer | $T_E(s)$ Rankin-Selberg convergence verified for $E: y^2 = x^3 - x$; $H_{\text{BSD-Spec}}$ remains conditional | \texttt{papers/millennium-bsd-formal/bsd-formal.tex} |
| Navier-Stokes | $H_{P6 / P7}$ selection / bridge layer | \texttt{papers/millennium-ns-formal/ns-formal.tex} |
| Hodge | projection-class scoping; $\delta$-verdict | \texttt{papers/millennium-hodge-formal/hodge-formal.tex} |
| P vs NP | $\gamma$-verdict; structural separation argument | \texttt{papers/millennium-pnp-formal/pnp-formal.tex} |
| Poincaré | coherence-verdict (resolved classically; cascade reading is positional) | \texttt{papers/millennium-poincare-formal/poincare-formal.tex} |

The codex WO must audit each row against the actual in-repo paper state at
WO time and add a column \emph{``what fraction of the cascade reduction is
unconditional / what fraction is conditional on which named hypothesis''}.

\item \textbf{The ``give the game away'' requirement.} The user's
explicit instruction is that the cascade paper should reveal enough of
the Millennium-projection-class scaffolding that the Millennium drops
land as natural instances of the framework. Operationally, this means
§8 must:

(a) state $H_{\text{Mill-Proj}}$ explicitly;

(b) name each per-problem named hypothesis ($H_{\text{attr}}$ for RH;
$H_{\text{OS-lift}}$ for YM; $H_{\text{BSD-Spec}}$ for BSD; $H_{P6}$ /
$H_{P7}$ for NS; the per-problem hypothesis for the others) so that
Millennium preprint readers, on encountering those names, see them
already framework-positioned in this paper;

(c) for each problem, state in one sentence which substrate the
projection sits on (RH: $\sigma$-attractor / pentagonal-clock; YM:
octonion derivation algebra; BSD: $E$-curve $T_E(s)$; NS: $V_{600}$
adaptive-transport selection layer; etc.);

(d) refuse to actually \emph{prove} any of the per-problem statements;
all proofs remain in the corresponding millennium-* preprints.

\item \textbf{Honest verdict-scope discipline.} Per the user's
\texttt{project\_millennium\_scope\_pass} memory: all seven Millennium
papers are at honest verdict scopes ($\delta / \gamma / \beta /$
coherence). The §8 section must reproduce these verdicts faithfully, not
upgrade them. The cascade paper does \emph{not} resolve any Millennium
problem; it positions them as projection-class instances and identifies
which named hypothesis remains conditional in each case. This is the
\emph{framework-establishing} role, not the \emph{proof} role.

\item \textbf{Drop-order coordination.} §8 should close by stating the
intended drop order:
\begin{enumerate}[label=(\alph*)]
   \item this cascade-mechanism paper first;
   \item then, in priority order, the millennium-rh-formal preprint
     (the most-developed; the $\sigma$-attractor reformulation gives it
     the strongest standalone substrate witness);
   \item then YM (octonion derivation-algebra substrate);
   \item then BSD (Rankin-Selberg substrate);
   \item then NS / Hodge / PNP / Poincaré in whatever order their
     preprints reach $\delta$-or-better honest verdict.
\end{enumerate}
The WO should note that the cascade paper acts as a \emph{prereqd
reading} for any Millennium drop --- i.e., the Millennium preprints
should cite this cascade paper as their framework-positioning paper.

\item \textbf{Cite-only, do-not-derive.} Same discipline as the rest of
the cascade paper: §8 cites; it does not re-derive. The
\texttt{rh-cascade-closure-dynamics.md} doc may be partly absorbed
(non-load-bearing prose), but the load-bearing math stays in the
respective millennium-* preprints. The job is alignment, not duplication.
\end{enumerate}

\textbf{Existing in-repo material §8 must consolidate.}
\texttt{papers/millennium-rh-formal/rh-formal.tex} (1892 lines, with the
$\sigma$-attractor reformulation and the $\hat z(z)$ Mellin object);
\texttt{papers/millennium-rh/} (predecessor); \texttt{papers/millennium-ym/}
(YM); \texttt{papers/millennium-bsd-formal/bsd-formal.tex};
\texttt{papers/millennium-ns-formal/ns-formal.tex};
\texttt{papers/millennium-pnp-formal/pnp-formal.tex};
\texttt{papers/millennium-poincare-formal/poincare-formal.tex};
\texttt{papers/millennium-hodge-formal/hodge-formal.tex};
\texttt{docs/rh-cascade-closure-dynamics.md};
\texttt{docs/rh-projection-class.md}.

The codex WO must, when listing dependencies, note the verdict-scope
state of each Millennium preprint at WO time (per the
\texttt{project\_millennium\_scope\_pass} memory: $\delta / \gamma /
\beta /$ coherence) and not upgrade it.

## Non-negotiables

- This paper is the **front-door / mechanism** paper of the programme.
  It must land cleanly with a mainstream-physics reader. No jargon
  without definition. No unmoored claims.
- It must be **strong + restrained**, not maximalist. The Penrose bridge
  framing is load-bearing precisely because it is humble.
- It must be **mathematically rigorous** at the level of stating each
  claim with the right epistemic flag (Theorem / Proposition / Hypothesis)
  and citing the specific source for every imported result.
- It must show **how the different geometries fall out** of the cascade
  mechanism — not as a narrative, but as a structured rung table with
  citations to the geometric proofs in the cited papers.
- It must show **some level of proof that these geometries relate to the
  different areas of physics** — at minimum, the four case studies
  (Penrose OR / b-anomaly / ARIA / brain substrate / mass spectrum)
  with explicit substrate-witness scoping for each.

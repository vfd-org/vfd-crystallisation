OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dde56-55fe-77f3-b2ac-438dbf350f05
--------
user
You are reviewing a physics/mathematical preprint in LaTeX. Treat this like a careful
journal-referee pass, not a code review.

Paper path:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex

Section files (read all 10):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex

Bibliography:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/references.bib

Verification script and results (the paper lifts numbers from these):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json

Companion preprint to validate inherited claims against:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/sections/

Source documents the kernel paper draws from:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/aria-closure-kernel.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md

This paper is an OPERATOR WITNESS, not a derivation. Hard discipline:
- never claim φ⁻² is derived (it is a design-level shift)
- never claim 600-cell uniqueness
- never claim the operator IS the unique kernel on either empirical landing
- never claim a Lyapunov / 2I-equivariance / selection theorem is delivered
- never inherit b-anomaly claims beyond what b-anomaly itself claims (AIC tie + Mode-B drift caveats inherited verbatim)
- never inherit aria-chess claims beyond substrate-witness scope
- per-vertex correlation is 0.976 unweighted, 0.888 φ-geometric, 0.884 φ-arithmetic
- shell-mean correlation is 0.923 unweighted (the per-vertex test is the headline)
- operator-norm ‖C_φ⁻¹‖ = φ² ≈ 2.618 (computed) matches closed-form
- Laplacian spectrum: {0, 12-6φ, 12-4φ, 9, 12, 14, 4φ+8, 15, 6φ+6} with multiplicities {1, 4, 9, 16, 25, 36, 9, 16, 4}, sum 120

Read the file in full, then produce a structured review with the following
sections:

1. **Claim audit** For every non-trivial claim (theorem, proposition,
   numerical result, headline statement), say whether the stated argument
   actually establishes the stated claim. Flag over-claims, hidden assumptions,
   missing hypotheses, or cases where the prose needs softening. Quote the
   specific claim and cite the file:line.

2. **Internal consistency** Identify any place where definitions,
   assumptions, or notation conflict across sections. Check that the abstract
   matches the headline numbers; that the inherited b-anomaly numbers in §6
   match what b-anomaly's README states; that the inherited aria-chess numbers
   in §7 match the aria-chess paper.

3. **External consistency / numerics** For each headline numeric verify against
   `repro/results.json` by reading it locally:
   - 120 vertices, 720 edges, degree 12 uniform
   - shell sizes {1, 12, 20, 12, 30, 12, 20, 12, 1}
   - Laplacian spectrum (closed-form Z[φ] values matching numerics)
   - operator norm ‖C_φ⁻¹‖ = φ²
   - per-vertex correlation 0.976 (unweighted) vs 0.888 (φ-geom) vs 0.884 (φ-arith)
   If you find any disagreement, flag with file:line in both source and paper.

4. **Operator-witness scope discipline** Identify any sentence that strays into
   selection-theorem territory, derivation-of-φ⁻² territory, or kernel-uniqueness
   territory. The paper must stay strictly inside operator-witness scope.

5. **Tightness** Identify passages where the tone is stronger than the
   evidence supports, or weaker. Suggest one-line edits.

6. **Surface issues** Typos, undefined macros, broken LaTeX, inconsistent
   capitalisation. The paper defines \Ph, \Lop, \Cph, \Rsixhundred as macros
   in main.tex preamble; check usage is consistent.

7. **Top three fixes** Your ranked list of the most important issues to
   address before this paper is publication-ready. Be specific; cite file:line.

8. **Verdict** "Publication ready: yes" or "Publication ready: no — must-fix
   list above". Be direct. Over-claiming is worse than under-claiming.

warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll read the LaTeX, bibliography, scripts/results, companion preprint, and source docs first, then cross-check claims against the numbers and inherited scope. Since the workspace is read-only, I’ll produce the referee-style review without editing files.
exec
/bin/bash -lc "wc -l /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/sections/01_introduction.tex papers/aria-closure-kernel/paper/sections/02_definition.tex papers/aria-closure-kernel/paper/sections/03_substrate.tex papers/aria-closure-kernel/paper/sections/04_spectrum.tex papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/sections/06_passive_witness.tex papers/aria-closure-kernel/paper/sections/07_active_witness.tex papers/aria-closure-kernel/paper/sections/08_programme_home.tex papers/aria-closure-kernel/paper/sections/09_limitations.tex papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "find papers/aria-chess-paper/paper/sections -maxdepth 1 -type f -name '*.tex' -print" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/references.bib papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json docs/aria-closure-kernel.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 291ms:
184 papers/aria-closure-kernel/paper/main.tex

 succeeded in 319ms:
  188 papers/aria-closure-kernel/paper/sections/01_introduction.tex
  121 papers/aria-closure-kernel/paper/sections/02_definition.tex
  127 papers/aria-closure-kernel/paper/sections/03_substrate.tex
   95 papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  124 papers/aria-closure-kernel/paper/sections/05_agreement.tex
  655 total

 succeeded in 316ms:
  130 papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  163 papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  131 papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  173 papers/aria-closure-kernel/paper/sections/09_limitations.tex
   80 papers/aria-closure-kernel/paper/sections/10_conclusion.tex
  677 total

 succeeded in 328ms:
227 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md

 succeeded in 311ms:
papers/aria-chess-paper/paper/sections/01_introduction.tex
papers/aria-chess-paper/paper/sections/02_method.tex
papers/aria-chess-paper/paper/sections/03_substrate.tex
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex
papers/aria-chess-paper/paper/sections/05_results.tex
papers/aria-chess-paper/paper/sections/06_stress_tests.tex
papers/aria-chess-paper/paper/sections/07_cross_domain.tex
papers/aria-chess-paper/paper/sections/08_discussion.tex
papers/aria-chess-paper/paper/sections/09_limitations.tex
papers/aria-chess-paper/paper/sections/10_conclusion.tex

 succeeded in 336ms:
  103 papers/aria-closure-kernel/paper/references.bib
  413 papers/aria-closure-kernel/repro/verify_kernel.py
  143 papers/aria-closure-kernel/repro/results.json
  295 docs/aria-closure-kernel.md
  954 total

codex
I’ve confirmed the corpus sizes. Next I’m reading the kernel paper with line numbers so every issue can be pinned to a specific location.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/01_introduction.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/02_definition.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/04_spectrum.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 397ms:
     1	\documentclass[11pt]{article}
     2	
     3	\usepackage[a4paper, margin=2.5cm]{geometry}
     4	\usepackage{amsmath, amssymb, amsthm}
     5	\usepackage{booktabs}
     6	\usepackage{enumitem}
     7	\usepackage{graphicx}
     8	\usepackage{natbib}
     9	\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
    10	\usepackage{xcolor}
    11	
    12	\graphicspath{{figures/}}
    13	
    14	\newcommand{\Ph}{\varphi}
    15	\newcommand{\Lop}{L_{V_{600}}}
    16	\newcommand{\Cph}{C_{\Ph}}
    17	\newcommand{\Rsixhundred}{V_{600}}
    18	
    19	\title{The closure-response operator
    20	       $\Cph = L + \Ph^{-2} I$:\\
    21	       a geometry-fixed kernel on the 600-cell with two\\
    22	       independent empirical witnesses}
    23	
    24	\author{%
    25	  Lee Smart\\[2pt]
    26	  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
    27	  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
    28	  \texttt{@vfd\_org}%
    29	}
    30	
    31	\date{April 2026}
    32	
    33	\begin{document}
    34	
    35	\maketitle
    36	
    37	\noindent\textbf{Status:} Preprint, not peer-reviewed.
    38	
    39	\noindent\emph{Headline.}
    40	We define a programme-level closure-response primitive
    41	$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with graph
    42	Laplacian $L_M$ and golden ratio $\Ph = (1 + \sqrt 5)/2$. We give
    43	the 600-cell instance $\Rsixhundred$ as the canonical discrete
    44	substrate (numerically reproduced: $|V|=120$, $|E|=720$, uniform
    45	degree~$12$, $H_3$ shell decomposition
    46	$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
    47	matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
    48	operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
    49	eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
    50	agreement at per-vertex Pearson correlation $0.976$ between the
    51	discrete Green response and the continuum kernel
    52	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
    53	\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
    54	same fixed graph is then the load-bearing object in two
    55	\emph{independent} empirical works: a passive-regime structural
    56	fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
    57	public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
    58	active-regime substrate witness against eighteen preregistered
    59	neuroscience correspondences plus six drug/sleep EEG
    60	signatures~\citep{SmartAriaChess2026}.
    61	
    62	\noindent\emph{Scope.}
    63	This paper presents an empirical \emph{operator witness}: a
    64	geometry-fixed response operator that is simultaneously consistent
    65	with two independent empirical landings under no shape-parameter
    66	retuning between regimes. It is \emph{not} a derivation of the
    67	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    68	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    69	selection theorem on the companion adaptive-closure-transport
    70	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    71	a model-preference claim against alternative kernels on either
    72	empirical landing (the b-anomaly AIC comparison and the aria-chess
    73	substrate-witness scope are documented in their own preprints and
    74	inherited verbatim here).
    75	
    76	\begin{abstract}
    77	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    78	a closure substrate $M$ with graph Laplacian $L_M$ and
    79	$\Ph = (1+\sqrt 5)/2$, give its canonical instance on the 600-cell
    80	graph $\Rsixhundred$, and document its appearance as the same
    81	fixed operator (no shape retuning) in two independent empirical
    82	works: (i)~a five-dataset structural fit of the
    83	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    84	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    85	preregistered substrate witness against cortical signatures plus
    86	six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
    87	include the numerical reproduction script
    88	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
    89	from canonical generators, verifies the graph facts
    90	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
    91	Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
    92	$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
    93	agreement at per-vertex Pearson correlation $0.976$ for the
    94	unweighted variant, decisively above the $\Ph$-cocycle weighted
    95	variants ($0.888$ geometric, $0.884$ arithmetic). The unweighted
    96	choice winning on the geometry-only criterion reproduces the
    97	qualitative ranking established independently by b-anomaly's data
    98	$\chi^{2}$ comparison.
    99	
   100	\noindent\emph{(i) Operator definition and properties.}
   101	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   102	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   103	$\Ph^{-2} \approx 0.382$, operator norm
   104	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   105	in one coordinate $x$ is the closed-form Green's function
   106	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   107	
   108	\noindent\emph{(ii) The 600-cell instance.}
   109	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   110	generated by three orbits ($8$~axis, $16$~half-integer,
   111	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   112	on the short-edge graph; the Laplacian has nine eigenvalue classes
   113	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   114	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   115	
   116	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   117	Per-vertex Pearson correlation between the discrete response
   118	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   119	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each vertex's chord
   120	distance: $0.976$ (unweighted Laplacian), $0.888$
   121	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   122	Same source vertex, same fixed shift, no parameter fitting.
   123	
   124	\noindent\emph{(iv) Two independent empirical witnesses.}
   125	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   126	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   127	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   128	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   129	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   130	with one fitted dimensionless amplitude per dataset and the kernel
   131	shape held fixed. (b)~Active regime,
   132	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   133	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   134	condition-dependent self-injection coupling
   135	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   136	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   137	degree, passes eighteen preregistered correspondences (frozen
   138	2026-04-18) and six drug/sleep EEG signatures.
   139	
   140	\noindent\emph{What we do not claim.}
   141	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   142	stability clamp making $\Cph$ strictly positive definite. We do
   143	not claim $\Rsixhundred$ is the unique substrate consistent with
   144	either empirical landing. We do not claim the operator is the
   145	unique kernel shape consistent with the b-anomaly data
   146	(b-anomaly's Mode-B caveat is inherited verbatim) nor that the
   147	aria-chess substrate witness establishes a selection theorem on
   148	the adaptive-closure-transport 4-tuple. The structural scope of
   149	this paper is: \emph{one geometry-fixed operator on one fixed
   150	graph appears as the load-bearing object in two independent
   151	empirical works in two distinct regimes, with no shape retuning
   152	between them}.
   153	\end{abstract}
   154	
   155	% =====================================================================
   156	\input{sections/01_introduction.tex}
   157	\input{sections/02_definition.tex}
   158	\input{sections/03_substrate.tex}
   159	\input{sections/04_spectrum.tex}
   160	\input{sections/05_agreement.tex}
   161	\input{sections/06_passive_witness.tex}
   162	\input{sections/07_active_witness.tex}
   163	\input{sections/08_programme_home.tex}
   164	\input{sections/09_limitations.tex}
   165	\input{sections/10_conclusion.tex}
   166	% =====================================================================
   167	
   168	\section*{Reproducibility}
   169	The complete numerical verification (vertex construction,
   170	short-edge graph build, Laplacian spectrum, operator-norm bound,
   171	discrete-to-continuum correlation across three Laplacian variants)
   172	is reproducible from \texttt{repro/verify\_kernel.py} in this
   173	paper's bundle. No randomness, no fitted parameters: all numbers
   174	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   175	\S\ref{sec:agreement} are deterministic outputs of the script.
   176	The two empirical witness preprints
   177	(b-anomaly~\citep{SmartBAnomaly2026},
   178	aria-chess~\citep{SmartAriaChess2026}) carry their own
   179	reproducibility artifacts; this paper does not duplicate them.
   180	
   181	\bibliographystyle{plainnat}
   182	\bibliography{references}
   183	
   184	\end{document}

 succeeded in 362ms:
     1	% =====================================================================
     2	\section{The 600-cell substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section gives the canonical discrete instance: $M = \Rsixhundred$,
     6	the 600-cell regular 4-polytope under H$_4$ Coxeter symmetry, with
     7	the standard short-edge graph Laplacian. All facts in this section
     8	are reproduced numerically by \texttt{repro/verify\_kernel.py} from
     9	the canonical generators alone.
    10	
    11	\subsection{Vertex set}\label{ssec:vertices}
    12	
    13	$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
    14	$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
    15	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
    16	generating orbits are:
    17	\begin{itemize}\itemsep=2pt
    18	\item \textbf{Axis orbit} ($8$ vertices): all permutations of
    19	  $(\pm 1, 0, 0, 0)$;
    20	\item \textbf{Half-integer orbit} ($16$ vertices): all sign
    21	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    22	\item \textbf{$\Ph$-mixed orbit} ($96$ vertices): all even
    23	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
    24	  $\Ph^{2} = \Ph + 1$ identity, equivalently
    25	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
    26	\end{itemize}
    27	The total is $8 + 16 + 96 = 120$ unit vectors. Reproduced by
    28	\texttt{repro/verify\_kernel.py:build\_v600}; the numerical check
    29	$\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms all vertices on
    30	$S^{3}$.
    31	
    32	The H$_4$ Coxeter group (order $14400$) acts transitively on the
    33	$120$ vertices. Every vertex therefore has \emph{identical} local
    34	structure under $H_{4}$; in particular, every vertex has the same
    35	degree in the short-edge graph defined below.
    36	
    37	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
    38	
    39	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
    40	Euclidean chord distance is
    41	\[
    42	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
    43	\]
    44	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
    45	if their inner product equals the canonical short-edge value
    46	\begin{equation}\label{eq:short_edge}
    47	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
    48	\end{equation}
    49	equivalently chord distance
    50	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
    51	nearest-neighbour adjacency on the canonical 600-cell embedding
    52	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
    53	
    54	\paragraph{Graph facts (forced by the construction).}
    55	The graph $G_{V_{600}}$ has:
    56	\begin{itemize}\itemsep=2pt
    57	\item $|V|=120$ vertices,
    58	\item $|E|=720$ edges,
    59	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
    60	  the vertex set forces uniformity of the local structure; the
    61	  short-edge nearest-neighbour graph inherits this uniformity),
    62	\item the graph is connected (the H$_4$ transitivity action is
    63	  transitive on $V$ and the edge orbit is non-empty, so every pair
    64	  of vertices is connected by some sequence of short edges).
    65	\end{itemize}
    66	All four facts are reproduced numerically:
    67	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
    68	degree-min/max $=12/12$ (uniform).
    69	
    70	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
    71	
    72	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
    73	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
    74	of constant inner product with $v_{0}$. The nine canonical inner
    75	products are
    76	\begin{equation}\label{eq:shell_inner}
    77	\langle v, v_{0}\rangle
    78	\;\in\;
    79	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
    80	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
    81	\end{equation}
    82	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
    83	antipode. The shell-size sequence is
    84	\begin{equation}\label{eq:shell_sizes}
    85	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
    86	\;=\;
    87	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
    88	\end{equation}
    89	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
    90	icosidodecahedral ring. The total is
    91	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
    92	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
    93	
    94	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
    95	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
    96	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
    97	
    98	\subsection{Inner-product check}\label{ssec:inner_product_check}
    99	
   100	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   101	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   102	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   103	vertex in shell $s_{2}$ if and only if their pairwise inner product
   104	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   105	adjacency types to those compatible with the H$_3$ orbit structure.
   106	The numerically constructed graph respects this: every edge has
   107	inner product exactly $\Ph/2$ within machine precision (tolerance
   108	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   109	
   110	\subsection{What the substrate fixes, and what it does not}
   111	
   112	\begin{itemize}\itemsep=2pt
   113	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   114	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   115	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   116	  Laplacian spectrum (\S\ref{sec:spectrum}).
   117	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   118	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   119	  (\S\ref{ssec:opnorm}); the operator-norm bound
   120	  $\|\Cph^{-1}\| = \Ph^{2}$.
   121	\item \textbf{Not fixed by this paper}: the choice of
   122	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other H$_n$
   123	  Coxeter substrates. The 600-cell choice is post-hoc motivated by
   124	  the empirical landings (\S\ref{sec:passive_witness},
   125	  \S\ref{sec:active_witness}). A formal substrate ablation is an
   126	  open build (\S\ref{sec:limitations}).
   127	\end{itemize}

 succeeded in 345ms:
     1	% =====================================================================
     2	\section{Discrete-to-continuum agreement}\label{sec:agreement}
     3	% =====================================================================
     4	
     5	This is the load-bearing geometric fact of the paper: the discrete
     6	response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
     7	source agrees per-vertex with the continuum kernel
     8	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
     9	the source. We give the test, the numerical result, and the variant
    10	comparison that picks out the unweighted Laplacian.
    11	
    12	\subsection{The test}\label{ssec:test}
    13	
    14	Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
    15	vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
    16	other entries zero). Compute
    17	\[
    18	\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
    19	\]
    20	by direct linear solve (no eigenmode truncation). For each vertex
    21	$v \in V$, compute the Euclidean chord distance
    22	$x(v) = \|v - v_{0}\|$ and the continuum prediction
    23	\[
    24	G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
    25	\]
    26	The agreement criterion is the Pearson correlation between
    27	$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
    28	source itself is excluded, since the discrete response there is
    29	trivially the diagonal of $\Cph^{-1}$ and the chord distance is
    30	zero, both degenerate for the comparison).
    31	
    32	\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
    33	
    34	\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
    35	\begin{itemize}\itemsep=2pt
    36	\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
    37	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
    38	  (averaging $\psi(v)$ over each H$_3$ shell first, then
    39	  correlating the $9$-point shell-mean trajectory with the
    40	  continuum prediction at the shell mean radius).
    41	\end{itemize}
    42	The two correlations measure the same fact at different
    43	resolutions: per-vertex tests at $|V|-1 = 119$ data points
    44	(every non-source vertex), while shell-mean tests at $9$ data
    45	points (one per shell). The per-vertex test is the more sensitive
    46	agreement criterion; the shell-mean test reduces noise from
    47	within-shell variation that arises because $\Cph^{-1}$ is not
    48	exactly H$_3$-invariant from a single-vertex source (the
    49	H$_3$ subgroup fixes only the pole, not the full vertex set).
    50	
    51	\subsection{Variant comparison}\label{ssec:variant_comparison}
    52	
    53	Two $\Ph$-cocycle weighted Laplacian variants are tested as
    54	controls:
    55	
    56	\begin{itemize}\itemsep=2pt
    57	\item \textbf{$\Ph$-geometric weights}: edge weight
    58	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
    59	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
    60	  is the shell index of $v$.
    61	\item \textbf{$\Ph$-arithmetic weights}: edge weight
    62	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
    63	  $\omega_{+}$.
    64	\end{itemize}
    65	The weighted Laplacian is then
    66	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
    67	We re-run the discrete-to-continuum test on each variant.
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-vertex and shell-mean Pearson correlations between the
    73	discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
    74	prediction $G(\|v - v_{0}\|)$ for three Laplacian variants.
    75	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
    76	\label{tab:variant_correlation}
    77	\begin{tabular}{l c c}
    78	\toprule
    79	Variant            & Per-vertex correlation & Shell-mean correlation \\
    80	\midrule
    81	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
    82	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
    83	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
    84	\bottomrule
    85	\end{tabular}
    86	\end{table}
    87	
    88	\textbf{Reading.} The unweighted Laplacian wins on both criteria
    89	by a clear margin ($+0.088$ per-vertex over the next variant,
    90	$+0.043$ shell-mean). This reproduces, on a different test, the
    91	qualitative ranking the b-anomaly paper~\citep{SmartBAnomaly2026}
    92	established independently against its data-$\chi^{2}$ criterion
    93	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
    94	b-anomaly numbers). Two independent criteria — geometry-only
    95	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
    96	agree on which Laplacian variant is preferred. We do not claim
    97	this is a uniqueness result; we report it as a two-criterion
    98	convergence (the b-anomaly paper's own caveat that the data was
    99	looked at first and the geometry criterion verified afterward is
   100	inherited verbatim).
   101	
   102	\subsection{What the agreement does and does not establish}
   103	
   104	\paragraph{Does establish.} A geometric agreement: the discrete
   105	response of a fixed-shift Green operator on a fixed graph behaves,
   106	to within the per-vertex Pearson correlation $0.976$, like the
   107	closed-form continuum exponential at the same length scale $\Ph$.
   108	This is a non-trivial agreement between two independently-defined
   109	objects: (i) the discrete inverse of a $120\times 120$
   110	Laplacian-plus-shift matrix; and (ii) a one-dimensional continuum
   111	exponential. The $\Ph$-mediated agreement is an empirical fact
   112	about the chosen substrate and shift, computed (not fitted) by
   113	the verification script.
   114	
   115	\paragraph{Does not establish.} Operator uniqueness on either
   116	empirical landing — the b-anomaly paper documents Mode-B
   117	free-width Gaussian alternatives that fit comparably in $\chi^{2}$
   118	at the cost of one extra shape parameter, and the aria-chess
   119	preprint does not run a substrate ablation; both caveats are
   120	inherited verbatim. The agreement also does not establish that
   121	$\Rsixhundred$ is the unique discrete substrate with this
   122	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   123	graphs would give different correlations on the same test, and a
   124	formal substrate ablation is an open build (\S\ref{sec:limitations}).

 succeeded in 348ms:
     1	% =====================================================================
     2	\section{The Laplacian spectrum}\label{sec:spectrum}
     3	% =====================================================================
     4	
     5	The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$ has
     6	nine distinct eigenvalue classes with closed-form values in
     7	$\mathbb{Z}[\Ph]$ and multiplicities summing to $|V| = 120$. The
     8	spectrum is computed numerically by
     9	\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
    10	$120\times 120$ symmetric eigendecomposition, deterministic at
    11	machine precision); we report the result in
    12	Table~\ref{tab:spectrum}.
    13	
    14	\begin{table}[ht]
    15	\centering
    16	\small
    17	\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
    18	Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
    19	values returned by \texttt{repro/verify\_kernel.py}; multiplicities
    20	sum to $120$.}
    21	\label{tab:spectrum}
    22	\begin{tabular}{c c c}
    23	\toprule
    24	Closed-form eigenvalue & Numerical value & Multiplicity \\
    25	\midrule
    26	$0$            & $-3\!\times\!10^{-15}$ (machine zero) & $1$ \\
    27	$12 - 6\Ph$    & $2.2918$  & $4$ \\
    28	$12 - 4\Ph$    & $5.5279$  & $9$ \\
    29	$9$            & $9.0000$  & $16$ \\
    30	$12$           & $12.0000$ & $25$ \\
    31	$14$           & $14.0000$ & $36$ \\
    32	$4\Ph + 8$     & $14.4721$ & $9$ \\
    33	$15$           & $15.0000$ & $16$ \\
    34	$6\Ph + 6$     & $15.7082$ & $4$ \\
    35	\midrule
    36	\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
    37	\bottomrule
    38	\end{tabular}
    39	\end{table}
    40	
    41	\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
    42	\begin{align*}
    43	12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
    44	12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
    45	4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
    46	6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
    47	\end{align*}
    48	The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
    49	$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
    50	are conjugate under the Galois automorphism
    51	$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
    52	fixed-point eigenvalues $\{0, 9, 12, 14, 15\}$ are rational and
    53	have multiplicities $\{1, 16, 25, 36, 16\}$ (sum $94$); the
    54	$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.
    55	
    56	\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
    57	$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
    58	remaining $26/120 = 21.7\%$ is $\sigma$-paired. The pairing is the
    59	shape used by the σ-attractor reformulation in the RH preprint
    60	~\citep{SmartRHFormal2026}: the $\sigma$-fix subspace is
    61	unconditional under the $\sigma$-projector, while the
    62	$\sigma$-paired subspace requires the closure-flow suppression
    63	hypothesis. We do not import that reading here; we report only that
    64	the spectrum has this structure.
    65	
    66	\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
    67	
    68	The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
    69	\[
    70	\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
    71	\;\approx\; 0.381966,
    72	\]
    73	and the operator-norm bound is
    74	\[
    75	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
    76	\]
    77	\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
    78	$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
    79	(predicted) — match to six decimal places. The largest eigenvalue
    80	of $\Cph$ is
    81	$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
    82	= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
    83	
    84	\subsection{H$_4$ irrep block decomposition}\label{ssec:irrep}
    85	
    86	The eigenspaces of $\Lop$ partition into H$_4$-proper and
    87	$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
    88	exponents are $\{1, 11, 19, 29\}$; under the
    89	$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
    90	$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis (used in the
    91	aria-chess companion's recurrent
    92	layer~\citep{SmartAriaChess2026}) realises this block decomposition
    93	at machine precision, providing a spectrally clean H$_4$-equivariant
    94	basis. We use this fact to label the spectrum but do not depend on
    95	it for the operator-witness claims of this paper.

 succeeded in 385ms:
     1	% =====================================================================
     2	\section{The closure-response operator}\label{sec:definition}
     3	% =====================================================================
     4	
     5	\subsection{Definition}
     6	
     7	Let $M$ be a closure substrate: a connected finite undirected graph
     8	$M=(V,E)$, a finite simplicial complex with chosen Laplacian, or a
     9	projected continuum coordinate. Let $L_M$ be the corresponding
    10	Laplacian (graph Laplacian $L = D - A$, simplicial Laplacian, or
    11	continuum operator $-\Delta$ with chosen boundary conditions).
    12	Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
    13	and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
    14	
    15	The \emph{closure-response operator} is
    16	\begin{equation}\label{eq:cphi}
    17	\Cph \;=\; L_M + \Ph^{-2} I.
    18	\end{equation}
    19	For a non-negative localised source $f$ on $M$, the
    20	\emph{closure response field} is
    21	\begin{equation}\label{eq:psi}
    22	\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
    23	\end{equation}
    24	
    25	\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
    26	
    27	The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
    28	require:
    29	
    30	\begin{itemize}\itemsep=2pt
    31	\item \textbf{(H1) Self-adjointness.} $L_M$ is self-adjoint on the
    32	  $L^{2}$ inner product on $M$ (with counting measure on a finite
    33	  graph, with Lebesgue measure with appropriate boundary conditions
    34	  in the continuum case).
    35	\item \textbf{(H2) Non-negativity.} $L_M \geq 0$ as a
    36	  quadratic form: $\langle f, L_M f\rangle \geq 0$ for all $f$.
    37	\item \textbf{(H3) Connectedness.} On a finite graph, $M$ is
    38	  connected (so the kernel of $L_M$ is exactly the constant
    39	  vector). In the continuum case, the $L_M$-zero subspace is
    40	  finite-dimensional and known.
    41	\end{itemize}
    42	
    43	The standard graph Laplacian on a connected finite undirected
    44	graph satisfies (H1)--(H3); so does the continuum
    45	$L = -d^{2}/dx^{2}$ on a bounded interval with Dirichlet boundary
    46	conditions, or on the full line with decay-at-infinity. Substrates
    47	outside this class — projected coordinates with non-standard
    48	boundaries, weighted Laplacians whose weight function is unbounded,
    49	or operators with negative spectrum — require their own analysis,
    50	which we do not give here.
    51	
    52	\subsection{Positive definiteness}\label{ssec:positivity}
    53	
    54	Under (H1)--(H3) on a finite connected graph, $L_M$ has a smallest
    55	eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
    56	eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
    57	\[
    58	\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
    59	                    \;=\; \Ph^{-2} \;>\; 0,
    60	\]
    61	so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
    62	well-defined and bounded.
    63	
    64	\subsection{Operator-norm bound}\label{ssec:opnorm}
    65	
    66	The operator norm of $\Cph^{-1}$ is the reciprocal of its smallest
    67	eigenvalue:
    68	\begin{equation}\label{eq:opnorm}
    69	\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
    70	              \;=\; 1/\Ph^{-2} \;=\; \Ph^{2}
    71	              \;\approx\; 2.618034.
    72	\end{equation}
    73	This is the response-amplification ceiling: for any source $f$,
    74	\[
    75	\|\psi\|_{2} \;\leq\; \Ph^{2}\, \|f\|_{2}.
    76	\]
    77	Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
    78	graph $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
    79	\S\ref{sec:agreement}); this matches the closed-form $\Ph^{2}$ to
    80	machine precision.
    81	
    82	\subsection{Continuum projection}\label{ssec:continuum}
    83	
    84	In one projected coordinate $x \in \mathbb{R}$ with
    85	$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
    86	$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
    87	exponential
    88	\begin{equation}\label{eq:green_continuum}
    89	G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
    90	\end{equation}
    91	The decay scale is $\Ph$ — the same constant that appears in the
    92	shift, by construction. Normalised, the kernel is
    93	$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
    94	
    95	This continuum Green's function is the comparison object for the
    96	discrete-to-continuum agreement test (\S\ref{sec:agreement}):
    97	the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
    98	chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
    99	is compared to $G(\|v - v_{\mathrm{src}}\|)$.
   100	
   101	\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
   102	
   103	The shift $\Ph^{-2}$ is chosen so that:
   104	\begin{enumerate}\itemsep=2pt
   105	\item $\Cph$ is strictly positive definite (the smallest eigenvalue
   106	  is exactly $\Ph^{-2}$);
   107	\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
   108	  same constant as the continuum decay scale (Eq.~\eqref{eq:green_continuum}),
   109	  giving a single dimensional parameter throughout the operator;
   110	\item the continuum projection (Eq.~\eqref{eq:green_continuum})
   111	  has decay scale $\Ph$, not a free length parameter.
   112	\end{enumerate}
   113	We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
   114	symmetry argument. It is a design-level choice motivated by
   115	(1)--(3); we report this explicitly and treat formal derivation as
   116	an open build (\S\ref{sec:limitations}). The companion
   117	adaptive-closure-transport
   118	preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
   119	selection-layer dynamics over $W$-space that would, if delivered,
   120	constrain the shift further; that derivation is not delivered
   121	there or here.

 succeeded in 401ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	A response operator on a fixed graph, with no shape parameters tuned
     6	to any dataset, that simultaneously describes (i) the $q^{2}$ shape
     7	of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
     8	flavour-physics datasets in their passive linear-response regime,
     9	and (ii) eighteen preregistered cortical correspondences plus six
    10	drug/sleep EEG signatures in the active dynamical regime of a
    11	recurrent self-model layer above the same graph, deserves a separate
    12	preprint that names the operator, gives its construction in full,
    13	and threads the relationship between the two empirical landings
    14	without inheriting either's load-bearing claims. That is what this
    15	paper does.
    16	
    17	The operator is
    18	\begin{equation}\label{eq:cphi_intro}
    19	\Cph \;=\; L_M + \Ph^{-2} I,
    20	\qquad \Ph \;=\; (1+\sqrt 5)/2,
    21	\end{equation}
    22	where $M$ is a closure substrate (graph, simplicial complex, or
    23	projected coordinate) and $L_M$ is its Laplacian. The shift
    24	$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
    25	non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
    26	positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
    27	operator-norm bound is
    28	\begin{equation}\label{eq:opnorm_intro}
    29	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
    30	\end{equation}
    31	The continuum projection in one coordinate $x$ has a closed-form
    32	Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
    33	$\Ph$ (\S\ref{sec:definition}).
    34	
    35	The canonical discrete substrate is the 600-cell graph
    36	$\Rsixhundred$: $120$ unit vectors on $S^{3}$, generated by three
    37	$H_{4}$ Coxeter orbits ($8$ axis vertices, $16$ half-integer
    38	vertices, $96$ $\Ph$-mixed vertices), connected by short edges
    39	$\langle v, w\rangle = \Ph/2$. The graph has $|E|=720$ edges,
    40	uniform degree~$12$ by H$_4$ transitivity, a $9$-shell $H_{3}$
    41	partition $\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
    42	$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
    43	classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
    44	All of these facts are reproduced numerically by
    45	\texttt{repro/verify\_kernel.py} from the canonical generators
    46	alone — no external data input.
    47	
    48	\subsection*{What this paper claims}
    49	
    50	We claim a single \emph{operator witness}: that one geometry-fixed
    51	operator, on one fixed graph, with no shape-parameter retuning
    52	between regimes, appears as the load-bearing object in two
    53	empirical works covering qualitatively distinct physical settings.
    54	
    55	\begin{enumerate}\itemsep=2pt
    56	\item \textbf{Operator definition is fixed by the construction.}
    57	  Once $\Rsixhundred$ is selected and the stability shift
    58	  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
    59	  parameter, no fitted threshold, no learned weight enters the
    60	  operator. The Laplacian spectrum, the operator-norm bound, and
    61	  the discrete-to-continuum agreement are computed (not fitted)
    62	  from the construction and reproduced in
    63	  \texttt{repro/verify\_kernel.py}.
    64	\item \textbf{Discrete-to-continuum agreement is empirical, not
    65	  postulated.} For a localised source at any vertex, the discrete
    66	  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
    67	  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
    68	  $\rho = 0.976$ on the unweighted graph Laplacian. This is
    69	  numerical agreement between two independently-defined objects (a
    70	  120-dimensional discrete inverse and a continuum exponential
    71	  kernel), not a definitional identity.
    72	\item \textbf{Variant comparison is decisive at the geometry-only
    73	  criterion.} Two $\Ph$-cocycle weighted Laplacian variants
    74	  ($\Ph$-geometric, $\Ph$-arithmetic edge weights via shell-grade
    75	  exponents $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    76	  correlation: $0.888$ and $0.884$ respectively. The unweighted
    77	  Laplacian wins on the geometry-only criterion. This reproduces,
    78	  on a different test, the qualitative ranking established
    79	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    80	  (\S\ref{sec:passive_witness}).
    81	\item \textbf{Two independent empirical landings, same operator.}
    82	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    83	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    84	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    85	  public datasets, with one fitted dimensionless amplitude per
    86	  dataset and the kernel held fixed; sign uniformity holds in
    87	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
    88	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
    89	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
    90	  recurrent self-model layer above the substrate, to pass eighteen
    91	  preregistered cortical correspondences (frozen 2026-04-18) plus
    92	  six drug/sleep EEG signatures.
    93	\end{enumerate}
    94	
    95	\subsection*{What this paper does \emph{not} claim}
    96	
    97	\begin{itemize}\itemsep=2pt
    98	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
    99	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   100	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   101	  functional or a symmetry argument; we report its role as a
   102	  regularisation-of-mass scale.
   103	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   104	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   105	  highly symmetric graphs, and continuum substrates are all
   106	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   107	  is post-hoc motivated by the empirical landings; a formal
   108	  ablation against alternative substrates is an open build.
   109	\item \emph{Not a kernel-uniqueness claim on either empirical
   110	  landing.} The b-anomaly's Mode-B analysis shows that a
   111	  free-width Gaussian charm-loop proxy fits the same five datasets
   112	  comparably in $\chi^{2}$ at the cost of one extra shape
   113	  parameter; the b-anomaly AIC comparison against
   114	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   115	  statistical tie on current data
   116	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   117	  Both caveats are inherited verbatim from the b-anomaly preprint.
   118	\item \emph{Not a selection theorem on the
   119	  ACT 4-tuple.} The companion adaptive-closure-transport
   120	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   121	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   122	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   123	  reduced flow, edge-space decomposition under $2I$-equivariance,
   124	  full reduced-flow convergence — is left open in that paper and
   125	  is not delivered here.
   126	\item \emph{Not a circuit-level model on the active-regime side.}
   127	  The aria-chess preprint operates at the architectural-algorithmic
   128	  level above $\Cph$. We import its empirical results verbatim and
   129	  do not relitigate them here; their substrate-witness scope
   130	  applies.
   131	\end{itemize}
   132	
   133	\subsection*{Mapping from numerics to admissible claims}
   134	
   135	To keep this paper inside the operator-witness scope, we use the
   136	same claim-boundary discipline as the aria-chess
   137	preprint~\citep{SmartAriaChess2026}: numerical results
   138	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   139	$\mathcal C_{\mathrm{admissible}}$ by the rule
   140	\[
   141	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   142	        \mathcal C_{\mathrm{admissible}},
   143	\qquad
   144	\mathcal C_{\mathrm{admissible}}
   145	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   146	\]
   147	A numerically computed quantity (the Laplacian spectrum, the
   148	operator-norm bound, the per-vertex correlation $0.976$) licenses
   149	a `computed'-type claim. A statistical agreement at the operator
   150	level (sign uniformity in $5/5$ datasets, an $18/18$ preregistered
   151	tally) licenses a `consistent with'-type claim. We never write
   152	`derives the kernel', `proves uniqueness', or `establishes
   153	selection'.
   154	
   155	\medskip
   156	\begin{center}
   157	\fbox{\parbox{0.92\linewidth}{\small
   158	\textbf{What is claimed / what is not.}\par
   159	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   160	600-cell graph, with computed spectrum, operator-norm bound, and
   161	discrete-to-continuum correlation; the same fixed operator appearing
   162	in two independent empirical works (b-anomaly five-dataset
   163	structural fit; aria-chess $18/18$ + $6/6$ preregistered substrate
   164	witness) without shape-parameter retuning between regimes.\par
   165	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   166	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   167	landing; a selection theorem on the ACT 4-tuple; that either
   168	empirical landing settles the underlying physics (flavour anomaly
   169	or consciousness) by the operator alone.
   170	}}
   171	\end{center}
   172	
   173	\subsection*{Layout}
   174	
   175	\S\ref{sec:definition} gives the operator definition, the positivity
   176	properties of $\Cph$, the operator-norm bound, and the continuum
   177	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   178	canonical generators, gives the graph facts, and the $9$-shell
   179	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   180	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   181	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   182	across three Laplacian variants. \S\ref{sec:passive_witness} and
   183	\S\ref{sec:active_witness} thread the two independent empirical
   184	witnesses (b-anomaly and aria-chess) at the operator level.
   185	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   186	for the polynomial-in-$L$ Lyapunov family that recurs across the
   187	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   188	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/06_passive_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/07_active_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/08_programme_home.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 224ms:
     1	@book{CoxeterRegularPolytopes,
     2	  author    = {Coxeter, H. S. M.},
     3	  title     = {Regular Polytopes},
     4	  publisher = {Dover},
     5	  edition   = {3rd},
     6	  year      = {1973},
     7	  address   = {New York}
     8	}
     9	
    10	@misc{Weisstein600Cell,
    11	  author       = {Weisstein, Eric W.},
    12	  title        = {{600-Cell}},
    13	  howpublished = {From MathWorld --- A Wolfram Web Resource},
    14	  url          = {https://mathworld.wolfram.com/600-Cell.html},
    15	  note         = {Accessed 2026-04-30}
    16	}
    17	
    18	@article{ChungSpectralGraph,
    19	  author    = {Chung, Fan R. K.},
    20	  title     = {Spectral Graph Theory},
    21	  journal   = {CBMS Regional Conference Series in Mathematics},
    22	  volume    = {92},
    23	  publisher = {American Mathematical Society},
    24	  year      = {1997}
    25	}
    26	
    27	@book{HumphreysReflectionGroups,
    28	  author    = {Humphreys, James E.},
    29	  title     = {Reflection Groups and Coxeter Groups},
    30	  publisher = {Cambridge University Press},
    31	  year      = {1990},
    32	  series    = {Cambridge Studies in Advanced Mathematics},
    33	  volume    = {29}
    34	}
    35	
    36	% Companion VFD preprints (the two empirical witnesses + selection-layer paper).
    37	
    38	@unpublished{SmartBAnomaly2026,
    39	  author = {Smart, Lee},
    40	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
    41	            angular anomaly: sign-uniform cross-dataset and cross-channel fit},
    42	  year   = {2026},
    43	  note   = {VFD preprint}
    44	}
    45	
    46	@unpublished{SmartAriaChess2026,
    47	  author = {Smart, Lee},
    48	  title  = {A geometry-fixed substrate witness for cortical signatures:
    49	            eighteen preregistered correspondences and six drug/sleep EEG
    50	            signatures from the 600-cell under H$_4$ Coxeter symmetry},
    51	  year   = {2026},
    52	  note   = {VFD preprint, papers/aria-chess-paper/}
    53	}
    54	
    55	@unpublished{SmartAdaptiveClosureTransport2026,
    56	  author = {Smart, Lee},
    57	  title  = {Adaptive Closure Transport: a 4-tuple bridge
    58	            $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to
    59	            selection},
    60	  year   = {2026},
    61	  note   = {VFD preprint, papers/adaptive-closure-transport/}
    62	}
    63	
    64	% Cited from the programme-home section.
    65	
    66	@unpublished{SmartRHFormal2026,
    67	  author = {Smart, Lee},
    68	  title  = {RH-formal: a $\sigma$-attractor reformulation of the Riemann
    69	            Hypothesis on the cascade closure substrate},
    70	  year   = {2026},
    71	  note   = {VFD preprint, papers/millennium-rh-formal/}
    72	}
    73	
    74	@unpublished{SmartYMMassGap2026,
    75	  author = {Smart, Lee},
    76	  title  = {The cascade gap operator on the 600-cell substrate},
    77	  year   = {2026},
    78	  note   = {VFD preprint, papers/millennium-ym/}
    79	}
    80	
    81	% External flavour-physics literature (b-anomaly context, cited in §6).
    82	
    83	@article{KrugerMatias2005,
    84	  author  = {Kr\"uger, Frank and Matias, Joaquim},
    85	  title   = {Probing new physics via the transverse amplitudes of
    86	             $B^0 \to K^{*0} (\to K^- \pi^+) l^+ l^-$ at low recoil},
    87	  journal = {Phys. Rev. D},
    88	  volume  = {71},
    89	  pages   = {094009},
    90	  year    = {2005},
    91	  doi     = {10.1103/PhysRevD.71.094009}
    92	}
    93	
    94	@article{LHCbAngular2020,
    95	  author  = {{LHCb Collaboration}},
    96	  title   = {Measurement of $\mathit{CP}$-averaged observables in the
    97	             $B^0 \to K^{*0} \mu^+ \mu^-$ decay},
    98	  journal = {Phys. Rev. Lett.},
    99	  volume  = {125},
   100	  pages   = {011802},
   101	  year    = {2020},
   102	  doi     = {10.1103/PhysRevLett.125.011802}
   103	}

 succeeded in 274ms:
     1	% =====================================================================
     2	\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
     3	% =====================================================================
     4	
     5	This section threads the first independent empirical landing of
     6	$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
     7	summarise here only what the operator-witness narrative requires
     8	and inherit the preprint's caveats verbatim.
     9	
    10	\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
    11	
    12	The Wilson-coefficient Hamiltonian for $b\to s\mu^{+}\mu^{-}$
    13	contains a $C_{9}^{(\prime)}$ contribution that, in the Standard
    14	Model, is approximately $q^{2}$-independent in the relevant
    15	kinematic range. The b-anomaly preprint replaces the constant SM
    16	shape with a fixed kernel
    17	\begin{equation}\label{eq:banomaly_kernel}
    18	\Delta C_{9}^{\mathrm{eff}}(q^{2})
    19	\;=\;
    20	A \cdot \kappa_{V_{600}}(q^{2}),
    21	\end{equation}
    22	where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
    23	$\Rsixhundred$ via a discrete-to-momentum projection (the b-anomaly
    24	preprint's §3 derivation; we do not relitigate it here), and $A$
    25	is a single fitted dimensionless amplitude per dataset. The kernel
    26	shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
    27	This is a \emph{structural} test: same fixed $\Cph$ on the same
    28	$\Rsixhundred$, no shape retuning between datasets.
    29	
    30	\subsection{The five-dataset structural fit}
    31	
    32	The b-anomaly preprint reports the following per-dataset table
    33	(verbatim from~\citep{SmartBAnomaly2026}, also at
    34	\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
    35	
    36	\begin{table}[ht]
    37	\centering
    38	\small
    39	\caption{B-anomaly five-dataset structural fit. Verbatim
    40	from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
    41	dataset, kernel shape held fixed.}
    42	\label{tab:banomaly}
    43	\begin{tabular}{l l r r r r}
    44	\toprule
    45	Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
    46	   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
    47	\midrule
    48	LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
    49	LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
    50	CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
    51	LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
    52	LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
    53	\bottomrule
    54	\end{tabular}
    55	\end{table}
    56	
    57	\subsection{What the structural fit establishes}
    58	
    59	\begin{itemize}\itemsep=2pt
    60	\item \textbf{Universality (5/5).} The same fixed kernel shape
    61	  describes all five datasets. The kernel never moves between
    62	  datasets; only one amplitude $A$ is fitted per dataset.
    63	\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
    64	  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
    65	  reproduces the established direction of the
    66	  anomaly~\citep{LHCbAngular2020} across all five independent
    67	  measurements.
    68	\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
    69	  $B_{s}\!\to\!\phi$ amplitudes differ by a factor partly
    70	  explained by the predicted Krüger--Matias
    71	  $P/S$-basis amplification ($\sim 2.2$~\citep{KrugerMatias2005}).
    72	  The b-anomaly preprint reports a residual factor $\sim 2$ gap
    73	  that the basis-amplification prediction does not account for; the
    74	  preprint flags this as an open item, not a discharge.
    75	\item \textbf{Geometry-first variant test.} Of three discrete
    76	  Laplacian variants on $\Rsixhundred$ (unweighted,
    77	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    78	  unweighted choice wins on both a pure-geometry criterion
    79	  (correlation $0.997$ with the continuum kernel, b-anomaly
    80	  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
    81	  ($\chi^{2}=13.555$). The two criteria agree on the variant
    82	  ranking — a two-criterion convergence on the same fixed
    83	  operator.
    84	\end{itemize}
    85	
    86	\subsection{What the structural fit does \emph{not} establish}
    87	
    88	The b-anomaly preprint is explicit about the following caveats,
    89	which we inherit verbatim:
    90	
    91	\begin{itemize}\itemsep=2pt
    92	\item \textbf{AIC tie on current data.} On Akaike model comparison,
    93	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
    94	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
    95	  indistinguishable: stacked AIC weights
    96	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
    97	  Current data cannot resolve the model comparison. AIC is blind
    98	  to the universality / shape-prediction claim itself, but it is
    99	  decisive about whether the shape is forced by data: it is not.
   100	\item \textbf{Mode-B drift caveat.} A free-width Gaussian
   101	  charm-loop proxy fits the same five datasets comparably in
   102	  $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$ is
   103	  not the unique $q^{2}$ shape consistent with the anomaly.
   104	\item \textbf{Linearised-vs-nonlinear refit drift.} An earlier
   105	  linearised analysis gave a stronger preference
   106	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   107	  the non-linear refit; the $+2.77$-AIC-unit drift is the largest
   108	  single methodological uncertainty in the b-anomaly project.
   109	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   110	  preprint's limitations section acknowledges that the LHCb~2025
   111	  data was looked at first, and only later was the agreement of
   112	  the data-$\chi^{2}$ ranking with the pure-geometry ranking
   113	  verified. The two-criterion agreement is criterion-independent
   114	  but not historically blind.
   115	\end{itemize}
   116	
   117	\subsection{Reading at the operator level}
   118	
   119	The b-anomaly result is the \emph{passive-regime} empirical
   120	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   121	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   122	fixed discrete-to-momentum projection, gives a sign-uniform
   123	description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
   124	five independent measurements without shape retuning. This does
   125	not establish the kernel as theorem-grade physics on the flavour
   126	side (the AIC tie and Mode-B caveats prevent that). It does
   127	establish, at the operator level, that the same fixed $\Cph$ on
   128	the same fixed $\Rsixhundred$ is consistent with one of two
   129	independent empirical landings without parameter retuning. The
   130	second landing is in \S\ref{sec:active_witness}.

 succeeded in 235ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
     6	600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
     7	geometry-fixed response primitive: positive definite under (H1)--(H3)
     8	on the substrate $(M, L_M)$, with smallest eigenvalue $\Ph^{-2}$
     9	and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
    10	The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
    11	$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
    12	Laplacian spectrum with closed-form values in $\mathbb{Z}[\Ph]$
    13	(Table~\ref{tab:spectrum}). The discrete-to-continuum agreement
    14	between $\psi = \Cph^{-1} f$ and the continuum kernel
    15	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex chord distances is
    16	Pearson $\rho = 0.976$ on the unweighted Laplacian, decisively
    17	above the $\Ph$-cocycle weighted variants ($0.888$ geometric,
    18	$0.884$ arithmetic). All numbers are reproduced from canonical
    19	generators by \texttt{repro/verify\_kernel.py}; no parameter is
    20	fitted.
    21	
    22	\textbf{Two independent empirical landings.} The same fixed
    23	$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
    24	retuning between regimes, appears as the load-bearing object in:
    25	\begin{enumerate}\itemsep=2pt
    26	\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
    27	  fitted dimensionless amplitude $A$ per dataset (kernel shape
    28	  held fixed) gives a sign-uniform
    29	  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
    30	  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
    31	  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
    32	  $B_s\to\phi$).
    33	\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
    34	  recurrent self-model layer above the same operator (one
    35	  condition-dependent self-injection coupling
    36	  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
    37	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    38	  degree) passes eighteen preregistered cortical correspondences
    39	  (frozen 2026-04-18) and six drug/sleep EEG signatures.
    40	\end{enumerate}
    41	The two witnesses are independent in the strict sense: no fitted
    42	parameter, threshold, or methodological choice is shared between
    43	them, the kernel is identical, and the empirical claims are tested
    44	on disjoint physical domains (flavour physics vs cortical
    45	neuroscience).
    46	
    47	\textbf{Operator-witness scope.} This is an operator witness, not
    48	a derivation of physics on either landing. We do not derive the
    49	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
    50	claim 600-cell uniqueness; alternative regular 4-polytopes are an
    51	explicit ablation build. We do not claim kernel uniqueness on
    52	either empirical landing; the b-anomaly's Mode-B Gaussian
    53	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
    54	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
    55	aria-chess substrate-witness scope is inherited verbatim. We do
    56	not deliver a selection theorem on the ACT
    57	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
    58	open builds (Lyapunov $V(W)$, edge-space decomposition under
    59	$2I$-equivariance, full reduced-flow convergence) remain open and
    60	are not delivered here.
    61	
    62	\textbf{Programme position.} The cascade-programme home for the
    63	polynomial-in-$L$ Lyapunov family — RH polynomial filter
    64	($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
    65	cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
    66	identified in \S\ref{sec:programme_home}. Family-membership is
    67	\emph{programme-positioned}, not formally classified. The two
    68	empirical landings strengthen external confidence in the
    69	\emph{response} primitive without reducing or addressing the
    70	selection gap.
    71	
    72	We are not aware of a prior preprint that simultaneously names a
    73	geometry-fixed Green operator on a fixed Coxeter graph, with a
    74	design-level mass shift not retuned between regimes, and threads
    75	two independent empirical landings on qualitatively distinct
    76	physical domains. We cannot rule out that such prior work exists.
    77	The empirical material gathered here is the operator witness; the
    78	broader programme to convert the witness into a selection-theorem-
    79	grade claim is sketched in the companion preprints and remains
    80	the natural next step.

 succeeded in 253ms:
     1	% =====================================================================
     2	\section{Programme home and the open selection layer}\label{sec:programme_home}
     3	% =====================================================================
     4	
     5	This section positions $\Cph$ within the broader cascade programme
     6	and identifies what the operator does not deliver. The framing
     7	matters for the hostile-review reading: $\Cph$ is the
     8	\emph{response} primitive; \emph{selection} (which response
     9	configuration the system picks under dynamics) is a separate layer
    10	that this paper does not close.
    11	
    12	\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
    13	
    14	Several constructions across the cascade-programme drafts are
    15	$L$-symmetric polynomial-in-$L$ functionals on a finite-dimensional
    16	substrate. They are programme-positioned as members of the same
    17	family as $\Cph$:
    18	
    19	\begin{itemize}\itemsep=2pt
    20	\item \textbf{RH polynomial filter}~\citep{SmartRHFormal2026}.
    21	  Cascade closure functional on $\mathbb{R}^{120}$:
    22	  $F_{\mathrm{filt}}(x) = \tfrac12 \langle x, p_{\mathrm{fix}}(L)^{2} x\rangle$
    23	  with $\Psi_{t} = e^{-t\, p_{\mathrm{fix}}(L)^{2}}$. Programme-positioned
    24	  as the $\sigma$-fix-annihilator instance of the family: a
    25	  degree-$10$ positive functional vanishing exactly on
    26	  $V_{\mathrm{fix}}$.
    27	\item \textbf{YM cascade gap operator}~\citep{SmartYMMassGap2026}.
    28	  Discrete cascade gap Hamiltonian, programme-positioned as a
    29	  $\Cph$-style mass-regularised Laplacian on $\Rsixhundred$.
    30	\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
    31	  The homeostatic regulariser
    32	  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
    33	  programme-positioned as a member of the same polynomial-in-$L$
    34	  family.
    35	\end{itemize}
    36	
    37	We list the family-membership claim as \emph{programme-positioned},
    38	not formally proved. Each named operator is in a
    39	polynomial-in-$L$ form with positivity and self-adjointness
    40	properties matching the family description; we do not claim a
    41	formal classification theorem identifying the family.
    42	
    43	\subsection{Response vs selection}
    44	
    45	The closure response $\psi = \Cph^{-1} f$ is determined by the
    46	geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
    47	shift $\Ph^{-2}$, and the response is the resulting linear inverse.
    48	This is a \emph{response} primitive. It does \emph{not} answer:
    49	\begin{itemize}\itemsep=2pt
    50	\item Why this substrate? (Selection across regular 4-polytopes
    51	  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
    52	\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
    53	  positive constant.)
    54	\item How does the system pick a response configuration over
    55	  time? (Crystallisation / Lyapunov descent dynamics on a
    56	  $W$-trajectory.)
    57	\end{itemize}
    58	
    59	The selection layer is open. It appears as an open hypothesis in
    60	three independent frames:
    61	\begin{enumerate}\itemsep=2pt
    62	\item \textbf{RH preprint}~\citep{SmartRHFormal2026}: the
    63	  closure-flow suppression hypothesis $\textup{H}_{\mathrm{attr}}$ at
    64	  the level of the original cascade closure functional. The
    65	  polynomial filter $\Psi_{t}$ is a finite-dimensional analogue,
    66	  by design.
    67	\item \textbf{Adaptive Closure
    68	  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
    69	  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
    70	  $V(W)$ on the reduced flow, an edge-space decomposition under
    71	  $2I$-equivariance, and a full reduced-flow convergence theorem
    72	  on $W$-trajectories — \emph{none delivered} in that paper.
    73	\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
    74	  the substrate-witness scope explicitly does \emph{not} deliver
    75	  a selection theorem; ACT is positioned as the future
    76	  selection-theorem witness.
    77	\end{enumerate}
    78	
    79	The convergence of the gap across these three frames is the
    80	strongest programme-level indication that the gap is a single
    81	mathematical problem rather than three independent ones (a
    82	programme-level reading, not a proof of equivalence). The two
    83	empirical witnesses landed in this paper strengthen external
    84	confidence in the \emph{response} primitive without reducing or
    85	addressing the selection gap.
    86	
    87	\subsection{What this paper closes vs leaves open}
    88	
    89	\paragraph{Closes (at the operator-witness level).}
    90	\begin{itemize}\itemsep=2pt
    91	\item The operator $\Cph$ is well-defined, positive definite, and
    92	  has $\|\Cph^{-1}\| = \Ph^{2}$ on any $(M, L_M)$ satisfying
    93	  (H1)--(H3) (\S\ref{sec:definition}).
    94	\item The 600-cell instance $\Rsixhundred$ has the construction
    95	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
    96	  Table~\ref{tab:spectrum}, both reproduced numerically
    97	  (\texttt{repro/verify\_kernel.py}).
    98	\item Discrete-to-continuum agreement at per-vertex Pearson
    99	  correlation $0.976$ on the unweighted variant, with the unweighted
   100	  variant winning the geometry-only criterion against two
   101	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
   102	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
   103	  the load-bearing object in two independent empirical works in
   104	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
   105	  \S\ref{sec:active_witness}).
   106	\end{itemize}
   107	
   108	\paragraph{Leaves open.}
   109	\begin{itemize}\itemsep=2pt
   110	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
   111	  as a design-level shift; not derived from a closure functional
   112	  or symmetry argument.
   113	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
   114	  post-hoc motivated by the empirical landings; alternative regular
   115	  4-polytopes are an explicit ablation build, not a discharged
   116	  comparison.
   117	\item \emph{Kernel-uniqueness on either empirical landing.} The
   118	  b-anomaly Mode-B caveat (free-width Gaussian alternatives fit
   119	  comparably) and the AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
   120	  $w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim from
   121	  ~\citep{SmartBAnomaly2026}.
   122	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
   123	  decomposition under $2I$-equivariance, full reduced-flow
   124	  convergence — all explicitly not delivered
   125	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   126	  here.
   127	\item \emph{Family-membership theorem.} The programme-home
   128	  positioning of cascade Lyapunov functionals as members of the
   129	  same polynomial-in-$L$ family is reported as
   130	  \emph{programme-positioned}, not formally classified.
   131	\end{itemize}

 succeeded in 263ms:
     1	% =====================================================================
     2	\section{Active-regime witness: aria-chess}\label{sec:active_witness}
     3	% =====================================================================
     4	
     5	This section threads the second independent empirical landing of
     6	$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
     7	summarise here only what the operator-witness narrative requires
     8	and inherit the preprint's substrate-witness scope verbatim.
     9	
    10	\subsection{What aria-chess tests}\label{ssec:aria_setup}
    11	
    12	The aria-chess preprint adds a recurrent self-model layer above
    13	the same $\Cph$ on the same $\Rsixhundred$. The architecture
    14	introduces:
    15	\begin{itemize}\itemsep=2pt
    16	\item One \emph{condition-dependent} self-injection coupling
    17	  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
    18	  WAKE/RECOVERY) that controls the strength of the recurrent
    19	  feedback;
    20	\item One \emph{substrate-pinned} nonlinearity
    21	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    22	  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
    23	  $k=12$ is not a free hyperparameter; it is the substrate's
    24	  average degree.
    25	\item Condition-specific \emph{biologically-motivated} stimulus
    26	  models (slow oscillation + spindles + K-complexes for SLEEP\_N3,
    27	  AR(1) noise + tonic shell + attention episodes for WAKE,
    28	  low-amplitude tonic noise for PROPOFOL). These are biologically-
    29	  motivated design choices, not measurement-fits to subject-level
    30	  EEG data.
    31	\end{itemize}
    32	The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
    33	b-anomaly and aria-chess; the same fixed shift used in the
    34	flavour-physics structural fit is used in the cortical substrate
    35	witness.
    36	
    37	\subsection{Eighteen preregistered correspondences}
    38	
    39	Eighteen quantitative predictions (P1--P18) were locked on
    40	2026-04-18 in the aria-chess preprint's
    41	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
    42	validation run. Each prediction has a specific numerical claim, a
    43	falsifiable threshold, and a named validation script. The
    44	preregistered tally as reported in~\citep{SmartAriaChess2026}:
    45	
    46	\begin{itemize}\itemsep=2pt
    47	\item $17/18$ at standard validation methodology ($5$-seed
    48	  cascade block plus state-reset protocol);
    49	\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
    50	  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
    51	  point estimate $+0.190$, $95\%$ CI $[+0.143, +0.239]$,
    52	  $0/2000$ resamples at-or-below zero, reported as $0.0000$).
    53	\item No preregistered threshold has been modified.
    54	\end{itemize}
    55	The aria-chess preprint reports this as methodology refinement
    56	(documented seed-count increase on a high-per-seed-variance
    57	interaction term), \emph{not} as a threshold change. We inherit the
    58	reading verbatim.
    59	
    60	\subsection{Six drug/sleep EEG signatures}
    61	
    62	On a single deterministic substrate trajectory at seed~$42$, the
    63	aria-chess preprint reports six biological signatures testing
    64	against literature-derived thresholds:
    65	
    66	\begin{itemize}\itemsep=2pt
    67	\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
    68	  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — overlaps the
    69	  Sleep-EDFx EEG CI $[2.50, 2.53]$ ($n=30$ subjects) and
    70	  aria-chess's prior cascade pipeline CI $[2.73, 3.25]$ in a
    71	  three-way confidence overlap.
    72	\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
    73	  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
    74	\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
    75	  wake (threshold $\in [1.5, 5.0]$, empirical reference
    76	  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
    77	\item \textbf{Propofol continuity drop}: $+0.066$
    78	  (threshold $> 0.020$).
    79	\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
    80	  direction confirmed; $\Phi$-proxy not full IIT).
    81	\item \textbf{Recovery deterministic identity to wake}: under the
    82	  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
    83	  to the WAKE trajectory.
    84	\end{itemize}
    85	
    86	\subsection{Cross-domain selectivity}
    87	
    88	\begin{itemize}\itemsep=2pt
    89	\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
    90	  positions across $4$ categories on $8$-D V2 features; substrate
    91	  routing lifts leave-one-out classification at canonical depth
    92	  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
    93	  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
    94	\item \textbf{Conversation pattern recognition (P14--P16)}:
    95	  $64$ utterances, $8$ categories; raw classification $87.5\%$,
    96	  substrate-routed lift $-4.4$pp (within the preregistered
    97	  neutrality band $|\cdot| < 10$pp). The substrate is selectively
    98	  amplifying in tasks where raw features are ambiguous and
    99	  approximately neutral when raw features are already
   100	  discriminative.
   101	\item \textbf{HCP brain functional connectivity (P17--P18)}:
   102	  full-cohort descriptive statistics on $n=1003$ subjects show
   103	  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
   104	  homogeneity, $+79.78\sigma$ on raw participation ratio (with
   105	  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
   106	  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
   107	  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
   108	  deviations below the HCP biological cohort.
   109	\end{itemize}
   110	
   111	\subsection{Reading at the operator level}
   112	
   113	The aria-chess result is the \emph{active-regime} empirical
   114	witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
   115	layer above $\Cph$ uses one condition-dependent coupling and one
   116	substrate-pinned nonlinearity at the graph's average degree
   117	$k=12$; no other shape parameter enters; the kernel shift
   118	$\Ph^{-2}$ is not retuned. Under those design choices, the same
   119	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
   120	preregistered cortical correspondences (frozen 2026-04-18) and six
   121	literature-thresholded EEG drug/sleep signatures.
   122	
   123	The aria-chess preprint stays inside substrate-witness scope: it
   124	does not claim the substrate \emph{is} consciousness, does not
   125	claim 600-cell uniqueness among regular 4-polytopes, and does not
   126	deliver a selection theorem on the ACT 4-tuple. We inherit the
   127	scope verbatim. What we add at the operator level is the
   128	observation that the same fixed $\Cph$ — under no shape-parameter
   129	retuning between regimes — is the load-bearing object on both
   130	empirical landings.
   131	
   132	\subsection{Two-witness structure}
   133	
   134	\begin{table}[ht]
   135	\centering
   136	\small
   137	\caption{Two independent empirical landings of $\Cph$ on
   138	$\Rsixhundred$, with no shape retuning between regimes.}
   139	\label{tab:two_witness}
   140	\begin{tabular}{l l l}
   141	\toprule
   142	& Passive regime & Active regime \\
   143	\midrule
   144	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   145	Domain             & flavour physics                    & cortical neuroscience \\
   146	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) &
   147	                     prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   148	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   149	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   150	Shift $\Ph^{-2}$     & not retuned                       & not retuned \\
   151	Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
   152	Free parameters    & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition \\
   153	Caveat             & AIC tie; Mode-B kernel non-uniqueness &
   154	                     single-seed; no polytope ablation \\
   155	\bottomrule
   156	\end{tabular}
   157	\end{table}
   158	
   159	The two witnesses are independent in the strict sense: no fitted
   160	parameter, threshold, or methodological choice is shared between
   161	them. The b-anomaly amplitude $A$ is fitted to flavour-physics
   162	$q^{2}$ shape; the aria-chess coupling $\eta$ is fixed by
   163	condition not by neural data. The kernel is identical.

 succeeded in 246ms:
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested
    15	whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
    16	Coxeter graphs would give comparable per-vertex correlations on
    17	the discrete-to-continuum agreement test, or comparable structural
    18	fits on either empirical landing. The 600-cell choice is post-hoc
    19	motivated by the empirical landings, not from an a-priori
    20	derivation. \emph{Disclosure:} \S\ref{sec:intro},
    21	\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
    22	\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
    23	empirical landings of \S\ref{sec:passive_witness} and
    24	\S\ref{sec:active_witness}. \emph{Strengthening build:}
    25	\texttt{repro/verify\_kernel.py} extension to the $24$-cell and
    26	$120$-cell, with the same per-vertex correlation criterion
    27	applied; verbatim re-run of the b-anomaly fit on alternative
    28	substrates from~\citep{SmartBAnomaly2026}; the aria-chess
    29	preprint's regime section already lists alternative-polytope
    30	ablation as an open build.
    31	
    32	\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
    33	nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
    34	comparable per-vertex correlation, or whether the empirical
    35	landings tolerate a shift sweep. The shift is held fixed across
    36	both regimes; perturbation analysis is an open build.
    37	\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
    38	for $\delta \in \{0.01, 0.05, 0.10, 0.25\}$ on the discrete-to-
    39	continuum correlation; report sensitivity envelope.
    40	
    41	\subsection{Post-hoc}\label{ssec:posthoc}
    42	
    43	\textbf{The 600-cell choice is post-hoc justified by empirical
    44	observables.} While the construction of $\Rsixhundred$ is
    45	theorem-level rigorous (H$_4$ Coxeter group theory), the choice
    46	of \emph{this} polytope as the discrete substrate instance is
    47	motivated by the empirical landings observed, not by an a-priori
    48	geometric or algebraic argument selecting it over the $24$-cell
    49	or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
    50	\emph{Evidence:} two independent empirical witnesses on
    51	$\Rsixhundred$. \emph{Strengthening build:} formal substrate
    52	ablation (above).
    53	
    54	\textbf{The geometry-first variant agreement is not historically
    55	blind on b-anomaly.} Per the b-anomaly preprint's limitations
    56	section, the LHCb 2025 data was inspected first and the
    57	pure-geometry ranking was verified afterward to agree with the
    58	data-$\chi^{2}$ ranking. The two-criterion convergence is
    59	\emph{criterion-independent} (geometry-only correlation here is a
    60	different test from b-anomaly's data $\chi^{2}$) but not
    61	historically pre-registered. \emph{Disclosure:} we inherit the
    62	caveat verbatim. \emph{Strengthening build:} a future blind variant
    63	test would freeze the variant choice before observing the data
    64	$\chi^{2}$.
    65	
    66	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    67	$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
    68	strictly positive definite; it is not derived from a closure
    69	functional or symmetry argument. \emph{Disclosure:}
    70	\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
    71	same operator with the same shift serves as the basis for two
    72	independent empirical witnesses across qualitatively distinct
    73	regimes (\S\ref{sec:passive_witness},
    74	\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
    75	the $\Ph^{-2}$ shift as the unique stability clamp under a named
    76	regularity criterion (e.g.\ minimum-amplitude amplification on a
    77	specified function class).
    78	
    79	\subsection{Interpretation}\label{ssec:interpretation}
    80	
    81	\textbf{The discrete-to-continuum agreement is descriptive, not
    82	causal.} The per-vertex correlation $0.976$ between $\psi$ on
    83	$\Rsixhundred$ and the continuum kernel
    84	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
    85	\emph{computed agreement} between two independently-defined
    86	objects, not a derivation that the discrete operator equals the
    87	continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
    88	this explicitly. \emph{Evidence:} the agreement is at machine
    89	precision in the operator-norm bound and at $\rho = 0.976$ in the
    90	per-vertex correlation. \emph{Strengthening build:} a formal
    91	discrete-continuum convergence proof under a specified large-graph
    92	limit; a continuum limit theorem on H$_n$ Coxeter substrates as
    93	$n \to \infty$.
    94	
    95	\textbf{Variant ranking is criterion-dependent.} The unweighted
    96	variant wins on both the geometry-only criterion of this paper
    97	and b-anomaly's data $\chi^{2}$, but neither criterion is the
    98	\emph{unique} natural ranking. Edge-weighted variants outside the
    99	$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
   100	Laplacian) are not tested here. \emph{Strengthening build:}
   101	extend \texttt{repro/verify\_kernel.py} to a wider variant
   102	catalogue.
   103	
   104	\subsection{Test/claim}\label{ssec:testclaim}
   105	
   106	\textbf{Two independent empirical landings, not formal physics.}
   107	The b-anomaly result is a structural fit (kernel shape held fixed)
   108	under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
   109	aria-chess result is a substrate witness (no claim that the
   110	substrate \emph{is} consciousness). Neither lands a theorem-grade
   111	physics claim on its own domain; both are appropriately
   112	hedged in their own preprints, and we inherit those hedges
   113	verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
   114	\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
   115	their own preregistered or literature-derived thresholds.
   116	\emph{Strengthening build:} more flavour-physics datasets
   117	(LHCb Run~3, Belle~II) for the passive-regime witness;
   118	cross-cohort EEG (TUH, NHM) and cross-parcellation HCP
   119	(Schaefer, Glasser) for the active-regime witness; both already
   120	listed in the respective preprints.
   121	
   122	\textbf{Discrete-to-continuum correlation is single-source.} The
   123	per-vertex correlation $0.976$ is computed from a single source
   124	vertex ($+x_{0}$ axis, the canonical pole). H$_4$ transitivity
   125	guarantees that any other source vertex gives the same correlation
   126	up to numerical precision (transitivity acts on $V$, and the
   127	shell decomposition is preserved); \texttt{repro/verify\_kernel.py}
   128	verifies this for the chosen pole. A multi-source robustness sweep
   129	is recorded in the script's output but is not headlined here.
   130	
   131	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   132	
   133	\textbf{Selection layer not delivered.} As enumerated in
   134	\S\ref{sec:programme_home}, the selection-layer constructions
   135	(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
   136	full reduced-flow convergence) are open in the companion ACT
   137	preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
   138	delivered here. The two empirical witnesses strengthen confidence
   139	in the response primitive without addressing the selection gap.
   140	
   141	\textbf{No deuteron / hadron / RH / capstone material is loaded
   142	into this paper.} The cascade-derivation programme, the capstone
   143	coalgebra paper, and the Millennium drafts share operator-level
   144	infrastructure with this paper but are not load-bearing here.
   145	Deliberately out of scope.
   146	
   147	\textbf{Out-of-scope items NOT delivered (correctly).}
   148	\begin{itemize}\itemsep=2pt
   149	\item Lyapunov function $V(W)$ on the reduced flow — open build
   150	  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
   151	\item $2I$-equivariance audit of the closure operator family —
   152	  open build of ACT.
   153	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   154	  Hodge edge Laplacian — open build of ACT.
   155	\item Selection theorem identifying $\Rsixhundred$ over alternative
   156	  regular 4-polytopes — see \S\ref{ssec:regime}.
   157	\item Formal discrete-to-continuum convergence theorem under a
   158	  specified large-graph limit — see \S\ref{ssec:interpretation}.
   159	\item First-principles derivation of the $\Ph^{-2}$ shift — see
   160	  \S\ref{ssec:posthoc}.
   161	\item Family-membership classification theorem for the
   162	  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
   163	\end{itemize}
   164	
   165	\subsection{The honest verdict}
   166	
   167	The result is an \emph{operator witness}: a geometry-fixed response
   168	operator on a fixed graph, with no shape parameters tuned to any
   169	dataset, is consistent with two independent empirical landings in
   170	qualitatively distinct regimes. We do not claim the operator is
   171	the unique kernel for either landing. We do not claim selection is
   172	delivered. We do not claim 600-cell uniqueness. The strengthening
   173	builds for stronger claims are listed above and remain open.

codex
The kernel paper’s own structure is mostly disciplined: it repeatedly marks the operator-witness boundary. I’m now checking the numerical artifact and the two source/companion documents, because the highest-risk issues are inherited claims and exact-number drift.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/verify_kernel.py' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba docs/aria-closure-kernel.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 245ms:
     1	# ARIA Closure-Response Green Kernel and the Cascade Programme
     2	
     3	**Status (2026-04-29).** Programme-level vocabulary: response
     4	primitive defined; externally witnessed by a structural sign-uniform
     5	test (b-anomaly paper, §4 below) without a model-preference claim;
     6	selection / crystallisation dynamics still open. This note is
     7	non-load-bearing for any individual Millennium paper; it documents
     8	the programme-wide home for the polynomial-in-$L$ Lyapunov family
     9	that recurs across the Millennium drafts.
    10	
    11	## 1. The closure-response operator
    12	
    13	Let $M$ be a closure substrate (graph, simplicial complex, or
    14	projected coordinate). Let $L_M$ be its Laplacian. Define the
    15	**$\varphi$-regularised closure operator**
    16	$$
    17	C_\varphi \;=\; L_M + \varphi^{-2} I.
    18	$$
    19	For a non-negative localised source $f$ on $M$, the **closure
    20	response field** is
    21	$$
    22	\psi \;=\; C_\varphi^{-1} f \;=\; (L_M + \varphi^{-2} I)^{-1} f.
    23	$$
    24	This is a Green's-function inverse. For self-adjoint non-negative
    25	$L_M$ on $M$ (e.g. the standard graph Laplacian on a connected
    26	finite graph, or the standard continuum Laplace operator with
    27	free-space / decay-at-infinity boundary conditions), $C_\varphi$
    28	is positive definite and $\varphi^{-2}$ acts as a coherence-length /
    29	mass regularisation; for a non-negative source $f$ on such an $M$,
    30	$\psi$ is non-oscillatory and centred on the support of $f$. In
    31	the continuum case with smooth $f$, $\psi$ is regular away from
    32	the singular support of $f$. (On a finite graph, "smoothness" is
    33	not directly meaningful; the regularity statement is a discrete
    34	exponential-decay envelope around the source, not a derivative
    35	condition.) Substrates outside this hypothesis class (e.g.
    36	projected coordinates with non-standard boundary conditions, or
    37	Laplacians with negative spectrum) require their own analysis.
    38	
    39	## 2. Continuum projection
    40	
    41	In one projected coordinate $x$, $L_\varphi = -d^2/dx^2 + \varphi^{-2}$,
    42	$L_\varphi G = \delta$, with closed-form Green's function
    43	$$
    44	G(x) \;=\; \frac{\varphi}{2}\, e^{-|x|/\varphi}.
    45	$$
    46	Normalised, this is the practical kernel
    47	$\kappa(x) = e^{-|x|/\varphi}$. The decay scale is $\varphi$.
    48	
    49	## 3. Discrete substrate: the 600-cell
    50	
    51	The discrete VFD lift uses the 600-cell graph $V_{600}$:
    52	- 120 vertices, 720 edges, each vertex degree 12;
    53	- edges defined by $\langle v, w \rangle = \varphi/2$;
    54	- 9-shell decomposition emerging intrinsically as
    55	  $\{1, 12, 20, 12, 30, 12, 20, 12, 1\}$;
    56	- antipodal symmetry $s(-v) = 8 - s(v)$.
    57	
    58	The discrete response is
    59	$\psi(v) = (L_{V_{600}} + \varphi^{-2} I)^{-1} f(v)$.
    60	
    61	**Compression diagnostic.** The b-anomaly headline fits use the
    62	full Green response on $V_{600}$. A spectral truncation diagnostic
    63	(`archive/reports/wo011_spectral.csv`) reports the relative
    64	reconstruction error stepping from $0.076$ (modes 1-8, with
    65	$\lambda_{\max}$ reaching $5.528$ at mode 6) to $0.040$ (modes
    66	9-14) and remaining at $0.040$ through mode 30; mode 15 marks the
    67	entry of the truncation into the $\lambda = 9$ block, not an
    68	additional error drop. This is a *spectral diagnostic of
    69	compression depth*, not a rank-1 projection map; the b-anomaly
    70	fits do not use the truncation. (The canonical full spectrum of
    71	the $V_{600}$ Laplacian has eigenvalue $9$ with multiplicity $16$;
    72	the multiplicity-6 figure originally reported in some prose is
    73	not consistent with the canonical spectrum or with the b-anomaly's
    74	own wo011 CSV and is dropped here.)
    75	
    76	## 4. Empirical validation: shipped five-dataset b-anomaly structural test
    77	
    78	Independent passive-regime witness for $C_\varphi$ ships in the
    79	b-anomaly repository (`/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/`,
    80	preprint `paper/main.pdf`, repro `repro/run_all.sh`). The witness is
    81	a **structural** test, not a detection claim or AIC preference:
    82	
    83	> A single fixed response kernel $\kappa(q^{2})$ — derived from the
    84	> 600-cell $V_{600}$ graph regularised by $\varphi^{-2}$ as a
    85	> discrete mass scale, with no shape parameters tuned to data —
    86	> provides a consistent description of the $q^{2}$ behaviour of the
    87	> $b\to s\mu^{+}\mu^{-}$ angular anomaly across **five public
    88	> datasets covering two collaborations, two isospin partners, and
    89	> three decay channels**. Only one dimensionless amplitude $A$ is
    90	> fitted per dataset; the kernel shape itself never moves.
    91	
    92	**Per-dataset table** (verbatim from `BANOMALY-001/vfd-b-anomaly/README.md`):
    93	
    94	| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
    95	|---|---|---:|---:|---:|---:|
    96	| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
    97	| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
    98	| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
    99	| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
   100	| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |
   101	
   102	**What the b-anomaly paper claims (source scope; bullets summarise from `README.md:24-28` plus paper §§6-7 detail):**
   103	
   104	- **Universality.** Same fixed kernel for all five datasets, one
   105	  amplitude per dataset, no shape retuning.
   106	- **Sign uniformity.** $A>0$ in **5/5** fits;
   107	  $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel
   108	  reproduces the established direction of the anomaly across all
   109	  five independent measurements.
   110	- **Cross-channel ratio.** $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
   111	  amplitudes differ by a factor partly explained by the predicted
   112	  Krüger–Matias $P$/$S$-basis amplification ($\sim 2.2$). The
   113	  detailed cross-channel section reports a predicted amplitude of
   114	  $+2.5$ vs the observed $+4.98$, leaving a factor $\sim 2$
   115	  residual gap that the basis-amplification prediction does not
   116	  account for.
   117	- **Geometry-first variant test.** Of three discrete Laplacian
   118	  variants, the unweighted choice wins on a pure-geometry criterion
   119	  (correlation $0.997$ with the continuum kernel); the same variant
   120	  also wins on the data $\chi^{2}$ — independent geometry and data
   121	  criteria agree. The two-criterion agreement is criterion-independent
   122	  but not historically blind: the b-anomaly limitations section
   123	  (`paper/sections/09_limitations.tex`) acknowledges that the data
   124	  was looked at first and only later verified to agree with the
   125	  pure-geometry ranking.
   126	
   127	**Statistical caveat (what the b-anomaly paper does NOT claim):**
   128	
   129	- On Akaike model comparison, the kernel and a constant
   130	  Wilson-coefficient shift ($\mathrm{FREE\_C9}$, also $k=1$) are
   131	  statistically indistinguishable on current data: stacked
   132	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   133	  Current data cannot resolve the model comparison. AIC is blind to
   134	  the universality/shape-prediction claim itself.
   135	- In the Mode-B stress test, a free-width Gaussian charm-loop
   136	  proxy fits comparably in $\chi^{2}$ at the cost of one extra
   137	  shape parameter; the kernel is *not* the unique $q^{2}$ shape
   138	  consistent with the anomaly.
   139	- An earlier linearised "Mode B" analysis gave a stronger
   140	  numerical preference for the kernel
   141	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that **did not
   142	  survive the non-linear refit**. The $+2.77$-AIC-unit drift is the
   143	  largest single methodological uncertainty in the project.
   144	
   145	**Cocycle convergence (operator-level, not edge-weight-level).**
   146	The b-anomaly geometry-first variant test compares three discrete
   147	edge-weighting schemes on $V_{600}$ — `UNWEIGHTED`,
   148	`PHI_GEOMETRIC` ($w_{vw} = \sqrt{\omega_+(v)\,\omega_+(w)}$ with
   149	$\omega_+(v) = \varphi^{\kappa(v)}$), and `PHI_ARITHMETIC`
   150	($w_{vw} = \tfrac{1}{2}[\omega_+(v) + \omega_+(w)]$) — under
   151	both a pure-geometry criterion (correlation with the continuum
   152	kernel) and a data criterion (LHCb 2025 $\chi^2$). The
   153	`UNWEIGHTED` Laplacian variant wins on both criteria
   154	(correlation $0.9968$ with the continuum kernel, data
   155	$\chi^2 = 13.555$; b-anomaly paper §3.4 Table 1, also
   156	`reports/wo016b_variant_geometry.md`). The φ-cocycle-weighted
   157	variants ($\omega_+(v) = \varphi^{\kappa(v)}$) are tested and
   158	**lose** on both criteria. So the b-anomaly result empirically
   159	strengthens the **unweighted** $L_{V_{600}} + \varphi^{-2} I$
   160	response operator and the 9-shell projection (which enters at the
   161	shell-mean step, not as an edge weight); it does **not**
   162	empirically strengthen the κ cocycle as an operative edge
   163	weighting.
   164	
   165	The cocycle convergence with the RH paper's pentagonal-clock
   166	$\kappa(v) = (s(v) - 4)^2$ (`papers/millennium-rh-formal/rh-formal.tex`,
   167	Definition `def:kappa`) is therefore **structural**: the same
   168	shell-grade pattern $\varphi^{0,1,4,9,16}$ shows up in both the
   169	discrete VFD lift's variant catalogue and the RH paper's cocycle.
   170	This is a theoretical convergence on a shared algebraic shell-grade
   171	infrastructure, not an empirical claim. ẑ **shares operator-level
   172	infrastructure** with the b-anomaly response operator (the same
   173	$V_{600} + \varphi^{-2} I$, the same 9-shell decomposition, the
   174	same shell-grade pattern $\varphi^{0,1,4,9,16}$); ẑ does **not**
   175	inherit any empirical claim about classical RH or the critical
   176	line.
   177	
   178	## 5. Programme home for cascade Lyapunov / projector functionals
   179	
   180	Several cascade-internal constructions are $L$-symmetric
   181	polynomial-in-$L$ functionals on a finite-dimensional substrate.
   182	They are positioned as programme-proposed members of the same
   183	family as $C_\varphi$ (the family-membership claim is not formally
   184	canonical and is not proved in any of the cited Millennium drafts):
   185	
   186	- **RH polynomial filter** (`rh-formal.tex`,
   187	  `def:closure_flow`): $F_{\mathrm{filt}}(x)
   188	  = \tfrac{1}{2}\langle x, p_{\mathrm{fix}}(L)^2 x\rangle$ with
   189	  $\Psi_t = e^{-t\,p_{\mathrm{fix}}(L)^2}$. Programme-positioned
   190	  as the **σ-fix-annihilator** instance of the family: a
   191	  degree-$10$ positive functional on $\R^{120}$ vanishing exactly
   192	  on $V_{\mathrm{fix}}$.
   193	- **YM cascade gap operator** (`ym-mass-gap.tex`,
   194	  Section~\ref{sec:cascade-gap}): the discrete cascade gap
   195	  Hamiltonian is programme-positioned as a $C_\varphi$-style
   196	  mass-regularised Laplacian on the 600-cell substrate.
   197	- **NS regularity functional** (`ns-formal.tex`): the cascade
   198	  hydrodynamic projector is programme-positioned in the same
   199	  Lyapunov-of-polynomial-in-$L$ family.
   200	- **BSD operator** (`bsd-formal.tex`): $T_E$ on the enlarged
   201	  Hecke module is programme-positioned as a
   202	  response-operator-family member.
   203	- **Hodge $\sigma$-projector** (`hodge-formal.tex`): the cascade
   204	  $\sigma$-projector is programme-positioned as a rank-1 /
   205	  spectral-projection limit of the same family.
   206	- **PNP cascade refinement** (`pnp-formal.tex`): the cascade
   207	  refinement on the restricted model class is programme-positioned
   208	  as a response-kernel projection in the bounded-resource regime.
   209	
   210	In each case the cascade construction is positioned as a
   211	programme-proposed family instance, selected by the structural role
   212	it plays in the corresponding Millennium reduction. These are not
   213	arbitrary constructions, but the family-membership claim is not
   214	formally canonical and is not proved in any of the cited papers.
   215	
   216	## 6. Response vs selection: the open layer
   217	
   218	The closure response primitive now has a **shipped passive-regime
   219	empirical landing**: the b-anomaly paper (§4 above) tests the fixed
   220	$C_\varphi$-derived $V_{600}$ kernel without shape retuning across
   221	five public flavour-physics datasets covering two collaborations,
   222	two isospin partners, and three decay channels. This **does not
   223	close the selection layer**. The active-regime companion remains
   224	the ARIA / aria-chess selection paper: a learning-rule / Lyapunov /
   225	coherence-descent construction for $W$-space, *not supplied* by
   226	b-anomaly.
   227	
   228	The closure response $\psi = C_\varphi^{-1} f$ is derived from
   229	geometry. It is *not* a selection rule. Crystallisation
   230	additionally requires a selection dynamic — a Lyapunov / coherence
   231	descent rule
   232	$$
   233	dW/dt \;=\; -\nabla V(W)
   234	$$
   235	or equivalent — that selects which response is the stable
   236	attractor.
   237	
   238	This selection layer is **open**. The same gap appears in three
   239	independent frames:
   240	- **RH paper**: open $\textup{H}_{\mathrm{attr}}$ at the level of
   241	  the original cascade closure functional (the polynomial filter
   242	  $\Psi_t$ is only a finite-dimensional analogue, by design).
   243	- **Adaptive Closure Transport** (`papers/adaptive-closure-transport/`):
   244	  edge-space lift / Lyapunov mechanism for the selection programme,
   245	  explicitly left open (lines 327--328, 377--382 of that paper).
   246	- **ARIA framework**: crystallisation / coherence-descent rule,
   247	  named as the next layer above response. The aria-chess paper
   248	  (active-regime empirical companion to adaptive-closure-transport)
   249	  is **named, not yet written**.
   250	
   251	The convergence of the gap across these three frames is the
   252	strongest programme-level indication that the gap is a single
   253	mathematical problem rather than three independent ones (a
   254	programme-level reading, not a proof of equivalence). The
   255	passive-regime b-anomaly landing strengthens external confidence
   256	in the *response* primitive without reducing or addressing the
   257	selection gap.
   258	
   259	## 7. Canonical references in this repository
   260	
   261	- `papers/millennium-rh-formal/rh-formal.tex` — polynomial filter
   262	  $F_{\mathrm{filt}}$ as σ-fix-annihilator family member (closing
   263	  subsection).
   264	- `papers/millennium-ym/ym-mass-gap.tex` — cascade gap operator as
   265	  $C_\varphi$-style member.
   266	- `papers/millennium-ns-formal/ns-formal.tex` — regularity
   267	  functional as family member.
   268	- `papers/millennium-bsd-formal/bsd-formal.tex` — $T_E$ as
   269	  family member.
   270	- `papers/millennium-hodge-formal/hodge-formal.tex` — σ-projector
   271	  as rank-1 limit.
   272	- `papers/millennium-pnp-formal/pnp-formal.tex` — cascade
   273	  refinement as response-kernel projection.
   274	- `papers/adaptive-closure-transport/adaptive-closure-transport.tex` —
   275	  selection layer, open.
   276	- `docs/convergence-with-smart.md` — programme-level architectural
   277	  consilience between cascade and Smart frames.
   278	- `docs/projection-narrative.md` (and related) — Layer 1 mainstream
   279	  coherence earning Layer 2 realisation.
   280	- `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf` —
   281	  primary shipped passive-regime empirical witness for the fixed
   282	  $C_\varphi$-derived $V_{600}$ kernel; five-dataset sign-uniform
   283	  structural test (LHCb + CMS, $K^{*0}/K^{*+}/\phi$ channels) with
   284	  honest AIC tie ($w_{\mathrm{VFD}} = 0.348$ vs
   285	  $w_{\mathrm{FREE\_C9}} = 0.652$) and Mode-B $+2.77$ drift caveat.
   286	- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md` —
   287	  Layer 1 + Layer 2 derivation (supporting).
   288	- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md` —
   289	  Layer 3 numerical bridge (supporting).
   290	- `BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md` —
   291	  variant-selection table; the unweighted Laplacian wins on both
   292	  pure-geometry and data $\chi^2$ criteria.
   293	- `BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md` —
   294	  Mode-B drift documentation; the largest single methodological
   295	  uncertainty in the project.

 succeeded in 264ms:
     1	{
     2	  "phi": 1.618033988749895,
     3	  "phi_inv_sq": 0.3819660112501051,
     4	  "n_vertices": 120,
     5	  "n_edges": 720,
     6	  "degree_sequence": {
     7	    "min": 12,
     8	    "max": 12,
     9	    "mean": 12.0
    10	  },
    11	  "shell_sizes": {
    12	    "0": 1,
    13	    "1": 12,
    14	    "2": 20,
    15	    "3": 12,
    16	    "4": 30,
    17	    "5": 12,
    18	    "6": 20,
    19	    "7": 12,
    20	    "8": 1
    21	  },
    22	  "shell_inner_products": [
    23	    1.0,
    24	    0.8090169943749475,
    25	    0.5,
    26	    0.3090169943749474,
    27	    0.0,
    28	    -0.3090169943749474,
    29	    -0.5,
    30	    -0.8090169943749475,
    31	    -1.0
    32	  ],
    33	  "antipodal_check": {
    34	    "pole_idx": 119,
    35	    "antipode_idx": 0,
    36	    "expected_shell_8_size": 1,
    37	    "observed_shell_8_size": 1
    38	  },
    39	  "laplacian_spectrum_grouped": [
    40	    {
    41	      "eigenvalue": -0.0,
    42	      "multiplicity": 1
    43	    },
    44	    {
    45	      "eigenvalue": 2.291796067500629,
    46	      "multiplicity": 4
    47	    },
    48	    {
    49	      "eigenvalue": 5.527864045000407,
    50	      "multiplicity": 9
    51	    },
    52	    {
    53	      "eigenvalue": 8.999999999999993,
    54	      "multiplicity": 16
    55	    },
    56	    {
    57	      "eigenvalue": 11.999999999999984,
    58	      "multiplicity": 25
    59	    },
    60	    {
    61	      "eigenvalue": 13.999999999999977,
    62	      "multiplicity": 36
    63	    },
    64	    {
    65	      "eigenvalue": 14.472135954999567,
    66	      "multiplicity": 9
    67	    },
    68	    {
    69	      "eigenvalue": 14.999999999999988,
    70	      "multiplicity": 16
    71	    },
    72	    {
    73	      "eigenvalue": 15.708203932499362,
    74	      "multiplicity": 4
    75	    }
    76	  ],
    77	  "operator_norm": {
    78	    "lambda_min_L": -1.01103545984405e-15,
    79	    "lambda_min_C_phi": 0.3819660112501041,
    80	    "operator_norm_C_phi_inv": 2.618033988749902,
    81	    "predicted_phi_squared": 2.618033988749895
    82	  },
    83	  "discrete_continuum_test": {
    84	    "shell_radii": [
    85	      0.0,
    86	      0.6180339887498948,
    87	      1.0,
    88	      1.1755705045849465,
    89	      1.4142135623730947,
    90	      1.618033988749895,
    91	      1.7320508075688772,
    92	      1.902113032590307,
    93	      2.0
    94	    ],
    95	    "shell_count": [
    96	      1,
    97	      12,
    98	      20,
    99	      12,
   100	      30,
   101	      12,
   102	      20,
   103	      12,
   104	      1
   105	    ],
   106	    "shell_psi_mean": [
   107	      0.11466009151487011,
   108	      0.034976446331995696,
   109	      0.024335208435661275,
   110	      0.021858804323929084,
   111	      0.019268782150762213,
   112	      0.01765857292134354,
   113	      0.016902552852001883,
   114	      0.015932370381507646,
   115	      0.01544087945358437
   116	    ],
   117	    "continuum_prediction": [
   118	      0.8090169943749475,
   119	      0.5521688638304681,
   120	      0.43606265394423777,
   121	      0.3912228691703586,
   122	      0.33757505628626344,
   123	      0.29762071978885557,
   124	      0.2773703603621507,
   125	      0.24969730865080123,
   126	      0.23503911473677247
   127	    ],
   128	    "pearson_correlation": 0.9232082699765517
   129	  },
   130	  "variant_correlation": {
   131	    "UNWEIGHTED": {
   132	      "shell_mean_correlation": 0.9232082699765517,
   133	      "per_vertex_correlation": 0.9762022978516623
   134	    },
   135	    "PHI_GEOMETRIC": {
   136	      "shell_mean_correlation": 0.879553132802029,
   137	      "per_vertex_correlation": 0.8883800503732451
   138	    },
   139	    "PHI_ARITHMETIC": {
   140	      "shell_mean_correlation": 0.8784315463215415,
   141	      "per_vertex_correlation": 0.8843640031310793
   142	    }
   143	  }
   144	}

 succeeded in 257ms:
     1	#!/usr/bin/env python3
     2	"""
     3	Aria closure kernel — numerical verification.
     4	
     5	Constructs V_600 from canonical generators, builds the short-edge
     6	nearest-neighbour graph, computes the Laplacian spectrum, builds
     7	C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
     8	test (shell-mean projection vs (phi/2) exp(-|x|/phi)), tests the
     9	unweighted vs phi-cocycle-weighted Laplacian variants on a
    10	geometry-only correlation criterion, and writes results.json.
    11	
    12	All constants (phi, the 600-cell vertex generators, the short-edge
    13	inner product phi/2) are mathematically determined by the choice of
    14	substrate; no parameter is fitted to any dataset.
    15	
    16	Determinism: numpy RNG is seeded only for the localised-source
    17	positions (seed 42); the eigendecomposition is deterministic.
    18	
    19	Run: python3 verify_kernel.py
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	import json
    25	import itertools
    26	import math
    27	from pathlib import Path
    28	
    29	import numpy as np
    30	from numpy.linalg import eigh, norm
    31	from scipy.spatial.distance import pdist, squareform
    32	
    33	
    34	PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
    35	INV_PHI = 1.0 / PHI                          # = phi - 1
    36	INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966
    37	
    38	
    39	# ---------------------------------------------------------------------------
    40	# 1. 600-cell vertex construction (120 vertices on S^3)
    41	# ---------------------------------------------------------------------------
    42	
    43	def even_perms(seq):
    44	    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    45	    n = len(seq)
    46	    out = []
    47	    for p in itertools.permutations(range(n)):
    48	        # signature
    49	        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    50	        if inv % 2 == 0:
    51	            out.append(tuple(seq[p[i]] for i in range(n)))
    52	    return out
    53	
    54	
    55	def build_v600():
    56	    """
    57	    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.
    58	
    59	    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    60	    - 16 vertices: all sign combinations of (+/- 1/2)^4
    61	    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
    62	      with all sign assignments
    63	    """
    64	    verts = set()
    65	
    66	    # 8 axis vertices
    67	    for sign in (-1, 1):
    68	        for i in range(4):
    69	            v = [0.0] * 4
    70	            v[i] = float(sign)
    71	            verts.add(tuple(v))
    72	
    73	    # 16 half-integer vertices
    74	    for signs in itertools.product((-1, 1), repeat=4):
    75	        v = tuple(0.5 * s for s in signs)
    76	        verts.add(v)
    77	
    78	    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    79	    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    80	    for signs in itertools.product((-1, 1), repeat=4):
    81	        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
    82	        signed = tuple(s * b for s, b in zip(signs, base))
    83	        for p in even_perms(signed):
    84	            verts.add(p)
    85	
    86	    V = np.array(sorted(verts), dtype=np.float64)
    87	    # Sanity check: all on the unit 3-sphere
    88	    radii = np.linalg.norm(V, axis=1)
    89	    assert np.allclose(radii, 1.0, atol=1e-10), \
    90	        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    91	    return V
    92	
    93	
    94	# ---------------------------------------------------------------------------
    95	# 2. Short-edge nearest-neighbour graph
    96	# ---------------------------------------------------------------------------
    97	
    98	def build_short_edge_graph(V, tol=1e-10):
    99	    """
   100	    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
   101	    criterion on the unit 3-sphere). For the 600-cell this gives a
   102	    12-regular graph on 120 vertices with 720 edges.
   103	    """
   104	    G = V @ V.T  # Gram matrix of inner products
   105	    short = PHI / 2.0
   106	    A = (np.abs(G - short) < tol).astype(np.float64)
   107	    np.fill_diagonal(A, 0.0)  # no self-loops
   108	    return A
   109	
   110	
   111	# ---------------------------------------------------------------------------
   112	# 3. Laplacian spectrum
   113	# ---------------------------------------------------------------------------
   114	
   115	def laplacian_spectrum(A):
   116	    """L = D - A; return sorted eigenvalues + eigenvectors."""
   117	    D = np.diag(A.sum(axis=1))
   118	    L = D - A
   119	    w, U = eigh(L)  # ascending order
   120	    return L, w, U
   121	
   122	
   123	def round_spectrum(w, decimals=6):
   124	    """Group eigenvalues into multiplicity classes (within numerical tol)."""
   125	    classes = []
   126	    seen = []
   127	    for val in w:
   128	        placed = False
   129	        for idx, ref in enumerate(seen):
   130	            if abs(val - ref) < 10 ** (-decimals):
   131	                classes[idx] = (ref, classes[idx][1] + 1)
   132	                placed = True
   133	                break
   134	        if not placed:
   135	            seen.append(val)
   136	            classes.append((round(float(val), decimals), 1))
   137	    return classes
   138	
   139	
   140	# ---------------------------------------------------------------------------
   141	# 4. Closure operator and discrete Green's function
   142	# ---------------------------------------------------------------------------
   143	
   144	def build_C_phi(L):
   145	    """C_phi = L + phi^-2 I."""
   146	    return L + INV_PHI2 * np.eye(L.shape[0])
   147	
   148	
   149	def green_response(C_phi, source_idx):
   150	    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
   151	    n = C_phi.shape[0]
   152	    f = np.zeros(n)
   153	    f[source_idx] = 1.0
   154	    psi = np.linalg.solve(C_phi, f)
   155	    return psi
   156	
   157	
   158	# ---------------------------------------------------------------------------
   159	# 5. Shell decomposition (9-shell H_3 partition)
   160	# ---------------------------------------------------------------------------
   161	
   162	def shell_indices(V, pole_idx):
   163	    """
   164	    Group vertices by their inner product with V[pole_idx]. The 600-cell's
   165	    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
   166	    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
   167	    """
   168	    pole = V[pole_idx]
   169	    inner = V @ pole
   170	    # The 9 canonical inner-product values:
   171	    canonical = np.array([
   172	        1.0,                # shell 0: pole itself
   173	        PHI / 2.0,          # shell 1
   174	        0.5,                # shell 2
   175	        1.0 / (2.0 * PHI),  # shell 3
   176	        0.0,                # shell 4 (equator)
   177	        -1.0 / (2.0 * PHI), # shell 5
   178	        -0.5,               # shell 6
   179	        -PHI / 2.0,         # shell 7
   180	        -1.0,               # shell 8: antipode
   181	    ])
   182	    shells = {k: [] for k in range(9)}
   183	    for i, val in enumerate(inner):
   184	        # snap to nearest canonical
   185	        k = int(np.argmin(np.abs(canonical - val)))
   186	        shells[k].append(i)
   187	    sizes = {k: len(shells[k]) for k in shells}
   188	    return shells, sizes, canonical
   189	
   190	
   191	# ---------------------------------------------------------------------------
   192	# 6. Discrete <-> continuum agreement test
   193	# ---------------------------------------------------------------------------
   194	
   195	def discrete_continuum_test(V, C_phi, source_idx):
   196	    """
   197	    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
   198	    shell radial coordinate x is the chord distance |v - v_source|. The
   199	    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).
   200	
   201	    Returns the per-shell discrete mean, the continuum prediction at each
   202	    shell radius, and the Pearson correlation between them.
   203	    """
   204	    psi = green_response(C_phi, source_idx)
   205	    shells, sizes, _ = shell_indices(V, source_idx)
   206	    pole = V[source_idx]
   207	
   208	    shell_means = []
   209	    shell_radii = []
   210	    shell_count = []
   211	    for k in range(9):
   212	        idxs = shells[k]
   213	        if not idxs:
   214	            continue
   215	        mean_psi = float(np.mean(psi[idxs]))
   216	        # mean chord radius from pole
   217	        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
   218	        shell_means.append(mean_psi)
   219	        shell_radii.append(chord)
   220	        shell_count.append(len(idxs))
   221	
   222	    shell_means = np.array(shell_means)
   223	    shell_radii = np.array(shell_radii)
   224	    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)
   225	
   226	    # Pearson correlation of (discrete shell mean) with (continuum prediction)
   227	    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
   228	        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
   229	    else:
   230	        corr = float("nan")
   231	
   232	    return {
   233	        "shell_radii": shell_radii.tolist(),
   234	        "shell_count": shell_count,
   235	        "shell_psi_mean": shell_means.tolist(),
   236	        "continuum_prediction": continuum.tolist(),
   237	        "pearson_correlation": corr,
   238	    }
   239	
   240	
   241	# ---------------------------------------------------------------------------
   242	# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
   243	# ---------------------------------------------------------------------------
   244	
   245	def cocycle_weights(V, source_idx):
   246	    """
   247	    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
   248	    the shell index of v with respect to a chosen pole. For the variant
   249	    test we compare the unweighted graph Laplacian to two weighted variants
   250	    discussed in the b-anomaly paper.
   251	    """
   252	    shells, _, _ = shell_indices(V, source_idx)
   253	    kappa = np.zeros(V.shape[0])
   254	    for k, idxs in shells.items():
   255	        for i in idxs:
   256	            kappa[i] = float(k)
   257	    return PHI ** kappa
   258	
   259	
   260	def weighted_laplacian(A, weights, mode="geometric"):
   261	    """
   262	    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
   263	    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
   264	    """
   265	    n = A.shape[0]
   266	    if mode == "geometric":
   267	        W = np.sqrt(np.outer(weights, weights))
   268	    elif mode == "arithmetic":
   269	        W = 0.5 * (weights[:, None] + weights[None, :])
   270	    else:
   271	        raise ValueError(mode)
   272	    A_w = A * W
   273	    D_w = np.diag(A_w.sum(axis=1))
   274	    return D_w - A_w
   275	
   276	
   277	def variant_correlation(V, A, source_idx, variant):
   278	    if variant == "UNWEIGHTED":
   279	        L_v = np.diag(A.sum(axis=1)) - A
   280	    else:
   281	        weights = cocycle_weights(V, source_idx)
   282	        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
   283	        L_v = weighted_laplacian(A, weights, mode=mode)
   284	    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
   285	    test = discrete_continuum_test(V, C_v, source_idx)
   286	    psi = green_response(C_v, source_idx)
   287	    pole = V[source_idx]
   288	    chord = np.linalg.norm(V - pole, axis=1)
   289	    # Continuum kernel at each vertex's chord radius
   290	    cont = (PHI / 2.0) * np.exp(-chord / PHI)
   291	    # Per-vertex correlation (excluding the source itself, which is degenerate)
   292	    mask = np.arange(V.shape[0]) != source_idx
   293	    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
   294	        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   295	    else:
   296	        per_vertex_corr = float("nan")
   297	    return {
   298	        "shell_mean_correlation": test["pearson_correlation"],
   299	        "per_vertex_correlation": per_vertex_corr,
   300	        "test": test,
   301	    }
   302	
   303	
   304	# ---------------------------------------------------------------------------
   305	# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
   306	# ---------------------------------------------------------------------------
   307	
   308	def operator_norm_check(L, w):
   309	    lam_min_L = float(w[0])           # 0
   310	    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
   311	    op_norm = 1.0 / lam_min_C         # phi^2
   312	    return {
   313	        "lambda_min_L": lam_min_L,
   314	        "lambda_min_C_phi": lam_min_C,
   315	        "operator_norm_C_phi_inv": op_norm,
   316	        "predicted_phi_squared": PHI ** 2,
   317	    }
   318	
   319	
   320	# ---------------------------------------------------------------------------
   321	# 9. Run everything and write results.json
   322	# ---------------------------------------------------------------------------
   323	
   324	def main():
   325	    out_path = Path(__file__).parent / "results.json"
   326	
   327	    V = build_v600()
   328	    n = V.shape[0]
   329	    A = build_short_edge_graph(V)
   330	    deg = A.sum(axis=1)
   331	    n_edges = int(A.sum() // 2)
   332	
   333	    L, w, U = laplacian_spectrum(A)
   334	    spectrum = round_spectrum(w, decimals=4)
   335	
   336	    C_phi = build_C_phi(L)
   337	    op_norm = operator_norm_check(L, w)
   338	
   339	    # Pick the +x_0 axis vertex as canonical pole/source.
   340	    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
   341	    pole = V[pole_idx]
   342	
   343	    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)
   344	
   345	    test = discrete_continuum_test(V, C_phi, pole_idx)
   346	
   347	    # Variant comparison on the same source
   348	    variants = {}
   349	    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   350	        out = variant_correlation(V, A, pole_idx, variant)
   351	        variants[variant] = {
   352	            "shell_mean_correlation": out["shell_mean_correlation"],
   353	            "per_vertex_correlation": out["per_vertex_correlation"],
   354	        }
   355	
   356	    result = {
   357	        "phi": PHI,
   358	        "phi_inv_sq": INV_PHI2,
   359	        "n_vertices": n,
   360	        "n_edges": n_edges,
   361	        "degree_sequence": {
   362	            "min": int(deg.min()),
   363	            "max": int(deg.max()),
   364	            "mean": float(deg.mean()),
   365	        },
   366	        "shell_sizes": shell_sizes,
   367	        "shell_inner_products": canonical_inner.tolist(),
   368	        "antipodal_check": {
   369	            "pole_idx": pole_idx,
   370	            "antipode_idx": int(np.argmin(V @ pole)),
   371	            "expected_shell_8_size": 1,
   372	            "observed_shell_8_size": shell_sizes.get(8, 0),
   373	        },
   374	        "laplacian_spectrum_grouped": [
   375	            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
   376	        ],
   377	        "operator_norm": op_norm,
   378	        "discrete_continuum_test": test,
   379	        "variant_correlation": variants,
   380	    }
   381	
   382	    with open(out_path, "w") as f:
   383	        json.dump(result, f, indent=2)
   384	
   385	    # Headline summary
   386	    print("=" * 60)
   387	    print("ARIA Closure Kernel — verification")
   388	    print("=" * 60)
   389	    print(f"|V|           = {n}  (expected 120)")
   390	    print(f"|E|           = {n_edges}  (expected 720)")
   391	    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
   392	    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
   393	    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
   394	    print()
   395	    print("Laplacian spectrum (eigenvalue, multiplicity):")
   396	    for ev, m in spectrum:
   397	        print(f"  {ev:>8.4f}   x {m}")
   398	    print()
   399	    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
   400	    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
   401	    print()
   402	    print("Discrete <-> continuum agreement (Pearson correlation):")
   403	    print(f"  variant         | shell-mean  | per-vertex")
   404	    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   405	        sm = variants[v]["shell_mean_correlation"]
   406	        pv = variants[v]["per_vertex_correlation"]
   407	        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
   408	    print()
   409	    print(f"Wrote {out_path}")
   410	
   411	
   412	if __name__ == "__main__":
   413	    main()

 succeeded in 295ms:
     1	# vfd-b-anomaly
     2	
     3	**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**
     4	
     5	[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
     6	[![Paper](https://img.shields.io/badge/paper-PDF-blue)](paper/main.pdf)
     7	
     8	This repository accompanies the preprint **[paper/main.pdf](paper/main.pdf)**. It contains all source code, processed data, intermediate result tables, and figures needed to reproduce every number in the paper from a clean checkout.
     9	
    10	---
    11	
    12	## Headline result
    13	
    14	A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.
    15	
    16	| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
    17	|---|---|---:|---:|---:|---:|
    18	| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
    19	| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
    20	| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
    21	| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
    22	| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |
    23	
    24	**What the data shows:**
    25	- **Universality.** The same fixed kernel describes all five datasets with one amplitude each — no shape retuning across datasets, channels, or isospin partners.
    26	- **Sign uniformity.** $A>0$ in **5/5** fits; $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel reproduces the established direction of the anomaly across all five independent measurements.
    27	- **Cross-channel ratio.** The $B\to K^{*}$ vs $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with the predicted Krüger–Matias $P$-basis vs $S$-basis amplification ($\sim 2.2$), with a residual $\sim 50\%$ overshoot.
    28	- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
    29	
    30	**Statistical caveat (what the paper does not claim):**
    31	- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
    32	- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
    33	- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
    34	
    35	The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.
    36	
    37	---
    38	
    39	## Figures from the paper
    40	
    41	| | |
    42	|---|---|
    43	| ![kernel shape](paper/figures/fig_F1_kernel_shape.png) | ![bin pulls](paper/figures/fig_F2_bin_pulls.png) |
    44	| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
    45	
    46	![cross-dataset](paper/figures/fig_F3_cross_dataset_A.png)
    47	
    48	**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.
    49	
    50	---
    51	
    52	## Repository contents
    53	
    54	```
    55	vfd-b-anomaly/
    56	├── README.md                      # this file
    57	├── LICENSE                        # MIT
    58	├── CITATION.cff                   # citation metadata
    59	├── CHANGELOG.md                   # findings history (linearisation drift, etc.)
    60	├── pyproject.toml                 # Python package definition
    61	├── .gitignore
    62	│
    63	├── paper/                         # the preprint
    64	│   ├── main.pdf                   # camera-ready PDF
    65	│   ├── main.tex                   # LaTeX source
    66	│   ├── sections/                  # 10 section files
    67	│   ├── figures/                   # F1, F2, F3 (PDF + PNG)
    68	│   ├── references.bib
    69	│   └── README.md                  # how to recompile
    70	│
    71	├── src/vfd_b_anomaly/             # core library (importable as `vfd_b_anomaly`)
    72	│   ├── flavio_predictor.py        # cached flavio.sm_prediction / np_prediction wrapper
    73	│   ├── hepdata_ingest.py          # HEPData JSON loader
    74	│   ├── wo009_full_lift.py         # 600-cell V_600 graph and discrete Green's response
    75	│   ├── wo010_universality.py      # frozen kernel evaluated at bin centres
    76	│   ├── wo014_cross_dataset.py     # cross-dataset dataset loaders + linearised fit
    77	│   ├── wo015_cross_channel.py     # Bs->phi cross-channel loader + linearised fit
    78	│   └── ...                        # see src/ for the full list
    79	│
    80	├── scripts/                       # paper-headline drivers
    81	│   ├── wo016a_akaike_stack.py     # Akaike weight stacking across 5 fits
    82	│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
    83	│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
    84	│   ├── wo016d_nonlinear_xdataset.py  # non-linear refit across all 5 datasets
    85	│   └── wo017_paper_figures.py     # F1, F2, F3 generation
    86	│
    87	├── reports/                       # paper-headline outputs (regenerated by run_all.sh)
    88	│   ├── wo009_full_lift.{json,csv,md}  # 600-cell graph spectral data
    89	│   ├── wo016a_akaike_stack.md         # paper §6 Akaike-weight stack
    90	│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
    91	│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
    92	│   └── wo016d_nonlinear_xdataset.md   # paper §6 non-linear cross-dataset table
    93	│
    94	├── data/
    95	│   ├── raw/                       # cached HEPData submissions (CC BY 4.0)
    96	│   └── processed/                 # flavio_cache.json (regeneratable)
    97	│
    98	├── tests/                         # pytest suite
    99	├── repro/                         # reproduction driver
   100	│   └── run_all.sh
   101	└── archive/                       # superseded scripts and reports cited as
   102	                                   # supporting evidence in §5; not on the
   103	                                   # path of run_all.sh
   104	```
   105	
   106	---
   107	
   108	## Reproduce in 5 steps (clean checkout)
   109	
   110	### 1. Install the package
   111	
   112	```bash
   113	git clone https://github.com/vfd-org/b-anomaly-reproduction.git vfd-b-anomaly
   114	cd vfd-b-anomaly
   115	pip install -e ".[dev,plotting]"
   116	```
   117	
   118	This pulls in `flavio` (2.4), `wilson` (2.5), `numpy`, `scipy`, `matplotlib`, `pytest`. flavio brings the BSZ form-factor parameterisation as a transitive dependency.
   119	
   120	### 2. Cache the HEPData archives
   121	
   122	The five datasets in the paper draw from five HEPData records. The first four are bundled in `data/raw/hepdata*/` (modest size, CC BY 4.0). For LHCb 2025 (the largest), download with:
   123	
   124	```bash
   125	mkdir -p data/raw/hepdata
   126	curl -L "https://www.hepdata.net/download/submission/ins3094698/original" \
   127	     -o data/raw/hepdata/HEPData-ins3094698-v1.zip
   128	python -c "import zipfile; zipfile.ZipFile('data/raw/hepdata/HEPData-ins3094698-v1.zip').extractall('data/raw/hepdata/extracted')"
   129	```
   130	
   131	### 3. Run all paper-headline experiments
   132	
   133	```bash
   134	bash repro/run_all.sh
   135	```
   136	
   137	This runs (in order):
   138	1. The non-linear LHCb 2025 refit (`scripts/wo016c_nonlinear_refit.py`).
   139	2. The full five-dataset non-linear refit (`scripts/wo016d_nonlinear_xdataset.py`).
   140	3. The Akaike-weight stack (`scripts/wo016a_akaike_stack.py`).
   141	4. The pure-geometry variant test (`scripts/wo016b_variant_geometry.py`).
   142	5. Paper figures F1, F2, F3 (`scripts/wo017_paper_figures.py`).
   143	
   144	Total wall time: ~5 minutes on a laptop, dominated by the non-linear flavio calls. A persistent on-disk cache (`data/processed/flavio_cache.json`) ensures subsequent runs are near-instant.
   145	
   146	### 4. Recompile the paper (optional)
   147	
   148	The PDF at `paper/main.pdf` is shipped pre-built. To regenerate from source:
   149	
   150	```bash
   151	# install tectonic once (~50 MB, single static binary, no sudo needed)
   152	curl -L https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz | tar -xz -C ~/.local/bin/
   153	
   154	# compile
   155	~/.local/bin/tectonic -X compile paper/main.tex
   156	```
   157	
   158	See `paper/README.md` for compile alternatives (TeX Live, Overleaf).
   159	
   160	### 5. Run tests
   161	
   162	```bash
   163	pytest -q
   164	```
   165	
   166	---
   167	
   168	## Contents of the paper
   169	
   170	The 25-page preprint (`paper/main.pdf`) has 10 sections:
   171	
   172	| § | content |
   173	|---|---|
   174	| 1 | Introduction; scope and epistemic status |
   175	| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
   176	| 3 | Three-layer kernel construction: continuum $\varphi$-tuned Green's function → bounded Dirichlet eigenmode → discrete 2I-equivariant lift on $V_{600}$. Variant-selection table on pure-geometry vs LHCb-data criteria. |
   177	| 4 | Results on LHCb 2025: non-linear vs linearised, drift table, leave-one-observable-out |
   178	| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
   179	| 6 | Cross-dataset non-linear fit across five datasets; Akaike-weight stack; sign-uniformity test |
   180	| 7 | Cross-channel fit on $B_{s}\!\to\!\phi$; basis-effect explanation of the amplitude gap |
   181	| 8 | Discussion: why the linearisation breaks; three readings of sign uniformity |
   182	| 9 | Limitations (linearisation issue is the lead) |
   183	| 10 | Conclusion; falsification programme; reproducibility |
   184	
   185	The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
   186	
   187	---
   188	
   189	## License and data attribution
   190	
   191	- **Project code** (everything under `src/`, `scripts/`, `tests/`, `repro/`, `paper/`): MIT licence — see [`LICENSE`](LICENSE).
   192	- **Cached HEPData supplementary archives** under `data/raw/`: © CERN for the benefit of the LHCb and CMS collaborations, distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The canonical citation for each archive is the corresponding HEPData record:
   193	  - LHCb 2025: [HEPData ins3094698](https://www.hepdata.net/record/ins3094698) (DOI [10.17182/hepdata.167733.v1](https://doi.org/10.17182/hepdata.167733.v1))
   194	  - LHCb 2015 $K^{*}$: [HEPData ins1409497](https://www.hepdata.net/record/ins1409497)
   195	  - LHCb 2021 $B^{+}\!\to\!K^{*+}$: [HEPData ins1838196](https://www.hepdata.net/record/ins1838196)
   196	  - CMS 2025: [HEPData ins2850101](https://www.hepdata.net/record/ins2850101)
   197	  - LHCb 2015 $B_{s}\!\to\!\phi$: [HEPData ins1380188](https://www.hepdata.net/record/ins1380188)
   198	- **flavio** ([arXiv:1810.08132](https://arxiv.org/abs/1810.08132)) and **wilson** ([arXiv:1804.05033](https://arxiv.org/abs/1804.05033)) provide the SM and non-linear new-physics predictions used as the headline backend; their licences are upstream.
   199	
   200	## Citation
   201	
   202	If you use this software or the accompanying paper, see [`CITATION.cff`](CITATION.cff). Suggested BibTeX:
   203	
   204	```bibtex
   205	@misc{Smart2026vfdBAnomaly,
   206	  author       = {Smart, Lee},
   207	  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
   208	  year         = {2026},
   209	  url          = {https://github.com/vfd-org/b-anomaly-reproduction/blob/main/paper/main.pdf},
   210	  note         = {Preprint, Institute of Vibrational Field Dynamics}
   211	}
   212	```
   213	
   214	For the LHCb 2025 dataset the project rests on, also cite:
   215	
   216	```bibtex
   217	@article{LHCb:2025BKstmumuComp,
   218	  author       = {{LHCb Collaboration}},
   219	  title        = {A comprehensive analysis of the $B^0\to K^{*0}\mu^+\mu^-$ decay},
   220	  eprint       = {2512.18053},
   221	  archivePrefix= {arXiv},
   222	  primaryClass = {hep-ex},
   223	  year         = {2025},
   224	  reportNumber = {LHCb-PAPER-2025-041, CERN-EP-2025-278},
   225	  doi          = {10.17182/hepdata.167733.v1}
   226	}
   227	```

exec
/bin/bash -lc 'wc -l papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "18/18|17/18|P4|0.190|six|6/6|Sleep-EDFx|2.252|0.463|1.83|0.066|0.33|93.8|53.1|87.5|-4.4|1003|11.58|79.78|6.80|eta|bounded_topk|seed|2026-04-18|preregister" papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"600-cell|unique|selection|consciousness|substrate witness|substrate-witness|not claim|ACT|Lyapunov|retun|C_\\\\varphi|C_\\{\\\\varphi\\}|varphi\\"'^-2|'"\\"'$'"\\\\eta\" papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 360ms:
rg: regex parse error:
    (?:600-cell|unique|selection|consciousness|substrate witness|substrate-witness|not claim|ACT|Lyapunov|retun|C_\varphi|C_\{\varphi\}|varphi\^-2|$\eta)
                                                                                                                                                    ^^
error: unrecognized escape sequence

 succeeded in 458ms:
   212 papers/aria-chess-paper/paper/main.tex
   170 papers/aria-chess-paper/paper/sections/01_introduction.tex
   201 papers/aria-chess-paper/paper/sections/02_method.tex
   173 papers/aria-chess-paper/paper/sections/03_substrate.tex
   197 papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex
   208 papers/aria-chess-paper/paper/sections/05_results.tex
   168 papers/aria-chess-paper/paper/sections/06_stress_tests.tex
   273 papers/aria-chess-paper/paper/sections/07_cross_domain.tex
   207 papers/aria-chess-paper/paper/sections/08_discussion.tex
   195 papers/aria-chess-paper/paper/sections/09_limitations.tex
    96 papers/aria-chess-paper/paper/sections/10_conclusion.tex
  2100 total

 succeeded in 447ms:
papers/aria-chess-paper/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-chess-paper/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
papers/aria-chess-paper/paper/main.tex:49:quantitative correspondences with neuroscience data — preregistered
papers/aria-chess-paper/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
papers/aria-chess-paper/paper/main.tex:53:trajectory at seed~$42$. No shape parameter is tuned to any neural
papers/aria-chess-paper/paper/main.tex:57:coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
papers/aria-chess-paper/paper/main.tex:64:neural dataset, is consistent with eighteen preregistered correspondences
papers/aria-chess-paper/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
papers/aria-chess-paper/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
papers/aria-chess-paper/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:85:additionally report six drug/sleep EEG signatures tested on a recurrent
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:99:This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:118:ablation model, and the original preregistered C$\times$P synergy
papers/aria-chess-paper/paper/main.tex:120:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
papers/aria-chess-paper/paper/main.tex:121:bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:133:leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
papers/aria-chess-paper/paper/main.tex:134:$\to$ substrate-routed $93.8\%$, with state reset; the
papers/aria-chess-paper/paper/main.tex:135:preregistered estimator P13 was $5$-fold CV with threshold
papers/aria-chess-paper/paper/main.tex:138:classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
papers/aria-chess-paper/paper/main.tex:143:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
papers/aria-chess-paper/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
papers/aria-chess-paper/paper/main.tex:160:is reported on a single deterministic trajectory; cross-seed CIs on
papers/aria-chess-paper/paper/main.tex:164:is consistent with eighteen preregistered neuroscience
papers/aria-chess-paper/paper/main.tex:165:correspondences and six drug/sleep EEG signatures, with all gaps in
papers/aria-chess-paper/paper/main.tex:167:without modifying any preregistered threshold.}
papers/aria-chess-paper/paper/main.tex:184:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
papers/aria-chess-paper/paper/main.tex:199:The complete pipeline (substrate construction, six-signature
papers/aria-chess-paper/paper/main.tex:201:preregistered validation, figure regeneration, this paper) is reproducible
papers/aria-chess-paper/paper/main.tex:204:deterministic given seeds; the substrate's spectral decomposition is
papers/aria-chess-paper/paper/main.tex:206:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
papers/aria-chess-paper/paper/sections/08_discussion.tex:24:  Sleep-EDFx within preregistered tolerance with pairwise CI overlap
papers/aria-chess-paper/paper/sections/08_discussion.tex:25:  on three reference ranges; six drug/sleep signatures pass at
papers/aria-chess-paper/paper/sections/08_discussion.tex:28:  against this many preregistered cortical correspondences from a
papers/aria-chess-paper/paper/sections/08_discussion.tex:34:  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
papers/aria-chess-paper/paper/sections/08_discussion.tex:38:  original 3-seed validation.
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:40:  threshold modification.} Every prediction in the preregistered set
papers/aria-chess-paper/paper/sections/08_discussion.tex:41:  passes at the preregistered thresholds. The two interaction tests
papers/aria-chess-paper/paper/sections/08_discussion.tex:42:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
papers/aria-chess-paper/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
papers/aria-chess-paper/paper/sections/08_discussion.tex:71:The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
papers/aria-chess-paper/paper/sections/08_discussion.tex:74:Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
papers/aria-chess-paper/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:143:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
papers/aria-chess-paper/paper/sections/08_discussion.tex:153:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
papers/aria-chess-paper/paper/sections/08_discussion.tex:154:  reliable detection at the preregistered threshold. The general
papers/aria-chess-paper/paper/sections/08_discussion.tex:155:  rule we draw — when preregistering an interaction effect on a
papers/aria-chess-paper/paper/sections/08_discussion.tex:156:  system with unknown per-seed variance, budget for at least this
papers/aria-chess-paper/paper/sections/08_discussion.tex:158:  taken as universal. The original 3-seed plan was the source of two
papers/aria-chess-paper/paper/sections/08_discussion.tex:166:  an explicit reset/equilibration discipline}, not just seed.
papers/aria-chess-paper/paper/sections/08_discussion.tex:191:\item Do the six drug/sleep signatures replicate across $10$--$20$
papers/aria-chess-paper/paper/sections/08_discussion.tex:192:  cross-seed runs of the recurrent layer? (Single-seed disclosure;
papers/aria-chess-paper/paper/sections/08_discussion.tex:198:  independent fresh-seed $N\!=\!20$ replication at a different seed
papers/aria-chess-paper/paper/sections/08_discussion.tex:203:\item Does the Sleep-EDFx three-way CI overlap survive on a different
papers/aria-chess-paper/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
papers/aria-chess-paper/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
papers/aria-chess-paper/paper/sections/10_conclusion.tex:15:$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
papers/aria-chess-paper/paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
papers/aria-chess-paper/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:25:propofol continuity drop $+0.066$; propofol integrated-information
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:30:overlaps the real Sleep-EDFx EEG
papers/aria-chess-paper/paper/sections/10_conclusion.tex:35:\textbf{Eighteen preregistered correspondences.} All eighteen pass at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
papers/aria-chess-paper/paper/sections/10_conclusion.tex:40:preregistered threshold has been modified. The original 2026-04-20
papers/aria-chess-paper/paper/sections/10_conclusion.tex:42:failure; the closure of the three gaps (P3, P4, P13) is documented
papers/aria-chess-paper/paper/sections/10_conclusion.tex:49:strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:52:the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
papers/aria-chess-paper/paper/sections/10_conclusion.tex:54:high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
papers/aria-chess-paper/paper/sections/10_conclusion.tex:62:canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
papers/aria-chess-paper/paper/sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
papers/aria-chess-paper/paper/sections/10_conclusion.tex:66:conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
papers/aria-chess-paper/paper/sections/10_conclusion.tex:69:on the full-cohort descriptive HCP $n\!=\!1003$ statistics
papers/aria-chess-paper/paper/sections/10_conclusion.tex:70:(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
papers/aria-chess-paper/paper/sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
papers/aria-chess-paper/paper/sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
papers/aria-chess-paper/paper/sections/10_conclusion.tex:80:strengthening builds — cross-seed CIs on the recurrent-layer
papers/aria-chess-paper/paper/sections/10_conclusion.tex:82:C$\times$P replication at a different seed range, cross-parcellation
papers/aria-chess-paper/paper/sections/10_conclusion.tex:88:tested against this many preregistered cortical correspondences from
papers/aria-chess-paper/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-chess-paper/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
papers/aria-chess-paper/paper/sections/09_limitations.tex:22:$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
papers/aria-chess-paper/paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
papers/aria-chess-paper/paper/sections/09_limitations.tex:26:\textbf{Single-seed determinism on the recurrent layer.} The v4
papers/aria-chess-paper/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
papers/aria-chess-paper/paper/sections/09_limitations.tex:28:a single deterministic trajectory at seed $42$. Empirical CIs across
papers/aria-chess-paper/paper/sections/09_limitations.tex:29:$10$--$20$ cross-seed runs would strengthen the per-signature claims
papers/aria-chess-paper/paper/sections/09_limitations.tex:31:WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
papers/aria-chess-paper/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
papers/aria-chess-paper/paper/sections/09_limitations.tex:35:\emph{Strengthening build:} 10--20 cross-seed runs of
papers/aria-chess-paper/paper/sections/09_limitations.tex:59:observables.} While the construction of $\Rsixhundred$ is theorem-
papers/aria-chess-paper/paper/sections/09_limitations.tex:65:preregistered correspondences plus six signatures; the H$_4$
papers/aria-chess-paper/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-chess-paper/paper/sections/09_limitations.tex:95:\textbf{The recurrent layer is a method, not a metaphysics claim.}
papers/aria-chess-paper/paper/sections/09_limitations.tex:97:we claim quantitative consistency with six published biological
papers/aria-chess-paper/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
papers/aria-chess-paper/paper/sections/09_limitations.tex:121:\textbf{Two preregistered interaction tests required higher $N$
papers/aria-chess-paper/paper/sections/09_limitations.tex:122:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
papers/aria-chess-paper/paper/sections/09_limitations.tex:124:underpowered interaction estimates on high-per-seed-variance terms,
papers/aria-chess-paper/paper/sections/09_limitations.tex:127:\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
papers/aria-chess-paper/paper/sections/09_limitations.tex:129:$19/20$ seeds positive. \emph{Strengthening build:} a second
papers/aria-chess-paper/paper/sections/09_limitations.tex:130:$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
papers/aria-chess-paper/paper/sections/09_limitations.tex:131:an $N\!=\!50$ characterisation of the per-seed distribution.
papers/aria-chess-paper/paper/sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
papers/aria-chess-paper/paper/sections/09_limitations.tex:141:builds for P3/P4/P13 above; no further claim is needed.
papers/aria-chess-paper/paper/sections/09_limitations.tex:153:\textbf{Single condition-dependent parameter $\eta$ is not derived
papers/aria-chess-paper/paper/sections/09_limitations.tex:154:as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
papers/aria-chess-paper/paper/sections/09_limitations.tex:157:extension where $\eta$ adapts on an error norm is an open build.
papers/aria-chess-paper/paper/sections/09_limitations.tex:172:\item Selection theorem for $\Rsixhundred$ over alternative regular
papers/aria-chess-paper/paper/sections/09_limitations.tex:175:  of the six signatures.
papers/aria-chess-paper/paper/sections/09_limitations.tex:179:\item Verification of P10 (chess null mapping) at the preregistered
papers/aria-chess-paper/paper/sections/09_limitations.tex:189:eighteen preregistered correspondences and six companion drug/sleep
papers/aria-chess-paper/paper/sections/09_limitations.tex:191:refinement and without modifying any preregistered threshold. We do
papers/aria-chess-paper/paper/sections/09_limitations.tex:194:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
papers/aria-chess-paper/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
papers/aria-chess-paper/paper/sections/02_method.tex:13:\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
papers/aria-chess-paper/paper/sections/02_method.tex:14:(P1--P18) were locked on 2026-04-18 in
papers/aria-chess-paper/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
papers/aria-chess-paper/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
papers/aria-chess-paper/paper/sections/02_method.tex:37:2026-04-20 validation reported failures (P3, P4, P13), the documented
papers/aria-chess-paper/paper/sections/02_method.tex:41:(P4, C$\times$P), and
papers/aria-chess-paper/paper/sections/02_method.tex:44:preregistered threshold.
papers/aria-chess-paper/paper/sections/02_method.tex:49:\to (\text{script}, \text{seed range}, \text{dataset/source},
papers/aria-chess-paper/paper/sections/02_method.tex:61:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:65:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:66:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:67:P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:68:P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:72:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
papers/aria-chess-paper/paper/sections/02_method.tex:87:\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
papers/aria-chess-paper/paper/sections/02_method.tex:111:matrix. The preregistered test (P18) was on $n=100$ subjects for
papers/aria-chess-paper/paper/sections/02_method.tex:112:computational tractability; full-cohort $n=1003$ statistics
papers/aria-chess-paper/paper/sections/02_method.tex:115:preregistered test.
papers/aria-chess-paper/paper/sections/02_method.tex:140:preregistered cascade-$\alpha$ tests, 2000 resamples for the
papers/aria-chess-paper/paper/sections/02_method.tex:141:$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
papers/aria-chess-paper/paper/sections/02_method.tex:142:preregistered; 42 for the deep-dive.
papers/aria-chess-paper/paper/sections/02_method.tex:146:$0/2000$ were below the preregistered floor $+0.10$; we report these
papers/aria-chess-paper/paper/sections/02_method.tex:161:on the full $n=1003$ subject distribution.
papers/aria-chess-paper/paper/sections/02_method.tex:175:preregistered floor). The reset protocol is documented in
papers/aria-chess-paper/paper/sections/02_method.tex:190:\item Eighteen preregistered:
papers/aria-chess-paper/paper/sections/02_method.tex:191:  \texttt{python3 run\_preregistered\_validation.py}
papers/aria-chess-paper/paper/sections/02_method.tex:197:All scripts are deterministic given seeds. Reruns at seed $42$ on the
papers/aria-chess-paper/paper/sections/01_introduction.tex:12:has yielded the kind of preregistered multi-domain quantitative
papers/aria-chess-paper/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
papers/aria-chess-paper/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
papers/aria-chess-paper/paper/sections/01_introduction.tex:28:single condition-dependent self-injection coupling $\eta$ and a
papers/aria-chess-paper/paper/sections/01_introduction.tex:30:against eighteen preregistered correspondences plus six companion
papers/aria-chess-paper/paper/sections/01_introduction.tex:37:consistent with eighteen preregistered correspondences (frozen
papers/aria-chess-paper/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
papers/aria-chess-paper/paper/sections/01_introduction.tex:42:\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:55:  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
papers/aria-chess-paper/paper/sections/01_introduction.tex:59:  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:65:\item \textbf{Eighteen preregistered correspondences pass.}
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:68:  test; \emph{no preregistered threshold has been modified}.
papers/aria-chess-paper/paper/sections/01_introduction.tex:72:  conversation $-4.4$pp lift, within preregistered neutrality bounds)
papers/aria-chess-paper/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
papers/aria-chess-paper/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
papers/aria-chess-paper/paper/sections/01_introduction.tex:105:  that some such mechanisms appear in the substrate's preregistered
papers/aria-chess-paper/paper/sections/01_introduction.tex:128:A result that lands inside its preregistered threshold licenses a
papers/aria-chess-paper/paper/sections/01_introduction.tex:129:`consistent with' claim. A result that exceeds the preregistered
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:142:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
papers/aria-chess-paper/paper/sections/01_introduction.tex:144:parameter $\eta$ and one graph-pinned nonlinearity, against published
papers/aria-chess-paper/paper/sections/01_introduction.tex:156:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
papers/aria-chess-paper/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
papers/aria-chess-paper/paper/sections/01_introduction.tex:161:\S\ref{sec:results} reports the empirical tables: six drug/sleep
papers/aria-chess-paper/paper/sections/01_introduction.tex:162:signatures, eighteen preregistered correspondences, three-way
papers/aria-chess-paper/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
papers/aria-chess-paper/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:18:\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
papers/aria-chess-paper/paper/sections/05_results.tex:28:seed 42).}
papers/aria-chess-paper/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:46:\label{tab:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:76:on the same deterministic substrate trajectory. The six signatures
papers/aria-chess-paper/paper/sections/05_results.tex:77:are not part of the dated 2026-04-18 P1--P18 preregistration; their
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:87:load-bearing for the headline claim. Single-seed disclosure:
papers/aria-chess-paper/paper/sections/05_results.tex:90:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:96:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
papers/aria-chess-paper/paper/sections/05_results.tex:101:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:111:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:121:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:122:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:130:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
papers/aria-chess-paper/paper/sections/05_results.tex:134:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
papers/aria-chess-paper/paper/sections/05_results.tex:142:  $N\!=\!3$ on a high-per-seed-variance interaction term.
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:145:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:156:  the preregistered test}, not as preregistration revision.
papers/aria-chess-paper/paper/sections/05_results.tex:159:\textbf{Headline verdict.} Eighteen preregistered correspondences
papers/aria-chess-paper/paper/sections/05_results.tex:160:all pass at preregistered thresholds, with two interaction tests
papers/aria-chess-paper/paper/sections/05_results.tex:181:ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
papers/aria-chess-paper/paper/sections/05_results.tex:182:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
papers/aria-chess-paper/paper/sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
papers/aria-chess-paper/paper/sections/05_results.tex:190:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
papers/aria-chess-paper/paper/sections/05_results.tex:194:intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
papers/aria-chess-paper/paper/sections/05_results.tex:208:with event-bootstrap; cross-seed CI is an open build).
papers/aria-chess-paper/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
papers/aria-chess-paper/paper/sections/03_substrate.tex:118:$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
papers/aria-chess-paper/paper/sections/03_substrate.tex:155:cascade is a decomposition of operators on $\Rsixhundred$, and the
papers/aria-chess-paper/paper/sections/03_substrate.tex:156:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
papers/aria-chess-paper/paper/sections/03_substrate.tex:162:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
papers/aria-chess-paper/paper/sections/03_substrate.tex:168:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:29:\textbf{Critical methodological detail.} Between successive depth
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:45:$5$    & $53.1\%$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:47:$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:74:$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:77:and P16 (conversation null); both pass. The 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:84:range. Verification at the preregistered $20$-perm setting is an open
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:87:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:95:4-category classification from raw $53.1\%$ (just above $25\%$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:96:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:107:substrate retains $65.4\%$ classification accuracy under random
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:126:\caption{Conversation preregistered tests.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:132:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:133:P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:139:\textbf{Reading.} Conversation raw features at $87.5\%$ are already
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:141:lift is $-4.4$pp, well within the preregistered neutrality band
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:146:selective-amplifier behaviour preregistered in 2026-04-18: in these
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:149:are already saturated (conversation raw $87.5\%$). We do not claim
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:158:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:160:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:171:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:172:$n=1003$ descriptive statistics.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:178:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:198:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:258:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:11:coupling $\eta$, and four trajectory observables. No shape parameter
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:14:This section is method, not metaphysics. We do not claim the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:30:with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:39:\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:41:\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:108:drop $+0.066$).
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:125:$\times$ $800$ ticks each at seed $42$:
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:127:\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:131:that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:142:$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:164:ablation grid is the basis for the preregistered tests P1--P5 and
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:11:was walked back. Closing this gap without modifying the preregistered
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:15:confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:28:Per-seed paired estimates use the same formula on a single seed's
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:45:$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:53:($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:60:\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:61:$32000$--$32019$, non-overlapping with original validation seeds in
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:64:seed $42$. Wallclock $1706$\,s on a single CPU
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:72:\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:95:Bootstrap on the 20-seed sample (2000 resamples):
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:97:\item bootstrap mean $\Delta_{CP} = +0.190$;
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:105:\textbf{Per-seed paired distribution.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:106:$19/20$ seeds give a positive paired-interaction estimate (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:107:$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:112:\textbf{The 95\% CI is entirely above the preregistered $+0.10$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:115:were below the preregistered $+0.10$ floor, reported as $0.0000$.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:127:architectural claim from the original 3-seed validation that held $C$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:132:(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:133:selected to be non-overlapping with the original $30000$s seeds.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:135:(i) a second independent $N\!=\!20$ run at a different seed range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:137:(ii) an $N\!=\!50$ characterisation of the per-seed sample
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:146:\item It does not establish an $\eta$-trajectory derivation; $\eta$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:160:at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:161:The original 3-seed preregistered validation gave estimates consistent
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:164:preregistering an interaction effect on a system with unknown
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:165:per-seed variance, budget the seed count from a power-analysis
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:166:assumption that the per-seed std could be as large as the interaction

exec
/bin/bash -lc "python - <<'PY'
import importlib.util, numpy as np
p='papers/aria-closure-kernel/repro/verify_kernel.py'
spec=importlib.util.spec_from_file_location('vk', p)
vk=importlib.util.module_from_spec(spec); spec.loader.exec_module(vk)
V=vk.build_v600(); A=vk.build_short_edge_graph(V); L,w,U=vk.laplacian_spectrum(A); C=vk.build_C_phi(L)
pole_idx=int(np.argmax(V @ np.array([1.0,0,0,0])))
psi=vk.green_response(C,pole_idx); shells, sizes, _=vk.shell_indices(V,pole_idx)
for k in range(9):
    vals=psi[shells[k]]
    print(k, len(vals), float(vals.std()), float(vals.min()), float(vals.max()))
PY" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 565ms:
/bin/bash: cannot create temp file for here-document: Read-only file system

exec
/bin/bash -lc "python -c \"import importlib.util,numpy as np;p='papers/aria-closure-kernel/repro/verify_kernel.py';spec=importlib.util.spec_from_file_location('vk',p);vk=importlib.util.module_from_spec(spec);spec.loader.exec_module(vk);V=vk.build_v600();A=vk.build_short_edge_graph(V);L,w,U=vk.laplacian_spectrum(A);C=vk.build_C_phi(L);pole_idx=int(np.argmax(V @ np.array([1.0,0,0,0])));psi=vk.green_response(C,pole_idx);shells,sizes,_=vk.shell_indices(V,pole_idx);[print(k,len(psi[shells[k]]),float(psi[shells[k]].std()),float(psi[shells[k]].min()),float(psi[shells[k]].max())) for k in range(9)]\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 127 in 370ms:
/bin/bash: python: command not found

exec
/bin/bash -lc "python3 -c \"import importlib.util,numpy as np;p='papers/aria-closure-kernel/repro/verify_kernel.py';spec=importlib.util.spec_from_file_location('vk',p);vk=importlib.util.module_from_spec(spec);spec.loader.exec_module(vk);V=vk.build_v600();A=vk.build_short_edge_graph(V);L,w,U=vk.laplacian_spectrum(A);C=vk.build_C_phi(L);pole_idx=int(np.argmax(V @ np.array([1.0,0,0,0])));psi=vk.green_response(C,pole_idx);shells,sizes,_=vk.shell_indices(V,pole_idx);[print(k,len(psi[shells[k]]),float(psi[shells[k]].std()),float(psi[shells[k]].min()),float(psi[shells[k]].max())) for k in range(9)]\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 2242ms:
0 1 0.0 0.11466009151487011 0.11466009151487011
1 12 1.1152711579477387e-17 0.034976446331995675 0.034976446331995696
2 20 5.647850449853784e-18 0.024335208435661268 0.02433520843566129
3 12 5.753426884836168e-18 0.021858804323929074 0.021858804323929084
4 30 3.955778153302621e-18 0.019268782150762206 0.01926878215076222
5 12 5.5763557897386935e-18 0.017658572921343527 0.017658572921343547
6 20 4.17776736080521e-18 0.01690255285200188 0.016902552852001894
7 12 3.3217425607229918e-18 0.015932370381507646 0.015932370381507653
8 1 0.0 0.01544087945358437 0.01544087945358437

exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/main.tex | sed -n '70,170p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/05_results.tex | sed -n '16,90p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/05_results.tex | sed -n '90,210p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/07_cross_domain.tex | sed -n '20,115p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/07_cross_domain.tex | sed -n '120,225p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/09_limitations.tex | sed -n '1,195p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 326ms:
    70	sits as the $L_M$ instance; the selection of the 600-cell as the active
    71	$M$ is treated as conjectural and is not load-bearing here.
    72	
    73	\begin{abstract}
    74	We test whether a geometry-fixed substrate — the 600-cell regular
    75	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    76	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    77	operator — is consistent with cortical signatures across five
    78	neuroscience domains. Eighteen quantitative predictions were
    79	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    80	before any validation run; each has a falsifiable threshold. The
    81	preregistered tally is $17/18$ at standard validation methodology
    82	($5$-seed cascade block plus state-reset protocol), and $18/18$ after
    83	a documented $N\!=\!20$ deep-dive on the residual high-variance
    84	interaction (P4); no preregistered threshold has been modified. We
    85	additionally report six drug/sleep EEG signatures tested on a recurrent
    86	self-model layer above the substrate, on a single deterministic
    87	trajectory at seed~$42$. The six signatures are not part of the
    88	P1--P18 preregistration; they are tested against thresholds drawn
    89	from the published literature (Sleep-EDFx CI for the wake $\alpha$,
    90	OpenNeuro \texttt{ds005620} point-estimate window for propofol
    91	switching, literature-direction predictions for $\Phi$ collapse,
    92	continuity drop, and recovery; \S\ref{sec:method}). They were
    93	obtained under condition-specific v4 stimulus models redesigned to
    94	be biologically realistic (\S\ref{sec:chain}).
    95	
    96	\noindent\emph{(i) Cortical avalanches.}
    97	Wake cascade-event power-law exponent $\alpha = 2.252$,
    98	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    99	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
   100	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
   101	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
   102	overlap.
   103	
   104	\noindent\emph{(ii) Drug/sleep state transitions.}
   105	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   106	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   107	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   108	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   109	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   110	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   111	direction confirmed); recovery deterministically identical to wake.
   112	All six signatures pass against their literature-derived thresholds
   113	on the single deterministic substrate trajectory.
   114	
   115	\noindent\emph{(iii) Causal mechanism isolation.}
   116	Two of four cascade mechanisms — context rotation $C$ and partial
   117	emission $P$ — are causally identifiable within the factorial
   118	ablation model, and the original preregistered C$\times$P synergy
   119	prediction $\geq +0.10$ closes
   120	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   121	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   122	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   123	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   124	underestimate ($+0.044$) as consistent with an underpowered interaction
   125	estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
   126	future preregistrations on similar high-variance ablation matrices
   127	should budget for this scale.
   128	
   129	\noindent\emph{(iv) Cross-domain selectivity.}
   130	The substrate exhibits selective amplification in the two cross-domain
   131	tasks tested: chess 4-category position classification on
   132	8-dimensional V2 features lifts $+40.6$ percentage points on
   133	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   134	$\to$ substrate-routed $93.8\%$, with state reset; the
   135	preregistered estimator P13 was $5$-fold CV with threshold
   136	$\geq\!+15$pp, the LOO finding above is a disclosed estimator/protocol
   137	refinement at the same threshold), while conversation utterance
   138	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   139	(threshold $|\cdot| < 10$pp), consistent with the substrate
   140	amplifying in these two tasks where raw features are ambiguous and
   141	remaining approximately neutral when raw features are already
   142	discriminative. On HCP brain functional connectivity
   143	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   144	descriptive statistics), the H$_4$-transitive substrate is a
   145	deterministic null reference: ARIA degree std
   146	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   147	on degree homogeneity, $+79.78\sigma$ on raw participation ratio
   148	(with the node-count caveat documented at \S\ref{ssec:hcp}: ARIA
   149	$|V|\!=\!120$ vs HCP ICA-50 $|V|\!=\!50$; the $\sigma$ value reflects
   150	both architectural and node-count differences), and $+6.80\sigma$ on
   151	clustering coefficient (implicit HCP across-subject sd $\approx 0.035$
   152	inferred from the reported gap; see \S\ref{ssec:hcp}).
   153	
   154	\noindent\emph{What we do not claim.}
   155	We do not claim the 600-cell is the unique substrate consistent with
   156	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   157	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   158	first principles; it is a design-level stability clamp on the
   159	shifted-Laplacian response. The recurrent layer above the substrate
   160	is reported on a single deterministic trajectory; cross-seed CIs on
   161	the per-condition signatures are an explicit strengthening build.
   162	The structural scope of this paper is: \emph{a geometry-fixed
   163	substrate, with no shape parameters tuned to any neural dataset,
   164	is consistent with eighteen preregistered neuroscience
   165	correspondences and six drug/sleep EEG signatures, with all gaps in
   166	the original preregistration closed by methodology refinement and
   167	without modifying any preregistered threshold.}
   168	\end{abstract}
   169	
   170	% =====================================================================

 succeeded in 321ms:
    16	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
    17	
    18	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
    19	$k_{\mathrm{thr}}=12$, single deterministic substrate
    20	(\S\ref{sec:chain}). Per-condition trajectory observables are
    21	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
    22	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
    23	
    24	\begin{table}[ht]
    25	\centering
    26	\small
    27	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
    28	seed 42).}
    29	\label{tab:per_condition}
    30	\begin{tabular}{l r r l r r r r}
    31	\toprule
    32	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
    33	\midrule
    34	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    35	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
    36	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
    37	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    38	\bottomrule
    39	\end{tabular}
    40	\end{table}
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{Six drug/sleep signatures with literature references.}
    46	\label{tab:six_signatures}
    47	\begin{tabular}{c l l c c l}
    48	\toprule
    49	\# & Signature & Reference & Predicted & Observed & Verdict \\
    50	\midrule
    51	1 & NREM-N3 var ratio (vs Wake) &
    52	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
    53	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
    54	2 & Propofol switching ratio &
    55	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
    56	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
    57	3 & Propofol continuity drop &
    58	   EEG microstate~\citep{Brodbeck2012Microstates} &
    59	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
    60	4 & Propofol $\Phi$ collapse (IIT) &
    61	   Tononi 2008~\citep{Tononi2008} &
    62	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
    63	5 & Recovery reversibility &
    64	   clinical anaesthesia &
    65	   identical to wake & $0$ diff & $\checkmark$ \\
    66	6 & Wake cortical-avalanche $\alpha$ &
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass against their literature-derived thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; their
    78	thresholds are drawn from the literature (Sleep-EDFx CI for
    79	wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
    80	propofol switching, literature-direction predictions for $\Phi$
    81	collapse, continuity drop, and recovery). They were tested on a
    82	recurrent-layer architecture redesigned at v4 with
    83	biologically-motivated condition-specific stimulus models
    84	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    85	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    86	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    87	load-bearing for the headline claim. Single-seed disclosure:
    88	\S\ref{ssec:regime}.
    89	
    90	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}

 succeeded in 351ms:
    90	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    91	
    92	\textbf{Tally.} $17/18$ at standard validation
    93	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    94	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    95	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    96	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    97	
    98	\begin{table}[ht]
    99	\centering
   100	\small
   101	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
   102	\label{tab:eighteen_prereg}
   103	\begin{tabular}{l l l l l}
   104	\toprule
   105	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   106	\midrule
   107	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   108	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   109	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   110	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   111	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   112	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   113	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   114	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   115	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   116	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   117	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   118	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   119	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   120	\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   121	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   122	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   123	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   124	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   125	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   126	\bottomrule
   127	\end{tabular}
   128	\end{table}
   129	
   130	\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
   131	estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
   132	validation tightened the estimator to LOO with state reset, a
   133	disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
   134	\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
   135	
   136	\textbf{Three predictions that flipped to PASS, with documented
   137	methodology refinement (no threshold change).}
   138	\begin{itemize}\itemsep=2pt
   139	\item P3 (D$\times$C interaction independence) was outside the band
   140	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   141	  Reading: consistent with an underpowered interaction estimate at
   142	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   143	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   144	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   145	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   146	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   147	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   148	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   149	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   150	  validation strengthened the estimator to LOO with state reset, a
   151	  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
   152	  without state reset on a state-drifted substrate, and $+40.6$pp
   153	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   154	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   155	  report this as a \emph{validation-protocol refinement relative to
   156	  the preregistered test}, not as preregistration revision.
   157	\end{itemize}
   158	
   159	\textbf{Headline verdict.} Eighteen preregistered correspondences
   160	all pass at preregistered thresholds, with two interaction tests
   161	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   162	detection of high-variance interaction terms, and one test
   163	requiring the documented state-reset protocol. The original $15/18$
   164	result was a methodology-limited tally, not a content failure.
   165	
   166	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   167	
   168	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   169	\emph{three independent reference ranges} simultaneously:
   170	
   171	\begin{table}[ht]
   172	\centering
   173	\small
   174	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   175	law.}
   176	\label{tab:alpha_overlap}
   177	\begin{tabular}{l c l c}
   178	\toprule
   179	Source & $\alpha$ & 95\% CI & $n$ \\
   180	\midrule
   181	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   182	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   183	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   184	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   185	\bottomrule
   186	\end{tabular}
   187	\end{table}
   188	
   189	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   190	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   191	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   192	and lies inside the cortical-avalanche band
   193	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   194	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   195	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   196	independent reference ranges.
   197	
   198	\textbf{Reading.} The substrate produces self-organised-critical
   199	cascade statistics matching the cortical-avalanche literature with
   200	no fitted parameter on neural data. The bounded-top-$K$ at
   201	$k=12$ is pinned to the substrate's average degree
   202	(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
   203	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   204	biological time-scale parameters but is not measurement-fitted to
   205	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   206	power-law exponent is one of the main empirical anchors in the paper
   207	(noting that the v4 WAKE CI is from a single deterministic trajectory
   208	with event-bootstrap; cross-seed CI is an open build).

 succeeded in 337ms:
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
    75	prediction across both domains (``$\geq 50\%$ on chess and
    76	conversation''). We split it for table clarity into P10 (chess null)
    77	and P16 (conversation null); both pass. The 2026-04-18 preregistration
    78	specified $20$ random label permutations for the null-mapping bound;
    79	the 2026-04-29 validation run used $15$ permutations
    80	(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
    81	is unchanged). We report this as a disclosed-protocol deviation, not
    82	a threshold change; the observed $65.4\%$ at $15$ perms sits well
    83	above the $50\%$ floor and the result is robust to perm count in this
    84	range. Verification at the preregistered $20$-perm setting is an open
    85	build (\S\ref{sec:limitations}).
    86	
    87	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    88	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    89	The 2026-04-29 validation tightened the estimator to LOO with state
    90	reset; we report the LOO finding ($+40.6$pp) above as a disclosed
    91	estimator/protocol refinement at the unchanged $+15$pp threshold,
    92	not a preregistration revision.
    93	
    94	\textbf{Reading.} Substrate routing amplifies chess-position
    95	4-category classification from raw $53.1\%$ (just above $25\%$
    96	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    97	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    98	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    99	(P9), itself well above any reasonable raw-features baseline.
   100	The original 2026-04-20 validation reported the LOO lift at
   101	$+3.1$pp, a state-drift artefact closed by the reset protocol
   102	(\S\ref{sec:method}).
   103	
   104	\textbf{Permutation null decomposition.} The null permutation
   105	mapping (P10) randomises the feature$\to$frame assignment, so each
   106	feature is routed to a different $S^{7}$ frame than canonical. The
   107	substrate retains $65.4\%$ classification accuracy under random
   108	permutation — well above the $25\%$ chance level for $4$ categories.
   109	We read this as a substrate-witness decomposition:
   110	a $65.4$ percentage-point accuracy floor persists under the
   111	architecture-only permutation null (it survives random
   112	feature$\to$frame reassignment; the architecture is acting on whatever
   113	input lands in the frames), with the remaining $\sim 17$pp accruing
   114	to canonical alignment. We do not claim this decomposition is
   115	unique; it is a description of the observed accuracy stack.

 succeeded in 326ms:
   120	$8$-dimensional injection-row features per utterance. Identical
   121	substrate routing pipeline to chess.
   122	
   123	\begin{table}[ht]
   124	\centering
   125	\small
   126	\caption{Conversation preregistered tests.}
   127	\label{tab:conv_prereg}
   128	\begin{tabular}{l l l l l}
   129	\toprule
   130	ID & Test & Threshold & Observed & Verdict \\
   131	\midrule
   132	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   133	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   134	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   135	\bottomrule
   136	\end{tabular}
   137	\end{table}
   138	
   139	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   140	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   141	lift is $-4.4$pp, well within the preregistered neutrality band
   142	$|\cdot|\!<\!10$pp. The substrate is approximately neutral on conversation.
   143	
   144	\textbf{Selective amplifier signature.} The pair (chess
   145	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   146	selective-amplifier behaviour preregistered in 2026-04-18: in these
   147	two tasks, the architecture amplifies when raw features are ambiguous
   148	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   149	are already saturated (conversation raw $87.5\%$). We do not claim
   150	this generalises to all classification tasks; cross-domain transfer
   151	to additional ambiguous-feature benchmarks is an open build
   152	(\S\ref{sec:limitations}).
   153	
   154	\subsection{HCP brain-graph H$_4$-transitive null
   155	            (P17--P18)}\label{ssec:hcp}
   156	
   157	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   158	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   159	$n=100$ subjects for computational tractability, with full-cohort
   160	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   161	connectivity matrix; thresholded at the same density as ARIA's
   162	vertex graph ($\rho=0.101$). Compare degree distribution and
   163	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   164	$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
   165	has identical local structure $\Rightarrow$ uniform degree $12$
   166	$\Rightarrow$ degree std $= 0$ as a theorem.
   167	
   168	\begin{table}[ht]
   169	\centering
   170	\small
   171	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   172	$n=1003$ descriptive statistics.}
   173	\label{tab:hcp}
   174	\begin{tabular}{l r r r}
   175	\toprule
   176	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   177	\midrule
   178	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   179	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   180	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   181	Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   182	\bottomrule
   183	\end{tabular}
   184	\end{table}
   185	
   186	\noindent$^{\flat}$ The HCP across-subject standard deviation for the
   187	clustering coefficient is not separately reported in
   188	\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
   189	from the same descriptive analysis as the other rows. Inferred from
   190	the reported gap and $\sigma$, the implicit HCP sd is
   191	$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
   192	forward as reported and flag the missing explicit sd here.
   193	
   194	\begin{itemize}\itemsep=2pt
   195	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   196	  $0.0000$, $\checkmark$.
   197	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   198	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   199	  HCP subjects have degree std below $2.0$.
   200	\end{itemize}
   201	
   202	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   203	structure is a deterministic group-theoretic null reference for
   204	cortical functional connectivity. Real cortex breaks the symmetry
   205	through hub-spoke functional specialisation; the $\sigma$-distances
   206	quantify the magnitude of biological symmetry-breaking with no
   207	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   208	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   209	clustering coefficient) are large on the ICA-50 pipeline at the
   210	density-matched threshold $\rho = 0.101$; cross-parcellation
   211	replication (Schaefer, Glasser) remains an open build.
   212	
   213	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   214	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   215	participation-ratio statistic
   216	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   217	node-count-dependent — its theoretical maximum is the node count of
   218	the graph. We report the raw $\mathrm{PR}$ values
   219	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   220	50-node graph) and the $\sigma$-distance against the HCP
   221	across-subject distribution, but the $+79.78\sigma$ value reflects
   222	both the architectural difference and the differing node counts. A
   223	node-count-normalised statistic
   224	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   225	a smaller absolute gap; we keep the raw-PR comparison as headline

 succeeded in 429ms:
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested whether
    15	other regular 4-polytopes ($24$-cell, $120$-cell) would produce
    16	comparable correspondences. The 600-cell was chosen because its
    17	H$_4$ Coxeter cascade structure aligns with the empirical signatures
    18	that motivated this paper, not from an a-priori derivation.
    19	\emph{Disclosure:} substrate-witness scope, no uniqueness claim
    20	(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
    21	on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
    22	$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
    23	battery and the eighteen preregistered tests, with thresholds
    24	preserved.
    25	
    26	\textbf{Single-seed determinism on the recurrent layer.} The v4
    27	six-signature results in~\S\ref{ssec:six_signatures} are reported on
    28	a single deterministic trajectory at seed $42$. Empirical CIs across
    29	$10$--$20$ cross-seed runs would strengthen the per-signature claims
    30	beyond the single-trajectory bootstrap of $58$ events that gives the
    31	WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
    32	in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
    33	\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
    34	overlap with two independent reference $\alpha$ ranges.
    35	\emph{Strengthening build:} 10--20 cross-seed runs of
    36	\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
    37	
    38	\textbf{Stylised stimulus models on the recurrent layer.} The v4
    39	stimulus models for WAKE (AR(1) noise + tonic shell + attention
    40	episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
    41	and PROPOFOL (low-amplitude tonic noise) are biologically motivated
    42	but abstract: a single shell anchor for tonic coherence, fixed
    43	$40$-tick period for slow-wave drive, etc. Real spatial structure of
    44	cortical input is much richer. The v4 stimulus models were redesigned
    45	after diagnostics on the v3 stimulus models to close v3 stimulus-model
    46	artefacts; v4 components are biologically-motivated and not fitted
    47	to subject-level measurements, but they are condition-specific
    48	design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
    49	explicitly frames v4 as a redesign. \emph{Evidence:} amplitudes and
    50	durations match published biological time scales; the v3$\to$v4
    51	diff is captured in
    52	\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}. \emph{Strengthening
    53	build:} replication on stimulus models derived from anatomically-grounded
    54	input statistics (e.g.\ retinotopic, tonotopic).
    55	
    56	\subsection{Post-hoc}\label{ssec:posthoc}
    57	
    58	\textbf{The 600-cell choice is post-hoc justified by empirical
    59	observables.} While the construction of $\Rsixhundred$ is theorem-
    60	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    61	polytope as the consciousness-substrate instance is motivated by the
    62	correspondences observed, not by an a-priori biological argument.
    63	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    64	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    65	preregistered correspondences plus six signatures; the H$_4$
    66	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    67	with the $24$-cell and $120$-cell on the same signatures; formal
    68	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    69	(deferred).
    70	
    71	\textbf{Cascade decomposition is one of several possible
    72	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    73	because it is machine-precise and biologically informative, but other
    74	bases (character-theoretic, Galois-twin) give the same physical
    75	predictions through different intermediate variables. \emph{Disclosure:}
    76	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    77	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    78	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    79	admissible decompositions.
    80	
    81	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    82	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    83	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    84	from a closure functional or symmetry argument. \emph{Disclosure:}
    85	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    86	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    87	derive it. \emph{Evidence:} the same operator (with the same shift)
    88	serves as the basis for the b-anomaly passive-regime
    89	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    90	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    91	named regularity criterion.
    92	
    93	\subsection{Interpretation}\label{ssec:interpretation}
    94	
    95	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    96	We do not claim the recurrent self-model layer ``is'' consciousness;
    97	we claim quantitative consistency with six published biological
    98	signatures on a deterministic trajectory. \emph{Disclosure:}
    99	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
   100	\emph{Evidence:} six signatures vs published thresholds.
   101	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
   102	formal account of which substrate observables map to which phenomenal
   103	contents (the bind\_phenomenal\_field channels) is not delivered.
   104	
   105	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   106	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   107	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   108	matches IIT direction. \emph{Strengthening build:} a
   109	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   110	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   111	
   112	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   113	do not claim ``cortex has drifted from an ideal polytope''; we
   114	quantify the distance between cortex and the deterministic H$_4$ null.
   115	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   116	$\sigma$-distances on three independent metrics. \emph{Strengthening
   117	build:} cross-parcellation replication (Schaefer, Glasser).
   118	
   119	\subsection{Test/claim}\label{ssec:testclaim}
   120	
   121	\textbf{Two preregistered interaction tests required higher $N$
   122	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   123	$N\!=\!20$. We document this transparently as consistent with
   124	underpowered interaction estimates on high-per-seed-variance terms,
   125	not a threshold change. \emph{Disclosure:}
   126	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   127	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   128	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   129	$19/20$ seeds positive. \emph{Strengthening build:} a second
   130	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   131	an $N\!=\!50$ characterisation of the per-seed distribution.
   132	
   133	\textbf{The original 2026-04-20 walks-back are reversed without
   134	threshold modification.} The reversals (P3, P4, P13) are documented
   135	in
   136	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   137	the original failure values, the methodology refinement, and the
   138	post-refinement values. \emph{Disclosure:} this paper carries those
   139	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   140	by-side results table. \emph{Strengthening build:} the strengthening
   141	builds for P3/P4/P13 above; no further claim is needed.
   142	
   143	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   144	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   145	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   146	this section. \emph{Strengthening build:} Bayesian posterior on
   147	$\Delta_{CP}$; full-IIT computation on the
   148	substrate's $S^{3}$ state space. The latter is computationally
   149	heavy and is deferred.
   150	
   151	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   152	
   153	\textbf{Single condition-dependent parameter $\eta$ is not derived
   154	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   155	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   156	this paper, not a learned trajectory. A predictive-processing
   157	extension where $\eta$ adapts on an error norm is an open build.
   158	
   159	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   160	this paper.} The companion programme (cascade-derivation, capstone
   161	coalgebra, RH formal) shares operator-level infrastructure but is not
   162	load-bearing here. Deliberately out of scope.
   163	
   164	\textbf{Out-of-scope items NOT delivered (correctly).}
   165	\begin{itemize}\itemsep=2pt
   166	\item Active-regime extension of the chess pattern-recognition test to
   167	  move-by-move game trajectories (this paper covers static positions only).
   168	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   169	  $2I$-equivariance — open build of the ACT companion paper.
   170	\item Lyapunov derivation $V(W)$ from a closure functional
   171	  $\mathcal{F}$ — open build of the ACT companion paper.
   172	\item Selection theorem for $\Rsixhundred$ over alternative regular
   173	  4-polytopes — see~\S\ref{ssec:regime}.
   174	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   175	  of the six signatures.
   176	\item Cross-parcellation replication of the HCP $\sigma$-distances
   177	  (Schaefer, Glasser, etc.).
   178	\item Bayesian posterior on the C$\times$P interaction.
   179	\item Verification of P10 (chess null mapping) at the preregistered
   180	  $20$-permutation count (the 2026-04-29 validation used $15$
   181	  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
   182	  robust in the $15$--$20$ range, but the prereg-exact rerun is open).
   183	\end{itemize}
   184	
   185	\subsection{The honest verdict}
   186	
   187	The result is a substrate witness: a geometry-fixed substrate, with
   188	no shape parameters tuned to any neural dataset, is consistent with
   189	eighteen preregistered correspondences and six companion drug/sleep
   190	EEG signatures, with all original gaps closed by methodology
   191	refinement and without modifying any preregistered threshold. We do
   192	not claim the substrate \emph{is} consciousness. We do not claim a
   193	selection theorem on the ACT bridge. We do not claim uniqueness for
   194	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   195	for these stronger claims are listed above and remain open.

exec
/bin/bash -lc "rg -n \"\\\\cite[p|t]?\\{|\\\\cite\\{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\[A-Za-z]+\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "canonical|unique|derive|derivation|selection theorem|Lyapunov|2I|retun|decisive|proves|establishes|forced|picks out|wins|load-bearing|independent|verbatim|not delivered|not claim" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 369ms:
rg: regex parse error:
    (?:\cite[p|t]?\{|\cite\{)
       ^^
error: unrecognized escape sequence

 exited 1 in 421ms:
 succeeded in 431ms:
papers/aria-closure-kernel/paper/main.tex:22:       independent empirical witnesses}
papers/aria-closure-kernel/paper/main.tex:43:the 600-cell instance $\Rsixhundred$ as the canonical discrete
papers/aria-closure-kernel/paper/main.tex:54:same fixed graph is then the load-bearing object in two
papers/aria-closure-kernel/paper/main.tex:55:\emph{independent} empirical works: a passive-regime structural
papers/aria-closure-kernel/paper/main.tex:65:with two independent empirical landings under no shape-parameter
papers/aria-closure-kernel/paper/main.tex:66:retuning between regimes. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:67:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:69:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:74:inherited verbatim here).
papers/aria-closure-kernel/paper/main.tex:79:$\Ph = (1+\sqrt 5)/2$, give its canonical instance on the 600-cell
papers/aria-closure-kernel/paper/main.tex:81:fixed operator (no shape retuning) in two independent empirical
papers/aria-closure-kernel/paper/main.tex:89:from canonical generators, verifies the graph facts
papers/aria-closure-kernel/paper/main.tex:94:unweighted variant, decisively above the $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/main.tex:97:qualitative ranking established independently by b-anomaly's data
papers/aria-closure-kernel/paper/main.tex:109:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:124:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:140:\noindent\emph{What we do not claim.}
papers/aria-closure-kernel/paper/main.tex:141:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:143:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:144:either empirical landing. We do not claim the operator is the
papers/aria-closure-kernel/paper/main.tex:145:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:146:(b-anomaly's Mode-B caveat is inherited verbatim) nor that the
papers/aria-closure-kernel/paper/main.tex:147:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:150:graph appears as the load-bearing object in two independent
papers/aria-closure-kernel/paper/main.tex:151:empirical works in two distinct regimes, with no shape retuning
papers/aria-closure-kernel/paper/sections/05_agreement.tex:5:This is the load-bearing geometric fact of the paper: the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:10:comparison that picks out the unweighted Laplacian.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
papers/aria-closure-kernel/paper/sections/05_agreement.tex:88:\textbf{Reading.} The unweighted Laplacian wins on both criteria
papers/aria-closure-kernel/paper/sections/05_agreement.tex:92:established independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:94:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:96:agree on which Laplacian variant is preferred. We do not claim
papers/aria-closure-kernel/paper/sections/05_agreement.tex:97:this is a uniqueness result; we report it as a two-criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:inherited verbatim).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:108:This is a non-trivial agreement between two independently-defined
papers/aria-closure-kernel/paper/sections/05_agreement.tex:115:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:120:inherited verbatim. The agreement also does not establish that
papers/aria-closure-kernel/paper/sections/05_agreement.tex:121:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:40:properties matching the family description; we do not claim a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:55:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:60:three independent frames:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:69:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  $2I$-equivariance, and a full reduced-flow convergence theorem
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:75:  a selection theorem; ACT is positioned as the future
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:81:mathematical problem rather than three independent ones (a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  the load-bearing object in two independent empirical works in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:110:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:111:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:113:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:120:  $w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim from
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:122:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:123:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:124:  convergence — all explicitly not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:125:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:27:applied; verbatim re-run of the b-anomaly fit on alternative
papers/aria-closure-kernel/paper/sections/09_limitations.tex:50:\emph{Evidence:} two independent empirical witnesses on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:62:caveat verbatim. \emph{Strengthening build:} a future blind variant
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:72:independent empirical witnesses across qualitatively distinct
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:75:the $\Ph^{-2}$ shift as the unique stability clamp under a named
papers/aria-closure-kernel/paper/sections/09_limitations.tex:85:\emph{computed agreement} between two independently-defined
papers/aria-closure-kernel/paper/sections/09_limitations.tex:86:objects, not a derivation that the discrete operator equals the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:96:variant wins on both the geometry-only criterion of this paper
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:106:\textbf{Two independent empirical landings, not formal physics.}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:vertex ($+x_{0}$ axis, the canonical pole). H$_4$ transitivity
papers/aria-closure-kernel/paper/sections/09_limitations.tex:133:\textbf{Selection layer not delivered.} As enumerated in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:135:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:142:into this paper.} The cascade-derivation programme, the capstone
papers/aria-closure-kernel/paper/sections/09_limitations.tex:144:infrastructure with this paper but are not load-bearing here.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:149:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:151:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:169:dataset, is consistent with two independent empirical landings in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:170:qualitatively distinct regimes. We do not claim the operator is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:171:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:172:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/02_definition.tex:113:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:115:(1)--(3); we report this explicitly and treat formal derivation as
papers/aria-closure-kernel/paper/sections/02_definition.tex:120:constrain the shift further; that derivation is not delivered
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:16:Pearson $\rho = 0.976$ on the unweighted Laplacian, decisively
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:$0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:24:retuning between regimes, appears as the load-bearing object in:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:41:The two witnesses are independent in the strict sense: no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:48:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:50:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:51:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:54:$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:55:aria-chess substrate-witness scope is inherited verbatim. We do
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:58:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:59:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:are not delivered here.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:design-level mass shift not retuned between regimes, and threads
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:75:two independent empirical landings on qualitatively distinct
papers/aria-closure-kernel/paper/sections/03_substrate.tex:5:This section gives the canonical discrete instance: $M = \Rsixhundred$,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the canonical generators alone.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
papers/aria-closure-kernel/paper/sections/03_substrate.tex:45:if their inner product equals the canonical short-edge value
papers/aria-closure-kernel/paper/sections/03_substrate.tex:51:nearest-neighbour adjacency on the canonical 600-cell embedding
papers/aria-closure-kernel/paper/sections/03_substrate.tex:54:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:of constant inner product with $v_{0}$. The nine canonical inner
papers/aria-closure-kernel/paper/sections/03_substrate.tex:92:verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:96:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:100:The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
papers/aria-closure-kernel/paper/sections/03_substrate.tex:101:the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
papers/aria-closure-kernel/paper/sections/01_introduction.tex:14:without inheriting either's load-bearing claims. That is what this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:35:The canonical discrete substrate is the 600-cell graph
papers/aria-closure-kernel/paper/sections/01_introduction.tex:45:\texttt{repro/verify\_kernel.py} from the canonical generators
papers/aria-closure-kernel/paper/sections/01_introduction.tex:51:operator, on one fixed graph, with no shape-parameter retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:52:between regimes, appears as the load-bearing object in two
papers/aria-closure-kernel/paper/sections/01_introduction.tex:69:  numerical agreement between two independently-defined objects (a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:72:\item \textbf{Variant comparison is decisive at the geometry-only
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  Laplacian wins on the geometry-only criterion. This reproduces,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:79:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:81:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:98:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:100:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:109:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:117:  Both caveats are inherited verbatim from the b-anomaly preprint.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:118:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:122:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:123:  reduced flow, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  is not delivered here.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:152:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:in two independent empirical works (b-anomaly five-dataset
papers/aria-closure-kernel/paper/sections/01_introduction.tex:164:witness) without shape-parameter retuning between regimes.\par
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:166:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:167:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:178:canonical generators, gives the graph facts, and the $9$-shell
papers/aria-closure-kernel/paper/sections/01_introduction.tex:183:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:5:This section threads the first independent empirical landing of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:8:and inherit the preprint's caveats verbatim.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:14:Model, is approximately $q^{2}$-independent in the relevant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:preprint's §3 derivation; we do not relitigate it here), and $A$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:28:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:57:\subsection{What the structural fit establishes}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  unweighted choice wins on both a pure-geometry criterion
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:89:which we inherit verbatim:
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:99:  decisive about whether the shape is forced by data: it is not.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:103:  not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  verified. The two-criterion agreement is criterion-independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:five independent measurements without shape retuning. This does
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:129:independent empirical landings without parameter retuning. The
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:5:This section threads the second independent empirical landing of
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:8:and inherit the preprint's substrate-witness scope verbatim.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:58:reading verbatim.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:64:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:91:  routing lifts leave-one-out classification at canonical depth
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:118:$\Ph^{-2}$ is not retuned. Under those design choices, the same
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:124:does not claim the substrate \emph{is} consciousness, does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:125:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:127:scope verbatim. What we add at the operator level is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:129:retuning between regimes — is the load-bearing object on both
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:137:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:138:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:Shift $\Ph^{-2}$     & not retuned                       & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:153:Caveat             & AIC tie; Mode-B kernel non-uniqueness &
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:159:The two witnesses are independent in the strict sense: no fitted

exec
/bin/bash -lc "rg -n \"citep\\{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 395ms:
papers/aria-closure-kernel/paper/main.tex:57:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:60:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:70:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:84:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:86:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:125:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:132:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:177:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:178:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/sections/02_definition.tex:118:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:91:qualitative ranking the b-anomaly paper~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:20:\item \textbf{RH polynomial filter}~\citep{SmartRHFormal2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:27:\item \textbf{YM cascade gap operator}~\citep{SmartYMMassGap2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:30:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:62:\item \textbf{RH preprint}~\citep{SmartRHFormal2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:68:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:73:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:121:  ~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:125:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:60:~\citep{SmartRHFormal2026}: the $\sigma$-fix subspace is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026}) realises this block decomposition
papers/aria-closure-kernel/paper/sections/03_substrate.tex:14:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:52:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:33:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:57:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71:  $P/S$-basis amplification ($\sim 2.2$~\citep{KrugerMatias2005}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:82:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:120:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:137:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:150:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.

exec
/bin/bash -lc "rg -n \"varphi|V_\\{600\\}|L_\\{V_\\{600\\}\\}|C_\\{\\\\Ph\\}|C_\\{\\\\varphi\\}|\\\\Cph|\\\\Ph|\\\\Lop|\\\\Rsixhundred\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "biologically-|theorem-|programme-|data-|geometry-|operator-|shape-|single-|two-|criterion-" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"H_\\"'$|H_'"\\{|H\\"'$|H'"\\"'$_|H'"\\"'$_|H'"\\"'$_4|H'"\\"'$_3|H'"\\"'$_n|H'"\\"'$|H'"\\"'$|H'"\\"'$|H'"\\\\"'$_" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 209ms:
rg: regex parse error:
    (?:varphi|V_\{600\}|L_\{V_\{600\}\}|C_\{\Ph\}|C_\{\varphi\}|\Cph|\Ph|\Lop|\Rsixhundred)
                                                                ^^
error: unrecognized escape sequence

 succeeded in 248ms:
papers/aria-closure-kernel/paper/main.tex:21:       a geometry-fixed kernel on the 600-cell with two\\
papers/aria-closure-kernel/paper/main.tex:40:We define a programme-level closure-response primitive
papers/aria-closure-kernel/paper/main.tex:48:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:64:geometry-fixed response operator that is simultaneously consistent
papers/aria-closure-kernel/paper/main.tex:65:with two independent empirical landings under no shape-parameter
papers/aria-closure-kernel/paper/main.tex:91:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:96:choice winning on the geometry-only criterion reproduces the
papers/aria-closure-kernel/paper/main.tex:149:this paper is: \emph{one geometry-fixed operator on one fixed
papers/aria-closure-kernel/paper/main.tex:170:short-edge graph build, Laplacian spectrum, operator-norm bound,
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:25:\item Condition-specific \emph{biologically-motivated} stimulus
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:28:  low-amplitude tonic noise for PROPOFOL). These are biologically-
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:128:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:                     single-seed; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:16:substrate. They are programme-positioned as members of the same
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:28:  Discrete cascade gap Hamiltonian, programme-positioned as a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:  programme-positioned as a member of the same polynomial-in-$L$
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:37:We list the family-membership claim as \emph{programme-positioned},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:80:strongest programme-level indication that the gap is a single
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:82:programme-level reading, not a proof of equivalence). The two
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:89:\paragraph{Closes (at the operator-witness level).}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:  variant winning the geometry-only criterion against two
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:127:\item \emph{Family-membership theorem.} The programme-home
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:  \emph{programme-positioned}, not formally classified.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:82:  ranking — a two-criterion convergence on the same fixed
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:98:  to the universality / shape-prediction claim itself, but it is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:112:  the data-$\chi^{2}$ ranking with the pure-geometry ranking
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  verified. The two-criterion agreement is criterion-independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:not establish the kernel as theorem-grade physics on the flavour
papers/aria-closure-kernel/paper/sections/03_substrate.tex:119:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:73:and the operator-norm bound is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:95:it for the operator-witness claims of this paper.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:48:exactly H$_3$-invariant from a single-vertex source (the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:92:established independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:94:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:97:this is a uniqueness result; we report it as a two-criterion
papers/aria-closure-kernel/paper/sections/01_introduction.tex:27:operator-norm bound is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:50:We claim a single \emph{operator witness}: that one geometry-fixed
papers/aria-closure-kernel/paper/sections/01_introduction.tex:51:operator, on one fixed graph, with no shape-parameter retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:60:  operator. The Laplacian spectrum, the operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:72:\item \textbf{Variant comparison is decisive at the geometry-only
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  Laplacian wins on the geometry-only criterion. This reproduces,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:79:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:135:To keep this paper inside the operator-witness scope, we use the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:148:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:159:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:160:600-cell graph, with computed spectrum, operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:164:witness) without shape-parameter retuning between regimes.\par
papers/aria-closure-kernel/paper/sections/01_introduction.tex:176:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:7:geometry-fixed response primitive: positive definite under (H1)--(H3)
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:67:\emph{programme-positioned}, not formally classified. The two
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:geometry-fixed Green operator on a fixed Coxeter graph, with a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:78:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/09_limitations.tex:45:theorem-level rigorous (H$_4$ Coxeter group theory), the choice
papers/aria-closure-kernel/paper/sections/09_limitations.tex:54:\textbf{The geometry-first variant agreement is not historically
papers/aria-closure-kernel/paper/sections/09_limitations.tex:58:data-$\chi^{2}$ ranking. The two-criterion convergence is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:95:\textbf{Variant ranking is criterion-dependent.} The unweighted
papers/aria-closure-kernel/paper/sections/09_limitations.tex:96:variant wins on both the geometry-only criterion of this paper
papers/aria-closure-kernel/paper/sections/09_limitations.tex:110:substrate \emph{is} consciousness). Neither lands a theorem-grade
papers/aria-closure-kernel/paper/sections/09_limitations.tex:122:\textbf{Discrete-to-continuum correlation is single-source.} The
papers/aria-closure-kernel/paper/sections/09_limitations.tex:143:coalgebra paper, and the Millennium drafts share operator-level
papers/aria-closure-kernel/paper/sections/09_limitations.tex:167:The result is an \emph{operator witness}: a geometry-fixed response

 succeeded in 317ms:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:34:structure under $H_{4}$; in particular, every vertex has the same
papers/aria-closure-kernel/paper/sections/01_introduction.tex:37:$H_{4}$ Coxeter orbits ($8$ axis vertices, $16$ half-integer
papers/aria-closure-kernel/paper/sections/01_introduction.tex:40:uniform degree~$12$ by H$_4$ transitivity, a $9$-shell $H_{3}$

exec
/bin/bash -lc "rg -n -F \"\\varphi\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n -F "V_{600}" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\Cph\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\Ph\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 271ms:
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}

 succeeded in 259ms:
papers/aria-closure-kernel/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
papers/aria-closure-kernel/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:44:The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
papers/aria-closure-kernel/paper/sections/03_substrate.tex:55:The graph $G_{V_{600}}$ has:
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:20:A \cdot \kappa_{V_{600}}(q^{2}),
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:26:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient

 succeeded in 325ms:
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with graph
papers/aria-closure-kernel/paper/main.tex:48:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:53:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:77:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:92:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:101:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:104:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:118:$\psi = \Cph^{-1} f$ for a localised source and the continuum
papers/aria-closure-kernel/paper/main.tex:126:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:132:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:142:stability clamp making $\Cph$ strictly positive definite. We do
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
papers/aria-closure-kernel/paper/sections/05_agreement.tex:18:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:29:trivially the diagonal of $\Cph^{-1}$ and the chord distance is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:47:within-shell variation that arises because $\Cph^{-1}$ is not
papers/aria-closure-kernel/paper/sections/05_agreement.tex:73:discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:56:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:58:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:61:so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:The operator norm of $\Cph^{-1}$ is the reciprocal of its smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:69:\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
papers/aria-closure-kernel/paper/sections/02_definition.tex:77:Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
papers/aria-closure-kernel/paper/sections/02_definition.tex:97:the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:\item $\Cph$ is strictly positive definite (the smallest eigenvalue
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:25:non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:58:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:66:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:83:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:89:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:100:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:106:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:121:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:159:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:176:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/09_limitations.tex:15:whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:5:This section positions $\Cph$ within the broader cascade programme
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:7:matters for the hostile-review reading: $\Cph$ is the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:family as $\Cph$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:29:  $\Cph$-style mass-regularised Laplacian on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:45:The closure response $\psi = \Cph^{-1} f$ is determined by the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:91:\item The operator $\Cph$ is well-defined, positive definite, and
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:  has $\|\Cph^{-1}\| = \Ph^{2}$ on any $(M, L_M)$ satisfying
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:14:between $\psi = \Cph^{-1} f$ and the continuum kernel
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/03_substrate.tex:118:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:120:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$ is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:120:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:127:establish, at the operator level, that the same fixed $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:114:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:115:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:119:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:128:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:137:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:66:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:68:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:70:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:75:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:80:of $\Cph$ is

 succeeded in 342ms:
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with graph
papers/aria-closure-kernel/paper/main.tex:42:Laplacian $L_M$ and golden ratio $\Ph = (1 + \sqrt 5)/2$. We give
papers/aria-closure-kernel/paper/main.tex:47:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:48:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:49:eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:52:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:67:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:77:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:79:$\Ph = (1+\sqrt 5)/2$, give its canonical instance on the 600-cell
papers/aria-closure-kernel/paper/main.tex:91:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:92:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:94:unweighted variant, decisively above the $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/main.tex:101:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:103:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:104:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:106:$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
papers/aria-closure-kernel/paper/main.tex:111:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:113:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:121:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:141:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/sections/02_definition.tex:12:Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
papers/aria-closure-kernel/paper/sections/02_definition.tex:13:and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:56:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:58:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:59:                    \;=\; \Ph^{-2} \;>\; 0,
papers/aria-closure-kernel/paper/sections/02_definition.tex:70:              \;=\; 1/\Ph^{-2} \;=\; \Ph^{2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:75:\|\psi\|_{2} \;\leq\; \Ph^{2}\, \|f\|_{2}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{sec:agreement}); this matches the closed-form $\Ph^{2}$ to
papers/aria-closure-kernel/paper/sections/02_definition.tex:85:$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
papers/aria-closure-kernel/paper/sections/02_definition.tex:86:$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
papers/aria-closure-kernel/paper/sections/02_definition.tex:101:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/sections/02_definition.tex:103:The shift $\Ph^{-2}$ is chosen so that:
papers/aria-closure-kernel/paper/sections/02_definition.tex:106:  is exactly $\Ph^{-2}$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:  has decay scale $\Ph$, not a free length parameter.
papers/aria-closure-kernel/paper/sections/02_definition.tex:113:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/05_agreement.tex:8:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
papers/aria-closure-kernel/paper/sections/05_agreement.tex:18:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:24:G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:53:Two $\Ph$-cocycle weighted Laplacian variants are tested as
papers/aria-closure-kernel/paper/sections/05_agreement.tex:57:\item \textbf{$\Ph$-geometric weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:59:  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:61:\item \textbf{$\Ph$-arithmetic weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:82:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:83:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:107:closed-form continuum exponential at the same length scale $\Ph$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:exponential. The $\Ph$-mediated agreement is an empirical fact
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\qquad \Ph \;=\; (1+\sqrt 5)/2,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:24:$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
papers/aria-closure-kernel/paper/sections/01_introduction.tex:26:positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:32:Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:vertices, $96$ $\Ph$-mixed vertices), connected by short edges
papers/aria-closure-kernel/paper/sections/01_introduction.tex:39:$\langle v, w\rangle = \Ph/2$. The graph has $|E|=720$ edges,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:43:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:58:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:73:  criterion.} Two $\Ph$-cocycle weighted Laplacian variants
papers/aria-closure-kernel/paper/sections/01_introduction.tex:74:  ($\Ph$-geometric, $\Ph$-arithmetic edge weights via shell-grade
papers/aria-closure-kernel/paper/sections/01_introduction.tex:75:  exponents $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:98:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:99:  $\Ph^{-2}$ is a design-level stability clamp that bounds
papers/aria-closure-kernel/paper/sections/01_introduction.tex:100:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:106:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
papers/aria-closure-kernel/paper/sections/03_substrate.tex:22:\item \textbf{$\Ph$-mixed orbit} ($96$ vertices): all even
papers/aria-closure-kernel/paper/sections/03_substrate.tex:23:  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:24:  $\Ph^{2} = \Ph + 1$ identity, equivalently
papers/aria-closure-kernel/paper/sections/03_substrate.tex:25:  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:47:\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:50:$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:79:\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:80:       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:104:is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:107:inner product exactly $\Ph/2$ within machine precision (tolerance
papers/aria-closure-kernel/paper/sections/03_substrate.tex:117:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:118:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:120:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:47:shift $\Ph^{-2}$, and the response is the resulting linear inverse.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:52:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:  has $\|\Cph^{-1}\| = \Ph^{2}$ on any $(M, L_M)$ satisfying
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:110:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:$\mathbb{Z}[\Ph]$ and multiplicities summing to $|V| = 120$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:18:Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:27:$12 - 6\Ph$    & $2.2918$  & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:28:$12 - 4\Ph$    & $5.5279$  & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:32:$4\Ph + 8$     & $14.4721$ & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:34:$6\Ph + 6$     & $15.7082$ & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:41:\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:43:12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:44:12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:45:4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:46:6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:48:The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:49:$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:51:$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:68:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:70:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:75:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:81:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:82:= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:89:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:8:on the substrate $(M, L_M)$, with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:12:Laplacian spectrum with closed-form values in $\mathbb{Z}[\Ph]$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:15:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex chord distances is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:above the $\Ph$-cocycle weighted variants ($0.888$ geometric,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:49:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:77:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:32:\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
papers/aria-closure-kernel/paper/sections/09_limitations.tex:33:nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
papers/aria-closure-kernel/paper/sections/09_limitations.tex:37:\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:75:the $\Ph^{-2}$ shift as the unique stability clamp under a named
papers/aria-closure-kernel/paper/sections/09_limitations.tex:84:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:99:$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:79:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:80:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:118:$\Ph^{-2}$ is not retuned. Under those design choices, the same
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:Shift $\Ph^{-2}$     & not retuned                       & not retuned \\

codex
**1. Claim Audit**

- “\(\|\Cph^{-1}\|=\Ph^2\)” is established for the 600-cell finite graph and for finite graphs with \(0\in\sigma(L)\): `main.tex:48`, `sections/02_definition.tex:64-80`, `results.json:77-82`. But `sections/08_programme_home.tex:91-93` overgeneralises this to “any \((M,L_M)\) satisfying (H1)--(H3)”; a Dirichlet continuum interval can have \(\lambda_{\min}(L)>0\), giving \(\|\Cph^{-1}\|<\Ph^2\).
- 600-cell vertex, edge, degree, shell, and spectrum claims match `results.json`: `sections/03_substrate.tex:55-68`, `sections/03_substrate.tex:83-92`, `sections/04_spectrum.tex:26-36`.
- “The graph is connected” is true for the 600-cell, but the stated proof is insufficient: transitivity plus a non-empty edge orbit does not alone prove connectedness. Also the script output does not report connected components: `sections/03_substrate.tex:62-68`, `verify_kernel.py:327-365`.
- The Laplacian spectrum claim is established numerically and matches the closed forms: `sections/04_spectrum.tex:26-34`, `results.json:39-75`.
- The H\(_4\) irrep/block claim is not established by the verification artifact; it is imported from aria-chess and should be labelled as such: `sections/04_spectrum.tex:84-95`.
- The headline per-vertex correlations are correct: paper `sections/05_agreement.tex:81-83`; artifact `results.json:130-142`.
- The explanation of shell-mean vs per-vertex correlation is wrong. `sections/05_agreement.tex:47-49` says within-shell variation arises because \(\Cph^{-1}\) is not H\(_3\)-invariant. For an H\(_3\)-fixed source on the unweighted 600-cell graph, the response is shell-constant up to numerical precision; my local check gave shell stds around \(10^{-17}\). The difference is weighting/excluding the source, not “noise.”
- The b-anomaly table matches the README: paper `sections/06_passive_witness.tex:48-52`; README `README.md:16-22`.
- The b-anomaly AIC tie and nonlinear drift numbers match the README: paper `sections/06_passive_witness.tex:92-108`; README `README.md:30-33`.
- The label “Mode-B drift caveat” is misused for the free-width Gaussian alternative: `sections/06_passive_witness.tex:100-103`. Mode-B drift is the linearised-vs-nonlinear refit issue.
- The aria-chess inherited numbers mostly match: \(17/18\), \(18/18\), P4 \(+0.190\), six signatures, chess/conversation/HCP numbers: `sections/07_active_witness.tex:47-83`, `sections/07_active_witness.tex:89-108`; companion `main.tex:81-152`, `sections/05_results.tex:92-164`, `sections/07_cross_domain.tex:45-99`, `sections/07_cross_domain.tex:132-149`, `sections/07_cross_domain.tex:178-224`.
- “Three-way confidence overlap” is too strong as written in the kernel paper: `sections/07_active_witness.tex:67-71`. The companion clarifies pairwise overlaps with the WAKE interval, not a common triple intersection: `sections/05_results.tex:189-196`.

**2. Internal Consistency**

- Abstract/headline numeric values match the body and `results.json`.
- Main scope discipline is good: the paper repeatedly says no \(\Ph^{-2}\) derivation, no 600-cell uniqueness, no kernel uniqueness, no ACT selection theorem: `main.tex:62-74`, `main.tex:140-152`.
- Conflict: `sections/09_limitations.tex:122-129` says a multi-source robustness sweep is recorded in script output. It is not in `results.json`, and `verify_kernel.py:339-354` uses one canonical pole.
- Conflict: `sections/05_agreement.tex:45-49` says shell averaging reduces within-shell variation; the graph symmetry implies shell-constant response.
- Conflict: `sections/07_active_witness.tex:151-154` lists active-regime “Free parameters” as only \(\eta\). The companion discloses v4 condition-specific stimulus-model design choices: `aria-chess sections/09_limitations.tex:38-48`.
- The repeated “canonical discrete substrate” language (`main.tex:43`, `sections/01_introduction.tex:35`, `sections/03_substrate.tex:5`) is stronger than the stated post-hoc substrate choice.

**3. External Consistency / Numerics**

All requested headline numerics agree with `results.json`:

- \(120\) vertices, \(720\) edges, degree \(12\): `results.json:4-10`.
- Shell sizes \(\{1,12,20,12,30,12,20,12,1\}\): `results.json:11-21`.
- Spectrum values and multiplicities match the stated \(\mathbb Z[\Ph]\) list: `results.json:39-75`.
- \(\|\Cph^{-1}\|=\Ph^2\approx2.618\): `results.json:77-82`.
- Correlations \(0.976\), \(0.888\), \(0.884\) and shell mean \(0.923\): `results.json:130-142`.

Disagreements are not in the requested numeric values, but in verification claims: connectedness and multi-source robustness are not reported by the artifact.

**4. Operator-Witness Scope Discipline**

No explicit forbidden theorem is claimed, but several sentences lean too far:

- “picks out the unweighted Laplacian” should be “selects among the three tested variants”: `sections/05_agreement.tex:10`.
- “decisively above” should be bounded to “within the tested variants”: `main.tex:94-95`, `sections/10_conclusion.tex:16-18`.
- “independent in the strict sense: no ... methodological choice is shared” is false because the operator/substrate/shift are shared by design: `sections/07_active_witness.tex:159-163`, `sections/10_conclusion.tex:41-45`.
- “strongest programme-level indication” is speculative and should be softened: `sections/08_programme_home.tex:79-85`.

**5. Tightness: Suggested One-Line Edits**

- `sections/05_agreement.tex:10`: “...and the variant comparison among two \(\Ph\)-cocycle weighted controls.”
- `sections/05_agreement.tex:45-49`: “The shell-mean test is an equal-shell summary; the per-vertex test weights shells by multiplicity and excludes the source.”
- `sections/09_limitations.tex:127-129`: “By H\(_4\) transitivity any source is equivalent; the script reports the canonical pole only.”
- `sections/07_active_witness.tex:67-71`: “The WAKE CI overlaps the Sleep-EDFx and prior-pipeline intervals pairwise.”
- `sections/07_active_witness.tex:151-154`: “Kernel shape parameters: none; active layer: fixed disclosed v4 stimulus protocols plus condition-dependent \(\eta\).”

**6. Surface Issues**

- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently for main symbols. Raw `V_{600}` appears mainly inside graph/kernel subscripts, which is acceptable.
- Inconsistent H notation: `H$_4$`, `$H_{4}$`, `H$_3$`; standardise.
- `sections/07_active_witness.tex:28-29`: source line break creates “biologically- motivated”; use “biologically motivated” or “biologically-motivated”.
- “b-anomaly” vs “B-anomaly” capitalisation varies.
- I did not compile because the workspace is read-only; surface LaTeX review is by inspection.

**7. Top Three Fixes**

1. Fix verification overclaims: add connected-component and multi-source checks to the artifact, or remove the claims. Key lines: `sections/03_substrate.tex:62-68`, `sections/09_limitations.tex:122-129`.
2. Correct the mathematical explanation around shell means and the overgeneralised operator-norm equality. Key lines: `sections/05_agreement.tex:45-49`, `sections/08_programme_home.tex:91-93`.
3. Tighten inherited empirical scope: relabel b-anomaly caveats, replace “three-way overlap” with pairwise overlap, and avoid understating aria-chess active-regime design choices. Key lines: `sections/06_passive_witness.tex:100-108`, `sections/07_active_witness.tex:67-71`, `sections/07_active_witness.tex:151-163`.

**8. Verdict**

Publication ready: no — must-fix list above. The core numbers are consistent, but several proof/verification and scope-discipline issues need correction before publication.
tokens used
136,354
**1. Claim Audit**

- “\(\|\Cph^{-1}\|=\Ph^2\)” is established for the 600-cell finite graph and for finite graphs with \(0\in\sigma(L)\): `main.tex:48`, `sections/02_definition.tex:64-80`, `results.json:77-82`. But `sections/08_programme_home.tex:91-93` overgeneralises this to “any \((M,L_M)\) satisfying (H1)--(H3)”; a Dirichlet continuum interval can have \(\lambda_{\min}(L)>0\), giving \(\|\Cph^{-1}\|<\Ph^2\).
- 600-cell vertex, edge, degree, shell, and spectrum claims match `results.json`: `sections/03_substrate.tex:55-68`, `sections/03_substrate.tex:83-92`, `sections/04_spectrum.tex:26-36`.
- “The graph is connected” is true for the 600-cell, but the stated proof is insufficient: transitivity plus a non-empty edge orbit does not alone prove connectedness. Also the script output does not report connected components: `sections/03_substrate.tex:62-68`, `verify_kernel.py:327-365`.
- The Laplacian spectrum claim is established numerically and matches the closed forms: `sections/04_spectrum.tex:26-34`, `results.json:39-75`.
- The H\(_4\) irrep/block claim is not established by the verification artifact; it is imported from aria-chess and should be labelled as such: `sections/04_spectrum.tex:84-95`.
- The headline per-vertex correlations are correct: paper `sections/05_agreement.tex:81-83`; artifact `results.json:130-142`.
- The explanation of shell-mean vs per-vertex correlation is wrong. `sections/05_agreement.tex:47-49` says within-shell variation arises because \(\Cph^{-1}\) is not H\(_3\)-invariant. For an H\(_3\)-fixed source on the unweighted 600-cell graph, the response is shell-constant up to numerical precision; my local check gave shell stds around \(10^{-17}\). The difference is weighting/excluding the source, not “noise.”
- The b-anomaly table matches the README: paper `sections/06_passive_witness.tex:48-52`; README `README.md:16-22`.
- The b-anomaly AIC tie and nonlinear drift numbers match the README: paper `sections/06_passive_witness.tex:92-108`; README `README.md:30-33`.
- The label “Mode-B drift caveat” is misused for the free-width Gaussian alternative: `sections/06_passive_witness.tex:100-103`. Mode-B drift is the linearised-vs-nonlinear refit issue.
- The aria-chess inherited numbers mostly match: \(17/18\), \(18/18\), P4 \(+0.190\), six signatures, chess/conversation/HCP numbers: `sections/07_active_witness.tex:47-83`, `sections/07_active_witness.tex:89-108`; companion `main.tex:81-152`, `sections/05_results.tex:92-164`, `sections/07_cross_domain.tex:45-99`, `sections/07_cross_domain.tex:132-149`, `sections/07_cross_domain.tex:178-224`.
- “Three-way confidence overlap” is too strong as written in the kernel paper: `sections/07_active_witness.tex:67-71`. The companion clarifies pairwise overlaps with the WAKE interval, not a common triple intersection: `sections/05_results.tex:189-196`.

**2. Internal Consistency**

- Abstract/headline numeric values match the body and `results.json`.
- Main scope discipline is good: the paper repeatedly says no \(\Ph^{-2}\) derivation, no 600-cell uniqueness, no kernel uniqueness, no ACT selection theorem: `main.tex:62-74`, `main.tex:140-152`.
- Conflict: `sections/09_limitations.tex:122-129` says a multi-source robustness sweep is recorded in script output. It is not in `results.json`, and `verify_kernel.py:339-354` uses one canonical pole.
- Conflict: `sections/05_agreement.tex:45-49` says shell averaging reduces within-shell variation; the graph symmetry implies shell-constant response.
- Conflict: `sections/07_active_witness.tex:151-154` lists active-regime “Free parameters” as only \(\eta\). The companion discloses v4 condition-specific stimulus-model design choices: `aria-chess sections/09_limitations.tex:38-48`.
- The repeated “canonical discrete substrate” language (`main.tex:43`, `sections/01_introduction.tex:35`, `sections/03_substrate.tex:5`) is stronger than the stated post-hoc substrate choice.

**3. External Consistency / Numerics**

All requested headline numerics agree with `results.json`:

- \(120\) vertices, \(720\) edges, degree \(12\): `results.json:4-10`.
- Shell sizes \(\{1,12,20,12,30,12,20,12,1\}\): `results.json:11-21`.
- Spectrum values and multiplicities match the stated \(\mathbb Z[\Ph]\) list: `results.json:39-75`.
- \(\|\Cph^{-1}\|=\Ph^2\approx2.618\): `results.json:77-82`.
- Correlations \(0.976\), \(0.888\), \(0.884\) and shell mean \(0.923\): `results.json:130-142`.

Disagreements are not in the requested numeric values, but in verification claims: connectedness and multi-source robustness are not reported by the artifact.

**4. Operator-Witness Scope Discipline**

No explicit forbidden theorem is claimed, but several sentences lean too far:

- “picks out the unweighted Laplacian” should be “selects among the three tested variants”: `sections/05_agreement.tex:10`.
- “decisively above” should be bounded to “within the tested variants”: `main.tex:94-95`, `sections/10_conclusion.tex:16-18`.
- “independent in the strict sense: no ... methodological choice is shared” is false because the operator/substrate/shift are shared by design: `sections/07_active_witness.tex:159-163`, `sections/10_conclusion.tex:41-45`.
- “strongest programme-level indication” is speculative and should be softened: `sections/08_programme_home.tex:79-85`.

**5. Tightness: Suggested One-Line Edits**

- `sections/05_agreement.tex:10`: “...and the variant comparison among two \(\Ph\)-cocycle weighted controls.”
- `sections/05_agreement.tex:45-49`: “The shell-mean test is an equal-shell summary; the per-vertex test weights shells by multiplicity and excludes the source.”
- `sections/09_limitations.tex:127-129`: “By H\(_4\) transitivity any source is equivalent; the script reports the canonical pole only.”
- `sections/07_active_witness.tex:67-71`: “The WAKE CI overlaps the Sleep-EDFx and prior-pipeline intervals pairwise.”
- `sections/07_active_witness.tex:151-154`: “Kernel shape parameters: none; active layer: fixed disclosed v4 stimulus protocols plus condition-dependent \(\eta\).”

**6. Surface Issues**

- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently for main symbols. Raw `V_{600}` appears mainly inside graph/kernel subscripts, which is acceptable.
- Inconsistent H notation: `H$_4$`, `$H_{4}$`, `H$_3$`; standardise.
- `sections/07_active_witness.tex:28-29`: source line break creates “biologically- motivated”; use “biologically motivated” or “biologically-motivated”.
- “b-anomaly” vs “B-anomaly” capitalisation varies.
- I did not compile because the workspace is read-only; surface LaTeX review is by inspection.

**7. Top Three Fixes**

1. Fix verification overclaims: add connected-component and multi-source checks to the artifact, or remove the claims. Key lines: `sections/03_substrate.tex:62-68`, `sections/09_limitations.tex:122-129`.
2. Correct the mathematical explanation around shell means and the overgeneralised operator-norm equality. Key lines: `sections/05_agreement.tex:45-49`, `sections/08_programme_home.tex:91-93`.
3. Tighten inherited empirical scope: relabel b-anomaly caveats, replace “three-way overlap” with pairwise overlap, and avoid understating aria-chess active-regime design choices. Key lines: `sections/06_passive_witness.tex:100-108`, `sections/07_active_witness.tex:67-71`, `sections/07_active_witness.tex:151-163`.

**8. Verdict**

Publication ready: no — must-fix list above. The core numbers are consistent, but several proof/verification and scope-discipline issues need correction before publication.

OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dde7f-5bb1-7dc1-8cc4-a7b682312b73
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
I’ll do this as a referee-style audit against the local sources, with line-level citations from the LaTeX and source docs. I’m starting by mapping file sizes and then I’ll read the paper section by section before checking the numeric provenance.
exec
/bin/bash -lc 'wc -l "papers/aria-closure-kernel/repro/verify_kernel.py" "papers/aria-closure-kernel/repro/results.json" "docs/aria-closure-kernel.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l "papers/aria-closure-kernel/paper/sections/06_passive_witness.tex" "papers/aria-closure-kernel/paper/sections/07_active_witness.tex" "papers/aria-closure-kernel/paper/sections/08_programme_home.tex" "papers/aria-closure-kernel/paper/sections/09_limitations.tex" "papers/aria-closure-kernel/paper/sections/10_conclusion.tex" "papers/aria-closure-kernel/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l "papers/aria-closure-kernel/paper/main.tex" "papers/aria-closure-kernel/paper/sections/01_introduction.tex" "papers/aria-closure-kernel/paper/sections/02_definition.tex" "papers/aria-closure-kernel/paper/sections/03_substrate.tex" "papers/aria-closure-kernel/paper/sections/04_spectrum.tex" "papers/aria-closure-kernel/paper/sections/05_agreement.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "find \"papers/aria-chess-paper/paper/sections\" -maxdepth 1 -type f -name '*.tex' -print" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 331ms:
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

 succeeded in 352ms:
  469 papers/aria-closure-kernel/repro/verify_kernel.py
  154 papers/aria-closure-kernel/repro/results.json
  295 docs/aria-closure-kernel.md
  227 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md
 1145 total

 succeeded in 352ms:
  141 papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  174 papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  138 papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  176 papers/aria-closure-kernel/paper/sections/09_limitations.tex
   90 papers/aria-closure-kernel/paper/sections/10_conclusion.tex
   68 papers/aria-closure-kernel/paper/references.bib
  787 total

 succeeded in 360ms:
  198 papers/aria-closure-kernel/paper/main.tex
  192 papers/aria-closure-kernel/paper/sections/01_introduction.tex
  122 papers/aria-closure-kernel/paper/sections/02_definition.tex
  137 papers/aria-closure-kernel/paper/sections/03_substrate.tex
  100 papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  144 papers/aria-closure-kernel/paper/sections/05_agreement.tex
  893 total

codex
The kernel paper is about 1,600 lines including bibliography, so the line-level pass is tractable. I’m reading the full LaTeX now, keeping the companion and source docs separate so I can distinguish paper-internal issues from inherited-claim issues.
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/main.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/01_introduction.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/02_definition.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/03_substrate.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 353ms:
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
    79	\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
    80	to machine precision.
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
   107	\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
   108	  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
   109	  are fixed by the single design choice $\Ph^{-2}$, giving a single
   110	  dimensional parameter throughout the operator;
   111	\item the continuum projection (Eq.~\eqref{eq:green_continuum})
   112	  has decay scale $\Ph$, not a free length parameter.
   113	\end{enumerate}
   114	We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
   115	symmetry argument. It is a design-level choice motivated by
   116	(1)--(3); we report this explicitly and treat formal derivation as
   117	an open build (\S\ref{sec:limitations}). The companion
   118	adaptive-closure-transport
   119	preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
   120	selection-layer dynamics over $W$-space that would, if delivered,
   121	constrain the shift further; that derivation is not delivered
   122	there or here.

 succeeded in 389ms:
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
    41	$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
    42	corresponding Laplacian $L_M$ (graph, simplicial, or continuum)
    43	and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
    44	the 600-cell instance $\Rsixhundred$ as the discrete substrate
    45	shared by the two empirical witnesses (the choice of this polytope
    46	is post-hoc motivated by those landings, \S\ref{sec:limitations};
    47	numerically reproduced: $|V|=120$, $|E|=720$, uniform
    48	degree~$12$, H$_3$ shell decomposition
    49	$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
    50	matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
    51	operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
    52	eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
    53	agreement at per-vertex Pearson correlation $0.976$ between the
    54	discrete Green response and the continuum kernel
    55	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
    56	\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
    57	same fixed graph is then the load-bearing object in two
    58	\emph{independent} empirical works: a passive-regime structural
    59	fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
    60	public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
    61	active-regime substrate witness against eighteen preregistered
    62	neuroscience correspondences plus six drug/sleep EEG
    63	signatures~\citep{SmartAriaChess2026}.
    64	
    65	\noindent\emph{Scope.}
    66	This paper presents an empirical \emph{operator witness}: a
    67	geometry-fixed response operator that is simultaneously consistent
    68	with two independent empirical landings under no shape-parameter
    69	retuning between regimes. It is \emph{not} a derivation of the
    70	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    71	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    72	selection theorem on the companion adaptive-closure-transport
    73	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    74	a model-preference claim against alternative kernels on either
    75	empirical landing (the b-anomaly AIC comparison and the aria-chess
    76	substrate-witness scope are documented in their own preprints and
    77	inherited verbatim here).
    78	
    79	\begin{abstract}
    80	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    81	a closure substrate $M$ with corresponding Laplacian $L_M$ and
    82	$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
    83	the discrete instance shared by two empirical witnesses, and
    84	document its appearance as the same fixed operator (no shape
    85	retuning) in two independent empirical
    86	works: (i)~a five-dataset structural fit of the
    87	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    88	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    89	preregistered substrate witness against cortical signatures plus
    90	six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
    91	include the numerical reproduction script
    92	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
    93	from canonical generators, verifies the graph facts
    94	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
    95	Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
    96	$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
    97	agreement at per-vertex Pearson correlation $0.976$ for the
    98	unweighted variant, above the two $\Ph$-cocycle weighted variants
    99	tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
   100	tested variants the unweighted Laplacian ranks highest on the
   101	geometry-only criterion, reproducing the qualitative ranking
   102	established separately by b-anomaly's data $\chi^{2}$ comparison
   103	(the b-anomaly preprint flags that its data was looked at first
   104	and the geometry ranking verified afterward; the agreement is
   105	criterion-independent but historically non-blind, a caveat we
   106	inherit verbatim).
   107	
   108	\noindent\emph{(i) Operator definition and properties.}
   109	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   110	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   111	$\Ph^{-2} \approx 0.382$, operator norm
   112	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   113	in one coordinate $x$ is the closed-form Green's function
   114	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   115	
   116	\noindent\emph{(ii) The 600-cell instance.}
   117	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   118	generated by three orbits ($8$~axis, $16$~half-integer,
   119	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   120	on the short-edge graph; the Laplacian has nine eigenvalue classes
   121	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   122	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   123	
   124	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   125	Per-vertex Pearson correlation between the discrete response
   126	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   127	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
   128	vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
   129	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   130	Same source vertex, same fixed shift, no parameter fitting; the
   131	correlation is invariant under choice of source up to numerical
   132	precision (multi-source sweep, \S\ref{sec:limitations}).
   133	
   134	\noindent\emph{(iv) Two independent empirical witnesses.}
   135	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   136	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   137	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   138	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   139	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   140	with one fitted dimensionless amplitude per dataset and the kernel
   141	shape held fixed. (b)~Active regime,
   142	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   143	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   144	condition-dependent self-injection coupling
   145	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   146	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   147	degree, passes $17/18$ preregistered correspondences (frozen
   148	2026-04-18) at standard methodology and $18/18$ after a documented
   149	$N\!=\!20$ deep-dive on the residual high-variance
   150	$C\!\times\!P$ interaction (P4), plus $6/6$ literature-thresholded
   151	drug/sleep EEG signatures on a single deterministic seed.
   152	
   153	\noindent\emph{What we do not claim.}
   154	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   155	stability clamp making $\Cph$ strictly positive definite. We do
   156	not claim $\Rsixhundred$ is the unique substrate consistent with
   157	either empirical landing. We do not claim the operator is the
   158	unique kernel shape consistent with the b-anomaly data
   159	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   160	drift caveats are inherited verbatim) nor that the
   161	aria-chess substrate witness establishes a selection theorem on
   162	the adaptive-closure-transport 4-tuple. The structural scope of
   163	this paper is: \emph{one geometry-fixed operator on one fixed
   164	graph appears as the load-bearing object in two independent
   165	empirical works in two distinct regimes, with no shape retuning
   166	between them}.
   167	\end{abstract}
   168	
   169	% =====================================================================
   170	\input{sections/01_introduction.tex}
   171	\input{sections/02_definition.tex}
   172	\input{sections/03_substrate.tex}
   173	\input{sections/04_spectrum.tex}
   174	\input{sections/05_agreement.tex}
   175	\input{sections/06_passive_witness.tex}
   176	\input{sections/07_active_witness.tex}
   177	\input{sections/08_programme_home.tex}
   178	\input{sections/09_limitations.tex}
   179	\input{sections/10_conclusion.tex}
   180	% =====================================================================
   181	
   182	\section*{Reproducibility}
   183	The complete numerical verification (vertex construction,
   184	short-edge graph build, Laplacian spectrum, operator-norm bound,
   185	discrete-to-continuum correlation across three Laplacian variants)
   186	is reproducible from \texttt{repro/verify\_kernel.py} in this
   187	paper's bundle. No randomness, no fitted parameters: all numbers
   188	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   189	\S\ref{sec:agreement} are deterministic outputs of the script.
   190	The two empirical witness preprints
   191	(b-anomaly~\citep{SmartBAnomaly2026},
   192	aria-chess~\citep{SmartAriaChess2026}) carry their own
   193	reproducibility artifacts; this paper does not duplicate them.
   194	
   195	\bibliographystyle{plainnat}
   196	\bibliography{references}
   197	
   198	\end{document}

 succeeded in 437ms:
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
    35	The discrete substrate used by the two empirical witnesses is
    36	the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
    37	generated by three standard coordinate families ($8$ axis vertices,
    38	$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
    39	short edges $\langle v, w\rangle = \Ph/2$. The choice of this
    40	polytope is post-hoc motivated by the empirical landings
    41	(\S\ref{sec:limitations}); the construction itself is theorem-level
    42	rigorous. The graph has $|E|=720$ edges, uniform degree~$12$ by
    43	H$_4$ transitivity, a $9$-shell H$_3$
    44	partition $\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
    45	$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
    46	classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
    47	All of these facts are reproduced numerically by
    48	\texttt{repro/verify\_kernel.py} from the canonical generators
    49	alone — no external data input.
    50	
    51	\subsection*{What this paper claims}
    52	
    53	We claim a single \emph{operator witness}: that one geometry-fixed
    54	operator, on one fixed graph, with no shape-parameter retuning
    55	between regimes, appears as the load-bearing object in two
    56	empirical works covering qualitatively distinct physical settings.
    57	
    58	\begin{enumerate}\itemsep=2pt
    59	\item \textbf{Operator definition is fixed by the construction.}
    60	  Once $\Rsixhundred$ is selected and the stability shift
    61	  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
    62	  parameter, no fitted threshold, no learned weight enters the
    63	  operator. The Laplacian spectrum, the operator-norm bound, and
    64	  the discrete-to-continuum agreement are computed (not fitted)
    65	  from the construction and reproduced in
    66	  \texttt{repro/verify\_kernel.py}.
    67	\item \textbf{Discrete-to-continuum agreement is empirical, not
    68	  postulated.} For a localised source at any vertex, the discrete
    69	  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
    70	  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
    71	  $\rho = 0.976$ on the unweighted graph Laplacian. This is
    72	  numerical agreement between two independently-defined objects (a
    73	  120-dimensional discrete inverse and a continuum exponential
    74	  kernel), not a definitional identity.
    75	\item \textbf{Variant comparison among the three tested variants.}
    76	  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
    77	  $\Ph$-arithmetic edge weights via shell-grade exponents
    78	  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    79	  correlation: $0.888$ and $0.884$ respectively. Within the three
    80	  tested variants, the unweighted Laplacian ranks highest on the
    81	  geometry-only criterion. This reproduces,
    82	  on a different test, the qualitative ranking established
    83	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    84	  (\S\ref{sec:passive_witness}).
    85	\item \textbf{Two independent empirical landings, same operator.}
    86	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    87	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    88	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    89	  public datasets, with one fitted dimensionless amplitude per
    90	  dataset and the kernel held fixed; sign uniformity holds in
    91	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
    92	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
    93	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
    94	  recurrent self-model layer above the substrate, to pass eighteen
    95	  preregistered cortical correspondences (frozen 2026-04-18) plus
    96	  six drug/sleep EEG signatures.
    97	\end{enumerate}
    98	
    99	\subsection*{What this paper does \emph{not} claim}
   100	
   101	\begin{itemize}\itemsep=2pt
   102	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
   103	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   104	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   105	  functional or a symmetry argument; we report its role as a
   106	  regularisation-of-mass scale.
   107	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   108	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   109	  highly symmetric graphs, and continuum substrates are all
   110	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   111	  is post-hoc motivated by the empirical landings; a formal
   112	  ablation against alternative substrates is an open build.
   113	\item \emph{Not a kernel-uniqueness claim on either empirical
   114	  landing.} The b-anomaly's free-width Gaussian alternative shows
   115	  that a free-width Gaussian charm-loop proxy fits the same five
   116	  datasets comparably in $\chi^{2}$ at the cost of one extra shape
   117	  parameter; the b-anomaly AIC comparison against
   118	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   119	  statistical tie on current data
   120	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   121	  Both caveats are inherited verbatim from the b-anomaly preprint.
   122	\item \emph{Not a selection theorem on the
   123	  ACT 4-tuple.} The companion adaptive-closure-transport
   124	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   125	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   126	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   127	  reduced flow, edge-space decomposition under $2I$-equivariance,
   128	  full reduced-flow convergence — is left open in that paper and
   129	  is not delivered here.
   130	\item \emph{Not a circuit-level model on the active-regime side.}
   131	  The aria-chess preprint operates at the architectural-algorithmic
   132	  level above $\Cph$. We import its empirical results verbatim and
   133	  do not relitigate them here; their substrate-witness scope
   134	  applies.
   135	\end{itemize}
   136	
   137	\subsection*{Mapping from numerics to admissible claims}
   138	
   139	To keep this paper inside the operator-witness scope, we use the
   140	same claim-boundary discipline as the aria-chess
   141	preprint~\citep{SmartAriaChess2026}: numerical results
   142	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   143	$\mathcal C_{\mathrm{admissible}}$ by the rule
   144	\[
   145	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   146	        \mathcal C_{\mathrm{admissible}},
   147	\qquad
   148	\mathcal C_{\mathrm{admissible}}
   149	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   150	\]
   151	A numerically computed quantity (the Laplacian spectrum, the
   152	operator-norm bound, the per-vertex correlation $0.976$) licenses
   153	a `computed'-type claim. A statistical agreement at the operator
   154	level (sign uniformity in $5/5$ datasets, an $18/18$ preregistered
   155	tally) licenses a `consistent with'-type claim. We never write
   156	`derives the kernel', `proves uniqueness', or `establishes
   157	selection'.
   158	
   159	\medskip
   160	\begin{center}
   161	\fbox{\parbox{0.92\linewidth}{\small
   162	\textbf{What is claimed / what is not.}\par
   163	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   164	600-cell graph, with computed spectrum, operator-norm bound, and
   165	discrete-to-continuum correlation; the same fixed operator appearing
   166	in two independent empirical works (b-anomaly five-dataset
   167	structural fit; aria-chess $18/18$ + $6/6$ preregistered substrate
   168	witness) without shape-parameter retuning between regimes.\par
   169	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   170	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   171	landing; a selection theorem on the ACT 4-tuple; that either
   172	empirical landing settles the underlying physics (flavour anomaly
   173	or consciousness) by the operator alone.
   174	}}
   175	\end{center}
   176	
   177	\subsection*{Layout}
   178	
   179	\S\ref{sec:definition} gives the operator definition, the positivity
   180	properties of $\Cph$, the operator-norm bound, and the continuum
   181	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   182	canonical generators, gives the graph facts, and the $9$-shell
   183	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   184	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   185	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   186	across three Laplacian variants. \S\ref{sec:passive_witness} and
   187	\S\ref{sec:active_witness} thread the two independent empirical
   188	witnesses (b-anomaly and aria-chess) at the operator level.
   189	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   190	for the polynomial-in-$L$ Lyapunov family that recurs across the
   191	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   192	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 439ms:
     1	% =====================================================================
     2	\section{The 600-cell substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section gives the discrete instance used by the two empirical
     6	witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
     7	under H$_4$ Coxeter symmetry, with the standard short-edge graph
     8	Laplacian. The choice of this polytope is post-hoc motivated by
     9	the empirical landings (\S\ref{sec:limitations}); the
    10	construction itself is theorem-level rigorous in H$_4$ Coxeter
    11	group theory. All facts in this section are reproduced numerically
    12	by \texttt{repro/verify\_kernel.py} from the canonical generators
    13	alone.
    14	
    15	\subsection{Vertex set}\label{ssec:vertices}
    16	
    17	$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
    18	$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
    19	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
    20	list partitions into three standard coordinate families:
    21	\begin{itemize}\itemsep=2pt
    22	\item \textbf{Axis family} ($8$ vertices): all permutations of
    23	  $(\pm 1, 0, 0, 0)$;
    24	\item \textbf{Half-integer family} ($16$ vertices): all sign
    25	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    26	\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
    27	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
    28	  $\Ph^{2} = \Ph + 1$ identity, equivalently
    29	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
    30	\end{itemize}
    31	The total is $8 + 16 + 96 = 120$ unit vectors. These are coordinate
    32	families, not H$_4$ orbits: H$_4$ acts transitively on the full
    33	$120$-vertex set, so the three families lie in a single H$_4$
    34	orbit. Reproduced by \texttt{repro/verify\_kernel.py:build\_v600};
    35	the numerical check $\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms
    36	all vertices on $S^{3}$.
    37	
    38	The H$_4$ Coxeter group (order $14400$) acts transitively on the
    39	$120$ vertices. Every vertex therefore has \emph{identical} local
    40	structure under $H_{4}$; in particular, every vertex has the same
    41	degree in the short-edge graph defined below.
    42	
    43	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
    44	
    45	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
    46	Euclidean chord distance is
    47	\[
    48	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
    49	\]
    50	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
    51	if their inner product equals the canonical short-edge value
    52	\begin{equation}\label{eq:short_edge}
    53	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
    54	\end{equation}
    55	equivalently chord distance
    56	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
    57	nearest-neighbour adjacency on the canonical 600-cell embedding
    58	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
    59	
    60	\paragraph{Graph facts (forced by the construction).}
    61	The graph $G_{V_{600}}$ has:
    62	\begin{itemize}\itemsep=2pt
    63	\item $|V|=120$ vertices,
    64	\item $|E|=720$ edges,
    65	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
    66	  the vertex set forces \emph{uniformity} of the local structure;
    67	  the short-edge nearest-neighbour construction gives the
    68	  numerical degree $12$, verified by
    69	  \texttt{repro/verify\_kernel.py}),
    70	\item the graph is connected (verified numerically by counting
    71	  connected components of the short-edge adjacency matrix; the
    72	  classical 600-cell connectivity result is well known
    73	  in~\citep{CoxeterRegularPolytopes}).
    74	\end{itemize}
    75	All four facts are reproduced numerically:
    76	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
    77	degree-min/max $=12/12$ (uniform), and one connected component.
    78	
    79	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
    80	
    81	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
    82	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
    83	of constant inner product with $v_{0}$. The nine canonical inner
    84	products are
    85	\begin{equation}\label{eq:shell_inner}
    86	\langle v, v_{0}\rangle
    87	\;\in\;
    88	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
    89	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
    90	\end{equation}
    91	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
    92	antipode. The shell-size sequence is
    93	\begin{equation}\label{eq:shell_sizes}
    94	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
    95	\;=\;
    96	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
    97	\end{equation}
    98	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
    99	icosidodecahedral ring. The total is
   100	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
   101	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
   102	
   103	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
   104	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
   105	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
   106	
   107	\subsection{Inner-product check}\label{ssec:inner_product_check}
   108	
   109	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   110	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   111	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   112	vertex in shell $s_{2}$ if and only if their pairwise inner product
   113	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   114	adjacency types to those compatible with the H$_3$ orbit structure.
   115	The numerically constructed graph respects this: every edge has
   116	inner product exactly $\Ph/2$ within machine precision (tolerance
   117	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   118	
   119	\subsection{What the substrate fixes, and what it does not}
   120	
   121	\begin{itemize}\itemsep=2pt
   122	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   123	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   124	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   125	  Laplacian spectrum (\S\ref{sec:spectrum}).
   126	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   127	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   128	  (\S\ref{ssec:opnorm}); the operator-norm bound
   129	  $\|\Cph^{-1}\| = \Ph^{2}$.
   130	\item \textbf{Not fixed by this paper}: the choice of
   131	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
   132	  4-polytopes / Coxeter substrates. The 600-cell choice is
   133	  post-hoc motivated by the empirical landings
   134	  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
   135	  formal substrate ablation is an
   136	  open build (\S\ref{sec:limitations}).
   137	\end{itemize}

exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/04_spectrum.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/05_agreement.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/06_passive_witness.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/07_active_witness.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 168ms:
     1	% =====================================================================
     2	\section{Discrete-to-continuum agreement}\label{sec:agreement}
     3	% =====================================================================
     4	
     5	This is the central geometric diagnostic of the paper: the
     6	discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
     7	localised source has high per-vertex Pearson correlation in radial
     8	shape with the continuum kernel
     9	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
    10	the source. Pearson correlation is a shape similarity statistic, not
    11	an equality claim. We give the test, the numerical result, and a variant
    12	comparison in which the unweighted Laplacian ranks highest among
    13	the three tested variants (unweighted, $\Ph$-geometric weighted,
    14	$\Ph$-arithmetic weighted).
    15	
    16	\subsection{The test}\label{ssec:test}
    17	
    18	Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
    19	vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
    20	other entries zero). Compute
    21	\[
    22	\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
    23	\]
    24	by direct linear solve (no eigenmode truncation). For each vertex
    25	$v \in V$, compute the Euclidean chord distance
    26	$x(v) = \|v - v_{0}\|$ and the continuum prediction
    27	\[
    28	G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
    29	\]
    30	The agreement criterion is the Pearson correlation between
    31	$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
    32	source itself is excluded, since the discrete response there is
    33	trivially the diagonal of $\Cph^{-1}$ and the chord distance is
    34	zero, both degenerate for the comparison).
    35	
    36	\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
    37	
    38	\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
    39	\begin{itemize}\itemsep=2pt
    40	\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
    41	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
    42	  (averaging $\psi(v)$ over each H$_3$ shell first, then
    43	  correlating the $9$-point shell-mean trajectory with the
    44	  continuum prediction at the shell mean radius).
    45	\end{itemize}
    46	The two correlations measure the same fact at different
    47	resolutions and with different source-vertex conventions:
    48	\begin{itemize}\itemsep=2pt
    49	\item Per-vertex test: $|V|-1 = 119$ data points (every
    50	  non-source vertex), source $v_{0}$ \emph{excluded} (the discrete
    51	  response there is the diagonal of $\Cph^{-1}$ and the chord
    52	  distance is $0$, both degenerate for the comparison).
    53	\item Shell-mean test: $9$ data points (one per H$_3$ shell);
    54	  shell $0$ contains only the source vertex, so it is included
    55	  on the shell-mean side and contributes a single
    56	  ($\psi(v_{0}), G(0)$) point.
    57	\end{itemize}
    58	On the unweighted 600-cell graph with an H$_3$-fixed source,
    59	$\psi$ is shell-constant up to numerical precision — the
    60	within-shell standard deviations are at machine precision
    61	($\sim 10^{-16}$). The two tests therefore differ in weighting and
    62	source convention, not in noise content: the per-vertex test
    63	weights each shell by its multiplicity
    64	($\{12, 20, 12, 30, 12, 20, 12, 1\}$ for the non-source shells)
    65	and excludes the source vertex, while the shell-mean test gives
    66	equal weight to every shell and includes the source. The
    67	per-vertex test is the headline agreement criterion in this paper.
    68	
    69	\subsection{Variant comparison}\label{ssec:variant_comparison}
    70	
    71	Two $\Ph$-cocycle weighted Laplacian variants are tested as
    72	controls:
    73	
    74	\begin{itemize}\itemsep=2pt
    75	\item \textbf{$\Ph$-geometric weights}: edge weight
    76	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
    77	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
    78	  is the shell index of $v$.
    79	\item \textbf{$\Ph$-arithmetic weights}: edge weight
    80	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
    81	  $\omega_{+}$.
    82	\end{itemize}
    83	The weighted Laplacian is then
    84	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
    85	We re-run the discrete-to-continuum test on each variant.
    86	
    87	\begin{table}[ht]
    88	\centering
    89	\small
    90	\caption{Per-vertex and shell-mean Pearson correlations between the
    91	discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
    92	prediction $G(\|v - v_{0}\|)$ for three Laplacian variants.
    93	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
    94	\label{tab:variant_correlation}
    95	\begin{tabular}{l c c}
    96	\toprule
    97	Variant            & Per-vertex correlation & Shell-mean correlation \\
    98	\midrule
    99	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
   100	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
   101	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
   102	\bottomrule
   103	\end{tabular}
   104	\end{table}
   105	
   106	\textbf{Reading.} Among the three tested variants, the unweighted
   107	Laplacian ranks highest on both reported criteria
   108	($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
   109	This reproduces, on a different test, the qualitative ranking the
   110	b-anomaly paper~\citep{SmartBAnomaly2026} established
   111	independently against its data-$\chi^{2}$ criterion
   112	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
   113	b-anomaly numbers). Two independent criteria — geometry-only
   114	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
   115	agree on which Laplacian variant is preferred. We do not claim
   116	this is a uniqueness result; we report it as a two-criterion
   117	convergence (the b-anomaly paper's own caveat that the data was
   118	looked at first and the geometry criterion verified afterward is
   119	inherited verbatim).
   120	
   121	\subsection{What the agreement does and does not establish}
   122	
   123	\paragraph{Does establish.} A geometric agreement: the discrete
   124	response of a fixed-shift Green operator on a fixed graph behaves,
   125	to within the per-vertex Pearson correlation $0.976$, like the
   126	closed-form continuum exponential at the same length scale $\Ph$.
   127	This is a non-trivial agreement between two independently-defined
   128	objects: (i) the discrete inverse of a $120\times 120$
   129	Laplacian-plus-shift matrix; and (ii) a one-dimensional continuum
   130	exponential. The $\Ph$-mediated agreement is an empirical fact
   131	about the chosen substrate and shift, computed (not fitted) by
   132	the verification script.
   133	
   134	\paragraph{Does not establish.} Operator uniqueness on either
   135	empirical landing — the b-anomaly paper documents a free-width
   136	Gaussian alternative that fits comparably in $\chi^{2}$ at the
   137	cost of one extra shape parameter, and the aria-chess preprint
   138	does not run a substrate ablation; both caveats are inherited
   139	verbatim. The agreement also does not establish that
   140	$\Rsixhundred$ is the unique discrete substrate with this
   141	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   142	graphs would need to be tested on the same correlation criterion
   143	to make any comparative claim, and a formal substrate ablation is
   144	an open build (\S\ref{sec:limitations}).

 succeeded in 176ms:
     1	% =====================================================================
     2	\section{The Laplacian spectrum}\label{sec:spectrum}
     3	% =====================================================================
     4	
     5	The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
     6	numerically resolves into nine distinct eigenvalue classes whose
     7	values match the closed-form $\mathbb{Z}[\Ph]$ list given in
     8	Table~\ref{tab:spectrum} to machine precision; multiplicities sum
     9	to $|V| = 120$. The spectrum is computed numerically by
    10	\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
    11	$120\times 120$ symmetric eigendecomposition, deterministic at
    12	machine precision); the closed-form identification is made by
    13	algebraic recognition of the displayed values, not by an exact
    14	arithmetic derivation in this paper.
    15	
    16	\begin{table}[ht]
    17	\centering
    18	\small
    19	\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
    20	Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
    21	values returned by \texttt{repro/verify\_kernel.py}; multiplicities
    22	sum to $120$.}
    23	\label{tab:spectrum}
    24	\begin{tabular}{c c c}
    25	\toprule
    26	Closed-form eigenvalue & Numerical value & Multiplicity \\
    27	\midrule
    28	$0$            & $-3\!\times\!10^{-15}$ (machine zero) & $1$ \\
    29	$12 - 6\Ph$    & $2.2918$  & $4$ \\
    30	$12 - 4\Ph$    & $5.5279$  & $9$ \\
    31	$9$            & $9.0000$  & $16$ \\
    32	$12$           & $12.0000$ & $25$ \\
    33	$14$           & $14.0000$ & $36$ \\
    34	$4\Ph + 8$     & $14.4721$ & $9$ \\
    35	$15$           & $15.0000$ & $16$ \\
    36	$6\Ph + 6$     & $15.7082$ & $4$ \\
    37	\midrule
    38	\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
    39	\bottomrule
    40	\end{tabular}
    41	\end{table}
    42	
    43	\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
    44	\begin{align*}
    45	12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
    46	12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
    47	4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
    48	6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
    49	\end{align*}
    50	The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
    51	$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
    52	are conjugate under the Galois automorphism
    53	$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
    54	fixed-point eigenvalues $\{0, 9, 12, 14, 15\}$ are rational and
    55	have multiplicities $\{1, 16, 25, 36, 16\}$ (sum $94$); the
    56	$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.
    57	
    58	\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
    59	$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
    60	remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
    61	artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
    62	reformulation; that reading is not imported here. We report only
    63	that the spectrum has this structure.
    64	
    65	\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
    66	
    67	The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
    68	\[
    69	\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
    70	\;\approx\; 0.381966,
    71	\]
    72	and the operator-norm bound is
    73	\[
    74	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
    75	\]
    76	\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
    77	$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
    78	(predicted) — match to six decimal places. The largest eigenvalue
    79	of $\Cph$ is
    80	$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
    81	= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
    82	
    83	\subsection{H$_4$ irrep block decomposition (imported context)}
    84	\label{ssec:irrep}
    85	
    86	The eigenspaces of $\Lop$ partition into H$_4$-proper and
    87	$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
    88	exponents are $\{1, 11, 19, 29\}$; under the
    89	$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
    90	$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
    91	aria-chess companion's recurrent
    92	layer~\citep{SmartAriaChess2026} realises this block decomposition
    93	at machine precision and provides a spectrally clean
    94	H$_4$-equivariant basis there.
    95	
    96	This subsection is imported context from the aria-chess companion;
    97	the irrep block decomposition is \emph{not} verified by
    98	\texttt{repro/verify\_kernel.py} of this paper and is not used as
    99	a load-bearing fact for any operator-witness claim made here. We
   100	include the labelling for orientation only.

 succeeded in 188ms:
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
    15	kinematic range. The b-anomaly preprint tests a fixed
    16	$q^{2}$-dependent effective shift on top of the SM backend, of the
    17	form
    18	\begin{equation}\label{eq:banomaly_kernel}
    19	\Delta C_{9}^{\mathrm{eff}}(q^{2})
    20	\;=\;
    21	A \cdot \kappa_{V_{600}}(q^{2}),
    22	\end{equation}
    23	where $\kappa_{V_{600}}(q^{2})$ is the projection of $\Cph$ on
    24	$\Rsixhundred$ to the flavour-physics $q^{2}$ axis (the b-anomaly
    25	preprint's §3 projection construction, which we do not relitigate
    26	here; this is a projection of the operator, not a derivation of
    27	$\Ph^{-2}$), and $A$ is a single fitted dimensionless amplitude
    28	per dataset. The kernel shape $\kappa_{V_{600}}$ is positive on
    29	the LHCb $q^{2}$ window with the b-anomaly preprint's sign
    30	convention, so a positive fitted $A$ corresponds to a negative
    31	$\Delta C_{9}^{\mathrm{eff}}$. The kernel
    32	shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
    33	This is a \emph{structural} test: same fixed $\Cph$ on the same
    34	$\Rsixhundred$, no shape retuning between datasets.
    35	
    36	\subsection{The five-dataset structural fit}
    37	
    38	The b-anomaly preprint reports the following per-dataset table
    39	(verbatim from~\citep{SmartBAnomaly2026}, also at
    40	\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{b-anomaly five-dataset structural fit. Verbatim
    46	from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
    47	dataset, kernel shape held fixed.}
    48	\label{tab:banomaly}
    49	\begin{tabular}{l l r r r r}
    50	\toprule
    51	Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
    52	   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
    53	\midrule
    54	LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
    55	LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
    56	CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
    57	LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
    58	LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
    59	\bottomrule
    60	\end{tabular}
    61	\end{table}
    62	
    63	\subsection{What the structural fit establishes}
    64	
    65	\begin{itemize}\itemsep=2pt
    66	\item \textbf{Universality (5/5).} The same fixed kernel shape
    67	  can be fit to all five datasets with one amplitude $A$ per
    68	  dataset and no shape retuning. The kernel never moves between
    69	  datasets.
    70	\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
    71	  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
    72	  reproduces the established direction of the
    73	  anomaly~\citep{LHCbAngular2020} across all five independent
    74	  measurements.
    75	\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
    76	  $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with
    77	  the predicted Krüger--Matias $P$-basis vs $S$-basis amplification
    78	  ($\sim 2.2$~\citep{KrugerMatias2005}), with a residual
    79	  $\sim 50\%$ overshoot on top of the K--M prediction. The
    80	  b-anomaly preprint reports this residual as an open item, not
    81	  a discharge.
    82	\item \textbf{Geometry-first variant test.} Of three discrete
    83	  Laplacian variants on $\Rsixhundred$ (unweighted,
    84	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    85	  unweighted choice wins on both a pure-geometry criterion
    86	  (correlation $0.997$ with the continuum kernel, b-anomaly
    87	  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
    88	  ($\chi^{2}=13.555$). The two criteria agree on the variant
    89	  ranking — a two-criterion convergence on the same fixed
    90	  operator.
    91	\end{itemize}
    92	
    93	\subsection{What the structural fit does \emph{not} establish}
    94	
    95	The b-anomaly preprint is explicit about the following caveats,
    96	which we inherit verbatim:
    97	
    98	\begin{itemize}\itemsep=2pt
    99	\item \textbf{AIC tie on current data.} On Akaike model comparison,
   100	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
   101	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
   102	  indistinguishable: stacked AIC weights
   103	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   104	  Current data cannot resolve the model comparison. AIC is blind
   105	  to the universality / shape-prediction claim itself, but it is
   106	  decisive about whether the shape is forced by data: it is not.
   107	\item \textbf{Free-width Gaussian alternative.} A free-width
   108	  Gaussian charm-loop proxy fits the same five datasets comparably
   109	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   110	  is not the unique $q^{2}$ shape consistent with the anomaly.
   111	\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
   112	  earlier analysis the b-anomaly project calls ``Mode B''
   113	  (linearised) gave a stronger preference
   114	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   115	  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
   116	  between Mode B (linearised) and the non-linear refit is the
   117	  largest single methodological uncertainty in the b-anomaly
   118	  project.
   119	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   120	  preprint's limitations section acknowledges that the LHCb~2025
   121	  data was looked at first, and only later was the agreement of
   122	  the data-$\chi^{2}$ ranking with the pure-geometry ranking
   123	  verified. The two-criterion agreement is criterion-independent
   124	  but not historically blind.
   125	\end{itemize}
   126	
   127	\subsection{Reading at the operator level}
   128	
   129	The b-anomaly result is the \emph{passive-regime} empirical
   130	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   131	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   132	fixed discrete-to-momentum projection, gives a sign-uniform
   133	description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
   134	five independent measurements without shape retuning. This does
   135	not establish the kernel as theorem-grade physics on the flavour
   136	side (the AIC tie, the free-width Gaussian alternative, and the
   137	Mode-B linearised-vs-nonlinear refit drift prevent that). It does
   138	establish, at the operator level, that the same fixed $\Cph$ on
   139	the same fixed $\Rsixhundred$ is consistent with one of two
   140	independent empirical landings without parameter retuning. The
   141	second landing is in \S\ref{sec:active_witness}.

 succeeded in 178ms:
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
    28	  low-amplitude tonic noise for PROPOFOL). These are
    29	  biologically-motivated design choices, not measurement-fits to
    30	  subject-level EEG data.
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
    68	  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
    69	  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
    70	  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
    71	  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
    72	  intervals do not overlap each other; the WAKE interval is the
    73	  pairwise common ground).
    74	\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
    75	  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
    76	\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
    77	  wake (threshold $\in [1.5, 5.0]$, empirical reference
    78	  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
    79	\item \textbf{Propofol continuity drop}: $+0.066$
    80	  (threshold $> 0.020$).
    81	\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
    82	  direction confirmed; $\Phi$-proxy not full IIT).
    83	\item \textbf{Recovery deterministic identity to wake}: under the
    84	  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
    85	  to the WAKE trajectory.
    86	\end{itemize}
    87	
    88	\subsection{Cross-domain selectivity}
    89	
    90	\begin{itemize}\itemsep=2pt
    91	\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
    92	  positions across $4$ categories on $8$-D V2 features; substrate
    93	  routing lifts leave-one-out classification at canonical depth
    94	  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
    95	  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
    96	\item \textbf{Conversation pattern recognition (P14--P16)}:
    97	  $64$ utterances, $8$ categories; raw classification $87.5\%$,
    98	  substrate-routed lift $-4.4$pp (within the preregistered
    99	  neutrality band $|\cdot| < 10$pp). The substrate is selectively
   100	  amplifying in tasks where raw features are ambiguous and
   101	  approximately neutral when raw features are already
   102	  discriminative.
   103	\item \textbf{HCP brain functional connectivity (P17--P18)}:
   104	  full-cohort descriptive statistics on $n=1003$ subjects show
   105	  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
   106	  homogeneity, $+79.78\sigma$ on raw participation ratio (with
   107	  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
   108	  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
   109	  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
   110	  deviations below the HCP biological cohort.
   111	\end{itemize}
   112	
   113	\subsection{Reading at the operator level}
   114	
   115	The aria-chess result is the \emph{active-regime} empirical
   116	witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
   117	layer above $\Cph$ uses one condition-dependent coupling and one
   118	substrate-pinned nonlinearity at the graph's average degree
   119	$k=12$; no other \emph{kernel-shape} parameter enters. Above the
   120	operator, aria-chess inherits its own dynamical and stimulus
   121	constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
   122	condition-specific biologically-motivated stimulus models); these
   123	are documented in the aria-chess preprint and are not retuned in
   124	this paper. The kernel shift $\Ph^{-2}$ is not retuned between
   125	b-anomaly and aria-chess. Under those design choices, the same
   126	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
   127	preregistered cortical correspondences (frozen 2026-04-18) and six
   128	literature-thresholded EEG drug/sleep signatures.
   129	
   130	The aria-chess preprint stays inside substrate-witness scope: it
   131	does not claim the substrate \emph{is} consciousness, does not
   132	claim 600-cell uniqueness among regular 4-polytopes, and does not
   133	deliver a selection theorem on the ACT 4-tuple. We inherit the
   134	scope verbatim. What we add at the operator level is the
   135	observation that the same fixed $\Cph$ — under no shape-parameter
   136	retuning between regimes — is the load-bearing object on both
   137	empirical landings.
   138	
   139	\subsection{Two-witness structure}
   140	
   141	\begin{table}[ht]
   142	\centering
   143	\small
   144	\caption{Two independent empirical landings of $\Cph$ on
   145	$\Rsixhundred$, with no shape retuning between regimes.}
   146	\label{tab:two_witness}
   147	\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
   148	\toprule
   149	& Passive regime & Active regime \\
   150	\midrule
   151	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   152	Domain             & flavour physics                    & cortical neuroscience \\
   153	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   154	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   155	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   156	Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
   157	Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
   158	Kernel-shape free params & 0                            & 0 \\
   159	Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
   160	Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
   161	\bottomrule
   162	\end{tabular}
   163	\end{table}
   164	
   165	The two witnesses share, by design, exactly the geometry-fixed
   166	operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
   167	the same shift $\Ph^{-2}$. They share no fitted parameter,
   168	threshold, dataset, or methodological choice above the operator
   169	level. The b-anomaly amplitude $A$ is fitted to flavour-physics
   170	$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
   171	is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
   172	neural data; the v4 stimulus protocols are biologically motivated,
   173	not subject-fit. Independence in this paper is independence at
   174	the empirical layer above the shared operator.

exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/08_programme_home.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/09_limitations.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/sections/10_conclusion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 272ms:
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
    20	\item \textbf{RH polynomial filter} (forthcoming RH artifact in
    21	  this programme). Cascade closure functional on $\mathbb{R}^{120}$:
    22	  $F_{\mathrm{filt}}(x) = \tfrac12 \langle x, p_{\mathrm{fix}}(L)^{2} x\rangle$
    23	  with $\Psi_{t} = e^{-t\, p_{\mathrm{fix}}(L)^{2}}$. Programme-positioned
    24	  as the $\sigma$-fix-annihilator instance of the family: a
    25	  degree-$10$ positive functional vanishing exactly on
    26	  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
    27	  any claim made in this paper.
    28	\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
    29	  this programme). Discrete cascade gap Hamiltonian,
    30	  programme-positioned as a $\Cph$-style mass-regularised Laplacian
    31	  on $\Rsixhundred$. The artifact itself is not load-bearing for
    32	  any claim made in this paper.
    33	\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
    34	  The homeostatic regulariser
    35	  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
    36	  programme-positioned as a member of the same polynomial-in-$L$
    37	  family.
    38	\end{itemize}
    39	
    40	We list the family-membership claim as \emph{programme-positioned},
    41	not formally proved. Each named operator is in a
    42	polynomial-in-$L$ form with positivity and self-adjointness
    43	properties matching the family description; we do not claim a
    44	formal classification theorem identifying the family.
    45	
    46	\subsection{Response vs selection}
    47	
    48	The closure response $\psi = \Cph^{-1} f$ is determined by the
    49	chosen substrate plus the design-level shift: $\Cph$ is fixed by
    50	the substrate $\Rsixhundred$ and the design-level choice
    51	$\Ph^{-2}$, and the response is the resulting linear inverse.
    52	This is a \emph{response} primitive. It does \emph{not} answer:
    53	\begin{itemize}\itemsep=2pt
    54	\item Why this substrate? (Selection across regular 4-polytopes
    55	  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
    56	\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
    57	  positive constant.)
    58	\item How does the system pick a response configuration over
    59	  time? (Crystallisation / Lyapunov descent dynamics on a
    60	  $W$-trajectory.)
    61	\end{itemize}
    62	
    63	The selection layer is open. It appears as an open hypothesis in
    64	three independent frames:
    65	\begin{enumerate}\itemsep=2pt
    66	\item \textbf{Forthcoming RH artifact}: the closure-flow suppression
    67	  hypothesis $\textup{H}_{\mathrm{attr}}$ at the level of the
    68	  original cascade closure functional. The polynomial filter
    69	  $\Psi_{t}$ is a finite-dimensional analogue, by design.
    70	\item \textbf{Adaptive Closure
    71	  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
    72	  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
    73	  $V(W)$ on the reduced flow, an edge-space decomposition under
    74	  $2I$-equivariance, and a full reduced-flow convergence theorem
    75	  on $W$-trajectories — \emph{none delivered} in that paper.
    76	\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
    77	  the substrate-witness scope explicitly does \emph{not} deliver
    78	  a selection theorem; ACT is positioned as the future
    79	  selection-theorem witness.
    80	\end{enumerate}
    81	
    82	The recurrence of an open selection gap across these three frames
    83	is a programme-level reading: the gap may be a single mathematical
    84	problem rather than three independent ones, but the present paper
    85	gives no proof of equivalence. The two empirical witnesses landed
    86	in this paper strengthen external confidence in the \emph{response}
    87	primitive without reducing or addressing the selection gap.
    88	
    89	\subsection{What this paper closes vs leaves open}
    90	
    91	\paragraph{Closes (at the operator-witness level).}
    92	\begin{itemize}\itemsep=2pt
    93	\item The operator $\Cph$ is well-defined and positive definite
    94	  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
    95	  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
    96	  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
    97	  with the standard combinatorial Laplacian). On substrates where
    98	  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
    99	  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
   100	  generally strict (\S\ref{sec:definition}).
   101	\item The 600-cell instance $\Rsixhundred$ has the construction
   102	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
   103	  Table~\ref{tab:spectrum}, both reproduced numerically
   104	  (\texttt{repro/verify\_kernel.py}).
   105	\item Discrete-to-continuum agreement at per-vertex Pearson
   106	  correlation $0.976$ on the unweighted variant, with the unweighted
   107	  variant winning the geometry-only criterion against two
   108	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
   109	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
   110	  the load-bearing object in two independent empirical works in
   111	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
   112	  \S\ref{sec:active_witness}).
   113	\end{itemize}
   114	
   115	\paragraph{Leaves open.}
   116	\begin{itemize}\itemsep=2pt
   117	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
   118	  as a design-level shift; not derived from a closure functional
   119	  or symmetry argument.
   120	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
   121	  post-hoc motivated by the empirical landings; alternative regular
   122	  4-polytopes are an explicit ablation build, not a discharged
   123	  comparison.
   124	\item \emph{Kernel-uniqueness on either empirical landing.} The
   125	  b-anomaly free-width Gaussian alternative (fits comparably with
   126	  one extra shape parameter) and the AIC tie
   127	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
   128	  inherited verbatim from~\citep{SmartBAnomaly2026}.
   129	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
   130	  decomposition under $2I$-equivariance, full reduced-flow
   131	  convergence — all explicitly not delivered
   132	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   133	  here.
   134	\item \emph{Family-membership theorem.} The programme-home
   135	  positioning of cascade Lyapunov functionals as members of the
   136	  same polynomial-in-$L$ family is reported as
   137	  \emph{programme-positioned}, not formally classified.
   138	\end{itemize}

 succeeded in 253ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
     6	600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
     7	geometry-fixed response primitive: positive definite under
     8	(H1)--(H3) on the substrate $(M, L_M)$, and on the connected
     9	finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
    10	smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
    11	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
    12	$\lambda_{\min}(L_M) > 0$ give the strict inequality
    13	$\|\Cph^{-1}\| < \Ph^{2}$).
    14	The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
    15	$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
    16	Laplacian spectrum that numerically resolves to the closed-form
    17	$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
    18	discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
    19	the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
    20	chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
    21	the unweighted Laplacian, above the two $\Ph$-cocycle weighted
    22	variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
    23	generators by \texttt{repro/verify\_kernel.py}; no parameter is
    24	fitted.
    25	
    26	\textbf{Two independent empirical landings.} The same fixed
    27	$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
    28	retuning between regimes, appears as the load-bearing object in:
    29	\begin{enumerate}\itemsep=2pt
    30	\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
    31	  fitted dimensionless amplitude $A$ per dataset (kernel shape
    32	  held fixed) gives a sign-uniform
    33	  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
    34	  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
    35	  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
    36	  $B_s\to\phi$).
    37	\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
    38	  recurrent self-model layer above the same operator (one
    39	  condition-dependent self-injection coupling
    40	  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
    41	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    42	  degree) passes eighteen preregistered cortical correspondences
    43	  (frozen 2026-04-18) and six drug/sleep EEG signatures.
    44	\end{enumerate}
    45	By design, the two witnesses share exactly the geometry-fixed
    46	operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
    47	$\Ph^{-2}$. Above that operator level, they share no fitted
    48	parameter, threshold, or dataset, and the empirical claims are
    49	tested on disjoint physical domains (flavour physics vs cortical
    50	neuroscience). Independence here is
    51	independence at the empirical layer above the shared operator,
    52	not statistical independence of the operator itself.
    53	
    54	\textbf{Operator-witness scope.} This is an operator witness, not
    55	a derivation of physics on either landing. We do not derive the
    56	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
    57	claim 600-cell uniqueness; alternative regular 4-polytopes are an
    58	explicit ablation build. We do not claim kernel uniqueness on
    59	either empirical landing; the b-anomaly's free-width Gaussian
    60	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
    61	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
    62	aria-chess substrate-witness scope is inherited verbatim. We do
    63	not deliver a selection theorem on the ACT
    64	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
    65	open builds (Lyapunov $V(W)$, edge-space decomposition under
    66	$2I$-equivariance, full reduced-flow convergence) remain open and
    67	are not delivered here.
    68	
    69	\textbf{Programme position.} The cascade-programme home for the
    70	polynomial-in-$L$ Lyapunov family — RH polynomial filter
    71	($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
    72	cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
    73	identified in \S\ref{sec:programme_home}. Family-membership is
    74	\emph{programme-positioned}, not formally classified. The two
    75	empirical landings strengthen external confidence in the
    76	\emph{response} primitive without reducing or addressing the
    77	selection gap.
    78	
    79	We have not found, in the standard arXiv categories we routinely
    80	follow, a prior preprint that simultaneously names a
    81	geometry-fixed Green operator on a fixed Coxeter graph, with a
    82	design-level mass shift not retuned between regimes, and threads
    83	two independent empirical landings on qualitatively distinct
    84	physical domains. This is a non-systematic literature observation,
    85	not a search-protocol prior-art claim; we cannot rule out that
    86	such prior work exists.
    87	The empirical material gathered here is the operator witness; the
    88	broader programme to convert the witness into a selection-theorem-
    89	grade claim is sketched in the companion preprints and remains
    90	the natural next step.

 succeeded in 263ms:
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
   122	\textbf{Discrete-to-continuum correlation reported on a single pole,
   123	verified across all $|V|$.} The headline per-vertex correlation
   124	$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
   125	source. H$_4$ transitivity predicts the correlation is invariant
   126	under choice of source vertex. \texttt{repro/verify\_kernel.py}
   127	sweeps over all $120$ vertices: every source returns the same
   128	per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
   129	(\texttt{multi\_source\_sweep.max\_minus\_min} in
   130	\texttt{results.json}). The single-pole headline is therefore a
   131	representative, not a sample, of the operator's behaviour under
   132	H$_4$ transitivity.
   133	
   134	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   135	
   136	\textbf{Selection layer not delivered.} As enumerated in
   137	\S\ref{sec:programme_home}, the selection-layer constructions
   138	(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
   139	full reduced-flow convergence) are open in the companion ACT
   140	preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
   141	delivered here. The two empirical witnesses strengthen confidence
   142	in the response primitive without addressing the selection gap.
   143	
   144	\textbf{No deuteron / hadron / RH / capstone material is loaded
   145	into this paper.} The cascade-derivation programme, the capstone
   146	coalgebra paper, and the Millennium drafts share operator-level
   147	infrastructure with this paper but are not load-bearing here.
   148	Deliberately out of scope.
   149	
   150	\textbf{Out-of-scope items NOT delivered (correctly).}
   151	\begin{itemize}\itemsep=2pt
   152	\item Lyapunov function $V(W)$ on the reduced flow — open build
   153	  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
   154	\item $2I$-equivariance audit of the closure operator family —
   155	  open build of ACT.
   156	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   157	  Hodge edge Laplacian — open build of ACT.
   158	\item Selection theorem identifying $\Rsixhundred$ over alternative
   159	  regular 4-polytopes — see \S\ref{ssec:regime}.
   160	\item Formal discrete-to-continuum convergence theorem under a
   161	  specified large-graph limit — see \S\ref{ssec:interpretation}.
   162	\item First-principles derivation of the $\Ph^{-2}$ shift — see
   163	  \S\ref{ssec:posthoc}.
   164	\item Family-membership classification theorem for the
   165	  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
   166	\end{itemize}
   167	
   168	\subsection{The honest verdict}
   169	
   170	The result is an \emph{operator witness}: a geometry-fixed response
   171	operator on a fixed graph, with no shape parameters tuned to any
   172	dataset, is consistent with two independent empirical landings in
   173	qualitatively distinct regimes. We do not claim the operator is
   174	the unique kernel for either landing. We do not claim selection is
   175	delivered. We do not claim 600-cell uniqueness. The strengthening
   176	builds for stronger claims are listed above and remain open.

 succeeded in 325ms:
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
    18	% Companion VFD preprints (the two empirical witnesses + selection-layer paper).
    19	
    20	@unpublished{SmartBAnomaly2026,
    21	  author = {Smart, Lee},
    22	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
    23	            angular anomaly: sign-uniform cross-dataset and cross-channel fit},
    24	  year   = {2026},
    25	  note   = {VFD preprint}
    26	}
    27	
    28	@unpublished{SmartAriaChess2026,
    29	  author = {Smart, Lee},
    30	  title  = {A geometry-fixed substrate witness for cortical signatures:
    31	            eighteen preregistered correspondences and six drug/sleep EEG
    32	            signatures from the 600-cell under H$_4$ Coxeter symmetry},
    33	  year   = {2026},
    34	  note   = {VFD preprint, papers/aria-chess-paper/}
    35	}
    36	
    37	@unpublished{SmartAdaptiveClosureTransport2026,
    38	  author = {Smart, Lee},
    39	  title  = {Adaptive Closure Transport: a 4-tuple bridge
    40	            $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to
    41	            selection},
    42	  year   = {2026},
    43	  note   = {VFD preprint, papers/adaptive-closure-transport/}
    44	}
    45	
    46	% External flavour-physics literature (b-anomaly context, cited in §6).
    47	
    48	@article{KrugerMatias2005,
    49	  author  = {Kr\"uger, Frank and Matias, Joaquim},
    50	  title   = {Probing new physics via the transverse amplitudes of
    51	             $B^0 \to K^{*0} (\to K^- \pi^+) l^+ l^-$ at low recoil},
    52	  journal = {Phys. Rev. D},
    53	  volume  = {71},
    54	  pages   = {094009},
    55	  year    = {2005},
    56	  doi     = {10.1103/PhysRevD.71.094009}
    57	}
    58	
    59	@article{LHCbAngular2020,
    60	  author  = {{LHCb Collaboration}},
    61	  title   = {Measurement of $\mathit{CP}$-averaged observables in the
    62	             $B^0 \to K^{*0} \mu^+ \mu^-$ decay},
    63	  journal = {Phys. Rev. Lett.},
    64	  volume  = {125},
    65	  pages   = {011802},
    66	  year    = {2020},
    67	  doi     = {10.1103/PhysRevLett.125.011802}
    68	}

codex
The paper is unusually explicit about scope boundaries, but I’m already tracking a few places where wording likely exceeds what the local verification actually proves: especially “same operator” across the inherited empirical papers and one continuum-operator hypothesis statement. Next I’m checking `results.json`, the verification script, and the two source documents for exact provenance.
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/repro/results.json"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-closure-kernel/repro/verify_kernel.py"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "docs/aria-closure-kernel.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 313ms:
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
    11	  "connectivity": {
    12	    "n_connected_components": 1,
    13	    "connected": true
    14	  },
    15	  "shell_sizes": {
    16	    "0": 1,
    17	    "1": 12,
    18	    "2": 20,
    19	    "3": 12,
    20	    "4": 30,
    21	    "5": 12,
    22	    "6": 20,
    23	    "7": 12,
    24	    "8": 1
    25	  },
    26	  "shell_inner_products": [
    27	    1.0,
    28	    0.8090169943749475,
    29	    0.5,
    30	    0.3090169943749474,
    31	    0.0,
    32	    -0.3090169943749474,
    33	    -0.5,
    34	    -0.8090169943749475,
    35	    -1.0
    36	  ],
    37	  "antipodal_check": {
    38	    "pole_idx": 119,
    39	    "antipode_idx": 0,
    40	    "expected_shell_8_size": 1,
    41	    "observed_shell_8_size": 1
    42	  },
    43	  "laplacian_spectrum_grouped": [
    44	    {
    45	      "eigenvalue": -0.0,
    46	      "multiplicity": 1
    47	    },
    48	    {
    49	      "eigenvalue": 2.291796067500629,
    50	      "multiplicity": 4
    51	    },
    52	    {
    53	      "eigenvalue": 5.527864045000407,
    54	      "multiplicity": 9
    55	    },
    56	    {
    57	      "eigenvalue": 8.999999999999993,
    58	      "multiplicity": 16
    59	    },
    60	    {
    61	      "eigenvalue": 11.999999999999984,
    62	      "multiplicity": 25
    63	    },
    64	    {
    65	      "eigenvalue": 13.999999999999977,
    66	      "multiplicity": 36
    67	    },
    68	    {
    69	      "eigenvalue": 14.472135954999567,
    70	      "multiplicity": 9
    71	    },
    72	    {
    73	      "eigenvalue": 14.999999999999988,
    74	      "multiplicity": 16
    75	    },
    76	    {
    77	      "eigenvalue": 15.708203932499362,
    78	      "multiplicity": 4
    79	    }
    80	  ],
    81	  "operator_norm": {
    82	    "lambda_min_L": -1.01103545984405e-15,
    83	    "lambda_min_C_phi": 0.3819660112501041,
    84	    "operator_norm_C_phi_inv": 2.618033988749902,
    85	    "predicted_phi_squared": 2.618033988749895
    86	  },
    87	  "discrete_continuum_test": {
    88	    "shell_radii": [
    89	      0.0,
    90	      0.6180339887498948,
    91	      1.0,
    92	      1.1755705045849465,
    93	      1.4142135623730947,
    94	      1.618033988749895,
    95	      1.7320508075688772,
    96	      1.902113032590307,
    97	      2.0
    98	    ],
    99	    "shell_count": [
   100	      1,
   101	      12,
   102	      20,
   103	      12,
   104	      30,
   105	      12,
   106	      20,
   107	      12,
   108	      1
   109	    ],
   110	    "shell_psi_mean": [
   111	      0.11466009151487011,
   112	      0.034976446331995696,
   113	      0.024335208435661275,
   114	      0.021858804323929084,
   115	      0.019268782150762213,
   116	      0.01765857292134354,
   117	      0.016902552852001883,
   118	      0.015932370381507646,
   119	      0.01544087945358437
   120	    ],
   121	    "continuum_prediction": [
   122	      0.8090169943749475,
   123	      0.5521688638304681,
   124	      0.43606265394423777,
   125	      0.3912228691703586,
   126	      0.33757505628626344,
   127	      0.29762071978885557,
   128	      0.2773703603621507,
   129	      0.24969730865080123,
   130	      0.23503911473677247
   131	    ],
   132	    "pearson_correlation": 0.9232082699765517
   133	  },
   134	  "variant_correlation": {
   135	    "UNWEIGHTED": {
   136	      "shell_mean_correlation": 0.9232082699765517,
   137	      "per_vertex_correlation": 0.9762022978516623
   138	    },
   139	    "PHI_GEOMETRIC": {
   140	      "shell_mean_correlation": 0.879553132802029,
   141	      "per_vertex_correlation": 0.8883800503732451
   142	    },
   143	    "PHI_ARITHMETIC": {
   144	      "shell_mean_correlation": 0.8784315463215415,
   145	      "per_vertex_correlation": 0.8843640031310793
   146	    }
   147	  },
   148	  "multi_source_sweep": {
   149	    "n_sources": 120,
   150	    "min_correlation": 0.9762022978516617,
   151	    "mean_correlation": 0.9762022978516628,
   152	    "max_correlation": 0.9762022978516637,
   153	    "max_minus_min": 1.9984014443252818e-15
   154	  }
   155	}

 succeeded in 288ms:
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

 succeeded in 303ms:
     1	#!/usr/bin/env python3
     2	"""
     3	Aria closure kernel — numerical verification.
     4	
     5	Constructs V_600 from canonical generators, builds the short-edge
     6	nearest-neighbour graph, computes the Laplacian spectrum, builds
     7	C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
     8	test as a per-vertex Pearson correlation between psi(v) and
     9	(phi/2) exp(-|x|/phi) at each non-source vertex's chord radius
    10	(plus a shell-mean cross-check), tests the unweighted vs
    11	phi-cocycle-weighted Laplacian variants on the same geometry-only
    12	correlation criterion, sweeps the per-vertex correlation across
    13	all 120 source vertices to verify H_4 transitivity, checks
    14	graph connectedness, and writes results.json.
    15	
    16	All constants (phi, the 600-cell vertex generators, the short-edge
    17	inner product phi/2) are mathematically determined by the choice of
    18	substrate; no parameter is fitted to any dataset.
    19	
    20	Determinism: numpy RNG is seeded only for the localised-source
    21	positions (seed 42); the eigendecomposition is deterministic.
    22	
    23	Run: python3 verify_kernel.py
    24	"""
    25	
    26	from __future__ import annotations
    27	
    28	import json
    29	import itertools
    30	import math
    31	from pathlib import Path
    32	
    33	import numpy as np
    34	from numpy.linalg import eigh, norm
    35	from scipy.spatial.distance import pdist, squareform
    36	from scipy.sparse import csr_matrix
    37	from scipy.sparse.csgraph import connected_components
    38	
    39	
    40	PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
    41	INV_PHI = 1.0 / PHI                          # = phi - 1
    42	INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966
    43	
    44	
    45	# ---------------------------------------------------------------------------
    46	# 1. 600-cell vertex construction (120 vertices on S^3)
    47	# ---------------------------------------------------------------------------
    48	
    49	def even_perms(seq):
    50	    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    51	    n = len(seq)
    52	    out = []
    53	    for p in itertools.permutations(range(n)):
    54	        # signature
    55	        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    56	        if inv % 2 == 0:
    57	            out.append(tuple(seq[p[i]] for i in range(n)))
    58	    return out
    59	
    60	
    61	def build_v600():
    62	    """
    63	    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.
    64	
    65	    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    66	    - 16 vertices: all sign combinations of (+/- 1/2)^4
    67	    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
    68	      with all sign assignments
    69	    """
    70	    verts = set()
    71	
    72	    # 8 axis vertices
    73	    for sign in (-1, 1):
    74	        for i in range(4):
    75	            v = [0.0] * 4
    76	            v[i] = float(sign)
    77	            verts.add(tuple(v))
    78	
    79	    # 16 half-integer vertices
    80	    for signs in itertools.product((-1, 1), repeat=4):
    81	        v = tuple(0.5 * s for s in signs)
    82	        verts.add(v)
    83	
    84	    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    85	    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    86	    for signs in itertools.product((-1, 1), repeat=4):
    87	        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
    88	        signed = tuple(s * b for s, b in zip(signs, base))
    89	        for p in even_perms(signed):
    90	            verts.add(p)
    91	
    92	    V = np.array(sorted(verts), dtype=np.float64)
    93	    # Sanity check: all on the unit 3-sphere
    94	    radii = np.linalg.norm(V, axis=1)
    95	    assert np.allclose(radii, 1.0, atol=1e-10), \
    96	        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    97	    return V
    98	
    99	
   100	# ---------------------------------------------------------------------------
   101	# 2. Short-edge nearest-neighbour graph
   102	# ---------------------------------------------------------------------------
   103	
   104	def build_short_edge_graph(V, tol=1e-10):
   105	    """
   106	    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
   107	    criterion on the unit 3-sphere). For the 600-cell this gives a
   108	    12-regular graph on 120 vertices with 720 edges.
   109	    """
   110	    G = V @ V.T  # Gram matrix of inner products
   111	    short = PHI / 2.0
   112	    A = (np.abs(G - short) < tol).astype(np.float64)
   113	    np.fill_diagonal(A, 0.0)  # no self-loops
   114	    return A
   115	
   116	
   117	# ---------------------------------------------------------------------------
   118	# 3. Laplacian spectrum
   119	# ---------------------------------------------------------------------------
   120	
   121	def laplacian_spectrum(A):
   122	    """L = D - A; return sorted eigenvalues + eigenvectors."""
   123	    D = np.diag(A.sum(axis=1))
   124	    L = D - A
   125	    w, U = eigh(L)  # ascending order
   126	    return L, w, U
   127	
   128	
   129	def round_spectrum(w, decimals=6):
   130	    """Group eigenvalues into multiplicity classes (within numerical tol)."""
   131	    classes = []
   132	    seen = []
   133	    for val in w:
   134	        placed = False
   135	        for idx, ref in enumerate(seen):
   136	            if abs(val - ref) < 10 ** (-decimals):
   137	                classes[idx] = (ref, classes[idx][1] + 1)
   138	                placed = True
   139	                break
   140	        if not placed:
   141	            seen.append(val)
   142	            classes.append((round(float(val), decimals), 1))
   143	    return classes
   144	
   145	
   146	# ---------------------------------------------------------------------------
   147	# 4. Closure operator and discrete Green's function
   148	# ---------------------------------------------------------------------------
   149	
   150	def build_C_phi(L):
   151	    """C_phi = L + phi^-2 I."""
   152	    return L + INV_PHI2 * np.eye(L.shape[0])
   153	
   154	
   155	def green_response(C_phi, source_idx):
   156	    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
   157	    n = C_phi.shape[0]
   158	    f = np.zeros(n)
   159	    f[source_idx] = 1.0
   160	    psi = np.linalg.solve(C_phi, f)
   161	    return psi
   162	
   163	
   164	# ---------------------------------------------------------------------------
   165	# 5. Shell decomposition (9-shell H_3 partition)
   166	# ---------------------------------------------------------------------------
   167	
   168	def shell_indices(V, pole_idx):
   169	    """
   170	    Group vertices by their inner product with V[pole_idx]. The 600-cell's
   171	    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
   172	    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
   173	    """
   174	    pole = V[pole_idx]
   175	    inner = V @ pole
   176	    # The 9 canonical inner-product values:
   177	    canonical = np.array([
   178	        1.0,                # shell 0: pole itself
   179	        PHI / 2.0,          # shell 1
   180	        0.5,                # shell 2
   181	        1.0 / (2.0 * PHI),  # shell 3
   182	        0.0,                # shell 4 (equator)
   183	        -1.0 / (2.0 * PHI), # shell 5
   184	        -0.5,               # shell 6
   185	        -PHI / 2.0,         # shell 7
   186	        -1.0,               # shell 8: antipode
   187	    ])
   188	    shells = {k: [] for k in range(9)}
   189	    for i, val in enumerate(inner):
   190	        # snap to nearest canonical
   191	        k = int(np.argmin(np.abs(canonical - val)))
   192	        shells[k].append(i)
   193	    sizes = {k: len(shells[k]) for k in shells}
   194	    return shells, sizes, canonical
   195	
   196	
   197	# ---------------------------------------------------------------------------
   198	# 6. Discrete <-> continuum agreement test
   199	# ---------------------------------------------------------------------------
   200	
   201	def discrete_continuum_test(V, C_phi, source_idx):
   202	    """
   203	    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
   204	    shell radial coordinate x is the chord distance |v - v_source|. The
   205	    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).
   206	
   207	    Returns the per-shell discrete mean, the continuum prediction at each
   208	    shell radius, and the Pearson correlation between them.
   209	    """
   210	    psi = green_response(C_phi, source_idx)
   211	    shells, sizes, _ = shell_indices(V, source_idx)
   212	    pole = V[source_idx]
   213	
   214	    shell_means = []
   215	    shell_radii = []
   216	    shell_count = []
   217	    for k in range(9):
   218	        idxs = shells[k]
   219	        if not idxs:
   220	            continue
   221	        mean_psi = float(np.mean(psi[idxs]))
   222	        # mean chord radius from pole
   223	        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
   224	        shell_means.append(mean_psi)
   225	        shell_radii.append(chord)
   226	        shell_count.append(len(idxs))
   227	
   228	    shell_means = np.array(shell_means)
   229	    shell_radii = np.array(shell_radii)
   230	    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)
   231	
   232	    # Pearson correlation of (discrete shell mean) with (continuum prediction)
   233	    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
   234	        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
   235	    else:
   236	        corr = float("nan")
   237	
   238	    return {
   239	        "shell_radii": shell_radii.tolist(),
   240	        "shell_count": shell_count,
   241	        "shell_psi_mean": shell_means.tolist(),
   242	        "continuum_prediction": continuum.tolist(),
   243	        "pearson_correlation": corr,
   244	    }
   245	
   246	
   247	# ---------------------------------------------------------------------------
   248	# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
   249	# ---------------------------------------------------------------------------
   250	
   251	def cocycle_weights(V, source_idx):
   252	    """
   253	    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
   254	    the shell index of v with respect to a chosen pole. For the variant
   255	    test we compare the unweighted graph Laplacian to two weighted variants
   256	    discussed in the b-anomaly paper.
   257	    """
   258	    shells, _, _ = shell_indices(V, source_idx)
   259	    kappa = np.zeros(V.shape[0])
   260	    for k, idxs in shells.items():
   261	        for i in idxs:
   262	            kappa[i] = float(k)
   263	    return PHI ** kappa
   264	
   265	
   266	def weighted_laplacian(A, weights, mode="geometric"):
   267	    """
   268	    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
   269	    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
   270	    """
   271	    n = A.shape[0]
   272	    if mode == "geometric":
   273	        W = np.sqrt(np.outer(weights, weights))
   274	    elif mode == "arithmetic":
   275	        W = 0.5 * (weights[:, None] + weights[None, :])
   276	    else:
   277	        raise ValueError(mode)
   278	    A_w = A * W
   279	    D_w = np.diag(A_w.sum(axis=1))
   280	    return D_w - A_w
   281	
   282	
   283	def variant_correlation(V, A, source_idx, variant):
   284	    if variant == "UNWEIGHTED":
   285	        L_v = np.diag(A.sum(axis=1)) - A
   286	    else:
   287	        weights = cocycle_weights(V, source_idx)
   288	        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
   289	        L_v = weighted_laplacian(A, weights, mode=mode)
   290	    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
   291	    test = discrete_continuum_test(V, C_v, source_idx)
   292	    psi = green_response(C_v, source_idx)
   293	    pole = V[source_idx]
   294	    chord = np.linalg.norm(V - pole, axis=1)
   295	    # Continuum kernel at each vertex's chord radius
   296	    cont = (PHI / 2.0) * np.exp(-chord / PHI)
   297	    # Per-vertex correlation (excluding the source itself, which is degenerate)
   298	    mask = np.arange(V.shape[0]) != source_idx
   299	    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
   300	        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   301	    else:
   302	        per_vertex_corr = float("nan")
   303	    return {
   304	        "shell_mean_correlation": test["pearson_correlation"],
   305	        "per_vertex_correlation": per_vertex_corr,
   306	        "test": test,
   307	    }
   308	
   309	
   310	# ---------------------------------------------------------------------------
   311	# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
   312	# ---------------------------------------------------------------------------
   313	
   314	def connectivity_check(A):
   315	    """
   316	    Numerical connectedness verification: count connected components of the
   317	    short-edge adjacency matrix. Connectedness is reported, not derived from
   318	    a structural argument.
   319	    """
   320	    n_components, _ = connected_components(csr_matrix(A), directed=False)
   321	    return {
   322	        "n_connected_components": int(n_components),
   323	        "connected": bool(n_components == 1),
   324	    }
   325	
   326	
   327	def multi_source_sweep(V, C_phi):
   328	    """
   329	    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
   330	    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
   331	    predicts the correlation is invariant under choice of source vertex; this
   332	    function verifies the prediction numerically across all 120 sources and
   333	    reports the min/mean/max envelope.
   334	    """
   335	    n = V.shape[0]
   336	    corrs = np.zeros(n)
   337	    for source_idx in range(n):
   338	        psi = green_response(C_phi, source_idx)
   339	        chord = np.linalg.norm(V - V[source_idx], axis=1)
   340	        cont = (PHI / 2.0) * np.exp(-chord / PHI)
   341	        mask = np.arange(n) != source_idx
   342	        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   343	    return {
   344	        "n_sources": int(n),
   345	        "min_correlation": float(corrs.min()),
   346	        "mean_correlation": float(corrs.mean()),
   347	        "max_correlation": float(corrs.max()),
   348	        "max_minus_min": float(corrs.max() - corrs.min()),
   349	    }
   350	
   351	
   352	def operator_norm_check(L, w):
   353	    lam_min_L = float(w[0])           # 0
   354	    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
   355	    op_norm = 1.0 / lam_min_C         # phi^2
   356	    return {
   357	        "lambda_min_L": lam_min_L,
   358	        "lambda_min_C_phi": lam_min_C,
   359	        "operator_norm_C_phi_inv": op_norm,
   360	        "predicted_phi_squared": PHI ** 2,
   361	    }
   362	
   363	
   364	# ---------------------------------------------------------------------------
   365	# 9. Run everything and write results.json
   366	# ---------------------------------------------------------------------------
   367	
   368	def main():
   369	    out_path = Path(__file__).parent / "results.json"
   370	
   371	    V = build_v600()
   372	    n = V.shape[0]
   373	    A = build_short_edge_graph(V)
   374	    deg = A.sum(axis=1)
   375	    n_edges = int(A.sum() // 2)
   376	
   377	    L, w, U = laplacian_spectrum(A)
   378	    spectrum = round_spectrum(w, decimals=4)
   379	
   380	    C_phi = build_C_phi(L)
   381	    op_norm = operator_norm_check(L, w)
   382	    connectivity = connectivity_check(A)
   383	    multi_source = multi_source_sweep(V, C_phi)
   384	
   385	    # Pick the +x_0 axis vertex as canonical pole/source.
   386	    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
   387	    pole = V[pole_idx]
   388	
   389	    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)
   390	
   391	    test = discrete_continuum_test(V, C_phi, pole_idx)
   392	
   393	    # Variant comparison on the same source
   394	    variants = {}
   395	    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   396	        out = variant_correlation(V, A, pole_idx, variant)
   397	        variants[variant] = {
   398	            "shell_mean_correlation": out["shell_mean_correlation"],
   399	            "per_vertex_correlation": out["per_vertex_correlation"],
   400	        }
   401	
   402	    result = {
   403	        "phi": PHI,
   404	        "phi_inv_sq": INV_PHI2,
   405	        "n_vertices": n,
   406	        "n_edges": n_edges,
   407	        "degree_sequence": {
   408	            "min": int(deg.min()),
   409	            "max": int(deg.max()),
   410	            "mean": float(deg.mean()),
   411	        },
   412	        "connectivity": connectivity,
   413	        "shell_sizes": shell_sizes,
   414	        "shell_inner_products": canonical_inner.tolist(),
   415	        "antipodal_check": {
   416	            "pole_idx": pole_idx,
   417	            "antipode_idx": int(np.argmin(V @ pole)),
   418	            "expected_shell_8_size": 1,
   419	            "observed_shell_8_size": shell_sizes.get(8, 0),
   420	        },
   421	        "laplacian_spectrum_grouped": [
   422	            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
   423	        ],
   424	        "operator_norm": op_norm,
   425	        "discrete_continuum_test": test,
   426	        "variant_correlation": variants,
   427	        "multi_source_sweep": multi_source,
   428	    }
   429	
   430	    with open(out_path, "w") as f:
   431	        json.dump(result, f, indent=2)
   432	
   433	    # Headline summary
   434	    print("=" * 60)
   435	    print("ARIA Closure Kernel — verification")
   436	    print("=" * 60)
   437	    print(f"|V|           = {n}  (expected 120)")
   438	    print(f"|E|           = {n_edges}  (expected 720)")
   439	    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
   440	    print(f"connected      = {connectivity['connected']}  "
   441	          f"(components = {connectivity['n_connected_components']})")
   442	    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
   443	    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
   444	    print()
   445	    print("Laplacian spectrum (eigenvalue, multiplicity):")
   446	    for ev, m in spectrum:
   447	        print(f"  {ev:>8.4f}   x {m}")
   448	    print()
   449	    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
   450	    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
   451	    print()
   452	    print("Discrete <-> continuum agreement (Pearson correlation):")
   453	    print(f"  variant         | shell-mean  | per-vertex")
   454	    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   455	        sm = variants[v]["shell_mean_correlation"]
   456	        pv = variants[v]["per_vertex_correlation"]
   457	        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
   458	    print()
   459	    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
   460	    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
   461	    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
   462	    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
   463	    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
   464	    print()
   465	    print(f"Wrote {out_path}")
   466	
   467	
   468	if __name__ == "__main__":
   469	    main()

 succeeded in 305ms:
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

codex
`results.json` matches the advertised kernel numerics: vertices, edges, shell sizes, spectrum, norm, and all three correlations are consistent with the abstract-level numbers. I’m now reading the companion aria-chess paper around its headline claims so the inherited active-regime statements can be checked against its own scope.
exec
/bin/bash -lc 'wc -l "papers/aria-chess-paper/paper/main.tex" "papers/aria-chess-paper/paper/sections/01_introduction.tex" "papers/aria-chess-paper/paper/sections/02_method.tex" "papers/aria-chess-paper/paper/sections/03_substrate.tex" "papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex" "papers/aria-chess-paper/paper/sections/05_results.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l "papers/aria-chess-paper/paper/sections/06_stress_tests.tex" "papers/aria-chess-paper/paper/sections/07_cross_domain.tex" "papers/aria-chess-paper/paper/sections/08_discussion.tex" "papers/aria-chess-paper/paper/sections/09_limitations.tex" "papers/aria-chess-paper/paper/sections/10_conclusion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"17/18|18/18|6/6|seed|P4|deep-dive|bounded_topk|k=12|eta|0\\.05|0\\.20|2026-04-18|substrate witness|selection theorem|600-cell|degree|93\\.8|53\\.1|87\\.5|4\\.4|1003|11\\.58|79\\.78|6\\.80|2\\.252|0\\.463|1\\.83|0\\.066|0\\.33\" \"papers/aria-chess-paper/paper\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"AIC|Mode B|Gaussian|w_\\{|FREE_C9|0\\.348|0\\.652|2\\.77|13\\.555|0\\.997|0\\.9968|LHCb 2025|looked at|historically|blind|residual|overshoot|4\\.98|2\\.2\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 290ms:
  168 papers/aria-chess-paper/paper/sections/06_stress_tests.tex
  273 papers/aria-chess-paper/paper/sections/07_cross_domain.tex
  207 papers/aria-chess-paper/paper/sections/08_discussion.tex
  195 papers/aria-chess-paper/paper/sections/09_limitations.tex
   96 papers/aria-chess-paper/paper/sections/10_conclusion.tex
  939 total

 succeeded in 310ms:
  212 papers/aria-chess-paper/paper/main.tex
  170 papers/aria-chess-paper/paper/sections/01_introduction.tex
  201 papers/aria-chess-paper/paper/sections/02_method.tex
  173 papers/aria-chess-paper/paper/sections/03_substrate.tex
  197 papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex
  208 papers/aria-chess-paper/paper/sections/05_results.tex
 1161 total

 succeeded in 339ms:
papers/aria-chess-paper/paper/main.tex:19:\title{A geometry-fixed substrate witness for cortical signatures:\\
papers/aria-chess-paper/paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
papers/aria-chess-paper/paper/main.tex:39:Once the 600-cell substrate is chosen, its graph structure is fixed:
papers/aria-chess-paper/paper/main.tex:40:$|V|=120$ vertices of uniform degree $12$ (forced by H$_4$ transitivity
papers/aria-chess-paper/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
papers/aria-chess-paper/paper/main.tex:53:trajectory at seed~$42$. No shape parameter is tuned to any neural
papers/aria-chess-paper/paper/main.tex:56:at the graph's average degree and one condition-dependent self-injection
papers/aria-chess-paper/paper/main.tex:57:coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
papers/aria-chess-paper/paper/main.tex:62:This paper presents an empirical \emph{substrate witness}: it shows
papers/aria-chess-paper/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:70:sits as the $L_M$ instance; the selection of the 600-cell as the active
papers/aria-chess-paper/paper/main.tex:74:We test whether a geometry-fixed substrate — the 600-cell regular
papers/aria-chess-paper/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:83:a documented $N\!=\!20$ deep-dive on the residual high-variance
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:120:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:133:leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
papers/aria-chess-paper/paper/main.tex:134:$\to$ substrate-routed $93.8\%$, with state reset; the
papers/aria-chess-paper/paper/main.tex:138:classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
papers/aria-chess-paper/paper/main.tex:143:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
papers/aria-chess-paper/paper/main.tex:145:deterministic null reference: ARIA degree std
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
papers/aria-chess-paper/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
papers/aria-chess-paper/paper/main.tex:155:We do not claim the 600-cell is the unique substrate consistent with
papers/aria-chess-paper/paper/main.tex:160:is reported on a single deterministic trajectory; cross-seed CIs on
papers/aria-chess-paper/paper/main.tex:193:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
papers/aria-chess-paper/paper/main.tex:200:consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
papers/aria-chess-paper/paper/main.tex:204:deterministic given seeds; the substrate's spectral decomposition is
papers/aria-chess-paper/paper/main.tex:206:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
papers/aria-chess-paper/paper/references.bib:162:  title  = {The 600-cell closure response kernel $C_\varphi = L + \varphi^{-2} I$ and its 9-shell projection},
papers/aria-chess-paper/paper/references.bib:176:  title        = {{ARIA-chess}: 600-cell substrate, recurrent self-model, and preregistered validation},
papers/aria-chess-paper/paper/README.md:3:A geometry-fixed substrate witness for cortical signatures: eighteen
papers/aria-chess-paper/paper/README.md:5:the 600-cell regular 4-polytope under H₄ Coxeter symmetry.
papers/aria-chess-paper/paper/README.md:44:# C×P synergy N=20 deep-dive (~28 min)
papers/aria-chess-paper/paper/README.md:54:All scripts are deterministic given seeds. The substrate's spectral
papers/aria-chess-paper/paper/README.md:55:decomposition is cached at module level. Reruns at seed 42 reproduce
papers/aria-chess-paper/paper/README.md:64:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` (N=20 deep-dive)
papers/aria-chess-paper/paper/README.md:66:- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` (18/18 tally)
papers/aria-chess-paper/paper/README.md:67:- `docs/brain_mapping/PAPER_PREDICTIONS.md` (preregistered 2026-04-18)
papers/aria-chess-paper/paper/README.md:72:This is a **substrate witness**: a geometry-fixed substrate is
papers/aria-chess-paper/paper/README.md:76:not a selection theorem on the companion adaptive-closure-transport
papers/aria-chess-paper/paper/README.md:77:4-tuple, and not a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
papers/aria-chess-paper/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
papers/aria-chess-paper/paper/sections/03_substrate.tex:38:sizes. The 600-cell construction itself is
papers/aria-chess-paper/paper/sections/03_substrate.tex:42:every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
papers/aria-chess-paper/paper/sections/03_substrate.tex:63:i.e.\ approximately $\{0, 2.292, 5.528, 9, 12, 14, 14.472, 15, 15.708\}$
papers/aria-chess-paper/paper/sections/03_substrate.tex:109:event distributions. The choice $k\!=\!12$ is the average degree of
papers/aria-chess-paper/paper/sections/03_substrate.tex:116:average degree, not a fitted threshold. No other shape parameter
papers/aria-chess-paper/paper/sections/03_substrate.tex:118:$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
papers/aria-chess-paper/paper/sections/03_substrate.tex:163:  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
papers/aria-chess-paper/paper/sections/03_substrate.tex:164:  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
papers/aria-chess-paper/paper/sections/05_results.tex:18:\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
papers/aria-chess-paper/paper/sections/05_results.tex:28:seed 42).}
papers/aria-chess-paper/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
papers/aria-chess-paper/paper/sections/05_results.tex:77:are not part of the dated 2026-04-18 P1--P18 preregistration; their
papers/aria-chess-paper/paper/sections/05_results.tex:87:load-bearing for the headline claim. Single-seed disclosure:
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:101:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
papers/aria-chess-paper/paper/sections/05_results.tex:109:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:115:P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:121:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:122:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:124:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:125:P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:134:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
papers/aria-chess-paper/paper/sections/05_results.tex:142:  $N\!=\!3$ on a high-per-seed-variance interaction term.
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:144:  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:181:ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
papers/aria-chess-paper/paper/sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
papers/aria-chess-paper/paper/sections/05_results.tex:201:$k=12$ is pinned to the substrate's average degree
papers/aria-chess-paper/paper/sections/05_results.tex:208:with event-bootstrap; cross-seed CI is an open build).
papers/aria-chess-paper/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
papers/aria-chess-paper/paper/sections/02_method.tex:13:\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
papers/aria-chess-paper/paper/sections/02_method.tex:14:(P1--P18) were locked on 2026-04-18 in
papers/aria-chess-paper/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:37:2026-04-20 validation reported failures (P3, P4, P13), the documented
papers/aria-chess-paper/paper/sections/02_method.tex:40:(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
papers/aria-chess-paper/paper/sections/02_method.tex:41:(P4, C$\times$P), and
papers/aria-chess-paper/paper/sections/02_method.tex:49:\to (\text{script}, \text{seed range}, \text{dataset/source},
papers/aria-chess-paper/paper/sections/02_method.tex:63:P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
papers/aria-chess-paper/paper/sections/02_method.tex:112:computational tractability; full-cohort $n=1003$ statistics
papers/aria-chess-paper/paper/sections/02_method.tex:113:(degree std, participation ratio, clustering coefficient $\sigma$-
papers/aria-chess-paper/paper/sections/02_method.tex:141:$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
papers/aria-chess-paper/paper/sections/02_method.tex:142:preregistered; 42 for the deep-dive.
papers/aria-chess-paper/paper/sections/02_method.tex:145:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
papers/aria-chess-paper/paper/sections/02_method.tex:161:on the full $n=1003$ subject distribution.
papers/aria-chess-paper/paper/sections/02_method.tex:188:\item C$\times$P synergy $N\!=\!20$ deep-dive:
papers/aria-chess-paper/paper/sections/02_method.tex:197:All scripts are deterministic given seeds. Reruns at seed $42$ on the
papers/aria-chess-paper/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
papers/aria-chess-paper/paper/sections/08_discussion.tex:15:Three things are claimed novel as a substrate witness:
papers/aria-chess-paper/paper/sections/08_discussion.tex:19:  data.} Once the 600-cell is chosen as the substrate, its graph
papers/aria-chess-paper/paper/sections/08_discussion.tex:20:  ($120$ vertices, uniform degree $12$ on the canonical short-edge
papers/aria-chess-paper/paper/sections/08_discussion.tex:38:  original 3-seed validation.
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:42:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
papers/aria-chess-paper/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
papers/aria-chess-paper/paper/sections/08_discussion.tex:71:The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
papers/aria-chess-paper/paper/sections/08_discussion.tex:74:Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
papers/aria-chess-paper/paper/sections/08_discussion.tex:80:circuits implement context rotation or partial emission. The 600-cell
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:119:\emph{substrate witness} for the family that ACT names; ACT is not the
papers/aria-chess-paper/paper/sections/08_discussion.tex:132:one we held until the $N\!=\!20$ deep-dive — is that these are mostly
papers/aria-chess-paper/paper/sections/08_discussion.tex:142:\emph{a hypothesis the substrate witness raises}, not as a proof.
papers/aria-chess-paper/paper/sections/08_discussion.tex:153:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
papers/aria-chess-paper/paper/sections/08_discussion.tex:156:  system with unknown per-seed variance, budget for at least this
papers/aria-chess-paper/paper/sections/08_discussion.tex:158:  taken as universal. The original 3-seed plan was the source of two
papers/aria-chess-paper/paper/sections/08_discussion.tex:166:  an explicit reset/equilibration discipline}, not just seed.
papers/aria-chess-paper/paper/sections/08_discussion.tex:181:group-theoretic graph with structure-level statements: degree std
papers/aria-chess-paper/paper/sections/08_discussion.tex:188:\subsection{Open questions raised by the substrate witness}
papers/aria-chess-paper/paper/sections/08_discussion.tex:192:  cross-seed runs of the recurrent layer? (Single-seed disclosure;
papers/aria-chess-paper/paper/sections/08_discussion.tex:198:  independent fresh-seed $N\!=\!20$ replication at a different seed
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:11:coupling $\eta$, and four trajectory observables. No shape parameter
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:14:This section is method, not metaphysics. We do not claim the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:26:\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:30:with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:39:\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:41:\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:53:avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:56:\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:104:\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:108:drop $+0.066$).
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:125:$\times$ $800$ ticks each at seed $42$:
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:127:\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:131:that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:141:\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:142:$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:169:(coupling $0.05$) cross-orbit pressure averaging that prevents
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:187:30-vertex icosidodecahedral ring with split degree distribution.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:194:($D$ at $0.05$, $P$ at $30\%$ scale saturating at pressure $3.0$,
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:195:$C$ rotation period, $E$ degree-ratio multiplier) are fixed design
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:29:\textbf{Critical methodological detail.} Between successive depth
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:45:$5$    & $53.1\%$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:47:$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:48:$40$   & $84.4\%$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:49:$60$   & $84.4\%$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:74:$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:77:and P16 (conversation null); both pass. The 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:87:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:95:4-category classification from raw $53.1\%$ (just above $25\%$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:96:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:107:substrate retains $65.4\%$ classification accuracy under random
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:132:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:133:P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:139:\textbf{Reading.} Conversation raw features at $87.5\%$ are already
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:141:lift is $-4.4$pp, well within the preregistered neutrality band
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:146:selective-amplifier behaviour preregistered in 2026-04-18: in these
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:149:are already saturated (conversation raw $87.5\%$). We do not claim
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:158:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:160:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:162:vertex graph ($\rho=0.101$). Compare degree distribution and
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:165:has identical local structure $\Rightarrow$ uniform degree $12$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:166:$\Rightarrow$ degree std $= 0$ as a theorem.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:172:$n=1003$ descriptive statistics.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:195:\item P17 (ARIA degree std, theorem): predicted $=0$, observed
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:197:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:198:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:199:  HCP subjects have degree std below $2.0$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:202:\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:258:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
papers/aria-chess-paper/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
papers/aria-chess-paper/paper/sections/01_introduction.tex:28:single condition-dependent self-injection coupling $\eta$ and a
papers/aria-chess-paper/paper/sections/01_introduction.tex:35:We claim a single \emph{substrate witness}: that a geometry-fixed
papers/aria-chess-paper/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
papers/aria-chess-paper/paper/sections/01_introduction.tex:44:  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
papers/aria-chess-paper/paper/sections/01_introduction.tex:45:  transitivity forces uniform vertex degree (here $12$ on the
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:59:  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:67:  $N\!=\!20$ deep-dive on the residual high-variance interaction
papers/aria-chess-paper/paper/sections/01_introduction.tex:72:  conversation $-4.4$pp lift, within preregistered neutrality bounds)
papers/aria-chess-paper/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
papers/aria-chess-paper/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
papers/aria-chess-paper/paper/sections/01_introduction.tex:83:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
papers/aria-chess-paper/paper/sections/01_introduction.tex:86:  build, not a discharged comparison. The 600-cell choice is post-hoc
papers/aria-chess-paper/paper/sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
papers/aria-chess-paper/paper/sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
papers/aria-chess-paper/paper/sections/01_introduction.tex:96:  this substrate fills the $L_M$ slot. The selection of the 600-cell
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:144:parameter $\eta$ and one graph-pinned nonlinearity, against published
papers/aria-chess-paper/paper/sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
papers/aria-chess-paper/paper/sections/01_introduction.tex:149:that cortex \emph{is} the 600-cell.
papers/aria-chess-paper/paper/sections/01_introduction.tex:156:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
papers/aria-chess-paper/paper/sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
papers/aria-chess-paper/paper/sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:15:confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:28:Per-seed paired estimates use the same formula on a single seed's
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:53:($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:60:\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:61:$32000$--$32019$, non-overlapping with original validation seeds in
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:64:seed $42$. Wallclock $1706$\,s on a single CPU
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:72:\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:95:Bootstrap on the 20-seed sample (2000 resamples):
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:105:\textbf{Per-seed paired distribution.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:106:$19/20$ seeds give a positive paired-interaction estimate (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:107:$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:117:\textbf{Architectural reading (substrate witness).} $C$ creates churn
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:127:architectural claim from the original 3-seed validation that held $C$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:130:\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:132:(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:133:selected to be non-overlapping with the original $30000$s seeds.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:135:(i) a second independent $N\!=\!20$ run at a different seed range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:137:(ii) an $N\!=\!50$ characterisation of the per-seed sample
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:146:\item It does not establish an $\eta$-trajectory derivation; $\eta$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:161:The original 3-seed preregistered validation gave estimates consistent
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:165:per-seed variance, budget the seed count from a power-analysis
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:166:assumption that the per-seed std could be as large as the interaction
papers/aria-chess-paper/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-chess-paper/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested whether
papers/aria-chess-paper/paper/sections/09_limitations.tex:16:comparable correspondences. The 600-cell was chosen because its
papers/aria-chess-paper/paper/sections/09_limitations.tex:26:\textbf{Single-seed determinism on the recurrent layer.} The v4
papers/aria-chess-paper/paper/sections/09_limitations.tex:28:a single deterministic trajectory at seed $42$. Empirical CIs across
papers/aria-chess-paper/paper/sections/09_limitations.tex:29:$10$--$20$ cross-seed runs would strengthen the per-signature claims
papers/aria-chess-paper/paper/sections/09_limitations.tex:31:WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
papers/aria-chess-paper/paper/sections/09_limitations.tex:35:\emph{Strengthening build:} 10--20 cross-seed runs of
papers/aria-chess-paper/paper/sections/09_limitations.tex:58:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-chess-paper/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
papers/aria-chess-paper/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-chess-paper/paper/sections/09_limitations.tex:95:\textbf{The recurrent layer is a method, not a metaphysics claim.}
papers/aria-chess-paper/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
papers/aria-chess-paper/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
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
papers/aria-chess-paper/paper/sections/09_limitations.tex:187:The result is a substrate witness: a geometry-fixed substrate, with
papers/aria-chess-paper/paper/sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
papers/aria-chess-paper/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
papers/aria-chess-paper/paper/sections/10_conclusion.tex:12:degree $12$ on the canonical short-edge nearest-neighbour graph, with
papers/aria-chess-paper/paper/sections/10_conclusion.tex:15:$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
papers/aria-chess-paper/paper/sections/10_conclusion.tex:17:degree enter the recurrent layer above the substrate. No shape
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:25:propofol continuity drop $+0.066$; propofol integrated-information
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:42:failure; the closure of the three gaps (P3, P4, P13) is documented
papers/aria-chess-paper/paper/sections/10_conclusion.tex:52:the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
papers/aria-chess-paper/paper/sections/10_conclusion.tex:54:high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
papers/aria-chess-paper/paper/sections/10_conclusion.tex:62:canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
papers/aria-chess-paper/paper/sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
papers/aria-chess-paper/paper/sections/10_conclusion.tex:66:conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
papers/aria-chess-paper/paper/sections/10_conclusion.tex:69:on the full-cohort descriptive HCP $n\!=\!1003$ statistics
papers/aria-chess-paper/paper/sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
papers/aria-chess-paper/paper/sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
papers/aria-chess-paper/paper/sections/10_conclusion.tex:75:\textbf{Substrate-witness scope.} This is a substrate witness, not a
papers/aria-chess-paper/paper/sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
papers/aria-chess-paper/paper/sections/10_conclusion.tex:79:uniqueness claim for the 600-cell among regular 4-polytopes. The
papers/aria-chess-paper/paper/sections/10_conclusion.tex:80:strengthening builds — cross-seed CIs on the recurrent-layer
papers/aria-chess-paper/paper/sections/10_conclusion.tex:82:C$\times$P replication at a different seed range, cross-parcellation
papers/aria-chess-paper/paper/sections/10_conclusion.tex:91:gathered here is the substrate witness; the broader programme to

 succeeded in 741ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:20:  2025, LHCb 2025, LHCb 2015 Bs->phi) are evaluated using flavio.np_prediction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:23:  shift on AIC; an earlier linearised analysis found a stronger result that did
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:20:- **Akaike-weight stacking** of $\Delta\mathrm{AIC}$ across the five fits
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:47:  basis-correction factor $\sim 2.2$, residual $\sim 50\%$ overshoot.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:50:  (correlation $0.997$ with the continuum kernel) decided
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:57:$\Delta\mathrm{AIC}$ values span $[-0.24, +1.09]$ around zero;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:58:stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:59:$w_{\mathrm{FREE\_C9}}=0.652$. On current data the two models are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:60:statistically indistinguishable on AIC — a question current data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:65:An earlier linearised analysis (Mode B, linear in $\Delta C_{9}$ via
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:66:central-difference slopes) had given $\Delta\mathrm{AIC} = -1.67$ in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:67:favour of the kernel on LHCb 2025. The non-linear refit using
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:68:`flavio.np_prediction` directly gives $\Delta\mathrm{AIC} = +1.09$ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:69:the same dataset — a $+2.77$ AIC-unit drift. The per-bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:70:linearisation residual reaches $4.3\sigma$ at the linearised best-fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:77:  AIC" (linearised) to "fixed geometry-derived kernel describes the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:78:  anomaly across five datasets, AIC-tied with $\mathrm{FREE\_C9}$"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:103:- All five datasets gave $\Delta\mathrm{AIC} < 0$ vs FREE\_C9, suggesting
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:105:- Stacked Akaike weight $w_{\mathrm{VFD}}=0.904$ vs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:106:  $w_{\mathrm{FREE\_C9}}=0.096$ (linearised).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:109:  amplification factor $\approx 2.2$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:118:- Reproduced the negative direction of $\Delta C_{9}$ on the LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:16:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:21:| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:22:| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:27:- **Cross-channel ratio.** The $B\to K^{*}$ vs $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with the predicted Krüger–Matias $P$-basis vs $S$-basis amplification ($\sim 2.2$), with a residual $\sim 50\%$ overshoot.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:28:- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31:- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:32:- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:33:- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:44:| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:48:**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:83:│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:91:│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:122:The five datasets in the paper draw from five HEPData records. The first four are bundled in `data/raw/hepdata*/` (modest size, CC BY 4.0). For LHCb 2025 (the largest), download with:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:138:1. The non-linear LHCb 2025 refit (`scripts/wo016c_nonlinear_refit.py`).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:175:| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:177:| 4 | Results on LHCb 2025: non-linear vs linearised, drift table, leave-one-observable-out |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:178:| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:185:The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:193:  - LHCb 2025: [HEPData ins3094698](https://www.hepdata.net/record/ins3094698) (DOI [10.17182/hepdata.167733.v1](https://doi.org/10.17182/hepdata.167733.v1))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:214:For the LHCb 2025 dataset the project rests on, also cite:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:51:$\Delta\mathrm{AIC}$ values span $[-0.24, +1.09]$ around zero, with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:52:stacked Akaike weight $w_{\mathrm{VFD}}=0.35$ vs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:53:$w_{\mathrm{FREE\_C9}}=0.65$. AIC compares per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:57:independent of, and complementary to, the AIC tie. An earlier
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:58:linearised analysis (Mode B, linear in $\Delta C_{9}$ via
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:77:\emph{pure-geometry criterion} (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:107:basis-correction factor $\sim 2.2$, with a residual $\sim 50\,\%$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:108:overshoot of the basis-corrected prediction that the published
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:111:\noindent\emph{(iv) AIC comparison.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:113:$\mathrm{FREE\_C9}$ (also $k=1$), the per-dataset $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:116:is $w_{\mathrm{VFD}}=0.35$ vs $w_{\mathrm{FREE\_C9}}=0.65$. On current
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:117:data the two models are statistically indistinguishable on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:121:claim independent of the AIC tie. AIC measures per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:125:Gaussian charm-loop proxy fits marginally better in $\chi^{2}$ at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/references.bib:6:% --- LHCb 2025 (current B0 -> K*0 mumu, 8.4 fb^-1) ---
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:5:#   1. Non-linear LHCb 2025 refit             → reports/wo016c_nonlinear_refit.{md,csv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:26:step "1/5  Non-linear LHCb 2025 refit (~30s)"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.md:5:| dataset | non-linear χ² (FREE) | non-linear χ² (VFD) | ΔAIC (NL) | ΔC9 (NL) | A (NL) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.md:11:| Bs2phi-LHCb-2015 | 13.201 | 12.962 | -0.240 | -4.122 | +4.984 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:5:    F2 - Bin pulls for the four LHCb 2025 angular observables under
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:6:         the non-linear FREE_C9 and VFD fits.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:77:               zorder=5, s=40, label="LHCb 2025 bin centres")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:164:    fig.suptitle("LHCb 2025 bin pulls under non-linear "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:189:        "LHCb-2025":         "LHCb 2025\n" + r"$B^0\to K^{*0}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:195:    aic_diff = {r["dataset"]: float(r["delta_aic_vs_FREE_C9"])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:219:                     fr"$\Delta\mathrm{{AIC}}={da:+.2f}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:233:                fr"$\Delta\mathrm{{AIC}}={aic_diff[ds_phi]:+.2f}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:235:    pred = 1.135 * 2.2  # P-basis * basis factor
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/README.md:73:$\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 did not survive a non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:55:    """Sanity: known LHCb 2025 P5' is positive at low q² and negative above ~ 4 GeV²."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_likelihood.py:63:    assert a3 > a0  # AIC penalty grows with k
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_likelihood.py:67:    # BIC penalises more harshly than AIC for n>=8
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:15:    closure_residual_q2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:42:def test_residual_constant_returns_uniform_negative_delta_c9():
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:44:    out = closure_residual_q2(q2, amplitude=0.5, mode=MODE_CONSTANT)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:49:def test_residual_log_phase_is_bounded():
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:51:    out = closure_residual_q2(q2, amplitude=1.0, mode=MODE_LOG_PHASE, theta=0.0)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:56:def test_residual_threshold_localised_near_charm_resonances():
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:58:    out = closure_residual_q2(q2, amplitude=1.0, mode=MODE_THRESHOLD, sigma=1.0)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:59:    # The residual should be largest in magnitude in the 9-14 GeV^2 region.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:68:        closure_residual_q2(q2, amplitude=-0.1, mode=MODE_CONSTANT)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:73:        closure_residual_q2(np.array([1.0]), amplitude=0.1, mode="quantum_woo")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:78:        closure_residual_q2(np.array([0.0, 1.0]), amplitude=0.1, mode=MODE_CONSTANT)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,evaluation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:2:LHCb-2015,B0->K*mumu,FREE_C9,32,1,30.69104835960865,32.69104835960865,34.15678426240838,0.0,-1.0796559803655492,-1.0796559803655492,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:4:LHCb-2021-Kstplus,B+->K*+mumu,FREE_C9,32,1,22.76511589608483,24.76511589608483,26.230851798884554,0.0,-1.8196686329963627,-1.8196686329963627,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:6:CMS-2025-noP4p,B0->K*mumu,FREE_C9,18,1,43.73143845773427,45.73143845773427,46.62181021563043,0.0,-0.9538642637928241,-0.9538642637928241,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:8:LHCb-2025,B0->K*mumu,FREE_C9,32,1,40.89068922835959,42.89068922835959,44.35642513115932,0.0,-1.0025621703516263,-1.0025621703516263,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:10:Bs2phi-LHCb-2015,Bs->phimumu,FREE_C9,24,1,13.201397760357471,15.201397760357471,16.37945159070542,0.0,-4.121891268879767,-4.121891268879767,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:11:Bs2phi-LHCb-2015,Bs->phimumu,VFD_GREEN_600CELL,24,1,12.961624102342121,14.961624102342121,16.139677932690066,-0.23977365801535022,4.98442594875091,-4.331132308287093,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:5:non-linear flavio refit on LHCb 2025 (Delta AIC drift = +2.77 AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:9:This script re-fits FREE_C9 and VFD_GREEN_600CELL on each of the five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:174:                  f"DAIC={result['delta_aic_vfd_minus_free']:+.3f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:183:            "chi2", "aic", "bic", "delta_aic_vs_FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:190:                r["dataset"], r["decay"], "FREE_C9", r["n_data"],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:213:        "ΔAIC (NL) | ΔC9 (NL) | A (NL) |",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:21:\item \textbf{LHCb 2025, four-observable joint fit (non-linear):}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:24:  $k=1$). On AIC the kernel and a constant-$\Delta C_{9}$ shift at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:26:  ($\Delta\mathrm{AIC}=+1.09$, mild preference for the constant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:29:  collaborations and 3 channels):} $\Delta\mathrm{AIC}\in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:32:  $w_{\mathrm{VFD}}=0.35$, $w_{\mathrm{FREE\_C9}}=0.65$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:38:  (factor $\sim 2$); $A=+4.98$ on the $S$-basis $B_{s}\!\to\!\phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:40:  $\langle 1/\sqrt{F_{L}(1-F_{L})}\rangle\approx 2.2$, with a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:41:  factor-of-$2$ unexplained residual.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:42:\item \textbf{Linearisation drift:} on LHCb 2025 the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:43:  $\Delta\mathrm{AIC}$ shifts by $+2.77$ between the linearised and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:70:$\Delta\mathrm{AIC}_{\mathrm{VFD\,vs\,FREE\_C9}}\geq 0$ on the LHCb
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:75:listed above are independent of, and unaffected by, this AIC tie.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:87:pure-geometry criterion (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:90:over a constant Wilson-coefficient shift. AIC compares per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:17:    FREE_C9       k=1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:88:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:110:        delta_aic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:139:        "FREE_C9", "reference", float(r.fun), 1, len(values),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:167:    eigenfunctions: residual(x) = sum_{k=1..n} c_k * cos((2k-1) pi x / (2 L)),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:168:    Delta_C9(x) = -residual(x). The amplitudes c_k are unconstrained sign — the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:185:        residual = basis @ c
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:186:        delta = -residual
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:224:    free_aic = next(r.aic for r in rows if r.model == "FREE_C9")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:227:        r.delta_aic_vs_FREE_C9 = r.aic - free_aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:5:result (dAIC = -1.67 vs FREE_C9 with shared amplitude across
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:14:    3. Alternative-model comparison: FREE_C9, FREE_C9 + C10,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:15:       charm-loop nuisance proxy (Gaussian residual at J/psi-psi(2S)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:193:    # FREE_C9 reference
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:202:        "FREE_C9_chi2": free.chi2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:203:        "FREE_C9_DC9": free.effective_delta_c9_mean,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:204:        "FREE_C9_aic": free.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:249:        "model": "FREE_C9 + FREE_C10",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:260:    """Charm-loop nuisance: a Gaussian residual centred at the J/psi-psi(2S)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:285:        "model": "Charm-loop Gaussian (free A, sigma)",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:496:        {"model": "FREE_C9", "k_params": 1, "chi2": free_c9.chi2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:498:         "delta_aic_vs_FREE_C9": 0.0, "params": f"DC9={free_c9.effective_delta_c9_mean:+.3f}"},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:501:         "delta_aic_vs_FREE_C9": vfd_kernel.aic - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:505:         "delta_aic_vs_FREE_C9": free_c9_c10["aic"] - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:509:         "delta_aic_vs_FREE_C9": charm_loop["aic"] - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:34:single-amplitude fit to P5' data. Compare chi^2 / AIC against:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:37:    - FREE_C9 (k = 1)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:44:    - dAIC vs FREE_C9 <= 0 (competitive with global C_9 shift)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:117:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:234:        delta_aic_vs_FREE_C9=aic_v - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:258:    # Reference rows. Re-derive FREE_C9 and KAPPA_EXP here so the comparison is local.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:294:            "delta_aic_vs_FREE_C9": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:302:            "model": "FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:306:            "delta_aic_vs_FREE_C9": 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:318:            "delta_aic_vs_FREE_C9": exp_aic - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:332:            "delta_aic_vs_FREE_C9": f.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:20:       data rejects (i.e. higher dAIC vs FREE_C9 than the rank-1 mode alone).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:199:                "delta_aic_vs_FREE_C9": r.aic_p5p - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:254:    print(f"FREE_C9 reference chi^2 = {res['free_c9_chi2']:.4f}, AIC = {res['free_c9_aic']:.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:1:# WO-016c — Non-linear flavio refit on LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:10:| model | chi^2 | AIC | Delta AIC vs FREE_C9 | fit param |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:12:| FREE_C9_linear | 39.303 | 41.303 | +0.000 | DC9=-1.340 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:13:| FREE_C9_nonlinear@linear-best-fit | 66.596 | 68.596 | +0.000 | DC9=-1.340 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:14:| FREE_C9_nonlinear_refit | 40.891 | 42.891 | +0.000 | DC9=-1.002 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:16:| VFD_nonlinear@linear-best-fit | 82.241 | 84.241 | +15.644 | A=+1.594 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:19:- Linearised Delta AIC (FREE_C9 vs VFD): -1.672
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:20:- Non-linear Delta AIC at linear best-fit: +15.644 (diagnostic only; both models held at linear best-fit)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:21:- Non-linear Delta AIC after refit: +1.093 (headline-comparable)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:22:- Drift in headline Delta AIC: +2.765
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:26:- FREE_C9 linear: Delta C9 = -1.3403
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:27:- FREE_C9 non-linear refit: Delta C9 = -1.0025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:31:## Per-bin linearisation residual (|nonlinear - linear| / sigma)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:33:- FREE_C9 at linear best-fit: max = 3.106 sigma, mean = 0.630 sigma
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:36:**Conclusion.** |Drift in headline Delta AIC| = 2.765 > 0.5 AIC unit. The headline must be updated to the non-linear refit value: Delta AIC_NL = +1.093 (vs linearised -1.672). The non-linear refit best-fit is DC9_FREE = -1.002 (vs linear -1.340) and A = +1.135 (vs linear +1.594).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:22:  $\Delta\mathrm{AIC}$ shifts from $-1.67$ (linearised) to $+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:35:  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38:  data was looked at first is acknowledged.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:45:  the relevant level on the joint LHCb 2025 fit; the broader
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:122:  ($\Delta\chi^{2}=1$ Gaussian approximation or non-parametric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:147:on AIC; the stacked Akaike weight is $\approx 1.9{:}1$ in favour of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:152:the stronger ``it beats the constant shift on AIC'' claim of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:2:\section{Results on LHCb 2025}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:5:This section reports the kernel fit on the LHCb 2025 dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:27:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:34:\caption{Headline non-linear joint fit on the four LHCb 2025 angular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:37:AIC by $1.09$ units, a marginal preference (Akaike weight ratio
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:48:on the LHCb 2025 four-observable joint fit, evaluated under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:51:$\pm 1\sigma$ bands. Both models leave residuals of $\lesssim 2\sigma$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:71:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:74:FREE\_C9 (Mode B)           & 1 &  39.30 &  41.30 & $0.00$  & $\Delta C_{9}=-1.34$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:75:VFD\_GREEN\_600CELL (Mode B)& 1 &  37.63 &  39.63 & $-1.67$ & $A=+1.59$, $\Delta C_{9}^{\mathrm{eff}}=-1.37$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:79:model $\mathrm{VFD\_GREEN\_600CELL}$ has lower AIC by $1.67$ units.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:92:quantity & linearised (Mode B) & non-linear refit & drift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:96:$\Delta\mathrm{AIC}$ (VFD vs FREE) & $-1.67$ & $+1.09$ & $\mathbf{+2.77}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:99:max per-bin linearisation residual & --  & $4.27\sigma$ & -- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:100:mean per-bin linearisation residual & -- & $0.71\sigma$ & -- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:105:$\Delta\mathrm{AIC}$ is $2.77$ units, larger than the Mode-B
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:107:evaluation. Per-bin linearisation residuals reach $4\sigma$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:124:($\Delta\mathrm{AIC}=-7.00$ vs FREE\_C9), reflecting that $P_{5}'$ is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:134:Refitting the shared kernel under Mode B after removing one of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:142:dropped & $n$ remaining & $A$ (Mode B) & $\Delta C_{9}^{\mathrm{eff}}$ mean & $\chi^{2}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:149:all (reference, Mode B)  & 32 & 1.594 & $-1.367$ & 37.63 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:153:Mode B (linearised). $A$ varies within $\pm 3\,\%$ across the four
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:169:\item $\mathrm{VFD\_GREEN\_600CELL}\ \mathrm{AIC} \leq \mathrm{FREE\_C9}\ \mathrm{AIC}$:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:170:  \textsc{fail} (non-linear $\Delta\mathrm{AIC}=+1.09$, marginal in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:183:indistinguishable from a constant Wilson-coefficient shift on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:24:LHCb 2025 (ref)   & $B^{0}\to K^{*0}\mu\mu$  & 2512.18053 & ins3094698 & 8.4 & 8 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:40:$P_{5}', P_{4}', P_{1}, P_{2}$, matching the LHCb 2025 reference fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:53:        $\Delta\mathrm{AIC}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:56:LHCb 2021 ($B^{+}\to K^{*+}$) & 32 & 22.77 & $-1.82$ & 22.93 & $\boldsymbol{+2.06}$ & $-1.59$ & $+0.17$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:58:LHCb 2025 (ref)               & 32 & 40.89 & $-1.00$ & 41.98 & $\boldsymbol{+1.14}$ & $-0.86$ & $+1.09$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:60:$B_{s}\!\to\!\phi$ 2015        & 24 & 13.20 & $-4.12$ & 12.96 & $\boldsymbol{+4.98}$ & $-3.85$ & $-0.24$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:65:$B_{s}\!\to\!\phi$, both by $\Delta\mathrm{AIC}=-0.24$) and disfavoured
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:66:on $3/5$ (LHCb 2021, CMS 2025 no-$P_{4}'$, LHCb 2025; max
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:67:$\Delta\mathrm{AIC}=+1.09$). $A>0$ in every fit;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:81:$B_{s}\!\to\!\phi$ fit, $A=+4.98$. The grey dashed line marks the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:83:$A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:86:non-linear $\Delta\mathrm{AIC}$ marginally favours VFD and orange
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:94:To convert the per-dataset $\Delta\mathrm{AIC}$ values into a single
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:96:dataset, $w_{M,d} = e^{-\Delta\mathrm{AIC}_{M,d}/2} / \sum_{M'}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:97:e^{-\Delta\mathrm{AIC}_{M',d}/2}$, and stack across datasets under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:107:dataset & non-linear $\Delta\mathrm{AIC}$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:113:LHCb 2025                  & $+1.093$ & $0.633$ & $0.367$ & FREE\_C9 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:117:\textbf{0.652} & \textbf{0.348} & \textbf{FREE\_C9 (mild)} \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:147:fit ($A=+4.98$) widens the spread to a factor $\sim 5$, but
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:160:\textbf{$\mathrm{VFD\ AIC} \leq \mathrm{FREE\_C9\ AIC}$ on every dataset}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:161:   & \textbf{\textsc{fail}} (passes on $2/5$; max $\Delta\mathrm{AIC}=+1.09$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:162:\textbf{stacked Akaike weight $w_{\mathrm{VFD}} \geq 0.5$}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:163:   & \textbf{\textsc{fail}} ($w_{\mathrm{VFD}} = 0.348$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:172:analysis. The two strict AIC-preference gates (top) \textsc{fail}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:176:preferred model on AIC.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:183:$7\times$ per data point. The residuals are dominated by $P_{4}'$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:189:the convention mismatch. Both $\Delta\mathrm{AIC}$ values agree
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:190:qualitatively (FREE\_C9 favoured by $\sim 0.5$ AIC unit either way)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:202:AIC criterion at equal parameter cost, the kernel does not improve
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:1:"""WO-016c — Non-linear flavio refit on LHCb 2025.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:3:Reviewer concern: the linearised response model (Mode B) extrapolates a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:6:question is whether the headline Delta AIC (-1.67) survives a fully
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:10:    1. Load LHCb 2025 4-observable joint dataset (32 points).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:13:    3. Re-fit both FREE_C9 (one global Delta C9) and VFD (one A;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:15:       directly. Compare non-linear best-fit Delta AIC to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:17:    4. Report whether the headline Delta AIC survives non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:86:    # ---- FREE_C9 non-linear ----
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:162:        ("FREE_C9_linear", chi2_free_lin, aic_free_lin, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:164:        ("FREE_C9_nonlinear@linear-best-fit", chi2_free_nl, aic_free_nl, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:166:        ("FREE_C9_nonlinear_refit", chi2_free_nl_refit, aic_free_nl_refit, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:178:        w.writerow(["model", "chi2", "aic", "delta_aic_vs_FREE_C9", "fit_param"])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:186:        "# WO-016c — Non-linear flavio refit on LHCb 2025",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:197:        "| model | chi^2 | AIC | Delta AIC vs FREE_C9 | fit param |",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:205:        f"- Linearised Delta AIC (FREE_C9 vs VFD): {delta_aic_lin:+.3f}"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:208:        f"- Non-linear Delta AIC at linear best-fit: {delta_aic_nl:+.3f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:212:        f"- Non-linear Delta AIC after refit: {delta_aic_nl_refit:+.3f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:216:        f"- Drift in headline Delta AIC: "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:222:    lines.append(f"- FREE_C9 linear: Delta C9 = {DC9_FREE_BEST:+.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:223:    lines.append(f"- FREE_C9 non-linear refit: Delta C9 = {DC9_FREE_NL:+.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:227:    lines.append("## Per-bin linearisation residual (|nonlinear - linear| / sigma)")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:230:        f"- FREE_C9 at linear best-fit: max = {pred_diff_free.max():.3f} sigma, "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:242:            f"**Conclusion.** |Drift in headline Delta AIC| = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:243:            f"{abs(drift):.3f} <= {threshold} AIC unit. The linearised "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:245:            f"Delta AIC is robust to non-linear flavio evaluation."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:249:            f"**Conclusion.** |Drift in headline Delta AIC| = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:250:            f"{abs(drift):.3f} > {threshold} AIC unit. The headline must be "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:252:            f"Delta AIC_NL = {delta_aic_nl_refit:+.3f} (vs linearised "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:1:dataset,model,AIC_delta,akaike_weight
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:2:LHCb-2015,FREE_C9,0.2411,0.469903
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:4:LHCb-2021-Kstplus,FREE_C9,0.0000,0.520988
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:6:CMS-2025-noP4p,FREE_C9,0.0000,0.558896
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:8:LHCb-2025,FREE_C9,0.0000,0.633273
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:10:Bs2phi-LHCb-2015,FREE_C9,0.2398,0.470064
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:14:STACKED,FREE_C9,-0.2404,0.651705
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:15:STACKED,VFD_GREEN_600CELL,-0.8670,0.348295
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/__init__.py:1:"""vfd_b_anomaly: reproduce LHCb B0 -> K*0 mu+ mu- C9 anomaly and test VFD closure-residual model.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:8:    M1  FREE_C9 (one global DC9)    k = 1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:13:    - M2 AIC and BIC <= M1 AIC and BIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:47:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:48:    delta_bic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:93:        delta_aic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:94:        delta_bic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:116:        model="FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:122:        delta_aic_vs_FREE_C9=0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:123:        delta_bic_vs_FREE_C9=0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:159:        delta_aic_vs_FREE_C9=np.nan,  # filled in by run()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:160:        delta_bic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:206:        delta_aic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:207:        delta_bic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:264:    free = next(r for r in rows if r.model == "FREE_C9")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:266:        if not np.isnan(r.delta_aic_vs_FREE_C9):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:268:        r.delta_aic_vs_FREE_C9 = r.aic - free.aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:269:        r.delta_bic_vs_FREE_C9 = r.bic - free.bic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:281:            "delta_aic_vs_FREE_C9": r.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo006_multi_observable.py:282:            "delta_bic_vs_FREE_C9": r.delta_bic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:3:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:7:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:19:    "delta_aic_vs_FREE_C9":-7.0000330722,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:31:    "delta_aic_vs_FREE_C9":53.9660791829,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:41:    "chi2":13.5553723813,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:43:    "delta_aic_vs_FREE_C9":-1.3559901954,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:55:    "delta_aic_vs_FREE_C9":53.9660791829,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:67:    "delta_aic_vs_FREE_C9":-0.1982697277,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:79:    "delta_aic_vs_FREE_C9":52.1596229368,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:91:    "delta_aic_vs_FREE_C9":-0.1297765399,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:41:| variant | edge weight w_{vw} | meaning |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:67:| model | k | chi^2 | A_hat | dAIC vs FREE_C9 | r vs exp | r vs cos |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:69:| FREE_C9 reference         | 1 | 6.70 | DC9 = -0.154 |  0.00 | -     | -     |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:72:| **FULL_LIFT[UNWEIGHTED] GREENS**     | 1 | **6.50** | **+0.178** | **-0.21** | **0.997** | 0.881 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:95:  (r = 0.997) and `PHI_ARITHMETIC_GREENS` (r = 0.899 — fails); marginal for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:99:- **dAIC vs FREE_C9 <= 0:** YES for all GREENS variants (-0.21, -0.10,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:103:criterion: r = 0.997 with the continuum Layer-1 kernel, dAIC vs FREE_C9 = -0.21,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:117:the continuum exp(-|x|/phi) kernel is r = 0.997 across 8 LHCb bin centres.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:119:beats FREE_C9 on AIC (dAIC = -0.21) and reaches chi^2 = 6.50 (vs 5.90 for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:164:matches the continuum derivation at r = 0.997 with one fitted amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:165:and beats a global C_9 shift on AIC. The proper Hodge-edge-space
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:1:model,chi2,aic,delta_aic_vs_FREE_C9,fit_param
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:2:FREE_C9_linear,39.3034,41.3034,0.0000,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:3:FREE_C9_nonlinear@linear-best-fit,66.5964,68.5964,0.0000,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:4:FREE_C9_nonlinear_refit,40.8907,42.8907,0.0000,DC9=-1.002
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:6:VFD_nonlinear@linear-best-fit,82.2408,84.2408,15.6444,A=+1.594
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:15:profile and FREE\_C9's flat profile compress the four LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:17:better $\chi^{2}$ ($\Delta\mathrm{AIC}=-1.67$). Under the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:22:$\Delta\mathrm{AIC}=+1.09$. Across five fits the non-linear stacked
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:23:Akaike weight is $w_{\mathrm{VFD}}=0.35$ vs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:24:$w_{\mathrm{FREE\_C9}}=0.65$, a mild preference for the constant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:33:preferred explanation under AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:44:Empirically the per-bin linearisation residual on LHCb 2025 reaches
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:75:$A_{S}=+4.98$ is roughly $4\times$ larger in absolute terms; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:78:sensitivity by $\langle 1/\sqrt{F_{L}(1-F_{L})}\rangle\approx 2.2$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:81:is $+4.98$, a factor-of-2 unexplained residual. We do \emph{not}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:82:characterise this as a clean basis-effect victory: the residual is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:123:alternative explanations of the LHCb 2025 result:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:127:  $A\in[+1.36, +1.85]$ in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:130:  in Mode B, worse than the $+2$ AIC penalty for the extra parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:133:  $A=+1.57\pm 0.16$, $100\,\%$ positive, in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:140:centre-peaked Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:141:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9 in Mode B; vs $-1.67$ for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:143:parameter. The geometric kernel and the free Gaussian capture the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:62:(\ref{eq:dirichlet_mode}) fit the LHCb 2025 $P_{5}'$ data at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:63:$\Delta\mathrm{AIC}\approx -7$ vs $\mathrm{FREE\_C9}$ on $P_{5}'$ alone
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:67:AIC penalty: $c_{3}/c_{1} = 0.18$, well below any $\varphi$-rational
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:130:\eqref{eq:kappa_lift} on the LHCb 2025 bin centres is $r=0.997$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:133:together with the continuum exponential and the LHCb 2025 bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:143:$e^{-|x|/\varphi}$ from Layer 1, with empirical correlation $r=0.997$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:155:edge-weighting schemes are admissible: unweighted ($w_{vw}=1$),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:157:($w_{vw}=\sqrt{\omega_{+}(v)\,\omega_{+}(w)}$), and $\varphi$-cocycle
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:158:arithmetic mean ($w_{vw}=\tfrac{1}{2}[\omega_{+}(v)+\omega_{+}(w)]$).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:161:continuum kernel $e^{-|x|/\varphi}$ and to the LHCb 2025 $P_{5}'$ data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:165:criterion ($\chi^{2}$ against the LHCb 2025 single-observable fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:173:        $\chi^{2}$ vs LHCb 2025 $P_{5}'$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:176:unweighted Laplacian          & $\mathbf{0.9968}$ & $\mathbf{13.555}$ & $1$ on both \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:194:same if only the geometric criterion had been applied, and the AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:197:\S\ref{sec:limitations}: the data was looked at first, and only later
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:14:analysis on LHCb 2025 (\S\ref{subsec:joint_fit}) gives different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:16:$\Delta\mathrm{AIC}$ of opposite sign vs $\mathrm{FREE\_C9}$ (see
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:21:non-linear $\Delta\mathrm{AIC}$ result. Numbers below are quoted
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:22:under Mode B and should be read accordingly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:48:the LHCb 2025 four-observable joint fit, $N=500$ trials. Sign-stable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:64:   VFD $A$ & $\Delta\mathrm{AIC}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:71:\caption{Region-split fits on the LHCb 2025 four-observable joint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:81:SM theory is least reliable — is the region where VFD's AIC advantage
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:95:model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & params \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:100:charm-loop Gaussian            & 2 & 35.41 & 39.41 & $-1.91$ & $A=+1.83$, $\sigma=8.96\,\mathrm{GeV}^{2}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:103:\caption{Joint-fit comparison on LHCb 2025 four observables.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:104:Adding $C_{10}$ does not help. The free centre-peaked Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:105:(charm-loop nuisance proxy) achieves a slightly lower AIC than the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:112:$+2$ AIC penalty for the extra parameter; the data does not want
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:113:$\Delta C_{10}$ at this level. The charm-loop Gaussian — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:116:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9, vs $-1.67$ for VFD), at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:118:for the cost of $1$ AIC unit, $\Delta\mathrm{AIC}_{\mathrm{charm\,vs\,VFD}}=-0.24$:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:165:test (Mode B) & criterion & result \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:168:                                & \textsc{pass} (Mode B; $99.8\,\%$ positive, CI $\pm 15\,\%$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:170:                                & \textsc{pass} (Mode B; 3/3 regions $\Delta\mathrm{AIC}<0$, all $A>0$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:172:                                & \textsc{pass} (Mode B; $\Delta\mathrm{AIC}=+1.73$ vs FREE\_C9) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:173:3b. charm-loop Gaussian         & VFD competitive at same shape level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:174:                                & \textsc{partial} (Mode B; $\Delta\mathrm{AIC}_{\mathrm{charm\,vs\,VFD}}=-0.24$, charm $k=2$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:176:                                & \textsc{pass} (Mode B; $100\,\%$ positive, CI $\pm 15\,\%$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:181:the linearised $\Delta\mathrm{AIC}$ values quoted above do not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:185:\caption{Stress-test acceptance summary on the LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:188:to the non-linear regime, but Mode-B AIC numbers do not.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.csv:2:FULL_LIFT[UNWEIGHTED]_GREENS,0.996799,13.5554,1,1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:123:to estimate the contamination from residual backgrounds. Inaccuracies in the simulation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:193:hadrons are misidentified as muons, are negligible. The residual contamination from peak-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:359:results when fitting pseudoexperiments and data, with residual discrepancies attributed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:378:systematic uncertainties typically arise from the hardware trigger correction, from residual
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:385:uncertainty is due to the residual backgrounds for the normalisation mode.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:482:4.0< q2 <6.0 GeV2/c4 bins, with tension at the level of 2.5 and 1 .9σ (2.2 and 1.7σ). The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:811:power corrections, and new physics, JHEP05(2013) 043,arXiv:1212.2263.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:863:low recoil, Phys. Rev.D87(2013) 034016,arXiv:1212.2321.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:879:standard model, Phys. Rev.D93(2016) 054041,arXiv:1412.2955.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:3:Per-dataset AIC deltas and Akaike weights, plus stacked weight.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:6:| dataset | FREE_C9 ΔAIC | VFD ΔAIC | w(FREE_C9) | w(VFD) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:16:- log-evidence(FREE_C9) − log-evidence(VFD) = 0.627
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:17:- Total ΔAIC sum (FREE_C9 vs VFD): -1.253
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:21:| FREE_C9 | 0.6517 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:22:| VFD_GREEN_600CELL | 0.3483 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:24:Auxiliary check: under the null hypothesis P(VFD lower AIC on all 5 fits) = $1/2^{5}$ = 0.0312.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:63:    lines.append("Data criterion: chi^2 against LHCb 2025 P5' on the joint fit.")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:100:            "treated as k>=2 in AIC comparisons."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:36:    3. VFD_GREEN_600CELL is AIC/BIC competitive with FREE_C9.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:143:    delta_aic_vs_FREE_C9: float; A: float; DC9_eff_mean: float; notes: str = ""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:214:        _warn_bound(data["dataset"], f"FREE_C9 ΔC9 {free_warn}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:231:        "FREE_C9": FitOutcome(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:232:            data["dataset"], p["decay"], "FREE_C9", n, 1,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:325:            "FREE_C9_chi2": fits["FREE_C9"].chi2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:326:            "FREE_C9_DC9": fits["FREE_C9"].A,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:330:            "delta_aic": fits["VFD"].delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:363:                "delta_aic_vs_FREE_C9": fr.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:420:                  f"n_data={r['n_data']}, FREE_C9 chi^2={r['FREE_C9_chi2']:.2f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:421:                  f"DC9={r['FREE_C9_DC9']:+.3f}, "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:423:                  f"dAIC={r['delta_aic']:+.3f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:431:    print(f"  All ΔAIC <= 0?     {(vfd['delta_aic_vs_FREE_C9'] <= 0).all()}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:1:model,k_params,chi2,amplitude,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,correlation_with_exp,correlation_with_cos,eigenvalue,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:2:FREE_C9,1,14.91136257673117,-1.3771673074587851,0.0,7.0000330721695825,,,,global C9 shift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:5:FULL_LIFT[UNWEIGHTED]_GREENS,1,13.555372381338534,1.684032143799957,-1.3559901953926374,5.644042876776945,0.9967985381030878,0.8811748187990005,0.38196601125011054,"shell-mean psi = [0.788, 0.813, 0.864, 0.89, 1.0, 0.89, 0.864, 0.813, 0.788]"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:5:Data criterion: chi^2 against LHCb 2025 P5' on the joint fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:9:| FULL_LIFT[UNWEIGHTED]_GREENS | 0.9968 | 13.555 | 1 | 1 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:13:- Pure-geometry winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (corr with continuum kernel = 0.9968)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:14:- LHCb-data winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (χ² = 13.555)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:10:\item \textbf{LHCb 2025} — $B^{0}\!\to\!K^{*0}\mu^{+}\mu^{-}$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:70:\subsection{Linearised response (Mode B; reported as diagnostic)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:87:This `Mode B' analysis is retained for two reasons: (i) it
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:90:(ii) the difference between linearised and non-linear $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:91:quantifies the non-linearity. On the LHCb 2025 joint fit the per-bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:92:linearisation residual reaches $4.3\sigma$ (mean $0.7\sigma$ across
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:94:$\Delta\mathrm{AIC}$ drifts from $-1.67$ (linearised) to $+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:95:(non-linear refit), a $2.77$-AIC-unit shift that flips the sign of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:109:best-fit on the LHCb 2025 4-observable joint fit is $-1.00$, lower
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:115:We use a Gaussian $\chi^{2}$ likelihood
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:125:$\mathrm{AIC}=\chi^{2}+2k$ \citep{Akaike1974} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:138:\item Charm-loop Gaussian — a free-amplitude, free-width Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:150:$\mathrm{xtol}=5\times 10^{-4}$; for Mode B the optimiser is Powell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:180:linearised optimiser (Mode B) & \texttt{scipy.minimize} Powell, tol $10^{-7}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:4:where Delta_M = AIC_M - AIC_min over the model set {FREE_C9, VFD_GREEN_600CELL}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:8:log-evidence is the sum of the AIC differences halved.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:75:        w.writerow(["dataset", "model", "AIC_delta", "akaike_weight"])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:85:    lines.append("Per-dataset AIC deltas and Akaike weights, plus stacked weight.")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:89:    lines.append("| dataset | FREE_C9 ΔAIC | VFD ΔAIC | w(FREE_C9) | w(VFD) |")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:94:            f"| {deltas.get('FREE_C9', 0):.3f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:96:            f"| {weights.get('FREE_C9', 0):.4f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:102:    lines.append(f"- log-evidence(FREE_C9) − log-evidence(VFD) = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:103:                 f"{log_w_total['FREE_C9'] - log_w_total['VFD_GREEN_600CELL']:.3f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:104:    lines.append(f"- Total ΔAIC sum (FREE_C9 vs VFD): "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:105:                 f"{-2*(log_w_total['FREE_C9'] - log_w_total['VFD_GREEN_600CELL']):.3f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016a_akaike_stack.py:115:                 f"P(VFD lower AIC on all {len(per_dataset)} fits) = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:30:model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & params \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:33:\textbf{VFD\_GREEN\_600CELL} & 1 & \textbf{12.96} & \textbf{14.96} & $\boldsymbol{-0.24}$ & $A=+4.98$, $\Delta C_{9}^{\mathrm{eff}}=-3.85$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:39:AIC by $0.24$ unit at equal $k=1$. Both fits give a sign-uniform
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:41:$\Delta\mathrm{AIC}=-0.08$; values are essentially equivalent at this
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:46:The 500-trial bootstrap on bins (run under Mode B, retained as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:49:poorly constrained. Region splits under Mode B give $A=+5.31$ in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:125:$P$-basis (where LHCb 2025, CMS 2025, LHCb 2015, LHCb 2021 all
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:135:\;\approx\; A_{P\text{-basis}}\times 2.2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:138:$B\to K^{*}$ (above). Using the non-linear LHCb 2025 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:142:A^{\mathrm{Bs}\to\phi}_{S, \text{predicted}} \;\approx\; +1.14 \times 2.2 \;\approx\; +2.5.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:144:The non-linear refit gives $A^{\mathrm{Bs}\to\phi}_{S, \text{observed}} = +4.98$, a factor of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:151:best-fit. We attribute the residual gap to:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:156:\item the per-bin scaling factor scatter $\pm 20\,\%$ around $2.2$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:163:residual that is at least as large as the basis-correction itself;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:176:$A$ same sign as the four $B\to K^{*}$ fits & \textsc{pass} ($A_{\mathrm{NL}}=+4.98>0$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:178:VFD AIC competitive with FREE\_C9   & \textsc{observed} (marginal $\Delta\mathrm{AIC}=-0.24$, $w_{\mathrm{VFD}}\approx 0.53$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:182:basis correction predicts amplitude & \textsc{partial} (predicted $+2.5$ vs observed $+4.98$; factor $\sim 2$ unexplained gap) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:186:four $B\to K^{*}$ fits and AIC-degenerate with FREE\_C9; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:14:    4. LHCb 2025 — current dataset (8.4 fb^-1, B0 -> K*0 mumu) — reference.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:28:    - VFD_GREEN_600CELL AIC <= FREE_C9 AIC on every dataset (or comparable).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:369:    """LHCb 2025 8.4 fb^-1 — already in `data/raw/hepdata/extracted` config_2."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:398:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:415:    """Fit FREE_C9 and VFD_GREEN_600CELL on a single dataset. Returns both."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:438:    # FREE_C9 fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:471:        "FREE_C9": FitResult(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:472:            dataset=data["dataset"], decay=decay, model="FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:474:            delta_aic_vs_FREE_C9=0.0, A=DC9_free,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:480:            delta_aic_vs_FREE_C9=aic_vfd - aic_free, A=A_vfd,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:537:                "delta_aic_vs_FREE_C9": fr.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:559:    print("Per-dataset summary (VFD vs FREE_C9):")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:571:    print(f"All VFD AIC <= FREE_C9?  "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:572:          f"{(vfd['delta_aic_vs_FREE_C9'] <= 0).all()}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:1:"""Gaussian chi-squared likelihood for binned observables.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:43:    residual = obs - pred
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:51:        return float(np.sum((residual / err) ** 2))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:59:        solved = np.linalg.solve(cov_sym, residual)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:62:    return float(residual @ solved)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:74:    """Akaike information criterion under Gaussian likelihood (constant terms dropped)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:79:    """Bayesian information criterion under Gaussian likelihood (constants dropped)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:75:\item On the LHCb 2025 dataset, the geometry-derived kernel and a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:77:  parameter cost ($k=1$ each), with $\Delta\mathrm{AIC}=+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:82:  LHCb 2025 (8.4\,fb$^{-1}$), and the cross-channel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:83:  $B_{s}\!\to\!\phi\mu\mu$ — the non-linear $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:86:  $w_{\mathrm{VFD}}=0.35$ vs $w_{\mathrm{FREE\_C9}}=0.65$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:95:  correction a residual $\sim 50\,\%$ overshoot remains, attributable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:102:\item That the kernel beats $\mathrm{FREE\_C9}$ on AIC. It does not,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:104:  Gaussian also fits comparably (\S\ref{sec:stress}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:116:amplitude per dataset is consistent (sign-uniform; AIC-degenerate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:1:"""VFD closure-residual model for ΔC9_VFD(q^2) = -A * R(q^2).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:3:Three constrained residual shapes are exposed:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:41:# all three are run and their AIC/BIC are reported so no post-hoc cherry-picking
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:233:def closure_residual_q2(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:251:    sigma : Gaussian width in GeV^2 (threshold mode only).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:263:        residual = np.ones_like(q2)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:266:        residual = np.cos(phase_scale * np.log(q2 / Q2_REF_GEV2) + theta)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:273:        residual = 0.5 * (b1 + b2)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:279:        residual = 0.5 * (b1 + b2)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:282:        residual = kappa_shape(q2, mode=mode)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:287:    return -amplitude * residual
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:291:    """Return (observables, bin_indices, q2_centres, residual_grid_centres).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:293:    The residual grid centres are per-row (one value per data point), since
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:321:    """Fit the VFD closure-residual model to observed data.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:341:            return closure_residual_q2(q2_centres, a, mode=mode)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:344:            return closure_residual_q2(q2_centres, a, mode=mode, theta=float(th))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:347:            return closure_residual_q2(q2_centres, a, mode=mode, sigma=float(sig))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:350:            return closure_residual_q2(q2_centres, a, mode=mode)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:353:            return closure_residual_q2(q2_centres, a, mode=mode)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:376:    # Recompute pure (un-regularised) chi^2 for AIC/BIC reporting.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:6:ΔAIC = -1.67 vs FREE_C9, A = +1.59, ΔC9_eff = -1.37 — in five ways:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:51:| region | q²_range (GeV²) | n_bins | n_data | FREE_C9 χ² | FREE_C9 ΔC9 | VFD χ² | VFD A | VFD ΔC9_eff | ΔAIC (VFD − FREE) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:57:VFD beats FREE_C9 in **every** q² region. The amplitude varies in a 40% band
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:66:| model | k | χ² | AIC | BIC | ΔAIC vs FREE_C9 | params |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:68:| FREE_C9                 | 1 | 39.32 | 41.32 | 42.78 |   0.00 | ΔC9 = −1.34 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:70:| FREE_C9 + FREE_C10      | 2 | 39.05 | 43.05 | 45.98 |  +1.73 | ΔC9 = −1.40, ΔC10 = +0.19 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:71:| Charm-loop Gaussian (free A, σ) | 2 | 35.41 | 39.41 | 42.34 |  −1.91 | A = +1.83, σ = 8.96 GeV² |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:75:- **Adding a free C10 does not help.** The 2-WC fit (FREE_C9 + FREE_C10)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:76:  reduces χ² by only 0.27 over FREE_C9 alone, while paying 2 AIC units for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:78:- **VFD beats FREE_C9 by a clean 1.67 AIC units at the same parameter cost.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:79:- **The charm-loop Gaussian nuisance** (free amplitude A and free width σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:81:  35.4 but costs an extra parameter; its raw ΔAIC is −1.91 vs FREE_C9.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:82:  Versus VFD it gains 0.24 χ² for the cost of 1 AIC unit, giving ΔAIC = −0.24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:116:In every test above, only the amplitude `A` (or, for FREE_C9 / FREE_C9+C10,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:128:| 2. q² region splits | universality across regions, no sign flip | PASS (3/3 regions ΔAIC < 0, all A>0, all ΔC9_eff<0) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:129:| 3. C9 + C10 | adding C10 does not displace VFD | PASS (FREE_C9+C10 ΔAIC = +1.73; VFD wins) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:130:| 3. charm-loop nuisance | VFD competitive at same shape level | PARTIAL — charm-loop ΔAIC = −1.91 (k=2) vs VFD −1.67 (k=1); VFD wins per-parameter |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:139:model that gains over VFD is a 2-parameter centre-peaked Gaussian, and that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:140:gain is below 1 AIC unit — consistent with picking up the same structural
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:156:- The charm-loop Gaussian is a phenomenological proxy, not a physical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:157:  charm-loop calculation. It captures whether the residual prefers a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_regions.csv:1:dataset,region,q2_range,n_bins,n_data,FREE_C9_chi2,FREE_C9_DC9,VFD_chi2,VFD_A,VFD_DC9_eff,delta_aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:9:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:20:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:22:    "lambda_max_used":2.2917960675
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:31:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:33:    "lambda_max_used":2.2917960675
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:42:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:44:    "lambda_max_used":2.2917960675
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:53:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:55:    "lambda_max_used":2.2917960675
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:64:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:75:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:86:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:97:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:108:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:119:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:130:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:141:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:152:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:163:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:174:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:185:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:196:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:207:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:218:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:229:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:240:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:251:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:262:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:273:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:284:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:295:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:306:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:317:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:328:    "delta_aic_vs_FREE_C9":-0.1170177074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:339:    "delta_aic_vs_FREE_C9":-0.1291318706,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:350:    "delta_aic_vs_FREE_C9":-0.1291318706,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:361:    "delta_aic_vs_FREE_C9":-0.1291318706,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:372:    "delta_aic_vs_FREE_C9":-0.2070713875,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:383:    "delta_aic_vs_FREE_C9":-0.2070713875,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:15:    - FREE_C9 (k = 1, one global Delta_C9)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:24:    - VFD_GREEN_600CELL AIC <= FREE_C9 AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:131:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:132:    delta_bic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:164:    a_v, b_v = _row("FREE_C9", "reference", 1, float(r.fun), len(values))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:167:        "FREE_C9", "reference", 1, float(r.fun), a_v, b_v, 0.0, 0.0, delta_hat,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:311:    free = next(r for r in rows if r.model == "FREE_C9")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:313:        if np.isnan(r.delta_aic_vs_FREE_C9):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:314:            r.delta_aic_vs_FREE_C9 = r.aic - free.aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:315:            r.delta_bic_vs_FREE_C9 = r.bic - free.bic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:327:            "delta_aic_vs_FREE_C9": r.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:328:            "delta_bic_vs_FREE_C9": r.delta_bic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:359:            "delta_aic_vs_FREE_C9", "effective_delta_c9_mean",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:1:model,role,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,coefficients,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:2:SM,baseline,0,10.177833873611222,10.177833873611222,10.177833873611222,1.4732607826469941,2.2739253735958034,{},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:3:FREE_C9,reference,1,6.704573090964229,8.704573090964228,8.784014632644064,0.0,0.8006645909488093,{'delta_c9': -0.15362183379908242},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:6:DIRICHLET_M2,primary,2,6.163031129936566,10.163031129936567,10.321914213296237,1.4584580389723385,2.2591226299211478,"{'c1': 0.21239003884560714, 'c3': 0.03791247788535561}","even-parity Dirichlet on [-x_max, x_max]; psi_k = cos((2k-1) pi x / (2 L))"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/processed/flavio_cache.json:286: "Bs->phimumu|FL|15.0000|17.0000|dC9=-0.5000": 0.34887540590922045,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_regions.csv:1:region,q2_range,n_bins,n_data,FREE_C9_chi2,FREE_C9_DC9,FREE_C9_aic,VFD_chi2,VFD_amplitude,VFD_DC9_eff,VFD_aic,delta_aic_VFD_vs_FREE
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_regions.csv:2:low_q2,"(0.06, 4.0)",3,12,20.863885005208587,-1.1325436424697062,22.863885005208587,20.771149995718762,1.3974,-1.1241015713252065,22.771149995718762,-0.09273500948982516
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/sm_baseline.py:48:        SMResponse(sm_value=+0.3484, dO_dC9=+0.0003),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:5:CMS 2025, LHCb 2025). WO-015 asks: does the same kernel — with no shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:41:| model | k | χ² | AIC | BIC | ΔAIC vs FREE_C9 | params |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:43:| FREE_C9 (k=1)             | 1 | 13.20 | 15.20 | 16.37 |  0.00 | ΔC9 = **−4.37** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:52:| 3. VFD AIC competitive with FREE_C9      | PASS (marginal, ΔAIC = −0.08) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:69:angular slopes dO/dC9 are tiny (≤ 0.001), so any non-zero residual
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:75:| region | q² range | n_data | FREE_C9 χ² | FREE_C9 ΔC9 | VFD χ² | VFD A | ΔAIC |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:84:FREE_C9 (ΔAIC = 0.00) and gives A = +5.31 (broadly consistent with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:109:amplitude for Bs → φμμ is **+2.5**, vs +1.6 for B → K*. A residual
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:117:3. Limited statistics (3 fb⁻¹ vs 8.4 fb⁻¹ for LHCb 2025).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:129:- VFD ties or marginally beats FREE_C9 (k=1 vs k=1) on the global fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:161:| dataset | decay | n | A | ΔC9_eff | ΔAIC | source |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:166:| LHCb 2025         | B⁰ → K*⁰ μμ | 32 | +1.59 | −1.37 | −1.67 | WO-014 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:174:- **beats or ties FREE_C9 in AIC on every dataset**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:1:n_modes,rel_recon_err,r_vs_full_kernel,r_vs_continuum_exp,chi2_p5p,aic_p5p,delta_aic_vs_FREE_C9,amplitude,lambda_max_used
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:3:2,0.07587406519107227,,,6.704573090964229,8.704573090964228,0.0,0.1536218337990829,2.2917960675006275
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:4:3,0.07587406519107227,,,6.704573090964229,8.704573090964228,0.0,0.1536218337990829,2.291796067500632
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:5:4,0.07587406519107227,,,6.704573090964229,8.704573090964228,0.0,0.1536218337990829,2.2917960675006332
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:6:5,0.07587406519107227,,,6.704573090964229,8.704573090964228,0.0,0.1536218337990829,2.2917960675006355
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/flavio_predictor.py:5:project's hand-tabulated `sm_baseline` is fixed to the LHCb 2025 8-bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:18:    5. EDGE-SPACE lift: w_{vw} = phi^{(kappa(v) + kappa(w))/2} (geometric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:35:    - dAIC vs FREE_C9 <= 0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:225:    """Compute edge-weighted adjacency A_w[i,j] = w_{ij} * adj[i,j].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:227:    mode = 'geometric'  : w_{ij} = phi^{(kappa_i + kappa_j) / 2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:228:    mode = 'arithmetic' : w_{ij} = (phi^{kappa_i} + phi^{kappa_j}) / 2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:229:    mode = 'unweighted' : w_{ij} = 1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:422:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:474:    # FREE_C9 reference
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:514:            delta_aic_vs_FREE_C9=aic_eig - free_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:531:            delta_aic_vs_FREE_C9=aic_g - free_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:538:        {"model": "FREE_C9", "k_params": 1, "chi2": free_chi2, "amplitude": float(free.x[0]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:539:         "delta_aic_vs_FREE_C9": 0.0, "delta_aic_vs_KAPPA_EXP": free_aic_v - exp_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:543:         "delta_aic_vs_FREE_C9": exp_aic_v - free_aic_v, "delta_aic_vs_KAPPA_EXP": 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:551:            "delta_aic_vs_FREE_C9": r.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:584:    print(res["models"][["model", "k_params", "chi2", "amplitude", "delta_aic_vs_FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:9:    "delta_aic_vs_FREE_C9":4.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:10:    "delta_bic_vs_FREE_C9":3.5624284566,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:18:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:24:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:25:    "delta_bic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:40:    "delta_aic_vs_FREE_C9":6.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:41:    "delta_bic_vs_FREE_C9":6.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:56:    "delta_aic_vs_FREE_C9":4.8317905293,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:57:    "delta_bic_vs_FREE_C9":5.6043792516,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_form_factor_variation.csv:21:19,1.4651325956960104,42.21115510963162,ok
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:41:5. Report chi^2, AIC, the eigenvalue lambda_1, and Pearson correlations
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:48:| variant | chi^2 | A_hat | lambda_1 | r vs exp | r vs cos | dAIC vs FREE_C9 | dAIC vs KAPPA_EXP |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:50:| FREE_C9            | 6.70 | DC9 = -0.154 | -    | -     | -     |  0.00 | +0.80 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:75:- **dAIC vs FREE_C9 <= 0:** YES, all three variants.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:104:4. **All three discrete variants beat FREE_C9.** Any of these single-amplitude,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:105:   shape-frozen lifts compresses P5' better than a global C_9 shift on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:106:   The continuum exp kernel still wins by ~0.3-0.5 AIC, but with only 8 bins
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:140:real LHCb P5' data with a single amplitude and beat FREE_C9 on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:152:  -> single-amplitude fit, dAIC vs FREE_C9 = -0.28 on real LHCb P5' data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.csv:2:Bs2phi-LHCb-2015,Bs->phimumu,FREE_C9,24,1,13.195107020387567,15.195107020387567,16.373160850735513,0.0,-4.365832398383627,-4.365832398383627,DC9=-4.366
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:3:**Hypothesis under test.** The B0 -> K*0 mu mu Re(C9) residual is dominated by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:5:bounded resonator, with maximum residual amplitude near the kinematic edges
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:19:Compared against the prior champion `kappa_exponential` and the FREE_C9 reference.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:23:`FREE_C9` reference: chi^2 = 6.7046, AIC = 8.7046.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:25:| mode | k | chi^2 | dAIC vs FREE_C9 | eff DC9 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:35:| `VFD_KAPPA_REFLECTIVE_EDGE`    | 1 | 8.927 | **+2.22** | -0.120 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:41:x           : [-2.77 -2.45 -2.08 -1.65 -1.15  0.04  1.10  1.60]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:55:  **WORSE** than the FREE_C9 control (dAIC > +1.9), i.e. worse than a global
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:63:not match the P5' data: the residual rises towards the midpoint and decays
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.csv:1:model,role,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,delta_bic_vs_FREE_C9,effective_delta_c9_mean,per_observable_delta_c9,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.csv:3:FREE_C9,reference,1,204.45608467044792,206.45608467044792,207.2286733926877,0.0,0.0,0.1938680707162974,"{'BR': 0.1938680707162974, 'P5p': 0.1938680707162974}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:48:46,1.6736283493538997,42.268291357870496
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:62:60,1.6083839623600897,42.23966859653963
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:136:134,1.511086878549419,32.2965360467998
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:156:154,1.6350758435148438,42.24238720224522
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:293:291,1.6127288116182092,42.21765023362732
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:319:317,1.4263878833233274,42.209249843580565
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:353:351,1.7314166679120127,42.28516288048897
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:379:377,1.6189311702374043,42.25198393497948
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:390:388,1.864338016410075,42.28697063697096
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_bootstrap_bins.csv:434:432,1.6350758435148434,42.24238720224521
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:7:    "delta_aic_vs_FREE_C9":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:15:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:19:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:31:    "delta_aic_vs_FREE_C9":-0.8006645909,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:43:    "delta_aic_vs_FREE_C9":-0.4620994693,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:55:    "delta_aic_vs_FREE_C9":-0.4620994693,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:67:    "delta_aic_vs_FREE_C9":-0.279376236,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.csv:1:model,k_params,chi2,amplitude,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,correlation_with_exp,correlation_with_cos,eigenvalue,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.csv:3:FREE_C9,1,6.704573090964229,-0.15362183379908242,0.0,0.8006645909488093,,,,global C_9 shift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:6:that compresses the LHCb P5' anomaly with a single amplitude (dAIC = -0.80
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:7:vs FREE_C9). WO-005 ruled out three boundary-anchored variants (sinh,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:109:champion, dAIC = -0.80), the empirical kernel is identified as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:117:If `DIRICHLET_M3` adds nothing (dAIC vs M2 around +1 from the AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:150:| model | k | chi^2 | AIC | dAIC vs FREE_C9 | dAIC vs KAPPA_EXP |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:152:| SM             | 0 | 10.18 | 10.18 | +1.47 | +2.27 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:153:| FREE_C9        | 1 |  6.70 |  8.70 |  0.00 | +0.80 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:156:| DIRICHLET_M2   | 2 |  6.16 | 10.16 | +1.46 | +2.26 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:166:1. **The Dirichlet ground state DIRICHLET_M1 beats FREE_C9 (dAIC = -0.44).**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:172:   AIC of each other.** They are the same shape topologically (centre-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:179:   by only 0.10 over DIRICHLET_M1 — far below the 2-AIC threshold for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:268:amplitude k = 1, both peak at the charmonium midpoint, and their AIC values
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:278:P5' alone — both are consistent with the data within 0.4 AIC. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:50:| [5.00, 8.00] | 0.0513 | 0.1128 | 2.20 | 2.07 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:71:LHCb 2025 / CMS 2025 / LHCb 2015 / LHCb 2021 all publish the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:83:              ≈ A_P-basis × ~2.2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:86:**Predicted A_S** = 1.594 × 2.2 ≈ **+3.5**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:104:the data is most informative), the kernel ties FREE_C9 with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:116:| LHCb 2025 (P-basis)  | P | +1.594 | +1.594 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:129:  is sign-uniform, ΔAIC ≤ 0 in every fit; the residual amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:1:model,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,params
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:2:FREE_C9,1,39.31675580142509,41.31675580142509,42.78249170422482,0.0,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:4:FREE_C9 + FREE_C10,2,39.049662892777846,43.049662892777846,45.981134698377296,1.7329070913527573,"DC9=-1.395, DC10=+0.186"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:5:"Charm-loop Gaussian (free A, sigma)",2,35.41169043468848,39.41169043468848,42.34316224028793,-1.9050653667366078,"A=+1.832, sigma=8.960 GeV^2"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:19:    - chi^2 / AIC of the amplitude-only fit to LHCb P5'.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:29:FREE_C9 reference: chi^2 = 6.7046, AIC = 8.7046.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:30:Full-kernel correlation with continuum exp(-|x|/phi): r = 0.997.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:32:| N modes | rel. recon. err | r vs full kernel | r vs cont. exp | chi^2 P5' | dAIC vs FREE_C9 | A_hat | lambda_max |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:35:|   2-5 | 7.59e-2 |   nan |   nan | 6.7046 |  0.00 | 0.154 |  2.29 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:41:|   100 | ~1e-14 | 1.000 | 0.997 | 6.498 | -0.21 | 0.178 | 14.47 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:42:|   120 (full) | ~1e-14 | 1.000 | 0.997 | 6.498 | -0.21 | 0.178 | 15.71 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:49:chi^2 stays at 6.7046 (= FREE_C9 exactly) and the relative L^2 error stays
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:74:Every truncation level N >= 9 has dAIC vs FREE_C9 strictly negative, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:75:the dAIC monotonically improves as N grows (-0.117 -> -0.129 -> -0.207).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:83:monotonic 0.849 -> 0.944 -> 0.997 as N grows.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:88:exp(-|x|/phi) at r = 0.997. This is the WO-009 result re-derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/constants.py:17:# q^2 reference scale used in log-phase residual (GeV^2).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/constants.py:27:# Golden ratio - used as a default phase scale in log-phase closure residual.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:3:2,2.2917960675006275,5.204170427930421e-18,1.946385009081278e-18,1.946385009081278e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:4:3,2.291796067500632,-1.734723475976807e-17,-6.487950030270916e-18,6.487950030270916e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:5:4,2.2917960675006332,0.0,0.0,0.0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:6:5,2.2917960675006355,1.4153582184214103e-16,5.293508460119633e-17,5.293508460119633e-17
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:16:15,8.999999999999996,2.0816681711721685e-17,2.2187973913740457e-18,2.2187973913740457e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:34:33,11.999999999999995,-2.211772431870429e-17,-1.786285336158119e-18,1.786285336158119e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:77:76,14.0,2.7755575615628914e-17,1.929887443338239e-18,1.929887443338239e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:84:83,14.000000000000007,3.2959746043559335e-17,2.2917413389641574e-18,2.2917413389641574e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:3:**Question.** WO-013 showed the universality result on the LHCb 2025 dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:25:| LHCb 2025 (ref.)  | B⁰→K*⁰ μμ  | 2512.18053 | ins3094698 | 8.4 fb⁻¹   | 8 (config_2 — already in repo) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:42:| dataset | n | FREE_C9 χ² | FREE_C9 ΔC9 | VFD χ² | **VFD A** | VFD ΔC9_eff | ΔAIC (VFD−FREE) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:45:| LHCb 2021 (B⁺→K*⁺)  | 32 |  27.1 | −2.24 |  26.6 | **+2.72** | −2.33 | −0.55 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:48:| LHCb 2025 (ref)      | 32 |  39.3 | −1.34 |  37.6 | **+1.59** | −1.37 | −1.67 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:57:| VFD AIC ≤ FREE_C9 AIC on every dataset | PASS — ΔAIC < 0 in all 5 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:66:    LHCb 2025:            A = +1.594
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:85:prefers the kernel by 0.55 AIC over a free C9 shift is the relevant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:91:about 7× per-point. Inspecting residuals reveals CMS publishes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:99:affects FREE_C9 and VFD identically**, so the *relative* ΔAIC is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:109:  LHCb 2015, LHCb 2021 B⁺→K*⁺, CMS 2025, plus the existing LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:153:> - LHCb 2025 (8.4 fb⁻¹)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:169:  a free 2-parameter centre-peaked Gaussian (charm-loop proxy) fits
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:2:LHCb-2015,B0->K*mumu,FREE_C9,32,1,31.59959432998963,33.59959432998963,35.06533023278936,0.0,-1.4793748908390585,-1.4793748908390585,DC9=-1.479
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:4:LHCb-2021-Kstplus,B+->K*+mumu,FREE_C9,32,1,27.11607072037183,29.11607072037183,30.581806623171556,0.0,-2.2437859535603693,-2.2437859535603693,DC9=-2.244
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:6:CMS-2025,B0->K*mumu,FREE_C9,24,1,169.35257876006892,171.35257876006892,172.53063259041687,0.0,-1.4870700145558682,-1.4870700145558682,DC9=-1.487
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:8:CMS-2025-noP4p,B0->K*mumu,FREE_C9,18,1,43.21465711778693,45.21465711778693,46.10502887568309,0.0,-1.3549233139256784,-1.3549233139256784,DC9=-1.355
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:10:LHCb-2025,B0->K*mumu,FREE_C9,32,1,39.30340988916652,41.30340988916652,42.769145791966245,0.0,-1.340331410060973,-1.340331410060973,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:9:    "delta_aic_vs_FREE_C9":1.4732607826,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:10:    "delta_aic_vs_KAPPA_EXP":2.2739253736,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:17:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:23:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:37:    "delta_aic_vs_FREE_C9":-0.8006645909,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:51:    "delta_aic_vs_FREE_C9":-0.4368311136,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:65:    "delta_aic_vs_FREE_C9":1.458458039,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:66:    "delta_aic_vs_KAPPA_EXP":2.2591226299,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:80:    "delta_aic_vs_FREE_C9":2.8587929029,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/Table4.yaml:24:    - asymerror: {minus: -0.348, plus: 0.364}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/Table7.yaml:32:    value: 2.296

exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/main.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/01_introduction.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/02_method.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/03_substrate.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 268ms:
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
    19	\title{A geometry-fixed substrate witness for cortical signatures:\\
    20	       eighteen preregistered correspondences and six drug/sleep EEG\\
    21	       signatures from the 600-cell under H$_4$ Coxeter symmetry}
    22	
    23	\author{%
    24	  Lee Smart\\[2pt]
    25	  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
    26	  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
    27	  \texttt{@vfd\_org}%
    28	}
    29	
    30	\date{April 2026}
    31	
    32	\begin{document}
    33	
    34	\maketitle
    35	
    36	\noindent\textbf{Status:} Preprint, not peer-reviewed.
    37	
    38	\noindent\emph{Headline.}
    39	Once the 600-cell substrate is chosen, its graph structure is fixed:
    40	$|V|=120$ vertices of uniform degree $12$ (forced by H$_4$ transitivity
    41	on the canonical short-edge nearest-neighbour graph), with
    42	$\Ph=(1+\sqrt 5)/2$ entering through the canonical vertex coordinates
    43	and through the response-operator stability shift $\Ph^{-2}$. The
    44	Laplacian spectrum is computed numerically from this graph and is
    45	reported as observed (\S\ref{sec:substrate}). Treated
    46	as an architectural-level substrate with a fixed shifted-Laplacian
    47	response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
    48	it, this single deterministic structure is consistent with eighteen
    49	quantitative correspondences with neuroscience data — preregistered
    50	on 2026-04-18 before any validation run — plus six drug/sleep EEG
    51	signatures of conscious vs unconscious states tested against
    52	literature-derived thresholds on a single deterministic substrate
    53	trajectory at seed~$42$. No shape parameter is tuned to any neural
    54	dataset. The recurrent layer above the substrate adds one
    55	substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
    56	at the graph's average degree and one condition-dependent self-injection
    57	coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
    58	models (\S\ref{sec:chain}) are biologically-motivated design choices,
    59	not measurement-fits.
    60	
    61	\noindent\emph{Scope.}
    62	This paper presents an empirical \emph{substrate witness}: it shows
    63	that a geometry-fixed substrate, with no shape parameters tuned to any
    64	neural dataset, is consistent with eighteen preregistered correspondences
    65	and six EEG signatures. It is not a derivation of consciousness, nor a
    66	selection theorem, nor a uniqueness claim for the 600-cell among regular
    67	4-polytopes. The companion adaptive-closure-transport
    68	preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
    69	4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
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
   171	\input{sections/01_introduction.tex}
   172	\input{sections/02_method.tex}
   173	\input{sections/03_substrate.tex}
   174	\input{sections/04_consciousness_chain.tex}
   175	\input{sections/05_results.tex}
   176	\input{sections/06_stress_tests.tex}
   177	\input{sections/07_cross_domain.tex}
   178	\input{sections/08_discussion.tex}
   179	\input{sections/09_limitations.tex}
   180	\input{sections/10_conclusion.tex}
   181	% =====================================================================
   182	
   183	\section*{Acknowledgements}
   184	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   185	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   186	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   187	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   188	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   189	datasets that made these comparisons possible. Cortical avalanche
   190	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   191	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   192	the propofol microstate comparison uses Brodbeck et
   193	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   194	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   195	and processed data are released under MIT licence at the project
   196	repository~\citep{ariaChessRepo}.
   197	
   198	\section*{Reproducibility}
   199	The complete pipeline (substrate construction, six-signature
   200	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   201	preregistered validation, figure regeneration, this paper) is reproducible
   202	from the project repository~\citep{ariaChessRepo} via the included
   203	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   204	deterministic given seeds; the substrate's spectral decomposition is
   205	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   206	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   207	$\sim 18$\,min.
   208	
   209	\bibliographystyle{plainnat}
   210	\bibliography{references}
   211	
   212	\end{document}

 succeeded in 261ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	Theories of consciousness divide into mechanism-driven proposals
     6	(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
     7	Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
     8	predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
     9	structure-driven proposals (geometric or topological substrates,
    10	neural-population dynamics). The mechanism-driven proposals offer
    11	compelling axiomatic stories; we are not aware of prior work that
    12	has yielded the kind of preregistered multi-domain quantitative
    13	benchmark on real EEG data tested here. The structure-driven
    14	proposals produce numbers but often rely on fitted parameters,
    15	learned weights, or domain-specific calibration.
    16	
    17	This paper takes a deliberately constrained third path. Once a
    18	substrate is chosen, we ask which neuroscience phenomena it is
    19	consistent with under \emph{no} shape parameter tuning, no learned
    20	weights, no subject-level measurement fitting, and no
    21	neural-data-fitted shape parameters. The substrate is the
    22	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    23	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    24	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    25	our knowledge it has not been proposed before as an empirical
    26	candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
    27	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    28	single condition-dependent self-injection coupling $\eta$ and a
    29	single graph-pinned nonlinearity, and test the resulting witness
    30	against eighteen preregistered correspondences plus six companion
    31	drug/sleep EEG signatures.
    32	
    33	\subsection*{What this paper claims}
    34	
    35	We claim a single \emph{substrate witness}: that a geometry-fixed
    36	substrate, with no shape parameters tuned to any neural dataset, is
    37	consistent with eighteen preregistered correspondences (frozen
    38	2026-04-18) and six companion drug/sleep EEG signatures of
    39	conscious vs unconscious states.
    40	
    41	\begin{enumerate}\itemsep=2pt
    42	\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
    43	  is selected, the vertex set ($|V|=120$, all on the unit
    44	  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
    45	  transitivity forces uniform vertex degree (here $12$ on the
    46	  short-edge nearest-neighbour graph); and the Laplacian spectrum is
    47	  computed from the resulting graph and reported as observed, with
    48	  multiplicities matching the expected H$_4$ block sizes
    49	  (\S\ref{sec:substrate}). The response operator
    50	  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
    51	  constructed and the stability shift $\Ph^{-2}$ is chosen as a
    52	  design-level clamp.
    53	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    54	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    55	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    56	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    57	  $[2.73, 3.25]$.
    58	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    59	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    60	  collapse to $0.463\!\times$ wake; propofol modality-switching
    61	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    62	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    63	  recovery deterministically identical to wake; wake cascade-$\alpha$
    64	  in the SOC band.
    65	\item \textbf{Eighteen preregistered correspondences pass.}
    66	  $17/18$ at standard methodology; $18/18$ after a documented
    67	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    68	  test; \emph{no preregistered threshold has been modified}.
    69	\item \textbf{Cross-domain selectivity.} The substrate exhibits
    70	  selective amplification in the two cross-domain tasks tested
    71	  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
    72	  conversation $-4.4$pp lift, within preregistered neutrality bounds)
    73	  and serves as an H$_4$-transitive deterministic null reference for
    74	  cortical functional connectivity (HCP full-cohort descriptive
    75	  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
    76	  $+79.78\sigma$ on raw participation ratio with the node-count caveat
    77	  of \S\ref{ssec:hcp}).
    78	\end{enumerate}
    79	
    80	\subsection*{What this paper does \emph{not} claim}
    81	
    82	\begin{itemize}\itemsep=2pt
    83	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    84	  the unique substrate consistent with these signatures. Other regular
    85	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    86	  build, not a discharged comparison. The 600-cell choice is post-hoc
    87	  motivated by the H$_4$ Coxeter cascade structure and biological
    88	  observables; it is not an a-priori derivation from first principles.
    89	\item \emph{Not a derivation of consciousness.} The substrate witness
    90	  shows quantitative agreement with cortical signatures; it does not
    91	  establish that the substrate \emph{is} consciousness, nor that
    92	  its dynamics implement specific phenomenal content.
    93	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    94	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    95	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    96	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    97	  as the active $M$ is conjectural in that paper and is treated as
    98	  non-load-bearing here. We do not deliver a Lyapunov function on the
    99	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
   100	  nor a formal edge-space decomposition. These are listed as open
   101	  builds in~\S\ref{sec:limitations}.
   102	\item \emph{Not a circuit-level model.} The substrate is at the
   103	  architectural-algorithmic level. We do not identify which neural
   104	  populations implement context rotation or partial emission, only
   105	  that some such mechanisms appear in the substrate's preregistered
   106	  ablation matrix and exhibit strong inter-mechanism coupling.
   107	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   108	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   109	  stability clamp (it makes $\Cph$ strictly positive definite and
   110	  bounds the Green response). It is not derived as a theorem from a
   111	  closure functional. The companion kernel
   112	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   113	\end{itemize}
   114	
   115	\subsection*{Mapping from numerical results to admissible claims}
   116	
   117	To keep this paper inside the substrate-witness scope, we use the
   118	following claim-boundary discipline. Numerical results
   119	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   120	$\mathcal C_{\mathrm{admissible}}$ by the rule
   121	\[
   122	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   123	\qquad
   124	\mathcal C_{\mathrm{admissible}}
   125	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   126	\]
   127	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   128	A result that lands inside its preregistered threshold licenses a
   129	`consistent with' claim. A result that exceeds the preregistered
   130	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   131	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   132	$\sigma$-distance result against an external null
   133	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   134	the biological distribution', not `cortex has drifted from an ideal
   135	polytope'. The claim-boundary rule is summarised in the box below
   136	and applied throughout~\S\ref{sec:results}.
   137	
   138	\medskip
   139	\begin{center}
   140	\fbox{\parbox{0.92\linewidth}{\small
   141	\textbf{What is tested / what is not claimed.}\par
   142	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   143	signatures, on a geometry-fixed substrate with one condition-dependent
   144	parameter $\eta$ and one graph-pinned nonlinearity, against published
   145	biological observables.\par
   146	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   147	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   148	identification; first-principles derivation of $\Ph^{-2}$ shift;
   149	that cortex \emph{is} the 600-cell.
   150	}}
   151	\end{center}
   152	
   153	\subsection*{Layout}
   154	
   155	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   156	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   157	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   158	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   159	\S\ref{sec:chain} adds the recurrent self-model layer above the
   160	substrate (single nonlinearity, single self-injection coupling).
   161	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   162	signatures, eighteen preregistered correspondences, three-way
   163	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   164	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   165	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   166	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   167	discusses the substrate witness and proposes a non-load-bearing
   168	ACT bridge (without claiming a selection theorem).
   169	\S\ref{sec:limitations} enumerates limitations and the
   170	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 259ms:
     1	% =====================================================================
     2	\section{Methods and provenance}\label{sec:method}
     3	% =====================================================================
     4	
     5	This section is a provenance ledger. It records, for each empirical
     6	claim downstream, the dataset, the preregistration date and document,
     7	the validation script, the seed range, the threshold, and the
     8	wallclock — the minimal information a hostile reviewer needs to
     9	reproduce or refute the claim.
    10	
    11	\subsection{Preregistration discipline}
    12	
    13	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
    14	(P1--P18) were locked on 2026-04-18 in
    15	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
    16	run. Each prediction has (i) a specific numerical claim, (ii) a
    17	falsifiable threshold, (iii) the validation test (script + seed range),
    18	and (iv) a rationale identifying what would falsify it.
    19	
    20	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
    21	predictions and rung observables — were preregistered on 2026-04-24
    22	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
    23	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
    24	not include those batteries in the headline 18/18 tally.} They are
    25	listed as future strengthening builds in~\S\ref{sec:limitations}.
    26	
    27	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
    29	biological signatures with literature-derived thresholds (NREM-N3
    30	variance ratio, propofol switching ratio, propofol continuity drop,
    31	propofol $\Phi$ collapse, recovery reversibility, wake
    32	cascade-$\alpha$). They are not part of the P1--P18 preregistration;
    33	they are reported as a companion validation set on the recurrent
    34	layer.
    35	
    36	\textbf{No threshold has been modified post-hoc.} Where the original
    37	2026-04-20 validation reported failures (P3, P4, P13), the documented
    38	methodological refinements were
    39	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    40	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    41	(P4, C$\times$P), and
    42	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    43	measurements for the chess LOO test (P13). None of these touched a
    44	preregistered threshold.
    45	
    46	\subsection{Provenance ledger}
    47	
    48	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    49	\to (\text{script}, \text{seed range}, \text{dataset/source},
    50	\text{threshold}, \text{result})$.
    51	
    52	\begin{table}[ht]
    53	\centering
    54	\small
    55	\caption{Provenance ledger for the headline empirical claims.}
    56	\label{tab:provenance}
    57	\begin{tabular}{l l l l l}
    58	\toprule
    59	Claim & Script & Seed range & Dataset / source & Threshold \\
    60	\midrule
    61	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    62	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    63	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    64	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    65	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    66	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    67	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    68	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    69	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    70	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    71	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    72	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    73	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    74	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    75	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    76	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    77	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    78	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    79	\midrule
    80	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    81	\bottomrule
    82	\end{tabular}
    83	\end{table}
    84	
    85	\subsection{Datasets and DOIs}
    86	
    87	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    88	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    89	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    90	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    91	fitting follows the Beggs--Plenz log-CCDF
    92	methodology~\citep{BeggsPlenz2003}.
    93	
    94	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    95	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    96	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    97	empirical reference for the propofol switching ratio
    98	($2.96\!\times$ wake) in Sig~2.
    99	
   100	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   101	EEG~\citep{OpenNeuroDS004902},
   102	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   103	psychedelic-state reference; not load-bearing for the headline tally.
   104	
   105	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   106	release~\citep{ZenodoDMT3992359},
   107	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   108	
   109	\textbf{HCP S1200.} Human Connectome Project
   110	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   111	matrix. The preregistered test (P18) was on $n=100$ subjects for
   112	computational tractability; full-cohort $n=1003$ statistics
   113	(degree std, participation ratio, clustering coefficient $\sigma$-
   114	distances) are reported as descriptive statistics on top of the
   115	preregistered test.
   116	
   117	\textbf{Microstate baseline (qualifier).} The continuity-drop
   118	signature (Sig~3) follows the EEG microstate methodology lineage of
   119	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   120	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   121	use it for the underlying microstate-fragmentation methodology, not
   122	as a propofol reference. A propofol-specific microstate citation
   123	would tighten this section; we treat that as an open
   124	strengthening build.
   125	
   126	\subsection{Statistical methods}
   127	
   128	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   129	ordinary least squares on the log-CCDF of the cascade-event size
   130	distribution, restricted to the central 80\% mass band (excluding the
   131	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   132	reported on the linear fit in log-space. A cascade event is defined
   133	as an attention-vertex shift between consecutive ticks
   134	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   135	the event size is the $\ell^{1}$ norm of the state-difference vector
   136	at that tick. Zero-size events are excluded.
   137	
   138	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   139	estimated by event-resampling bootstrap (500 resamples for the
   140	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   141	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   142	preregistered; 42 for the deep-dive.
   143	
   144	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   145	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   146	$0/2000$ were below the preregistered floor $+0.10$; we report these
   147	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   148	zero-probability statement on a finite resample.
   149	
   150	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   151	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   152	\[
   153	\Delta_{CP}
   154	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   155	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   156	\]
   157	
   158	\textbf{$\sigma$-distance against external nulls.} For the HCP
   159	comparisons we report
   160	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   161	on the full $n=1003$ subject distribution.
   162	
   163	\subsection{State-reset protocol}
   164	
   165	The substrate exhibits state drift: across approximately five
   166	successive depth-sweep evaluations the pressure field equilibrates
   167	to a uniform attractor and classification structure collapses to
   168	raw-feature baseline. Multi-trial benchmarks therefore require an
   169	explicit reset between successive evaluations.
   170	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   171	re-initialises pressure-field, crossed-vertex, and training state to
   172	canonical baseline. With reset between depth measurements, the chess
   173	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   174	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   175	preregistered floor). The reset protocol is documented in
   176	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   177	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   178	multi-trial benchmark on a non-stationary substrate must specify
   179	state-reset protocol.
   180	
   181	\subsection{Reproducibility commands}
   182	
   183	\begin{itemize}\itemsep=2pt
   184	\item Substrate self-test:
   185	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   186	\item Six drug/sleep signatures:
   187	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   188	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   189	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   190	\item Eighteen preregistered:
   191	  \texttt{python3 run\_preregistered\_validation.py}
   192	  ($\sim 18$\,min).
   193	\item Whole-paper repro:
   194	  \texttt{bash reproduce\_paper\_claims.sh}.
   195	\end{itemize}
   196	
   197	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   198	recurrent layer should reproduce per-condition means in this paper to
   199	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   200	NumPy version differences in the bootstrap RNG; the qualitative
   201	verdicts (CI overlaps, $P$-value thresholds) are unaffected.

 succeeded in 251ms:
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	computed Laplacian spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure. We compute the resulting Laplacian spectrum from the
    37	constructed graph; multiplicities match the expected H$_4$ block
    38	sizes. The 600-cell construction itself is
    39	standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    40	\paragraph{Graph facts (forced by the construction).}
    41	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, and
    42	every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
    43	vertex set; the short-edge nearest-neighbour graph inherits this
    44	uniformity). These facts are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}
    45	and reproduced numerically by
    46	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    47	
    48	\paragraph{Laplacian spectrum (computed numerically).}
    49	The unweighted graph Laplacian $\Lop = D - A$ has nine distinct
    50	eigenvalues with multiplicities summing to $120$:
    51	\[
    52	\sigma(\Lop) \;=\;
    53	\bigl\{0^{1},\;
    54	       (12\!-\!6\Ph)^{4},\;
    55	       (12\!-\!4\Ph)^{9},\;
    56	       9^{16},\;
    57	       12^{25},\;
    58	       14^{36},\;
    59	       (4\Ph + 8)^{9},\;
    60	       15^{16},\;
    61	       (6\Ph + 6)^{4}\bigr\},
    62	\]
    63	i.e.\ approximately $\{0, 2.292, 5.528, 9, 12, 14, 14.472, 15, 15.708\}$
    64	with multiplicities $\{1, 4, 9, 16, 25, 36, 9, 16, 4\}$. We computed
    65	this directly from the constructed Laplacian
    66	(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
    67	the spectrum is reproducible at machine precision and the
    68	multiplicities match the expected H$_4$ block sizes. We do not derive
    69	the closed-form entries here; the values in $\mathbb{Z}[\Ph]$ are
    70	reported as observed.
    71	
    72	\paragraph{H$_4$ irrep block decomposition.}
    73	The eigenspaces partition into H$_4$-proper and $\sigma$-twin Coxeter
    74	exponent classes. For H$_4$ proper the exponents are $\{1, 11, 19, 29\}$;
    75	for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
    76	of $\mathbb{Z}[\Ph]$ the exponents become $\{7, 13, 17, 23\}$. The
    77	$\sigma$-orbit projector basis
    78	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
    79	decomposition with cross-block norm $<10^{-15}$, providing a
    80	machine-precise structural index used by the recurrent layer in
    81	\S\ref{sec:chain} (the $K_{7}$-class projector is the default
    82	phenomenal-binding profile).
    83	
    84	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    85	
    86	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    87	is the discrete Green's function of the shifted Laplacian:
    88	\begin{equation}\label{eq:cphi}
    89	\Cph \;=\; \Lop + \Ph^{-2} I,
    90	\qquad
    91	\psi \;=\; \Cph^{-1} f.
    92	\end{equation}
    93	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    94	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    95	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    96	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    97	\emph{not} a derived theorem; it is a stability choice. The companion
    98	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    99	$\Cph$ as the basis for an independent passive-regime witness in
   100	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
   101	form (without retuning the shift) describes the
   102	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
   103	This paper imports $\Cph$ from that line; we do not re-derive it.
   104	
   105	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
   106	not produce critical-state cascade statistics; the recurrent layer
   107	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
   108	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
   109	event distributions. The choice $k\!=\!12$ is the average degree of
   110	$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
   111	fitted to any dataset.
   112	
   113	\paragraph{Disclosure (substrate-witness scope).}
   114	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
   115	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
   116	average degree, not a fitted threshold. No other shape parameter
   117	enters. The condition-dependent self-injection coupling
   118	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   119	varies between conditions in~\S\ref{sec:chain}; it is reported
   120	explicitly per condition.
   121	
   122	\subsection{Shell decomposition}\label{ssec:shells}
   123	
   124	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   125	spherical shells indexed by Euclidean inner product with a chosen pole:
   126	\[
   127	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   128	\]
   129	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   130	(the icosidodecahedral ring). When projecting onto a continuum kernel
   131	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   132	shell-mean projection of the equatorial-source response,
   133	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   134	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   135	This paper does not use that continuum projection; we work with the
   136	discrete operator throughout.
   137	
   138	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   139	
   140	The recurrent layer in~\S\ref{sec:chain} references a cascade
   141	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   142	\to S^{7}\to 0$, implemented in
   143	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   144	An arbitrary operator on the $E_{8}$ root system descends to the
   145	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   146	preserving the Frobenius norm to within $10^{-15}$. The
   147	$\sigma$-orbit projector basis from
   148	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   149	decomposition at machine precision.
   150	
   151	The descent provides numerical stability for the cascade ablations:
   152	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   153	remaining operator structure is exactly preserved. We do not claim
   154	the cascade itself is forced by physics on a pre-substrate level; the
   155	cascade is a decomposition of operators on $\Rsixhundred$, and the
   156	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   157	by the empirical correspondences in~\S\ref{sec:results}.
   158	
   159	\subsection{What the substrate is fixed-by, and what it is not}
   160	
   161	\begin{itemize}\itemsep=2pt
   162	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   163	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   164	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   165	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   166	  is not a derivation; it is a design-level clamp that bounds the
   167	  response inverse.
   168	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   169	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   170	  cascade structure and the empirical correspondences. A formal
   171	  ablation against alternative regular 4-polytopes is an open build
   172	  (\S\ref{sec:limitations}).
   173	\end{itemize}

exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/05_results.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/06_stress_tests.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/07_cross_domain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 236ms:
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	The proxy is designed to be small under H$_{4}$-equivariant dynamics
    77	(when block autocorrelations within irrep classes match the full-system
    78	autocorrelation) and to increase when dynamics produce cross-class
    79	asymmetries. It is not a theorem on information transport; it is a
    80	proxy that captures one observable signature of cross-class
    81	non-equivariance. This is a port of the published
    82	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    83	pipeline, adapted to take amplitude trajectories from any source.
    84	
    85	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    86	a full implementation of IIT. ARIA does not implement cause-effect
    87	repertoires, exclusion postulate, or integration-over-partitions
    88	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    89	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    90	of effect on the propofol-vs-wake state contrast; it is not a
    91	discharge of the IIT axioms.
    92	
    93	\subsection{The continuity composite}
    94	
    95	Implementation:
    96	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    97	A composite first-person continuity score over a 64-tick rolling
    98	window:
    99	\begin{align*}
   100	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
   101	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   102	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   103	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   104	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   105	\end{align*}
   106	This composite produces the propofol continuity-drop signature
   107	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   108	drop $+0.066$).
   109	
   110	\subsection{The phenomenal-field binding}
   111	
   112	Implementation:
   113	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   114	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   115	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   116	valence, modality\_label). The modality\_label is determined by which
   117	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   118	the $\sigma$-orbit projector basis. The default profile
   119	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   120	labelling; H$_4$-proper classes contribute amplitude bias.
   121	
   122	\subsection{Stimulus models}
   123	
   124	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   125	$\times$ $800$ ticks each at seed $42$:
   126	
   127	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   128	coherence (small always-on bias), and attention episodes (20--50
   129	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   130	within-shell rotation per tick). The AR(1) gives temporal correlation
   131	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   132	modality; attention episodes mimic biological visual fixation
   133	(200--400~ms dwell time analogue); within-shell rotation generates
   134	cascade events without changing modality.
   135	
   136	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   137	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   138	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   139	($4\%$ of ticks at amplitude $0.8$).
   140	
   141	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   142	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   143	background drive.
   144	
   145	\textbf{RECOVERY.} Identical to WAKE — verifies deterministic
   146	repeatability under the WAKE stimulus protocol after exposure to
   147	PROPOFOL (no hidden persistent modification of the substrate state).
   148	
   149	The v4 stimulus models were redesigned after diagnostics on the
   150	v3 stimulus models (which produced 4/6 signatures) to use
   151	biologically-motivated stimulus components — AR(1) cortical noise,
   152	attention episodes, slow-wave drive, spindles, K-complexes — at
   153	amplitudes and durations matching published biological time scales.
   154	They are not fitted to subject-level measurements, but they are
   155	condition-specific design choices iterated to close v3 stimulus-model
   156	artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
   157	the v3$\to$v4 redesign). The full stimulus code is
   158	\texttt{demo\_drug\_sleep\_v4.py}.
   159	
   160	\subsection{Cascade-mechanism ablation matrix}
   161	
   162	The cascade dynamics on the substrate use four mechanisms acting on
   163	the pressure field, each ablatable independently. The $2^{4}$
   164	ablation grid is the basis for the preregistered tests P1--P5 and
   165	the C$\times$P stress test in~\S\ref{sec:stress}.
   166	
   167	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   168	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   169	(coupling $0.05$) cross-orbit pressure averaging that prevents
   170	cascades from localising to one orbit.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   172	
   173	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   174	observer frame on the S$^{7}$ rung rotates periodically based on
   175	which uncrossed vertices have accumulated pressure aligning with
   176	each frame's preferences. This creates churn in \emph{which}
   177	vertices are uncrossed at any tick.
   178	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   179	
   180	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   181	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   182	saturating at pressure $3.0$. Without this mechanism, only fully-
   183	crossed vertices emit.
   184	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   185	
   186	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   187	30-vertex icosidodecahedral ring with split degree distribution.
   188	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   189	vertices overcome their connectivity deficit.
   190	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   191	
   192	The four mechanisms' \emph{targets} are geometry-pinned (D$_4$ orbits,
   193	$S^{7}$ rung, equatorial shell); their gains and coupling constants
   194	($D$ at $0.05$, $P$ at $30\%$ scale saturating at pressure $3.0$,
   195	$C$ rotation period, $E$ degree-ratio multiplier) are fixed design
   196	choices reported here, not learned from data. Their causal effects
   197	within the factorial ablation model are reported in~\S\ref{sec:stress}.

 succeeded in 221ms:
     1	% =====================================================================
     2	\section{Results}\label{sec:results}
     3	% =====================================================================
     4	
     5	This section is the empirical core. \S\ref{ssec:six_signatures}
     6	gives the six drug/sleep EEG signatures on the recurrent layer
     7	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
     8	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
     9	gives the three-way $\alpha$ overlap. We lift the result map
    10	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
    11	verdict)}$ verbatim from the validation outputs without
    12	recomputation; sources are
    13	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    14	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    15	
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

 succeeded in 260ms:
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the measured interaction collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice on this cascade-ablation matrix specifically: in this matrix,
   159	P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
   160	at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
   161	The original 3-seed preregistered validation gave estimates consistent
   162	with underpowered detection on both interaction tests; both close at
   163	higher $N$ without threshold modification. The general lesson: when
   164	preregistering an interaction effect on a system with unknown
   165	per-seed variance, budget the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Future preregistrations on similar high-variance
   168	ablation matrices should plan for this scale.

 succeeded in 282ms:
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph H$_4$-transitive null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
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
   116	
   117	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   118	
   119	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
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
   226	because the HCP subject distribution and the across-subject
   227	$\sigma$ are computed in the same units, but flag the node-count
   228	caveat here.
   229	
   230	\textbf{What we do not claim.}
   231	\begin{itemize}\itemsep=2pt
   232	\item We do not claim cortex has ``drifted from an ideal polytope'';
   233	  the substrate is a useful a-priori null whose deviation from real
   234	  cortex is precisely measurable.
   235	\item We do not claim parcellation invariance: the $\sigma$-distances
   236	  are reported on ICA-50; alternative parcellations (Schaefer,
   237	  Glasser) would give different per-metric numbers but, on the
   238	  basis of the qualitative pattern that cortex is hub-concentrated
   239	  relative to ARIA's transitive null, we expect them to preserve the
   240	  signs. Verification across parcellations is an open build
   241	  (\S\ref{sec:limitations}).
   242	\end{itemize}
   243	
   244	\subsection{Cross-domain summary as a selective amplifier
   245	            \texorpdfstring{$+$}{+} H$_4$-transitive null}
   246	
   247	\begin{table}[ht]
   248	\centering
   249	\small
   250	\caption{Cross-domain summary on a single substrate.}
   251	\label{tab:cross_domain_summary}
   252	\begin{tabular}{l r r r r r}
   253	\toprule
   254	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   255	\midrule
   256	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   257	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   258	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
   259	\bottomrule
   260	\end{tabular}
   261	\end{table}
   262	
   263	The geometric content ($\approx 65$--$71\%$ across the two domains)
   264	is the architecture-invariant null floor. The semantic content
   265	($12$--$18$pp) is the domain-specific contribution. On HCP,
   266	$\sigma$-distances against the biological cohort are
   267	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   268	clustering coefficient).
   269	
   270	\textbf{Headline cross-domain reading.} The substrate is
   271	\emph{selectively} amplifying (not unconditionally), and it is an
   272	H$_4$-transitive deterministic null on connectivity (not a fitted
   273	model). Both readings sit inside the substrate-witness scope.

exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/08_discussion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/09_limitations.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/sections/10_conclusion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "papers/aria-chess-paper/paper/README.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 228ms:
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

 succeeded in 237ms:
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} Once the 600-cell is chosen as the substrate, its graph
    20	  ($120$ vertices, uniform degree $12$ on the canonical short-edge
    21	  nearest-neighbour graph) and the response operator
    22	  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
    23	  shape parameter is tuned to neural data); cascade-$\alpha$ matches
    24	  Sleep-EDFx within preregistered tolerance with pairwise CI overlap
    25	  on three reference ranges; six drug/sleep signatures pass at
    26	  literature-derived thresholds on a single deterministic substrate.
    27	  We are not aware of a prior geometric substrate that has been tested
    28	  against this many preregistered cortical correspondences from a
    29	  graph fixed by the construction with no neural-data-fitted shape
    30	  parameters; we cannot rule out that such a model exists.
    31	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    32	  are strongly coupled cascade-state stabilisers, not
    33	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    34	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    35	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    36	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    37	  substantive correction to the architectural reading from the
    38	  original 3-seed validation.
    39	\item \textbf{The 18/18 preregistered correspondences with no
    40	  threshold modification.} Every prediction in the preregistered set
    41	  passes at the preregistered thresholds. The two interaction tests
    42	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    43	  one test (P13) required the documented state-reset protocol. We
    44	  report this transparently as methodology refinement, not as
    45	  threshold change.
    46	\end{enumerate}
    47	
    48	\subsection{Comparison to existing theories of consciousness}
    49	
    50	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    51	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    52	wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
    53	under H$_4$-equivariant dynamics and to increase when dynamics
    54	produce cross-class asymmetries. ARIA does not implement the full
    55	IIT axioms (cause-effect repertoires, exclusion postulate,
    56	integration-over-partitions); it reproduces an observable consequence
    57	on the propofol--wake state contrast. This is a consistency-of-direction
    58	result, not a discharge of IIT.
    59	
    60	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    61	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    62	functionally analogous to a workspace with rotating attentional
    63	selection; the active observer frame plays the role of a temporary
    64	in-workspace subset of features. ARIA does not commit to the GWT
    65	broadcast/access distinction at the architectural level; the
    66	analogy is descriptive.
    67	
    68	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    69	ARIA does not implement prediction-error minimisation or hierarchical
    70	generative models.
    71	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    72	modulation of the substrate response by cosine direction alignment
    73	with the prior phenomenal snapshot, not by learned prediction errors.
    74	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    75	learning rate over a prediction-error norm) are an open build, not
    76	delivered here.
    77	
    78	\textbf{vs neural mass models.} ARIA operates at the
    79	architectural-algorithmic level; it does not specify which neural
    80	circuits implement context rotation or partial emission. The 600-cell
    81	substrate is proposed as an abstract description of the criticality-
    82	maintaining structure of cortex, not as a circuit model.
    83	
    84	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    85	
    86	The companion adaptive-closure-transport
    87	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    88	4-tuple bridge
    89	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    90	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    91	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    92	$D_{\mathrm{ACT}}$:
    93	\[
    94	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    95	\;\longmapsto\;
    96	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    97	   \ \texttt{homeostatic\_reset}).
    98	\]
    99	\textbf{This bridge is non-load-bearing for the present paper.} It is
   100	included as a route-K (alternative-route) reading; the substrate-
   101	witness claims (six signatures, $18/18$, chess $+40.6$pp,
   102	HCP $\sigma$-distances) do not require any of the ACT theorems.
   103	
   104	\textbf{What ACT would have to deliver to make this load-bearing.}
   105	The companion preprint identifies four open builds, each of which is
   106	deferred:
   107	\begin{itemize}\itemsep=2pt
   108	\item A Lyapunov function $V(W)$ on the reduced flow whose
   109	  monotonicity proves selection — not delivered.
   110	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   111	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   112	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   113	\item A formal $2I$-equivariance audit of the closure operator
   114	  family — not delivered.
   115	\item A full reduced-flow convergence theorem on
   116	  $W$-trajectories — not delivered.
   117	\end{itemize}
   118	Until these are delivered, ARIA is positioned as the empirical
   119	\emph{substrate witness} for the family that ACT names; ACT is not the
   120	selection-theorem witness for ARIA. The companion kernel
   121	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   122	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   123	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   124	infrastructure with this paper, but does not transfer empirical
   125	support for ARIA.
   126	
   127	\subsection{The strong-coupling reading for cortical architecture}
   128	
   129	Real cortical criticality is maintained by multiple parallel
   130	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   131	homeostatic plasticity, gain control. The naive expectation — and the
   132	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   133	orthogonal, so losing one removes only its own main effect. The
   134	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   135	strongly coupled. Disabling one cascades into losing the synergistic
   136	contribution of the other.
   137	
   138	This matches clinical observations: anaesthesia (which targets
   139	GABAergic transmission) and seizure (which targets E/I balance)
   140	produce widespread network-level dysfunction beyond their direct
   141	targets — qualitatively consistent with a strong-coupling hypothesis. We position this as
   142	\emph{a hypothesis the substrate witness raises}, not as a proof.
   143	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   144	real-cortex pharmacological coupling is a step we do not take in
   145	this paper.
   146	
   147	\subsection{Methodological contributions}
   148	
   149	Two methodological items are worth recording outside the headline:
   150	\begin{enumerate}\itemsep=2pt
   151	\item \textbf{$N\!\geq\!20$ for similar high-variance ablation matrices.}
   152	  Allocation discipline for preregistration: in this cascade-ablation
   153	  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
   154	  reliable detection at the preregistered threshold. The general
   155	  rule we draw — when preregistering an interaction effect on a
   156	  system with unknown per-seed variance, budget for at least this
   157	  scale — should be tested against other ablation matrices, not
   158	  taken as universal. The original 3-seed plan was the source of two
   159	  underpowered-interaction estimates in this work.
   160	\item \textbf{State-reset protocol on non-stationary substrates.}
   161	  ARIA's substrate is a non-stationary dynamical system; the
   162	  pressure field equilibrates within $\sim 5$ successive evaluations.
   163	  Any multi-trial benchmark must specify a state-reset protocol or
   164	  document the drift. Generalisable lesson: \emph{published
   165	  cross-domain benchmarks on non-stationary substrates should report
   166	  an explicit reset/equilibration discipline}, not just seed.
   167	\end{enumerate}
   168	
   169	\subsection{The substrate as an H$_4$-transitive connectivity null}
   170	
   171	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   172	deterministic null reference for cortical functional connectivity.
   173	Real cortex breaks the symmetry through hub-spoke functional
   174	specialisation; the $\sigma$-distances from ARIA quantify the
   175	magnitude of biological symmetry-breaking with no fitted parameters.
   176	
   177	This is a methodological contribution to comparative connectomics.
   178	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   179	edge-randomised graphs) compare cortex to a random graph with matched
   180	density. ARIA is a different kind of null: a deterministic
   181	group-theoretic graph with structure-level statements: degree std
   182	$=\!0$ by H$_4$ transitivity, and a fully-determined Laplacian
   183	spectrum (\S\ref{ssec:graph}) computed from the constructed graph.
   184	Both null kinds are useful; ARIA gives a specific, reproducible,
   185	group-theoretic baseline that cortex deviates from in quantifiable
   186	$\sigma$-units.
   187	
   188	\subsection{Open questions raised by the substrate witness}
   189	
   190	\begin{itemize}\itemsep=2pt
   191	\item Do the six drug/sleep signatures replicate across $10$--$20$
   192	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   193	  see \S\ref{sec:limitations}.)
   194	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   195	  reproduce comparable signature sets, or is the $600$-cell
   196	  distinguished?
   197	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   198	  independent fresh-seed $N\!=\!20$ replication at a different seed
   199	  range?
   200	\item Does the substrate's amplifier behaviour transfer to other
   201	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   202	  pattern, audio classification)?
   203	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   204	  EEG cohort (TUH, NHM)?
   205	\end{itemize}
   206	We list these as open questions raised by the witness, not as gaps
   207	in the witness itself.

 succeeded in 320ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
     6	symmetry, with the shifted-Laplacian response operator
     7	$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
     8	geometry-fixed substrate that is consistent with eighteen
     9	preregistered neuroscience correspondences plus six companion
    10	drug/sleep EEG signatures of conscious vs unconscious states. Once
    11	the substrate is chosen, its graph structure ($120$ vertices, uniform
    12	degree $12$ on the canonical short-edge nearest-neighbour graph, with
    13	the Laplacian spectrum reported in~\S\ref{ssec:graph} as observed) is
    14	fixed; only one condition-dependent self-injection coupling
    15	$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
    16	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
    17	degree enter the recurrent layer above the substrate. No shape
    18	parameter is tuned to any neural dataset.
    19	
    20	\textbf{Headline tally.} On a single deterministic trajectory, six
    21	drug/sleep EEG signatures pass against their literature-derived
    22	thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
    23	Tononi 2008): NREM-N3 phenomenal-intensity variance ratio
    24	$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
    25	propofol continuity drop $+0.066$; propofol integrated-information
    26	$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    27	recovery deterministically identical to wake under the WAKE stimulus
    28	protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
    29	$95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$. The wake $95\%$ CI
    30	overlaps the real Sleep-EDFx EEG
    31	$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
    32	CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
    33	$[2.73, 3.25]$.
    34	
    35	\textbf{Eighteen preregistered correspondences.} All eighteen pass at
    36	preregistered thresholds, with two interaction tests requiring
    37	$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
    38	high-variance interaction terms, and one cross-domain test requiring
    39	the documented \texttt{homeostatic\_reset} state-reset protocol. No
    40	preregistered threshold has been modified. The original 2026-04-20
    41	$15/18$ tally was a methodology-limited reading, not a content
    42	failure; the closure of the three gaps (P3, P4, P13) is documented
    43	transparently in
    44	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    45	
    46	\textbf{Strong-coupling architectural finding.} Two cascade
    47	mechanisms — context rotation $C$ and partial emission $P$ — are
    48	causally identifiable within the factorial ablation model and exhibit
    49	strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
    50	$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
    51	at or below zero, reported as $0.0000$) is comparable in magnitude to
    52	the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
    53	is consistent with an underpowered interaction estimate on a
    54	high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
    55	contribute $N\!\approx\!20$ as a planning scale for this cascade
    56	matrix, recommended as a preregistration-practice consideration for
    57	similar high-variance ablation matrices.
    58	
    59	\textbf{Cross-domain selectivity.} The substrate exhibits selective
    60	amplification on the two tasks tested: chess 4-category position
    61	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
    62	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
    63	$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
    64	$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
    65	refinement at the same threshold), while
    66	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
    67	(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
    68	deterministic null reference for cortical functional connectivity:
    69	on the full-cohort descriptive HCP $n\!=\!1003$ statistics
    70	(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
    71	structure is at $-11.58\sigma$ on degree homogeneity,
    72	$+79.78\sigma$ on participation ratio (with the node-count caveat of
    73	\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
    74	
    75	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    76	derivation of consciousness, not a selection theorem on the
    77	companion adaptive-closure-transport
    78	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    79	uniqueness claim for the 600-cell among regular 4-polytopes. The
    80	strengthening builds — cross-seed CIs on the recurrent-layer
    81	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    82	C$\times$P replication at a different seed range, cross-parcellation
    83	HCP replication, a Lyapunov function on the reduced flow,
    84	$2I$-equivariance audit of the closure operator family — are
    85	explicitly listed in~\S\ref{sec:limitations} and remain open.
    86	
    87	We are not aware of a prior deterministic geometric architecture
    88	tested against this many preregistered cortical correspondences from
    89	a graph fixed by the construction with no shape parameters tuned to
    90	neural data; we cannot rule out that such prior work exists. The empirical material
    91	gathered here is the substrate witness; the broader programme to
    92	turn the witness into a selection-theorem-grade claim — including the
    93	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    94	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    95	operator $\Cph$ — is sketched in the companion preprints and remains
    96	the natural next step.

 succeeded in 317ms:
     1	# aria-chess paper
     2	
     3	A geometry-fixed substrate witness for cortical signatures: eighteen
     4	preregistered correspondences and six drug/sleep EEG signatures from
     5	the 600-cell regular 4-polytope under H₄ Coxeter symmetry.
     6	
     7	## Build
     8	
     9	```
    10	pdflatex main.tex
    11	bibtex main
    12	pdflatex main.tex
    13	pdflatex main.tex
    14	```
    15	
    16	Or whatever your LaTeX toolchain prefers. The bibliography uses
    17	`natbib` with `plainnat` style. All paths are relative to this
    18	directory; figures (if added) live under `figures/`.
    19	
    20	## Sections
    21	
    22	```
    23	sections/01_introduction.tex
    24	sections/02_method.tex
    25	sections/03_substrate.tex
    26	sections/04_consciousness_chain.tex
    27	sections/05_results.tex
    28	sections/06_stress_tests.tex
    29	sections/07_cross_domain.tex
    30	sections/08_discussion.tex
    31	sections/09_limitations.tex
    32	sections/10_conclusion.tex
    33	```
    34	
    35	## Reproduction
    36	
    37	The empirical numbers in §5–§7 are reproduced from the project
    38	repository's deterministic scripts. From the repo root:
    39	
    40	```bash
    41	# six drug/sleep signatures (~30 s)
    42	python3 demo_drug_sleep_v4.py
    43	
    44	# C×P synergy N=20 deep-dive (~28 min)
    45	python3 demo_p4_cxp_deep_dive.py
    46	
    47	# eighteen preregistered correspondences (~18 min)
    48	python3 run_preregistered_validation.py
    49	
    50	# whole-paper repro
    51	bash reproduce_paper_claims.sh
    52	```
    53	
    54	All scripts are deterministic given seeds. The substrate's spectral
    55	decomposition is cached at module level. Reruns at seed 42 reproduce
    56	per-condition means in §5.1 to 4 decimal places.
    57	
    58	## Source documents
    59	
    60	The paper text is lifted from:
    61	
    62	- `docs/brain_mapping/MANUSCRIPT_V2.md` (paper-shaped manuscript draft)
    63	- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` (six signatures)
    64	- `docs/brain_mapping/P4_SYNERGY_FINDING.md` (N=20 deep-dive)
    65	- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` (chess / conversation / HCP)
    66	- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` (18/18 tally)
    67	- `docs/brain_mapping/PAPER_PREDICTIONS.md` (preregistered 2026-04-18)
    68	- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` (state-reset protocol)
    69	
    70	## Scope
    71	
    72	This is a **substrate witness**: a geometry-fixed substrate is
    73	consistent with eighteen preregistered neuroscience correspondences
    74	and six drug/sleep EEG signatures, with no fitted shape parameters
    75	on any neural dataset. It is **not** a derivation of consciousness,
    76	not a selection theorem on the companion adaptive-closure-transport
    77	4-tuple, and not a uniqueness claim for the 600-cell among regular
    78	4-polytopes. See §1 and §9 for the explicit claim-boundary discipline.
    79	
    80	## Status
    81	
    82	Preprint, not peer-reviewed. April 2026.

exec
/bin/bash -lc "rg -n \"looked at first|historically blind|criterion-independent|variant|pure-geometry|0\\.997|13\\.555|13\\.555|unweighted|FREE_C9|Mode B|2\\.77|Gaussian|0\\.348|0\\.652|residual|overshoot\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "find \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections\" -maxdepth 1 -type f -name '*.tex' -print" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 247ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex

 succeeded in 337ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:58:linearised analysis (Mode B, linear in $\Delta C_{9}$ via
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:65:derived from a finite 2I-equivariant graph substrate (the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:76:edge-weighting variants, the unweighted Laplacian is selected by a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:77:\emph{pure-geometry criterion} (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:107:basis-correction factor $\sim 2.2$, with a residual $\sim 50\,\%$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:108:overshoot of the basis-corrected prediction that the published
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:125:Gaussian charm-loop proxy fits marginally better in $\chi^{2}$ at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:22:under Mode B and should be read accordingly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:100:charm-loop Gaussian            & 2 & 35.41 & 39.41 & $-1.91$ & $A=+1.83$, $\sigma=8.96\,\mathrm{GeV}^{2}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:104:Adding $C_{10}$ does not help. The free centre-peaked Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:113:$\Delta C_{10}$ at this level. The charm-loop Gaussian — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:165:test (Mode B) & criterion & result \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:168:                                & \textsc{pass} (Mode B; $99.8\,\%$ positive, CI $\pm 15\,\%$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:170:                                & \textsc{pass} (Mode B; 3/3 regions $\Delta\mathrm{AIC}<0$, all $A>0$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:172:                                & \textsc{pass} (Mode B; $\Delta\mathrm{AIC}=+1.73$ vs FREE\_C9) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:173:3b. charm-loop Gaussian         & VFD competitive at same shape level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:174:                                & \textsc{partial} (Mode B; $\Delta\mathrm{AIC}_{\mathrm{charm\,vs\,VFD}}=-0.24$, charm $k=2$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:176:                                & \textsc{pass} (Mode B; $100\,\%$ positive, CI $\pm 15\,\%$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:44:Empirically the per-bin linearisation residual on LHCb 2025 reaches
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:57:operator $L_{V_{600}} + \varphi^{-2}I$ to the 2I-equivariant cocycle
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:66:Table~\ref{tab:variant_selection}); the unweighted Laplacian wins on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:67:both the pure-geometry and LHCb-data criteria, with the rankings
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:81:is $+4.98$, a factor-of-2 unexplained residual. We do \emph{not}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:82:characterise this as a clean basis-effect victory: the residual is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:103:\item \emph{The kernel is the right object.} The 2I-equivariant graph
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:127:  $A\in[+1.36, +1.85]$ in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:130:  in Mode B, worse than the $+2$ AIC penalty for the extra parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:133:  $A=+1.57\pm 0.16$, $100\,\%$ positive, in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:140:centre-peaked Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:141:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9 in Mode B; vs $-1.67$ for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:143:parameter. The geometric kernel and the free Gaussian capture the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:70:\subsection{Linearised response (Mode B; reported as diagnostic)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:87:This `Mode B' analysis is retained for two reasons: (i) it
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:92:linearisation residual reaches $4.3\sigma$ (mean $0.7\sigma$ across
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:95:(non-linear refit), a $2.77$-AIC-unit shift that flips the sign of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:115:We use a Gaussian $\chi^{2}$ likelihood
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:138:\item Charm-loop Gaussian — a free-amplitude, free-width Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:150:$\mathrm{xtol}=5\times 10^{-4}$; for Mode B the optimiser is Powell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:180:linearised optimiser (Mode B) & \texttt{scipy.minimize} Powell, tol $10^{-7}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:8:2I-equivariant graph realisation on the 600-cell $V_{600}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:11:kernel; the continuum and bounded variants are reported as theoretical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:70:\subsection{Layer 3 — discrete 2I-equivariant lift on $V_{600}$}\label{subsec:layer3}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:130:\eqref{eq:kappa_lift} on the LHCb 2025 bin centres is $r=0.997$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:143:$e^{-|x|/\varphi}$ from Layer 1, with empirical correlation $r=0.997$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:151:\paragraph{Cocycle, edge weighting, and variant selection.} The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:155:edge-weighting schemes are admissible: unweighted ($w_{vw}=1$),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:160:for each variant; the shell-mean profile is then compared to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:162:on the LHCb bin grid. Two criteria are used: a \emph{pure-geometry}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:172:variant & $\mathrm{corr}(\overline{\psi}, e^{-|x|/\varphi})$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:176:unweighted Laplacian          & $\mathbf{0.9968}$ & $\mathbf{13.555}$ & $1$ on both \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:181:\caption{Variant selection. The unweighted Laplacian wins on both the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:182:pure-geometry criterion (correlation with the Layer-1 continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:184:variant choice is consistent with selection on geometric grounds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:186:Reproducible from \texttt{scripts/wo016b\_variant\_geometry.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:187:(reports/wo016b\_variant\_geometry.csv).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:188:\label{tab:variant_selection}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:191:The unweighted Laplacian is selected as the primary kernel. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:192:two-criterion agreement means the variant choice does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:193:extra effective fit parameter: the variant choice would have been the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:197:\S\ref{sec:limitations}: the data was looked at first, and only later
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:198:verified to agree with the pure-geometry ranking.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:215:(Eq.~\ref{eq:Lphi}), and the variant table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:216:(Table~\ref{tab:variant_selection}). A reader unfamiliar with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:221:with 2I-equivariant boundary maps from the 1200 triangular faces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:34:of a finite 2I-equivariant graph (the 600-cell $V_{600}$, vertices and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:95:  correction a residual $\sim 50\,\%$ overshoot remains, attributable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:104:  Gaussian also fits comparably (\S\ref{sec:stress}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:30:  The unweighted Laplacian was originally selected because it gave
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:31:  the best LHCb-data $\chi^{2}$ among the three admissible variants
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:32:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:33:  We subsequently verified that the same variant wins on a pure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:36:  this basis. The variant choice therefore does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38:  data was looked at first is acknowledged.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:51:  2I-equivariant graph but is not derived from a first-principles
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:59:  \delta_{1}^{\mathsf T}\delta_{1}$ with 2I-equivariant boundary maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:122:  ($\Delta\chi^{2}=1$ Gaussian approximation or non-parametric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:51:$\pm 1\sigma$ bands. Both models leave residuals of $\lesssim 2\sigma$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:74:FREE\_C9 (Mode B)           & 1 &  39.30 &  41.30 & $0.00$  & $\Delta C_{9}=-1.34$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:75:VFD\_GREEN\_600CELL (Mode B)& 1 &  37.63 &  39.63 & $-1.67$ & $A=+1.59$, $\Delta C_{9}^{\mathrm{eff}}=-1.37$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:92:quantity & linearised (Mode B) & non-linear refit & drift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:96:$\Delta\mathrm{AIC}$ (VFD vs FREE) & $-1.67$ & $+1.09$ & $\mathbf{+2.77}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:99:max per-bin linearisation residual & --  & $4.27\sigma$ & -- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:100:mean per-bin linearisation residual & -- & $0.71\sigma$ & -- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:105:$\Delta\mathrm{AIC}$ is $2.77$ units, larger than the Mode-B
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:107:evaluation. Per-bin linearisation residuals reach $4\sigma$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:134:Refitting the shared kernel under Mode B after removing one of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:142:dropped & $n$ remaining & $A$ (Mode B) & $\Delta C_{9}^{\mathrm{eff}}$ mean & $\chi^{2}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:149:all (reference, Mode B)  & 32 & 1.594 & $-1.367$ & 37.63 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:153:Mode B (linearised). $A$ varies within $\pm 3\,\%$ across the four
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:6:$\kappa(q^{2})$ from a finite 2I-equivariant graph (the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:41:  factor-of-$2$ unexplained residual.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:43:  $\Delta\mathrm{AIC}$ shifts by $+2.77$ between the linearised and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:49:  pure-geometry-confirmed discrete variant choice
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:50:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:86:factor; and the unweighted Laplacian variant is selected by a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:87:pure-geometry criterion (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:56:LHCb 2021 ($B^{+}\to K^{*+}$) & 32 & 22.77 & $-1.82$ & 22.93 & $\boldsymbol{+2.06}$ & $-1.59$ & $+0.17$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:117:\textbf{0.652} & \textbf{0.348} & \textbf{FREE\_C9 (mild)} \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:163:   & \textbf{\textsc{fail}} ($w_{\mathrm{VFD}} = 0.348$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:183:$7\times$ per data point. The residuals are dominated by $P_{4}'$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:46:The 500-trial bootstrap on bins (run under Mode B, retained as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:49:poorly constrained. Region splits under Mode B give $A=+5.31$ in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:151:best-fit. We attribute the residual gap to:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:163:residual that is at least as large as the basis-correction itself;

 succeeded in 329ms:
     1	# WO-016b — Variant selection by pure-geometry criterion
     2	
     3	Pure-geometry criterion: correlation between the discrete shell-mean of the V_600 Green's response and the continuum kernel $\kappa(x) = e^{-|x|/\varphi}$ from Layer 1 of the derivation. This criterion does **not** use LHCb data.
     4	
     5	Data criterion: chi^2 against LHCb 2025 P5' on the joint fit.
     6	
     7	| variant | corr(κ_continuum) | χ² (LHCb) | geom rank | data rank |
     8	|---|---:|---:|---:|---:|
     9	| FULL_LIFT[UNWEIGHTED]_GREENS | 0.9968 | 13.555 | 1 | 1 |
    10	| FULL_LIFT[PHI_GEOMETRIC]_GREENS | 0.9130 | 14.713 | 2 | 2 |
    11	| FULL_LIFT[PHI_ARITHMETIC]_GREENS | 0.8989 | 14.782 | 3 | 3 |
    12	
    13	- Pure-geometry winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (corr with continuum kernel = 0.9968)
    14	- LHCb-data winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (χ² = 13.555)
    15	
    16	**Agreement.** The same variant (unweighted Laplacian) wins on both criteria. The variant choice is consistent with pure-geometry selection independent of the data; the LHCb data merely confirms it. Effective parameter count for VFD remains k=1 under the pure-geometry interpretation.

 succeeded in 332ms:
     1	# WO-016c — Non-linear flavio refit on LHCb 2025
     2	
     3	Tests whether the linearised Mode-B response is sufficient at the fitted Delta C9 ~ -1.4. Three comparisons:
     4	1. Linear fit (paper headline).
     5	2. Non-linear evaluation at the linearised best-fit point (drift diagnostic — both models pinned at linear best-fit).
     6	3. Non-linear refit (best-fit values found by `flavio.np_prediction`).
     7	
     8	## Headline
     9	
    10	| model | chi^2 | AIC | Delta AIC vs FREE_C9 | fit param |
    11	|---|---:|---:|---:|---|
    12	| FREE_C9_linear | 39.303 | 41.303 | +0.000 | DC9=-1.340 |
    13	| FREE_C9_nonlinear@linear-best-fit | 66.596 | 68.596 | +0.000 | DC9=-1.340 |
    14	| FREE_C9_nonlinear_refit | 40.891 | 42.891 | +0.000 | DC9=-1.002 |
    15	| VFD_linear | 37.631 | 39.631 | -1.672 | A=+1.594 |
    16	| VFD_nonlinear@linear-best-fit | 82.241 | 84.241 | +15.644 | A=+1.594 |
    17	| VFD_nonlinear_refit | 41.983 | 43.983 | +1.093 | A=+1.135 |
    18	
    19	- Linearised Delta AIC (FREE_C9 vs VFD): -1.672
    20	- Non-linear Delta AIC at linear best-fit: +15.644 (diagnostic only; both models held at linear best-fit)
    21	- Non-linear Delta AIC after refit: +1.093 (headline-comparable)
    22	- Drift in headline Delta AIC: +2.765
    23	
    24	## Best-fit parameters
    25	
    26	- FREE_C9 linear: Delta C9 = -1.3403
    27	- FREE_C9 non-linear refit: Delta C9 = -1.0025
    28	- VFD linear: A = +1.5935
    29	- VFD non-linear refit: A = +1.1350
    30	
    31	## Per-bin linearisation residual (|nonlinear - linear| / sigma)
    32	
    33	- FREE_C9 at linear best-fit: max = 3.106 sigma, mean = 0.630 sigma
    34	- VFD at linear best-fit: max = 4.269 sigma, mean = 0.714 sigma
    35	
    36	**Conclusion.** |Drift in headline Delta AIC| = 2.765 > 0.5 AIC unit. The headline must be updated to the non-linear refit value: Delta AIC_NL = +1.093 (vs linearised -1.672). The non-linear refit best-fit is DC9_FREE = -1.002 (vs linear -1.340) and A = +1.135 (vs linear +1.594).

codex
The aria-chess inherited numbers broadly match the companion: the `17/18 -> 18/18`, P4 deep-dive, six EEG signatures, chess/conversation/HCP figures, and scope caveats are present there. I’m doing one more static LaTeX/notation pass and checking for places where “independent”, “same operator”, or “closes” should be softened.
exec
/bin/bash -lc 'rg -n "derive|derived|derivation|unique|uniqueness|selection|Lyapunov|2I|equivariance|theorem|forced|fixed|closes|establish|establishes|load-bearing|same fixed|independent|criterion-independent|consensus|appears|operator is|the operator" "papers/aria-closure-kernel/paper/main.tex" "papers/aria-closure-kernel/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\[A-Za-z]+\" \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"TODO|FIXME|??|undefined|citation|citep\\{|ref\\{|label\\{|\\\\input|\\\\bibliography|checkmark|Krüger|—|–|"'`|``|'"''\" \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\" \"papers/aria-closure-kernel/paper/references.bib\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\label\\{|\\\\ref\\{|\\\\citep\\{|\\\\cite\\{\" \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 321ms:
/bin/bash: -c: line 0: unexpected EOF while looking for matching ``'
/bin/bash: -c: line 1: syntax error: unexpected end of file

 exited 2 in 314ms:
rg: regex parse error:
    (?:\label\{|\ref\{|\citep\{|\cite\{)
       ^^
error: unrecognized escape sequence

 exited 1 in 397ms:
 succeeded in 478ms:
papers/aria-closure-kernel/paper/main.tex:21:       a geometry-fixed kernel on the 600-cell with two\\
papers/aria-closure-kernel/paper/main.tex:22:       independent empirical witnesses}
papers/aria-closure-kernel/paper/main.tex:50:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:56:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:57:same fixed graph is then the load-bearing object in two
papers/aria-closure-kernel/paper/main.tex:58:\emph{independent} empirical works: a passive-regime structural
papers/aria-closure-kernel/paper/main.tex:67:geometry-fixed response operator that is simultaneously consistent
papers/aria-closure-kernel/paper/main.tex:68:with two independent empirical landings under no shape-parameter
papers/aria-closure-kernel/paper/main.tex:69:retuning between regimes. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:70:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:72:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:84:document its appearance as the same fixed operator (no shape
papers/aria-closure-kernel/paper/main.tex:85:retuning) in two independent empirical
papers/aria-closure-kernel/paper/main.tex:102:established separately by b-anomaly's data $\chi^{2}$ comparison
papers/aria-closure-kernel/paper/main.tex:105:criterion-independent but historically non-blind, a caveat we
papers/aria-closure-kernel/paper/main.tex:130:Same source vertex, same fixed shift, no parameter fitting; the
papers/aria-closure-kernel/paper/main.tex:134:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:141:shape held fixed. (b)~Active regime,
papers/aria-closure-kernel/paper/main.tex:154:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:156:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:157:either empirical landing. We do not claim the operator is the
papers/aria-closure-kernel/paper/main.tex:158:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:161:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:163:this paper is: \emph{one geometry-fixed operator on one fixed
papers/aria-closure-kernel/paper/main.tex:164:graph appears as the load-bearing object in two independent
papers/aria-closure-kernel/paper/sections/05_agreement.tex:58:On the unweighted 600-cell graph with an H$_3$-fixed source,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:110:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:113:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:116:this is a uniqueness result; we report it as a two-criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:121:\subsection{What the agreement does and does not establish}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:123:\paragraph{Does establish.} A geometric agreement: the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:124:response of a fixed-shift Green operator on a fixed graph behaves,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:127:This is a non-trivial agreement between two independently-defined
papers/aria-closure-kernel/paper/sections/05_agreement.tex:134:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:139:verbatim. The agreement also does not establish that
papers/aria-closure-kernel/paper/sections/05_agreement.tex:140:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:109:  are fixed by the single design choice $\Ph^{-2}$, giving a single
papers/aria-closure-kernel/paper/sections/02_definition.tex:110:  dimensional parameter throughout the operator;
papers/aria-closure-kernel/paper/sections/02_definition.tex:114:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:116:(1)--(3); we report this explicitly and treat formal derivation as
papers/aria-closure-kernel/paper/sections/02_definition.tex:120:selection-layer dynamics over $W$-space that would, if delivered,
papers/aria-closure-kernel/paper/sections/02_definition.tex:121:constrain the shift further; that derivation is not delivered
papers/aria-closure-kernel/paper/sections/03_substrate.tex:10:construction itself is theorem-level rigorous in H$_4$ Coxeter
papers/aria-closure-kernel/paper/sections/03_substrate.tex:60:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:105:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:130:\item \textbf{Not fixed by this paper}: the choice of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:6:and identifies what the operator does not deliver. The framing
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:8:\emph{response} primitive; \emph{selection} (which response
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:26:  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:41:not formally proved. Each named operator is in a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:44:formal classification theorem identifying the family.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:chosen substrate plus the design-level shift: $\Cph$ is fixed by
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:59:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:63:The selection layer is open. It appears as an open hypothesis in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:64:three independent frames:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:72:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  $2I$-equivariance, and a full reduced-flow convergence theorem
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:78:  a selection theorem; ACT is positioned as the future
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:79:  selection-theorem witness.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:82:The recurrence of an open selection gap across these three frames
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:84:problem rather than three independent ones, but the present paper
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:87:primitive without reducing or addressing the selection gap.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:89:\subsection{What this paper closes vs leaves open}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:91:\paragraph{Closes (at the operator-witness level).}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:94:  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:110:  the load-bearing object in two independent empirical works in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:118:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:120:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:124:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:129:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:134:\item \emph{Family-membership theorem.} The programme-home
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:135:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:14:arithmetic derivation in this paper.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:54:fixed-point eigenvalues $\{0, 9, 12, 14, 15\}$ are rational and
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:59:$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:72:and the operator-norm bound is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:99:a load-bearing fact for any operator-witness claim made here. We
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:35:landings tolerate a shift sweep. The shift is held fixed across
papers/aria-closure-kernel/paper/sections/09_limitations.tex:45:theorem-level rigorous (H$_4$ Coxeter group theory), the choice
papers/aria-closure-kernel/paper/sections/09_limitations.tex:50:\emph{Evidence:} two independent empirical witnesses on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:72:independent empirical witnesses across qualitatively distinct
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:75:the $\Ph^{-2}$ shift as the unique stability clamp under a named
papers/aria-closure-kernel/paper/sections/09_limitations.tex:85:\emph{computed agreement} between two independently-defined
papers/aria-closure-kernel/paper/sections/09_limitations.tex:86:objects, not a derivation that the discrete operator equals the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:92:limit; a continuum limit theorem on H$_n$ Coxeter substrates as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:106:\textbf{Two independent empirical landings, not formal physics.}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:107:The b-anomaly result is a structural fit (kernel shape held fixed)
papers/aria-closure-kernel/paper/sections/09_limitations.tex:110:substrate \emph{is} consciousness). Neither lands a theorem-grade
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:131:representative, not a sample, of the operator's behaviour under
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:138:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:142:in the response primitive without addressing the selection gap.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:145:into this paper.} The cascade-derivation programme, the capstone
papers/aria-closure-kernel/paper/sections/09_limitations.tex:147:infrastructure with this paper but are not load-bearing here.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:158:\item Selection theorem identifying $\Rsixhundred$ over alternative
papers/aria-closure-kernel/paper/sections/09_limitations.tex:160:\item Formal discrete-to-continuum convergence theorem under a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:164:\item Family-membership classification theorem for the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:170:The result is an \emph{operator witness}: a geometry-fixed response
papers/aria-closure-kernel/paper/sections/09_limitations.tex:171:operator on a fixed graph, with no shape parameters tuned to any
papers/aria-closure-kernel/paper/sections/09_limitations.tex:172:dataset, is consistent with two independent empirical landings in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:173:qualitatively distinct regimes. We do not claim the operator is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:7:geometry-fixed response primitive: positive definite under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:28:retuning between regimes, appears as the load-bearing object in:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:32:  held fixed) gives a sign-uniform
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:45:By design, the two witnesses share exactly the geometry-fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:52:not statistical independence of the operator itself.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:55:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:57:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:58:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:66:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:77:selection gap.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:81:geometry-fixed Green operator on a fixed Coxeter graph, with a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:83:two independent empirical landings on qualitatively distinct
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:87:The empirical material gathered here is the operator witness; the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:88:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/01_introduction.tex:5:A response operator on a fixed graph, with no shape parameters tuned
papers/aria-closure-kernel/paper/sections/01_introduction.tex:12:preprint that names the operator, gives its construction in full,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:14:without inheriting either's load-bearing claims. That is what this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:17:The operator is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:53:We claim a single \emph{operator witness}: that one geometry-fixed
papers/aria-closure-kernel/paper/sections/01_introduction.tex:54:operator, on one fixed graph, with no shape-parameter retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:55:between regimes, appears as the load-bearing object in two
papers/aria-closure-kernel/paper/sections/01_introduction.tex:59:\item \textbf{Operator definition is fixed by the construction.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:63:  operator. The Laplacian spectrum, the operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:72:  numerical agreement between two independently-defined objects (a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:82:  on a different test, the qualitative ranking established
papers/aria-closure-kernel/paper/sections/01_introduction.tex:83:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:85:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:90:  dataset and the kernel held fixed; sign uniformity holds in
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:102:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:104:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:107:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:113:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:122:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:127:  reduced flow, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:139:To keep this paper inside the operator-witness scope, we use the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:153:a `computed'-type claim. A statistical agreement at the operator
papers/aria-closure-kernel/paper/sections/01_introduction.tex:156:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:157:selection'.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:163:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:discrete-to-continuum correlation; the same fixed operator appearing
papers/aria-closure-kernel/paper/sections/01_introduction.tex:166:in two independent empirical works (b-anomaly five-dataset
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:170:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:171:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:173:or consciousness) by the operator alone.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:187:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:witnesses (b-anomaly and aria-chess) at the operator level.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:190:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:5:This section threads the first independent empirical landing of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:14:Model, is approximately $q^{2}$-independent in the relevant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:15:kinematic range. The b-anomaly preprint tests a fixed
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:26:here; this is a projection of the operator, not a derivation of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:32:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:dataset, kernel shape held fixed.}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:63:\subsection{What the structural fit establishes}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:\item \textbf{Universality (5/5).} The same fixed kernel shape
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:72:  reproduces the established direction of the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:73:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:89:  ranking — a two-criterion convergence on the same fixed
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:\subsection{What the structural fit does \emph{not} establish}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106:  decisive about whether the shape is forced by data: it is not.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:110:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:123:  verified. The two-criterion agreement is criterion-independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:127:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:132:fixed discrete-to-momentum projection, gives a sign-uniform
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:134:five independent measurements without shape retuning. This does
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:135:not establish the kernel as theorem-grade physics on the flavour
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:138:establish, at the operator level, that the same fixed $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:139:the same fixed $\Rsixhundred$ is consistent with one of two
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:140:independent empirical landings without parameter retuning. The
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:5:This section threads the second independent empirical landing of
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:33:b-anomaly and aria-chess; the same fixed shift used in the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:64:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:109:  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:113:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:121:constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:132:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:133:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:134:scope verbatim. What we add at the operator level is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:136:retuning between regimes — is the load-bearing object on both
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:165:The two witnesses share, by design, exactly the geometry-fixed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:168:threshold, dataset, or methodological choice above the operator
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:171:is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by

exec
/bin/bash -lc "rg -n '\\\\[A-Za-z]+' \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '\\\\label\\{|\\\\ref\\{|\\\\citep\\{|\\\\cite\\{' \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n 'TODO|FIXME|undefined|citation|checkmark|Krüger|—|–' \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\" \"papers/aria-closure-kernel/paper/references.bib\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '\\\\newcommand|\\\\Ph|\\\\Lop|\\\\Cph|\\\\Rsixhundred|V_\\{600\\}|C_\\{\\\\Ph\\}|L_\\{V_\\{600\\}\\}' \"papers/aria-closure-kernel/paper/main.tex\" \"papers/aria-closure-kernel/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 276ms:
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:60:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:63:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:73:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:88:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:90:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:122:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:132:precision (multi-source sweep, \S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:135:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:142:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:188:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:189:\S\ref{sec:agreement} are deterministic outputs of the script.
papers/aria-closure-kernel/paper/main.tex:191:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:192:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:16:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:36:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:69:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:94:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:110:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/05_agreement.tex:112:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:144:an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:18:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:43:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:52:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:73:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:79:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:85:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:93:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:107:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:125:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:134:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/03_substrate.tex:136:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:18:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:28:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:84:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:86:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:92:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:124:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:141:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:181:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:183:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:187:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:191:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:192:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:146:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:151:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:52:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:68:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:96:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:117:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:111:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:112:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:132:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:39:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:46:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:48:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:73:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  ($\sim 2.2$~\citep{KrugerMatias2005}), with a residual
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:141:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:Table~\ref{tab:spectrum} to machine precision; multiplicities sum
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:23:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:84:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:21:\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:49:or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:70:\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:73:regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:87:continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
papers/aria-closure-kernel/paper/sections/09_limitations.tex:104:\subsection{Test/claim}\label{ssec:testclaim}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:114:\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
papers/aria-closure-kernel/paper/sections/09_limitations.tex:134:\subsection{State-drift / out-of-scope}\label{ssec:scope}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:30:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:37:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:64:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:identified in \S\ref{sec:programme_home}. Family-membership is

 succeeded in 286ms:
papers/aria-closure-kernel/paper/main.tex:1:\documentclass[11pt]{article}
papers/aria-closure-kernel/paper/main.tex:3:\usepackage[a4paper, margin=2.5cm]{geometry}
papers/aria-closure-kernel/paper/main.tex:4:\usepackage{amsmath, amssymb, amsthm}
papers/aria-closure-kernel/paper/main.tex:5:\usepackage{booktabs}
papers/aria-closure-kernel/paper/main.tex:6:\usepackage{enumitem}
papers/aria-closure-kernel/paper/main.tex:7:\usepackage{graphicx}
papers/aria-closure-kernel/paper/main.tex:8:\usepackage{natbib}
papers/aria-closure-kernel/paper/main.tex:9:\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
papers/aria-closure-kernel/paper/main.tex:10:\usepackage{xcolor}
papers/aria-closure-kernel/paper/main.tex:12:\graphicspath{{figures/}}
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-closure-kernel/paper/main.tex:19:\title{The closure-response operator
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:24:\author{%
papers/aria-closure-kernel/paper/main.tex:26:  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
papers/aria-closure-kernel/paper/main.tex:27:  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
papers/aria-closure-kernel/paper/main.tex:28:  \texttt{@vfd\_org}%
papers/aria-closure-kernel/paper/main.tex:31:\date{April 2026}
papers/aria-closure-kernel/paper/main.tex:33:\begin{document}
papers/aria-closure-kernel/paper/main.tex:35:\maketitle
papers/aria-closure-kernel/paper/main.tex:37:\noindent\textbf{Status:} Preprint, not peer-reviewed.
papers/aria-closure-kernel/paper/main.tex:39:\noindent\emph{Headline.}
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
papers/aria-closure-kernel/paper/main.tex:43:and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
papers/aria-closure-kernel/paper/main.tex:44:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:50:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:52:eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:56:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:58:\emph{independent} empirical works: a passive-regime structural
papers/aria-closure-kernel/paper/main.tex:59:fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
papers/aria-closure-kernel/paper/main.tex:60:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:63:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:65:\noindent\emph{Scope.}
papers/aria-closure-kernel/paper/main.tex:66:This paper presents an empirical \emph{operator witness}: a
papers/aria-closure-kernel/paper/main.tex:69:retuning between regimes. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:70:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:71:claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
papers/aria-closure-kernel/paper/main.tex:73:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:79:\begin{abstract}
papers/aria-closure-kernel/paper/main.tex:80:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:82:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:87:$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
papers/aria-closure-kernel/paper/main.tex:88:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:90:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:92:(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
papers/aria-closure-kernel/paper/main.tex:95:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:96:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:98:unweighted variant, above the two $\Ph$-cocycle weighted variants
papers/aria-closure-kernel/paper/main.tex:102:established separately by b-anomaly's data $\chi^{2}$ comparison
papers/aria-closure-kernel/paper/main.tex:108:\noindent\emph{(i) Operator definition and properties.}
papers/aria-closure-kernel/paper/main.tex:109:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:111:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:112:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:114:$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
papers/aria-closure-kernel/paper/main.tex:116:\noindent\emph{(ii) The 600-cell instance.}
papers/aria-closure-kernel/paper/main.tex:117:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:119:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:121:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:122:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:124:\noindent\emph{(iii) Discrete-to-continuum agreement.}
papers/aria-closure-kernel/paper/main.tex:126:$\psi = \Cph^{-1} f$ for a localised source and the continuum
papers/aria-closure-kernel/paper/main.tex:127:prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
papers/aria-closure-kernel/paper/main.tex:129:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:132:precision (multi-source sweep, \S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:134:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:135:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:136:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:137:$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
papers/aria-closure-kernel/paper/main.tex:138:$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
papers/aria-closure-kernel/paper/main.tex:139:(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
papers/aria-closure-kernel/paper/main.tex:142:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:143:$\Rsixhundred$, augmented by a recurrent self-model layer with one
papers/aria-closure-kernel/paper/main.tex:145:$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
papers/aria-closure-kernel/paper/main.tex:146:$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
papers/aria-closure-kernel/paper/main.tex:150:$C\!\times\!P$ interaction (P4), plus $6/6$ literature-thresholded
papers/aria-closure-kernel/paper/main.tex:153:\noindent\emph{What we do not claim.}
papers/aria-closure-kernel/paper/main.tex:154:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:155:stability clamp making $\Cph$ strictly positive definite. We do
papers/aria-closure-kernel/paper/main.tex:156:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:163:this paper is: \emph{one geometry-fixed operator on one fixed
papers/aria-closure-kernel/paper/main.tex:167:\end{abstract}
papers/aria-closure-kernel/paper/main.tex:170:\input{sections/01_introduction.tex}
papers/aria-closure-kernel/paper/main.tex:171:\input{sections/02_definition.tex}
papers/aria-closure-kernel/paper/main.tex:172:\input{sections/03_substrate.tex}
papers/aria-closure-kernel/paper/main.tex:173:\input{sections/04_spectrum.tex}
papers/aria-closure-kernel/paper/main.tex:174:\input{sections/05_agreement.tex}
papers/aria-closure-kernel/paper/main.tex:175:\input{sections/06_passive_witness.tex}
papers/aria-closure-kernel/paper/main.tex:176:\input{sections/07_active_witness.tex}
papers/aria-closure-kernel/paper/main.tex:177:\input{sections/08_programme_home.tex}
papers/aria-closure-kernel/paper/main.tex:178:\input{sections/09_limitations.tex}
papers/aria-closure-kernel/paper/main.tex:179:\input{sections/10_conclusion.tex}
papers/aria-closure-kernel/paper/main.tex:182:\section*{Reproducibility}
papers/aria-closure-kernel/paper/main.tex:186:is reproducible from \texttt{repro/verify\_kernel.py} in this
papers/aria-closure-kernel/paper/main.tex:188:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:189:\S\ref{sec:agreement} are deterministic outputs of the script.
papers/aria-closure-kernel/paper/main.tex:191:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:192:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/main.tex:195:\bibliographystyle{plainnat}
papers/aria-closure-kernel/paper/main.tex:196:\bibliography{references}
papers/aria-closure-kernel/paper/main.tex:198:\end{document}
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:5:\subsection{Definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:11:continuum operator $-\Delta$ with chosen boundary conditions).
papers/aria-closure-kernel/paper/sections/02_definition.tex:12:Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
papers/aria-closure-kernel/paper/sections/02_definition.tex:13:and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:15:The \emph{closure-response operator} is
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:18:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:20:\emph{closure response field} is
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:23:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:30:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/02_definition.tex:31:\item \textbf{(H1) Self-adjointness.} $L_M$ is self-adjoint on the
papers/aria-closure-kernel/paper/sections/02_definition.tex:35:\item \textbf{(H2) Non-negativity.} $L_M \geq 0$ as a
papers/aria-closure-kernel/paper/sections/02_definition.tex:36:  quadratic form: $\langle f, L_M f\rangle \geq 0$ for all $f$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:37:\item \textbf{(H3) Connectedness.} On a finite graph, $M$ is
papers/aria-closure-kernel/paper/sections/02_definition.tex:41:\end{itemize}
papers/aria-closure-kernel/paper/sections/02_definition.tex:52:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:55:eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
papers/aria-closure-kernel/paper/sections/02_definition.tex:56:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:58:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:59:                    \;=\; \Ph^{-2} \;>\; 0,
papers/aria-closure-kernel/paper/sections/02_definition.tex:61:so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:The operator norm of $\Cph^{-1}$ is the reciprocal of its smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:68:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:69:\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
papers/aria-closure-kernel/paper/sections/02_definition.tex:70:              \;=\; 1/\Ph^{-2} \;=\; \Ph^{2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:71:              \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/02_definition.tex:72:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:75:\|\psi\|_{2} \;\leq\; \Ph^{2}\, \|f\|_{2}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:77:Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
papers/aria-closure-kernel/paper/sections/02_definition.tex:78:graph $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:84:In one projected coordinate $x \in \mathbb{R}$ with
papers/aria-closure-kernel/paper/sections/02_definition.tex:85:$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
papers/aria-closure-kernel/paper/sections/02_definition.tex:86:$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:90:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
papers/aria-closure-kernel/paper/sections/02_definition.tex:96:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:97:the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
papers/aria-closure-kernel/paper/sections/02_definition.tex:98:chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
papers/aria-closure-kernel/paper/sections/02_definition.tex:99:is compared to $G(\|v - v_{\mathrm{src}}\|)$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:101:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/sections/02_definition.tex:103:The shift $\Ph^{-2}$ is chosen so that:
papers/aria-closure-kernel/paper/sections/02_definition.tex:104:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:\item $\Cph$ is strictly positive definite (the smallest eigenvalue
papers/aria-closure-kernel/paper/sections/02_definition.tex:106:  is exactly $\Ph^{-2}$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:108:  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:109:  are fixed by the single design choice $\Ph^{-2}$, giving a single
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:\item the continuum projection (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:112:  has decay scale $\Ph$, not a free length parameter.
papers/aria-closure-kernel/paper/sections/02_definition.tex:113:\end{enumerate}
papers/aria-closure-kernel/paper/sections/02_definition.tex:114:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:117:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:5:This section positions $\Cph$ within the broader cascade programme
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:7:matters for the hostile-review reading: $\Cph$ is the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:8:\emph{response} primitive; \emph{selection} (which response
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:family as $\Cph$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:19:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:20:\item \textbf{RH polynomial filter} (forthcoming RH artifact in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:21:  this programme). Cascade closure functional on $\mathbb{R}^{120}$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:22:  $F_{\mathrm{filt}}(x) = \tfrac12 \langle x, p_{\mathrm{fix}}(L)^{2} x\rangle$
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:23:  with $\Psi_{t} = e^{-t\, p_{\mathrm{fix}}(L)^{2}}$. Programme-positioned
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:24:  as the $\sigma$-fix-annihilator instance of the family: a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:26:  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:28:\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:30:  programme-positioned as a $\Cph$-style mass-regularised Laplacian
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:35:  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:38:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:40:We list the family-membership claim as \emph{programme-positioned},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:48:The closure response $\psi = \Cph^{-1} f$ is determined by the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:chosen substrate plus the design-level shift: $\Cph$ is fixed by
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:50:the substrate $\Rsixhundred$ and the design-level choice
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:51:$\Ph^{-2}$, and the response is the resulting linear inverse.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:52:This is a \emph{response} primitive. It does \emph{not} answer:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:53:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:54:\item Why this substrate? (Selection across regular 4-polytopes
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:55:  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:56:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:58:\item How does the system pick a response configuration over
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:61:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:65:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:66:\item \textbf{Forthcoming RH artifact}: the closure-flow suppression
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:67:  hypothesis $\textup{H}_{\mathrm{attr}}$ at the level of the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:69:  $\Psi_{t}$ is a finite-dimensional analogue, by design.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:70:\item \textbf{Adaptive Closure
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:72:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:75:  on $W$-trajectories — \emph{none delivered} in that paper.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:77:  the substrate-witness scope explicitly does \emph{not} deliver
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:80:\end{enumerate}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:86:in this paper strengthen external confidence in the \emph{response}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:89:\subsection{What this paper closes vs leaves open}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:91:\paragraph{Closes (at the operator-witness level).}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:93:\item The operator $\Cph$ is well-defined and positive definite
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:95:  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:96:  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:98:  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:99:  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:104:  (\texttt{repro/verify\_kernel.py}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:105:\item Discrete-to-continuum agreement at per-vertex Pearson
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:111:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:112:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:113:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:115:\paragraph{Leaves open.}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:116:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:120:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:124:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:127:  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:129:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:132:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:134:\item \emph{Family-membership theorem.} The programme-home
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:137:  \emph{programme-positioned}, not formally classified.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:138:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12:The Wilson-coefficient Hamiltonian for $b\to s\mu^{+}\mu^{-}$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:13:contains a $C_{9}^{(\prime)}$ contribution that, in the Standard
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:19:\Delta C_{9}^{\mathrm{eff}}(q^{2})
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:21:A \cdot \kappa_{V_{600}}(q^{2}),
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:\end{equation}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:23:where $\kappa_{V_{600}}(q^{2})$ is the projection of $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:$\Rsixhundred$ to the flavour-physics $q^{2}$ axis (the b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:$\Ph^{-2}$), and $A$ is a single fitted dimensionless amplitude
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:28:per dataset. The kernel shape $\kappa_{V_{600}}$ is positive on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:31:$\Delta C_{9}^{\mathrm{eff}}$. The kernel
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:32:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:34:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:36:\subsection{The five-dataset structural fit}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:39:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:42:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:43:\centering
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:44:\small
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:45:\caption{b-anomaly five-dataset structural fit. Verbatim
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:46:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:48:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:49:\begin{tabular}{l l r r r r}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:50:\toprule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:51:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:53:\midrule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:54:LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:55:LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:56:CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:57:LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:58:LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:59:\bottomrule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:60:\end{tabular}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:61:\end{table}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:63:\subsection{What the structural fit establishes}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:65:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:\item \textbf{Universality (5/5).} The same fixed kernel shape
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:70:\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71:  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:73:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:75:\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:76:  $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  ($\sim 2.2$~\citep{KrugerMatias2005}), with a residual
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:79:  $\sim 50\%$ overshoot on top of the K--M prediction. The
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:82:\item \textbf{Geometry-first variant test.} Of three discrete
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:83:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:84:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:87:  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:88:  ($\chi^{2}=13.555$). The two criteria agree on the variant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:91:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:\subsection{What the structural fit does \emph{not} establish}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:98:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:99:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:101:  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:103:  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:107:\item \textbf{Free-width Gaussian alternative.} A free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:114:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:119:\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:  the data-$\chi^{2}$ ranking with the pure-geometry ranking
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:127:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:129:The b-anomaly result is the \emph{passive-regime} empirical
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:130:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:131:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:133:description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:138:establish, at the operator level, that the same fixed $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:139:the same fixed $\Rsixhundred$ is consistent with one of two
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:141:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5:The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:values match the closed-form $\mathbb{Z}[\Ph]$ list given in
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:Table~\ref{tab:spectrum} to machine precision; multiplicities sum
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:10:\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:11:$120\times 120$ symmetric eigendecomposition, deterministic at
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:16:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:17:\centering
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:18:\small
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:19:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:20:Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:21:values returned by \texttt{repro/verify\_kernel.py}; multiplicities
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:23:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:24:\begin{tabular}{c c c}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:25:\toprule
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:27:\midrule
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:28:$0$            & $-3\!\times\!10^{-15}$ (machine zero) & $1$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:29:$12 - 6\Ph$    & $2.2918$  & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:30:$12 - 4\Ph$    & $5.5279$  & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:34:$4\Ph + 8$     & $14.4721$ & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:36:$6\Ph + 6$     & $15.7082$ & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:37:\midrule
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:38:\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:39:\bottomrule
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:40:\end{tabular}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:41:\end{table}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:43:\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:44:\begin{align*}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:45:12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:46:12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:47:4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:48:6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:49:\end{align*}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:50:The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:51:$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:53:$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:56:$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:58:\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:59:$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:60:remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:61:artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:69:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:70:\;\approx\; 0.381966,
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:74:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:76:\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:79:of $\Cph$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:80:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:81:= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:83:\subsection{H$_4$ irrep block decomposition (imported context)}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:84:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:86:The eigenspaces of $\Lop$ partition into H$_4$-proper and
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:87:$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:89:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:90:$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:97:the irrep block decomposition is \emph{not} verified by
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:98:\texttt{repro/verify\_kernel.py} of this paper and is not used as
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:12:$\lambda_{\min}(L_M) > 0$ give the strict inequality
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:$\|\Cph^{-1}\| < \Ph^{2}$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:19:the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:21:the unweighted Laplacian, above the two $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:generators by \texttt{repro/verify\_kernel.py}; no parameter is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:29:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:30:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:33:  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:34:  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:36:  $B_s\to\phi$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:37:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:40:  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:41:  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:44:\end{enumerate}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:46:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:$\Ph^{-2}$. Above that operator level, they share no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:54:\textbf{Operator-witness scope.} This is an operator witness, not
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:61:$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:64:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:69:\textbf{Programme position.} The cascade-programme home for the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:72:cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:identified in \S\ref{sec:programme_home}. Family-membership is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:\emph{programme-positioned}, not formally classified. The two
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:76:\emph{response} primitive without reducing or addressing the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:9:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
papers/aria-closure-kernel/paper/sections/05_agreement.tex:13:the three tested variants (unweighted, $\Ph$-geometric weighted,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:$\Ph$-arithmetic weighted).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:16:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:25:$v \in V$, compute the Euclidean chord distance
papers/aria-closure-kernel/paper/sections/05_agreement.tex:28:G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:31:$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:33:trivially the diagonal of $\Cph^{-1}$ and the chord distance is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:36:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:38:\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
papers/aria-closure-kernel/paper/sections/05_agreement.tex:39:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:40:\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:42:  (averaging $\psi(v)$ over each H$_3$ shell first, then
papers/aria-closure-kernel/paper/sections/05_agreement.tex:45:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:48:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:49:\item Per-vertex test: $|V|-1 = 119$ data points (every
papers/aria-closure-kernel/paper/sections/05_agreement.tex:50:  non-source vertex), source $v_{0}$ \emph{excluded} (the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:51:  response there is the diagonal of $\Cph^{-1}$ and the chord
papers/aria-closure-kernel/paper/sections/05_agreement.tex:53:\item Shell-mean test: $9$ data points (one per H$_3$ shell);
papers/aria-closure-kernel/paper/sections/05_agreement.tex:56:  ($\psi(v_{0}), G(0)$) point.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:57:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:59:$\psi$ is shell-constant up to numerical precision — the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:61:($\sim 10^{-16}$). The two tests therefore differ in weighting and
papers/aria-closure-kernel/paper/sections/05_agreement.tex:69:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:71:Two $\Ph$-cocycle weighted Laplacian variants are tested as
papers/aria-closure-kernel/paper/sections/05_agreement.tex:74:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:75:\item \textbf{$\Ph$-geometric weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:76:  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:77:  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:79:\item \textbf{$\Ph$-arithmetic weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:80:  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
papers/aria-closure-kernel/paper/sections/05_agreement.tex:81:  $\omega_{+}$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:82:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:87:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/05_agreement.tex:88:\centering
papers/aria-closure-kernel/paper/sections/05_agreement.tex:89:\small
papers/aria-closure-kernel/paper/sections/05_agreement.tex:90:\caption{Per-vertex and shell-mean Pearson correlations between the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:91:discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
papers/aria-closure-kernel/paper/sections/05_agreement.tex:93:Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:94:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:95:\begin{tabular}{l c c}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:96:\toprule
papers/aria-closure-kernel/paper/sections/05_agreement.tex:98:\midrule
papers/aria-closure-kernel/paper/sections/05_agreement.tex:99:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:102:\bottomrule
papers/aria-closure-kernel/paper/sections/05_agreement.tex:103:\end{tabular}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:104:\end{table}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:106:\textbf{Reading.} Among the three tested variants, the unweighted
papers/aria-closure-kernel/paper/sections/05_agreement.tex:110:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:112:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:114:correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
papers/aria-closure-kernel/paper/sections/05_agreement.tex:121:\subsection{What the agreement does and does not establish}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:123:\paragraph{Does establish.} A geometric agreement: the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:126:closed-form continuum exponential at the same length scale $\Ph$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:128:objects: (i) the discrete inverse of a $120\times 120$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:130:exponential. The $\Ph$-mediated agreement is an empirical fact
papers/aria-closure-kernel/paper/sections/05_agreement.tex:134:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:136:Gaussian alternative that fits comparably in $\chi^{2}$ at the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:140:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/05_agreement.tex:144:an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:12:by \texttt{repro/verify\_kernel.py} from the canonical generators
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:17:$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
papers/aria-closure-kernel/paper/sections/03_substrate.tex:18:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
papers/aria-closure-kernel/paper/sections/03_substrate.tex:21:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:22:\item \textbf{Axis family} ($8$ vertices): all permutations of
papers/aria-closure-kernel/paper/sections/03_substrate.tex:23:  $(\pm 1, 0, 0, 0)$;
papers/aria-closure-kernel/paper/sections/03_substrate.tex:24:\item \textbf{Half-integer family} ($16$ vertices): all sign
papers/aria-closure-kernel/paper/sections/03_substrate.tex:25:  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
papers/aria-closure-kernel/paper/sections/03_substrate.tex:26:\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
papers/aria-closure-kernel/paper/sections/03_substrate.tex:27:  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:28:  $\Ph^{2} = \Ph + 1$ identity, equivalently
papers/aria-closure-kernel/paper/sections/03_substrate.tex:29:  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:30:\end{itemize}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:34:orbit. Reproduced by \texttt{repro/verify\_kernel.py:build\_v600};
papers/aria-closure-kernel/paper/sections/03_substrate.tex:35:the numerical check $\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms
papers/aria-closure-kernel/paper/sections/03_substrate.tex:39:$120$ vertices. Every vertex therefore has \emph{identical} local
papers/aria-closure-kernel/paper/sections/03_substrate.tex:43:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:45:For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:48:\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:50:The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
papers/aria-closure-kernel/paper/sections/03_substrate.tex:52:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:54:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:56:$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:60:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:62:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:63:\item $|V|=120$ vertices,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:64:\item $|E|=720$ edges,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:65:\item every vertex has degree exactly $12$ (H$_4$ transitivity on
papers/aria-closure-kernel/paper/sections/03_substrate.tex:66:  the vertex set forces \emph{uniformity} of the local structure;
papers/aria-closure-kernel/paper/sections/03_substrate.tex:69:  \texttt{repro/verify\_kernel.py}),
papers/aria-closure-kernel/paper/sections/03_substrate.tex:70:\item the graph is connected (verified numerically by counting
papers/aria-closure-kernel/paper/sections/03_substrate.tex:73:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:\end{itemize}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:76:\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:79:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:85:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:86:\langle v, v_{0}\rangle
papers/aria-closure-kernel/paper/sections/03_substrate.tex:87:\;\in\;
papers/aria-closure-kernel/paper/sections/03_substrate.tex:88:\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:89:       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:90:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:91:indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:93:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
papers/aria-closure-kernel/paper/sections/03_substrate.tex:97:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:101:verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:103:\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:107:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:109:The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
papers/aria-closure-kernel/paper/sections/03_substrate.tex:110:the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
papers/aria-closure-kernel/paper/sections/03_substrate.tex:113:is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:116:inner product exactly $\Ph/2$ within machine precision (tolerance
papers/aria-closure-kernel/paper/sections/03_substrate.tex:117:$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:119:\subsection{What the substrate fixes, and what it does not}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:121:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:122:\item \textbf{Fixed by the construction once $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:125:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:130:\item \textbf{Not fixed by this paper}: the choice of
papers/aria-closure-kernel/paper/sections/03_substrate.tex:131:  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
papers/aria-closure-kernel/paper/sections/03_substrate.tex:134:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/03_substrate.tex:136:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:137:\end{itemize}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:9:$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:10:\mathrm{strengthening\ build})$.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested
papers/aria-closure-kernel/paper/sections/09_limitations.tex:15:whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:21:\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:25:\texttt{repro/verify\_kernel.py} extension to the $24$-cell and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:32:\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
papers/aria-closure-kernel/paper/sections/09_limitations.tex:33:nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
papers/aria-closure-kernel/paper/sections/09_limitations.tex:37:\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:38:for $\delta \in \{0.01, 0.05, 0.10, 0.25\}$ on the discrete-to-
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:43:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-closure-kernel/paper/sections/09_limitations.tex:44:observables.} While the construction of $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:46:of \emph{this} polytope as the discrete substrate instance is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:49:or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:50:\emph{Evidence:} two independent empirical witnesses on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:51:$\Rsixhundred$. \emph{Strengthening build:} formal substrate
papers/aria-closure-kernel/paper/sections/09_limitations.tex:54:\textbf{The geometry-first variant agreement is not historically
papers/aria-closure-kernel/paper/sections/09_limitations.tex:58:data-$\chi^{2}$ ranking. The two-criterion convergence is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:60:different test from b-anomaly's data $\chi^{2}$) but not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:61:historically pre-registered. \emph{Disclosure:} we inherit the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:62:caveat verbatim. \emph{Strengthening build:} a future blind variant
papers/aria-closure-kernel/paper/sections/09_limitations.tex:64:$\chi^{2}$.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:69:functional or symmetry argument. \emph{Disclosure:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:70:\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:73:regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:75:the $\Ph^{-2}$ shift as the unique stability clamp under a named
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:81:\textbf{The discrete-to-continuum agreement is descriptive, not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:83:$\Rsixhundred$ and the continuum kernel
papers/aria-closure-kernel/paper/sections/09_limitations.tex:84:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:85:\emph{computed agreement} between two independently-defined
papers/aria-closure-kernel/paper/sections/09_limitations.tex:87:continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
papers/aria-closure-kernel/paper/sections/09_limitations.tex:88:this explicitly. \emph{Evidence:} the agreement is at machine
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:90:per-vertex correlation. \emph{Strengthening build:} a formal
papers/aria-closure-kernel/paper/sections/09_limitations.tex:93:$n \to \infty$.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:95:\textbf{Variant ranking is criterion-dependent.} The unweighted
papers/aria-closure-kernel/paper/sections/09_limitations.tex:97:and b-anomaly's data $\chi^{2}$, but neither criterion is the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:99:$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
papers/aria-closure-kernel/paper/sections/09_limitations.tex:100:Laplacian) are not tested here. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:101:extend \texttt{repro/verify\_kernel.py} to a wider variant
papers/aria-closure-kernel/paper/sections/09_limitations.tex:104:\subsection{Test/claim}\label{ssec:testclaim}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:106:\textbf{Two independent empirical landings, not formal physics.}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:110:substrate \emph{is} consciousness). Neither lands a theorem-grade
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:114:\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
papers/aria-closure-kernel/paper/sections/09_limitations.tex:116:\emph{Strengthening build:} more flavour-physics datasets
papers/aria-closure-kernel/paper/sections/09_limitations.tex:122:\textbf{Discrete-to-continuum correlation reported on a single pole,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:126:under choice of source vertex. \texttt{repro/verify\_kernel.py}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:129:(\texttt{multi\_source\_sweep.max\_minus\_min} in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:130:\texttt{results.json}). The single-pole headline is therefore a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:134:\subsection{State-drift / out-of-scope}\label{ssec:scope}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:136:\textbf{Selection layer not delivered.} As enumerated in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:144:\textbf{No deuteron / hadron / RH / capstone material is loaded
papers/aria-closure-kernel/paper/sections/09_limitations.tex:150:\textbf{Out-of-scope items NOT delivered (correctly).}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:151:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:156:\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:158:\item Selection theorem identifying $\Rsixhundred$ over alternative
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:160:\item Formal discrete-to-continuum convergence theorem under a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:164:\item Family-membership classification theorem for the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:166:\end{itemize}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:168:\subsection{The honest verdict}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:170:The result is an \emph{operator witness}: a geometry-fixed response
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:7:of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
papers/aria-closure-kernel/paper/sections/01_introduction.tex:18:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\qquad \Ph \;=\; (1+\sqrt 5)/2,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:21:\end{equation}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:24:$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
papers/aria-closure-kernel/paper/sections/01_introduction.tex:25:non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
papers/aria-closure-kernel/paper/sections/01_introduction.tex:26:positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:28:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:30:\end{equation}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:32:Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:36:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
papers/aria-closure-kernel/paper/sections/01_introduction.tex:39:short edges $\langle v, w\rangle = \Ph/2$. The choice of this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:46:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:48:\texttt{repro/verify\_kernel.py} from the canonical generators
papers/aria-closure-kernel/paper/sections/01_introduction.tex:51:\subsection*{What this paper claims}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:53:We claim a single \emph{operator witness}: that one geometry-fixed
papers/aria-closure-kernel/paper/sections/01_introduction.tex:58:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/01_introduction.tex:59:\item \textbf{Operator definition is fixed by the construction.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:60:  Once $\Rsixhundred$ is selected and the stability shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:61:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:66:  \texttt{repro/verify\_kernel.py}.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:67:\item \textbf{Discrete-to-continuum agreement is empirical, not
papers/aria-closure-kernel/paper/sections/01_introduction.tex:69:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:70:  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
papers/aria-closure-kernel/paper/sections/01_introduction.tex:71:  $\rho = 0.976$ on the unweighted graph Laplacian. This is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:75:\item \textbf{Variant comparison among the three tested variants.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:76:  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  $\Ph$-arithmetic edge weights via shell-grade exponents
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:83:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:84:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:85:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:86:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
papers/aria-closure-kernel/paper/sections/01_introduction.tex:91:  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:92:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:97:\end{enumerate}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:99:\subsection*{What this paper does \emph{not} claim}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:101:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/01_introduction.tex:102:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:  $\Ph^{-2}$ is a design-level stability clamp that bounds
papers/aria-closure-kernel/paper/sections/01_introduction.tex:104:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:107:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:110:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:113:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:116:  datasets comparably in $\chi^{2}$ at the cost of one extra shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:118:  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:120:  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:122:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:124:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:130:\item \emph{Not a circuit-level model on the active-regime side.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:132:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:135:\end{itemize}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:137:\subsection*{Mapping from numerics to admissible claims}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:141:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/01_introduction.tex:142:$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
papers/aria-closure-kernel/paper/sections/01_introduction.tex:143:$\mathcal C_{\mathrm{admissible}}$ by the rule
papers/aria-closure-kernel/paper/sections/01_introduction.tex:145:q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
papers/aria-closure-kernel/paper/sections/01_introduction.tex:146:        \mathcal C_{\mathrm{admissible}},
papers/aria-closure-kernel/paper/sections/01_introduction.tex:147:\qquad
papers/aria-closure-kernel/paper/sections/01_introduction.tex:148:\mathcal C_{\mathrm{admissible}}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:149:   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:159:\medskip
papers/aria-closure-kernel/paper/sections/01_introduction.tex:160:\begin{center}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:161:\fbox{\parbox{0.92\linewidth}{\small
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:\textbf{What is claimed / what is not.}\par
papers/aria-closure-kernel/paper/sections/01_introduction.tex:163:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:168:witness) without shape-parameter retuning between regimes.\par
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:170:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:175:\end{center}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:177:\subsection*{Layout}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:181:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:183:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:187:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:191:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:192:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:15:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:16:\item One \emph{condition-dependent} self-injection coupling
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:17:  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:20:\item One \emph{substrate-pinned} nonlinearity
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:21:  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:25:\item Condition-specific \emph{biologically-motivated} stimulus
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:31:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:37:\subsection{Eighteen preregistered correspondences}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:41:\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:46:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:49:\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:50:  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:53:\item No preregistered threshold has been modified.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:54:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:57:interaction term), \emph{not} as a threshold change. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:60:\subsection{Six drug/sleep EEG signatures}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:66:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:67:\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:74:\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:75:  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:76:\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:77:  wake (threshold $\in [1.5, 5.0]$, empirical reference
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:78:  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:79:\item \textbf{Propofol continuity drop}: $+0.066$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:82:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:83:\item \textbf{Recovery deterministic identity to wake}: under the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:86:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:88:\subsection{Cross-domain selectivity}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:90:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:91:\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:95:  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:96:\item \textbf{Conversation pattern recognition (P14--P16)}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:99:  neutrality band $|\cdot| < 10$pp). The substrate is selectively
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:103:\item \textbf{HCP brain functional connectivity (P17--P18)}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:105:  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:106:  homogeneity, $+79.78\sigma$ on raw participation ratio (with
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:108:  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:111:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:113:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:115:The aria-chess result is the \emph{active-regime} empirical
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:117:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:119:$k=12$; no other \emph{kernel-shape} parameter enters. Above the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:124:this paper. The kernel shift $\Ph^{-2}$ is not retuned between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:131:does not claim the substrate \emph{is} consciousness, does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:139:\subsection{Two-witness structure}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:141:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:142:\centering
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:143:\small
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:145:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:146:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147:\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:\toprule
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:\midrule
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:151:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:153:Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:155:Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:156:Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:159:Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:161:\bottomrule
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:162:\end{tabular}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:163:\end{table}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:166:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:167:the same shift $\Ph^{-2}$. They share no fitted parameter,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:170:$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$

 succeeded in 331ms:
papers/aria-closure-kernel/paper/sections/05_agreement.tex:59:$\psi$ is shell-constant up to numerical precision — the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:113:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:114:correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
papers/aria-closure-kernel/paper/sections/05_agreement.tex:135:empirical landing — the b-anomaly paper documents a free-width
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:75:  on $W$-trajectories — \emph{none delivered} in that paper.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:131:  convergence — all explicitly not delivered
papers/aria-closure-kernel/paper/sections/02_definition.tex:47:outside this class — projected coordinates with non-standard
papers/aria-closure-kernel/paper/sections/02_definition.tex:49:or operators with negative spectrum — require their own analysis,
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:157:  Hodge edge Laplacian — open build of ACT.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:72:cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:(predicted) — match to six decimal places. The largest eigenvalue
papers/aria-closure-kernel/paper/sections/01_introduction.tex:49:alone — no external data input.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  full reduced-flow convergence — is left open in that paper and
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:77:  the predicted Krüger--Matias $P$-basis vs $S$-basis amplification
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:89:  ranking — a two-criterion convergence on the same fixed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:68:  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:136:retuning between regimes — is the load-bearing object on both

 succeeded in 346ms:
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
papers/aria-closure-kernel/paper/main.tex:43:and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
papers/aria-closure-kernel/paper/main.tex:44:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:50:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:52:eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:56:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:70:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:71:claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
papers/aria-closure-kernel/paper/main.tex:80:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:82:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:92:(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
papers/aria-closure-kernel/paper/main.tex:95:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:96:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:98:unweighted variant, above the two $\Ph$-cocycle weighted variants
papers/aria-closure-kernel/paper/main.tex:109:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:111:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:112:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:114:$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
papers/aria-closure-kernel/paper/main.tex:117:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:119:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:121:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:126:$\psi = \Cph^{-1} f$ for a localised source and the continuum
papers/aria-closure-kernel/paper/main.tex:129:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:136:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:142:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:143:$\Rsixhundred$, augmented by a recurrent self-model layer with one
papers/aria-closure-kernel/paper/main.tex:154:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:155:stability clamp making $\Cph$ strictly positive definite. We do
papers/aria-closure-kernel/paper/main.tex:156:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:9:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
papers/aria-closure-kernel/paper/sections/05_agreement.tex:13:the three tested variants (unweighted, $\Ph$-geometric weighted,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:$\Ph$-arithmetic weighted).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:28:G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:33:trivially the diagonal of $\Cph^{-1}$ and the chord distance is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:51:  response there is the diagonal of $\Cph^{-1}$ and the chord
papers/aria-closure-kernel/paper/sections/05_agreement.tex:71:Two $\Ph$-cocycle weighted Laplacian variants are tested as
papers/aria-closure-kernel/paper/sections/05_agreement.tex:75:\item \textbf{$\Ph$-geometric weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:77:  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:79:\item \textbf{$\Ph$-arithmetic weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:91:discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:126:closed-form continuum exponential at the same length scale $\Ph$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:130:exponential. The $\Ph$-mediated agreement is an empirical fact
papers/aria-closure-kernel/paper/sections/05_agreement.tex:140:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/02_definition.tex:12:Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
papers/aria-closure-kernel/paper/sections/02_definition.tex:13:and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:56:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:58:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:59:                    \;=\; \Ph^{-2} \;>\; 0,
papers/aria-closure-kernel/paper/sections/02_definition.tex:61:so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:The operator norm of $\Cph^{-1}$ is the reciprocal of its smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:69:\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
papers/aria-closure-kernel/paper/sections/02_definition.tex:70:              \;=\; 1/\Ph^{-2} \;=\; \Ph^{2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:75:\|\psi\|_{2} \;\leq\; \Ph^{2}\, \|f\|_{2}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:77:Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
papers/aria-closure-kernel/paper/sections/02_definition.tex:78:graph $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:85:$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
papers/aria-closure-kernel/paper/sections/02_definition.tex:86:$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
papers/aria-closure-kernel/paper/sections/02_definition.tex:97:the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
papers/aria-closure-kernel/paper/sections/02_definition.tex:101:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/sections/02_definition.tex:103:The shift $\Ph^{-2}$ is chosen so that:
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:\item $\Cph$ is strictly positive definite (the smallest eigenvalue
papers/aria-closure-kernel/paper/sections/02_definition.tex:106:  is exactly $\Ph^{-2}$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:108:  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:109:  are fixed by the single design choice $\Ph^{-2}$, giving a single
papers/aria-closure-kernel/paper/sections/02_definition.tex:112:  has decay scale $\Ph$, not a free length parameter.
papers/aria-closure-kernel/paper/sections/02_definition.tex:114:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:5:This section positions $\Cph$ within the broader cascade programme
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:7:matters for the hostile-review reading: $\Cph$ is the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:family as $\Cph$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:30:  programme-positioned as a $\Cph$-style mass-regularised Laplacian
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:48:The closure response $\psi = \Cph^{-1} f$ is determined by the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:chosen substrate plus the design-level shift: $\Cph$ is fixed by
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:50:the substrate $\Rsixhundred$ and the design-level choice
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:51:$\Ph^{-2}$, and the response is the resulting linear inverse.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:56:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:93:\item The operator $\Cph$ is well-defined and positive definite
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:95:  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:99:  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:21:A \cdot \kappa_{V_{600}}(q^{2}),
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:23:where $\kappa_{V_{600}}(q^{2})$ is the projection of $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:$\Rsixhundred$ to the flavour-physics $q^{2}$ axis (the b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:$\Ph^{-2}$), and $A$ is a single fitted dimensionless amplitude
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:28:per dataset. The kernel shape $\kappa_{V_{600}}$ is positive on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:32:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:34:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:83:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:84:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:130:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:131:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:138:establish, at the operator level, that the same fixed $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:139:the same fixed $\Rsixhundred$ is consistent with one of two
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5:The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:values match the closed-form $\mathbb{Z}[\Ph]$ list given in
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:19:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:20:Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:29:$12 - 6\Ph$    & $2.2918$  & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:30:$12 - 4\Ph$    & $5.5279$  & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:34:$4\Ph + 8$     & $14.4721$ & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:36:$6\Ph + 6$     & $15.7082$ & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:43:\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:45:12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:46:12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:47:4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:48:6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:50:The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:51:$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:53:$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:69:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:74:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:79:of $\Cph$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:80:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:81:= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:86:The eigenspaces of $\Lop$ partition into H$_4$-proper and
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:89:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:82:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:117:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:124:this paper. The kernel shift $\Ph^{-2}$ is not retuned between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:145:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:155:Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:156:Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:166:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:167:the same shift $\Ph^{-2}$. They share no fitted parameter,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:$\|\Cph^{-1}\| < \Ph^{2}$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:19:the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:21:the unweighted Laplacian, above the two $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:46:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:$\Ph^{-2}$. Above that operator level, they share no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:15:whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:32:\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
papers/aria-closure-kernel/paper/sections/09_limitations.tex:33:nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
papers/aria-closure-kernel/paper/sections/09_limitations.tex:37:\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:44:observables.} While the construction of $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:51:$\Rsixhundred$. \emph{Strengthening build:} formal substrate
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:75:the $\Ph^{-2}$ shift as the unique stability clamp under a named
papers/aria-closure-kernel/paper/sections/09_limitations.tex:83:$\Rsixhundred$ and the continuum kernel
papers/aria-closure-kernel/paper/sections/09_limitations.tex:84:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:99:$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
papers/aria-closure-kernel/paper/sections/09_limitations.tex:158:\item Selection theorem identifying $\Rsixhundred$ over alternative
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:17:$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
papers/aria-closure-kernel/paper/sections/03_substrate.tex:26:\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
papers/aria-closure-kernel/paper/sections/03_substrate.tex:27:  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:28:  $\Ph^{2} = \Ph + 1$ identity, equivalently
papers/aria-closure-kernel/paper/sections/03_substrate.tex:29:  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:45:For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:50:The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:56:$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:61:The graph $G_{V_{600}}$ has:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:88:\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:89:       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:113:is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:116:inner product exactly $\Ph/2$ within machine precision (tolerance
papers/aria-closure-kernel/paper/sections/03_substrate.tex:122:\item \textbf{Fixed by the construction once $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:131:  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\qquad \Ph \;=\; (1+\sqrt 5)/2,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:24:$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
papers/aria-closure-kernel/paper/sections/01_introduction.tex:25:non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
papers/aria-closure-kernel/paper/sections/01_introduction.tex:26:positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:32:Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:36:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
papers/aria-closure-kernel/paper/sections/01_introduction.tex:39:short edges $\langle v, w\rangle = \Ph/2$. The choice of this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:46:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:60:  Once $\Rsixhundred$ is selected and the stability shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:61:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:69:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:76:  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  $\Ph$-arithmetic edge weights via shell-grade exponents
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:102:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:  $\Ph^{-2}$ is a design-level stability clamp that bounds
papers/aria-closure-kernel/paper/sections/01_introduction.tex:104:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:107:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:110:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:132:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:163:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:170:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:181:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:\S\ref{sec:programme_home} positions $\Cph$ as the programme home

codex
I read the kernel paper, all 10 section files, bibliography, `verify_kernel.py`, `results.json`, the closure-kernel source note, the b-anomaly README, and the aria-chess companion paper sections.

**1. Claim Audit**
- “`\|\Cph^{-1}\|=\Ph^2`” is established for the connected finite 600-cell graph and any zero-mode nonnegative self-adjoint Laplacian, but the abstract/general framing can read too broadly. Qualify `main.tex:95-96`, `sections/02_definition.tex:66-80`; `sections/10_conclusion.tex:11-13` already states the stricter version correctly.
- “Continuum projection ... `G(x)=(\Ph/2)e^{-|x|/\Ph}`” is correct on the full line, `sections/02_definition.tex:84-90`, but the hypotheses mix finite graph, bounded Dirichlet, and full-line cases imprecisely at `sections/02_definition.tex:37-46`.
- 600-cell graph facts are supported by standard construction plus the verification script: `sections/03_substrate.tex:17-36`, `60-77`, `79-101`. “Theorem-level rigorous” at `sections/03_substrate.tex:8-11` is acceptable only as a cited Coxeter fact, not as proved in-paper.
- Spectrum claim is appropriately bounded: computed numerically, algebraically recognized, not exactly derived, `sections/04_spectrum.tex:5-14`, table `28-38`.
- Discrete-to-continuum correlation claim is established numerically, `sections/05_agreement.tex:38-67`, but “two independently-defined objects” at `sections/05_agreement.tex:127-130` is too strong because both share the same chosen `\Ph^{-2}` scale.
- Must fix: b-anomaly sign convention. Equation `\Delta C_9^{eff}=A\kappa_{V600}` with positive `\kappa` implies positive shift, but prose says positive `A` gives negative `\Delta C_9`, `sections/06_passive_witness.tex:18-31`. Add a minus sign or define `\kappa` as signed.
- “Load-bearing object” is stronger than established for both empirical papers, since each uses substantial projection/dynamical machinery above `\Cph`: `main.tex:56-58`, `sections/01_introduction.tex:53-56`, `sections/07_active_witness.tex:135-137`, `sections/10_conclusion.tex:26-28`.
- Aria-chess inherited claims are within companion scope, provided the `17/18 -> 18/18 after N=20` caveat remains attached: kernel `main.tex:147-151`, companion `aria-chess main.tex:79-84`, `sections/05_results.tex:92-96`.

**2. Internal Consistency**
- Abstract/headline numerics match the body and `results.json`: `0.976`, `0.888`, `0.884`, `2.618`, spectrum, graph size.
- b-anomaly table matches the README rows: kernel `sections/06_passive_witness.tex:54-58`; source README `README.md:16-22`.
- AIC tie, Gaussian alternative, and Mode-B drift match README: kernel `sections/06_passive_witness.tex:99-118`; source README `README.md:30-33`.
- The “not historically blind” caveat is not in the b-anomaly README, which says the geometry criterion was independent of LHCb data at `README.md:28`; it is in the b-anomaly paper limitations. Cite that source directly if keeping `sections/06_passive_witness.tex:119-124`.
- `\Cph` is used in the variant table caption, `sections/05_agreement.tex:90-93`, but weighted variants are not literally the same `\Cph`; they are `(L_w+\Ph^{-2}I)^{-1}`.
- Cross-channel “~50% overshoot” at `sections/06_passive_witness.tex:75-80` matches the README, but arithmetic from `A=1.14`, factor `2.2`, observed `4.98` is closer to a factor-of-two residual.

**3. External Consistency / Numerics**
- `results.json:4-10` confirms `120` vertices, `720` edges, degree min/max/mean `12/12/12`; paper matches `sections/03_substrate.tex:63-77`.
- `results.json:15-25` confirms shell sizes `{1,12,20,12,30,12,20,12,1}`; paper matches `sections/03_substrate.tex:93-101`.
- `results.json:43-80` confirms spectrum and multiplicities `{1,4,9,16,25,36,9,16,4}`; paper matches `sections/04_spectrum.tex:28-38`.
- `results.json:81-86` confirms `\|\Cph^{-1}\|=2.6180339887`, matching `\Ph^2`; paper matches `sections/04_spectrum.tex:67-78`.
- `results.json:134-146` confirms per-vertex correlations `0.976202`, `0.888380`, `0.884364`; paper rounds correctly at `main.tex:97-99`, `sections/05_agreement.tex:99-101`.
- `results.json:132` confirms shell-mean unweighted `0.923208`; paper matches `sections/05_agreement.tex:40-44`.

**4. Operator-Witness Scope Discipline**
The paper mostly stays inside scope. The explicit exclusions are strong: `main.tex:153-166`, `sections/01_introduction.tex:99-135`, `sections/09_limitations.tex:150-176`. The main scope risk is not φ-derivation or uniqueness; it is over-describing the two empirical papers as sharing the same “load-bearing object” rather than sharing the same response primitive underneath different projections/layers.

**5. Tightness**
Suggested one-line edits:
- `sections/06_passive_witness.tex:19-21`: change to `\Delta C_9^{eff}(q^2) = -A\,\kappa_{V600}(q^2)` or explicitly define signed `\kappa`.
- `sections/05_agreement.tex:113-117`: “Two distinct criteria agree on the tested variant ranking, with the b-anomaly historical non-blind caveat.”
- `main.tex:56-58`: “The same fixed `\Cph` is then the shared response primitive used underneath two empirical works...”
- `sections/05_agreement.tex:127-130`: “separately evaluated discrete and continuum Green responses sharing the same design scale.”
- `sections/06_passive_witness.tex:78-80`: replace “~50% overshoot” with “observed amplitude is about twice the basis-corrected prediction.”

**6. Surface Issues**
- Static LaTeX check only; I did not compile because the workspace is read-only and compilation writes aux files.
- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are defined in `main.tex:14-17` and used consistently overall.
- Title uses `L` while the paper uses `L_M`; `main.tex:19-21` should say `L_M+\Ph^{-2}I` for precision.
- Old LaTeX engines may need UTF-8 handling for en dashes and “Krüger”; modern LaTeX should be fine.
- No obvious undefined macro in static scan; `\checkmark` is covered by `amssymb`.

**7. Top Three Fixes**
1. Fix the b-anomaly sign inconsistency in `sections/06_passive_witness.tex:18-31`; this is a mathematical contradiction.
2. Soften “load-bearing object / same fixed operator” language across `main.tex:56-58`, `sections/01_introduction.tex:53-56`, `sections/07_active_witness.tex:135-137`, `sections/10_conclusion.tex:26-28`.
3. Tighten operator-domain hypotheses and norm-equality wording in `sections/02_definition.tex:37-46`, `66-80`, and abstract `main.tex:95-96`.

**8. Verdict**
Publication ready: no — must-fix list above. The numerics are internally consistent, but the sign error and several over-strong scope formulations need correction before submission.
tokens used
193,748
I read the kernel paper, all 10 section files, bibliography, `verify_kernel.py`, `results.json`, the closure-kernel source note, the b-anomaly README, and the aria-chess companion paper sections.

**1. Claim Audit**
- “`\|\Cph^{-1}\|=\Ph^2`” is established for the connected finite 600-cell graph and any zero-mode nonnegative self-adjoint Laplacian, but the abstract/general framing can read too broadly. Qualify `main.tex:95-96`, `sections/02_definition.tex:66-80`; `sections/10_conclusion.tex:11-13` already states the stricter version correctly.
- “Continuum projection ... `G(x)=(\Ph/2)e^{-|x|/\Ph}`” is correct on the full line, `sections/02_definition.tex:84-90`, but the hypotheses mix finite graph, bounded Dirichlet, and full-line cases imprecisely at `sections/02_definition.tex:37-46`.
- 600-cell graph facts are supported by standard construction plus the verification script: `sections/03_substrate.tex:17-36`, `60-77`, `79-101`. “Theorem-level rigorous” at `sections/03_substrate.tex:8-11` is acceptable only as a cited Coxeter fact, not as proved in-paper.
- Spectrum claim is appropriately bounded: computed numerically, algebraically recognized, not exactly derived, `sections/04_spectrum.tex:5-14`, table `28-38`.
- Discrete-to-continuum correlation claim is established numerically, `sections/05_agreement.tex:38-67`, but “two independently-defined objects” at `sections/05_agreement.tex:127-130` is too strong because both share the same chosen `\Ph^{-2}` scale.
- Must fix: b-anomaly sign convention. Equation `\Delta C_9^{eff}=A\kappa_{V600}` with positive `\kappa` implies positive shift, but prose says positive `A` gives negative `\Delta C_9`, `sections/06_passive_witness.tex:18-31`. Add a minus sign or define `\kappa` as signed.
- “Load-bearing object” is stronger than established for both empirical papers, since each uses substantial projection/dynamical machinery above `\Cph`: `main.tex:56-58`, `sections/01_introduction.tex:53-56`, `sections/07_active_witness.tex:135-137`, `sections/10_conclusion.tex:26-28`.
- Aria-chess inherited claims are within companion scope, provided the `17/18 -> 18/18 after N=20` caveat remains attached: kernel `main.tex:147-151`, companion `aria-chess main.tex:79-84`, `sections/05_results.tex:92-96`.

**2. Internal Consistency**
- Abstract/headline numerics match the body and `results.json`: `0.976`, `0.888`, `0.884`, `2.618`, spectrum, graph size.
- b-anomaly table matches the README rows: kernel `sections/06_passive_witness.tex:54-58`; source README `README.md:16-22`.
- AIC tie, Gaussian alternative, and Mode-B drift match README: kernel `sections/06_passive_witness.tex:99-118`; source README `README.md:30-33`.
- The “not historically blind” caveat is not in the b-anomaly README, which says the geometry criterion was independent of LHCb data at `README.md:28`; it is in the b-anomaly paper limitations. Cite that source directly if keeping `sections/06_passive_witness.tex:119-124`.
- `\Cph` is used in the variant table caption, `sections/05_agreement.tex:90-93`, but weighted variants are not literally the same `\Cph`; they are `(L_w+\Ph^{-2}I)^{-1}`.
- Cross-channel “~50% overshoot” at `sections/06_passive_witness.tex:75-80` matches the README, but arithmetic from `A=1.14`, factor `2.2`, observed `4.98` is closer to a factor-of-two residual.

**3. External Consistency / Numerics**
- `results.json:4-10` confirms `120` vertices, `720` edges, degree min/max/mean `12/12/12`; paper matches `sections/03_substrate.tex:63-77`.
- `results.json:15-25` confirms shell sizes `{1,12,20,12,30,12,20,12,1}`; paper matches `sections/03_substrate.tex:93-101`.
- `results.json:43-80` confirms spectrum and multiplicities `{1,4,9,16,25,36,9,16,4}`; paper matches `sections/04_spectrum.tex:28-38`.
- `results.json:81-86` confirms `\|\Cph^{-1}\|=2.6180339887`, matching `\Ph^2`; paper matches `sections/04_spectrum.tex:67-78`.
- `results.json:134-146` confirms per-vertex correlations `0.976202`, `0.888380`, `0.884364`; paper rounds correctly at `main.tex:97-99`, `sections/05_agreement.tex:99-101`.
- `results.json:132` confirms shell-mean unweighted `0.923208`; paper matches `sections/05_agreement.tex:40-44`.

**4. Operator-Witness Scope Discipline**
The paper mostly stays inside scope. The explicit exclusions are strong: `main.tex:153-166`, `sections/01_introduction.tex:99-135`, `sections/09_limitations.tex:150-176`. The main scope risk is not φ-derivation or uniqueness; it is over-describing the two empirical papers as sharing the same “load-bearing object” rather than sharing the same response primitive underneath different projections/layers.

**5. Tightness**
Suggested one-line edits:
- `sections/06_passive_witness.tex:19-21`: change to `\Delta C_9^{eff}(q^2) = -A\,\kappa_{V600}(q^2)` or explicitly define signed `\kappa`.
- `sections/05_agreement.tex:113-117`: “Two distinct criteria agree on the tested variant ranking, with the b-anomaly historical non-blind caveat.”
- `main.tex:56-58`: “The same fixed `\Cph` is then the shared response primitive used underneath two empirical works...”
- `sections/05_agreement.tex:127-130`: “separately evaluated discrete and continuum Green responses sharing the same design scale.”
- `sections/06_passive_witness.tex:78-80`: replace “~50% overshoot” with “observed amplitude is about twice the basis-corrected prediction.”

**6. Surface Issues**
- Static LaTeX check only; I did not compile because the workspace is read-only and compilation writes aux files.
- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are defined in `main.tex:14-17` and used consistently overall.
- Title uses `L` while the paper uses `L_M`; `main.tex:19-21` should say `L_M+\Ph^{-2}I` for precision.
- Old LaTeX engines may need UTF-8 handling for en dashes and “Krüger”; modern LaTeX should be fine.
- No obvious undefined macro in static scan; `\checkmark` is covered by `amssymb`.

**7. Top Three Fixes**
1. Fix the b-anomaly sign inconsistency in `sections/06_passive_witness.tex:18-31`; this is a mathematical contradiction.
2. Soften “load-bearing object / same fixed operator” language across `main.tex:56-58`, `sections/01_introduction.tex:53-56`, `sections/07_active_witness.tex:135-137`, `sections/10_conclusion.tex:26-28`.
3. Tighten operator-domain hypotheses and norm-equality wording in `sections/02_definition.tex:37-46`, `66-80`, and abstract `main.tex:95-96`.

**8. Verdict**
Publication ready: no — must-fix list above. The numerics are internally consistent, but the sign error and several over-strong scope formulations need correction before submission.

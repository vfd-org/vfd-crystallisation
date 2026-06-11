Reading additional input from stdin...
OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019ddeb5-3d4b-7e23-ab7d-9cbf5483062b
--------
user
You are reviewing a physics/mathematical preprint in LaTeX (Round 11). Treat this like a careful journal-referee pass.

Paper path:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex

Section files (read all 10):
  papers/aria-closure-kernel/paper/sections/01_introduction.tex
  papers/aria-closure-kernel/paper/sections/02_definition.tex
  papers/aria-closure-kernel/paper/sections/03_substrate.tex
  papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  papers/aria-closure-kernel/paper/sections/05_agreement.tex
  papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  papers/aria-closure-kernel/paper/sections/09_limitations.tex
  papers/aria-closure-kernel/paper/sections/10_conclusion.tex

Bibliography:
  papers/aria-closure-kernel/paper/references.bib

Verification script and results (the paper lifts numbers from these):
  papers/aria-closure-kernel/repro/verify_kernel.py
  papers/aria-closure-kernel/repro/results.json

Companion preprints to validate inherited claims against:
  papers/aria-chess-paper/paper/main.tex
  papers/aria-chess-paper/paper/sections/05_results.tex
  papers/aria-chess-paper/paper/sections/09_limitations.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md

This paper is an OPERATOR WITNESS. Hard discipline:
- never claim phi^-2 is derived
- never claim 600-cell uniqueness
- never claim kernel uniqueness on either landing
- never claim a Lyapunov / 2I-equivariance / selection theorem
- inherit b-anomaly caveats verbatim (AIC tie + Mode-B drift)
- inherit aria-chess substrate-witness scope
- per-vertex correlation: 0.976 (unweighted) / 0.888 (phi-geom) / 0.884 (phi-arith); shell-mean 0.923 (unweighted)
- operator-norm phi^2 ~ 2.618 matches closed-form
- Laplacian spectrum: {0, 12-6phi, 12-4phi, 9, 12, 14, 4phi+8, 15, 6phi+6} multiplicities {1,4,9,16,25,36,9,16,4} sum 120

Round 10 left these issues; this round verifies they are fixed:
1. Active-witness tally now mentions P3 (N=5) and P13 (LOO/state-reset) refinements alongside P4 (N=20) -- check main.tex and sec07
2. The 0.976 framing now says 'multiplicity-weighted shell-radius correlation, not 119 independent samples' in abstract + intro + sec05
3. results.json + verify_kernel.py are now consistent (both at full precision; the script was changed to keep full precision)
4. Programme-home section trimmed: RH/YM forthcoming-artifact bullets removed; only published ACT companion remains; sec04 sigma-fix paragraph no longer references forthcoming RH

Read the file in full, then produce a structured review:
1. **Claim audit** -- cite file:line for each issue
2. **Internal consistency**
3. **External consistency / numerics**
4. **Operator-witness scope discipline**
5. **Tightness**
6. **Surface issues**
7. **Top three fixes**
8. **Verdict** -- exactly 'Publication ready: yes' or 'Publication ready: no -- must-fix list above'

Be direct. Over-claiming is worse than under-claiming. Don't pad.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll read the kernel paper, the verification artifacts, and the named companion sources first, then cross-check the Round 10 items and the hard scope constraints against exact line references.
  → Read kernel paper, sections, bibliography, and repro artifacts
  • Read companion preprints for inherited claims and caveats
  • Cross-check numerics, scope discipline, and Round 10 fixes
  • Write structured referee review with file:line citations
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/01_introduction.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/02_definition.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 249ms:
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
    20	       $\Cph = L_M + \Ph^{-2} I$:\\
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
    55	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (this is a multiplicity-weighted
    56	shell-radius correlation, since $\psi$ is shell-constant to
    57	machine precision under H$_3$-fixed source; not $119$ independent
    58	radial samples; \S\ref{sec:agreement};
    59	\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
    60	same fixed graph is then the shared response primitive used
    61	underneath two \emph{independent} empirical works: a passive-regime structural
    62	fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
    63	public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
    64	active-regime substrate witness against eighteen preregistered
    65	substrate/neuroscience correspondences plus six drug/sleep EEG
    66	signatures~\citep{SmartAriaChess2026}.
    67	
    68	\noindent\emph{Scope.}
    69	This paper presents an empirical \emph{operator witness}: a
    70	geometry-fixed response operator with operator shape held fixed
    71	across two disjoint-domain empirical landings (flavour physics
    72	and cortical neuroscience) with no kernel-shape retuning between
    73	regimes; the substrate $\Rsixhundred$ is post-hoc disclosed as
    74	the choice motivated by these landings, not selected by an
    75	independent criterion. It is \emph{not} a derivation of the
    76	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    77	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    78	selection theorem on the companion adaptive-closure-transport
    79	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    80	a model-preference claim against alternative kernels on either
    81	empirical landing (the b-anomaly AIC comparison and the aria-chess
    82	substrate-witness scope are documented in their own preprints and
    83	inherited verbatim here).
    84	
    85	\begin{abstract}
    86	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    87	a closure substrate $M$ with corresponding Laplacian $L_M$ and
    88	$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
    89	the discrete instance shared by two empirical witnesses, and
    90	document its appearance as the same fixed operator (no shape
    91	retuning) in two independent empirical
    92	works: (i)~a five-dataset structural fit of the
    93	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    94	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    95	preregistered substrate witness against substrate/neuroscience
    96	signatures plus six drug/sleep EEG
    97	signatures~\citep{SmartAriaChess2026}. We
    98	include the numerical reproduction script
    99	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
   100	from canonical generators, verifies the graph facts
   101	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
   102	Laplacian spectrum numerically matching closed-form $\mathbb{Z}[\Ph]$
   103	values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
   104	on the connected finite graph $\Rsixhundred$ where
   105	$\lambda_{\min}(L_M)=0$), and tests the discrete-to-continuum
   106	agreement at multiplicity-weighted shell-radius Pearson
   107	correlation $0.976$ for the unweighted variant (the discrete
   108	response is shell-constant to machine precision), above the two
   109	$\Ph$-cocycle weighted variants tested ($0.888$ geometric, $0.884$
   110	arithmetic). Within the three
   111	tested variants the unweighted Laplacian ranks highest on the
   112	geometry-only criterion, reproducing the qualitative ranking
   113	established separately by b-anomaly's data $\chi^{2}$ comparison
   114	(the b-anomaly preprint flags that its data was looked at first
   115	and the geometry ranking verified afterward; the agreement is
   116	criterion-independent but historically non-blind, a caveat we
   117	inherit verbatim).
   118	
   119	\noindent\emph{(i) Operator definition and properties.}
   120	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   121	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   122	$\Ph^{-2} \approx 0.382$, operator norm
   123	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   124	in one coordinate $x$ is the closed-form Green's function
   125	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   126	
   127	\noindent\emph{(ii) The 600-cell instance.}
   128	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   129	generated by three orbits ($8$~axis, $16$~half-integer,
   130	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   131	on the short-edge graph; the Laplacian has nine eigenvalue classes
   132	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   133	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   134	
   135	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   136	Multiplicity-weighted per-vertex Pearson correlation (shell-constant
   137	response, see \S\ref{sec:agreement}) between the discrete response
   138	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   139	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
   140	vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
   141	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   142	Same source vertex, same fixed shift, no parameter fitting; the
   143	correlation is invariant under choice of source up to numerical
   144	precision (multi-source sweep, \S\ref{sec:limitations}).
   145	
   146	\noindent\emph{(iv) Two independent empirical witnesses.}
   147	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   148	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   149	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   150	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   151	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   152	with one fitted dimensionless amplitude per dataset and the kernel
   153	shape held fixed. (b)~Active regime,
   154	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   155	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   156	condition-dependent self-injection coupling
   157	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   158	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   159	degree, passes $17/18$ preregistered correspondences (frozen
   160	2026-04-18) at standard methodology and $18/18$ after a documented
   161	$N\!=\!20$ deep-dive on the residual high-variance
   162	$C\!\times\!P$ interaction (P4) — alongside two further documented
   163	methodology refinements in the aria-chess set ($N\!=\!5$ for P3
   164	within its preregistered band; LOO/state-reset for the P13 chess
   165	substrate-lift, originally preregistered with $5$-fold CV; no
   166	threshold modifications) — plus $6/6$ literature-thresholded
   167	drug/sleep EEG signatures on a single deterministic seed.
   168	
   169	\noindent\emph{What we do not claim.}
   170	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   171	stability clamp making $\Cph$ strictly positive definite. We do
   172	not claim $\Rsixhundred$ is the unique substrate consistent with
   173	either empirical landing. We do not claim the operator is the
   174	unique kernel shape consistent with the b-anomaly data
   175	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   176	drift caveats are inherited verbatim) nor that the
   177	aria-chess substrate witness establishes a selection theorem on
   178	the adaptive-closure-transport 4-tuple. The structural scope of
   179	this paper is: \emph{one geometry-fixed operator on one fixed
   180	graph appears as the shared response primitive underneath two independent
   181	empirical works in two distinct regimes, with no shape retuning
   182	between them}.
   183	\end{abstract}
   184	
   185	% =====================================================================
   186	\input{sections/01_introduction.tex}
   187	\input{sections/02_definition.tex}
   188	\input{sections/03_substrate.tex}
   189	\input{sections/04_spectrum.tex}
   190	\input{sections/05_agreement.tex}
   191	\input{sections/06_passive_witness.tex}
   192	\input{sections/07_active_witness.tex}
   193	\input{sections/08_programme_home.tex}
   194	\input{sections/09_limitations.tex}
   195	\input{sections/10_conclusion.tex}
   196	% =====================================================================
   197	
   198	\section*{Reproducibility}
   199	The complete numerical verification (vertex construction,
   200	short-edge graph build, Laplacian spectrum, operator-norm bound,
   201	discrete-to-continuum correlation across three Laplacian variants)
   202	is reproducible from \texttt{repro/verify\_kernel.py} in this
   203	paper's bundle. No randomness, no fitted parameters: all numbers
   204	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   205	\S\ref{sec:agreement} are deterministic outputs of the script.
   206	The two empirical witness preprints
   207	(b-anomaly~\citep{SmartBAnomaly2026},
   208	aria-chess~\citep{SmartAriaChess2026}) carry their own
   209	reproducibility artifacts; this paper does not duplicate them.
   210	
   211	\bibliographystyle{plainnat}
   212	\bibliography{references}
   213	
   214	\end{document}

 succeeded in 251ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	A response operator on a fixed graph, with no shape parameters
     6	tuned to any dataset, that simultaneously gives (i) a structural
     7	fit consistent with the $q^{2}$ shape of the
     8	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
     9	flavour-physics datasets in their passive linear-response regime,
    10	and (ii) eighteen preregistered substrate/neuroscience
    11	correspondences plus six drug/sleep EEG signatures in the active
    12	dynamical regime of a
    13	recurrent self-model layer above the same graph, deserves a separate
    14	preprint that names the operator, gives its construction in full,
    15	and threads the relationship between the two empirical landings
    16	without inheriting either's load-bearing claims. That is what this
    17	paper does.
    18	
    19	The operator is
    20	\begin{equation}\label{eq:cphi_intro}
    21	\Cph \;=\; L_M + \Ph^{-2} I,
    22	\qquad \Ph \;=\; (1+\sqrt 5)/2,
    23	\end{equation}
    24	where $M$ is a closure substrate (graph, simplicial complex, or
    25	projected coordinate) and $L_M$ is its Laplacian. The shift
    26	$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
    27	non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
    28	positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
    29	operator-norm bound is
    30	\begin{equation}\label{eq:opnorm_intro}
    31	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
    32	\end{equation}
    33	The continuum projection in one coordinate $x$ has a closed-form
    34	Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
    35	$\Ph$ (\S\ref{sec:definition}).
    36	
    37	The discrete substrate used by the two empirical witnesses is
    38	the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
    39	generated by three standard coordinate families ($8$ axis vertices,
    40	$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
    41	short edges $\langle v, w\rangle = \Ph/2$. The choice of this
    42	polytope is post-hoc motivated by the empirical landings
    43	(\S\ref{sec:limitations}); the construction itself is theorem-level
    44	rigorous. The graph has $|E|=720$ edges, uniform degree by H$_4$
    45	transitivity (with the value $12$ from the short-edge
    46	construction), a $9$-shell H$_3$ partition
    47	$\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
    48	$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
    49	classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
    50	All of these facts are reproduced numerically by
    51	\texttt{repro/verify\_kernel.py} from the canonical generators
    52	alone — no external data input.
    53	
    54	\subsection*{What this paper claims}
    55	
    56	We claim a single \emph{operator witness}: that one geometry-fixed
    57	operator, on one fixed graph, with no shape-parameter retuning
    58	between regimes, appears as the shared response primitive
    59	underneath two
    60	empirical works covering qualitatively distinct physical settings.
    61	
    62	\begin{enumerate}\itemsep=2pt
    63	\item \textbf{Operator definition is fixed by the construction.}
    64	  Once $\Rsixhundred$ is selected and the stability shift
    65	  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
    66	  parameter, no fitted threshold, no learned weight enters the
    67	  operator. The Laplacian spectrum, the operator-norm bound, and
    68	  the discrete-to-continuum agreement are computed (not fitted)
    69	  from the construction and reproduced in
    70	  \texttt{repro/verify\_kernel.py}.
    71	\item \textbf{Discrete-to-continuum agreement is empirical, not
    72	  postulated.} For a localised source at any vertex, the discrete
    73	  response $\psi = \Cph^{-1} f$ is shell-constant to machine
    74	  precision, and the multiplicity-weighted per-vertex Pearson
    75	  correlation between $\psi(v)$ and $G(\|v - v_{\mathrm{src}}\|)$
    76	  is $\rho = 0.976$ on the unweighted graph Laplacian. (This is a
    77	  multiplicity-weighted shell-radius correlation, not $119$
    78	  independent radial samples; the within-shell variance is at
    79	  machine precision; see \S\ref{ssec:result_unweighted}.) It is
    80	  numerical agreement between two independently-defined objects
    81	  (a 120-dimensional discrete inverse and a continuum exponential
    82	  kernel), not a definitional identity.
    83	\item \textbf{Variant comparison among the three tested variants.}
    84	  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
    85	  $\Ph$-arithmetic edge weights via shell-grade exponents
    86	  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    87	  correlation: $0.888$ and $0.884$ respectively. Within the three
    88	  tested variants, the unweighted Laplacian ranks highest on the
    89	  geometry-only criterion. This reproduces,
    90	  on a different test, the qualitative ranking established
    91	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    92	  (\S\ref{sec:passive_witness}).
    93	\item \textbf{Two independent empirical landings, same operator.}
    94	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    95	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    96	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    97	  public datasets, with one fitted dimensionless amplitude per
    98	  dataset and the kernel held fixed; sign uniformity holds in
    99	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
   100	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
   101	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
   102	  recurrent self-model layer above the substrate, to pass eighteen
   103	  preregistered substrate/neuroscience correspondences (frozen
   104	  2026-04-18) plus six drug/sleep EEG signatures.
   105	\end{enumerate}
   106	
   107	\subsection*{What this paper does \emph{not} claim}
   108	
   109	\begin{itemize}\itemsep=2pt
   110	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
   111	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   112	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   113	  functional or a symmetry argument; we report its role as a
   114	  regularisation-of-mass scale.
   115	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   116	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   117	  highly symmetric graphs, and continuum substrates are all
   118	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   119	  is post-hoc motivated by the empirical landings; a formal
   120	  ablation against alternative substrates is an open build.
   121	\item \emph{Not a kernel-uniqueness claim on either empirical
   122	  landing.} The b-anomaly's free-width Gaussian alternative shows
   123	  that a free-width Gaussian charm-loop proxy fits the same five
   124	  datasets comparably in $\chi^{2}$ at the cost of one extra shape
   125	  parameter; the b-anomaly AIC comparison against
   126	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   127	  statistical tie on current data
   128	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   129	  Both caveats are inherited verbatim from the b-anomaly preprint.
   130	\item \emph{Not a selection theorem on the
   131	  ACT 4-tuple.} The companion adaptive-closure-transport
   132	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   133	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   134	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   135	  reduced flow, edge-space decomposition under $2I$-equivariance
   136	  (where $2I$ is the binary icosahedral group, the $\mathrm{SU}(2)$
   137	  preimage of the icosahedral symmetry of $\Rsixhundred$),
   138	  full reduced-flow convergence — is left open in that paper and
   139	  is not delivered here.
   140	\item \emph{Not a circuit-level model on the active-regime side.}
   141	  The aria-chess preprint operates at the architectural-algorithmic
   142	  level above $\Cph$. We import its empirical results verbatim and
   143	  do not relitigate them here; their substrate-witness scope
   144	  applies.
   145	\end{itemize}
   146	
   147	\subsection*{Mapping from numerics to admissible claims}
   148	
   149	To keep this paper inside the operator-witness scope, we use the
   150	same claim-boundary discipline as the aria-chess
   151	preprint~\citep{SmartAriaChess2026}: numerical results
   152	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   153	$\mathcal C_{\mathrm{admissible}}$ by the rule
   154	\[
   155	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   156	        \mathcal C_{\mathrm{admissible}},
   157	\qquad
   158	\mathcal C_{\mathrm{admissible}}
   159	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   160	\]
   161	A numerically computed quantity (the Laplacian spectrum, the
   162	operator-norm bound, the per-vertex correlation $0.976$) licenses
   163	a `computed'-type claim. Downstream empirical agreement using the
   164	fixed operator (sign uniformity in $5/5$ b-anomaly datasets, the
   165	aria-chess $17/18$ standard plus $18/18$ after the documented
   166	$N\!=\!20$ P4 deep-dive) licenses a `consistent
   167	with'-type claim. We never write
   168	`derives the kernel', `proves uniqueness', or `establishes
   169	selection'.
   170	
   171	\medskip
   172	\begin{center}
   173	\fbox{\parbox{0.92\linewidth}{\small
   174	\textbf{What is claimed / what is not.}\par
   175	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   176	600-cell graph, with computed spectrum, operator-norm bound, and
   177	discrete-to-continuum correlation; the same fixed operator appearing
   178	in two independent empirical works (b-anomaly five-dataset
   179	structural fit; aria-chess $17/18$ preregistered correspondences
   180	under the standard validation protocol and $18/18$ after the
   181	documented P4 $N\!=\!20$ deep-dive (thresholds unchanged), plus
   182	$6/6$ literature-thresholded companion EEG signatures) without
   183	shape-parameter retuning between regimes.\par
   184	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   185	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   186	landing; a selection theorem on the ACT 4-tuple; that either
   187	empirical landing settles the underlying physics (flavour anomaly
   188	or consciousness) by the operator alone.
   189	}}
   190	\end{center}
   191	
   192	\subsection*{Layout}
   193	
   194	\S\ref{sec:definition} gives the operator definition, the positivity
   195	properties of $\Cph$, the operator-norm bound, and the continuum
   196	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   197	canonical generators, gives the graph facts, and the $9$-shell
   198	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   199	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   200	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   201	across three Laplacian variants. \S\ref{sec:passive_witness} and
   202	\S\ref{sec:active_witness} thread the two independent empirical
   203	witnesses (b-anomaly and aria-chess) at the operator level.
   204	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   205	for the polynomial-in-$L$ Lyapunov family that recurs across the
   206	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   207	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 267ms:
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
    37	\item \textbf{(H3) Known spectral bottom.} On a finite graph, $M$
    38	  is connected (so the kernel of $L_M$ is exactly the constant
    39	  vector and $\lambda_{\min}(L_M) = 0$). In the continuum case,
    40	  the spectral bottom $\inf \sigma(L_M)$ is explicitly known on
    41	  the chosen domain (it equals $0$ for the full line; equals the
    42	  first Dirichlet eigenvalue $> 0$ on a bounded Dirichlet
    43	  interval). The full-line case has $\inf \sigma(L_M) = 0$ as
    44	  spectral bottom but not as an eigenvalue, which is sufficient
    45	  for the operator-norm identity in
    46	  \S\ref{ssec:opnorm}; H3 does not require a finite-dimensional
    47	  zero eigenspace.
    48	\end{itemize}
    49	
    50	Three concrete settings illustrate the hypothesis class:
    51	\begin{itemize}\itemsep=2pt
    52	\item the standard combinatorial Laplacian on a connected finite
    53	  undirected graph (the 600-cell case, $\lambda_{\min}(L_M) = 0$);
    54	\item the continuum $L = -d^{2}/dx^{2}$ on the full line with
    55	  decay-at-infinity (spectral bottom $\inf \sigma(L_M) = 0$,
    56	  not attained as an eigenvalue; used for the closed-form Green's
    57	  function in \S\ref{ssec:continuum});
    58	\item the continuum $L = -d^{2}/dx^{2}$ on a bounded interval
    59	  with Dirichlet boundary conditions ($\lambda_{\min}(L_M) > 0$).
    60	\end{itemize}
    61	Substrates outside this class — projected coordinates with
    62	non-standard boundaries, weighted Laplacians whose weight function
    63	is unbounded, or operators with negative spectrum — require their
    64	own analysis, which we do not give here.
    65	
    66	\subsection{Positive definiteness}\label{ssec:positivity}
    67	
    68	Under (H1)--(H3) on a finite connected graph, $L_M$ has a smallest
    69	eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
    70	eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
    71	\[
    72	\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
    73	                    \;=\; \Ph^{-2} \;>\; 0,
    74	\]
    75	so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
    76	well-defined and bounded.
    77	
    78	\subsection{Operator-norm bound}\label{ssec:opnorm}
    79	
    80	The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
    81	eigenvalue of $\Cph$:
    82	\begin{equation}\label{eq:opnorm}
    83	\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
    84	              \;=\; 1/(\lambda_{\min}(L_M) + \Ph^{-2}).
    85	\end{equation}
    86	On any substrate where $\lambda_{\min}(L_M) = 0$ (e.g.\ the
    87	connected finite graph $\Rsixhundred$, or the full-line continuum
    88	case used in \S\ref{ssec:continuum}), this reduces to the identity
    89	\begin{equation}\label{eq:opnorm_zero_mode}
    90	\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
    91	\end{equation}
    92	On substrates where $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet
    93	intervals), Eq.~\eqref{eq:opnorm} gives the strict inequality
    94	$\|\Cph^{-1}\| < \Ph^{2}$. The response-amplification ceiling is,
    95	in either case, $\|\psi\|_{2} \leq \|\Cph^{-1}\|\, \|f\|_{2}$. On
    96	substrates with $\lambda_{\min}(L_M) > 0$ a finite ceiling is
    97	already guaranteed by the Dirichlet structure alone; on substrates
    98	with $\lambda_{\min}(L_M) = 0$ (the cases of interest here) the
    99	shift $\Ph^{-2}$ is what guarantees a finite ceiling and pins it
   100	at $\Ph^{2}$. Numerically reproduced as $\|\Cph^{-1}\| =
   101	2.618034$ on $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
   102	\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
   103	to machine precision.
   104	
   105	\subsection{Continuum projection}\label{ssec:continuum}
   106	
   107	In one projected coordinate $x \in \mathbb{R}$ with
   108	$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
   109	$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
   110	exponential
   111	\begin{equation}\label{eq:green_continuum}
   112	G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
   113	\end{equation}
   114	The decay scale is $\Ph$ — the same constant that appears in the
   115	shift, by construction. Normalised, the kernel is
   116	$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
   117	
   118	This continuum Green's function is the comparison object for the
   119	discrete-to-continuum agreement test (\S\ref{sec:agreement}):
   120	the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
   121	chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
   122	is compared to $G(\|v - v_{\mathrm{src}}\|)$.
   123	
   124	\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
   125	
   126	The shift $\Ph^{-2}$ is chosen so that:
   127	\begin{enumerate}\itemsep=2pt
   128	\item $\Cph$ is strictly positive definite (the smallest eigenvalue
   129	  is exactly $\Ph^{-2}$);
   130	\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
   131	  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
   132	  are fixed by the single design choice $\Ph^{-2}$, giving a single
   133	  dimensional parameter throughout the operator;
   134	\item the continuum projection (Eq.~\eqref{eq:green_continuum})
   135	  has decay scale $\Ph$, not a free length parameter.
   136	\end{enumerate}
   137	We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
   138	symmetry argument. It is a design-level choice motivated by
   139	(1)--(3); we report this explicitly and treat formal derivation as
   140	an open build (\S\ref{sec:limitations}). The companion
   141	adaptive-closure-transport
   142	preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
   143	selection-layer dynamics over $W$-space that would, if delivered,
   144	constrain the shift further; that derivation is not delivered
   145	there or here.

 succeeded in 259ms:
     1	% =====================================================================
     2	\section{The 600-cell substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section gives the discrete instance used by the two empirical
     6	witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
     7	under H$_4$ Coxeter symmetry, with the standard short-edge graph
     8	Laplacian. The choice of this polytope is post-hoc motivated by
     9	the empirical landings (\S\ref{sec:limitations}); the
    10	construction itself is a classical Coxeter-group result we cite,
    11	not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
    12	this section are reproduced numerically by
    13	\texttt{repro/verify\_kernel.py} from the canonical generators
    14	alone.
    15	
    16	\subsection{Vertex set}\label{ssec:vertices}
    17	
    18	$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
    19	$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
    20	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
    21	list partitions into three standard coordinate families:
    22	\begin{itemize}\itemsep=2pt
    23	\item \textbf{Axis family} ($8$ vertices): all permutations of
    24	  $(\pm 1, 0, 0, 0)$;
    25	\item \textbf{Half-integer family} ($16$ vertices): all sign
    26	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    27	\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
    28	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
    29	  $\Ph^{2} = \Ph + 1$ identity, equivalently
    30	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
    31	\end{itemize}
    32	The total is $8 + 16 + 96 = 120$ unit vectors. These are coordinate
    33	families, not H$_4$ orbits: H$_4$ acts transitively on the full
    34	$120$-vertex set, so the three families lie in a single H$_4$
    35	orbit. Reproduced by \texttt{repro/verify\_kernel.py:build\_v600};
    36	the numerical check $\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms
    37	all vertices on $S^{3}$.
    38	
    39	The H$_4$ Coxeter group (order $14400$) acts transitively on the
    40	$120$ vertices. Every vertex therefore has \emph{identical} local
    41	structure under $H_{4}$; in particular, every vertex has the same
    42	degree in the short-edge graph defined below.
    43	
    44	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
    45	
    46	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
    47	Euclidean chord distance is
    48	\[
    49	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
    50	\]
    51	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
    52	if their inner product equals the canonical short-edge value
    53	\begin{equation}\label{eq:short_edge}
    54	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
    55	\end{equation}
    56	equivalently chord distance
    57	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
    58	nearest-neighbour adjacency on the canonical 600-cell embedding
    59	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
    60	
    61	\paragraph{Graph facts (forced by the construction).}
    62	The graph $G_{V_{600}}$ has:
    63	\begin{itemize}\itemsep=2pt
    64	\item $|V|=120$ vertices,
    65	\item $|E|=720$ edges,
    66	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
    67	  the vertex set forces \emph{uniformity} of the local structure;
    68	  the short-edge nearest-neighbour construction gives the
    69	  numerical degree $12$, verified by
    70	  \texttt{repro/verify\_kernel.py}),
    71	\item the graph is connected (verified numerically by counting
    72	  connected components of the short-edge adjacency matrix; the
    73	  classical 600-cell connectivity result is well known
    74	  in~\citep{CoxeterRegularPolytopes}).
    75	\end{itemize}
    76	All four facts are reproduced numerically:
    77	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
    78	degree-min/max $=12/12$ (uniform), and one connected component.
    79	
    80	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
    81	
    82	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
    83	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
    84	of constant inner product with $v_{0}$. The nine canonical inner
    85	products are
    86	\begin{equation}\label{eq:shell_inner}
    87	\langle v, v_{0}\rangle
    88	\;\in\;
    89	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
    90	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
    91	\end{equation}
    92	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
    93	antipode. The shell-size sequence is
    94	\begin{equation}\label{eq:shell_sizes}
    95	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
    96	\;=\;
    97	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
    98	\end{equation}
    99	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
   100	icosidodecahedral ring. The total is
   101	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
   102	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
   103	
   104	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
   105	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
   106	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
   107	
   108	\subsection{Inner-product check}\label{ssec:inner_product_check}
   109	
   110	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   111	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   112	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   113	vertex in shell $s_{2}$ if and only if their pairwise inner product
   114	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   115	adjacency types to those compatible with the H$_3$ orbit structure.
   116	The numerically constructed graph respects this: every edge has
   117	inner product exactly $\Ph/2$ within machine precision (tolerance
   118	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   119	
   120	\subsection{What the substrate fixes, and what it does not}
   121	
   122	\begin{itemize}\itemsep=2pt
   123	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   124	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   125	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   126	  Laplacian spectrum (\S\ref{sec:spectrum}).
   127	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   128	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   129	  (\S\ref{ssec:opnorm}); the operator-norm bound
   130	  $\|\Cph^{-1}\| = \Ph^{2}$.
   131	\item \textbf{Not fixed by this paper}: the choice of
   132	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
   133	  4-polytopes / Coxeter substrates. The 600-cell choice is
   134	  post-hoc motivated by the empirical landings
   135	  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
   136	  formal substrate ablation is an
   137	  open build (\S\ref{sec:limitations}).
   138	\end{itemize}

codex
I’ve read the main file and the first three sections. The headline and abstract now explicitly fence off derivation, uniqueness, and the 119-sample framing; I’m continuing through the numerics and witness sections for places where that discipline may slip.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/04_spectrum.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/06_passive_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/07_active_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 271ms:
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
    28	$0$            & machine zero ($\sim 10^{-15}$)         & $1$ \\
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
    60	remaining $26/120 = 21.7\%$ is $\sigma$-paired. We report this
    61	structural fact about the spectrum and do not use it in any claim
    62	made by this paper.
    63	
    64	\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
    65	
    66	The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
    67	\[
    68	\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
    69	\;\approx\; 0.381966,
    70	\]
    71	and the operator-norm bound is
    72	\[
    73	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
    74	\]
    75	\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
    76	$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
    77	(predicted) — match to six decimal places. The largest eigenvalue
    78	of $\Cph$ is
    79	$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
    80	= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
    81	
    82	\subsection{H$_4$ irrep block decomposition (imported context)}
    83	\label{ssec:irrep}
    84	
    85	The eigenspaces of $\Lop$ partition into H$_4$-proper and
    86	$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
    87	exponents are $\{1, 11, 19, 29\}$; under the
    88	$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
    89	$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
    90	aria-chess companion's recurrent
    91	layer~\citep{SmartAriaChess2026} realises this block decomposition
    92	at machine precision and provides a spectrally clean
    93	H$_4$-equivariant basis there.
    94	
    95	This subsection is imported context from the aria-chess companion;
    96	the irrep block decomposition is \emph{not} verified by
    97	\texttt{repro/verify\_kernel.py} of this paper and is not used as
    98	a load-bearing fact for any operator-witness claim made here. We
    99	include the labelling for orientation only.

 succeeded in 261ms:
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
    40	\item \textbf{Multiplicity-weighted per-vertex Pearson correlation
    41	  over shell-constant responses}: $\rho = 0.976$. ($\psi$ is
    42	  shell-constant to machine precision under H$_3$-fixed source, so
    43	  the per-vertex test is mathematically a multiplicity-weighted
    44	  shell-radius correlation rather than $119$ independent radial
    45	  samples; see the within-shell-variance discussion at the end of
    46	  this subsection.)
    47	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
    48	  (averaging $\psi(v)$ over each H$_3$ shell first, then
    49	  correlating the $9$-point shell-mean trajectory with the
    50	  continuum prediction at the shell mean radius).
    51	\end{itemize}
    52	The two correlations measure the same shell-radius fact at
    53	different weightings and with different source-vertex conventions:
    54	\begin{itemize}\itemsep=2pt
    55	\item Per-vertex test: $|V|-1 = 119$ data points (every
    56	  non-source vertex), source $v_{0}$ \emph{excluded} (the discrete
    57	  response there is the diagonal of $\Cph^{-1}$ and the chord
    58	  distance is $0$, both degenerate for the comparison).
    59	\item Shell-mean test: $9$ data points (one per H$_3$ shell);
    60	  shell $0$ contains only the source vertex, so it is included
    61	  on the shell-mean side and contributes a single
    62	  ($\psi(v_{0}), G(0)$) point.
    63	\end{itemize}
    64	On the unweighted 600-cell graph with an H$_3$-fixed source,
    65	$\psi$ is shell-constant up to numerical precision — the
    66	within-shell standard deviations are at machine precision
    67	($\sim 10^{-16}$). The two tests therefore differ in weighting and
    68	source convention, not in noise content: the per-vertex test
    69	weights each shell by its multiplicity
    70	($\{12, 20, 12, 30, 12, 20, 12, 1\}$ for the non-source shells)
    71	and excludes the source vertex, while the shell-mean test gives
    72	equal weight to every shell and includes the source. The
    73	per-vertex test is the headline agreement criterion in this paper.
    74	
    75	\subsection{Variant comparison}\label{ssec:variant_comparison}
    76	
    77	Two $\Ph$-cocycle weighted Laplacian variants are tested as
    78	controls:
    79	
    80	\begin{itemize}\itemsep=2pt
    81	\item \textbf{$\Ph$-geometric weights}: edge weight
    82	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
    83	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
    84	  is the shell index of $v$.
    85	\item \textbf{$\Ph$-arithmetic weights}: edge weight
    86	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
    87	  $\omega_{+}$.
    88	\end{itemize}
    89	The weighted Laplacian is then
    90	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
    91	We re-run the discrete-to-continuum test on each variant.
    92	
    93	\begin{table}[ht]
    94	\centering
    95	\small
    96	\caption{Per-vertex and shell-mean Pearson correlations between the
    97	discrete response $\psi = (L_{w} + \Ph^{-2} I)^{-1} e_{v_{0}}$
    98	and the continuum prediction $G(\|v - v_{0}\|)$ for three
    99	Laplacian variants ($L_{w}$ unweighted or $\Ph$-cocycle weighted).
   100	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
   101	\label{tab:variant_correlation}
   102	\begin{tabular}{l c c}
   103	\toprule
   104	Variant            & Per-vertex correlation & Shell-mean correlation \\
   105	\midrule
   106	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
   107	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
   108	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
   109	\bottomrule
   110	\end{tabular}
   111	\end{table}
   112	
   113	\textbf{Reading.} Among the three tested variants, the unweighted
   114	Laplacian ranks highest on both reported criteria
   115	($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
   116	This reproduces, on a different test, the qualitative ranking the
   117	b-anomaly paper~\citep{SmartBAnomaly2026} established
   118	independently against its data-$\chi^{2}$ criterion
   119	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
   120	b-anomaly numbers). Two independent criteria — geometry-only
   121	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
   122	agree on which of the three tested variants ranks highest. We do not claim
   123	this is a uniqueness or blind-selection result; we report it as a
   124	two-criterion agreement on the highest-ranked tested variant (the
   125	b-anomaly paper's own caveat that the data was looked at first
   126	and the geometry criterion verified afterward is inherited
   127	verbatim).
   128	
   129	\subsection{What the agreement does and does not establish}
   130	
   131	\paragraph{Does establish.} A geometric agreement: the discrete
   132	response of a fixed-shift Green operator on a fixed graph
   133	correlates per-vertex in radial shape, at Pearson $0.976$, with
   134	the closed-form continuum exponential at the same length scale
   135	$\Ph$. This is a non-trivial Pearson correlation between
   136	separately evaluated discrete and continuum Green responses
   137	sharing the same design-level scale $\Ph^{-2}$: (i) the discrete
   138	inverse of a $120\times 120$ Laplacian-plus-shift matrix; and
   139	(ii) a one-dimensional continuum exponential. The $\Ph$-mediated
   140	agreement is an empirical fact about the chosen substrate and
   141	shift, computed (not fitted) by the verification script.
   142	
   143	\paragraph{Does not establish.} Operator uniqueness on either
   144	empirical landing — the b-anomaly paper documents a free-width
   145	Gaussian alternative that fits comparably in $\chi^{2}$ at the
   146	cost of one extra shape parameter, and the aria-chess preprint
   147	does not run a substrate ablation; both caveats are inherited
   148	verbatim. The agreement also does not establish that
   149	$\Rsixhundred$ is the unique discrete substrate with this
   150	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   151	graphs would need to be tested on the same correlation criterion
   152	to make any comparative claim, and a formal substrate ablation is
   153	an open build (\S\ref{sec:limitations}).

 succeeded in 287ms:
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
    21	-\,A \cdot \kappa_{V_{600}}(q^{2}),
    22	\end{equation}
    23	where $\kappa_{V_{600}}(q^{2}) > 0$ on the LHCb $q^{2}$ window is
    24	the projection of $\Cph$ on $\Rsixhundred$ to the flavour-physics
    25	$q^{2}$ axis (the b-anomaly preprint's §3 projection construction,
    26	which we do not relitigate here; this is a projection of the
    27	operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
    28	fitted dimensionless amplitude per dataset. The explicit minus
    29	sign in Eq.~\eqref{eq:banomaly_kernel} reflects the b-anomaly
    30	preprint's sign convention: a positive fitted $A>0$ produces a
    31	negative $\Delta C_{9}^{\mathrm{eff}}<0$, the established
    32	direction of the angular anomaly. The kernel shape
    33	$\kappa_{V_{600}}$ is held fixed across all five datasets.
    34	This is a \emph{structural} test: same fixed $\Cph$ on the same
    35	$\Rsixhundred$, no shape retuning between datasets.
    36	
    37	\subsection{The five-dataset structural fit}
    38	
    39	The b-anomaly preprint reports the following per-dataset table
    40	(verbatim from~\citep{SmartBAnomaly2026}, also at
    41	\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
    42	
    43	\begin{table}[ht]
    44	\centering
    45	\small
    46	\caption{b-anomaly five-dataset structural fit. Verbatim
    47	from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
    48	dataset, kernel shape held fixed.}
    49	\label{tab:banomaly}
    50	\begin{tabular}{l l r r r r}
    51	\toprule
    52	Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
    53	   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
    54	\midrule
    55	LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
    56	LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
    57	CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
    58	LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
    59	LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
    60	\bottomrule
    61	\end{tabular}
    62	\end{table}
    63	
    64	\subsection{What the structural fit reports}
    65	
    66	\begin{itemize}\itemsep=2pt
    67	\item \textbf{Universality (5/5).} The same fixed kernel shape
    68	  can be fit to all five datasets with one amplitude $A$ per
    69	  dataset and no shape retuning. The kernel never moves between
    70	  datasets.
    71	\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
    72	  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
    73	  reproduces the established direction of the
    74	  anomaly~\citep{LHCbAngular2020} across all five independent
    75	  measurements.
    76	\item \textbf{Cross-channel ratio.} The b-anomaly README reports
    77	  the basis amplification (the predicted Krüger--Matias $P$-basis
    78	  vs $S$-basis factor $\sim 2.2$~\citep{KrugerMatias2005}) as
    79	  partly explanatory for the $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
    80	  amplitude gap. Working through the explicit arithmetic with
    81	  $B\to K^{*}$ best-fit $A_{P} \approx 1.14$: the basis-corrected
    82	  prediction for $B_{s}\!\to\!\phi$ is
    83	  $A_{P} \cdot 2.2 \approx 2.5$; the observed $B_{s}\!\to\!\phi$
    84	  amplitude is $A \approx 4.98$, leaving an unresolved amplitude
    85	  excess of about a factor two above the basis-corrected
    86	  prediction. The b-anomaly preprint reports this residual as an
    87	  open item, not a discharge.
    88	\item \textbf{Geometry-first variant test.} Of three discrete
    89	  Laplacian variants on $\Rsixhundred$ (unweighted,
    90	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    91	  unweighted choice ranks highest on both a pure-geometry
    92	  criterion (correlation $0.997$ with the continuum kernel under
    93	  the b-anomaly preprint's $q^{2}$/shell-projection geometry
    94	  metric, §3.4 of~\citep{SmartBAnomaly2026} — \emph{not} this
    95	  paper's per-vertex test, whose unweighted score is $0.976$;
    96	  the two metrics differ in what is correlated) and the LHCb~2025
    97	  data $\chi^{2}$ ($\chi^{2}=13.555$). The two criteria agree on
    98	  the variant ranking — a two-criterion agreement on the same
    99	  fixed operator.
   100	\end{itemize}
   101	
   102	\subsection{What the structural fit does \emph{not} establish}
   103	
   104	The b-anomaly preprint is explicit about the following caveats,
   105	which we inherit verbatim:
   106	
   107	\begin{itemize}\itemsep=2pt
   108	\item \textbf{AIC tie on current data.} On Akaike model comparison,
   109	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
   110	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
   111	  indistinguishable: stacked AIC weights
   112	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   113	  Current data cannot resolve the model comparison. AIC is blind
   114	  to the universality / shape-prediction claim itself, but it is
   115	  decisive about whether the shape is forced by data: it is not.
   116	\item \textbf{Free-width Gaussian alternative.} A free-width
   117	  Gaussian charm-loop proxy fits the same five datasets comparably
   118	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   119	  is not the unique $q^{2}$ shape consistent with the anomaly.
   120	\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
   121	  earlier analysis the b-anomaly project labels Mode-B
   122	  (linearised) gave a stronger preference
   123	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   124	  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
   125	  between Mode-B (linearised) and the non-linear refit is the
   126	  largest single methodological uncertainty in the b-anomaly
   127	  project.
   128	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   129	  preprint's limitations section~\citep{SmartBAnomaly2026}
   130	  acknowledges that the LHCb~2025 data was looked at first, and
   131	  only later was the agreement of the data-$\chi^{2}$ ranking with
   132	  the pure-geometry ranking verified. (The b-anomaly README
   133	  emphasises that the geometry-only criterion is independent of
   134	  the LHCb data; the historical non-blindness is in the project's
   135	  ordering, not in the criterion.) The two-criterion agreement is
   136	  criterion-independent but not historically blind.
   137	\end{itemize}
   138	
   139	\subsection{Reading at the operator level}
   140	
   141	The b-anomaly result is the \emph{passive-regime} empirical
   142	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   143	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   144	fixed discrete-to-momentum projection, gives a sign-uniform
   145	structural fit consistent with the $b\to s\mu^{+}\mu^{-}$ angular
   146	anomaly across five independent measurements without shape
   147	retuning. This does
   148	not establish the kernel as theorem-grade physics on the flavour
   149	side (the AIC tie, the free-width Gaussian alternative, and the
   150	Mode-B linearised-to-non-linear refit drift prevent that). It
   151	does support, at the operator-witness level, the inherited reading
   152	that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
   153	consistent with one of two independent empirical landings without
   154	parameter retuning. The
   155	second landing is in \S\ref{sec:active_witness}.

 succeeded in 278ms:
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
    57	interaction term), \emph{not} as a threshold change. Two further
    58	predictions in the aria-chess set carry their own documented
    59	methodology refinements that we also inherit: P3
    60	($D\!\times\!C$ independence) closes at $N\!=\!5$ within
    61	its preregistered band, and P13 (chess substrate lift) was
    62	preregistered with $5$-fold cross-validation but the
    63	landed value $+40.6$pp uses the documented leave-one-out /
    64	state-reset protocol; both refinements are reported
    65	in~\citep{SmartAriaChess2026} with no threshold modification, and
    66	we inherit those caveats verbatim.
    67	
    68	\subsection{Six drug/sleep EEG signatures}
    69	
    70	On a single deterministic substrate trajectory at seed~$42$, the
    71	aria-chess preprint reports six biological signatures testing
    72	against literature-derived thresholds:
    73	
    74	\begin{itemize}\itemsep=2pt
    75	\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
    76	  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
    77	  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
    78	  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
    79	  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
    80	  intervals do not overlap each other; the WAKE interval is the
    81	  pairwise common ground).
    82	\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
    83	  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
    84	\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
    85	  wake (threshold $\in [1.5, 5.0]$, empirical reference
    86	  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
    87	\item \textbf{Propofol continuity drop}: $+0.066$
    88	  (threshold $> 0.020$).
    89	\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
    90	  direction confirmed; $\Phi$-proxy not full IIT).
    91	\item \textbf{Recovery deterministic identity to wake}: under the
    92	  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
    93	  to the WAKE trajectory.
    94	\end{itemize}
    95	
    96	\subsection{Cross-domain selectivity}
    97	
    98	\begin{itemize}\itemsep=2pt
    99	\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
   100	  positions across $4$ categories on $8$-D V2 features; under the
   101	  disclosed leave-one-out / state-reset refinement of the
   102	  preregistered $\geq +15$pp substrate-lift test (the original
   103	  prereg used $5$-fold cross-validation; the LOO/state-reset
   104	  protocol is documented in the aria-chess
   105	  preprint~\citep{SmartAriaChess2026}), substrate routing lifts
   106	  classification at canonical depth $n=25$ ticks from raw
   107	  $53.1\%$ to substrate-routed $93.8\%$ ($+40.6$pp), above the
   108	  preregistered $\geq +15$pp floor.
   109	\item \textbf{Conversation pattern recognition (P14--P16)}:
   110	  $64$ utterances, $8$ categories; raw classification $87.5\%$,
   111	  substrate-routed lift $-4.4$pp (within the preregistered
   112	  neutrality band $|\cdot| < 10$pp). The substrate is selectively
   113	  amplifying in tasks where raw features are ambiguous and
   114	  approximately neutral when raw features are already
   115	  discriminative.
   116	\item \textbf{HCP brain functional connectivity (P17--P18)}:
   117	  full-cohort descriptive statistics on $n=1003$ subjects show
   118	  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
   119	  homogeneity, $+79.78\sigma$ on raw participation ratio (with
   120	  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
   121	  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
   122	  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
   123	  deviations below the HCP biological cohort.
   124	\end{itemize}
   125	
   126	\subsection{Reading at the operator level}
   127	
   128	The aria-chess result is the \emph{active-regime} empirical
   129	witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
   130	layer above $\Cph$ uses one condition-dependent coupling and one
   131	substrate-pinned nonlinearity at the graph's average degree
   132	$k=12$; no other \emph{kernel-shape} parameter enters. Above the
   133	operator, aria-chess inherits its own dynamical and stimulus
   134	constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
   135	condition-specific biologically-motivated stimulus models); these
   136	are documented in the aria-chess preprint and are not retuned in
   137	this paper. The kernel shift $\Ph^{-2}$ is not retuned between
   138	b-anomaly and aria-chess. Under those design choices, the same
   139	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with the
   140	aria-chess active-regime tally (frozen 2026-04-18): $17/18$
   141	preregistered cortical correspondences under the standard
   142	validation protocol, $18/18$ after the documented $N\!=\!20$ P4
   143	deep-dive (thresholds unchanged), plus six literature-thresholded
   144	EEG drug/sleep signatures.
   145	
   146	The aria-chess preprint stays inside substrate-witness scope: it
   147	does not claim the substrate \emph{is} consciousness, does not
   148	claim 600-cell uniqueness among regular 4-polytopes, and does not
   149	deliver a selection theorem on the ACT 4-tuple. We inherit the
   150	scope verbatim. What we add at the operator level is the
   151	observation that the same fixed $\Cph$ — under no shape-parameter
   152	retuning between regimes — is the shared response primitive
   153	underneath both empirical landings (the b-anomaly $q^{2}$
   154	projection above $\Cph$ and the aria-chess recurrent self-model
   155	layer above $\Cph$ are distinct above-operator constructions; the
   156	operator below them is the same).
   157	
   158	\subsection{Two-witness structure}
   159	
   160	\begin{table}[ht]
   161	\centering
   162	\small
   163	\caption{Two independent empirical landings of $\Cph$ on
   164	$\Rsixhundred$, with no shape retuning between regimes.}
   165	\label{tab:two_witness}
   166	\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
   167	\toprule
   168	& Passive regime & Active regime \\
   169	\midrule
   170	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   171	Domain             & flavour physics                    & cortical neuroscience \\
   172	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   173	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   174	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   175	Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
   176	Headline           & $5/5$ sign uniformity              & $17/18$ standard, $18/18$ after P4 deep-dive; $6/6$ EEG \\
   177	Kernel-shape free params & 0                            & 0 \\
   178	Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
   179	Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
   180	\bottomrule
   181	\end{tabular}
   182	\end{table}
   183	
   184	The two witnesses share, by design, exactly the geometry-fixed
   185	operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
   186	the same shift $\Ph^{-2}$. They share no fitted parameter,
   187	threshold, dataset, or methodological choice above the operator
   188	level. The b-anomaly amplitude $A$ is fitted to flavour-physics
   189	$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
   190	is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
   191	neural data; the v4 stimulus protocols are biologically motivated,
   192	not subject-fit. Independence in this paper is independence at
   193	the empirical layer above the shared operator.

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/08_programme_home.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 302ms:
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
    12	\subsection{Programme position}
    13	
    14	$\Cph$ is one instance of a polynomial-in-$L$ functional on a
    15	finite-dimensional substrate. The published companion adaptive-
    16	closure-transport
    17	preprint~\citep{SmartAdaptiveClosureTransport2026} positions a
    18	homeostatic regulariser $R_{\mathrm{hom}}$ in the 4-tuple
    19	$(M, L_M, W, R_{\mathrm{hom}})$ as a member of the same
    20	polynomial-in-$L$ family. We use this as the only published
    21	programme-level reference point for $\Cph$. We make no
    22	classification claim, no family-membership theorem, and no
    23	forecast about other forthcoming members of this programme; any
    24	broader programme arc lies outside the operator-witness scope of
    25	this paper.
    26	
    27	\subsection{Response vs selection}
    28	
    29	The closure response $\psi = \Cph^{-1} f$ is determined by the
    30	chosen substrate plus the design-level shift: $\Cph$ is fixed by
    31	the substrate $\Rsixhundred$ and the design-level choice
    32	$\Ph^{-2}$, and the response is the resulting linear inverse.
    33	This is a \emph{response} primitive. It does \emph{not} answer:
    34	\begin{itemize}\itemsep=2pt
    35	\item Why this substrate? (Selection across regular 4-polytopes
    36	  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
    37	\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
    38	  positive constant.)
    39	\item How does the system pick a response configuration over
    40	  time? (Crystallisation / Lyapunov descent dynamics on a
    41	  $W$-trajectory.)
    42	\end{itemize}
    43	
    44	The selection layer is open. The companion adaptive-closure-
    45	transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    46	proposes a Lyapunov $V(W)$ on the reduced flow, an edge-space
    47	decomposition under the $2I$ binary-icosahedral symmetry of
    48	$\Rsixhundred$, and a full reduced-flow convergence theorem on
    49	$W$-trajectories; that paper explicitly does \emph{not} deliver
    50	those, and we do not deliver them here. The aria-chess
    51	companion~\citep{SmartAriaChess2026} likewise stays inside
    52	substrate-witness scope and does \emph{not} deliver a selection
    53	theorem. The two empirical witnesses landed in this paper provide
    54	external consistency checks on the \emph{response} primitive
    55	without reducing or addressing the selection gap.
    56	
    57	\subsection{What this paper closes vs leaves open}
    58	
    59	\paragraph{Closes (at the operator-witness level).}
    60	\begin{itemize}\itemsep=2pt
    61	\item The operator $\Cph$ is well-defined and positive definite
    62	  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
    63	  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
    64	  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
    65	  with the standard combinatorial Laplacian). On substrates where
    66	  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
    67	  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
    68	  generally strict (\S\ref{sec:definition}).
    69	\item The 600-cell instance $\Rsixhundred$ has the construction
    70	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
    71	  Table~\ref{tab:spectrum}, both reproduced numerically
    72	  (\texttt{repro/verify\_kernel.py}).
    73	\item Discrete-to-continuum agreement at per-vertex Pearson
    74	  correlation $0.976$ on the unweighted variant, with the unweighted
    75	  variant winning the geometry-only criterion against two
    76	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
    77	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
    78	  the shared response primitive underneath two independent empirical works in
    79	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
    80	  \S\ref{sec:active_witness}).
    81	\end{itemize}
    82	
    83	\paragraph{Leaves open.}
    84	\begin{itemize}\itemsep=2pt
    85	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
    86	  as a design-level shift; not derived from a closure functional
    87	  or symmetry argument.
    88	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
    89	  post-hoc motivated by the empirical landings; alternative regular
    90	  4-polytopes are an explicit ablation build, not a discharged
    91	  comparison.
    92	\item \emph{Kernel-uniqueness on either empirical landing.} The
    93	  b-anomaly free-width Gaussian alternative (fits comparably with
    94	  one extra shape parameter) and the AIC tie
    95	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
    96	  inherited verbatim from~\citep{SmartBAnomaly2026}.
    97	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
    98	  decomposition under $2I$-equivariance, full reduced-flow
    99	  convergence — all explicitly not delivered
   100	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   101	  here.
   102	\item \emph{Family-membership theorem.} The programme-home
   103	  positioning of cascade Lyapunov functionals as members of the
   104	  same polynomial-in-$L$ family is reported as
   105	  \emph{programme-positioned}, not formally classified.
   106	\end{itemize}

 succeeded in 292ms:
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
    58	data-$\chi^{2}$ ranking. The two-criterion agreement is
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
    75	or justify a distinguished shift under a named criterion (e.g.\
    76	minimum-amplitude amplification on a specified function class);
    77	uniqueness is not assumed and is itself an open problem.
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

 succeeded in 322ms:
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
    28	retuning between regimes, appears as the shared response
    29	primitive underneath:
    30	\begin{enumerate}\itemsep=2pt
    31	\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
    32	  fitted dimensionless amplitude $A$ per dataset (kernel shape
    33	  held fixed) gives a sign-uniform
    34	  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
    35	  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
    36	  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
    37	  $B_s\to\phi$).
    38	\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
    39	  recurrent self-model layer above the same operator (one
    40	  condition-dependent self-injection coupling
    41	  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
    42	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    43	  degree) is consistent with the aria-chess active-regime tally
    44	  (frozen 2026-04-18): $17/18$ preregistered
    45	  substrate/neuroscience correspondences under the standard
    46	  validation protocol, $18/18$ after the documented $N\!=\!20$
    47	  P4 deep-dive (thresholds unchanged), plus six
    48	  literature-thresholded drug/sleep EEG signatures.
    49	\end{enumerate}
    50	By design, the two witnesses share exactly the geometry-fixed
    51	operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
    52	$\Ph^{-2}$. Above that operator level, they share no fitted
    53	parameter, threshold, or dataset, and the empirical claims are
    54	tested on disjoint physical domains (flavour physics vs cortical
    55	neuroscience). Independence here is
    56	independence at the empirical layer above the shared operator,
    57	not statistical independence of the operator itself.
    58	
    59	\textbf{Operator-witness scope.} This is an operator witness, not
    60	a derivation of physics on either landing. We do not derive the
    61	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
    62	claim 600-cell uniqueness; alternative regular 4-polytopes are an
    63	explicit ablation build. We do not claim kernel uniqueness on
    64	either empirical landing; the b-anomaly's free-width Gaussian
    65	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
    66	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
    67	aria-chess substrate-witness scope is inherited verbatim. We do
    68	not deliver a selection theorem on the ACT
    69	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
    70	open builds (Lyapunov $V(W)$, edge-space decomposition under
    71	$2I$-equivariance, full reduced-flow convergence) remain open and
    72	are not delivered here.
    73	
    74	\textbf{Programme position.} \S\ref{sec:programme_home} positions
    75	$\Cph$ within a broader programme-level family of
    76	polynomial-in-$L$ functionals (with the schematic family members
    77	named there as non-load-bearing future-programme context, not
    78	established here). Family-membership is
    79	\emph{programme-positioned}, not formally classified. The two
    80	empirical landings provide external consistency checks on the
    81	\emph{response} primitive without reducing or addressing the
    82	selection gap.
    83	
    84	The empirical material gathered here is the operator witness; the
    85	broader programme to convert the witness into a selection-theorem-
    86	grade claim is sketched in the companion preprints and remains
    87	the natural next step.

 succeeded in 329ms:
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

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/verify_kernel.py' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"round|P3|P13|119|independent|forthcoming|RH|Yang|Lyapunov|2I|selection theorem|unique|uniqueness|derived|derive|Mode-B|AIC|0\\.976|0\\.976202|0\\.888|0\\.884|0\\.923|0\\.997|sigma|σ|forthcoming-artifact\" papers/aria-closure-kernel/paper papers/aria-closure-kernel/repro" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 218ms:
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
    45	      "eigenvalue": -1.01103545984405e-15,
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

 succeeded in 229ms:
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
   130	    """Group eigenvalues into multiplicity classes (within numerical tol).
   131	
   132	    Eigenvalues stored at full precision; ``decimals`` only sets the
   133	    grouping tolerance.
   134	    """
   135	    classes = []
   136	    seen = []
   137	    for val in w:
   138	        placed = False
   139	        for idx, ref in enumerate(seen):
   140	            if abs(val - ref) < 10 ** (-decimals):
   141	                classes[idx] = (ref, classes[idx][1] + 1)
   142	                placed = True
   143	                break
   144	        if not placed:
   145	            seen.append(val)
   146	            classes.append((float(val), 1))
   147	    return classes
   148	
   149	
   150	# ---------------------------------------------------------------------------
   151	# 4. Closure operator and discrete Green's function
   152	# ---------------------------------------------------------------------------
   153	
   154	def build_C_phi(L):
   155	    """C_phi = L + phi^-2 I."""
   156	    return L + INV_PHI2 * np.eye(L.shape[0])
   157	
   158	
   159	def green_response(C_phi, source_idx):
   160	    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
   161	    n = C_phi.shape[0]
   162	    f = np.zeros(n)
   163	    f[source_idx] = 1.0
   164	    psi = np.linalg.solve(C_phi, f)
   165	    return psi
   166	
   167	
   168	# ---------------------------------------------------------------------------
   169	# 5. Shell decomposition (9-shell H_3 partition)
   170	# ---------------------------------------------------------------------------
   171	
   172	def shell_indices(V, pole_idx):
   173	    """
   174	    Group vertices by their inner product with V[pole_idx]. The 600-cell's
   175	    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
   176	    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
   177	    """
   178	    pole = V[pole_idx]
   179	    inner = V @ pole
   180	    # The 9 canonical inner-product values:
   181	    canonical = np.array([
   182	        1.0,                # shell 0: pole itself
   183	        PHI / 2.0,          # shell 1
   184	        0.5,                # shell 2
   185	        1.0 / (2.0 * PHI),  # shell 3
   186	        0.0,                # shell 4 (equator)
   187	        -1.0 / (2.0 * PHI), # shell 5
   188	        -0.5,               # shell 6
   189	        -PHI / 2.0,         # shell 7
   190	        -1.0,               # shell 8: antipode
   191	    ])
   192	    shells = {k: [] for k in range(9)}
   193	    for i, val in enumerate(inner):
   194	        # snap to nearest canonical
   195	        k = int(np.argmin(np.abs(canonical - val)))
   196	        shells[k].append(i)
   197	    sizes = {k: len(shells[k]) for k in shells}
   198	    return shells, sizes, canonical
   199	
   200	
   201	# ---------------------------------------------------------------------------
   202	# 6. Discrete <-> continuum agreement test
   203	# ---------------------------------------------------------------------------
   204	
   205	def discrete_continuum_test(V, C_phi, source_idx):
   206	    """
   207	    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
   208	    shell radial coordinate x is the chord distance |v - v_source|. The
   209	    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).
   210	
   211	    Returns the per-shell discrete mean, the continuum prediction at each
   212	    shell radius, and the Pearson correlation between them.
   213	    """
   214	    psi = green_response(C_phi, source_idx)
   215	    shells, sizes, _ = shell_indices(V, source_idx)
   216	    pole = V[source_idx]
   217	
   218	    shell_means = []
   219	    shell_radii = []
   220	    shell_count = []
   221	    for k in range(9):
   222	        idxs = shells[k]
   223	        if not idxs:
   224	            continue
   225	        mean_psi = float(np.mean(psi[idxs]))
   226	        # mean chord radius from pole
   227	        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
   228	        shell_means.append(mean_psi)
   229	        shell_radii.append(chord)
   230	        shell_count.append(len(idxs))
   231	
   232	    shell_means = np.array(shell_means)
   233	    shell_radii = np.array(shell_radii)
   234	    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)
   235	
   236	    # Pearson correlation of (discrete shell mean) with (continuum prediction)
   237	    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
   238	        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
   239	    else:
   240	        corr = float("nan")
   241	
   242	    return {
   243	        "shell_radii": shell_radii.tolist(),
   244	        "shell_count": shell_count,
   245	        "shell_psi_mean": shell_means.tolist(),
   246	        "continuum_prediction": continuum.tolist(),
   247	        "pearson_correlation": corr,
   248	    }
   249	
   250	
   251	# ---------------------------------------------------------------------------
   252	# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
   253	# ---------------------------------------------------------------------------
   254	
   255	def cocycle_weights(V, source_idx):
   256	    """
   257	    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
   258	    the shell index of v with respect to a chosen pole. For the variant
   259	    test we compare the unweighted graph Laplacian to two weighted variants
   260	    discussed in the b-anomaly paper.
   261	    """
   262	    shells, _, _ = shell_indices(V, source_idx)
   263	    kappa = np.zeros(V.shape[0])
   264	    for k, idxs in shells.items():
   265	        for i in idxs:
   266	            kappa[i] = float(k)
   267	    return PHI ** kappa
   268	
   269	
   270	def weighted_laplacian(A, weights, mode="geometric"):
   271	    """
   272	    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
   273	    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
   274	    """
   275	    n = A.shape[0]
   276	    if mode == "geometric":
   277	        W = np.sqrt(np.outer(weights, weights))
   278	    elif mode == "arithmetic":
   279	        W = 0.5 * (weights[:, None] + weights[None, :])
   280	    else:
   281	        raise ValueError(mode)
   282	    A_w = A * W
   283	    D_w = np.diag(A_w.sum(axis=1))
   284	    return D_w - A_w
   285	
   286	
   287	def variant_correlation(V, A, source_idx, variant):
   288	    if variant == "UNWEIGHTED":
   289	        L_v = np.diag(A.sum(axis=1)) - A
   290	    else:
   291	        weights = cocycle_weights(V, source_idx)
   292	        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
   293	        L_v = weighted_laplacian(A, weights, mode=mode)
   294	    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
   295	    test = discrete_continuum_test(V, C_v, source_idx)
   296	    psi = green_response(C_v, source_idx)
   297	    pole = V[source_idx]
   298	    chord = np.linalg.norm(V - pole, axis=1)
   299	    # Continuum kernel at each vertex's chord radius
   300	    cont = (PHI / 2.0) * np.exp(-chord / PHI)
   301	    # Per-vertex correlation (excluding the source itself, which is degenerate)
   302	    mask = np.arange(V.shape[0]) != source_idx
   303	    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
   304	        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   305	    else:
   306	        per_vertex_corr = float("nan")
   307	    return {
   308	        "shell_mean_correlation": test["pearson_correlation"],
   309	        "per_vertex_correlation": per_vertex_corr,
   310	        "test": test,
   311	    }
   312	
   313	
   314	# ---------------------------------------------------------------------------
   315	# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
   316	# ---------------------------------------------------------------------------
   317	
   318	def connectivity_check(A):
   319	    """
   320	    Numerical connectedness verification: count connected components of the
   321	    short-edge adjacency matrix. Connectedness is reported, not derived from
   322	    a structural argument.
   323	    """
   324	    n_components, _ = connected_components(csr_matrix(A), directed=False)
   325	    return {
   326	        "n_connected_components": int(n_components),
   327	        "connected": bool(n_components == 1),
   328	    }
   329	
   330	
   331	def multi_source_sweep(V, C_phi):
   332	    """
   333	    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
   334	    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
   335	    predicts the correlation is invariant under choice of source vertex; this
   336	    function verifies the prediction numerically across all 120 sources and
   337	    reports the min/mean/max envelope.
   338	    """
   339	    n = V.shape[0]
   340	    corrs = np.zeros(n)
   341	    for source_idx in range(n):
   342	        psi = green_response(C_phi, source_idx)
   343	        chord = np.linalg.norm(V - V[source_idx], axis=1)
   344	        cont = (PHI / 2.0) * np.exp(-chord / PHI)
   345	        mask = np.arange(n) != source_idx
   346	        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   347	    return {
   348	        "n_sources": int(n),
   349	        "min_correlation": float(corrs.min()),
   350	        "mean_correlation": float(corrs.mean()),
   351	        "max_correlation": float(corrs.max()),
   352	        "max_minus_min": float(corrs.max() - corrs.min()),
   353	    }
   354	
   355	
   356	def operator_norm_check(L, w):
   357	    lam_min_L = float(w[0])           # 0
   358	    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
   359	    op_norm = 1.0 / lam_min_C         # phi^2
   360	    return {
   361	        "lambda_min_L": lam_min_L,
   362	        "lambda_min_C_phi": lam_min_C,
   363	        "operator_norm_C_phi_inv": op_norm,
   364	        "predicted_phi_squared": PHI ** 2,
   365	    }
   366	
   367	
   368	# ---------------------------------------------------------------------------
   369	# 9. Run everything and write results.json
   370	# ---------------------------------------------------------------------------
   371	
   372	def main():
   373	    out_path = Path(__file__).parent / "results.json"
   374	
   375	    V = build_v600()
   376	    n = V.shape[0]
   377	    A = build_short_edge_graph(V)
   378	    deg = A.sum(axis=1)
   379	    n_edges = int(A.sum() // 2)
   380	
   381	    L, w, U = laplacian_spectrum(A)
   382	    spectrum = round_spectrum(w, decimals=4)
   383	
   384	    C_phi = build_C_phi(L)
   385	    op_norm = operator_norm_check(L, w)
   386	    connectivity = connectivity_check(A)
   387	    multi_source = multi_source_sweep(V, C_phi)
   388	
   389	    # Pick the +x_0 axis vertex as canonical pole/source.
   390	    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
   391	    pole = V[pole_idx]
   392	
   393	    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)
   394	
   395	    test = discrete_continuum_test(V, C_phi, pole_idx)
   396	
   397	    # Variant comparison on the same source
   398	    variants = {}
   399	    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   400	        out = variant_correlation(V, A, pole_idx, variant)
   401	        variants[variant] = {
   402	            "shell_mean_correlation": out["shell_mean_correlation"],
   403	            "per_vertex_correlation": out["per_vertex_correlation"],
   404	        }
   405	
   406	    result = {
   407	        "phi": PHI,
   408	        "phi_inv_sq": INV_PHI2,
   409	        "n_vertices": n,
   410	        "n_edges": n_edges,
   411	        "degree_sequence": {
   412	            "min": int(deg.min()),
   413	            "max": int(deg.max()),
   414	            "mean": float(deg.mean()),
   415	        },
   416	        "connectivity": connectivity,
   417	        "shell_sizes": shell_sizes,
   418	        "shell_inner_products": canonical_inner.tolist(),
   419	        "antipodal_check": {
   420	            "pole_idx": pole_idx,
   421	            "antipode_idx": int(np.argmin(V @ pole)),
   422	            "expected_shell_8_size": 1,
   423	            "observed_shell_8_size": shell_sizes.get(8, 0),
   424	        },
   425	        "laplacian_spectrum_grouped": [
   426	            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
   427	        ],
   428	        "operator_norm": op_norm,
   429	        "discrete_continuum_test": test,
   430	        "variant_correlation": variants,
   431	        "multi_source_sweep": multi_source,
   432	    }
   433	
   434	    with open(out_path, "w") as f:
   435	        json.dump(result, f, indent=2)
   436	
   437	    # Headline summary
   438	    print("=" * 60)
   439	    print("ARIA Closure Kernel — verification")
   440	    print("=" * 60)
   441	    print(f"|V|           = {n}  (expected 120)")
   442	    print(f"|E|           = {n_edges}  (expected 720)")
   443	    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
   444	    print(f"connected      = {connectivity['connected']}  "
   445	          f"(components = {connectivity['n_connected_components']})")
   446	    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
   447	    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
   448	    print()
   449	    print("Laplacian spectrum (eigenvalue, multiplicity):")
   450	    for ev, m in spectrum:
   451	        print(f"  {ev:>8.4f}   x {m}")
   452	    print()
   453	    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
   454	    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
   455	    print()
   456	    print("Discrete <-> continuum agreement (Pearson correlation):")
   457	    print(f"  variant         | shell-mean  | per-vertex")
   458	    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   459	        sm = variants[v]["shell_mean_correlation"]
   460	        pv = variants[v]["per_vertex_correlation"]
   461	        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
   462	    print()
   463	    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
   464	    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
   465	    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
   466	    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
   467	    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
   468	    print()
   469	    print(f"Wrote {out_path}")
   470	
   471	
   472	if __name__ == "__main__":
   473	    main()

 succeeded in 212ms:
  473 papers/aria-closure-kernel/repro/verify_kernel.py
  154 papers/aria-closure-kernel/repro/results.json
  627 total

 succeeded in 316ms:
papers/aria-closure-kernel/repro/README.md:35:   - **0.976** (unweighted Laplacian — wins)
papers/aria-closure-kernel/repro/README.md:36:   - 0.888 (φ-geometric weights)
papers/aria-closure-kernel/repro/README.md:37:   - 0.884 (φ-arithmetic weights)
papers/aria-closure-kernel/repro/verify_kernel.py:129:def round_spectrum(w, decimals=6):
papers/aria-closure-kernel/repro/verify_kernel.py:321:    short-edge adjacency matrix. Connectedness is reported, not derived from
papers/aria-closure-kernel/repro/verify_kernel.py:382:    spectrum = round_spectrum(w, decimals=4)
papers/aria-closure-kernel/paper/references.bib:22:  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
papers/aria-closure-kernel/paper/README.md:4:600-cell graph $V_{600}$, threading two independent empirical witnesses
papers/aria-closure-kernel/paper/README.md:41:sections/08_programme_home.tex        polynomial-in-L Lyapunov family + open selection layer
papers/aria-closure-kernel/paper/README.md:50:- a uniqueness claim for the 600-cell among regular 4-polytopes,
papers/aria-closure-kernel/paper/README.md:51:- a selection theorem on the ACT 4-tuple,
papers/aria-closure-kernel/paper/README.md:52:- a kernel-uniqueness claim on either empirical landing
papers/aria-closure-kernel/paper/README.md:53:  (b-anomaly Mode-B and AIC-tie caveats inherited verbatim;
papers/aria-closure-kernel/paper/main.tex:22:       independent empirical witnesses}
papers/aria-closure-kernel/paper/main.tex:53:agreement at per-vertex Pearson correlation $0.976$ between the
papers/aria-closure-kernel/paper/main.tex:57:machine precision under H$_3$-fixed source; not $119$ independent
papers/aria-closure-kernel/paper/main.tex:61:underneath two \emph{independent} empirical works: a passive-regime structural
papers/aria-closure-kernel/paper/main.tex:75:independent criterion. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:76:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:78:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:81:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:91:retuning) in two independent empirical
papers/aria-closure-kernel/paper/main.tex:107:correlation $0.976$ for the unweighted variant (the discrete
papers/aria-closure-kernel/paper/main.tex:109:$\Ph$-cocycle weighted variants tested ($0.888$ geometric, $0.884$
papers/aria-closure-kernel/paper/main.tex:116:criterion-independent but historically non-blind, a caveat we
papers/aria-closure-kernel/paper/main.tex:140:vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
papers/aria-closure-kernel/paper/main.tex:141:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:146:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:163:methodology refinements in the aria-chess set ($N\!=\!5$ for P3
papers/aria-closure-kernel/paper/main.tex:164:within its preregistered band; LOO/state-reset for the P13 chess
papers/aria-closure-kernel/paper/main.tex:170:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:172:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:174:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:175:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:177:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:180:graph appears as the shared response primitive underneath two independent
papers/aria-closure-kernel/repro/results.json:38:    "pole_idx": 119,
papers/aria-closure-kernel/repro/results.json:132:    "pearson_correlation": 0.9232082699765517
papers/aria-closure-kernel/repro/results.json:136:      "shell_mean_correlation": 0.9232082699765517,
papers/aria-closure-kernel/repro/results.json:137:      "per_vertex_correlation": 0.9762022978516623
papers/aria-closure-kernel/repro/results.json:141:      "per_vertex_correlation": 0.8883800503732451
papers/aria-closure-kernel/repro/results.json:145:      "per_vertex_correlation": 0.8843640031310793
papers/aria-closure-kernel/repro/results.json:150:    "min_correlation": 0.9762022978516617,
papers/aria-closure-kernel/repro/results.json:151:    "mean_correlation": 0.9762022978516628,
papers/aria-closure-kernel/repro/results.json:152:    "max_correlation": 0.9762022978516637,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:  over shell-constant responses}: $\rho = 0.976$. ($\psi$ is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:44:  shell-radius correlation rather than $119$ independent radial
papers/aria-closure-kernel/paper/sections/05_agreement.tex:47:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:55:\item Per-vertex test: $|V|-1 = 119$ data points (every
papers/aria-closure-kernel/paper/sections/05_agreement.tex:106:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:107:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:108:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:118:independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:120:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:123:this is a uniqueness or blind-selection result; we report it as a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:133:correlates per-vertex in radial shape, at Pearson $0.976$, with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:143:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:149:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:23:forecast about other forthcoming members of this programme; any
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:40:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:proposes a Lyapunov $V(W)$ on the reduced flow, an edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:47:decomposition under the $2I$ binary-icosahedral symmetry of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  correlation $0.976$ on the unweighted variant, with the unweighted
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:78:  the shared response primitive underneath two independent empirical works in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:86:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:88:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:94:  one extra shape parameter) and the AIC tie
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:97:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:98:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/02_definition.tex:40:  the spectral bottom $\inf \sigma(L_M)$ is explicitly known on
papers/aria-closure-kernel/paper/sections/02_definition.tex:43:  interval). The full-line case has $\inf \sigma(L_M) = 0$ as
papers/aria-closure-kernel/paper/sections/02_definition.tex:55:  decay-at-infinity (spectral bottom $\inf \sigma(L_M) = 0$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:137:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:5:This section threads the first independent empirical landing of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:14:Model, is approximately $q^{2}$-independent in the relevant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:92:  criterion (correlation $0.997$ with the continuum kernel under
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:95:  paper's per-vertex test, whose unweighted score is $0.976$;
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:119:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:120:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:  earlier analysis the b-anomaly project labels Mode-B
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:123:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:  between Mode-B (linearised) and the non-linear refit is the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:133:  emphasises that the geometry-only criterion is independent of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:136:  criterion-independent but not historically blind.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:146:anomaly across five independent measurements without shape
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:149:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:150:Mode-B linearised-to-non-linear refit drift prevent that). It
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:153:consistent with one of two independent empirical landings without
papers/aria-closure-kernel/paper/sections/01_introduction.tex:76:  is $\rho = 0.976$ on the unweighted graph Laplacian. (This is a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  multiplicity-weighted shell-radius correlation, not $119$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  independent radial samples; the within-shell variance is at
papers/aria-closure-kernel/paper/sections/01_introduction.tex:80:  numerical agreement between two independently-defined objects
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  correlation: $0.888$ and $0.884$ respectively. Within the three
papers/aria-closure-kernel/paper/sections/01_introduction.tex:91:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:112:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:115:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:121:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  parameter; the b-anomaly AIC comparison against
papers/aria-closure-kernel/paper/sections/01_introduction.tex:130:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:134:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:135:  reduced flow, edge-space decomposition under $2I$-equivariance
papers/aria-closure-kernel/paper/sections/01_introduction.tex:136:  (where $2I$ is the binary icosahedral group, the $\mathrm{SU}(2)$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:168:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:178:in two independent empirical works (b-anomaly five-dataset
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:202:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:205:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:5:This section threads the second independent empirical landing of
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:59:methodology refinements that we also inherit: P3
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:61:its preregistered band, and P13 (chess substrate lift) was
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:72:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:  pairwise common ground).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:99:\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:118:  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:119:  homogeneity, $+79.78\sigma$ on raw participation ratio (with
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:121:  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:149:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:163:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:179:Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:62:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:68:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/03_substrate.tex:83:fixing $v_{0}$ partitions the remaining $119$ vertices into shells
papers/aria-closure-kernel/paper/sections/03_substrate.tex:106:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:50:\emph{Evidence:} two independent empirical witnesses on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:72:independent empirical witnesses across qualitatively distinct
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:77:uniqueness is not assumed and is itself an open problem.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:85:\emph{computed agreement} between two independently-defined
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:106:\textbf{Two independent empirical landings, not formal physics.}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:138:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:144:\textbf{No deuteron / hadron / RH / capstone material is loaded
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:172:dataset, is consistent with two independent empirical landings in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:53:$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:56:$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:58:\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:59:$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:60:remaining $26/120 = 21.7\%$ is $\sigma$-paired. We report this
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:86:$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:88:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:89:$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the

codex
The verification artifacts are internally aligned on full-precision values: the script stores full floats in `results.json`, and the paper rounds them only in prose/tables. I’m now checking the companion sources for inherited caveats and tallies.
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/05_results.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 193ms:
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

 succeeded in 183ms:
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

 succeeded in 189ms:
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

 succeeded in 197ms:
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

codex
The companion checks confirm the active-witness refinements for P3, P4, and P13 are now represented in the kernel paper. One remaining external caveat from aria-chess limitations may still need to be carried over: P10’s prereg-exact 20-permutation rerun is listed there as open while the kernel paper summarizes only the 18/18 tally.
exec
/bin/bash -lc "rg -n \"\\\\label\\{|\\\\ref\\{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"derived|derivation|derive|unique|uniqueness|selection|Lyapunov|2I|equivariance|600-cell|119|independent radial|AIC|Mode-B|FREE_C9|P3|P4|P10|P13|forthcoming|RH|YM|Yang|Millennium|operator-norm|operator norm|phi\\"'^2|Ph'"\\"'^2|0'"\\.976|0\\.888|0\\.884|0\\.923|0\\.997|18/18|17/18\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "P10|20-permutation|permutation|15 permutations|18/18|17/18|P3|P4|P13|threshold|state-reset|leave-one-out|LOO" papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/05_results.tex papers/aria-chess-paper/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"AIC|Mode-B|Gaussian|FREE_C9|w_\\{|0\\.348|0\\.652|2\\.77|non-linear|linearised|variant|0\\.997|derived|unique\" /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md papers/aria-closure-kernel/paper/sections/06_passive_witness.tex papers/aria-closure-kernel/paper/main.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 215ms:
rg: regex parse error:
    (?:\label\{|\ref\{)
       ^^
error: unrecognized escape sequence

 succeeded in 217ms:
papers/aria-closure-kernel/paper/main.tex:76:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:81:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:107:correlation $0.976$ for the unweighted variant (the discrete
papers/aria-closure-kernel/paper/main.tex:109:$\Ph$-cocycle weighted variants tested ($0.888$ geometric, $0.884$
papers/aria-closure-kernel/paper/main.tex:111:tested variants the unweighted Laplacian ranks highest on the
papers/aria-closure-kernel/paper/main.tex:143:correlation is invariant under choice of source up to numerical
papers/aria-closure-kernel/paper/main.tex:172:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:174:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:175:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:201:discrete-to-continuum correlation across three Laplacian variants)
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:88:\item \textbf{Geometry-first variant test.} Of three discrete
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:89:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:92:  criterion (correlation $0.997$ with the continuum kernel under
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:98:  the variant ranking — a two-criterion agreement on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:112:  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:116:\item \textbf{Free-width Gaussian alternative.} A free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:117:  Gaussian charm-loop proxy fits the same five datasets comparably
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:119:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:120:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:  earlier analysis the b-anomaly project labels Mode-B
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:  (linearised) gave a stronger preference
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:123:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:  between Mode-B (linearised) and the non-linear refit is the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:128:\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:149:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:150:Mode-B linearised-to-non-linear refit drift prevent that). It
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:3:**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:14:A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:16:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:28:- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31:- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:32:- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:33:- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:35:The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:44:| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:76:│   ├── wo014_cross_dataset.py     # cross-dataset dataset loaders + linearised fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:77:│   ├── wo015_cross_channel.py     # Bs->phi cross-channel loader + linearised fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:82:│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:83:│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:84:│   ├── wo016d_nonlinear_xdataset.py  # non-linear refit across all 5 datasets
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:90:│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:91:│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:92:│   └── wo016d_nonlinear_xdataset.md   # paper §6 non-linear cross-dataset table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:138:1. The non-linear LHCb 2025 refit (`scripts/wo016c_nonlinear_refit.py`).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:139:2. The full five-dataset non-linear refit (`scripts/wo016d_nonlinear_xdataset.py`).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:141:4. The pure-geometry variant test (`scripts/wo016b_variant_geometry.py`).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:144:Total wall time: ~5 minutes on a laptop, dominated by the non-linear flavio calls. A persistent on-disk cache (`data/processed/flavio_cache.json`) ensures subsequent runs are near-instant.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:175:| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:176:| 3 | Three-layer kernel construction: continuum $\varphi$-tuned Green's function → bounded Dirichlet eigenmode → discrete 2I-equivariant lift on $V_{600}$. Variant-selection table on pure-geometry vs LHCb-data criteria. |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:177:| 4 | Results on LHCb 2025: non-linear vs linearised, drift table, leave-one-observable-out |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:178:| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:179:| 6 | Cross-dataset non-linear fit across five datasets; Akaike-weight stack; sign-uniformity test |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:185:The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:198:- **flavio** ([arXiv:1810.08132](https://arxiv.org/abs/1810.08132)) and **wilson** ([arXiv:1804.05033](https://arxiv.org/abs/1804.05033)) provide the SM and non-linear new-physics predictions used as the headline backend; their licences are upstream.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:207:  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},

 succeeded in 231ms:
papers/aria-chess-paper/paper/main.tex:52:literature-derived thresholds on a single deterministic substrate
papers/aria-chess-paper/paper/main.tex:80:before any validation run; each has a falsifiable threshold. The
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:88:P1--P18 preregistration; they are tested against thresholds drawn
papers/aria-chess-paper/paper/main.tex:106:(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:122:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:133:leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
papers/aria-chess-paper/paper/main.tex:135:preregistered estimator P13 was $5$-fold CV with threshold
papers/aria-chess-paper/paper/main.tex:136:$\geq\!+15$pp, the LOO finding above is a disclosed estimator/protocol
papers/aria-chess-paper/paper/main.tex:137:refinement at the same threshold), while conversation utterance
papers/aria-chess-paper/paper/main.tex:139:(threshold $|\cdot| < 10$pp), consistent with the substrate
papers/aria-chess-paper/paper/main.tex:167:without modifying any preregistered threshold.}
papers/aria-chess-paper/paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:122:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
papers/aria-chess-paper/paper/sections/09_limitations.tex:125:not a threshold change. \emph{Disclosure:}
papers/aria-chess-paper/paper/sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
papers/aria-chess-paper/paper/sections/09_limitations.tex:141:builds for P3/P4/P13 above; no further claim is needed.
papers/aria-chess-paper/paper/sections/09_limitations.tex:179:\item Verification of P10 (chess null mapping) at the preregistered
papers/aria-chess-paper/paper/sections/09_limitations.tex:180:  $20$-permutation count (the 2026-04-29 validation used $15$
papers/aria-chess-paper/paper/sections/09_limitations.tex:181:  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
papers/aria-chess-paper/paper/sections/09_limitations.tex:191:refinement and without modifying any preregistered threshold. We do
papers/aria-chess-paper/paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:96:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
papers/aria-chess-paper/paper/sections/05_results.tex:109:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:117:P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:130:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
papers/aria-chess-paper/paper/sections/05_results.tex:131:estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
papers/aria-chess-paper/paper/sections/05_results.tex:132:validation tightened the estimator to LOO with state reset, a
papers/aria-chess-paper/paper/sections/05_results.tex:133:disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
papers/aria-chess-paper/paper/sections/05_results.tex:137:methodology refinement (no threshold change).}
papers/aria-chess-paper/paper/sections/05_results.tex:139:\item P3 (D$\times$C interaction independence) was outside the band
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:149:  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
papers/aria-chess-paper/paper/sections/05_results.tex:150:  validation strengthened the estimator to LOO with state reset, a
papers/aria-chess-paper/paper/sections/05_results.tex:151:  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
papers/aria-chess-paper/paper/sections/05_results.tex:160:all pass at preregistered thresholds, with two interaction tests
papers/aria-chess-paper/paper/sections/05_results.tex:163:requiring the documented state-reset protocol. The original $15/18$

 succeeded in 256ms:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:14:arithmetic derivation in this paper.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:71:and the operator-norm bound is
papers/aria-closure-kernel/paper/sections/02_definition.tex:45:  for the operator-norm identity in
papers/aria-closure-kernel/paper/sections/02_definition.tex:53:  undirected graph (the 600-cell case, $\lambda_{\min}(L_M) = 0$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:80:The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:130:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:137:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:139:(1)--(3); we report this explicitly and treat formal derivation as
papers/aria-closure-kernel/paper/sections/02_definition.tex:143:selection-layer dynamics over $W$-space that would, if delivered,
papers/aria-closure-kernel/paper/sections/02_definition.tex:144:constrain the shift further; that derivation is not delivered
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:49:\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:50:  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:59:methodology refinements that we also inherit: P3
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:61:its preregistered band, and P13 (chess substrate lift) was
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:72:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:99:\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:140:aria-chess active-regime tally (frozen 2026-04-18): $17/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:142:validation protocol, $18/18$ after the documented $N\!=\!20$ P4
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:149:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:176:Headline           & $5/5$ sign uniformity              & $17/18$ standard, $18/18$ after P4 deep-dive; $6/6$ EEG \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:179:Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:operator-norm bound is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:67:  operator. The Laplacian spectrum, the operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:76:  is $\rho = 0.976$ on the unweighted graph Laplacian. (This is a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  multiplicity-weighted shell-radius correlation, not $119$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  independent radial samples; the within-shell variance is at
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  correlation: $0.888$ and $0.884$ respectively. Within the three
papers/aria-closure-kernel/paper/sections/01_introduction.tex:110:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:112:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:115:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:118:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:121:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  parameter; the b-anomaly AIC comparison against
papers/aria-closure-kernel/paper/sections/01_introduction.tex:130:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:133:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:134:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:135:  reduced flow, edge-space decomposition under $2I$-equivariance
papers/aria-closure-kernel/paper/sections/01_introduction.tex:136:  (where $2I$ is the binary icosahedral group, the $\mathrm{SU}(2)$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:aria-chess $17/18$ standard plus $18/18$ after the documented
papers/aria-closure-kernel/paper/sections/01_introduction.tex:166:$N\!=\!20$ P4 deep-dive) licenses a `consistent
papers/aria-closure-kernel/paper/sections/01_introduction.tex:168:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:selection'.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:176:600-cell graph, with computed spectrum, operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:structural fit; aria-chess $17/18$ preregistered correspondences
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:under the standard validation protocol and $18/18$ after the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:181:documented P4 $N\!=\!20$ deep-dive (thresholds unchanged), plus
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:195:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:205:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:206:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:14:The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:44:  (frozen 2026-04-18): $17/18$ preregistered
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:46:  validation protocol, $18/18$ after the documented $N\!=\!20$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:  P4 deep-dive (thresholds unchanged), plus six
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:62:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:68:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:82:selection gap.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:85:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:  over shell-constant responses}: $\rho = 0.976$. ($\psi$ is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:44:  shell-radius correlation rather than $119$ independent radial
papers/aria-closure-kernel/paper/sections/05_agreement.tex:47:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:55:\item Per-vertex test: $|V|-1 = 119$ data points (every
papers/aria-closure-kernel/paper/sections/05_agreement.tex:64:On the unweighted 600-cell graph with an H$_3$-fixed source,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:106:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:107:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:108:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:123:this is a uniqueness or blind-selection result; we report it as a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:133:correlates per-vertex in radial shape, at Pearson $0.976$, with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:143:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:149:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/main.tex:21:       a geometry-fixed kernel on the 600-cell with two\\
papers/aria-closure-kernel/paper/main.tex:44:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:53:agreement at per-vertex Pearson correlation $0.976$ between the
papers/aria-closure-kernel/paper/main.tex:57:machine precision under H$_3$-fixed source; not $119$ independent
papers/aria-closure-kernel/paper/main.tex:75:independent criterion. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:76:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:78:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:81:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:88:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:103:values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
papers/aria-closure-kernel/paper/main.tex:107:correlation $0.976$ for the unweighted variant (the discrete
papers/aria-closure-kernel/paper/main.tex:109:$\Ph$-cocycle weighted variants tested ($0.888$ geometric, $0.884$
papers/aria-closure-kernel/paper/main.tex:122:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:127:\noindent\emph{(ii) The 600-cell instance.}
papers/aria-closure-kernel/paper/main.tex:140:vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
papers/aria-closure-kernel/paper/main.tex:141:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:159:degree, passes $17/18$ preregistered correspondences (frozen
papers/aria-closure-kernel/paper/main.tex:160:2026-04-18) at standard methodology and $18/18$ after a documented
papers/aria-closure-kernel/paper/main.tex:162:$C\!\times\!P$ interaction (P4) — alongside two further documented
papers/aria-closure-kernel/paper/main.tex:163:methodology refinements in the aria-chess set ($N\!=\!5$ for P3
papers/aria-closure-kernel/paper/main.tex:164:within its preregistered band; LOO/state-reset for the P13 chess
papers/aria-closure-kernel/paper/main.tex:170:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:172:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:174:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:175:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:177:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:200:short-edge graph build, Laplacian spectrum, operator-norm bound,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested
papers/aria-closure-kernel/paper/sections/09_limitations.tex:18:fits on either empirical landing. The 600-cell choice is post-hoc
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:43:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:77:uniqueness is not assumed and is itself an open problem.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:86:objects, not a derivation that the discrete operator equals the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:138:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:142:in the response primitive without addressing the selection gap.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:144:\textbf{No deuteron / hadron / RH / capstone material is loaded
papers/aria-closure-kernel/paper/sections/09_limitations.tex:145:into this paper.} The cascade-derivation programme, the capstone
papers/aria-closure-kernel/paper/sections/09_limitations.tex:146:coalgebra paper, and the Millennium drafts share operator-level
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:nearest-neighbour adjacency on the canonical 600-cell embedding
papers/aria-closure-kernel/paper/sections/03_substrate.tex:73:  classical 600-cell connectivity result is well known
papers/aria-closure-kernel/paper/sections/03_substrate.tex:83:fixing $v_{0}$ partitions the remaining $119$ vertices into shells
papers/aria-closure-kernel/paper/sections/03_substrate.tex:106:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:133:  4-polytopes / Coxeter substrates. The 600-cell choice is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:92:  criterion (correlation $0.997$ with the continuum kernel under
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:95:  paper's per-vertex test, whose unweighted score is $0.976$;
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:119:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:120:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:  earlier analysis the b-anomaly project labels Mode-B
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:123:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:  between Mode-B (linearised) and the non-linear refit is the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:149:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:150:Mode-B linearised-to-non-linear refit drift prevent that). It
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:8:\emph{response} primitive; \emph{selection} (which response
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:23:forecast about other forthcoming members of this programme; any
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:27:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:40:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:44:The selection layer is open. The companion adaptive-closure-
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:proposes a Lyapunov $V(W)$ on the reduced flow, an edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:47:decomposition under the $2I$ binary-icosahedral symmetry of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:52:substrate-witness scope and does \emph{not} deliver a selection
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:55:without reducing or addressing the selection gap.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:62:  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:69:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  correlation $0.976$ on the unweighted variant, with the unweighted
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:85:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:86:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:88:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:94:  one extra shape parameter) and the AIC tie
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:97:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:98:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  positioning of cascade Lyapunov functionals as members of the

exec
/bin/bash -lc "rg -n -F \"\\label{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\ref{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\citep\\{|\\\\citet\\{|cite\\{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"@.*\\{\" papers/aria-closure-kernel/paper/references.bib" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 360ms:
rg: regex parse error:
    (?:\citep\{|\citet\{|cite\{)
       ^^
error: unrecognized escape sequence

 succeeded in 416ms:
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:49:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:23:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:64:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:83:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:104:\subsection{Test/claim}\label{ssec:testclaim}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:134:\subsection{State-drift / out-of-scope}\label{ssec:scope}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:16:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:44:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:80:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:86:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:108:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:30:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:16:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:36:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:75:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:78:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:\begin{equation}\label{eq:opnorm_zero_mode}
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:165:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}

 succeeded in 400ms:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:68:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:70:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:79:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:80:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:119:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:153:an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:46:  \S\ref{ssec:opnorm}; H3 does not require a finite-dimensional
papers/aria-closure-kernel/paper/sections/02_definition.tex:57:  function in \S\ref{ssec:continuum});
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:case used in \S\ref{ssec:continuum}), this reduces to the identity
papers/aria-closure-kernel/paper/sections/02_definition.tex:102:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:140:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:\textbf{Programme position.} \S\ref{sec:programme_home} positions
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:155:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:Table~\ref{tab:spectrum} to machine precision; multiplicities sum
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:21:\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:49:or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:70:\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:73:regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:87:continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:114:\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:135:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/03_substrate.tex:137:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:58:radial samples; \S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:133:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:137:response, see \S\ref{sec:agreement}) between the discrete response
papers/aria-closure-kernel/paper/main.tex:144:precision (multi-source sweep, \S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:204:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:205:\S\ref{sec:agreement} are deterministic outputs of the script.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:35:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:43:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:79:  machine precision; see \S\ref{ssec:result_unweighted}.) It is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:92:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:194:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:196:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:198:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:200:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:201:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:202:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:204:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:206:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:207:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 407ms:
1:@book{CoxeterRegularPolytopes,
10:@misc{Weisstein600Cell,
20:@unpublished{SmartBAnomaly2026,
28:@unpublished{SmartAriaChess2026,
37:@unpublished{SmartAdaptiveClosureTransport2026,
48:@article{KrugerMatias2005,
59:@article{LHCbAngular2020,

exec
/bin/bash -lc "rg -n -F \"\\citep{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\citet{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\cite{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "three-way|overlap|Sleep-EDFx|prior cascade|pairwise" papers/aria-closure-kernel/paper/sections/07_active_witness.tex papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/05_results.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 468ms:
 succeeded in 479ms:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:preprint~\citep{SmartAdaptiveClosureTransport2026} positions a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:45:transport preprint~\citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:51:companion~\citep{SmartAriaChess2026} likewise stays inside
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:96:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:31:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:69:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:65:in~\citep{SmartAriaChess2026} with no threshold modification, and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:105:  preprint~\citep{SmartAriaChess2026}), substrate routing lifts
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:170:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  vs $S$-basis factor $\sim 2.2$~\citep{KrugerMatias2005}) as
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:94:  metric, §3.4 of~\citep{SmartBAnomaly2026} — \emph{not} this
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:129:  preprint's limitations section~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:117:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:91:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/03_substrate.tex:11:not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:59:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/02_definition.tex:142:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:94:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:100:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:132:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:151:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/main.tex:63:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:66:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:79:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:94:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:97:signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:147:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:154:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:207:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:208:aria-chess~\citep{SmartAriaChess2026}) carry their own

 succeeded in 481ms:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:77:  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:78:  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:79:  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:80:  intervals do not overlap each other; the WAKE interval is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:  pairwise common ground).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:172:Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
papers/aria-chess-paper/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
papers/aria-chess-paper/paper/main.tex:99:This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
papers/aria-chess-paper/paper/main.tex:100:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
papers/aria-chess-paper/paper/main.tex:101:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
papers/aria-chess-paper/paper/main.tex:102:overlap.
papers/aria-chess-paper/paper/main.tex:184:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
papers/aria-chess-paper/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:9:gives the three-way $\alpha$ overlap. We lift the result map
papers/aria-chess-paper/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:166:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:168:The substrate's wake cascade-$\alpha$ confidence interval overlaps
papers/aria-chess-paper/paper/sections/05_results.tex:174:\caption{Three-way $\alpha$ overlap on the wake cascade-event power
papers/aria-chess-paper/paper/sections/05_results.tex:176:\label{tab:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:182:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
papers/aria-chess-paper/paper/sections/05_results.tex:183:ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
papers/aria-chess-paper/paper/sections/05_results.tex:190:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
papers/aria-chess-paper/paper/sections/05_results.tex:193:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
papers/aria-chess-paper/paper/sections/05_results.tex:194:intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
papers/aria-chess-paper/paper/sections/05_results.tex:205:any specific subject (\S\ref{sec:chain}). Three-way overlap on the

 exited 1 in 493ms:
  ✓ Read kernel paper, sections, bibliography, and repro artifacts
  ✓ Read companion preprints for inherited claims and caveats
  ✓ Cross-check numerics, scope discipline, and Round 10 fixes
  → Write structured referee review with file:line citations
codex
**Claim Audit**
- Must-fix: the active-witness import still omits aria-chess’s P10 caveat. Kernel paper reports the active tally and P3/P4/P13 refinements in [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:159>) and [07_active_witness.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47>), but aria-chess limitations say P10 used 15 permutations while the preregistered count was 20, with prereg-exact rerun open: [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/sections/09_limitations.tex:179>). Add this caveat wherever the imported `18/18` tally is summarized.
- Must-fix: Round-10 programme trimming is incomplete outside §8. The introduction still says §8 positions `C_phi` in a Lyapunov family recurring across “Millennium drafts” [01_introduction.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex:204>), while §8 itself says only the published ACT companion is used and no broader programme forecast is made [08_programme_home.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/08_programme_home.tex:20>). The conclusion also refers to “schematic family members named there” though §8 no longer names them [10_conclusion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74>).
- Mathematical precision issue: §2 correctly notes the full-line continuum has spectral bottom 0 but no zero eigenvalue [02_definition.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:40>), then later phrases the general operator norm as the reciprocal of the “smallest eigenvalue” and includes the full-line continuum in the same `lambda_min=0` wording [02_definition.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:80>). Use `inf sigma(L_M)` for the continuum case; keep eigenvalue language for finite graphs.

**Internal Consistency**
- The Round 10 P3/P4/P13 active-witness refinement is fixed in the abstract/headline and §7.
- The `0.976` wording is now correctly framed as multiplicity-weighted shell-radius correlation, not 119 independent radial samples: [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:106>), [01_introduction.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex:76>), [05_agreement.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:40>).
- Minor stale surface mismatch: main says “No randomness” [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:203>), while the script docstring mentions RNG seeding [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:20>). The code appears deterministic; fix the docstring.

**External Consistency / Numerics**
- Numerics match: spectrum and multiplicities in `results.json` [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:43>), operator norm [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:81>), and correlations [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:134>) agree with the paper.
- Script/results full-precision issue is fixed: grouping uses tolerance, but stored eigenvalues/correlations are full floats [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:129>), [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:425>).
- b-anomaly AIC tie and Mode-B drift are inherited correctly: [06_passive_witness.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108>) and [README.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31>).

**Operator-Witness Scope Discipline**
- Mostly disciplined: no derivation of `phi^-2`, no 600-cell uniqueness, no kernel uniqueness, no ACT selection theorem.
- The remaining scope risk is inherited active-witness exactness: without P10 caveat, “18/18 preregistered” reads too cleanly.

**Tightness**
- Good numerical tightness.
- Stale programme-language residues weaken the tightened ACT-only framing.

**Surface Issues**
- Remove or rewrite “Millennium drafts” and “future-programme context” residues.
- Fix continuum spectral-bottom wording.
- Clean the RNG docstring.

**Top Three Fixes**
1. Add the aria-chess P10 15-vs-20 permutation caveat to active-witness summaries.
2. Remove stale Millennium/future-programme language; keep §8 ACT-only.
3. Replace continuum “smallest eigenvalue” wording with spectral-bottom wording.

**Verdict**
Publication ready: no -- must-fix list above
tokens used
106,299
**Claim Audit**
- Must-fix: the active-witness import still omits aria-chess’s P10 caveat. Kernel paper reports the active tally and P3/P4/P13 refinements in [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:159>) and [07_active_witness.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47>), but aria-chess limitations say P10 used 15 permutations while the preregistered count was 20, with prereg-exact rerun open: [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/sections/09_limitations.tex:179>). Add this caveat wherever the imported `18/18` tally is summarized.
- Must-fix: Round-10 programme trimming is incomplete outside §8. The introduction still says §8 positions `C_phi` in a Lyapunov family recurring across “Millennium drafts” [01_introduction.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex:204>), while §8 itself says only the published ACT companion is used and no broader programme forecast is made [08_programme_home.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/08_programme_home.tex:20>). The conclusion also refers to “schematic family members named there” though §8 no longer names them [10_conclusion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74>).
- Mathematical precision issue: §2 correctly notes the full-line continuum has spectral bottom 0 but no zero eigenvalue [02_definition.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:40>), then later phrases the general operator norm as the reciprocal of the “smallest eigenvalue” and includes the full-line continuum in the same `lambda_min=0` wording [02_definition.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:80>). Use `inf sigma(L_M)` for the continuum case; keep eigenvalue language for finite graphs.

**Internal Consistency**
- The Round 10 P3/P4/P13 active-witness refinement is fixed in the abstract/headline and §7.
- The `0.976` wording is now correctly framed as multiplicity-weighted shell-radius correlation, not 119 independent radial samples: [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:106>), [01_introduction.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex:76>), [05_agreement.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:40>).
- Minor stale surface mismatch: main says “No randomness” [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:203>), while the script docstring mentions RNG seeding [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:20>). The code appears deterministic; fix the docstring.

**External Consistency / Numerics**
- Numerics match: spectrum and multiplicities in `results.json` [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:43>), operator norm [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:81>), and correlations [results.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:134>) agree with the paper.
- Script/results full-precision issue is fixed: grouping uses tolerance, but stored eigenvalues/correlations are full floats [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:129>), [verify_kernel.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py:425>).
- b-anomaly AIC tie and Mode-B drift are inherited correctly: [06_passive_witness.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108>) and [README.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31>).

**Operator-Witness Scope Discipline**
- Mostly disciplined: no derivation of `phi^-2`, no 600-cell uniqueness, no kernel uniqueness, no ACT selection theorem.
- The remaining scope risk is inherited active-witness exactness: without P10 caveat, “18/18 preregistered” reads too cleanly.

**Tightness**
- Good numerical tightness.
- Stale programme-language residues weaken the tightened ACT-only framing.

**Surface Issues**
- Remove or rewrite “Millennium drafts” and “future-programme context” residues.
- Fix continuum spectral-bottom wording.
- Clean the RNG docstring.

**Top Three Fixes**
1. Add the aria-chess P10 15-vs-20 permutation caveat to active-witness summaries.
2. Remove stale Millennium/future-programme language; keep §8 ACT-only.
3. Replace continuum “smallest eigenvalue” wording with spectral-bottom wording.

**Verdict**
Publication ready: no -- must-fix list above

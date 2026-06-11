OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dde67-74b5-7e60-837c-887ad81a578b
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
I’ll read the LaTeX, source notes, companion paper, and repro outputs as local source material, then cross-check the numerical and inherited-claim surfaces before writing the referee-style review.
exec
/bin/bash -lc 'find papers/aria-chess-paper/paper -maxdepth 2 -type f | sort' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "wc -l docs/aria-closure-kernel.md /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 163ms:
papers/aria-chess-paper/paper/README.md
papers/aria-chess-paper/paper/main.pdf
papers/aria-chess-paper/paper/main.tex
papers/aria-chess-paper/paper/references.bib
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

 succeeded in 201ms:
  187 papers/aria-closure-kernel/paper/main.tex
  191 papers/aria-closure-kernel/paper/sections/01_introduction.tex
  121 papers/aria-closure-kernel/paper/sections/02_definition.tex
  132 papers/aria-closure-kernel/paper/sections/03_substrate.tex
   98 papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  131 papers/aria-closure-kernel/paper/sections/05_agreement.tex
  132 papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  169 papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  137 papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  176 papers/aria-closure-kernel/paper/sections/09_limitations.tex
   83 papers/aria-closure-kernel/paper/sections/10_conclusion.tex
   86 papers/aria-closure-kernel/paper/references.bib
  465 papers/aria-closure-kernel/repro/verify_kernel.py
  154 papers/aria-closure-kernel/repro/results.json
 2262 total

 succeeded in 217ms:
   295 docs/aria-closure-kernel.md
   227 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md
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
  2622 total

codex
The closure-kernel paper is about 1,450 lines plus repro and references, so I’m reading it with line numbers in batches. I’ll keep the cross-checks local and cite exact lines in the final review.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/01_introduction.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/02_definition.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 283ms:
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

 succeeded in 293ms:
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
    37	generated by three H$_4$ Coxeter orbits ($8$ axis vertices, $16$
    38	half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
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
    75	\item \textbf{Variant comparison is decisive at the geometry-only
    76	  criterion.} Two $\Ph$-cocycle weighted Laplacian variants
    77	  ($\Ph$-geometric, $\Ph$-arithmetic edge weights via shell-grade
    78	  exponents $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    79	  correlation: $0.888$ and $0.884$ respectively. The unweighted
    80	  Laplacian wins on the geometry-only criterion. This reproduces,
    81	  on a different test, the qualitative ranking established
    82	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    83	  (\S\ref{sec:passive_witness}).
    84	\item \textbf{Two independent empirical landings, same operator.}
    85	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    86	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    87	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    88	  public datasets, with one fitted dimensionless amplitude per
    89	  dataset and the kernel held fixed; sign uniformity holds in
    90	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
    91	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
    92	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
    93	  recurrent self-model layer above the substrate, to pass eighteen
    94	  preregistered cortical correspondences (frozen 2026-04-18) plus
    95	  six drug/sleep EEG signatures.
    96	\end{enumerate}
    97	
    98	\subsection*{What this paper does \emph{not} claim}
    99	
   100	\begin{itemize}\itemsep=2pt
   101	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
   102	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   103	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   104	  functional or a symmetry argument; we report its role as a
   105	  regularisation-of-mass scale.
   106	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   107	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   108	  highly symmetric graphs, and continuum substrates are all
   109	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   110	  is post-hoc motivated by the empirical landings; a formal
   111	  ablation against alternative substrates is an open build.
   112	\item \emph{Not a kernel-uniqueness claim on either empirical
   113	  landing.} The b-anomaly's free-width Gaussian alternative shows
   114	  that a free-width Gaussian charm-loop proxy fits the same five
   115	  datasets comparably in $\chi^{2}$ at the cost of one extra shape
   116	  parameter; the b-anomaly AIC comparison against
   117	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   118	  statistical tie on current data
   119	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   120	  Both caveats are inherited verbatim from the b-anomaly preprint.
   121	\item \emph{Not a selection theorem on the
   122	  ACT 4-tuple.} The companion adaptive-closure-transport
   123	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   124	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   125	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   126	  reduced flow, edge-space decomposition under $2I$-equivariance,
   127	  full reduced-flow convergence — is left open in that paper and
   128	  is not delivered here.
   129	\item \emph{Not a circuit-level model on the active-regime side.}
   130	  The aria-chess preprint operates at the architectural-algorithmic
   131	  level above $\Cph$. We import its empirical results verbatim and
   132	  do not relitigate them here; their substrate-witness scope
   133	  applies.
   134	\end{itemize}
   135	
   136	\subsection*{Mapping from numerics to admissible claims}
   137	
   138	To keep this paper inside the operator-witness scope, we use the
   139	same claim-boundary discipline as the aria-chess
   140	preprint~\citep{SmartAriaChess2026}: numerical results
   141	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   142	$\mathcal C_{\mathrm{admissible}}$ by the rule
   143	\[
   144	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   145	        \mathcal C_{\mathrm{admissible}},
   146	\qquad
   147	\mathcal C_{\mathrm{admissible}}
   148	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   149	\]
   150	A numerically computed quantity (the Laplacian spectrum, the
   151	operator-norm bound, the per-vertex correlation $0.976$) licenses
   152	a `computed'-type claim. A statistical agreement at the operator
   153	level (sign uniformity in $5/5$ datasets, an $18/18$ preregistered
   154	tally) licenses a `consistent with'-type claim. We never write
   155	`derives the kernel', `proves uniqueness', or `establishes
   156	selection'.
   157	
   158	\medskip
   159	\begin{center}
   160	\fbox{\parbox{0.92\linewidth}{\small
   161	\textbf{What is claimed / what is not.}\par
   162	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   163	600-cell graph, with computed spectrum, operator-norm bound, and
   164	discrete-to-continuum correlation; the same fixed operator appearing
   165	in two independent empirical works (b-anomaly five-dataset
   166	structural fit; aria-chess $18/18$ + $6/6$ preregistered substrate
   167	witness) without shape-parameter retuning between regimes.\par
   168	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   169	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   170	landing; a selection theorem on the ACT 4-tuple; that either
   171	empirical landing settles the underlying physics (flavour anomaly
   172	or consciousness) by the operator alone.
   173	}}
   174	\end{center}
   175	
   176	\subsection*{Layout}
   177	
   178	\S\ref{sec:definition} gives the operator definition, the positivity
   179	properties of $\Cph$, the operator-norm bound, and the continuum
   180	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   181	canonical generators, gives the graph facts, and the $9$-shell
   182	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   183	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   184	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   185	across three Laplacian variants. \S\ref{sec:passive_witness} and
   186	\S\ref{sec:active_witness} thread the two independent empirical
   187	witnesses (b-anomaly and aria-chess) at the operator level.
   188	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   189	for the polynomial-in-$L$ Lyapunov family that recurs across the
   190	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   191	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 305ms:
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
    42	Laplacian $L_M$ and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
    43	the 600-cell instance $\Rsixhundred$ as the discrete substrate
    44	shared by the two empirical witnesses (the choice of this polytope
    45	is post-hoc motivated by those landings, \S\ref{sec:limitations};
    46	numerically reproduced: $|V|=120$, $|E|=720$, uniform
    47	degree~$12$, H$_3$ shell decomposition
    48	$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
    49	matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
    50	operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
    51	eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
    52	agreement at per-vertex Pearson correlation $0.976$ between the
    53	discrete Green response and the continuum kernel
    54	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
    55	\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
    56	same fixed graph is then the load-bearing object in two
    57	\emph{independent} empirical works: a passive-regime structural
    58	fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
    59	public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
    60	active-regime substrate witness against eighteen preregistered
    61	neuroscience correspondences plus six drug/sleep EEG
    62	signatures~\citep{SmartAriaChess2026}.
    63	
    64	\noindent\emph{Scope.}
    65	This paper presents an empirical \emph{operator witness}: a
    66	geometry-fixed response operator that is simultaneously consistent
    67	with two independent empirical landings under no shape-parameter
    68	retuning between regimes. It is \emph{not} a derivation of the
    69	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    70	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    71	selection theorem on the companion adaptive-closure-transport
    72	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    73	a model-preference claim against alternative kernels on either
    74	empirical landing (the b-anomaly AIC comparison and the aria-chess
    75	substrate-witness scope are documented in their own preprints and
    76	inherited verbatim here).
    77	
    78	\begin{abstract}
    79	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    80	a closure substrate $M$ with graph Laplacian $L_M$ and
    81	$\Ph = (1+\sqrt 5)/2$, give its canonical instance on the 600-cell
    82	graph $\Rsixhundred$, and document its appearance as the same
    83	fixed operator (no shape retuning) in two independent empirical
    84	works: (i)~a five-dataset structural fit of the
    85	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    86	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    87	preregistered substrate witness against cortical signatures plus
    88	six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
    89	include the numerical reproduction script
    90	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
    91	from canonical generators, verifies the graph facts
    92	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
    93	Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
    94	$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
    95	agreement at per-vertex Pearson correlation $0.976$ for the
    96	unweighted variant, above the two $\Ph$-cocycle weighted variants
    97	tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
    98	tested variants the unweighted Laplacian wins on the geometry-only
    99	criterion, reproducing the qualitative ranking established
   100	independently by b-anomaly's data $\chi^{2}$ comparison.
   101	
   102	\noindent\emph{(i) Operator definition and properties.}
   103	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   104	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   105	$\Ph^{-2} \approx 0.382$, operator norm
   106	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   107	in one coordinate $x$ is the closed-form Green's function
   108	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   109	
   110	\noindent\emph{(ii) The 600-cell instance.}
   111	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   112	generated by three orbits ($8$~axis, $16$~half-integer,
   113	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   114	on the short-edge graph; the Laplacian has nine eigenvalue classes
   115	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   116	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   117	
   118	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   119	Per-vertex Pearson correlation between the discrete response
   120	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   121	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each vertex's chord
   122	distance: $0.976$ (unweighted Laplacian), $0.888$
   123	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   124	Same source vertex, same fixed shift, no parameter fitting.
   125	
   126	\noindent\emph{(iv) Two independent empirical witnesses.}
   127	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   128	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   129	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   130	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   131	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   132	with one fitted dimensionless amplitude per dataset and the kernel
   133	shape held fixed. (b)~Active regime,
   134	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   135	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   136	condition-dependent self-injection coupling
   137	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   138	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   139	degree, passes eighteen preregistered correspondences (frozen
   140	2026-04-18) and six drug/sleep EEG signatures.
   141	
   142	\noindent\emph{What we do not claim.}
   143	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   144	stability clamp making $\Cph$ strictly positive definite. We do
   145	not claim $\Rsixhundred$ is the unique substrate consistent with
   146	either empirical landing. We do not claim the operator is the
   147	unique kernel shape consistent with the b-anomaly data
   148	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   149	drift caveats are inherited verbatim) nor that the
   150	aria-chess substrate witness establishes a selection theorem on
   151	the adaptive-closure-transport 4-tuple. The structural scope of
   152	this paper is: \emph{one geometry-fixed operator on one fixed
   153	graph appears as the load-bearing object in two independent
   154	empirical works in two distinct regimes, with no shape retuning
   155	between them}.
   156	\end{abstract}
   157	
   158	% =====================================================================
   159	\input{sections/01_introduction.tex}
   160	\input{sections/02_definition.tex}
   161	\input{sections/03_substrate.tex}
   162	\input{sections/04_spectrum.tex}
   163	\input{sections/05_agreement.tex}
   164	\input{sections/06_passive_witness.tex}
   165	\input{sections/07_active_witness.tex}
   166	\input{sections/08_programme_home.tex}
   167	\input{sections/09_limitations.tex}
   168	\input{sections/10_conclusion.tex}
   169	% =====================================================================
   170	
   171	\section*{Reproducibility}
   172	The complete numerical verification (vertex construction,
   173	short-edge graph build, Laplacian spectrum, operator-norm bound,
   174	discrete-to-continuum correlation across three Laplacian variants)
   175	is reproducible from \texttt{repro/verify\_kernel.py} in this
   176	paper's bundle. No randomness, no fitted parameters: all numbers
   177	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   178	\S\ref{sec:agreement} are deterministic outputs of the script.
   179	The two empirical witness preprints
   180	(b-anomaly~\citep{SmartBAnomaly2026},
   181	aria-chess~\citep{SmartAriaChess2026}) carry their own
   182	reproducibility artifacts; this paper does not duplicate them.
   183	
   184	\bibliographystyle{plainnat}
   185	\bibliography{references}
   186	
   187	\end{document}

 succeeded in 328ms:
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
    19	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
    20	generating orbits are:
    21	\begin{itemize}\itemsep=2pt
    22	\item \textbf{Axis orbit} ($8$ vertices): all permutations of
    23	  $(\pm 1, 0, 0, 0)$;
    24	\item \textbf{Half-integer orbit} ($16$ vertices): all sign
    25	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    26	\item \textbf{$\Ph$-mixed orbit} ($96$ vertices): all even
    27	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
    28	  $\Ph^{2} = \Ph + 1$ identity, equivalently
    29	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
    30	\end{itemize}
    31	The total is $8 + 16 + 96 = 120$ unit vectors. Reproduced by
    32	\texttt{repro/verify\_kernel.py:build\_v600}; the numerical check
    33	$\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms all vertices on
    34	$S^{3}$.
    35	
    36	The H$_4$ Coxeter group (order $14400$) acts transitively on the
    37	$120$ vertices. Every vertex therefore has \emph{identical} local
    38	structure under $H_{4}$; in particular, every vertex has the same
    39	degree in the short-edge graph defined below.
    40	
    41	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
    42	
    43	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
    44	Euclidean chord distance is
    45	\[
    46	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
    47	\]
    48	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
    49	if their inner product equals the canonical short-edge value
    50	\begin{equation}\label{eq:short_edge}
    51	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
    52	\end{equation}
    53	equivalently chord distance
    54	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
    55	nearest-neighbour adjacency on the canonical 600-cell embedding
    56	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
    57	
    58	\paragraph{Graph facts (forced by the construction).}
    59	The graph $G_{V_{600}}$ has:
    60	\begin{itemize}\itemsep=2pt
    61	\item $|V|=120$ vertices,
    62	\item $|E|=720$ edges,
    63	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
    64	  the vertex set forces uniformity of the local structure; the
    65	  short-edge nearest-neighbour graph inherits this uniformity),
    66	\item the graph is connected (verified numerically by counting
    67	  connected components of the short-edge adjacency matrix; the
    68	  classical 600-cell connectivity result is well known
    69	  in~\citep{CoxeterRegularPolytopes}).
    70	\end{itemize}
    71	All four facts are reproduced numerically:
    72	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
    73	degree-min/max $=12/12$ (uniform), and one connected component.
    74	
    75	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
    76	
    77	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
    78	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
    79	of constant inner product with $v_{0}$. The nine canonical inner
    80	products are
    81	\begin{equation}\label{eq:shell_inner}
    82	\langle v, v_{0}\rangle
    83	\;\in\;
    84	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
    85	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
    86	\end{equation}
    87	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
    88	antipode. The shell-size sequence is
    89	\begin{equation}\label{eq:shell_sizes}
    90	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
    91	\;=\;
    92	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
    93	\end{equation}
    94	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
    95	icosidodecahedral ring. The total is
    96	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
    97	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
    98	
    99	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
   100	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
   101	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
   102	
   103	\subsection{Inner-product check}\label{ssec:inner_product_check}
   104	
   105	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   106	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   107	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   108	vertex in shell $s_{2}$ if and only if their pairwise inner product
   109	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   110	adjacency types to those compatible with the H$_3$ orbit structure.
   111	The numerically constructed graph respects this: every edge has
   112	inner product exactly $\Ph/2$ within machine precision (tolerance
   113	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   114	
   115	\subsection{What the substrate fixes, and what it does not}
   116	
   117	\begin{itemize}\itemsep=2pt
   118	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   119	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   120	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   121	  Laplacian spectrum (\S\ref{sec:spectrum}).
   122	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   123	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   124	  (\S\ref{ssec:opnorm}); the operator-norm bound
   125	  $\|\Cph^{-1}\| = \Ph^{2}$.
   126	\item \textbf{Not fixed by this paper}: the choice of
   127	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other H$_n$
   128	  Coxeter substrates. The 600-cell choice is post-hoc motivated by
   129	  the empirical landings (\S\ref{sec:passive_witness},
   130	  \S\ref{sec:active_witness}). A formal substrate ablation is an
   131	  open build (\S\ref{sec:limitations}).
   132	\end{itemize}

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/04_spectrum.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/06_passive_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/07_active_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 292ms:
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
    58	remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
    59	artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
    60	reformulation; that reading is not imported here. We report only
    61	that the spectrum has this structure.
    62	
    63	\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
    64	
    65	The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
    66	\[
    67	\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
    68	\;\approx\; 0.381966,
    69	\]
    70	and the operator-norm bound is
    71	\[
    72	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
    73	\]
    74	\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
    75	$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
    76	(predicted) — match to six decimal places. The largest eigenvalue
    77	of $\Cph$ is
    78	$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
    79	= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
    80	
    81	\subsection{H$_4$ irrep block decomposition (imported context)}
    82	\label{ssec:irrep}
    83	
    84	The eigenspaces of $\Lop$ partition into H$_4$-proper and
    85	$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
    86	exponents are $\{1, 11, 19, 29\}$; under the
    87	$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
    88	$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
    89	aria-chess companion's recurrent
    90	layer~\citep{SmartAriaChess2026} realises this block decomposition
    91	at machine precision and provides a spectrally clean
    92	H$_4$-equivariant basis there.
    93	
    94	This subsection is imported context from the aria-chess companion;
    95	the irrep block decomposition is \emph{not} verified by
    96	\texttt{repro/verify\_kernel.py} of this paper and is not used as
    97	a load-bearing fact for any operator-witness claim made here. We
    98	include the labelling for orientation only.

 succeeded in 266ms:
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
   119	$k=12$; no other shape parameter enters; the kernel shift
   120	$\Ph^{-2}$ is not retuned. Under those design choices, the same
   121	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
   122	preregistered cortical correspondences (frozen 2026-04-18) and six
   123	literature-thresholded EEG drug/sleep signatures.
   124	
   125	The aria-chess preprint stays inside substrate-witness scope: it
   126	does not claim the substrate \emph{is} consciousness, does not
   127	claim 600-cell uniqueness among regular 4-polytopes, and does not
   128	deliver a selection theorem on the ACT 4-tuple. We inherit the
   129	scope verbatim. What we add at the operator level is the
   130	observation that the same fixed $\Cph$ — under no shape-parameter
   131	retuning between regimes — is the load-bearing object on both
   132	empirical landings.
   133	
   134	\subsection{Two-witness structure}
   135	
   136	\begin{table}[ht]
   137	\centering
   138	\small
   139	\caption{Two independent empirical landings of $\Cph$ on
   140	$\Rsixhundred$, with no shape retuning between regimes.}
   141	\label{tab:two_witness}
   142	\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
   143	\toprule
   144	& Passive regime & Active regime \\
   145	\midrule
   146	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   147	Domain             & flavour physics                    & cortical neuroscience \\
   148	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   149	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   150	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   151	Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
   152	Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
   153	Kernel-shape free params & 0                            & 0 \\
   154	Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
   155	Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
   156	\bottomrule
   157	\end{tabular}
   158	\end{table}
   159	
   160	The two witnesses share, by design, exactly the geometry-fixed
   161	operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
   162	the same shift $\Ph^{-2}$. They share no fitted parameter,
   163	threshold, dataset, or methodological choice above the operator
   164	level. The b-anomaly amplitude $A$ is fitted to flavour-physics
   165	$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
   166	is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
   167	neural data; the v4 stimulus protocols are biologically motivated,
   168	not subject-fit. Independence in this paper is independence at
   169	the empirical layer above the shared operator.

 succeeded in 288ms:
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
    39	\caption{b-anomaly five-dataset structural fit. Verbatim
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
   100	\item \textbf{Free-width Gaussian alternative.} A free-width
   101	  Gaussian charm-loop proxy fits the same five datasets comparably
   102	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   103	  is not the unique $q^{2}$ shape consistent with the anomaly.
   104	\item \textbf{Mode-B drift (linearised-vs-nonlinear refit).} An
   105	  earlier linearised analysis gave a stronger preference
   106	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   107	  the non-linear refit; the $+2.77$-AIC-unit drift between
   108	  linearised and Mode-B (non-linear) refits is the largest single
   109	  methodological uncertainty in the b-anomaly project.
   110	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   111	  preprint's limitations section acknowledges that the LHCb~2025
   112	  data was looked at first, and only later was the agreement of
   113	  the data-$\chi^{2}$ ranking with the pure-geometry ranking
   114	  verified. The two-criterion agreement is criterion-independent
   115	  but not historically blind.
   116	\end{itemize}
   117	
   118	\subsection{Reading at the operator level}
   119	
   120	The b-anomaly result is the \emph{passive-regime} empirical
   121	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   122	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   123	fixed discrete-to-momentum projection, gives a sign-uniform
   124	description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
   125	five independent measurements without shape retuning. This does
   126	not establish the kernel as theorem-grade physics on the flavour
   127	side (the AIC tie, the free-width Gaussian alternative, and the
   128	Mode-B linearised-vs-nonlinear refit drift prevent that). It does
   129	establish, at the operator level, that the same fixed $\Cph$ on
   130	the same fixed $\Rsixhundred$ is consistent with one of two
   131	independent empirical landings without parameter retuning. The
   132	second landing is in \S\ref{sec:active_witness}.

 succeeded in 304ms:
     1	% =====================================================================
     2	\section{Discrete-to-continuum agreement}\label{sec:agreement}
     3	% =====================================================================
     4	
     5	This is the load-bearing geometric fact of the paper: the discrete
     6	response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
     7	source agrees per-vertex with the continuum kernel
     8	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
     9	the source. We give the test, the numerical result, and a variant
    10	comparison that selects the unweighted Laplacian among the three
    11	tested variants (unweighted, $\Ph$-geometric weighted,
    12	$\Ph$-arithmetic weighted).
    13	
    14	\subsection{The test}\label{ssec:test}
    15	
    16	Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
    17	vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
    18	other entries zero). Compute
    19	\[
    20	\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
    21	\]
    22	by direct linear solve (no eigenmode truncation). For each vertex
    23	$v \in V$, compute the Euclidean chord distance
    24	$x(v) = \|v - v_{0}\|$ and the continuum prediction
    25	\[
    26	G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
    27	\]
    28	The agreement criterion is the Pearson correlation between
    29	$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
    30	source itself is excluded, since the discrete response there is
    31	trivially the diagonal of $\Cph^{-1}$ and the chord distance is
    32	zero, both degenerate for the comparison).
    33	
    34	\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
    35	
    36	\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
    37	\begin{itemize}\itemsep=2pt
    38	\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
    39	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
    40	  (averaging $\psi(v)$ over each H$_3$ shell first, then
    41	  correlating the $9$-point shell-mean trajectory with the
    42	  continuum prediction at the shell mean radius).
    43	\end{itemize}
    44	The two correlations measure the same fact at different
    45	resolutions: per-vertex tests at $|V|-1 = 119$ data points
    46	(every non-source vertex), while shell-mean tests at $9$ data
    47	points (one per shell). On the unweighted 600-cell graph with
    48	an H$_3$-fixed source, $\psi$ is shell-constant up to numerical
    49	precision — the within-shell standard deviations are at machine
    50	precision ($\sim 10^{-16}$). The two tests therefore differ in
    51	weighting, not in noise content: the per-vertex test weights each
    52	shell by its multiplicity ($\{12, 20, 12, 30, 12, 20, 12, 1\}$
    53	for the non-source shells) and excludes the source vertex,
    54	while the shell-mean test gives equal weight to every shell. The
    55	per-vertex test is the headline agreement criterion in this paper.
    56	
    57	\subsection{Variant comparison}\label{ssec:variant_comparison}
    58	
    59	Two $\Ph$-cocycle weighted Laplacian variants are tested as
    60	controls:
    61	
    62	\begin{itemize}\itemsep=2pt
    63	\item \textbf{$\Ph$-geometric weights}: edge weight
    64	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
    65	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
    66	  is the shell index of $v$.
    67	\item \textbf{$\Ph$-arithmetic weights}: edge weight
    68	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
    69	  $\omega_{+}$.
    70	\end{itemize}
    71	The weighted Laplacian is then
    72	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
    73	We re-run the discrete-to-continuum test on each variant.
    74	
    75	\begin{table}[ht]
    76	\centering
    77	\small
    78	\caption{Per-vertex and shell-mean Pearson correlations between the
    79	discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
    80	prediction $G(\|v - v_{0}\|)$ for three Laplacian variants.
    81	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
    82	\label{tab:variant_correlation}
    83	\begin{tabular}{l c c}
    84	\toprule
    85	Variant            & Per-vertex correlation & Shell-mean correlation \\
    86	\midrule
    87	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
    88	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
    89	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
    90	\bottomrule
    91	\end{tabular}
    92	\end{table}
    93	
    94	\textbf{Reading.} Within the three tested variants, the unweighted
    95	Laplacian wins on both criteria by a clear margin ($+0.088$
    96	per-vertex over the next variant, $+0.043$ shell-mean). This
    97	reproduces, on a different test, the qualitative ranking the
    98	b-anomaly paper~\citep{SmartBAnomaly2026} established
    99	independently against its data-$\chi^{2}$ criterion
   100	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
   101	b-anomaly numbers). Two independent criteria — geometry-only
   102	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
   103	agree on which Laplacian variant is preferred. We do not claim
   104	this is a uniqueness result; we report it as a two-criterion
   105	convergence (the b-anomaly paper's own caveat that the data was
   106	looked at first and the geometry criterion verified afterward is
   107	inherited verbatim).
   108	
   109	\subsection{What the agreement does and does not establish}
   110	
   111	\paragraph{Does establish.} A geometric agreement: the discrete
   112	response of a fixed-shift Green operator on a fixed graph behaves,
   113	to within the per-vertex Pearson correlation $0.976$, like the
   114	closed-form continuum exponential at the same length scale $\Ph$.
   115	This is a non-trivial agreement between two independently-defined
   116	objects: (i) the discrete inverse of a $120\times 120$
   117	Laplacian-plus-shift matrix; and (ii) a one-dimensional continuum
   118	exponential. The $\Ph$-mediated agreement is an empirical fact
   119	about the chosen substrate and shift, computed (not fitted) by
   120	the verification script.
   121	
   122	\paragraph{Does not establish.} Operator uniqueness on either
   123	empirical landing — the b-anomaly paper documents a free-width
   124	Gaussian alternative that fits comparably in $\chi^{2}$ at the
   125	cost of one extra shape parameter, and the aria-chess preprint
   126	does not run a substrate ablation; both caveats are inherited
   127	verbatim. The agreement also does not establish that
   128	$\Rsixhundred$ is the unique discrete substrate with this
   129	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   130	graphs would give different correlations on the same test, and a
   131	formal substrate ablation is an open build (\S\ref{sec:limitations}).

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/08_programme_home.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 244ms:
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
    49	geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
    50	shift $\Ph^{-2}$, and the response is the resulting linear inverse.
    51	This is a \emph{response} primitive. It does \emph{not} answer:
    52	\begin{itemize}\itemsep=2pt
    53	\item Why this substrate? (Selection across regular 4-polytopes
    54	  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
    55	\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
    56	  positive constant.)
    57	\item How does the system pick a response configuration over
    58	  time? (Crystallisation / Lyapunov descent dynamics on a
    59	  $W$-trajectory.)
    60	\end{itemize}
    61	
    62	The selection layer is open. It appears as an open hypothesis in
    63	three independent frames:
    64	\begin{enumerate}\itemsep=2pt
    65	\item \textbf{Forthcoming RH artifact}: the closure-flow suppression
    66	  hypothesis $\textup{H}_{\mathrm{attr}}$ at the level of the
    67	  original cascade closure functional. The polynomial filter
    68	  $\Psi_{t}$ is a finite-dimensional analogue, by design.
    69	\item \textbf{Adaptive Closure
    70	  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
    71	  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
    72	  $V(W)$ on the reduced flow, an edge-space decomposition under
    73	  $2I$-equivariance, and a full reduced-flow convergence theorem
    74	  on $W$-trajectories — \emph{none delivered} in that paper.
    75	\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
    76	  the substrate-witness scope explicitly does \emph{not} deliver
    77	  a selection theorem; ACT is positioned as the future
    78	  selection-theorem witness.
    79	\end{enumerate}
    80	
    81	The recurrence of an open selection gap across these three frames
    82	is a programme-level reading: the gap may be a single mathematical
    83	problem rather than three independent ones, but the present paper
    84	gives no proof of equivalence. The two empirical witnesses landed
    85	in this paper strengthen external confidence in the \emph{response}
    86	primitive without reducing or addressing the selection gap.
    87	
    88	\subsection{What this paper closes vs leaves open}
    89	
    90	\paragraph{Closes (at the operator-witness level).}
    91	\begin{itemize}\itemsep=2pt
    92	\item The operator $\Cph$ is well-defined and positive definite
    93	  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
    94	  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
    95	  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
    96	  with the standard combinatorial Laplacian). On substrates where
    97	  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
    98	  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
    99	  generally strict (\S\ref{sec:definition}).
   100	\item The 600-cell instance $\Rsixhundred$ has the construction
   101	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
   102	  Table~\ref{tab:spectrum}, both reproduced numerically
   103	  (\texttt{repro/verify\_kernel.py}).
   104	\item Discrete-to-continuum agreement at per-vertex Pearson
   105	  correlation $0.976$ on the unweighted variant, with the unweighted
   106	  variant winning the geometry-only criterion against two
   107	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
   108	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
   109	  the load-bearing object in two independent empirical works in
   110	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
   111	  \S\ref{sec:active_witness}).
   112	\end{itemize}
   113	
   114	\paragraph{Leaves open.}
   115	\begin{itemize}\itemsep=2pt
   116	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
   117	  as a design-level shift; not derived from a closure functional
   118	  or symmetry argument.
   119	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
   120	  post-hoc motivated by the empirical landings; alternative regular
   121	  4-polytopes are an explicit ablation build, not a discharged
   122	  comparison.
   123	\item \emph{Kernel-uniqueness on either empirical landing.} The
   124	  b-anomaly free-width Gaussian alternative (fits comparably with
   125	  one extra shape parameter) and the AIC tie
   126	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
   127	  inherited verbatim from~\citep{SmartBAnomaly2026}.
   128	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
   129	  decomposition under $2I$-equivariance, full reduced-flow
   130	  convergence — all explicitly not delivered
   131	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   132	  here.
   133	\item \emph{Family-membership theorem.} The programme-home
   134	  positioning of cascade Lyapunov functionals as members of the
   135	  same polynomial-in-$L$ family is reported as
   136	  \emph{programme-positioned}, not formally classified.
   137	\end{itemize}

 succeeded in 265ms:
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

 succeeded in 237ms:
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
    64	% External flavour-physics literature (b-anomaly context, cited in §6).
    65	
    66	@article{KrugerMatias2005,
    67	  author  = {Kr\"uger, Frank and Matias, Joaquim},
    68	  title   = {Probing new physics via the transverse amplitudes of
    69	             $B^0 \to K^{*0} (\to K^- \pi^+) l^+ l^-$ at low recoil},
    70	  journal = {Phys. Rev. D},
    71	  volume  = {71},
    72	  pages   = {094009},
    73	  year    = {2005},
    74	  doi     = {10.1103/PhysRevD.71.094009}
    75	}
    76	
    77	@article{LHCbAngular2020,
    78	  author  = {{LHCb Collaboration}},
    79	  title   = {Measurement of $\mathit{CP}$-averaged observables in the
    80	             $B^0 \to K^{*0} \mu^+ \mu^-$ decay},
    81	  journal = {Phys. Rev. Lett.},
    82	  volume  = {125},
    83	  pages   = {011802},
    84	  year    = {2020},
    85	  doi     = {10.1103/PhysRevLett.125.011802}
    86	}

 succeeded in 247ms:
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
    41	By design, the two witnesses share exactly the geometry-fixed
    42	operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
    43	$\Ph^{-2}$. They share no fitted parameter, threshold, dataset,
    44	or methodological choice above the operator level, and the
    45	empirical claims are tested on disjoint physical domains (flavour
    46	physics vs cortical neuroscience). Independence here is
    47	independence at the empirical layer above the shared operator,
    48	not statistical independence of the operator itself.
    49	
    50	\textbf{Operator-witness scope.} This is an operator witness, not
    51	a derivation of physics on either landing. We do not derive the
    52	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
    53	claim 600-cell uniqueness; alternative regular 4-polytopes are an
    54	explicit ablation build. We do not claim kernel uniqueness on
    55	either empirical landing; the b-anomaly's free-width Gaussian
    56	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
    57	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
    58	aria-chess substrate-witness scope is inherited verbatim. We do
    59	not deliver a selection theorem on the ACT
    60	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
    61	open builds (Lyapunov $V(W)$, edge-space decomposition under
    62	$2I$-equivariance, full reduced-flow convergence) remain open and
    63	are not delivered here.
    64	
    65	\textbf{Programme position.} The cascade-programme home for the
    66	polynomial-in-$L$ Lyapunov family — RH polynomial filter
    67	($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
    68	cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
    69	identified in \S\ref{sec:programme_home}. Family-membership is
    70	\emph{programme-positioned}, not formally classified. The two
    71	empirical landings strengthen external confidence in the
    72	\emph{response} primitive without reducing or addressing the
    73	selection gap.
    74	
    75	We are not aware of a prior preprint that simultaneously names a
    76	geometry-fixed Green operator on a fixed Coxeter graph, with a
    77	design-level mass shift not retuned between regimes, and threads
    78	two independent empirical landings on qualitatively distinct
    79	physical domains. We cannot rule out that such prior work exists.
    80	The empirical material gathered here is the operator witness; the
    81	broader programme to convert the witness into a selection-theorem-
    82	grade claim is sketched in the companion preprints and remains
    83	the natural next step.

codex
I have the kernel paper’s internal claims and line numbers. Next I’m checking the exact repro payload and the two source/companion documents to separate genuine mismatches from merely assertive wording.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/verify_kernel.py' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba docs/aria-closure-kernel.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 196ms:
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

 succeeded in 189ms:
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
    32	from scipy.sparse import csr_matrix
    33	from scipy.sparse.csgraph import connected_components
    34	
    35	
    36	PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
    37	INV_PHI = 1.0 / PHI                          # = phi - 1
    38	INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966
    39	
    40	
    41	# ---------------------------------------------------------------------------
    42	# 1. 600-cell vertex construction (120 vertices on S^3)
    43	# ---------------------------------------------------------------------------
    44	
    45	def even_perms(seq):
    46	    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    47	    n = len(seq)
    48	    out = []
    49	    for p in itertools.permutations(range(n)):
    50	        # signature
    51	        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    52	        if inv % 2 == 0:
    53	            out.append(tuple(seq[p[i]] for i in range(n)))
    54	    return out
    55	
    56	
    57	def build_v600():
    58	    """
    59	    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.
    60	
    61	    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    62	    - 16 vertices: all sign combinations of (+/- 1/2)^4
    63	    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
    64	      with all sign assignments
    65	    """
    66	    verts = set()
    67	
    68	    # 8 axis vertices
    69	    for sign in (-1, 1):
    70	        for i in range(4):
    71	            v = [0.0] * 4
    72	            v[i] = float(sign)
    73	            verts.add(tuple(v))
    74	
    75	    # 16 half-integer vertices
    76	    for signs in itertools.product((-1, 1), repeat=4):
    77	        v = tuple(0.5 * s for s in signs)
    78	        verts.add(v)
    79	
    80	    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    81	    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    82	    for signs in itertools.product((-1, 1), repeat=4):
    83	        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
    84	        signed = tuple(s * b for s, b in zip(signs, base))
    85	        for p in even_perms(signed):
    86	            verts.add(p)
    87	
    88	    V = np.array(sorted(verts), dtype=np.float64)
    89	    # Sanity check: all on the unit 3-sphere
    90	    radii = np.linalg.norm(V, axis=1)
    91	    assert np.allclose(radii, 1.0, atol=1e-10), \
    92	        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    93	    return V
    94	
    95	
    96	# ---------------------------------------------------------------------------
    97	# 2. Short-edge nearest-neighbour graph
    98	# ---------------------------------------------------------------------------
    99	
   100	def build_short_edge_graph(V, tol=1e-10):
   101	    """
   102	    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
   103	    criterion on the unit 3-sphere). For the 600-cell this gives a
   104	    12-regular graph on 120 vertices with 720 edges.
   105	    """
   106	    G = V @ V.T  # Gram matrix of inner products
   107	    short = PHI / 2.0
   108	    A = (np.abs(G - short) < tol).astype(np.float64)
   109	    np.fill_diagonal(A, 0.0)  # no self-loops
   110	    return A
   111	
   112	
   113	# ---------------------------------------------------------------------------
   114	# 3. Laplacian spectrum
   115	# ---------------------------------------------------------------------------
   116	
   117	def laplacian_spectrum(A):
   118	    """L = D - A; return sorted eigenvalues + eigenvectors."""
   119	    D = np.diag(A.sum(axis=1))
   120	    L = D - A
   121	    w, U = eigh(L)  # ascending order
   122	    return L, w, U
   123	
   124	
   125	def round_spectrum(w, decimals=6):
   126	    """Group eigenvalues into multiplicity classes (within numerical tol)."""
   127	    classes = []
   128	    seen = []
   129	    for val in w:
   130	        placed = False
   131	        for idx, ref in enumerate(seen):
   132	            if abs(val - ref) < 10 ** (-decimals):
   133	                classes[idx] = (ref, classes[idx][1] + 1)
   134	                placed = True
   135	                break
   136	        if not placed:
   137	            seen.append(val)
   138	            classes.append((round(float(val), decimals), 1))
   139	    return classes
   140	
   141	
   142	# ---------------------------------------------------------------------------
   143	# 4. Closure operator and discrete Green's function
   144	# ---------------------------------------------------------------------------
   145	
   146	def build_C_phi(L):
   147	    """C_phi = L + phi^-2 I."""
   148	    return L + INV_PHI2 * np.eye(L.shape[0])
   149	
   150	
   151	def green_response(C_phi, source_idx):
   152	    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
   153	    n = C_phi.shape[0]
   154	    f = np.zeros(n)
   155	    f[source_idx] = 1.0
   156	    psi = np.linalg.solve(C_phi, f)
   157	    return psi
   158	
   159	
   160	# ---------------------------------------------------------------------------
   161	# 5. Shell decomposition (9-shell H_3 partition)
   162	# ---------------------------------------------------------------------------
   163	
   164	def shell_indices(V, pole_idx):
   165	    """
   166	    Group vertices by their inner product with V[pole_idx]. The 600-cell's
   167	    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
   168	    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
   169	    """
   170	    pole = V[pole_idx]
   171	    inner = V @ pole
   172	    # The 9 canonical inner-product values:
   173	    canonical = np.array([
   174	        1.0,                # shell 0: pole itself
   175	        PHI / 2.0,          # shell 1
   176	        0.5,                # shell 2
   177	        1.0 / (2.0 * PHI),  # shell 3
   178	        0.0,                # shell 4 (equator)
   179	        -1.0 / (2.0 * PHI), # shell 5
   180	        -0.5,               # shell 6
   181	        -PHI / 2.0,         # shell 7
   182	        -1.0,               # shell 8: antipode
   183	    ])
   184	    shells = {k: [] for k in range(9)}
   185	    for i, val in enumerate(inner):
   186	        # snap to nearest canonical
   187	        k = int(np.argmin(np.abs(canonical - val)))
   188	        shells[k].append(i)
   189	    sizes = {k: len(shells[k]) for k in shells}
   190	    return shells, sizes, canonical
   191	
   192	
   193	# ---------------------------------------------------------------------------
   194	# 6. Discrete <-> continuum agreement test
   195	# ---------------------------------------------------------------------------
   196	
   197	def discrete_continuum_test(V, C_phi, source_idx):
   198	    """
   199	    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
   200	    shell radial coordinate x is the chord distance |v - v_source|. The
   201	    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).
   202	
   203	    Returns the per-shell discrete mean, the continuum prediction at each
   204	    shell radius, and the Pearson correlation between them.
   205	    """
   206	    psi = green_response(C_phi, source_idx)
   207	    shells, sizes, _ = shell_indices(V, source_idx)
   208	    pole = V[source_idx]
   209	
   210	    shell_means = []
   211	    shell_radii = []
   212	    shell_count = []
   213	    for k in range(9):
   214	        idxs = shells[k]
   215	        if not idxs:
   216	            continue
   217	        mean_psi = float(np.mean(psi[idxs]))
   218	        # mean chord radius from pole
   219	        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
   220	        shell_means.append(mean_psi)
   221	        shell_radii.append(chord)
   222	        shell_count.append(len(idxs))
   223	
   224	    shell_means = np.array(shell_means)
   225	    shell_radii = np.array(shell_radii)
   226	    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)
   227	
   228	    # Pearson correlation of (discrete shell mean) with (continuum prediction)
   229	    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
   230	        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
   231	    else:
   232	        corr = float("nan")
   233	
   234	    return {
   235	        "shell_radii": shell_radii.tolist(),
   236	        "shell_count": shell_count,
   237	        "shell_psi_mean": shell_means.tolist(),
   238	        "continuum_prediction": continuum.tolist(),
   239	        "pearson_correlation": corr,
   240	    }
   241	
   242	
   243	# ---------------------------------------------------------------------------
   244	# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
   245	# ---------------------------------------------------------------------------
   246	
   247	def cocycle_weights(V, source_idx):
   248	    """
   249	    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
   250	    the shell index of v with respect to a chosen pole. For the variant
   251	    test we compare the unweighted graph Laplacian to two weighted variants
   252	    discussed in the b-anomaly paper.
   253	    """
   254	    shells, _, _ = shell_indices(V, source_idx)
   255	    kappa = np.zeros(V.shape[0])
   256	    for k, idxs in shells.items():
   257	        for i in idxs:
   258	            kappa[i] = float(k)
   259	    return PHI ** kappa
   260	
   261	
   262	def weighted_laplacian(A, weights, mode="geometric"):
   263	    """
   264	    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
   265	    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
   266	    """
   267	    n = A.shape[0]
   268	    if mode == "geometric":
   269	        W = np.sqrt(np.outer(weights, weights))
   270	    elif mode == "arithmetic":
   271	        W = 0.5 * (weights[:, None] + weights[None, :])
   272	    else:
   273	        raise ValueError(mode)
   274	    A_w = A * W
   275	    D_w = np.diag(A_w.sum(axis=1))
   276	    return D_w - A_w
   277	
   278	
   279	def variant_correlation(V, A, source_idx, variant):
   280	    if variant == "UNWEIGHTED":
   281	        L_v = np.diag(A.sum(axis=1)) - A
   282	    else:
   283	        weights = cocycle_weights(V, source_idx)
   284	        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
   285	        L_v = weighted_laplacian(A, weights, mode=mode)
   286	    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
   287	    test = discrete_continuum_test(V, C_v, source_idx)
   288	    psi = green_response(C_v, source_idx)
   289	    pole = V[source_idx]
   290	    chord = np.linalg.norm(V - pole, axis=1)
   291	    # Continuum kernel at each vertex's chord radius
   292	    cont = (PHI / 2.0) * np.exp(-chord / PHI)
   293	    # Per-vertex correlation (excluding the source itself, which is degenerate)
   294	    mask = np.arange(V.shape[0]) != source_idx
   295	    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
   296	        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   297	    else:
   298	        per_vertex_corr = float("nan")
   299	    return {
   300	        "shell_mean_correlation": test["pearson_correlation"],
   301	        "per_vertex_correlation": per_vertex_corr,
   302	        "test": test,
   303	    }
   304	
   305	
   306	# ---------------------------------------------------------------------------
   307	# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
   308	# ---------------------------------------------------------------------------
   309	
   310	def connectivity_check(A):
   311	    """
   312	    Numerical connectedness verification: count connected components of the
   313	    short-edge adjacency matrix. Connectedness is reported, not derived from
   314	    a structural argument.
   315	    """
   316	    n_components, _ = connected_components(csr_matrix(A), directed=False)
   317	    return {
   318	        "n_connected_components": int(n_components),
   319	        "connected": bool(n_components == 1),
   320	    }
   321	
   322	
   323	def multi_source_sweep(V, C_phi):
   324	    """
   325	    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
   326	    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
   327	    predicts the correlation is invariant under choice of source vertex; this
   328	    function verifies the prediction numerically across all 120 sources and
   329	    reports the min/mean/max envelope.
   330	    """
   331	    n = V.shape[0]
   332	    corrs = np.zeros(n)
   333	    for source_idx in range(n):
   334	        psi = green_response(C_phi, source_idx)
   335	        chord = np.linalg.norm(V - V[source_idx], axis=1)
   336	        cont = (PHI / 2.0) * np.exp(-chord / PHI)
   337	        mask = np.arange(n) != source_idx
   338	        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   339	    return {
   340	        "n_sources": int(n),
   341	        "min_correlation": float(corrs.min()),
   342	        "mean_correlation": float(corrs.mean()),
   343	        "max_correlation": float(corrs.max()),
   344	        "max_minus_min": float(corrs.max() - corrs.min()),
   345	    }
   346	
   347	
   348	def operator_norm_check(L, w):
   349	    lam_min_L = float(w[0])           # 0
   350	    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
   351	    op_norm = 1.0 / lam_min_C         # phi^2
   352	    return {
   353	        "lambda_min_L": lam_min_L,
   354	        "lambda_min_C_phi": lam_min_C,
   355	        "operator_norm_C_phi_inv": op_norm,
   356	        "predicted_phi_squared": PHI ** 2,
   357	    }
   358	
   359	
   360	# ---------------------------------------------------------------------------
   361	# 9. Run everything and write results.json
   362	# ---------------------------------------------------------------------------
   363	
   364	def main():
   365	    out_path = Path(__file__).parent / "results.json"
   366	
   367	    V = build_v600()
   368	    n = V.shape[0]
   369	    A = build_short_edge_graph(V)
   370	    deg = A.sum(axis=1)
   371	    n_edges = int(A.sum() // 2)
   372	
   373	    L, w, U = laplacian_spectrum(A)
   374	    spectrum = round_spectrum(w, decimals=4)
   375	
   376	    C_phi = build_C_phi(L)
   377	    op_norm = operator_norm_check(L, w)
   378	    connectivity = connectivity_check(A)
   379	    multi_source = multi_source_sweep(V, C_phi)
   380	
   381	    # Pick the +x_0 axis vertex as canonical pole/source.
   382	    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
   383	    pole = V[pole_idx]
   384	
   385	    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)
   386	
   387	    test = discrete_continuum_test(V, C_phi, pole_idx)
   388	
   389	    # Variant comparison on the same source
   390	    variants = {}
   391	    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   392	        out = variant_correlation(V, A, pole_idx, variant)
   393	        variants[variant] = {
   394	            "shell_mean_correlation": out["shell_mean_correlation"],
   395	            "per_vertex_correlation": out["per_vertex_correlation"],
   396	        }
   397	
   398	    result = {
   399	        "phi": PHI,
   400	        "phi_inv_sq": INV_PHI2,
   401	        "n_vertices": n,
   402	        "n_edges": n_edges,
   403	        "degree_sequence": {
   404	            "min": int(deg.min()),
   405	            "max": int(deg.max()),
   406	            "mean": float(deg.mean()),
   407	        },
   408	        "connectivity": connectivity,
   409	        "shell_sizes": shell_sizes,
   410	        "shell_inner_products": canonical_inner.tolist(),
   411	        "antipodal_check": {
   412	            "pole_idx": pole_idx,
   413	            "antipode_idx": int(np.argmin(V @ pole)),
   414	            "expected_shell_8_size": 1,
   415	            "observed_shell_8_size": shell_sizes.get(8, 0),
   416	        },
   417	        "laplacian_spectrum_grouped": [
   418	            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
   419	        ],
   420	        "operator_norm": op_norm,
   421	        "discrete_continuum_test": test,
   422	        "variant_correlation": variants,
   423	        "multi_source_sweep": multi_source,
   424	    }
   425	
   426	    with open(out_path, "w") as f:
   427	        json.dump(result, f, indent=2)
   428	
   429	    # Headline summary
   430	    print("=" * 60)
   431	    print("ARIA Closure Kernel — verification")
   432	    print("=" * 60)
   433	    print(f"|V|           = {n}  (expected 120)")
   434	    print(f"|E|           = {n_edges}  (expected 720)")
   435	    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
   436	    print(f"connected      = {connectivity['connected']}  "
   437	          f"(components = {connectivity['n_connected_components']})")
   438	    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
   439	    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
   440	    print()
   441	    print("Laplacian spectrum (eigenvalue, multiplicity):")
   442	    for ev, m in spectrum:
   443	        print(f"  {ev:>8.4f}   x {m}")
   444	    print()
   445	    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
   446	    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
   447	    print()
   448	    print("Discrete <-> continuum agreement (Pearson correlation):")
   449	    print(f"  variant         | shell-mean  | per-vertex")
   450	    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   451	        sm = variants[v]["shell_mean_correlation"]
   452	        pv = variants[v]["per_vertex_correlation"]
   453	        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
   454	    print()
   455	    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
   456	    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
   457	    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
   458	    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
   459	    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
   460	    print()
   461	    print(f"Wrote {out_path}")
   462	
   463	
   464	if __name__ == "__main__":
   465	    main()

 succeeded in 180ms:
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

 succeeded in 249ms:
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
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/01_introduction.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/02_method.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 263ms:
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

 succeeded in 253ms:
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

 succeeded in 245ms:
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

 succeeded in 295ms:
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
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/05_results.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/06_stress_tests.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/07_cross_domain.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 197ms:
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

 succeeded in 204ms:
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

 succeeded in 201ms:
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

 succeeded in 195ms:
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
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/08_discussion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 296ms:
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

 succeeded in 308ms:
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

 succeeded in 335ms:
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

 succeeded in 328ms:
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
    15	  note         = {Accessed 2026-04-29}
    16	}
    17	
    18	@article{BeggsPlenz2003,
    19	  author  = {Beggs, John M. and Plenz, Dietmar},
    20	  title   = {Neuronal Avalanches in Neocortical Circuits},
    21	  journal = {Journal of Neuroscience},
    22	  volume  = {23},
    23	  number  = {35},
    24	  pages   = {11167--11177},
    25	  year    = {2003},
    26	  doi     = {10.1523/JNEUROSCI.23-35-11167.2003}
    27	}
    28	
    29	@article{Tononi2008,
    30	  author  = {Tononi, Giulio},
    31	  title   = {Consciousness as Integrated Information: a Provisional Manifesto},
    32	  journal = {Biological Bulletin},
    33	  volume  = {215},
    34	  number  = {3},
    35	  pages   = {216--242},
    36	  year    = {2008},
    37	  doi     = {10.2307/25470707}
    38	}
    39	
    40	@article{BalduzziTononi2008,
    41	  author  = {Balduzzi, David and Tononi, Giulio},
    42	  title   = {Integrated Information in Discrete Dynamical Systems: Motivation and Theoretical Framework},
    43	  journal = {PLoS Computational Biology},
    44	  volume  = {4},
    45	  number  = {6},
    46	  pages   = {e1000091},
    47	  year    = {2008},
    48	  doi     = {10.1371/journal.pcbi.1000091}
    49	}
    50	
    51	@book{Baars1988GWT,
    52	  author    = {Baars, Bernard J.},
    53	  title     = {A Cognitive Theory of Consciousness},
    54	  publisher = {Cambridge University Press},
    55	  year      = {1988},
    56	  address   = {Cambridge}
    57	}
    58	
    59	@book{Dehaene2014ConsciousAndBrain,
    60	  author    = {Dehaene, Stanislas},
    61	  title     = {Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts},
    62	  publisher = {Viking},
    63	  year      = {2014},
    64	  address   = {New York}
    65	}
    66	
    67	@article{FristonFreeEnergy2010,
    68	  author  = {Friston, Karl},
    69	  title   = {The Free-Energy Principle: a Unified Brain Theory?},
    70	  journal = {Nature Reviews Neuroscience},
    71	  volume  = {11},
    72	  number  = {2},
    73	  pages   = {127--138},
    74	  year    = {2010},
    75	  doi     = {10.1038/nrn2787}
    76	}
    77	
    78	@article{ClarkPP2013,
    79	  author  = {Clark, Andy},
    80	  title   = {Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science},
    81	  journal = {Behavioral and Brain Sciences},
    82	  volume  = {36},
    83	  number  = {3},
    84	  pages   = {181--204},
    85	  year    = {2013},
    86	  doi     = {10.1017/S0140525X12000477}
    87	}
    88	
    89	@article{Brodbeck2012Microstates,
    90	  author  = {Brodbeck, Verena and Kuhn, Andreas and von Wegner, Frederic and Morzelewski, Antoine and Tagliazucchi, Enzo and Borisov, Sergey and Michel, Christoph M. and Laufs, Helmut},
    91	  title   = {{EEG} microstates of wakefulness and {NREM} sleep},
    92	  journal = {NeuroImage},
    93	  volume  = {62},
    94	  number  = {3},
    95	  pages   = {2129--2139},
    96	  year    = {2012},
    97	  doi     = {10.1016/j.neuroimage.2012.05.060}
    98	}
    99	
   100	@article{VanEssen2013HCP,
   101	  author  = {Van Essen, David C. and Smith, Stephen M. and Barch, Deanna M. and Behrens, Timothy E. J. and Yacoub, Essa and Ugurbil, Kamil},
   102	  title   = {The {WU-Minn Human Connectome Project}: an Overview},
   103	  journal = {NeuroImage},
   104	  volume  = {80},
   105	  pages   = {62--79},
   106	  year    = {2013},
   107	  doi     = {10.1016/j.neuroimage.2013.05.041}
   108	}
   109	
   110	@article{PhysioNet2000,
   111	  author  = {Goldberger, Ary L. and Amaral, Luis A. N. and Glass, Leon and Hausdorff, Jeffrey M. and Ivanov, Plamen Ch. and Mark, Roger G. and Mietus, Joseph E. and Moody, George B. and Peng, Chung-Kang and Stanley, H. Eugene},
   112	  title   = {{PhysioBank, PhysioToolkit, and PhysioNet}: components of a new research resource for complex physiologic signals},
   113	  journal = {Circulation},
   114	  volume  = {101},
   115	  number  = {23},
   116	  pages   = {e215--e220},
   117	  year    = {2000},
   118	  doi     = {10.1161/01.CIR.101.23.e215}
   119	}
   120	
   121	@misc{SleepEDFx,
   122	  author       = {Kemp, Bob and Zwinderman, Aeilko H. and Tuk, Bert and Kamphuisen, Hilbert A. C. and Obery{\'e}, Josefien J. L.},
   123	  title        = {{Sleep-EDFx}: Sleep Cassette and Telemetry recordings},
   124	  howpublished = {PhysioNet},
   125	  year         = {2013},
   126	  note         = {Accessed 2026-04-29}
   127	}
   128	
   129	@misc{OpenNeuroDS005620,
   130	  author       = {Lichvar, Erin and others},
   131	  title        = {{OpenNeuro Dataset ds005620}: propofol-induced loss of consciousness {EEG}},
   132	  howpublished = {OpenNeuro},
   133	  year         = {2024},
   134	  doi          = {10.18112/openneuro.ds005620.v1.0.0}
   135	}
   136	
   137	@misc{OpenNeuroDS004902,
   138	  author       = {Timmermann, Christopher and others},
   139	  title        = {{OpenNeuro Dataset ds004902}: {DMT-induced} altered states of consciousness {EEG}},
   140	  howpublished = {OpenNeuro},
   141	  year         = {2023},
   142	  doi          = {10.18112/openneuro.ds004902.v1.0.8}
   143	}
   144	
   145	@misc{ZenodoDMT3992359,
   146	  author       = {Timmermann, Christopher},
   147	  title        = {{DMT EEG} dataset},
   148	  howpublished = {Zenodo},
   149	  year         = {2020},
   150	  doi          = {10.5281/zenodo.3992359}
   151	}
   152	
   153	@unpublished{SmartAdaptiveClosureTransport2026,
   154	  author = {Smart, Lee},
   155	  title  = {Adaptive Closure Transport: a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to selection},
   156	  year   = {2026},
   157	  note   = {VFD preprint, papers/adaptive-closure-transport/}
   158	}
   159	
   160	@unpublished{SmartAriaClosureKernel2026,
   161	  author = {Smart, Lee},
   162	  title  = {The 600-cell closure response kernel $C_\varphi = L + \varphi^{-2} I$ and its 9-shell projection},
   163	  year   = {2026},
   164	  note   = {VFD preprint, docs/aria-closure-kernel.md}
   165	}
   166	
   167	@unpublished{SmartBAnomaly2026,
   168	  author = {Smart, Lee},
   169	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
   170	  year   = {2026},
   171	  note   = {VFD preprint, papers/b-anomaly/}
   172	}
   173	
   174	@misc{ariaChessRepo,
   175	  author       = {Smart, Lee},
   176	  title        = {{ARIA-chess}: 600-cell substrate, recurrent self-model, and preregistered validation},
   177	  howpublished = {GitHub repository},
   178	  year         = {2026},
   179	  note         = {Accessed 2026-04-29}
   180	}

codex
The repro JSON matches the headline graph, spectrum, norm, and correlation numbers so far. I’m now scanning for scope creep and LaTeX/surface issues: wording like “selects,” “decisive,” “forced,” “derived,” plus macro/citation consistency.
exec
/bin/bash -lc 'rg -n "derive|derived|derivation|unique|uniqueness|selection|selects|decisive|theorem|forced|fixed by|load-bearing|preferred|wins|independent|AIC|Mode-B|Gaussian|Lyapunov|2I|equivariance|not delivered|post-hoc|retun|shape" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\Ph|\\\\Lop|\\\\Cph|\\\\Rsixhundred|C_\\\\varphi|V_\\{600\\}|varphi|φ|Phi|PHI|C_phi|L_\\{V_\\{600\\}\\}\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"citep\\{|ref\\{|label\\{|bibliograph|TODO|FIXME|undefined|??|ẑ|Krüger|σ|—|–|"'`|``|'"\\"'$'"\\"'$" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"97[6]?|0\\.976|0\\.923|0\\.888|0\\.884|2\\.618|720|120|degree|spectrum|12 - 6|12 - 4|4\\\\Ph|6\\\\Ph|shell\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/repro/results.json docs/aria-closure-kernel.md /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 204ms:
/bin/bash: -c: line 0: unexpected EOF while looking for matching ``'
/bin/bash: -c: line 1: syntax error: unexpected end of file

 exited 2 in 217ms:
rg: regex parse error:
    (?:\Ph|\Lop|\Cph|\Rsixhundred|C_\varphi|V_\{600\}|varphi|φ|Phi|PHI|C_phi|L_\{V_\{600\}\})
           ^^
error: unrecognized escape sequence

 succeeded in 259ms:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:5:This section threads the second independent empirical landing of
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:64:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:109:  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:119:$k=12$; no other shape parameter enters; the kernel shift
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:120:$\Ph^{-2}$ is not retuned. Under those design choices, the same
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:127:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:128:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:130:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:131:retuning between regimes — is the load-bearing object on both
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:139:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:140:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:151:Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:153:Kernel-shape free params & 0                            & 0 \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:155:Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:165:$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:166:is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:5:This section threads the first independent empirical landing of
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:14:Model, is approximately $q^{2}$-independent in the relevant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:16:shape with a fixed kernel
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:preprint's §3 derivation; we do not relitigate it here), and $A$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:26:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:28:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:41:dataset, kernel shape held fixed.}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:45:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:60:\item \textbf{Universality (5/5).} The same fixed kernel shape
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  unweighted choice wins on both a pure-geometry criterion
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:92:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:95:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:97:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:98:  to the universality / shape-prediction claim itself, but it is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:99:  decisive about whether the shape is forced by data: it is not.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:\item \textbf{Free-width Gaussian alternative.} A free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:101:  Gaussian charm-loop proxy fits the same five datasets comparably
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:103:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:104:\item \textbf{Mode-B drift (linearised-vs-nonlinear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:107:  the non-linear refit; the $+2.77$-AIC-unit drift between
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:  linearised and Mode-B (non-linear) refits is the largest single
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:114:  verified. The two-criterion agreement is criterion-independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:five independent measurements without shape retuning. This does
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:126:not establish the kernel as theorem-grade physics on the flavour
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:127:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:128:Mode-B linearised-vs-nonlinear refit drift prevent that). It does
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:131:independent empirical landings without parameter retuning. The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:8:\emph{response} primitive; \emph{selection} (which response
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:26:  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:44:formal classification theorem identifying the family.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:58:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:62:The selection layer is open. It appears as an open hypothesis in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:63:three independent frames:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:73:  $2I$-equivariance, and a full reduced-flow convergence theorem
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:77:  a selection theorem; ACT is positioned as the future
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:78:  selection-theorem witness.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:81:The recurrence of an open selection gap across these three frames
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:83:problem rather than three independent ones, but the present paper
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:86:primitive without reducing or addressing the selection gap.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:  the load-bearing object in two independent empirical works in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:116:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:119:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:120:  post-hoc motivated by the empirical landings; alternative regular
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:123:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:124:  b-anomaly free-width Gaussian alternative (fits comparably with
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:125:  one extra shape parameter) and the AIC tie
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:129:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:  convergence — all explicitly not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:131:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:133:\item \emph{Family-membership theorem.} The programme-home
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:134:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:18:fits on either empirical landing. The 600-cell choice is post-hoc
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:43:\textbf{The 600-cell choice is post-hoc justified by empirical
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
papers/aria-closure-kernel/paper/sections/09_limitations.tex:92:limit; a continuum limit theorem on H$_n$ Coxeter substrates as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:96:variant wins on both the geometry-only criterion of this paper
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:106:\textbf{Two independent empirical landings, not formal physics.}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:107:The b-anomaly result is a structural fit (kernel shape held fixed)
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:110:substrate \emph{is} consciousness). Neither lands a theorem-grade
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:136:\textbf{Selection layer not delivered.} As enumerated in
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
papers/aria-closure-kernel/paper/sections/09_limitations.tex:171:operator on a fixed graph, with no shape parameters tuned to any
papers/aria-closure-kernel/paper/sections/09_limitations.tex:172:dataset, is consistent with two independent empirical landings in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:16:Pearson $\rho = 0.976$ on the unweighted Laplacian, decisively
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:24:retuning between regimes, appears as the load-bearing object in:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:  fitted dimensionless amplitude $A$ per dataset (kernel shape
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:51:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:53:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:54:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:55:either empirical landing; the b-anomaly's free-width Gaussian
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:59:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:61:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:62:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:are not delivered here.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:66:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:selection gap.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:77:design-level mass shift not retuned between regimes, and threads
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:78:two independent empirical landings on qualitatively distinct
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:81:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/05_agreement.tex:5:This is the load-bearing geometric fact of the paper: the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:10:comparison that selects the unweighted Laplacian among the three
papers/aria-closure-kernel/paper/sections/05_agreement.tex:95:Laplacian wins on both criteria by a clear margin ($+0.088$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:99:independently against its data-$\chi^{2}$ criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:103:agree on which Laplacian variant is preferred. We do not claim
papers/aria-closure-kernel/paper/sections/05_agreement.tex:104:this is a uniqueness result; we report it as a two-criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:115:This is a non-trivial agreement between two independently-defined
papers/aria-closure-kernel/paper/sections/05_agreement.tex:122:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:124:Gaussian alternative that fits comparably in $\chi^{2}$ at the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:125:cost of one extra shape parameter, and the aria-chess preprint
papers/aria-closure-kernel/paper/sections/05_agreement.tex:128:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:59:artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:97:a load-bearing fact for any operator-witness claim made here. We
papers/aria-closure-kernel/paper/sections/03_substrate.tex:8:Laplacian. The choice of this polytope is post-hoc motivated by
papers/aria-closure-kernel/paper/sections/03_substrate.tex:10:construction itself is theorem-level rigorous in H$_4$ Coxeter
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:101:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:\item \textbf{Not fixed by this paper}: the choice of
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  Coxeter substrates. The 600-cell choice is post-hoc motivated by
papers/aria-closure-kernel/paper/sections/02_definition.tex:113:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:115:(1)--(3); we report this explicitly and treat formal derivation as
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:selection-layer dynamics over $W$-space that would, if delivered,
papers/aria-closure-kernel/paper/sections/02_definition.tex:120:constrain the shift further; that derivation is not delivered
papers/aria-closure-kernel/paper/main.tex:22:       independent empirical witnesses}
papers/aria-closure-kernel/paper/main.tex:45:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:56:same fixed graph is then the load-bearing object in two
papers/aria-closure-kernel/paper/main.tex:57:\emph{independent} empirical works: a passive-regime structural
papers/aria-closure-kernel/paper/main.tex:67:with two independent empirical landings under no shape-parameter
papers/aria-closure-kernel/paper/main.tex:68:retuning between regimes. It is \emph{not} a derivation of the
papers/aria-closure-kernel/paper/main.tex:69:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:71:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:74:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:83:fixed operator (no shape retuning) in two independent empirical
papers/aria-closure-kernel/paper/main.tex:98:tested variants the unweighted Laplacian wins on the geometry-only
papers/aria-closure-kernel/paper/main.tex:100:independently by b-anomaly's data $\chi^{2}$ comparison.
papers/aria-closure-kernel/paper/main.tex:126:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:133:shape held fixed. (b)~Active regime,
papers/aria-closure-kernel/paper/main.tex:143:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:145:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:147:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:148:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:150:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:153:graph appears as the load-bearing object in two independent
papers/aria-closure-kernel/paper/main.tex:154:empirical works in two distinct regimes, with no shape retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:5:A response operator on a fixed graph, with no shape parameters tuned
papers/aria-closure-kernel/paper/sections/01_introduction.tex:6:to any dataset, that simultaneously describes (i) the $q^{2}$ shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:14:without inheriting either's load-bearing claims. That is what this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:40:polytope is post-hoc motivated by the empirical landings
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:54:operator, on one fixed graph, with no shape-parameter retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:55:between regimes, appears as the load-bearing object in two
papers/aria-closure-kernel/paper/sections/01_introduction.tex:59:\item \textbf{Operator definition is fixed by the construction.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:61:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:72:  numerical agreement between two independently-defined objects (a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:75:\item \textbf{Variant comparison is decisive at the geometry-only
papers/aria-closure-kernel/paper/sections/01_introduction.tex:80:  Laplacian wins on the geometry-only criterion. This reproduces,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:82:  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
papers/aria-closure-kernel/paper/sections/01_introduction.tex:84:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
papers/aria-closure-kernel/paper/sections/01_introduction.tex:101:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:106:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:110:  is post-hoc motivated by the empirical landings; a formal
papers/aria-closure-kernel/paper/sections/01_introduction.tex:112:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:113:  landing.} The b-anomaly's free-width Gaussian alternative shows
papers/aria-closure-kernel/paper/sections/01_introduction.tex:114:  that a free-width Gaussian charm-loop proxy fits the same five
papers/aria-closure-kernel/paper/sections/01_introduction.tex:115:  datasets comparably in $\chi^{2}$ at the cost of one extra shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:116:  parameter; the b-anomaly AIC comparison against
papers/aria-closure-kernel/paper/sections/01_introduction.tex:121:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:124:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:  reduced flow, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  is not delivered here.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:155:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:156:selection'.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:in two independent empirical works (b-anomaly five-dataset
papers/aria-closure-kernel/paper/sections/01_introduction.tex:167:witness) without shape-parameter retuning between regimes.\par
papers/aria-closure-kernel/paper/sections/01_introduction.tex:168:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:170:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:for the polynomial-in-$L$ Lyapunov family that recurs across the

 exited 2 in 289ms:
rg: regex parse error:
    (?:97[6]?|0\.976|0\.923|0\.888|0\.884|2\.618|720|120|degree|spectrum|12 - 6|12 - 4|4\Ph|6\Ph|shell)
                                                                                        ^^^
error: Unicode property not found

exec
/bin/bash -lc "rg -n -F -e '\\Ph' -e '\\Lop' -e '\\Cph' -e '\\Rsixhundred' -e 'C_\\varphi' -e 'V_{600}' -e 'varphi' -e 'φ' -e 'Phi' -e 'PHI' -e 'C_phi' -e 'L_{V_{600}}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F -e '\\citep{' -e '\\ref{' -e '\\label{' -e '\\bibliograph' -e 'TODO' -e 'FIXME' -e 'undefined' -e '??' -e 'ẑ' -e 'Krüger' -e 'σ' -e '—' -e '–' -e '"'$$'"' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F -e '0.976' -e '0.923' -e '0.888' -e '0.884' -e '2.618' -e '720' -e '120' -e 'degree' -e 'spectrum' -e '12 - 6' -e '12 - 4' -e '4\\Ph' -e '6\\Ph' -e 'shell' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/repro/results.json docs/aria-closure-kernel.md /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F -e '17/18' -e '18/18' -e 'six' -e '6/6' -e 'seed 42' -e 'single deterministic' -e '0.463' -e '1.83' -e '0.066' -e '0.33' -e '2.252' -e '93.8' -e '40.6' -e '-4.4' -e '1003' -e '11.58' -e '79.78' -e '6.80' papers/aria-closure-kernel/paper/sections/07_active_witness.tex papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 246ms:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:(Table~\ref{tab:spectrum}). The discrete-to-continuum agreement
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:33:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:66:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:68:cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:69:identified in \S\ref{sec:programme_home}. Family-membership is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:68:  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:130:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:131:retuning between regimes — is the load-bearing object on both
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:141:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:146:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:70:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  on $W$-trajectories — \emph{none delivered} in that paper.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:75:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:99:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:107:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:110:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:111:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:127:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:  convergence — all explicitly not delivered
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:131:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
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
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:157:  Hodge edge Laplacian — open build of ACT.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:17:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:42:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:70:  explained by the predicted Krüger--Matias
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71:  $P/S$-basis amplification ($\sim 2.2$~\citep{KrugerMatias2005}).
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:82:  ranking — a two-criterion convergence on the same fixed
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:132:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:12:Table~\ref{tab:spectrum}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:21:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:63:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:76:(predicted) — match to six decimal places. The largest eigenvalue
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:82:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:90:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:34:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:49:precision — the within-shell standard deviations are at machine
papers/aria-closure-kernel/paper/sections/05_agreement.tex:57:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:82:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:98:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:102:correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
papers/aria-closure-kernel/paper/sections/05_agreement.tex:123:empirical landing — the b-anomaly paper documents a free-width
papers/aria-closure-kernel/paper/sections/05_agreement.tex:131:formal substrate ablation is an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:18:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:41:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:50:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:56:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:69:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:75:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:81:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:89:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:103:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:121:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:124:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  the empirical landings (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:130:  \S\ref{sec:active_witness}). A formal substrate ablation is an
papers/aria-closure-kernel/paper/sections/03_substrate.tex:131:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:18:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:28:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:49:alone — no external data input.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:83:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:85:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:91:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:123:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:127:  full reduced-flow convergence — is left open in that paper and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:140:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/01_introduction.tex:178:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:182:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:185:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:190:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:191:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:47:outside this class — projected coordinates with non-standard
papers/aria-closure-kernel/paper/sections/02_definition.tex:49:or operators with negative spectrum — require their own analysis,
papers/aria-closure-kernel/paper/sections/02_definition.tex:52:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:68:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{sec:agreement}); this matches the closed-form $\Ph^{2}$ to
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:96:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:116:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/sections/02_definition.tex:118:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/main.tex:45:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:54:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:59:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:62:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:72:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:86:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:88:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:116:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:127:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:134:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:177:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:178:\S\ref{sec:agreement} are deterministic outputs of the script.
papers/aria-closure-kernel/paper/main.tex:180:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:181:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/main.tex:184:\bibliographystyle{plainnat}
papers/aria-closure-kernel/paper/main.tex:185:\bibliography{references}

 succeeded in 253ms:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:5:This section positions $\Cph$ within the broader cascade programme
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:7:matters for the hostile-review reading: $\Cph$ is the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:family as $\Cph$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:30:  programme-positioned as a $\Cph$-style mass-regularised Laplacian
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:48:The closure response $\psi = \Cph^{-1} f$ is determined by the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:50:shift $\Ph^{-2}$, and the response is the resulting linear inverse.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:55:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\item The operator $\Cph$ is well-defined and positive definite
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:94:  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:98:  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:107:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:116:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:82:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:117:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:120:$\Ph^{-2}$ is not retuned. Under those design choices, the same
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:121:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:130:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:139:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:140:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:149:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:151:Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:161:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:162:the same shift $\Ph^{-2}$. They share no fitted parameter,
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
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
papers/aria-closure-kernel/paper/sections/05_agreement.tex:8:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
papers/aria-closure-kernel/paper/sections/05_agreement.tex:11:tested variants (unweighted, $\Ph$-geometric weighted,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:12:$\Ph$-arithmetic weighted).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:20:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:26:G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:31:trivially the diagonal of $\Cph^{-1}$ and the chord distance is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:59:Two $\Ph$-cocycle weighted Laplacian variants are tested as
papers/aria-closure-kernel/paper/sections/05_agreement.tex:63:\item \textbf{$\Ph$-geometric weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:65:  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:67:\item \textbf{$\Ph$-arithmetic weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:79:discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
papers/aria-closure-kernel/paper/sections/05_agreement.tex:88:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:89:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:114:closed-form continuum exponential at the same length scale $\Ph$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:118:exponential. The $\Ph$-mediated agreement is an empirical fact
papers/aria-closure-kernel/paper/sections/05_agreement.tex:128:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:20:A \cdot \kappa_{V_{600}}(q^{2}),
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:where $\kappa_{V_{600}}(q^{2})$ is derived from $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:23:$\Rsixhundred$ via a discrete-to-momentum projection (the b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:26:shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:28:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:76:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:77:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:129:establish, at the operator level, that the same fixed $\Cph$ on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:130:the same fixed $\Rsixhundred$ is consistent with one of two
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:17:$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
papers/aria-closure-kernel/paper/sections/03_substrate.tex:26:\item \textbf{$\Ph$-mixed orbit} ($96$ vertices): all even
papers/aria-closure-kernel/paper/sections/03_substrate.tex:27:  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:28:  $\Ph^{2} = \Ph + 1$ identity, equivalently
papers/aria-closure-kernel/paper/sections/03_substrate.tex:29:  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:43:For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:48:The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
papers/aria-closure-kernel/paper/sections/03_substrate.tex:51:\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:54:$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:59:The graph $G_{V_{600}}$ has:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:84:\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:85:       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:109:is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:112:inner product exactly $\Ph/2$ within machine precision (tolerance
papers/aria-closure-kernel/paper/sections/03_substrate.tex:118:\item \textbf{Fixed by the construction once $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:122:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:123:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:125:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:8:on the substrate $(M, L_M)$, with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:12:Laplacian spectrum with closed-form values in $\mathbb{Z}[\Ph]$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:14:between $\psi = \Cph^{-1} f$ and the continuum kernel
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:15:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex chord distances is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:above the $\Ph$-cocycle weighted variants ($0.888$ geometric,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:42:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:43:$\Ph^{-2}$. They share no fitted parameter, threshold, dataset,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:52:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\qquad \Ph \;=\; (1+\sqrt 5)/2,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:24:$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
papers/aria-closure-kernel/paper/sections/01_introduction.tex:25:non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
papers/aria-closure-kernel/paper/sections/01_introduction.tex:26:positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:32:Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:36:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
papers/aria-closure-kernel/paper/sections/01_introduction.tex:39:short edges $\langle v, w\rangle = \Ph/2$. The choice of this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:46:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:60:  Once $\Rsixhundred$ is selected and the stability shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:61:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:69:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:76:  criterion.} Two $\Ph$-cocycle weighted Laplacian variants
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  ($\Ph$-geometric, $\Ph$-arithmetic edge weights via shell-grade
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  exponents $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:86:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:92:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:101:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:102:  $\Ph^{-2}$ is a design-level stability clamp that bounds
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:106:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:109:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:124:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:131:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:168:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:183:in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5:The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$ has
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:$\mathbb{Z}[\Ph]$ and multiplicities summing to $|V| = 120$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:17:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
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
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:63:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:72:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:75:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:of $\Cph$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:79:= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:84:The eigenspaces of $\Lop$ partition into H$_4$-proper and
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:87:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
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
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\S\ref{sec:agreement}); this matches the closed-form $\Ph^{2}$ to
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
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:  has decay scale $\Ph$, not a free length parameter.
papers/aria-closure-kernel/paper/sections/02_definition.tex:113:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with graph
papers/aria-closure-kernel/paper/main.tex:42:Laplacian $L_M$ and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
papers/aria-closure-kernel/paper/main.tex:43:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:49:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:50:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:51:eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:54:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:55:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:69:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:70:claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
papers/aria-closure-kernel/paper/main.tex:79:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:81:$\Ph = (1+\sqrt 5)/2$, give its canonical instance on the 600-cell
papers/aria-closure-kernel/paper/main.tex:82:graph $\Rsixhundred$, and document its appearance as the same
papers/aria-closure-kernel/paper/main.tex:90:(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
papers/aria-closure-kernel/paper/main.tex:93:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:94:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:96:unweighted variant, above the two $\Ph$-cocycle weighted variants
papers/aria-closure-kernel/paper/main.tex:103:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:105:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:106:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:108:$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
papers/aria-closure-kernel/paper/main.tex:111:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:113:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:115:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:120:$\psi = \Cph^{-1} f$ for a localised source and the continuum
papers/aria-closure-kernel/paper/main.tex:123:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:128:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:134:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:135:$\Rsixhundred$, augmented by a recurrent self-model layer with one
papers/aria-closure-kernel/paper/main.tex:143:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:144:stability clamp making $\Cph$ strictly positive definite. We do
papers/aria-closure-kernel/paper/main.tex:145:not claim $\Rsixhundred$ is the unique substrate consistent with

 succeeded in 260ms:
papers/aria-closure-kernel/paper/main.tex:46:numerically reproduced: $|V|=120$, $|E|=720$, uniform
papers/aria-closure-kernel/paper/main.tex:47:degree~$12$, H$_3$ shell decomposition
papers/aria-closure-kernel/paper/main.tex:48:$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
papers/aria-closure-kernel/paper/main.tex:52:agreement at per-vertex Pearson correlation $0.976$ between the
papers/aria-closure-kernel/paper/main.tex:92:($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
papers/aria-closure-kernel/paper/main.tex:93:Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
papers/aria-closure-kernel/paper/main.tex:94:$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:95:agreement at per-vertex Pearson correlation $0.976$ for the
papers/aria-closure-kernel/paper/main.tex:97:tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
papers/aria-closure-kernel/paper/main.tex:106:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:111:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:113:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:115:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:116:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:122:distance: $0.976$ (unweighted Laplacian), $0.888$
papers/aria-closure-kernel/paper/main.tex:123:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:139:degree, passes eighteen preregistered correspondences (frozen
papers/aria-closure-kernel/paper/main.tex:162:\input{sections/04_spectrum.tex}
papers/aria-closure-kernel/paper/main.tex:173:short-edge graph build, Laplacian spectrum, operator-norm bound,
papers/aria-closure-kernel/paper/main.tex:177:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:36:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:42:rigorous. The graph has $|E|=720$ edges, uniform degree~$12$ by
papers/aria-closure-kernel/paper/sections/01_introduction.tex:43:H$_4$ transitivity, a $9$-shell H$_3$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:45:$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
papers/aria-closure-kernel/paper/sections/01_introduction.tex:46:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:63:  operator. The Laplacian spectrum, the operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:71:  $\rho = 0.976$ on the unweighted graph Laplacian. This is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:73:  120-dimensional discrete inverse and a continuum exponential
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  ($\Ph$-geometric, $\Ph$-arithmetic edge weights via shell-grade
papers/aria-closure-kernel/paper/sections/01_introduction.tex:79:  correlation: $0.888$ and $0.884$ respectively. The unweighted
papers/aria-closure-kernel/paper/sections/01_introduction.tex:107:  regular 4-polytopes (the $24$-cell, the $120$-cell), other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:150:A numerically computed quantity (the Laplacian spectrum, the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:151:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:163:600-cell graph, with computed spectrum, operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:181:canonical generators, gives the graph facts, and the $9$-shell
papers/aria-closure-kernel/paper/sections/01_introduction.tex:182:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:12:Laplacian spectrum with closed-form values in $\mathbb{Z}[\Ph]$
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:(Table~\ref{tab:spectrum}). The discrete-to-continuum agreement
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:16:Pearson $\rho = 0.976$ on the unweighted Laplacian, decisively
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:above the $\Ph$-cocycle weighted variants ($0.888$ geometric,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:$0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:  degree) passes eighteen preregistered cortical correspondences
papers/aria-closure-kernel/paper/sections/09_limitations.tex:15:whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:26:$120$-cell, with the same per-vertex correlation criterion
papers/aria-closure-kernel/paper/sections/09_limitations.tex:49:or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:127:sweeps over all $120$ vertices: every source returns the same
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:21:  this programme). Cascade closure functional on $\mathbb{R}^{120}$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:25:  degree-$10$ positive functional vanishing exactly on
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:54:  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:105:  correlation $0.976$ on the unweighted variant, with the unweighted
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:24:  average degree.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:27:  AR(1) noise + tonic shell + attention episodes for WAKE,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:105:  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:107:  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:108:  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:118:substrate-pinned nonlinearity at the graph's average degree
papers/aria-closure-kernel/repro/results.json:4:  "n_vertices": 120,
papers/aria-closure-kernel/repro/results.json:5:  "n_edges": 720,
papers/aria-closure-kernel/repro/results.json:6:  "degree_sequence": {
papers/aria-closure-kernel/repro/results.json:15:  "shell_sizes": {
papers/aria-closure-kernel/repro/results.json:26:  "shell_inner_products": [
papers/aria-closure-kernel/repro/results.json:40:    "expected_shell_8_size": 1,
papers/aria-closure-kernel/repro/results.json:41:    "observed_shell_8_size": 1
papers/aria-closure-kernel/repro/results.json:43:  "laplacian_spectrum_grouped": [
papers/aria-closure-kernel/repro/results.json:84:    "operator_norm_C_phi_inv": 2.618033988749902,
papers/aria-closure-kernel/repro/results.json:85:    "predicted_phi_squared": 2.618033988749895
papers/aria-closure-kernel/repro/results.json:88:    "shell_radii": [
papers/aria-closure-kernel/repro/results.json:99:    "shell_count": [
papers/aria-closure-kernel/repro/results.json:110:    "shell_psi_mean": [
papers/aria-closure-kernel/repro/results.json:132:    "pearson_correlation": 0.9232082699765517
papers/aria-closure-kernel/repro/results.json:136:      "shell_mean_correlation": 0.9232082699765517,
papers/aria-closure-kernel/repro/results.json:137:      "per_vertex_correlation": 0.9762022978516623
papers/aria-closure-kernel/repro/results.json:140:      "shell_mean_correlation": 0.879553132802029,
papers/aria-closure-kernel/repro/results.json:141:      "per_vertex_correlation": 0.8883800503732451
papers/aria-closure-kernel/repro/results.json:144:      "shell_mean_correlation": 0.8784315463215415,
papers/aria-closure-kernel/repro/results.json:145:      "per_vertex_correlation": 0.8843640031310793
papers/aria-closure-kernel/repro/results.json:149:    "n_sources": 120,
papers/aria-closure-kernel/repro/results.json:150:    "min_correlation": 0.9762022978516617,
papers/aria-closure-kernel/repro/results.json:151:    "mean_correlation": 0.9762022978516628,
papers/aria-closure-kernel/repro/results.json:152:    "max_correlation": 0.9762022978516637,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:38:\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:39:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:40:  (averaging $\psi(v)$ over each H$_3$ shell first, then
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:  correlating the $9$-point shell-mean trajectory with the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:42:  continuum prediction at the shell mean radius).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:46:(every non-source vertex), while shell-mean tests at $9$ data
papers/aria-closure-kernel/paper/sections/05_agreement.tex:47:points (one per shell). On the unweighted 600-cell graph with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:48:an H$_3$-fixed source, $\psi$ is shell-constant up to numerical
papers/aria-closure-kernel/paper/sections/05_agreement.tex:49:precision — the within-shell standard deviations are at machine
papers/aria-closure-kernel/paper/sections/05_agreement.tex:52:shell by its multiplicity ($\{12, 20, 12, 30, 12, 20, 12, 1\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:53:for the non-source shells) and excludes the source vertex,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:54:while the shell-mean test gives equal weight to every shell. The
papers/aria-closure-kernel/paper/sections/05_agreement.tex:66:  is the shell index of $v$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:78:\caption{Per-vertex and shell-mean Pearson correlations between the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:87:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:88:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:89:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:96:per-vertex over the next variant, $+0.043$ shell-mean). This
papers/aria-closure-kernel/paper/sections/05_agreement.tex:113:to within the per-vertex Pearson correlation $0.976$, like the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:116:objects: (i) the discrete inverse of a $120\times 120$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:129:property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:$\mathbb{Z}[\Ph]$ and multiplicities summing to $|V| = 120$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:spectrum is computed numerically by
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:9:\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:10:$120\times 120$ symmetric eigendecomposition, deterministic at
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:12:Table~\ref{tab:spectrum}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:17:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:20:sum to $120$.}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:21:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:27:$12 - 6\Ph$    & $2.2918$  & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:28:$12 - 4\Ph$    & $5.5279$  & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:32:$4\Ph + 8$     & $14.4721$ & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:34:$6\Ph + 6$     & $15.7082$ & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:36:\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:43:12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:44:12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:45:4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:46:6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:48:The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:49:$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:57:$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:58:remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:61:that the spectrum has this structure.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:72:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:75:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:17:$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
papers/aria-closure-kernel/paper/sections/03_substrate.tex:31:The total is $8 + 16 + 96 = 120$ unit vectors. Reproduced by
papers/aria-closure-kernel/paper/sections/03_substrate.tex:37:$120$ vertices. Every vertex therefore has \emph{identical} local
papers/aria-closure-kernel/paper/sections/03_substrate.tex:39:degree in the short-edge graph defined below.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:61:\item $|V|=120$ vertices,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:62:\item $|E|=720$ edges,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:63:\item every vertex has degree exactly $12$ (H$_4$ transitivity on
papers/aria-closure-kernel/paper/sections/03_substrate.tex:72:\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:73:degree-min/max $=12/12$ (uniform), and one connected component.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:75:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:78:fixing $v_{0}$ partitions the remaining $119$ vertices into shells
papers/aria-closure-kernel/paper/sections/03_substrate.tex:81:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:87:indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:88:antipode. The shell-size sequence is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:89:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:The middle shell $S_{4}$ has $30$ equatorial vertices forming the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:96:$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
papers/aria-closure-kernel/paper/sections/03_substrate.tex:97:verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:100:shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:101:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:106:the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
papers/aria-closure-kernel/paper/sections/03_substrate.tex:107:are jointly consistent: a vertex in shell $s_{1}$ is connected to a
papers/aria-closure-kernel/paper/sections/03_substrate.tex:108:vertex in shell $s_{2}$ if and only if their pairwise inner product
papers/aria-closure-kernel/paper/sections/03_substrate.tex:119:  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
papers/aria-closure-kernel/paper/sections/03_substrate.tex:121:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/02_definition.tex:49:or operators with negative spectrum — require their own analysis,
papers/aria-closure-kernel/paper/sections/02_definition.tex:71:              \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/02_definition.tex:77:Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
docs/aria-closure-kernel.md:37:Laplacians with negative spectrum) require their own analysis.
docs/aria-closure-kernel.md:52:- 120 vertices, 720 edges, each vertex degree 12;
docs/aria-closure-kernel.md:54:- 9-shell decomposition emerging intrinsically as
docs/aria-closure-kernel.md:70:fits do not use the truncation. (The canonical full spectrum of
docs/aria-closure-kernel.md:73:not consistent with the canonical spectrum or with the b-anomaly's
docs/aria-closure-kernel.md:160:response operator and the 9-shell projection (which enters at the
docs/aria-closure-kernel.md:161:shell-mean step, not as an edge weight); it does **not**
docs/aria-closure-kernel.md:168:shell-grade pattern $\varphi^{0,1,4,9,16}$ shows up in both the
docs/aria-closure-kernel.md:170:This is a theoretical convergence on a shared algebraic shell-grade
docs/aria-closure-kernel.md:173:$V_{600} + \varphi^{-2} I$, the same 9-shell decomposition, the
docs/aria-closure-kernel.md:174:same shell-grade pattern $\varphi^{0,1,4,9,16}$); ẑ does **not**
docs/aria-closure-kernel.md:191:  degree-$10$ positive functional on $\R^{120}$ vanishing exactly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:44:| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |

 succeeded in 274ms:
papers/aria-chess-paper/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
papers/aria-chess-paper/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
papers/aria-chess-paper/paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:25:propofol continuity drop $+0.066$; propofol integrated-information
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:61:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
papers/aria-chess-paper/paper/sections/10_conclusion.tex:66:conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
papers/aria-chess-paper/paper/sections/10_conclusion.tex:69:on the full-cohort descriptive HCP $n\!=\!1003$ statistics
papers/aria-chess-paper/paper/sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
papers/aria-chess-paper/paper/sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
papers/aria-chess-paper/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
papers/aria-chess-paper/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:19:$k_{\mathrm{thr}}=12$, single deterministic substrate
papers/aria-chess-paper/paper/sections/05_results.tex:28:seed 42).}
papers/aria-chess-paper/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:46:\label{tab:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:76:on the same deterministic substrate trajectory. The six signatures
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:122:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:152:  without state reset on a state-drifted substrate, and $+40.6$pp
papers/aria-chess-paper/paper/sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
papers/aria-chess-paper/paper/sections/05_results.tex:207:(noting that the v4 WAKE CI is from a single deterministic trajectory
papers/aria-chess-paper/paper/sections/08_discussion.tex:25:  on three reference ranges; six drug/sleep signatures pass at
papers/aria-chess-paper/paper/sections/08_discussion.tex:26:  literature-derived thresholds on a single deterministic substrate.
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
papers/aria-chess-paper/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:143:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
papers/aria-chess-paper/paper/sections/08_discussion.tex:191:\item Do the six drug/sleep signatures replicate across $10$--$20$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:47:$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:90:reset; we report the LOO finding ($+40.6$pp) above as a disclosed
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:96:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:133:P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:141:lift is $-4.4$pp, well within the preregistered neutrality band
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:158:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:160:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:172:$n=1003$ descriptive statistics.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
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
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
papers/aria-chess-paper/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
papers/aria-chess-paper/paper/sections/09_limitations.tex:22:$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
papers/aria-chess-paper/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
papers/aria-chess-paper/paper/sections/09_limitations.tex:28:a single deterministic trajectory at seed $42$. Empirical CIs across
papers/aria-chess-paper/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
papers/aria-chess-paper/paper/sections/09_limitations.tex:59:observables.} While the construction of $\Rsixhundred$ is theorem-
papers/aria-chess-paper/paper/sections/09_limitations.tex:65:preregistered correspondences plus six signatures; the H$_4$
papers/aria-chess-paper/paper/sections/09_limitations.tex:97:we claim quantitative consistency with six published biological
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
papers/aria-chess-paper/paper/sections/09_limitations.tex:172:\item Selection theorem for $\Rsixhundred$ over alternative regular
papers/aria-chess-paper/paper/sections/09_limitations.tex:175:  of the six signatures.
papers/aria-chess-paper/paper/sections/09_limitations.tex:189:eighteen preregistered correspondences and six companion drug/sleep
papers/aria-chess-paper/paper/sections/09_limitations.tex:194:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:108:drop $+0.066$).
papers/aria-chess-paper/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
papers/aria-chess-paper/paper/sections/03_substrate.tex:155:cascade is a decomposition of operators on $\Rsixhundred$, and the
papers/aria-chess-paper/paper/sections/03_substrate.tex:156:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
papers/aria-chess-paper/paper/sections/03_substrate.tex:162:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
papers/aria-chess-paper/paper/sections/03_substrate.tex:168:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
papers/aria-chess-paper/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
papers/aria-chess-paper/paper/sections/02_method.tex:112:computational tractability; full-cohort $n=1003$ statistics
papers/aria-chess-paper/paper/sections/02_method.tex:161:on the full $n=1003$ subject distribution.
papers/aria-chess-paper/paper/sections/02_method.tex:174:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
papers/aria-chess-paper/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
papers/aria-chess-paper/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
papers/aria-chess-paper/paper/sections/01_introduction.tex:30:against eighteen preregistered correspondences plus six companion
papers/aria-chess-paper/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
papers/aria-chess-paper/paper/sections/01_introduction.tex:42:\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:58:\item \textbf{Six drug/sleep signatures.} On a single deterministic
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:71:  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
papers/aria-chess-paper/paper/sections/01_introduction.tex:72:  conversation $-4.4$pp lift, within preregistered neutrality bounds)
papers/aria-chess-paper/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
papers/aria-chess-paper/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
papers/aria-chess-paper/paper/sections/01_introduction.tex:130:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
papers/aria-chess-paper/paper/sections/01_introduction.tex:161:\S\ref{sec:results} reports the empirical tables: six drug/sleep
papers/aria-chess-paper/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-chess-paper/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
papers/aria-chess-paper/paper/main.tex:48:it, this single deterministic structure is consistent with eighteen
papers/aria-chess-paper/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
papers/aria-chess-paper/paper/main.tex:52:literature-derived thresholds on a single deterministic substrate
papers/aria-chess-paper/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
papers/aria-chess-paper/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:85:additionally report six drug/sleep EEG signatures tested on a recurrent
papers/aria-chess-paper/paper/main.tex:86:self-model layer above the substrate, on a single deterministic
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:113:on the single deterministic substrate trajectory.
papers/aria-chess-paper/paper/main.tex:132:8-dimensional V2 features lifts $+40.6$ percentage points on
papers/aria-chess-paper/paper/main.tex:134:$\to$ substrate-routed $93.8\%$, with state reset; the
papers/aria-chess-paper/paper/main.tex:138:classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
papers/aria-chess-paper/paper/main.tex:143:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
papers/aria-chess-paper/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
papers/aria-chess-paper/paper/main.tex:160:is reported on a single deterministic trajectory; cross-seed CIs on
papers/aria-chess-paper/paper/main.tex:165:correspondences and six drug/sleep EEG signatures, with all gaps in
papers/aria-chess-paper/paper/main.tex:199:The complete pipeline (substrate construction, six-signature
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:49:\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:62:On a single deterministic substrate trajectory at seed~$42$, the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:63:aria-chess preprint reports six biological signatures testing
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:67:\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:75:  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:76:\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:79:\item \textbf{Propofol continuity drop}: $+0.066$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:94:  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:95:  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:98:  substrate-routed lift $-4.4$pp (within the preregistered
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:104:  full-cohort descriptive statistics on $n=1003$ subjects show
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:105:  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:106:  homogeneity, $+79.78\sigma$ on raw participation ratio (with
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:108:  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:109:  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:121:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:122:preregistered cortical correspondences (frozen 2026-04-18) and six
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:140:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:152:Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:161:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and

codex
There are a few wording candidates that are not numerical errors but do affect referee confidence, especially “decisive,” “selects,” and a section-reference ambiguity. I’m also doing a compile-style sanity check into `/tmp` so any broken LaTeX or missing citations are caught without touching the manuscript directory.
exec
/bin/bash -lc 'command -v tectonic' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'command -v latexmk' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'command -v pdflatex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'command -v chktex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 279ms:
/home/nexusloq/.local/bin/tectonic

 exited 1 in 325ms:
 exited 1 in 336ms:
 exited 1 in 453ms:
exec
/bin/bash -lc "tectonic -X compile --outdir /tmp /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper
 exited 1 in 7189ms:
note: "version 2" Tectonic command-line interface activated
note: Running TeX ...
warning: sections/01_introduction.tex:96: Overfull \hbox (4.6799pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
note: Running BibTeX on main.aux ...
note: warnings were issued by BibTeX; use --print and/or --keep-logs for details.
note: Rerunning TeX because bibtex was run ...
warning: sections/01_introduction.tex:96: Overfull \hbox (2.249pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
note: Rerunning TeX because "main.aux" changed ...
warning: main.tex:101: Overfull \hbox (11.61586pt too wide) in paragraph at lines 79--101
warning: sections/01_introduction.tex:96: Overfull \hbox (25.53964pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
note: Rerunning TeX because "main.aux" changed ...
warning: main.tex:101: Overfull \hbox (11.61586pt too wide) in paragraph at lines 79--101
warning: sections/01_introduction.tex:96: Overfull \hbox (25.53964pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
warning: internal consistency problem when checking if main.bbl changed
note: Rerunning TeX because "main.bbl" changed ...
warning: main.tex:101: Overfull \hbox (11.61586pt too wide) in paragraph at lines 79--101
warning: sections/01_introduction.tex:96: Overfull \hbox (25.53964pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
warning: internal consistency problem when checking if main.bbl changed
note: Rerunning TeX because "main.bbl" changed ...
warning: main.tex:101: Overfull \hbox (11.61586pt too wide) in paragraph at lines 79--101
warning: sections/01_introduction.tex:96: Overfull \hbox (25.53964pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
note: Rerunning TeX because "main.bbl" changed ...
warning: internal consistency problem when checking if main.bbl changed
warning: main.tex:101: Overfull \hbox (11.61586pt too wide) in paragraph at lines 79--101
warning: sections/01_introduction.tex:96: Overfull \hbox (25.53964pt too wide) in paragraph at lines 84--96
warning: sections/01_introduction.tex:149: Overfull \hbox (14.86632pt too wide) detected at line 149
warning: sections/02_definition.tex:81: Overfull \hbox (17.93068pt too wide) in paragraph at lines 76--81
warning: sections/03_substrate.tex:35: Overfull \hbox (7.8411pt too wide) in paragraph at lines 31--35
warning: sections/07_active_witness.tex:20: Overfull \hbox (15.98984pt too wide) in paragraph at lines 16--20
warning: sections/07_active_witness.tex:153: Underfull \hbox (badness 10000) in paragraph at lines 153--153
warning: sections/07_active_witness.tex:158: Overfull \hbox (8.68645pt too wide) in paragraph at lines 142--158
warning: sections/08_programme_home.tex:108: Overfull \hbox (2.23352pt too wide) in paragraph at lines 104--108
warning: sections/08_programme_home.tex:133: Overfull \hbox (15.37508pt too wide) in paragraph at lines 128--133
warning: sections/10_conclusion.tex:21: Overfull \hbox (33.23872pt too wide) in paragraph at lines 5--21
note: Running xdvipdfmx ...
warning: internal consistency problem when checking if main.bbl changed
warning: TeX rerun seems needed, but stopping at 6 passes
warning: warnings were issued by the TeX engine; use --print and/or --keep-logs for details.
note: Writing `/tmp/main.pdf` (196.95 KiB)
error: Read-only file system (os error 30)

exec
/bin/bash -lc 'ls -l /tmp/main.*' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,220p' /tmp/main.blg" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,240p' /tmp/main.log" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 265ms:
sed: can't read /tmp/main.log: No such file or directory

 exited 2 in 274ms:
sed: can't read /tmp/main.blg: No such file or directory

 exited 2 in 301ms:
ls: cannot access '/tmp/main.*': No such file or directory

exec
/bin/bash -lc "rg -o \"citep\\{["'^}]+'"\\}\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "''^@" papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\S\\\\ref\\{ssec:opnorm\\}|ssec:opnorm|ssec:graph|ssec:regime|ssec:interpretation|ssec:posthoc\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\paragraph\\{|\\\\subsection\\{|\\\\section\\{\" papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 267ms:
1:@book{CoxeterRegularPolytopes,
10:@misc{Weisstein600Cell,
18:@article{ChungSpectralGraph,
27:@book{HumphreysReflectionGroups,
38:@unpublished{SmartBAnomaly2026,
46:@unpublished{SmartAriaChess2026,
55:@unpublished{SmartAdaptiveClosureTransport2026,
66:@article{KrugerMatias2005,
77:@article{LHCbAngular2020,

 succeeded in 306ms:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:citep{LHCbAngular2020}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:citep{KrugerMatias2005}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/02_definition.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:citep{CoxeterRegularPolytopes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:citep{CoxeterRegularPolytopes}
papers/aria-closure-kernel/paper/main.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/main.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:citep{SmartAriaChess2026}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:citep{SmartAdaptiveClosureTransport2026}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:citep{SmartAriaChess2026}

 exited 2 in 346ms:
rg: regex parse error:
    (?:\paragraph\{|\subsection\{|\section\{)
       ^^^
error: Unicode property not found

 succeeded in 358ms:
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:70:\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:63:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:41:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:124:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:\subsection{Operator-norm bound}\label{ssec:opnorm}

exec
/bin/bash -lc "rg -n -F -e '\\section{' -e '\\subsection{' -e '\\paragraph{' papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 317ms:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:88:\subsection{What this paper closes vs leaves open}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:90:\paragraph{Closes (at the operator-witness level).}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:114:\paragraph{Leaves open.}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:30:\subsection{The five-dataset structural fit}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:57:\subsection{What the structural fit establishes}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:86:\subsection{What the structural fit does \emph{not} establish}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:118:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:104:\subsection{Test/claim}\label{ssec:testclaim}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:134:\subsection{State-drift / out-of-scope}\label{ssec:scope}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:168:\subsection{The honest verdict}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:37:\subsection{Eighteen preregistered correspondences}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:60:\subsection{Six drug/sleep EEG signatures}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:88:\subsection{Cross-domain selectivity}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:113:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:134:\subsection{Two-witness structure}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:34:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:57:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:109:\subsection{What the agreement does and does not establish}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:\paragraph{Does establish.} A geometric agreement: the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:122:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:41:\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:56:\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:63:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:81:\subsection{H$_4$ irrep block decomposition (imported context)}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:15:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:41:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:75:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:99:\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:103:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:115:\subsection{What the substrate fixes, and what it does not}
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:5:\subsection{Definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:52:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:101:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}

codex
**1. Claim Audit**

- “operator-norm bound `‖Cφ⁻¹‖ = φ²`” is established for the connected finite graph case and matches numerics (`02_definition.tex:64-80`, `results.json:81-86`). The broader substrate wording should keep the `λ_min(L_M)=0` hypothesis visible; §8 does this correctly (`08_programme_home.tex:92-99`).
- “Laplacian spectrum has closed-form values in `Z[φ]`” matches the numerical spectrum (`04_spectrum.tex:5-20`, `results.json:43-80`), but the paper does not prove exact closed-form eigenvalues, only identifies numerical eigenvalues with the displayed expressions. Soften to “numerically matches the following `Z[φ]` values” unless an exact arithmetic derivation is added.
- “per-vertex Pearson correlation `0.976`” is established and matches JSON (`05_agreement.tex:36-39`, `results.json:134-138`). However the headline/abstract should say “non-source vertices”; the test excludes the source (`05_agreement.tex:28-32`, `verify_kernel.py:293-296`).
- “Variant comparison is decisive” is too strong (`01_introduction.tex:75-83`, `10_conclusion.tex:16-18`). The evidence establishes “best among three tested variants,” not a decisive kernel/substrate selection.
- “the unweighted Laplacian wins … this reproduces … b-anomaly ranking” is acceptable only as a qualitative two-criterion agreement, and the paper’s caveat is good (`05_agreement.tex:94-107`). Avoid “selects” at `05_agreement.tex:10`.
- b-anomaly structural table matches the README (`06_passive_witness.tex:48-52`, README `16-22`). AIC tie and Mode-B drift also match (`06_passive_witness.tex:92-109`, README `30-33`).
- “Cross-channel ratio … residual factor ~2 gap” does not match the README wording “residual ~50% overshoot” (`06_passive_witness.tex:68-74`, README `24-28`). Resolve this before calling the passage inherited.
- aria-chess inherited numbers match the companion paper: `17/18`, `18/18`, P4 deep-dive, six EEG signatures, chess/conversation/HCP numbers (`07_active_witness.tex:47-110`; aria-chess `main.tex:81-152`, `sections/05_results.tex:92-128`, `sections/07_cross_domain.tex:47-181`).
- “no other shape parameter enters” overstates the active model (`07_active_witness.tex:117-120`). Aria-chess has `decay=0.95`, condition-specific stimulus models, and fixed cascade gains (`04_consciousness_chain.tex:30`, `127-157`, `192-196`). Say “no other kernel-shape parameter enters.”

**2. Internal Consistency**

- Abstract/headline numbers agree with the body and JSON: `120`, `720`, degree `12`, shells, spectrum, norm, and correlations.
- Definition scope is slightly inconsistent: `main.tex:40-42` and `main.tex:79-80` say “graph Laplacian,” while `02_definition.tex:7-11` allows graph, simplicial, or continuum Laplacians. Use “corresponding Laplacian.”
- `main.tex:52-54` and `main.tex:119-124` omit the source-exclusion detail used in §5.
- The active-witness table says “Kernel-shape free params 0” (`07_active_witness.tex:153`), which is fine; the prose line “no other shape parameter enters” is not.
- The margin “`+0.043` shell-mean” should round to `+0.044` from JSON (`05_agreement.tex:95-96`, `results.json:136-141`).

**3. External Consistency / Numerics**

All requested headline numerics match `results.json`:

- `120` vertices, `720` edges, degree `12/12/12.0`: `results.json:4-13`; paper `03_substrate.tex:61-73`.
- Shell sizes `{1,12,20,12,30,12,20,12,1}`: `results.json:15-25`; paper `03_substrate.tex:89-97`.
- Spectrum values and multiplicities match: `results.json:43-80`; paper `04_spectrum.tex:26-36`.
- `‖Cφ⁻¹‖ = 2.618033988749902`, predicted `φ² = 2.618033988749895`: `results.json:81-86`; paper `04_spectrum.tex:65-76`.
- Correlations match: unweighted `0.976202`, `0.923208`; φ-geometric `0.888380`, `0.879553`; φ-arithmetic `0.884364`, `0.878432`: `results.json:134-146`; paper `05_agreement.tex:87-89`.

**4. Operator-Witness Scope Discipline**

Mostly disciplined. Must soften or clarify:

- `05_agreement.tex:10`: “selects the unweighted Laplacian” risks selection-theorem language. Use “ranks highest among.”
- `01_introduction.tex:75`: “decisive” is too strong for three tested variants.
- `07_active_witness.tex:117-120`: “no other shape parameter enters” strays beyond operator-witness scope because aria-chess has above-operator design constants.
- `06_passive_witness.tex:22-24`: “derived from `Cφ` … §3 derivation” is acceptable only if clearly about the b-anomaly projection, not a derivation of `φ⁻²`.

**5. Tightness**

Suggested one-line edits:

- `04_spectrum.tex:5-7`: “has nine distinct eigenvalue classes with closed-form values” → “numerically resolves into nine classes matching the following `Z[φ]` closed-form list.”
- `05_agreement.tex:94-105`: “selects / preferred / two-criterion convergence” → “Among the three tested variants, the unweighted Laplacian ranks highest on both reported criteria.”
- `06_passive_witness.tex:60-62`: “describes all five datasets” → “can be fit to all five datasets with one amplitude per dataset.”
- `07_active_witness.tex:117-120`: “no other shape parameter enters” → “no other kernel-shape parameter enters; above-operator dynamical and stimulus constants are inherited from aria-chess.”
- `10_conclusion.tex:16`: “decisively above” → “above, within the three tested variants.”

**6. Surface Issues**

- Tectonic reached PDF generation but exited nonzero under the read-only filesystem; warnings were overfull/underfull boxes, not syntax failures. Notable overfulls: `main.tex:101`, `01_introduction.tex:96,149`, `02_definition.tex:81`, `03_substrate.tex:35`, `07_active_witness.tex:20,158`, `08_programme_home.tex:108,133`, `10_conclusion.tex:21`.
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.
- Unused bibliography entries: `ChungSpectralGraph`, `HumphreysReflectionGroups`.
- Consider replacing `\mathrm{bounded\_topk}` with `\operatorname{bounded\_topk}` or `\texttt{bounded\_topk}` for cleaner typography.
- “Mode-B” vs “Mode B” is inconsistent with the README; choose one.

**7. Top Three Fixes**

1. Fix active-regime parameter overclaim at `07_active_witness.tex:117-120`; distinguish kernel-shape parameters from aria-chess’s recurrent/stimulus constants.
2. Soften exact/closed-form spectrum language at `04_spectrum.tex:5-20` unless an exact derivation is added.
3. Resolve b-anomaly inheritance mismatch on the cross-channel residual at `06_passive_witness.tex:68-74` versus README `24-28`.

**8. Verdict**

Publication ready: no — must-fix list above. The numerical core is consistent, but several scope/tone issues need tightening before this is publication-ready.
tokens used
163,144
**1. Claim Audit**

- “operator-norm bound `‖Cφ⁻¹‖ = φ²`” is established for the connected finite graph case and matches numerics (`02_definition.tex:64-80`, `results.json:81-86`). The broader substrate wording should keep the `λ_min(L_M)=0` hypothesis visible; §8 does this correctly (`08_programme_home.tex:92-99`).
- “Laplacian spectrum has closed-form values in `Z[φ]`” matches the numerical spectrum (`04_spectrum.tex:5-20`, `results.json:43-80`), but the paper does not prove exact closed-form eigenvalues, only identifies numerical eigenvalues with the displayed expressions. Soften to “numerically matches the following `Z[φ]` values” unless an exact arithmetic derivation is added.
- “per-vertex Pearson correlation `0.976`” is established and matches JSON (`05_agreement.tex:36-39`, `results.json:134-138`). However the headline/abstract should say “non-source vertices”; the test excludes the source (`05_agreement.tex:28-32`, `verify_kernel.py:293-296`).
- “Variant comparison is decisive” is too strong (`01_introduction.tex:75-83`, `10_conclusion.tex:16-18`). The evidence establishes “best among three tested variants,” not a decisive kernel/substrate selection.
- “the unweighted Laplacian wins … this reproduces … b-anomaly ranking” is acceptable only as a qualitative two-criterion agreement, and the paper’s caveat is good (`05_agreement.tex:94-107`). Avoid “selects” at `05_agreement.tex:10`.
- b-anomaly structural table matches the README (`06_passive_witness.tex:48-52`, README `16-22`). AIC tie and Mode-B drift also match (`06_passive_witness.tex:92-109`, README `30-33`).
- “Cross-channel ratio … residual factor ~2 gap” does not match the README wording “residual ~50% overshoot” (`06_passive_witness.tex:68-74`, README `24-28`). Resolve this before calling the passage inherited.
- aria-chess inherited numbers match the companion paper: `17/18`, `18/18`, P4 deep-dive, six EEG signatures, chess/conversation/HCP numbers (`07_active_witness.tex:47-110`; aria-chess `main.tex:81-152`, `sections/05_results.tex:92-128`, `sections/07_cross_domain.tex:47-181`).
- “no other shape parameter enters” overstates the active model (`07_active_witness.tex:117-120`). Aria-chess has `decay=0.95`, condition-specific stimulus models, and fixed cascade gains (`04_consciousness_chain.tex:30`, `127-157`, `192-196`). Say “no other kernel-shape parameter enters.”

**2. Internal Consistency**

- Abstract/headline numbers agree with the body and JSON: `120`, `720`, degree `12`, shells, spectrum, norm, and correlations.
- Definition scope is slightly inconsistent: `main.tex:40-42` and `main.tex:79-80` say “graph Laplacian,” while `02_definition.tex:7-11` allows graph, simplicial, or continuum Laplacians. Use “corresponding Laplacian.”
- `main.tex:52-54` and `main.tex:119-124` omit the source-exclusion detail used in §5.
- The active-witness table says “Kernel-shape free params 0” (`07_active_witness.tex:153`), which is fine; the prose line “no other shape parameter enters” is not.
- The margin “`+0.043` shell-mean” should round to `+0.044` from JSON (`05_agreement.tex:95-96`, `results.json:136-141`).

**3. External Consistency / Numerics**

All requested headline numerics match `results.json`:

- `120` vertices, `720` edges, degree `12/12/12.0`: `results.json:4-13`; paper `03_substrate.tex:61-73`.
- Shell sizes `{1,12,20,12,30,12,20,12,1}`: `results.json:15-25`; paper `03_substrate.tex:89-97`.
- Spectrum values and multiplicities match: `results.json:43-80`; paper `04_spectrum.tex:26-36`.
- `‖Cφ⁻¹‖ = 2.618033988749902`, predicted `φ² = 2.618033988749895`: `results.json:81-86`; paper `04_spectrum.tex:65-76`.
- Correlations match: unweighted `0.976202`, `0.923208`; φ-geometric `0.888380`, `0.879553`; φ-arithmetic `0.884364`, `0.878432`: `results.json:134-146`; paper `05_agreement.tex:87-89`.

**4. Operator-Witness Scope Discipline**

Mostly disciplined. Must soften or clarify:

- `05_agreement.tex:10`: “selects the unweighted Laplacian” risks selection-theorem language. Use “ranks highest among.”
- `01_introduction.tex:75`: “decisive” is too strong for three tested variants.
- `07_active_witness.tex:117-120`: “no other shape parameter enters” strays beyond operator-witness scope because aria-chess has above-operator design constants.
- `06_passive_witness.tex:22-24`: “derived from `Cφ` … §3 derivation” is acceptable only if clearly about the b-anomaly projection, not a derivation of `φ⁻²`.

**5. Tightness**

Suggested one-line edits:

- `04_spectrum.tex:5-7`: “has nine distinct eigenvalue classes with closed-form values” → “numerically resolves into nine classes matching the following `Z[φ]` closed-form list.”
- `05_agreement.tex:94-105`: “selects / preferred / two-criterion convergence” → “Among the three tested variants, the unweighted Laplacian ranks highest on both reported criteria.”
- `06_passive_witness.tex:60-62`: “describes all five datasets” → “can be fit to all five datasets with one amplitude per dataset.”
- `07_active_witness.tex:117-120`: “no other shape parameter enters” → “no other kernel-shape parameter enters; above-operator dynamical and stimulus constants are inherited from aria-chess.”
- `10_conclusion.tex:16`: “decisively above” → “above, within the three tested variants.”

**6. Surface Issues**

- Tectonic reached PDF generation but exited nonzero under the read-only filesystem; warnings were overfull/underfull boxes, not syntax failures. Notable overfulls: `main.tex:101`, `01_introduction.tex:96,149`, `02_definition.tex:81`, `03_substrate.tex:35`, `07_active_witness.tex:20,158`, `08_programme_home.tex:108,133`, `10_conclusion.tex:21`.
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.
- Unused bibliography entries: `ChungSpectralGraph`, `HumphreysReflectionGroups`.
- Consider replacing `\mathrm{bounded\_topk}` with `\operatorname{bounded\_topk}` or `\texttt{bounded\_topk}` for cleaner typography.
- “Mode-B” vs “Mode B” is inconsistent with the README; choose one.

**7. Top Three Fixes**

1. Fix active-regime parameter overclaim at `07_active_witness.tex:117-120`; distinguish kernel-shape parameters from aria-chess’s recurrent/stimulus constants.
2. Soften exact/closed-form spectrum language at `04_spectrum.tex:5-20` unless an exact derivation is added.
3. Resolve b-anomaly inheritance mismatch on the cross-channel residual at `06_passive_witness.tex:68-74` versus README `24-28`.

**8. Verdict**

Publication ready: no — must-fix list above. The numerical core is consistent, but several scope/tone issues need tightening before this is publication-ready.

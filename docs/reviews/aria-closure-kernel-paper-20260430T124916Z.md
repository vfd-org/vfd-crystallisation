OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dde6f-bc7f-70e3-a842-f1b51c42b29f
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
I’ll treat this as a referee-style textual and mathematical audit. I’m going to read the LaTeX, source notes, companion paper, b-anomaly README, and the verification outputs first, then cross-check the paper’s claims against those sources.
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/sections/01_introduction.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/sections/02_definition.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/main.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/sections/03_substrate.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/sections/04_spectrum.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 217ms:
\documentclass[11pt]{article}

\usepackage[a4paper, margin=2.5cm]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{natbib}
\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
\usepackage{xcolor}

\graphicspath{{figures/}}

\newcommand{\Ph}{\varphi}
\newcommand{\Lop}{L_{V_{600}}}
\newcommand{\Cph}{C_{\Ph}}
\newcommand{\Rsixhundred}{V_{600}}

\title{The closure-response operator
       $\Cph = L + \Ph^{-2} I$:\\
       a geometry-fixed kernel on the 600-cell with two\\
       independent empirical witnesses}

\author{%
  Lee Smart\\[2pt]
  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
  \texttt{@vfd\_org}%
}

\date{April 2026}

\begin{document}

\maketitle

\noindent\textbf{Status:} Preprint, not peer-reviewed.

\noindent\emph{Headline.}
We define a programme-level closure-response primitive
$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
corresponding Laplacian $L_M$ (graph, simplicial, or continuum)
and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
the 600-cell instance $\Rsixhundred$ as the discrete substrate
shared by the two empirical witnesses (the choice of this polytope
is post-hoc motivated by those landings, \S\ref{sec:limitations};
numerically reproduced: $|V|=120$, $|E|=720$, uniform
degree~$12$, H$_3$ shell decomposition
$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
agreement at per-vertex Pearson correlation $0.976$ between the
discrete Green response and the continuum kernel
$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
same fixed graph is then the load-bearing object in two
\emph{independent} empirical works: a passive-regime structural
fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
active-regime substrate witness against eighteen preregistered
neuroscience correspondences plus six drug/sleep EEG
signatures~\citep{SmartAriaChess2026}.

\noindent\emph{Scope.}
This paper presents an empirical \emph{operator witness}: a
geometry-fixed response operator that is simultaneously consistent
with two independent empirical landings under no shape-parameter
retuning between regimes. It is \emph{not} a derivation of the
$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
selection theorem on the companion adaptive-closure-transport
4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
a model-preference claim against alternative kernels on either
empirical landing (the b-anomaly AIC comparison and the aria-chess
substrate-witness scope are documented in their own preprints and
inherited verbatim here).

\begin{abstract}
We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
a closure substrate $M$ with corresponding Laplacian $L_M$ and
$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
the discrete instance shared by two empirical witnesses, and
document its appearance as the same fixed operator (no shape
retuning) in two independent empirical
works: (i)~a five-dataset structural fit of the
$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
preregistered substrate witness against cortical signatures plus
six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
include the numerical reproduction script
(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
from canonical generators, verifies the graph facts
($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
Laplacian spectrum in $\mathbb{Z}[\Ph]$, operator-norm bound
$\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$), and tests the discrete-to-continuum
agreement at per-vertex Pearson correlation $0.976$ for the
unweighted variant, above the two $\Ph$-cocycle weighted variants
tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
tested variants the unweighted Laplacian wins on the geometry-only
criterion, reproducing the qualitative ranking established
independently by b-anomaly's data $\chi^{2}$ comparison.

\noindent\emph{(i) Operator definition and properties.}
$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
non-negative $L_M$ on a connected finite graph; smallest eigenvalue
$\Ph^{-2} \approx 0.382$, operator norm
$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
in one coordinate $x$ is the closed-form Green's function
$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.

\noindent\emph{(ii) The 600-cell instance.}
$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
generated by three orbits ($8$~axis, $16$~half-integer,
$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
on the short-edge graph; the Laplacian has nine eigenvalue classes
in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
\ref{tab:spectrum}, \S\ref{sec:substrate}).

\noindent\emph{(iii) Discrete-to-continuum agreement.}
Per-vertex Pearson correlation between the discrete response
$\psi = \Cph^{-1} f$ for a localised source and the continuum
prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
Same source vertex, same fixed shift, no parameter fitting; the
correlation is invariant under choice of source up to numerical
precision (multi-source sweep, \S\ref{sec:limitations}).

\noindent\emph{(iv) Two independent empirical witnesses.}
(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
with one fitted dimensionless amplitude per dataset and the kernel
shape held fixed. (b)~Active regime,
aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
$\Rsixhundred$, augmented by a recurrent self-model layer with one
condition-dependent self-injection coupling
$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
degree, passes eighteen preregistered correspondences (frozen
2026-04-18) and six drug/sleep EEG signatures.

\noindent\emph{What we do not claim.}
We do not derive the $\Ph^{-2}$ floor; it is a design-level
stability clamp making $\Cph$ strictly positive definite. We do
not claim $\Rsixhundred$ is the unique substrate consistent with
either empirical landing. We do not claim the operator is the
unique kernel shape consistent with the b-anomaly data
(b-anomaly's free-width Gaussian alternative and Mode-B refit
drift caveats are inherited verbatim) nor that the
aria-chess substrate witness establishes a selection theorem on
the adaptive-closure-transport 4-tuple. The structural scope of
this paper is: \emph{one geometry-fixed operator on one fixed
graph appears as the load-bearing object in two independent
empirical works in two distinct regimes, with no shape retuning
between them}.
\end{abstract}

% =====================================================================
\input{sections/01_introduction.tex}
\input{sections/02_definition.tex}
\input{sections/03_substrate.tex}
\input{sections/04_spectrum.tex}
\input{sections/05_agreement.tex}
\input{sections/06_passive_witness.tex}
\input{sections/07_active_witness.tex}
\input{sections/08_programme_home.tex}
\input{sections/09_limitations.tex}
\input{sections/10_conclusion.tex}
% =====================================================================

\section*{Reproducibility}
The complete numerical verification (vertex construction,
short-edge graph build, Laplacian spectrum, operator-norm bound,
discrete-to-continuum correlation across three Laplacian variants)
is reproducible from \texttt{repro/verify\_kernel.py} in this
paper's bundle. No randomness, no fitted parameters: all numbers
in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
\S\ref{sec:agreement} are deterministic outputs of the script.
The two empirical witness preprints
(b-anomaly~\citep{SmartBAnomaly2026},
aria-chess~\citep{SmartAriaChess2026}) carry their own
reproducibility artifacts; this paper does not duplicate them.

\bibliographystyle{plainnat}
\bibliography{references}

\end{document}

 succeeded in 217ms:
% =====================================================================
\section{The closure-response operator}\label{sec:definition}
% =====================================================================

\subsection{Definition}

Let $M$ be a closure substrate: a connected finite undirected graph
$M=(V,E)$, a finite simplicial complex with chosen Laplacian, or a
projected continuum coordinate. Let $L_M$ be the corresponding
Laplacian (graph Laplacian $L = D - A$, simplicial Laplacian, or
continuum operator $-\Delta$ with chosen boundary conditions).
Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.

The \emph{closure-response operator} is
\begin{equation}\label{eq:cphi}
\Cph \;=\; L_M + \Ph^{-2} I.
\end{equation}
For a non-negative localised source $f$ on $M$, the
\emph{closure response field} is
\begin{equation}\label{eq:psi}
\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
\end{equation}

\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}

The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
require:

\begin{itemize}\itemsep=2pt
\item \textbf{(H1) Self-adjointness.} $L_M$ is self-adjoint on the
  $L^{2}$ inner product on $M$ (with counting measure on a finite
  graph, with Lebesgue measure with appropriate boundary conditions
  in the continuum case).
\item \textbf{(H2) Non-negativity.} $L_M \geq 0$ as a
  quadratic form: $\langle f, L_M f\rangle \geq 0$ for all $f$.
\item \textbf{(H3) Connectedness.} On a finite graph, $M$ is
  connected (so the kernel of $L_M$ is exactly the constant
  vector). In the continuum case, the $L_M$-zero subspace is
  finite-dimensional and known.
\end{itemize}

The standard graph Laplacian on a connected finite undirected
graph satisfies (H1)--(H3); so does the continuum
$L = -d^{2}/dx^{2}$ on a bounded interval with Dirichlet boundary
conditions, or on the full line with decay-at-infinity. Substrates
outside this class — projected coordinates with non-standard
boundaries, weighted Laplacians whose weight function is unbounded,
or operators with negative spectrum — require their own analysis,
which we do not give here.

\subsection{Positive definiteness}\label{ssec:positivity}

Under (H1)--(H3) on a finite connected graph, $L_M$ has a smallest
eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
\[
\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
                    \;=\; \Ph^{-2} \;>\; 0,
\]
so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
well-defined and bounded.

\subsection{Operator-norm bound}\label{ssec:opnorm}

The operator norm of $\Cph^{-1}$ is the reciprocal of its smallest
eigenvalue:
\begin{equation}\label{eq:opnorm}
\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
              \;=\; 1/\Ph^{-2} \;=\; \Ph^{2}
              \;\approx\; 2.618034.
\end{equation}
This is the response-amplification ceiling: for any source $f$,
\[
\|\psi\|_{2} \;\leq\; \Ph^{2}\, \|f\|_{2}.
\]
Numerically reproduced as $\|\Cph^{-1}\| = 2.618034$ on the 600-cell
graph $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
\S\ref{sec:agreement}); this matches the closed-form $\Ph^{2}$ to
machine precision.

\subsection{Continuum projection}\label{ssec:continuum}

In one projected coordinate $x \in \mathbb{R}$ with
$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
exponential
\begin{equation}\label{eq:green_continuum}
G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
\end{equation}
The decay scale is $\Ph$ — the same constant that appears in the
shift, by construction. Normalised, the kernel is
$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.

This continuum Green's function is the comparison object for the
discrete-to-continuum agreement test (\S\ref{sec:agreement}):
the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
is compared to $G(\|v - v_{\mathrm{src}}\|)$.

\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}

The shift $\Ph^{-2}$ is chosen so that:
\begin{enumerate}\itemsep=2pt
\item $\Cph$ is strictly positive definite (the smallest eigenvalue
  is exactly $\Ph^{-2}$);
\item the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ is the
  same constant as the continuum decay scale (Eq.~\eqref{eq:green_continuum}),
  giving a single dimensional parameter throughout the operator;
\item the continuum projection (Eq.~\eqref{eq:green_continuum})
  has decay scale $\Ph$, not a free length parameter.
\end{enumerate}
We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
symmetry argument. It is a design-level choice motivated by
(1)--(3); we report this explicitly and treat formal derivation as
an open build (\S\ref{sec:limitations}). The companion
adaptive-closure-transport
preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
selection-layer dynamics over $W$-space that would, if delivered,
constrain the shift further; that derivation is not delivered
there or here.

 succeeded in 218ms:
% =====================================================================
\section{Introduction}\label{sec:intro}
% =====================================================================

A response operator on a fixed graph, with no shape parameters tuned
to any dataset, that simultaneously describes (i) the $q^{2}$ shape
of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
flavour-physics datasets in their passive linear-response regime,
and (ii) eighteen preregistered cortical correspondences plus six
drug/sleep EEG signatures in the active dynamical regime of a
recurrent self-model layer above the same graph, deserves a separate
preprint that names the operator, gives its construction in full,
and threads the relationship between the two empirical landings
without inheriting either's load-bearing claims. That is what this
paper does.

The operator is
\begin{equation}\label{eq:cphi_intro}
\Cph \;=\; L_M + \Ph^{-2} I,
\qquad \Ph \;=\; (1+\sqrt 5)/2,
\end{equation}
where $M$ is a closure substrate (graph, simplicial complex, or
projected coordinate) and $L_M$ is its Laplacian. The shift
$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
operator-norm bound is
\begin{equation}\label{eq:opnorm_intro}
\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
\end{equation}
The continuum projection in one coordinate $x$ has a closed-form
Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
$\Ph$ (\S\ref{sec:definition}).

The discrete substrate used by the two empirical witnesses is
the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
generated by three H$_4$ Coxeter orbits ($8$ axis vertices, $16$
half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
short edges $\langle v, w\rangle = \Ph/2$. The choice of this
polytope is post-hoc motivated by the empirical landings
(\S\ref{sec:limitations}); the construction itself is theorem-level
rigorous. The graph has $|E|=720$ edges, uniform degree~$12$ by
H$_4$ transitivity, a $9$-shell H$_3$
partition $\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
All of these facts are reproduced numerically by
\texttt{repro/verify\_kernel.py} from the canonical generators
alone — no external data input.

\subsection*{What this paper claims}

We claim a single \emph{operator witness}: that one geometry-fixed
operator, on one fixed graph, with no shape-parameter retuning
between regimes, appears as the load-bearing object in two
empirical works covering qualitatively distinct physical settings.

\begin{enumerate}\itemsep=2pt
\item \textbf{Operator definition is fixed by the construction.}
  Once $\Rsixhundred$ is selected and the stability shift
  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
  parameter, no fitted threshold, no learned weight enters the
  operator. The Laplacian spectrum, the operator-norm bound, and
  the discrete-to-continuum agreement are computed (not fitted)
  from the construction and reproduced in
  \texttt{repro/verify\_kernel.py}.
\item \textbf{Discrete-to-continuum agreement is empirical, not
  postulated.} For a localised source at any vertex, the discrete
  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
  $\rho = 0.976$ on the unweighted graph Laplacian. This is
  numerical agreement between two independently-defined objects (a
  120-dimensional discrete inverse and a continuum exponential
  kernel), not a definitional identity.
\item \textbf{Variant comparison among the three tested variants.}
  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
  $\Ph$-arithmetic edge weights via shell-grade exponents
  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
  correlation: $0.888$ and $0.884$ respectively. Within the three
  tested variants, the unweighted Laplacian ranks highest on the
  geometry-only criterion. This reproduces,
  on a different test, the qualitative ranking established
  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
  (\S\ref{sec:passive_witness}).
\item \textbf{Two independent empirical landings, same operator.}
  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
  public datasets, with one fitted dimensionless amplitude per
  dataset and the kernel held fixed; sign uniformity holds in
  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
  recurrent self-model layer above the substrate, to pass eighteen
  preregistered cortical correspondences (frozen 2026-04-18) plus
  six drug/sleep EEG signatures.
\end{enumerate}

\subsection*{What this paper does \emph{not} claim}

\begin{itemize}\itemsep=2pt
\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
  $\Ph^{-2}$ is a design-level stability clamp that bounds
  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
  functional or a symmetry argument; we report its role as a
  regularisation-of-mass scale.
\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
  regular 4-polytopes (the $24$-cell, the $120$-cell), other
  highly symmetric graphs, and continuum substrates are all
  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
  is post-hoc motivated by the empirical landings; a formal
  ablation against alternative substrates is an open build.
\item \emph{Not a kernel-uniqueness claim on either empirical
  landing.} The b-anomaly's free-width Gaussian alternative shows
  that a free-width Gaussian charm-loop proxy fits the same five
  datasets comparably in $\chi^{2}$ at the cost of one extra shape
  parameter; the b-anomaly AIC comparison against
  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
  statistical tie on current data
  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
  Both caveats are inherited verbatim from the b-anomaly preprint.
\item \emph{Not a selection theorem on the
  ACT 4-tuple.} The companion adaptive-closure-transport
  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
  fills the response slot. Selection — Lyapunov $V(W)$ on the
  reduced flow, edge-space decomposition under $2I$-equivariance,
  full reduced-flow convergence — is left open in that paper and
  is not delivered here.
\item \emph{Not a circuit-level model on the active-regime side.}
  The aria-chess preprint operates at the architectural-algorithmic
  level above $\Cph$. We import its empirical results verbatim and
  do not relitigate them here; their substrate-witness scope
  applies.
\end{itemize}

\subsection*{Mapping from numerics to admissible claims}

To keep this paper inside the operator-witness scope, we use the
same claim-boundary discipline as the aria-chess
preprint~\citep{SmartAriaChess2026}: numerical results
$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
$\mathcal C_{\mathrm{admissible}}$ by the rule
\[
q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
        \mathcal C_{\mathrm{admissible}},
\qquad
\mathcal C_{\mathrm{admissible}}
   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
\]
A numerically computed quantity (the Laplacian spectrum, the
operator-norm bound, the per-vertex correlation $0.976$) licenses
a `computed'-type claim. A statistical agreement at the operator
level (sign uniformity in $5/5$ datasets, an $18/18$ preregistered
tally) licenses a `consistent with'-type claim. We never write
`derives the kernel', `proves uniqueness', or `establishes
selection'.

\medskip
\begin{center}
\fbox{\parbox{0.92\linewidth}{\small
\textbf{What is claimed / what is not.}\par
\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
600-cell graph, with computed spectrum, operator-norm bound, and
discrete-to-continuum correlation; the same fixed operator appearing
in two independent empirical works (b-anomaly five-dataset
structural fit; aria-chess $18/18$ + $6/6$ preregistered substrate
witness) without shape-parameter retuning between regimes.\par
\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
$\Rsixhundred$; uniqueness of the kernel shape on either empirical
landing; a selection theorem on the ACT 4-tuple; that either
empirical landing settles the underlying physics (flavour anomaly
or consciousness) by the operator alone.
}}
\end{center}

\subsection*{Layout}

\S\ref{sec:definition} gives the operator definition, the positivity
properties of $\Cph$, the operator-norm bound, and the continuum
projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
canonical generators, gives the graph facts, and the $9$-shell
decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
across three Laplacian variants. \S\ref{sec:passive_witness} and
\S\ref{sec:active_witness} thread the two independent empirical
witnesses (b-anomaly and aria-chess) at the operator level.
\S\ref{sec:programme_home} positions $\Cph$ as the programme home
for the polynomial-in-$L$ Lyapunov family that recurs across the
Millennium drafts. \S\ref{sec:limitations} enumerates limitations
in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 236ms:
% =====================================================================
\section{The Laplacian spectrum}\label{sec:spectrum}
% =====================================================================

The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
numerically resolves into nine distinct eigenvalue classes whose
values match the closed-form $\mathbb{Z}[\Ph]$ list given in
Table~\ref{tab:spectrum} to machine precision; multiplicities sum
to $|V| = 120$. The spectrum is computed numerically by
\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
$120\times 120$ symmetric eigendecomposition, deterministic at
machine precision); the closed-form identification is made by
algebraic recognition of the displayed values, not by an exact
arithmetic derivation in this paper.

\begin{table}[ht]
\centering
\small
\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
values returned by \texttt{repro/verify\_kernel.py}; multiplicities
sum to $120$.}
\label{tab:spectrum}
\begin{tabular}{c c c}
\toprule
Closed-form eigenvalue & Numerical value & Multiplicity \\
\midrule
$0$            & $-3\!\times\!10^{-15}$ (machine zero) & $1$ \\
$12 - 6\Ph$    & $2.2918$  & $4$ \\
$12 - 4\Ph$    & $5.5279$  & $9$ \\
$9$            & $9.0000$  & $16$ \\
$12$           & $12.0000$ & $25$ \\
$14$           & $14.0000$ & $36$ \\
$4\Ph + 8$     & $14.4721$ & $9$ \\
$15$           & $15.0000$ & $16$ \\
$6\Ph + 6$     & $15.7082$ & $4$ \\
\midrule
\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
\begin{align*}
12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
\end{align*}
The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
are conjugate under the Galois automorphism
$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
fixed-point eigenvalues $\{0, 9, 12, 14, 15\}$ are rational and
have multiplicities $\{1, 16, 25, 36, 16\}$ (sum $94$); the
$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.

\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
reformulation; that reading is not imported here. We report only
that the spectrum has this structure.

\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}

The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
\[
\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
\;\approx\; 0.381966,
\]
and the operator-norm bound is
\[
\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
\]
\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
(predicted) — match to six decimal places. The largest eigenvalue
of $\Cph$ is
$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.

\subsection{H$_4$ irrep block decomposition (imported context)}
\label{ssec:irrep}

The eigenspaces of $\Lop$ partition into H$_4$-proper and
$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
exponents are $\{1, 11, 19, 29\}$; under the
$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
aria-chess companion's recurrent
layer~\citep{SmartAriaChess2026} realises this block decomposition
at machine precision and provides a spectrally clean
H$_4$-equivariant basis there.

This subsection is imported context from the aria-chess companion;
the irrep block decomposition is \emph{not} verified by
\texttt{repro/verify\_kernel.py} of this paper and is not used as
a load-bearing fact for any operator-witness claim made here. We
include the labelling for orientation only.

 succeeded in 248ms:
% =====================================================================
\section{The 600-cell substrate}\label{sec:substrate}
% =====================================================================

This section gives the discrete instance used by the two empirical
witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
under H$_4$ Coxeter symmetry, with the standard short-edge graph
Laplacian. The choice of this polytope is post-hoc motivated by
the empirical landings (\S\ref{sec:limitations}); the
construction itself is theorem-level rigorous in H$_4$ Coxeter
group theory. All facts in this section are reproduced numerically
by \texttt{repro/verify\_kernel.py} from the canonical generators
alone.

\subsection{Vertex set}\label{ssec:vertices}

$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical
generating orbits are:
\begin{itemize}\itemsep=2pt
\item \textbf{Axis orbit} ($8$ vertices): all permutations of
  $(\pm 1, 0, 0, 0)$;
\item \textbf{Half-integer orbit} ($16$ vertices): all sign
  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
\item \textbf{$\Ph$-mixed orbit} ($96$ vertices): all even
  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
  $\Ph^{2} = \Ph + 1$ identity, equivalently
  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
\end{itemize}
The total is $8 + 16 + 96 = 120$ unit vectors. Reproduced by
\texttt{repro/verify\_kernel.py:build\_v600}; the numerical check
$\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms all vertices on
$S^{3}$.

The H$_4$ Coxeter group (order $14400$) acts transitively on the
$120$ vertices. Every vertex therefore has \emph{identical} local
structure under $H_{4}$; in particular, every vertex has the same
degree in the short-edge graph defined below.

\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}

For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
Euclidean chord distance is
\[
\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
\]
The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
if their inner product equals the canonical short-edge value
\begin{equation}\label{eq:short_edge}
\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
\end{equation}
equivalently chord distance
$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
nearest-neighbour adjacency on the canonical 600-cell embedding
into $S^{3}$~\citep{CoxeterRegularPolytopes}.

\paragraph{Graph facts (forced by the construction).}
The graph $G_{V_{600}}$ has:
\begin{itemize}\itemsep=2pt
\item $|V|=120$ vertices,
\item $|E|=720$ edges,
\item every vertex has degree exactly $12$ (H$_4$ transitivity on
  the vertex set forces uniformity of the local structure; the
  short-edge nearest-neighbour graph inherits this uniformity),
\item the graph is connected (verified numerically by counting
  connected components of the short-edge adjacency matrix; the
  classical 600-cell connectivity result is well known
  in~\citep{CoxeterRegularPolytopes}).
\end{itemize}
All four facts are reproduced numerically:
\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
degree-min/max $=12/12$ (uniform), and one connected component.

\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}

Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
fixing $v_{0}$ partitions the remaining $119$ vertices into shells
of constant inner product with $v_{0}$. The nine canonical inner
products are
\begin{equation}\label{eq:shell_inner}
\langle v, v_{0}\rangle
\;\in\;
\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
\end{equation}
indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
antipode. The shell-size sequence is
\begin{equation}\label{eq:shell_sizes}
(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
\;=\;
(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
\end{equation}
The middle shell $S_{4}$ has $30$ equatorial vertices forming the
icosidodecahedral ring. The total is
$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.

\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
The antipode $-v_{0}$ is the unique shell-$8$ vertex.

\subsection{Inner-product check}\label{ssec:inner_product_check}

The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
are jointly consistent: a vertex in shell $s_{1}$ is connected to a
vertex in shell $s_{2}$ if and only if their pairwise inner product
is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
adjacency types to those compatible with the H$_3$ orbit structure.
The numerically constructed graph respects this: every edge has
inner product exactly $\Ph/2$ within machine precision (tolerance
$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).

\subsection{What the substrate fixes, and what it does not}

\begin{itemize}\itemsep=2pt
\item \textbf{Fixed by the construction once $\Rsixhundred$ is
  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
  Laplacian spectrum (\S\ref{sec:spectrum}).
\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
  (\S\ref{ssec:opnorm}); the operator-norm bound
  $\|\Cph^{-1}\| = \Ph^{2}$.
\item \textbf{Not fixed by this paper}: the choice of
  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other H$_n$
  Coxeter substrates. The 600-cell choice is post-hoc motivated by
  the empirical landings (\S\ref{sec:passive_witness},
  \S\ref{sec:active_witness}). A formal substrate ablation is an
  open build (\S\ref{sec:limitations}).
\end{itemize}

codex
The opening material is already mostly disciplined about scope, but I’m seeing several claims whose strength depends on companion documents or exact wording, so I’m switching to line-numbered reads for all relevant files before judging them.
exec
/bin/bash -lc "sed -n '1,280p' 'papers/aria-closure-kernel/paper/sections/05_agreement.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,300p' 'papers/aria-closure-kernel/paper/sections/06_passive_witness.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,320p' 'papers/aria-closure-kernel/paper/sections/07_active_witness.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,320p' 'papers/aria-closure-kernel/paper/sections/08_programme_home.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,340p' 'papers/aria-closure-kernel/paper/sections/09_limitations.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 265ms:
% =====================================================================
\section{Discrete-to-continuum agreement}\label{sec:agreement}
% =====================================================================

This is the load-bearing geometric fact of the paper: the discrete
response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
source agrees per-vertex with the continuum kernel
$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
the source. We give the test, the numerical result, and a variant
comparison in which the unweighted Laplacian ranks highest among
the three tested variants (unweighted, $\Ph$-geometric weighted,
$\Ph$-arithmetic weighted).

\subsection{The test}\label{ssec:test}

Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
other entries zero). Compute
\[
\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
\]
by direct linear solve (no eigenmode truncation). For each vertex
$v \in V$, compute the Euclidean chord distance
$x(v) = \|v - v_{0}\|$ and the continuum prediction
\[
G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
\]
The agreement criterion is the Pearson correlation between
$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
source itself is excluded, since the discrete response there is
trivially the diagonal of $\Cph^{-1}$ and the chord distance is
zero, both degenerate for the comparison).

\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}

\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
\begin{itemize}\itemsep=2pt
\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
  (averaging $\psi(v)$ over each H$_3$ shell first, then
  correlating the $9$-point shell-mean trajectory with the
  continuum prediction at the shell mean radius).
\end{itemize}
The two correlations measure the same fact at different
resolutions: per-vertex tests at $|V|-1 = 119$ data points
(every non-source vertex), while shell-mean tests at $9$ data
points (one per shell). On the unweighted 600-cell graph with
an H$_3$-fixed source, $\psi$ is shell-constant up to numerical
precision — the within-shell standard deviations are at machine
precision ($\sim 10^{-16}$). The two tests therefore differ in
weighting, not in noise content: the per-vertex test weights each
shell by its multiplicity ($\{12, 20, 12, 30, 12, 20, 12, 1\}$
for the non-source shells) and excludes the source vertex,
while the shell-mean test gives equal weight to every shell. The
per-vertex test is the headline agreement criterion in this paper.

\subsection{Variant comparison}\label{ssec:variant_comparison}

Two $\Ph$-cocycle weighted Laplacian variants are tested as
controls:

\begin{itemize}\itemsep=2pt
\item \textbf{$\Ph$-geometric weights}: edge weight
  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
  is the shell index of $v$.
\item \textbf{$\Ph$-arithmetic weights}: edge weight
  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
  $\omega_{+}$.
\end{itemize}
The weighted Laplacian is then
$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
We re-run the discrete-to-continuum test on each variant.

\begin{table}[ht]
\centering
\small
\caption{Per-vertex and shell-mean Pearson correlations between the
discrete response $\psi = \Cph^{-1} e_{v_{0}}$ and the continuum
prediction $G(\|v - v_{0}\|)$ for three Laplacian variants.
Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
\label{tab:variant_correlation}
\begin{tabular}{l c c}
\toprule
Variant            & Per-vertex correlation & Shell-mean correlation \\
\midrule
\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Reading.} Among the three tested variants, the unweighted
Laplacian ranks highest on both reported criteria
($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
This reproduces, on a different test, the qualitative ranking the
b-anomaly paper~\citep{SmartBAnomaly2026} established
independently against its data-$\chi^{2}$ criterion
on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
b-anomaly numbers). Two independent criteria — geometry-only
correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
agree on which Laplacian variant is preferred. We do not claim
this is a uniqueness result; we report it as a two-criterion
convergence (the b-anomaly paper's own caveat that the data was
looked at first and the geometry criterion verified afterward is
inherited verbatim).

\subsection{What the agreement does and does not establish}

\paragraph{Does establish.} A geometric agreement: the discrete
response of a fixed-shift Green operator on a fixed graph behaves,
to within the per-vertex Pearson correlation $0.976$, like the
closed-form continuum exponential at the same length scale $\Ph$.
This is a non-trivial agreement between two independently-defined
objects: (i) the discrete inverse of a $120\times 120$
Laplacian-plus-shift matrix; and (ii) a one-dimensional continuum
exponential. The $\Ph$-mediated agreement is an empirical fact
about the chosen substrate and shift, computed (not fitted) by
the verification script.

\paragraph{Does not establish.} Operator uniqueness on either
empirical landing — the b-anomaly paper documents a free-width
Gaussian alternative that fits comparably in $\chi^{2}$ at the
cost of one extra shape parameter, and the aria-chess preprint
does not run a substrate ablation; both caveats are inherited
verbatim. The agreement also does not establish that
$\Rsixhundred$ is the unique discrete substrate with this
property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
graphs would give different correlations on the same test, and a
formal substrate ablation is an open build (\S\ref{sec:limitations}).

 succeeded in 254ms:
% =====================================================================
\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
% =====================================================================

This section threads the first independent empirical landing of
$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
summarise here only what the operator-witness narrative requires
and inherit the preprint's caveats verbatim.

\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}

The Wilson-coefficient Hamiltonian for $b\to s\mu^{+}\mu^{-}$
contains a $C_{9}^{(\prime)}$ contribution that, in the Standard
Model, is approximately $q^{2}$-independent in the relevant
kinematic range. The b-anomaly preprint replaces the constant SM
shape with a fixed kernel
\begin{equation}\label{eq:banomaly_kernel}
\Delta C_{9}^{\mathrm{eff}}(q^{2})
\;=\;
A \cdot \kappa_{V_{600}}(q^{2}),
\end{equation}
where $\kappa_{V_{600}}(q^{2})$ is the projection of $\Cph$ on
$\Rsixhundred$ to the flavour-physics $q^{2}$ axis (the b-anomaly
preprint's §3 projection construction, which we do not relitigate
here; this is a projection of the operator, not a derivation of
$\Ph^{-2}$), and $A$ is a single fitted dimensionless amplitude
per dataset. The kernel
shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
This is a \emph{structural} test: same fixed $\Cph$ on the same
$\Rsixhundred$, no shape retuning between datasets.

\subsection{The five-dataset structural fit}

The b-anomaly preprint reports the following per-dataset table
(verbatim from~\citep{SmartBAnomaly2026}, also at
\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):

\begin{table}[ht]
\centering
\small
\caption{b-anomaly five-dataset structural fit. Verbatim
from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
dataset, kernel shape held fixed.}
\label{tab:banomaly}
\begin{tabular}{l l r r r r}
\toprule
Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
\midrule
LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
\bottomrule
\end{tabular}
\end{table}

\subsection{What the structural fit establishes}

\begin{itemize}\itemsep=2pt
\item \textbf{Universality (5/5).} The same fixed kernel shape
  can be fit to all five datasets with one amplitude $A$ per
  dataset and no shape retuning. The kernel never moves between
  datasets.
\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
  reproduces the established direction of the
  anomaly~\citep{LHCbAngular2020} across all five independent
  measurements.
\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
  $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with
  the predicted Krüger--Matias $P$-basis vs $S$-basis amplification
  ($\sim 2.2$~\citep{KrugerMatias2005}), with a residual
  $\sim 50\%$ overshoot. The b-anomaly preprint reports the
  residual as an open item, not a discharge.
\item \textbf{Geometry-first variant test.} Of three discrete
  Laplacian variants on $\Rsixhundred$ (unweighted,
  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
  unweighted choice wins on both a pure-geometry criterion
  (correlation $0.997$ with the continuum kernel, b-anomaly
  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
  ($\chi^{2}=13.555$). The two criteria agree on the variant
  ranking — a two-criterion convergence on the same fixed
  operator.
\end{itemize}

\subsection{What the structural fit does \emph{not} establish}

The b-anomaly preprint is explicit about the following caveats,
which we inherit verbatim:

\begin{itemize}\itemsep=2pt
\item \textbf{AIC tie on current data.} On Akaike model comparison,
  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
  indistinguishable: stacked AIC weights
  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
  Current data cannot resolve the model comparison. AIC is blind
  to the universality / shape-prediction claim itself, but it is
  decisive about whether the shape is forced by data: it is not.
\item \textbf{Free-width Gaussian alternative.} A free-width
  Gaussian charm-loop proxy fits the same five datasets comparably
  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
  is not the unique $q^{2}$ shape consistent with the anomaly.
\item \textbf{Mode-B drift (linearised-vs-nonlinear refit).} An
  earlier linearised analysis gave a stronger preference
  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
  the non-linear refit; the $+2.77$-AIC-unit drift between
  linearised and Mode-B (non-linear) refits is the largest single
  methodological uncertainty in the b-anomaly project.
\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
  preprint's limitations section acknowledges that the LHCb~2025
  data was looked at first, and only later was the agreement of
  the data-$\chi^{2}$ ranking with the pure-geometry ranking
  verified. The two-criterion agreement is criterion-independent
  but not historically blind.
\end{itemize}

\subsection{Reading at the operator level}

The b-anomaly result is the \emph{passive-regime} empirical
witness for $\Cph$ on $\Rsixhundred$: a single linear response
$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
fixed discrete-to-momentum projection, gives a sign-uniform
description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
five independent measurements without shape retuning. This does
not establish the kernel as theorem-grade physics on the flavour
side (the AIC tie, the free-width Gaussian alternative, and the
Mode-B linearised-vs-nonlinear refit drift prevent that). It does
establish, at the operator level, that the same fixed $\Cph$ on
the same fixed $\Rsixhundred$ is consistent with one of two
independent empirical landings without parameter retuning. The
second landing is in \S\ref{sec:active_witness}.

 succeeded in 243ms:
% =====================================================================
\section{Active-regime witness: aria-chess}\label{sec:active_witness}
% =====================================================================

This section threads the second independent empirical landing of
$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
summarise here only what the operator-witness narrative requires
and inherit the preprint's substrate-witness scope verbatim.

\subsection{What aria-chess tests}\label{ssec:aria_setup}

The aria-chess preprint adds a recurrent self-model layer above
the same $\Cph$ on the same $\Rsixhundred$. The architecture
introduces:
\begin{itemize}\itemsep=2pt
\item One \emph{condition-dependent} self-injection coupling
  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
  WAKE/RECOVERY) that controls the strength of the recurrent
  feedback;
\item One \emph{substrate-pinned} nonlinearity
  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
  $k=12$ is not a free hyperparameter; it is the substrate's
  average degree.
\item Condition-specific \emph{biologically-motivated} stimulus
  models (slow oscillation + spindles + K-complexes for SLEEP\_N3,
  AR(1) noise + tonic shell + attention episodes for WAKE,
  low-amplitude tonic noise for PROPOFOL). These are
  biologically-motivated design choices, not measurement-fits to
  subject-level EEG data.
\end{itemize}
The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
b-anomaly and aria-chess; the same fixed shift used in the
flavour-physics structural fit is used in the cortical substrate
witness.

\subsection{Eighteen preregistered correspondences}

Eighteen quantitative predictions (P1--P18) were locked on
2026-04-18 in the aria-chess preprint's
\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
validation run. Each prediction has a specific numerical claim, a
falsifiable threshold, and a named validation script. The
preregistered tally as reported in~\citep{SmartAriaChess2026}:

\begin{itemize}\itemsep=2pt
\item $17/18$ at standard validation methodology ($5$-seed
  cascade block plus state-reset protocol);
\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
  point estimate $+0.190$, $95\%$ CI $[+0.143, +0.239]$,
  $0/2000$ resamples at-or-below zero, reported as $0.0000$).
\item No preregistered threshold has been modified.
\end{itemize}
The aria-chess preprint reports this as methodology refinement
(documented seed-count increase on a high-per-seed-variance
interaction term), \emph{not} as a threshold change. We inherit the
reading verbatim.

\subsection{Six drug/sleep EEG signatures}

On a single deterministic substrate trajectory at seed~$42$, the
aria-chess preprint reports six biological signatures testing
against literature-derived thresholds:

\begin{itemize}\itemsep=2pt
\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
  intervals do not overlap each other; the WAKE interval is the
  pairwise common ground).
\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
  wake (threshold $\in [1.5, 5.0]$, empirical reference
  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
\item \textbf{Propofol continuity drop}: $+0.066$
  (threshold $> 0.020$).
\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
  direction confirmed; $\Phi$-proxy not full IIT).
\item \textbf{Recovery deterministic identity to wake}: under the
  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
  to the WAKE trajectory.
\end{itemize}

\subsection{Cross-domain selectivity}

\begin{itemize}\itemsep=2pt
\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
  positions across $4$ categories on $8$-D V2 features; substrate
  routing lifts leave-one-out classification at canonical depth
  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
\item \textbf{Conversation pattern recognition (P14--P16)}:
  $64$ utterances, $8$ categories; raw classification $87.5\%$,
  substrate-routed lift $-4.4$pp (within the preregistered
  neutrality band $|\cdot| < 10$pp). The substrate is selectively
  amplifying in tasks where raw features are ambiguous and
  approximately neutral when raw features are already
  discriminative.
\item \textbf{HCP brain functional connectivity (P17--P18)}:
  full-cohort descriptive statistics on $n=1003$ subjects show
  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
  homogeneity, $+79.78\sigma$ on raw participation ratio (with
  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
  deviations below the HCP biological cohort.
\end{itemize}

\subsection{Reading at the operator level}

The aria-chess result is the \emph{active-regime} empirical
witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
layer above $\Cph$ uses one condition-dependent coupling and one
substrate-pinned nonlinearity at the graph's average degree
$k=12$; no other \emph{kernel-shape} parameter enters. Above the
operator, aria-chess inherits its own dynamical and stimulus
constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
condition-specific biologically-motivated stimulus models); these
are documented in the aria-chess preprint and are not retuned in
this paper. The kernel shift $\Ph^{-2}$ is not retuned between
b-anomaly and aria-chess. Under those design choices, the same
fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
preregistered cortical correspondences (frozen 2026-04-18) and six
literature-thresholded EEG drug/sleep signatures.

The aria-chess preprint stays inside substrate-witness scope: it
does not claim the substrate \emph{is} consciousness, does not
claim 600-cell uniqueness among regular 4-polytopes, and does not
deliver a selection theorem on the ACT 4-tuple. We inherit the
scope verbatim. What we add at the operator level is the
observation that the same fixed $\Cph$ — under no shape-parameter
retuning between regimes — is the load-bearing object on both
empirical landings.

\subsection{Two-witness structure}

\begin{table}[ht]
\centering
\small
\caption{Two independent empirical landings of $\Cph$ on
$\Rsixhundred$, with no shape retuning between regimes.}
\label{tab:two_witness}
\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
\toprule
& Passive regime & Active regime \\
\midrule
Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
Domain             & flavour physics                    & cortical neuroscience \\
Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
Kernel-shape free params & 0                            & 0 \\
Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
\bottomrule
\end{tabular}
\end{table}

The two witnesses share, by design, exactly the geometry-fixed
operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
the same shift $\Ph^{-2}$. They share no fitted parameter,
threshold, dataset, or methodological choice above the operator
level. The b-anomaly amplitude $A$ is fitted to flavour-physics
$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
neural data; the v4 stimulus protocols are biologically motivated,
not subject-fit. Independence in this paper is independence at
the empirical layer above the shared operator.

 succeeded in 230ms:
% =====================================================================
\section{Programme home and the open selection layer}\label{sec:programme_home}
% =====================================================================

This section positions $\Cph$ within the broader cascade programme
and identifies what the operator does not deliver. The framing
matters for the hostile-review reading: $\Cph$ is the
\emph{response} primitive; \emph{selection} (which response
configuration the system picks under dynamics) is a separate layer
that this paper does not close.

\subsection{Programme home: polynomial-in-$L$ Lyapunov family}

Several constructions across the cascade-programme drafts are
$L$-symmetric polynomial-in-$L$ functionals on a finite-dimensional
substrate. They are programme-positioned as members of the same
family as $\Cph$:

\begin{itemize}\itemsep=2pt
\item \textbf{RH polynomial filter} (forthcoming RH artifact in
  this programme). Cascade closure functional on $\mathbb{R}^{120}$:
  $F_{\mathrm{filt}}(x) = \tfrac12 \langle x, p_{\mathrm{fix}}(L)^{2} x\rangle$
  with $\Psi_{t} = e^{-t\, p_{\mathrm{fix}}(L)^{2}}$. Programme-positioned
  as the $\sigma$-fix-annihilator instance of the family: a
  degree-$10$ positive functional vanishing exactly on
  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
  any claim made in this paper.
\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
  this programme). Discrete cascade gap Hamiltonian,
  programme-positioned as a $\Cph$-style mass-regularised Laplacian
  on $\Rsixhundred$. The artifact itself is not load-bearing for
  any claim made in this paper.
\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
  The homeostatic regulariser
  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
  programme-positioned as a member of the same polynomial-in-$L$
  family.
\end{itemize}

We list the family-membership claim as \emph{programme-positioned},
not formally proved. Each named operator is in a
polynomial-in-$L$ form with positivity and self-adjointness
properties matching the family description; we do not claim a
formal classification theorem identifying the family.

\subsection{Response vs selection}

The closure response $\psi = \Cph^{-1} f$ is determined by the
geometry: $\Cph$ is fixed by the substrate $\Rsixhundred$ and the
shift $\Ph^{-2}$, and the response is the resulting linear inverse.
This is a \emph{response} primitive. It does \emph{not} answer:
\begin{itemize}\itemsep=2pt
\item Why this substrate? (Selection across regular 4-polytopes
  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
  positive constant.)
\item How does the system pick a response configuration over
  time? (Crystallisation / Lyapunov descent dynamics on a
  $W$-trajectory.)
\end{itemize}

The selection layer is open. It appears as an open hypothesis in
three independent frames:
\begin{enumerate}\itemsep=2pt
\item \textbf{Forthcoming RH artifact}: the closure-flow suppression
  hypothesis $\textup{H}_{\mathrm{attr}}$ at the level of the
  original cascade closure functional. The polynomial filter
  $\Psi_{t}$ is a finite-dimensional analogue, by design.
\item \textbf{Adaptive Closure
  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
  $V(W)$ on the reduced flow, an edge-space decomposition under
  $2I$-equivariance, and a full reduced-flow convergence theorem
  on $W$-trajectories — \emph{none delivered} in that paper.
\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
  the substrate-witness scope explicitly does \emph{not} deliver
  a selection theorem; ACT is positioned as the future
  selection-theorem witness.
\end{enumerate}

The recurrence of an open selection gap across these three frames
is a programme-level reading: the gap may be a single mathematical
problem rather than three independent ones, but the present paper
gives no proof of equivalence. The two empirical witnesses landed
in this paper strengthen external confidence in the \emph{response}
primitive without reducing or addressing the selection gap.

\subsection{What this paper closes vs leaves open}

\paragraph{Closes (at the operator-witness level).}
\begin{itemize}\itemsep=2pt
\item The operator $\Cph$ is well-defined and positive definite
  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
  with the standard combinatorial Laplacian). On substrates where
  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
  generally strict (\S\ref{sec:definition}).
\item The 600-cell instance $\Rsixhundred$ has the construction
  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
  Table~\ref{tab:spectrum}, both reproduced numerically
  (\texttt{repro/verify\_kernel.py}).
\item Discrete-to-continuum agreement at per-vertex Pearson
  correlation $0.976$ on the unweighted variant, with the unweighted
  variant winning the geometry-only criterion against two
  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
  the load-bearing object in two independent empirical works in
  qualitatively distinct regimes (\S\ref{sec:passive_witness},
  \S\ref{sec:active_witness}).
\end{itemize}

\paragraph{Leaves open.}
\begin{itemize}\itemsep=2pt
\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
  as a design-level shift; not derived from a closure functional
  or symmetry argument.
\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
  post-hoc motivated by the empirical landings; alternative regular
  4-polytopes are an explicit ablation build, not a discharged
  comparison.
\item \emph{Kernel-uniqueness on either empirical landing.} The
  b-anomaly free-width Gaussian alternative (fits comparably with
  one extra shape parameter) and the AIC tie
  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
  inherited verbatim from~\citep{SmartBAnomaly2026}.
\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
  decomposition under $2I$-equivariance, full reduced-flow
  convergence — all explicitly not delivered
  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
  here.
\item \emph{Family-membership theorem.} The programme-home
  positioning of cascade Lyapunov functionals as members of the
  same polynomial-in-$L$ family is reported as
  \emph{programme-positioned}, not formally classified.
\end{itemize}

 succeeded in 286ms:
% =====================================================================
\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
% =====================================================================

This section enumerates limitations transparently, organised as a
five-move guard matrix following the b-anomaly preprint
template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
test/claim, state-drift. For each guard we record
$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
\mathrm{strengthening\ build})$.

\subsection{Regime}\label{ssec:regime}

\textbf{Single substrate (the 600-cell).} We have not tested
whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
Coxeter graphs would give comparable per-vertex correlations on
the discrete-to-continuum agreement test, or comparable structural
fits on either empirical landing. The 600-cell choice is post-hoc
motivated by the empirical landings, not from an a-priori
derivation. \emph{Disclosure:} \S\ref{sec:intro},
\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
empirical landings of \S\ref{sec:passive_witness} and
\S\ref{sec:active_witness}. \emph{Strengthening build:}
\texttt{repro/verify\_kernel.py} extension to the $24$-cell and
$120$-cell, with the same per-vertex correlation criterion
applied; verbatim re-run of the b-anomaly fit on alternative
substrates from~\citep{SmartBAnomaly2026}; the aria-chess
preprint's regime section already lists alternative-polytope
ablation as an open build.

\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
comparable per-vertex correlation, or whether the empirical
landings tolerate a shift sweep. The shift is held fixed across
both regimes; perturbation analysis is an open build.
\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
for $\delta \in \{0.01, 0.05, 0.10, 0.25\}$ on the discrete-to-
continuum correlation; report sensitivity envelope.

\subsection{Post-hoc}\label{ssec:posthoc}

\textbf{The 600-cell choice is post-hoc justified by empirical
observables.} While the construction of $\Rsixhundred$ is
theorem-level rigorous (H$_4$ Coxeter group theory), the choice
of \emph{this} polytope as the discrete substrate instance is
motivated by the empirical landings observed, not by an a-priori
geometric or algebraic argument selecting it over the $24$-cell
or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
\emph{Evidence:} two independent empirical witnesses on
$\Rsixhundred$. \emph{Strengthening build:} formal substrate
ablation (above).

\textbf{The geometry-first variant agreement is not historically
blind on b-anomaly.} Per the b-anomaly preprint's limitations
section, the LHCb 2025 data was inspected first and the
pure-geometry ranking was verified afterward to agree with the
data-$\chi^{2}$ ranking. The two-criterion convergence is
\emph{criterion-independent} (geometry-only correlation here is a
different test from b-anomaly's data $\chi^{2}$) but not
historically pre-registered. \emph{Disclosure:} we inherit the
caveat verbatim. \emph{Strengthening build:} a future blind variant
test would freeze the variant choice before observing the data
$\chi^{2}$.

\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
strictly positive definite; it is not derived from a closure
functional or symmetry argument. \emph{Disclosure:}
\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
same operator with the same shift serves as the basis for two
independent empirical witnesses across qualitatively distinct
regimes (\S\ref{sec:passive_witness},
\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
the $\Ph^{-2}$ shift as the unique stability clamp under a named
regularity criterion (e.g.\ minimum-amplitude amplification on a
specified function class).

\subsection{Interpretation}\label{ssec:interpretation}

\textbf{The discrete-to-continuum agreement is descriptive, not
causal.} The per-vertex correlation $0.976$ between $\psi$ on
$\Rsixhundred$ and the continuum kernel
$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
\emph{computed agreement} between two independently-defined
objects, not a derivation that the discrete operator equals the
continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
this explicitly. \emph{Evidence:} the agreement is at machine
precision in the operator-norm bound and at $\rho = 0.976$ in the
per-vertex correlation. \emph{Strengthening build:} a formal
discrete-continuum convergence proof under a specified large-graph
limit; a continuum limit theorem on H$_n$ Coxeter substrates as
$n \to \infty$.

\textbf{Variant ranking is criterion-dependent.} The unweighted
variant wins on both the geometry-only criterion of this paper
and b-anomaly's data $\chi^{2}$, but neither criterion is the
\emph{unique} natural ranking. Edge-weighted variants outside the
$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
Laplacian) are not tested here. \emph{Strengthening build:}
extend \texttt{repro/verify\_kernel.py} to a wider variant
catalogue.

\subsection{Test/claim}\label{ssec:testclaim}

\textbf{Two independent empirical landings, not formal physics.}
The b-anomaly result is a structural fit (kernel shape held fixed)
under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
aria-chess result is a substrate witness (no claim that the
substrate \emph{is} consciousness). Neither lands a theorem-grade
physics claim on its own domain; both are appropriately
hedged in their own preprints, and we inherit those hedges
verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
their own preregistered or literature-derived thresholds.
\emph{Strengthening build:} more flavour-physics datasets
(LHCb Run~3, Belle~II) for the passive-regime witness;
cross-cohort EEG (TUH, NHM) and cross-parcellation HCP
(Schaefer, Glasser) for the active-regime witness; both already
listed in the respective preprints.

\textbf{Discrete-to-continuum correlation reported on a single pole,
verified across all $|V|$.} The headline per-vertex correlation
$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
source. H$_4$ transitivity predicts the correlation is invariant
under choice of source vertex. \texttt{repro/verify\_kernel.py}
sweeps over all $120$ vertices: every source returns the same
per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
(\texttt{multi\_source\_sweep.max\_minus\_min} in
\texttt{results.json}). The single-pole headline is therefore a
representative, not a sample, of the operator's behaviour under
H$_4$ transitivity.

\subsection{State-drift / out-of-scope}\label{ssec:scope}

\textbf{Selection layer not delivered.} As enumerated in
\S\ref{sec:programme_home}, the selection-layer constructions
(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
full reduced-flow convergence) are open in the companion ACT
preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
delivered here. The two empirical witnesses strengthen confidence
in the response primitive without addressing the selection gap.

\textbf{No deuteron / hadron / RH / capstone material is loaded
into this paper.} The cascade-derivation programme, the capstone
coalgebra paper, and the Millennium drafts share operator-level
infrastructure with this paper but are not load-bearing here.
Deliberately out of scope.

\textbf{Out-of-scope items NOT delivered (correctly).}
\begin{itemize}\itemsep=2pt
\item Lyapunov function $V(W)$ on the reduced flow — open build
  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
\item $2I$-equivariance audit of the closure operator family —
  open build of ACT.
\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
  Hodge edge Laplacian — open build of ACT.
\item Selection theorem identifying $\Rsixhundred$ over alternative
  regular 4-polytopes — see \S\ref{ssec:regime}.
\item Formal discrete-to-continuum convergence theorem under a
  specified large-graph limit — see \S\ref{ssec:interpretation}.
\item First-principles derivation of the $\Ph^{-2}$ shift — see
  \S\ref{ssec:posthoc}.
\item Family-membership classification theorem for the
  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
\end{itemize}

\subsection{The honest verdict}

The result is an \emph{operator witness}: a geometry-fixed response
operator on a fixed graph, with no shape parameters tuned to any
dataset, is consistent with two independent empirical landings in
qualitatively distinct regimes. We do not claim the operator is
the unique kernel for either landing. We do not claim selection is
delivered. We do not claim 600-cell uniqueness. The strengthening
builds for stronger claims are listed above and remain open.

exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/sections/10_conclusion.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' 'papers/aria-closure-kernel/repro/results.json'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,320p' 'papers/aria-closure-kernel/repro/verify_kernel.py'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,280p' 'docs/aria-closure-kernel.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 264ms:
@book{CoxeterRegularPolytopes,
  author    = {Coxeter, H. S. M.},
  title     = {Regular Polytopes},
  publisher = {Dover},
  edition   = {3rd},
  year      = {1973},
  address   = {New York}
}

@misc{Weisstein600Cell,
  author       = {Weisstein, Eric W.},
  title        = {{600-Cell}},
  howpublished = {From MathWorld --- A Wolfram Web Resource},
  url          = {https://mathworld.wolfram.com/600-Cell.html},
  note         = {Accessed 2026-04-30}
}

% Companion VFD preprints (the two empirical witnesses + selection-layer paper).

@unpublished{SmartBAnomaly2026,
  author = {Smart, Lee},
  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
            angular anomaly: sign-uniform cross-dataset and cross-channel fit},
  year   = {2026},
  note   = {VFD preprint}
}

@unpublished{SmartAriaChess2026,
  author = {Smart, Lee},
  title  = {A geometry-fixed substrate witness for cortical signatures:
            eighteen preregistered correspondences and six drug/sleep EEG
            signatures from the 600-cell under H$_4$ Coxeter symmetry},
  year   = {2026},
  note   = {VFD preprint, papers/aria-chess-paper/}
}

@unpublished{SmartAdaptiveClosureTransport2026,
  author = {Smart, Lee},
  title  = {Adaptive Closure Transport: a 4-tuple bridge
            $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to
            selection},
  year   = {2026},
  note   = {VFD preprint, papers/adaptive-closure-transport/}
}

% External flavour-physics literature (b-anomaly context, cited in §6).

@article{KrugerMatias2005,
  author  = {Kr\"uger, Frank and Matias, Joaquim},
  title   = {Probing new physics via the transverse amplitudes of
             $B^0 \to K^{*0} (\to K^- \pi^+) l^+ l^-$ at low recoil},
  journal = {Phys. Rev. D},
  volume  = {71},
  pages   = {094009},
  year    = {2005},
  doi     = {10.1103/PhysRevD.71.094009}
}

@article{LHCbAngular2020,
  author  = {{LHCb Collaboration}},
  title   = {Measurement of $\mathit{CP}$-averaged observables in the
             $B^0 \to K^{*0} \mu^+ \mu^-$ decay},
  journal = {Phys. Rev. Lett.},
  volume  = {125},
  pages   = {011802},
  year    = {2020},
  doi     = {10.1103/PhysRevLett.125.011802}
}

 succeeded in 279ms:
% =====================================================================
\section{Conclusion}\label{sec:conclusion}
% =====================================================================

The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
geometry-fixed response primitive: positive definite under (H1)--(H3)
on the substrate $(M, L_M)$, with smallest eigenvalue $\Ph^{-2}$
and operator-norm bound $\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$.
The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
Laplacian spectrum that numerically resolves to the closed-form
$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
the unweighted Laplacian, above the two $\Ph$-cocycle weighted
variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
generators by \texttt{repro/verify\_kernel.py}; no parameter is
fitted.

\textbf{Two independent empirical landings.} The same fixed
$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
retuning between regimes, appears as the load-bearing object in:
\begin{enumerate}\itemsep=2pt
\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
  fitted dimensionless amplitude $A$ per dataset (kernel shape
  held fixed) gives a sign-uniform
  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
  $B_s\to\phi$).
\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
  recurrent self-model layer above the same operator (one
  condition-dependent self-injection coupling
  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
  degree) passes eighteen preregistered cortical correspondences
  (frozen 2026-04-18) and six drug/sleep EEG signatures.
\end{enumerate}
By design, the two witnesses share exactly the geometry-fixed
operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
$\Ph^{-2}$. They share no fitted parameter, threshold, dataset,
or methodological choice above the operator level, and the
empirical claims are tested on disjoint physical domains (flavour
physics vs cortical neuroscience). Independence here is
independence at the empirical layer above the shared operator,
not statistical independence of the operator itself.

\textbf{Operator-witness scope.} This is an operator witness, not
a derivation of physics on either landing. We do not derive the
$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
claim 600-cell uniqueness; alternative regular 4-polytopes are an
explicit ablation build. We do not claim kernel uniqueness on
either empirical landing; the b-anomaly's free-width Gaussian
alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
aria-chess substrate-witness scope is inherited verbatim. We do
not deliver a selection theorem on the ACT
4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
open builds (Lyapunov $V(W)$, edge-space decomposition under
$2I$-equivariance, full reduced-flow convergence) remain open and
are not delivered here.

\textbf{Programme position.} The cascade-programme home for the
polynomial-in-$L$ Lyapunov family — RH polynomial filter
($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
identified in \S\ref{sec:programme_home}. Family-membership is
\emph{programme-positioned}, not formally classified. The two
empirical landings strengthen external confidence in the
\emph{response} primitive without reducing or addressing the
selection gap.

We are not aware of a prior preprint that simultaneously names a
geometry-fixed Green operator on a fixed Coxeter graph, with a
design-level mass shift not retuned between regimes, and threads
two independent empirical landings on qualitatively distinct
physical domains. We cannot rule out that such prior work exists.
The empirical material gathered here is the operator witness; the
broader programme to convert the witness into a selection-theorem-
grade claim is sketched in the companion preprints and remains
the natural next step.

 succeeded in 231ms:
# ARIA Closure-Response Green Kernel and the Cascade Programme

**Status (2026-04-29).** Programme-level vocabulary: response
primitive defined; externally witnessed by a structural sign-uniform
test (b-anomaly paper, §4 below) without a model-preference claim;
selection / crystallisation dynamics still open. This note is
non-load-bearing for any individual Millennium paper; it documents
the programme-wide home for the polynomial-in-$L$ Lyapunov family
that recurs across the Millennium drafts.

## 1. The closure-response operator

Let $M$ be a closure substrate (graph, simplicial complex, or
projected coordinate). Let $L_M$ be its Laplacian. Define the
**$\varphi$-regularised closure operator**
$$
C_\varphi \;=\; L_M + \varphi^{-2} I.
$$
For a non-negative localised source $f$ on $M$, the **closure
response field** is
$$
\psi \;=\; C_\varphi^{-1} f \;=\; (L_M + \varphi^{-2} I)^{-1} f.
$$
This is a Green's-function inverse. For self-adjoint non-negative
$L_M$ on $M$ (e.g. the standard graph Laplacian on a connected
finite graph, or the standard continuum Laplace operator with
free-space / decay-at-infinity boundary conditions), $C_\varphi$
is positive definite and $\varphi^{-2}$ acts as a coherence-length /
mass regularisation; for a non-negative source $f$ on such an $M$,
$\psi$ is non-oscillatory and centred on the support of $f$. In
the continuum case with smooth $f$, $\psi$ is regular away from
the singular support of $f$. (On a finite graph, "smoothness" is
not directly meaningful; the regularity statement is a discrete
exponential-decay envelope around the source, not a derivative
condition.) Substrates outside this hypothesis class (e.g.
projected coordinates with non-standard boundary conditions, or
Laplacians with negative spectrum) require their own analysis.

## 2. Continuum projection

In one projected coordinate $x$, $L_\varphi = -d^2/dx^2 + \varphi^{-2}$,
$L_\varphi G = \delta$, with closed-form Green's function
$$
G(x) \;=\; \frac{\varphi}{2}\, e^{-|x|/\varphi}.
$$
Normalised, this is the practical kernel
$\kappa(x) = e^{-|x|/\varphi}$. The decay scale is $\varphi$.

## 3. Discrete substrate: the 600-cell

The discrete VFD lift uses the 600-cell graph $V_{600}$:
- 120 vertices, 720 edges, each vertex degree 12;
- edges defined by $\langle v, w \rangle = \varphi/2$;
- 9-shell decomposition emerging intrinsically as
  $\{1, 12, 20, 12, 30, 12, 20, 12, 1\}$;
- antipodal symmetry $s(-v) = 8 - s(v)$.

The discrete response is
$\psi(v) = (L_{V_{600}} + \varphi^{-2} I)^{-1} f(v)$.

**Compression diagnostic.** The b-anomaly headline fits use the
full Green response on $V_{600}$. A spectral truncation diagnostic
(`archive/reports/wo011_spectral.csv`) reports the relative
reconstruction error stepping from $0.076$ (modes 1-8, with
$\lambda_{\max}$ reaching $5.528$ at mode 6) to $0.040$ (modes
9-14) and remaining at $0.040$ through mode 30; mode 15 marks the
entry of the truncation into the $\lambda = 9$ block, not an
additional error drop. This is a *spectral diagnostic of
compression depth*, not a rank-1 projection map; the b-anomaly
fits do not use the truncation. (The canonical full spectrum of
the $V_{600}$ Laplacian has eigenvalue $9$ with multiplicity $16$;
the multiplicity-6 figure originally reported in some prose is
not consistent with the canonical spectrum or with the b-anomaly's
own wo011 CSV and is dropped here.)

## 4. Empirical validation: shipped five-dataset b-anomaly structural test

Independent passive-regime witness for $C_\varphi$ ships in the
b-anomaly repository (`/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/`,
preprint `paper/main.pdf`, repro `repro/run_all.sh`). The witness is
a **structural** test, not a detection claim or AIC preference:

> A single fixed response kernel $\kappa(q^{2})$ — derived from the
> 600-cell $V_{600}$ graph regularised by $\varphi^{-2}$ as a
> discrete mass scale, with no shape parameters tuned to data —
> provides a consistent description of the $q^{2}$ behaviour of the
> $b\to s\mu^{+}\mu^{-}$ angular anomaly across **five public
> datasets covering two collaborations, two isospin partners, and
> three decay channels**. Only one dimensionless amplitude $A$ is
> fitted per dataset; the kernel shape itself never moves.

**Per-dataset table** (verbatim from `BANOMALY-001/vfd-b-anomaly/README.md`):

| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
|---|---|---:|---:|---:|---:|
| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |

**What the b-anomaly paper claims (source scope; bullets summarise from `README.md:24-28` plus paper §§6-7 detail):**

- **Universality.** Same fixed kernel for all five datasets, one
  amplitude per dataset, no shape retuning.
- **Sign uniformity.** $A>0$ in **5/5** fits;
  $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel
  reproduces the established direction of the anomaly across all
  five independent measurements.
- **Cross-channel ratio.** $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
  amplitudes differ by a factor partly explained by the predicted
  Krüger–Matias $P$/$S$-basis amplification ($\sim 2.2$). The
  detailed cross-channel section reports a predicted amplitude of
  $+2.5$ vs the observed $+4.98$, leaving a factor $\sim 2$
  residual gap that the basis-amplification prediction does not
  account for.
- **Geometry-first variant test.** Of three discrete Laplacian
  variants, the unweighted choice wins on a pure-geometry criterion
  (correlation $0.997$ with the continuum kernel); the same variant
  also wins on the data $\chi^{2}$ — independent geometry and data
  criteria agree. The two-criterion agreement is criterion-independent
  but not historically blind: the b-anomaly limitations section
  (`paper/sections/09_limitations.tex`) acknowledges that the data
  was looked at first and only later verified to agree with the
  pure-geometry ranking.

**Statistical caveat (what the b-anomaly paper does NOT claim):**

- On Akaike model comparison, the kernel and a constant
  Wilson-coefficient shift ($\mathrm{FREE\_C9}$, also $k=1$) are
  statistically indistinguishable on current data: stacked
  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
  Current data cannot resolve the model comparison. AIC is blind to
  the universality/shape-prediction claim itself.
- In the Mode-B stress test, a free-width Gaussian charm-loop
  proxy fits comparably in $\chi^{2}$ at the cost of one extra
  shape parameter; the kernel is *not* the unique $q^{2}$ shape
  consistent with the anomaly.
- An earlier linearised "Mode B" analysis gave a stronger
  numerical preference for the kernel
  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that **did not
  survive the non-linear refit**. The $+2.77$-AIC-unit drift is the
  largest single methodological uncertainty in the project.

**Cocycle convergence (operator-level, not edge-weight-level).**
The b-anomaly geometry-first variant test compares three discrete
edge-weighting schemes on $V_{600}$ — `UNWEIGHTED`,
`PHI_GEOMETRIC` ($w_{vw} = \sqrt{\omega_+(v)\,\omega_+(w)}$ with
$\omega_+(v) = \varphi^{\kappa(v)}$), and `PHI_ARITHMETIC`
($w_{vw} = \tfrac{1}{2}[\omega_+(v) + \omega_+(w)]$) — under
both a pure-geometry criterion (correlation with the continuum
kernel) and a data criterion (LHCb 2025 $\chi^2$). The
`UNWEIGHTED` Laplacian variant wins on both criteria
(correlation $0.9968$ with the continuum kernel, data
$\chi^2 = 13.555$; b-anomaly paper §3.4 Table 1, also
`reports/wo016b_variant_geometry.md`). The φ-cocycle-weighted
variants ($\omega_+(v) = \varphi^{\kappa(v)}$) are tested and
**lose** on both criteria. So the b-anomaly result empirically
strengthens the **unweighted** $L_{V_{600}} + \varphi^{-2} I$
response operator and the 9-shell projection (which enters at the
shell-mean step, not as an edge weight); it does **not**
empirically strengthen the κ cocycle as an operative edge
weighting.

The cocycle convergence with the RH paper's pentagonal-clock
$\kappa(v) = (s(v) - 4)^2$ (`papers/millennium-rh-formal/rh-formal.tex`,
Definition `def:kappa`) is therefore **structural**: the same
shell-grade pattern $\varphi^{0,1,4,9,16}$ shows up in both the
discrete VFD lift's variant catalogue and the RH paper's cocycle.
This is a theoretical convergence on a shared algebraic shell-grade
infrastructure, not an empirical claim. ẑ **shares operator-level
infrastructure** with the b-anomaly response operator (the same
$V_{600} + \varphi^{-2} I$, the same 9-shell decomposition, the
same shell-grade pattern $\varphi^{0,1,4,9,16}$); ẑ does **not**
inherit any empirical claim about classical RH or the critical
line.

## 5. Programme home for cascade Lyapunov / projector functionals

Several cascade-internal constructions are $L$-symmetric
polynomial-in-$L$ functionals on a finite-dimensional substrate.
They are positioned as programme-proposed members of the same
family as $C_\varphi$ (the family-membership claim is not formally
canonical and is not proved in any of the cited Millennium drafts):

- **RH polynomial filter** (`rh-formal.tex`,
  `def:closure_flow`): $F_{\mathrm{filt}}(x)
  = \tfrac{1}{2}\langle x, p_{\mathrm{fix}}(L)^2 x\rangle$ with
  $\Psi_t = e^{-t\,p_{\mathrm{fix}}(L)^2}$. Programme-positioned
  as the **σ-fix-annihilator** instance of the family: a
  degree-$10$ positive functional on $\R^{120}$ vanishing exactly
  on $V_{\mathrm{fix}}$.
- **YM cascade gap operator** (`ym-mass-gap.tex`,
  Section~\ref{sec:cascade-gap}): the discrete cascade gap
  Hamiltonian is programme-positioned as a $C_\varphi$-style
  mass-regularised Laplacian on the 600-cell substrate.
- **NS regularity functional** (`ns-formal.tex`): the cascade
  hydrodynamic projector is programme-positioned in the same
  Lyapunov-of-polynomial-in-$L$ family.
- **BSD operator** (`bsd-formal.tex`): $T_E$ on the enlarged
  Hecke module is programme-positioned as a
  response-operator-family member.
- **Hodge $\sigma$-projector** (`hodge-formal.tex`): the cascade
  $\sigma$-projector is programme-positioned as a rank-1 /
  spectral-projection limit of the same family.
- **PNP cascade refinement** (`pnp-formal.tex`): the cascade
  refinement on the restricted model class is programme-positioned
  as a response-kernel projection in the bounded-resource regime.

In each case the cascade construction is positioned as a
programme-proposed family instance, selected by the structural role
it plays in the corresponding Millennium reduction. These are not
arbitrary constructions, but the family-membership claim is not
formally canonical and is not proved in any of the cited papers.

## 6. Response vs selection: the open layer

The closure response primitive now has a **shipped passive-regime
empirical landing**: the b-anomaly paper (§4 above) tests the fixed
$C_\varphi$-derived $V_{600}$ kernel without shape retuning across
five public flavour-physics datasets covering two collaborations,
two isospin partners, and three decay channels. This **does not
close the selection layer**. The active-regime companion remains
the ARIA / aria-chess selection paper: a learning-rule / Lyapunov /
coherence-descent construction for $W$-space, *not supplied* by
b-anomaly.

The closure response $\psi = C_\varphi^{-1} f$ is derived from
geometry. It is *not* a selection rule. Crystallisation
additionally requires a selection dynamic — a Lyapunov / coherence
descent rule
$$
dW/dt \;=\; -\nabla V(W)
$$
or equivalent — that selects which response is the stable
attractor.

This selection layer is **open**. The same gap appears in three
independent frames:
- **RH paper**: open $\textup{H}_{\mathrm{attr}}$ at the level of
  the original cascade closure functional (the polynomial filter
  $\Psi_t$ is only a finite-dimensional analogue, by design).
- **Adaptive Closure Transport** (`papers/adaptive-closure-transport/`):
  edge-space lift / Lyapunov mechanism for the selection programme,
  explicitly left open (lines 327--328, 377--382 of that paper).
- **ARIA framework**: crystallisation / coherence-descent rule,
  named as the next layer above response. The aria-chess paper
  (active-regime empirical companion to adaptive-closure-transport)
  is **named, not yet written**.

The convergence of the gap across these three frames is the
strongest programme-level indication that the gap is a single
mathematical problem rather than three independent ones (a
programme-level reading, not a proof of equivalence). The
passive-regime b-anomaly landing strengthens external confidence
in the *response* primitive without reducing or addressing the
selection gap.

## 7. Canonical references in this repository

- `papers/millennium-rh-formal/rh-formal.tex` — polynomial filter
  $F_{\mathrm{filt}}$ as σ-fix-annihilator family member (closing
  subsection).
- `papers/millennium-ym/ym-mass-gap.tex` — cascade gap operator as
  $C_\varphi$-style member.
- `papers/millennium-ns-formal/ns-formal.tex` — regularity
  functional as family member.
- `papers/millennium-bsd-formal/bsd-formal.tex` — $T_E$ as
  family member.
- `papers/millennium-hodge-formal/hodge-formal.tex` — σ-projector
  as rank-1 limit.
- `papers/millennium-pnp-formal/pnp-formal.tex` — cascade
  refinement as response-kernel projection.
- `papers/adaptive-closure-transport/adaptive-closure-transport.tex` —
  selection layer, open.
- `docs/convergence-with-smart.md` — programme-level architectural
  consilience between cascade and Smart frames.
- `docs/projection-narrative.md` (and related) — Layer 1 mainstream
  coherence earning Layer 2 realisation.
- `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf` —

 succeeded in 239ms:
#!/usr/bin/env python3
"""
Aria closure kernel — numerical verification.

Constructs V_600 from canonical generators, builds the short-edge
nearest-neighbour graph, computes the Laplacian spectrum, builds
C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
test (shell-mean projection vs (phi/2) exp(-|x|/phi)), tests the
unweighted vs phi-cocycle-weighted Laplacian variants on a
geometry-only correlation criterion, and writes results.json.

All constants (phi, the 600-cell vertex generators, the short-edge
inner product phi/2) are mathematically determined by the choice of
substrate; no parameter is fitted to any dataset.

Determinism: numpy RNG is seeded only for the localised-source
positions (seed 42); the eigendecomposition is deterministic.

Run: python3 verify_kernel.py
"""

from __future__ import annotations

import json
import itertools
import math
from pathlib import Path

import numpy as np
from numpy.linalg import eigh, norm
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
INV_PHI = 1.0 / PHI                          # = phi - 1
INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966


# ---------------------------------------------------------------------------
# 1. 600-cell vertex construction (120 vertices on S^3)
# ---------------------------------------------------------------------------

def even_perms(seq):
    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    n = len(seq)
    out = []
    for p in itertools.permutations(range(n)):
        # signature
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        if inv % 2 == 0:
            out.append(tuple(seq[p[i]] for i in range(n)))
    return out


def build_v600():
    """
    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.

    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    - 16 vertices: all sign combinations of (+/- 1/2)^4
    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
      with all sign assignments
    """
    verts = set()

    # 8 axis vertices
    for sign in (-1, 1):
        for i in range(4):
            v = [0.0] * 4
            v[i] = float(sign)
            verts.add(tuple(v))

    # 16 half-integer vertices
    for signs in itertools.product((-1, 1), repeat=4):
        v = tuple(0.5 * s for s in signs)
        verts.add(v)

    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    for signs in itertools.product((-1, 1), repeat=4):
        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
        signed = tuple(s * b for s, b in zip(signs, base))
        for p in even_perms(signed):
            verts.add(p)

    V = np.array(sorted(verts), dtype=np.float64)
    # Sanity check: all on the unit 3-sphere
    radii = np.linalg.norm(V, axis=1)
    assert np.allclose(radii, 1.0, atol=1e-10), \
        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    return V


# ---------------------------------------------------------------------------
# 2. Short-edge nearest-neighbour graph
# ---------------------------------------------------------------------------

def build_short_edge_graph(V, tol=1e-10):
    """
    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
    criterion on the unit 3-sphere). For the 600-cell this gives a
    12-regular graph on 120 vertices with 720 edges.
    """
    G = V @ V.T  # Gram matrix of inner products
    short = PHI / 2.0
    A = (np.abs(G - short) < tol).astype(np.float64)
    np.fill_diagonal(A, 0.0)  # no self-loops
    return A


# ---------------------------------------------------------------------------
# 3. Laplacian spectrum
# ---------------------------------------------------------------------------

def laplacian_spectrum(A):
    """L = D - A; return sorted eigenvalues + eigenvectors."""
    D = np.diag(A.sum(axis=1))
    L = D - A
    w, U = eigh(L)  # ascending order
    return L, w, U


def round_spectrum(w, decimals=6):
    """Group eigenvalues into multiplicity classes (within numerical tol)."""
    classes = []
    seen = []
    for val in w:
        placed = False
        for idx, ref in enumerate(seen):
            if abs(val - ref) < 10 ** (-decimals):
                classes[idx] = (ref, classes[idx][1] + 1)
                placed = True
                break
        if not placed:
            seen.append(val)
            classes.append((round(float(val), decimals), 1))
    return classes


# ---------------------------------------------------------------------------
# 4. Closure operator and discrete Green's function
# ---------------------------------------------------------------------------

def build_C_phi(L):
    """C_phi = L + phi^-2 I."""
    return L + INV_PHI2 * np.eye(L.shape[0])


def green_response(C_phi, source_idx):
    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
    n = C_phi.shape[0]
    f = np.zeros(n)
    f[source_idx] = 1.0
    psi = np.linalg.solve(C_phi, f)
    return psi


# ---------------------------------------------------------------------------
# 5. Shell decomposition (9-shell H_3 partition)
# ---------------------------------------------------------------------------

def shell_indices(V, pole_idx):
    """
    Group vertices by their inner product with V[pole_idx]. The 600-cell's
    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
    """
    pole = V[pole_idx]
    inner = V @ pole
    # The 9 canonical inner-product values:
    canonical = np.array([
        1.0,                # shell 0: pole itself
        PHI / 2.0,          # shell 1
        0.5,                # shell 2
        1.0 / (2.0 * PHI),  # shell 3
        0.0,                # shell 4 (equator)
        -1.0 / (2.0 * PHI), # shell 5
        -0.5,               # shell 6
        -PHI / 2.0,         # shell 7
        -1.0,               # shell 8: antipode
    ])
    shells = {k: [] for k in range(9)}
    for i, val in enumerate(inner):
        # snap to nearest canonical
        k = int(np.argmin(np.abs(canonical - val)))
        shells[k].append(i)
    sizes = {k: len(shells[k]) for k in shells}
    return shells, sizes, canonical


# ---------------------------------------------------------------------------
# 6. Discrete <-> continuum agreement test
# ---------------------------------------------------------------------------

def discrete_continuum_test(V, C_phi, source_idx):
    """
    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
    shell radial coordinate x is the chord distance |v - v_source|. The
    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).

    Returns the per-shell discrete mean, the continuum prediction at each
    shell radius, and the Pearson correlation between them.
    """
    psi = green_response(C_phi, source_idx)
    shells, sizes, _ = shell_indices(V, source_idx)
    pole = V[source_idx]

    shell_means = []
    shell_radii = []
    shell_count = []
    for k in range(9):
        idxs = shells[k]
        if not idxs:
            continue
        mean_psi = float(np.mean(psi[idxs]))
        # mean chord radius from pole
        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
        shell_means.append(mean_psi)
        shell_radii.append(chord)
        shell_count.append(len(idxs))

    shell_means = np.array(shell_means)
    shell_radii = np.array(shell_radii)
    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)

    # Pearson correlation of (discrete shell mean) with (continuum prediction)
    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
    else:
        corr = float("nan")

    return {
        "shell_radii": shell_radii.tolist(),
        "shell_count": shell_count,
        "shell_psi_mean": shell_means.tolist(),
        "continuum_prediction": continuum.tolist(),
        "pearson_correlation": corr,
    }


# ---------------------------------------------------------------------------
# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
# ---------------------------------------------------------------------------

def cocycle_weights(V, source_idx):
    """
    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
    the shell index of v with respect to a chosen pole. For the variant
    test we compare the unweighted graph Laplacian to two weighted variants
    discussed in the b-anomaly paper.
    """
    shells, _, _ = shell_indices(V, source_idx)
    kappa = np.zeros(V.shape[0])
    for k, idxs in shells.items():
        for i in idxs:
            kappa[i] = float(k)
    return PHI ** kappa


def weighted_laplacian(A, weights, mode="geometric"):
    """
    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
    """
    n = A.shape[0]
    if mode == "geometric":
        W = np.sqrt(np.outer(weights, weights))
    elif mode == "arithmetic":
        W = 0.5 * (weights[:, None] + weights[None, :])
    else:
        raise ValueError(mode)
    A_w = A * W
    D_w = np.diag(A_w.sum(axis=1))
    return D_w - A_w


def variant_correlation(V, A, source_idx, variant):
    if variant == "UNWEIGHTED":
        L_v = np.diag(A.sum(axis=1)) - A
    else:
        weights = cocycle_weights(V, source_idx)
        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
        L_v = weighted_laplacian(A, weights, mode=mode)
    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
    test = discrete_continuum_test(V, C_v, source_idx)
    psi = green_response(C_v, source_idx)
    pole = V[source_idx]
    chord = np.linalg.norm(V - pole, axis=1)
    # Continuum kernel at each vertex's chord radius
    cont = (PHI / 2.0) * np.exp(-chord / PHI)
    # Per-vertex correlation (excluding the source itself, which is degenerate)
    mask = np.arange(V.shape[0]) != source_idx
    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
    else:
        per_vertex_corr = float("nan")
    return {
        "shell_mean_correlation": test["pearson_correlation"],
        "per_vertex_correlation": per_vertex_corr,
        "test": test,
    }


# ---------------------------------------------------------------------------
# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
# ---------------------------------------------------------------------------

def connectivity_check(A):
    """
    Numerical connectedness verification: count connected components of the
    short-edge adjacency matrix. Connectedness is reported, not derived from
    a structural argument.
    """
    n_components, _ = connected_components(csr_matrix(A), directed=False)
    return {
        "n_connected_components": int(n_components),
        "connected": bool(n_components == 1),
    }

 succeeded in 305ms:
{
  "phi": 1.618033988749895,
  "phi_inv_sq": 0.3819660112501051,
  "n_vertices": 120,
  "n_edges": 720,
  "degree_sequence": {
    "min": 12,
    "max": 12,
    "mean": 12.0
  },
  "connectivity": {
    "n_connected_components": 1,
    "connected": true
  },
  "shell_sizes": {
    "0": 1,
    "1": 12,
    "2": 20,
    "3": 12,
    "4": 30,
    "5": 12,
    "6": 20,
    "7": 12,
    "8": 1
  },
  "shell_inner_products": [
    1.0,
    0.8090169943749475,
    0.5,
    0.3090169943749474,
    0.0,
    -0.3090169943749474,
    -0.5,
    -0.8090169943749475,
    -1.0
  ],
  "antipodal_check": {
    "pole_idx": 119,
    "antipode_idx": 0,
    "expected_shell_8_size": 1,
    "observed_shell_8_size": 1
  },
  "laplacian_spectrum_grouped": [
    {
      "eigenvalue": -0.0,
      "multiplicity": 1
    },
    {
      "eigenvalue": 2.291796067500629,
      "multiplicity": 4
    },
    {
      "eigenvalue": 5.527864045000407,
      "multiplicity": 9
    },
    {
      "eigenvalue": 8.999999999999993,
      "multiplicity": 16
    },
    {
      "eigenvalue": 11.999999999999984,
      "multiplicity": 25
    },
    {
      "eigenvalue": 13.999999999999977,
      "multiplicity": 36
    },
    {
      "eigenvalue": 14.472135954999567,
      "multiplicity": 9
    },
    {
      "eigenvalue": 14.999999999999988,
      "multiplicity": 16
    },
    {
      "eigenvalue": 15.708203932499362,
      "multiplicity": 4
    }
  ],
  "operator_norm": {
    "lambda_min_L": -1.01103545984405e-15,
    "lambda_min_C_phi": 0.3819660112501041,
    "operator_norm_C_phi_inv": 2.618033988749902,
    "predicted_phi_squared": 2.618033988749895
  },
  "discrete_continuum_test": {
    "shell_radii": [
      0.0,
      0.6180339887498948,
      1.0,
      1.1755705045849465,
      1.4142135623730947,
      1.618033988749895,
      1.7320508075688772,
      1.902113032590307,
      2.0
    ],
    "shell_count": [
      1,
      12,
      20,
      12,
      30,
      12,
      20,
      12,
      1
    ],
    "shell_psi_mean": [
      0.11466009151487011,
      0.034976446331995696,
      0.024335208435661275,
      0.021858804323929084,
      0.019268782150762213,
      0.01765857292134354,
      0.016902552852001883,
      0.015932370381507646,
      0.01544087945358437
    ],
    "continuum_prediction": [
      0.8090169943749475,
      0.5521688638304681,
      0.43606265394423777,
      0.3912228691703586,
      0.33757505628626344,
      0.29762071978885557,
      0.2773703603621507,
      0.24969730865080123,
      0.23503911473677247
    ],
    "pearson_correlation": 0.9232082699765517
  },
  "variant_correlation": {
    "UNWEIGHTED": {
      "shell_mean_correlation": 0.9232082699765517,
      "per_vertex_correlation": 0.9762022978516623
    },
    "PHI_GEOMETRIC": {
      "shell_mean_correlation": 0.879553132802029,
      "per_vertex_correlation": 0.8883800503732451
    },
    "PHI_ARITHMETIC": {
      "shell_mean_correlation": 0.8784315463215415,
      "per_vertex_correlation": 0.8843640031310793
    }
  },
  "multi_source_sweep": {
    "n_sources": 120,
    "min_correlation": 0.9762022978516617,
    "mean_correlation": 0.9762022978516628,
    "max_correlation": 0.9762022978516637,
    "max_minus_min": 1.9984014443252818e-15
  }
}
exec
/bin/bash -lc "sed -n '320,700p' 'papers/aria-closure-kernel/repro/verify_kernel.py'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '280,620p' 'docs/aria-closure-kernel.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,320p' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"AIC|Mode-B|Mode B|Gaussian|0\\.348|0\\.652|13\\.555|0\\.9968|0\\.997|2\\.77|FREE_C9|free-width|linearised|non-linear|LHCb 2025|variant|correlation\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg --files 'papers/aria-chess-paper/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 301ms:
    }


def multi_source_sweep(V, C_phi):
    """
    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
    predicts the correlation is invariant under choice of source vertex; this
    function verifies the prediction numerically across all 120 sources and
    reports the min/mean/max envelope.
    """
    n = V.shape[0]
    corrs = np.zeros(n)
    for source_idx in range(n):
        psi = green_response(C_phi, source_idx)
        chord = np.linalg.norm(V - V[source_idx], axis=1)
        cont = (PHI / 2.0) * np.exp(-chord / PHI)
        mask = np.arange(n) != source_idx
        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
    return {
        "n_sources": int(n),
        "min_correlation": float(corrs.min()),
        "mean_correlation": float(corrs.mean()),
        "max_correlation": float(corrs.max()),
        "max_minus_min": float(corrs.max() - corrs.min()),
    }


def operator_norm_check(L, w):
    lam_min_L = float(w[0])           # 0
    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
    op_norm = 1.0 / lam_min_C         # phi^2
    return {
        "lambda_min_L": lam_min_L,
        "lambda_min_C_phi": lam_min_C,
        "operator_norm_C_phi_inv": op_norm,
        "predicted_phi_squared": PHI ** 2,
    }


# ---------------------------------------------------------------------------
# 9. Run everything and write results.json
# ---------------------------------------------------------------------------

def main():
    out_path = Path(__file__).parent / "results.json"

    V = build_v600()
    n = V.shape[0]
    A = build_short_edge_graph(V)
    deg = A.sum(axis=1)
    n_edges = int(A.sum() // 2)

    L, w, U = laplacian_spectrum(A)
    spectrum = round_spectrum(w, decimals=4)

    C_phi = build_C_phi(L)
    op_norm = operator_norm_check(L, w)
    connectivity = connectivity_check(A)
    multi_source = multi_source_sweep(V, C_phi)

    # Pick the +x_0 axis vertex as canonical pole/source.
    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
    pole = V[pole_idx]

    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)

    test = discrete_continuum_test(V, C_phi, pole_idx)

    # Variant comparison on the same source
    variants = {}
    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
        out = variant_correlation(V, A, pole_idx, variant)
        variants[variant] = {
            "shell_mean_correlation": out["shell_mean_correlation"],
            "per_vertex_correlation": out["per_vertex_correlation"],
        }

    result = {
        "phi": PHI,
        "phi_inv_sq": INV_PHI2,
        "n_vertices": n,
        "n_edges": n_edges,
        "degree_sequence": {
            "min": int(deg.min()),
            "max": int(deg.max()),
            "mean": float(deg.mean()),
        },
        "connectivity": connectivity,
        "shell_sizes": shell_sizes,
        "shell_inner_products": canonical_inner.tolist(),
        "antipodal_check": {
            "pole_idx": pole_idx,
            "antipode_idx": int(np.argmin(V @ pole)),
            "expected_shell_8_size": 1,
            "observed_shell_8_size": shell_sizes.get(8, 0),
        },
        "laplacian_spectrum_grouped": [
            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
        ],
        "operator_norm": op_norm,
        "discrete_continuum_test": test,
        "variant_correlation": variants,
        "multi_source_sweep": multi_source,
    }

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    # Headline summary
    print("=" * 60)
    print("ARIA Closure Kernel — verification")
    print("=" * 60)
    print(f"|V|           = {n}  (expected 120)")
    print(f"|E|           = {n_edges}  (expected 720)")
    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
    print(f"connected      = {connectivity['connected']}  "
          f"(components = {connectivity['n_connected_components']})")
    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
    print()
    print("Laplacian spectrum (eigenvalue, multiplicity):")
    for ev, m in spectrum:
        print(f"  {ev:>8.4f}   x {m}")
    print()
    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
    print()
    print("Discrete <-> continuum agreement (Pearson correlation):")
    print(f"  variant         | shell-mean  | per-vertex")
    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
        sm = variants[v]["shell_mean_correlation"]
        pv = variants[v]["per_vertex_correlation"]
        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
    print()
    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
    print()
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

 succeeded in 278ms:
# vfd-b-anomaly

**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/paper-PDF-blue)](paper/main.pdf)

This repository accompanies the preprint **[paper/main.pdf](paper/main.pdf)**. It contains all source code, processed data, intermediate result tables, and figures needed to reproduce every number in the paper from a clean checkout.

---

## Headline result

A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.

| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
|---|---|---:|---:|---:|---:|
| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |

**What the data shows:**
- **Universality.** The same fixed kernel describes all five datasets with one amplitude each — no shape retuning across datasets, channels, or isospin partners.
- **Sign uniformity.** $A>0$ in **5/5** fits; $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel reproduces the established direction of the anomaly across all five independent measurements.
- **Cross-channel ratio.** The $B\to K^{*}$ vs $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with the predicted Krüger–Matias $P$-basis vs $S$-basis amplification ($\sim 2.2$), with a residual $\sim 50\%$ overshoot.
- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.

**Statistical caveat (what the paper does not claim):**
- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.

The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.

---

## Figures from the paper

| | |
|---|---|
| ![kernel shape](paper/figures/fig_F1_kernel_shape.png) | ![bin pulls](paper/figures/fig_F2_bin_pulls.png) |
| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |

![cross-dataset](paper/figures/fig_F3_cross_dataset_A.png)

**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.

---

## Repository contents

```
vfd-b-anomaly/
├── README.md                      # this file
├── LICENSE                        # MIT
├── CITATION.cff                   # citation metadata
├── CHANGELOG.md                   # findings history (linearisation drift, etc.)
├── pyproject.toml                 # Python package definition
├── .gitignore
│
├── paper/                         # the preprint
│   ├── main.pdf                   # camera-ready PDF
│   ├── main.tex                   # LaTeX source
│   ├── sections/                  # 10 section files
│   ├── figures/                   # F1, F2, F3 (PDF + PNG)
│   ├── references.bib
│   └── README.md                  # how to recompile
│
├── src/vfd_b_anomaly/             # core library (importable as `vfd_b_anomaly`)
│   ├── flavio_predictor.py        # cached flavio.sm_prediction / np_prediction wrapper
│   ├── hepdata_ingest.py          # HEPData JSON loader
│   ├── wo009_full_lift.py         # 600-cell V_600 graph and discrete Green's response
│   ├── wo010_universality.py      # frozen kernel evaluated at bin centres
│   ├── wo014_cross_dataset.py     # cross-dataset dataset loaders + linearised fit
│   ├── wo015_cross_channel.py     # Bs->phi cross-channel loader + linearised fit
│   └── ...                        # see src/ for the full list
│
├── scripts/                       # paper-headline drivers
│   ├── wo016a_akaike_stack.py     # Akaike weight stacking across 5 fits
│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
│   ├── wo016d_nonlinear_xdataset.py  # non-linear refit across all 5 datasets
│   └── wo017_paper_figures.py     # F1, F2, F3 generation
│
├── reports/                       # paper-headline outputs (regenerated by run_all.sh)
│   ├── wo009_full_lift.{json,csv,md}  # 600-cell graph spectral data
│   ├── wo016a_akaike_stack.md         # paper §6 Akaike-weight stack
│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
│   └── wo016d_nonlinear_xdataset.md   # paper §6 non-linear cross-dataset table
│
├── data/
│   ├── raw/                       # cached HEPData submissions (CC BY 4.0)
│   └── processed/                 # flavio_cache.json (regeneratable)
│
├── tests/                         # pytest suite
├── repro/                         # reproduction driver
│   └── run_all.sh
└── archive/                       # superseded scripts and reports cited as
                                   # supporting evidence in §5; not on the
                                   # path of run_all.sh
```

---

## Reproduce in 5 steps (clean checkout)

### 1. Install the package

```bash
git clone https://github.com/vfd-org/b-anomaly-reproduction.git vfd-b-anomaly
cd vfd-b-anomaly
pip install -e ".[dev,plotting]"
```

This pulls in `flavio` (2.4), `wilson` (2.5), `numpy`, `scipy`, `matplotlib`, `pytest`. flavio brings the BSZ form-factor parameterisation as a transitive dependency.

### 2. Cache the HEPData archives

The five datasets in the paper draw from five HEPData records. The first four are bundled in `data/raw/hepdata*/` (modest size, CC BY 4.0). For LHCb 2025 (the largest), download with:

```bash
mkdir -p data/raw/hepdata
curl -L "https://www.hepdata.net/download/submission/ins3094698/original" \
     -o data/raw/hepdata/HEPData-ins3094698-v1.zip
python -c "import zipfile; zipfile.ZipFile('data/raw/hepdata/HEPData-ins3094698-v1.zip').extractall('data/raw/hepdata/extracted')"
```

### 3. Run all paper-headline experiments

```bash
bash repro/run_all.sh
```

This runs (in order):
1. The non-linear LHCb 2025 refit (`scripts/wo016c_nonlinear_refit.py`).
2. The full five-dataset non-linear refit (`scripts/wo016d_nonlinear_xdataset.py`).
3. The Akaike-weight stack (`scripts/wo016a_akaike_stack.py`).
4. The pure-geometry variant test (`scripts/wo016b_variant_geometry.py`).
5. Paper figures F1, F2, F3 (`scripts/wo017_paper_figures.py`).

Total wall time: ~5 minutes on a laptop, dominated by the non-linear flavio calls. A persistent on-disk cache (`data/processed/flavio_cache.json`) ensures subsequent runs are near-instant.

### 4. Recompile the paper (optional)

The PDF at `paper/main.pdf` is shipped pre-built. To regenerate from source:

```bash
# install tectonic once (~50 MB, single static binary, no sudo needed)
curl -L https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz | tar -xz -C ~/.local/bin/

# compile
~/.local/bin/tectonic -X compile paper/main.tex
```

See `paper/README.md` for compile alternatives (TeX Live, Overleaf).

### 5. Run tests

```bash
pytest -q
```

---

## Contents of the paper

The 25-page preprint (`paper/main.pdf`) has 10 sections:

| § | content |
|---|---|
| 1 | Introduction; scope and epistemic status |
| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
| 3 | Three-layer kernel construction: continuum $\varphi$-tuned Green's function → bounded Dirichlet eigenmode → discrete 2I-equivariant lift on $V_{600}$. Variant-selection table on pure-geometry vs LHCb-data criteria. |
| 4 | Results on LHCb 2025: non-linear vs linearised, drift table, leave-one-observable-out |
| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
| 6 | Cross-dataset non-linear fit across five datasets; Akaike-weight stack; sign-uniformity test |
| 7 | Cross-channel fit on $B_{s}\!\to\!\phi$; basis-effect explanation of the amplitude gap |
| 8 | Discussion: why the linearisation breaks; three readings of sign uniformity |
| 9 | Limitations (linearisation issue is the lead) |
| 10 | Conclusion; falsification programme; reproducibility |

The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.

---

## License and data attribution

- **Project code** (everything under `src/`, `scripts/`, `tests/`, `repro/`, `paper/`): MIT licence — see [`LICENSE`](LICENSE).
- **Cached HEPData supplementary archives** under `data/raw/`: © CERN for the benefit of the LHCb and CMS collaborations, distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The canonical citation for each archive is the corresponding HEPData record:
  - LHCb 2025: [HEPData ins3094698](https://www.hepdata.net/record/ins3094698) (DOI [10.17182/hepdata.167733.v1](https://doi.org/10.17182/hepdata.167733.v1))
  - LHCb 2015 $K^{*}$: [HEPData ins1409497](https://www.hepdata.net/record/ins1409497)
  - LHCb 2021 $B^{+}\!\to\!K^{*+}$: [HEPData ins1838196](https://www.hepdata.net/record/ins1838196)
  - CMS 2025: [HEPData ins2850101](https://www.hepdata.net/record/ins2850101)
  - LHCb 2015 $B_{s}\!\to\!\phi$: [HEPData ins1380188](https://www.hepdata.net/record/ins1380188)
- **flavio** ([arXiv:1810.08132](https://arxiv.org/abs/1810.08132)) and **wilson** ([arXiv:1804.05033](https://arxiv.org/abs/1804.05033)) provide the SM and non-linear new-physics predictions used as the headline backend; their licences are upstream.

## Citation

If you use this software or the accompanying paper, see [`CITATION.cff`](CITATION.cff). Suggested BibTeX:

```bibtex
@misc{Smart2026vfdBAnomaly,
  author       = {Smart, Lee},
  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
  year         = {2026},
  url          = {https://github.com/vfd-org/b-anomaly-reproduction/blob/main/paper/main.pdf},
  note         = {Preprint, Institute of Vibrational Field Dynamics}
}
```

For the LHCb 2025 dataset the project rests on, also cite:

```bibtex
@article{LHCb:2025BKstmumuComp,
  author       = {{LHCb Collaboration}},
  title        = {A comprehensive analysis of the $B^0\to K^{*0}\mu^+\mu^-$ decay},
  eprint       = {2512.18053},
  archivePrefix= {arXiv},
  primaryClass = {hep-ex},
  year         = {2025},
  reportNumber = {LHCb-PAPER-2025-041, CERN-EP-2025-278},
  doi          = {10.17182/hepdata.167733.v1}
}
```

 succeeded in 327ms:
- `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf` —
  primary shipped passive-regime empirical witness for the fixed
  $C_\varphi$-derived $V_{600}$ kernel; five-dataset sign-uniform
  structural test (LHCb + CMS, $K^{*0}/K^{*+}/\phi$ channels) with
  honest AIC tie ($w_{\mathrm{VFD}} = 0.348$ vs
  $w_{\mathrm{FREE\_C9}} = 0.652$) and Mode-B $+2.77$ drift caveat.
- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md` —
  Layer 1 + Layer 2 derivation (supporting).
- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md` —
  Layer 3 numerical bridge (supporting).
- `BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md` —
  variant-selection table; the unweighted Laplacian wins on both
  pure-geometry and data $\chi^2$ criteria.
- `BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md` —
  Mode-B drift documentation; the largest single methodological
  uncertainty in the project.

 succeeded in 624ms:
papers/aria-chess-paper/paper/main.tex
papers/aria-chess-paper/paper/main.pdf
papers/aria-chess-paper/paper/references.bib
papers/aria-chess-paper/paper/README.md
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex
papers/aria-chess-paper/paper/sections/02_method.tex
papers/aria-chess-paper/paper/sections/03_substrate.tex
papers/aria-chess-paper/paper/sections/01_introduction.tex
papers/aria-chess-paper/paper/sections/05_results.tex
papers/aria-chess-paper/paper/sections/06_stress_tests.tex
papers/aria-chess-paper/paper/sections/08_discussion.tex
papers/aria-chess-paper/paper/sections/07_cross_domain.tex
papers/aria-chess-paper/paper/sections/09_limitations.tex
papers/aria-chess-paper/paper/sections/10_conclusion.tex

 succeeded in 1007ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:14:A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:16:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:21:| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:28:- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31:- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:32:- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:33:- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:44:| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:48:**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:76:│   ├── wo014_cross_dataset.py     # cross-dataset dataset loaders + linearised fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:77:│   ├── wo015_cross_channel.py     # Bs->phi cross-channel loader + linearised fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:82:│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:83:│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:84:│   ├── wo016d_nonlinear_xdataset.py  # non-linear refit across all 5 datasets
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:90:│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:91:│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:92:│   └── wo016d_nonlinear_xdataset.md   # paper §6 non-linear cross-dataset table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:122:The five datasets in the paper draw from five HEPData records. The first four are bundled in `data/raw/hepdata*/` (modest size, CC BY 4.0). For LHCb 2025 (the largest), download with:
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:193:  - LHCb 2025: [HEPData ins3094698](https://www.hepdata.net/record/ins3094698) (DOI [10.17182/hepdata.167733.v1](https://doi.org/10.17182/hepdata.167733.v1))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:198:- **flavio** ([arXiv:1810.08132](https://arxiv.org/abs/1810.08132)) and **wilson** ([arXiv:1804.05033](https://arxiv.org/abs/1804.05033)) provide the SM and non-linear new-physics predictions used as the headline backend; their licences are upstream.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:214:For the LHCb 2025 dataset the project rests on, also cite:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:17:  2I-equivariant graph (the 600-cell V_600) regularised by the golden ratio
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:20:  2025, LHCb 2025, LHCb 2015 Bs->phi) are evaluated using flavio.np_prediction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:21:  directly (non-linear in Delta C_9). The kernel is sign-uniform across all five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:23:  shift on AIC; an earlier linearised analysis found a stronger result that did
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CITATION.cff:24:  not survive the non-linear refit, and is reported as a methodology diagnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:20:- **Akaike-weight stacking** of $\Delta\mathrm{AIC}$ across the five fits
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:22:- **Pure-geometry variant-selection test** for the kernel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:23:  ([`scripts/wo016b_variant_geometry.py`](scripts/wo016b_variant_geometry.py)),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:25:  (correlation with continuum kernel) and LHCb-data criteria — defending
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:40:What the data shows under non-linear evaluation:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:48:- **Geometry-first variant test.** Of three discrete Laplacian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:49:  variants, the unweighted choice wins on a pure-geometry criterion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:50:  (correlation $0.997$ with the continuum kernel) decided
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:51:  independently of LHCb input. The same variant later wins on the
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:71:$\Delta C_{9}=-1.34$, well outside the linear regime. The non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:72:numbers are the headline; the linearised numbers are retained in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:77:  AIC" (linearised) to "fixed geometry-derived kernel describes the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:78:  anomaly across five datasets, AIC-tied with $\mathrm{FREE\_C9}$"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:79:  (non-linear).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:86:- Five-dataset linearised Mode-B fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:102:### Findings (linearised; later superseded by 0.2.0 non-linear refit)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:103:- All five datasets gave $\Delta\mathrm{AIC} < 0$ vs FREE\_C9, suggesting
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:104:  the kernel beat the constant shift in linearised analysis.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:106:  $w_{\mathrm{FREE\_C9}}=0.096$ (linearised).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:111:These linearised numbers are retained in the paper as a methodology
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:112:diagnostic and superseded by the 0.2.0 non-linear refit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:118:- Reproduced the negative direction of $\Delta C_{9}$ on the LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md:119:  $P_{5}'$ data using a one-observable Mode-B linearised fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.md:3:Re-runs the WO-014 cross-dataset and WO-015 cross-channel fits with `flavio.np_prediction` directly (non-linear) instead of the Mode-B Taylor expansion. The linearised values from reports/wo014_cross_dataset.csv and reports/wo015_cross_channel.csv are quoted in parentheses for comparison.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.md:5:| dataset | non-linear χ² (FREE) | non-linear χ² (VFD) | ΔAIC (NL) | ΔC9 (NL) | A (NL) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:5:#   1. Non-linear LHCb 2025 refit             → reports/wo016c_nonlinear_refit.{md,csv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:8:#   4. Pure-geometry variant-selection check  → reports/wo016b_variant_geometry.{md,csv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:26:step "1/5  Non-linear LHCb 2025 refit (~30s)"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:35:step "4/5  Pure-geometry variant-selection check"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/repro/run_all.sh:36:python3 scripts/wo016b_variant_geometry.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:3:Generates three figures for the headline non-linear analysis:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:5:    F2 - Bin pulls for the four LHCb 2025 angular observables under
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:6:         the non-linear FREE_C9 and VFD fits.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:8:         non-linear bootstrap-style error bars.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:77:               zorder=5, s=40, label="LHCb 2025 bin centres")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:100:# F2 — bin pulls under non-linear refit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:164:    fig.suptitle("LHCb 2025 bin pulls under non-linear "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:189:        "LHCb-2025":         "LHCb 2025\n" + r"$B^0\to K^{*0}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:195:    aic_diff = {r["dataset"]: float(r["delta_aic_vs_FREE_C9"])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:213:    ax_main.set_ylabel(r"fitted amplitude $A$ (non-linear)")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:219:                     fr"$\Delta\mathrm{{AIC}}={da:+.2f}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:233:                fr"$\Delta\mathrm{{AIC}}={aic_diff[ds_phi]:+.2f}$",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo017_paper_figures.py:240:    fig.suptitle("Cross-dataset and cross-channel non-linear amplitudes",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:3:Per-dataset AIC deltas and Akaike weights, plus stacked weight.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:6:| dataset | FREE_C9 ΔAIC | VFD ΔAIC | w(FREE_C9) | w(VFD) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:16:- log-evidence(FREE_C9) − log-evidence(VFD) = 0.627
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:17:- Total ΔAIC sum (FREE_C9 vs VFD): -1.253
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:21:| FREE_C9 | 0.6517 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:22:| VFD_GREEN_600CELL | 0.3483 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md:24:Auxiliary check: under the null hypothesis P(VFD lower AIC on all 5 fits) = $1/2^{5}$ = 0.0312.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:1:model,chi2,aic,delta_aic_vs_FREE_C9,fit_param
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:2:FREE_C9_linear,39.3034,41.3034,0.0000,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:3:FREE_C9_nonlinear@linear-best-fit,66.5964,68.5964,0.0000,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.csv:4:FREE_C9_nonlinear_refit,40.8907,42.8907,0.0000,DC9=-1.002
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_vfd_closure.py:27:    """No hidden per-bin freedom: param count must be invariant under grid expansion."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:3:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:7:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:9:    "correlation_with_exp":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:10:    "correlation_with_cos":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:19:    "delta_aic_vs_FREE_C9":-7.0000330722,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:21:    "correlation_with_exp":1.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:22:    "correlation_with_cos":0.8573973265,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:31:    "delta_aic_vs_FREE_C9":53.9660791829,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:33:    "correlation_with_exp":0.8488890174,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:34:    "correlation_with_cos":0.9989213436,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:41:    "chi2":13.5553723813,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:43:    "delta_aic_vs_FREE_C9":-1.3559901954,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:45:    "correlation_with_exp":0.9967985381,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:46:    "correlation_with_cos":0.8811748188,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:55:    "delta_aic_vs_FREE_C9":53.9660791829,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:57:    "correlation_with_exp":0.9167541597,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:58:    "correlation_with_cos":0.5939777935,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:67:    "delta_aic_vs_FREE_C9":-0.1982697277,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:69:    "correlation_with_exp":0.9129905074,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:70:    "correlation_with_cos":0.5866213391,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:79:    "delta_aic_vs_FREE_C9":52.1596229368,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:81:    "correlation_with_exp":0.8065358205,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:82:    "correlation_with_cos":0.4450507202,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:91:    "delta_aic_vs_FREE_C9":-0.1297765399,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:93:    "correlation_with_exp":0.8988651524,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.json:94:    "correlation_with_cos":0.5626113001,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,evaluation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:2:LHCb-2015,B0->K*mumu,FREE_C9,32,1,30.69104835960865,32.69104835960865,34.15678426240838,0.0,-1.0796559803655492,-1.0796559803655492,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:4:LHCb-2021-Kstplus,B+->K*+mumu,FREE_C9,32,1,22.76511589608483,24.76511589608483,26.230851798884554,0.0,-1.8196686329963627,-1.8196686329963627,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:6:CMS-2025-noP4p,B0->K*mumu,FREE_C9,18,1,43.73143845773427,45.73143845773427,46.62181021563043,0.0,-0.9538642637928241,-0.9538642637928241,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:8:LHCb-2025,B0->K*mumu,FREE_C9,32,1,40.89068922835959,42.89068922835959,44.35642513115932,0.0,-1.0025621703516263,-1.0025621703516263,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.csv:10:Bs2phi-LHCb-2015,Bs->phimumu,FREE_C9,24,1,13.201397760357471,15.201397760357471,16.37945159070542,0.0,-4.121891268879767,-4.121891268879767,nonlinear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:4:for the kernel. Reviewer asked: was that selected by data correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:6:criterion (correlation with the continuum Green's function
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:9:This script extracts the GREENS-mode variants from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:10:reports/wo009_full_lift.json and ranks them by `correlation_with_exp`,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:13:variant choice is consistent with both pure-geometry and LHCb-data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:15:would mean the variant choice is *only* data-informed.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:18:Output : reports/wo016b_variant_geometry.{csv,md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:29:OUT_CSV = REPO / "reports" / "wo016b_variant_geometry.csv"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:30:OUT_MD = REPO / "reports" / "wo016b_variant_geometry.md"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:37:    by_geom = sorted(greens, key=lambda r: -float(r["correlation_with_exp"]))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:42:        w.writerow(["variant", "corr_with_exp", "chi2_vs_lhcb",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:49:                f"{float(r['correlation_with_exp']):.6f}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:57:        "Pure-geometry criterion: correlation between the discrete "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:63:    lines.append("Data criterion: chi^2 against LHCb 2025 P5' on the joint fit.")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:65:    lines.append("| variant | corr(κ_continuum) | χ² (LHCb) | geom rank | data rank |")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:72:            f"| {float(r['correlation_with_exp']):.4f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:83:                 f"{float(by_geom[0]['correlation_with_exp']):.4f})")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:89:            "**Agreement.** The same variant (unweighted Laplacian) wins "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:90:            "on both criteria. The variant choice is consistent with "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:98:            "LHCb-data winner. The variant chosen in the paper is "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016b_variant_geometry.py:100:            "treated as k>=2 in AIC comparisons."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/source_manifest.json:29:    "notes": "HEPData supplementary archive obtained 2026-04-28 from https://www.hepdata.net/download/submission/ins3094698/original. Contains 6 fit configurations (config_1..config_6) each with results + stat/syst/total correlation matrices in both YAML and JSON. Paper text explicitly directs readers to the HEPData page for systematic uncertainties and full observable results."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:4:kernel variants. This script tests how robust the WO-010 universality
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:325:    full multivariate constraint (correlations preserved). For each draw we
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:496:        {"model": "FREE_C9", "k_params": 1, "chi2": free_c9.chi2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:498:         "delta_aic_vs_FREE_C9": 0.0, "params": f"DC9={free_c9.effective_delta_c9_mean:+.3f}"},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:501:         "delta_aic_vs_FREE_C9": vfd_kernel.aic - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:505:         "delta_aic_vs_FREE_C9": free_c9_c10["aic"] - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo013_stress_test.py:509:         "delta_aic_vs_FREE_C9": charm_loop["aic"] - free_c9.aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:3:Critical: the linearised Mode-B drift diagnostic (wo016c) showed that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:4:the linearised response gives a materially different result from a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:5:non-linear flavio refit on LHCb 2025 (Delta AIC drift = +2.77 AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:6:units). The paper headlines must therefore be re-derived in non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:9:This script re-fits FREE_C9 and VFD_GREEN_600CELL on each of the five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:174:                  f"DAIC={result['delta_aic_vfd_minus_free']:+.3f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:183:            "chi2", "aic", "bic", "delta_aic_vs_FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:190:                r["dataset"], r["decay"], "FREE_C9", r["n_data"],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:207:        "with `flavio.np_prediction` directly (non-linear) instead of the "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:208:        "Mode-B Taylor expansion. The linearised values from "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:212:        "| dataset | non-linear χ² (FREE) | non-linear χ² (VFD) | "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016d_nonlinear_xdataset.py:213:        "ΔAIC (NL) | ΔC9 (NL) | A (NL) |",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:1:dataset,model,AIC_delta,akaike_weight
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:2:LHCb-2015,FREE_C9,0.2411,0.469903
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:4:LHCb-2021-Kstplus,FREE_C9,0.0000,0.520988
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:6:CMS-2025-noP4p,FREE_C9,0.0000,0.558896
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:8:LHCb-2025,FREE_C9,0.0000,0.633273
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:10:Bs2phi-LHCb-2015,FREE_C9,0.2398,0.470064
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:14:STACKED,FREE_C9,-0.2404,0.651705
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.csv:15:STACKED,VFD_GREEN_600CELL,-0.8670,0.348295
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:3:Pure-geometry criterion: correlation between the discrete shell-mean of the V_600 Green's response and the continuum kernel $\kappa(x) = e^{-|x|/\varphi}$ from Layer 1 of the derivation. This criterion does **not** use LHCb data.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:5:Data criterion: chi^2 against LHCb 2025 P5' on the joint fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:7:| variant | corr(κ_continuum) | χ² (LHCb) | geom rank | data rank |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:9:| FULL_LIFT[UNWEIGHTED]_GREENS | 0.9968 | 13.555 | 1 | 1 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:13:- Pure-geometry winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (corr with continuum kernel = 0.9968)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:14:- LHCb-data winner: **FULL_LIFT[UNWEIGHTED]_GREENS** (χ² = 13.555)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md:16:**Agreement.** The same variant (unweighted Laplacian) wins on both criteria. The variant choice is consistent with pure-geometry selection independent of the data; the LHCb data merely confirms it. Effective parameter count for VFD remains k=1 under the pure-geometry interpretation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:1:model,k_params,chi2,amplitude,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,correlation_with_exp,correlation_with_cos,eigenvalue,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:2:FREE_C9,1,14.91136257673117,-1.3771673074587851,0.0,7.0000330721695825,,,,global C9 shift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.csv:5:FULL_LIFT[UNWEIGHTED]_GREENS,1,13.555372381338534,1.684032143799957,-1.3559901953926374,5.644042876776945,0.9967985381030878,0.8811748187990005,0.38196601125011054,"shell-mean psi = [0.788, 0.813, 0.864, 0.89, 1.0, 0.89, 0.864, 0.813, 0.788]"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:1:# WO-016c — Non-linear flavio refit on LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:3:Tests whether the linearised Mode-B response is sufficient at the fitted Delta C9 ~ -1.4. Three comparisons:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:5:2. Non-linear evaluation at the linearised best-fit point (drift diagnostic — both models pinned at linear best-fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:10:| model | chi^2 | AIC | Delta AIC vs FREE_C9 | fit param |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:12:| FREE_C9_linear | 39.303 | 41.303 | +0.000 | DC9=-1.340 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:13:| FREE_C9_nonlinear@linear-best-fit | 66.596 | 68.596 | +0.000 | DC9=-1.340 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:14:| FREE_C9_nonlinear_refit | 40.891 | 42.891 | +0.000 | DC9=-1.002 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:19:- Linearised Delta AIC (FREE_C9 vs VFD): -1.672
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:20:- Non-linear Delta AIC at linear best-fit: +15.644 (diagnostic only; both models held at linear best-fit)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:21:- Non-linear Delta AIC after refit: +1.093 (headline-comparable)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:22:- Drift in headline Delta AIC: +2.765
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:26:- FREE_C9 linear: Delta C9 = -1.3403
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:27:- FREE_C9 non-linear refit: Delta C9 = -1.0025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:29:- VFD non-linear refit: A = +1.1350
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:33:- FREE_C9 at linear best-fit: max = 3.106 sigma, mean = 0.630 sigma
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md:36:**Conclusion.** |Drift in headline Delta AIC| = 2.765 > 0.5 AIC unit. The headline must be updated to the non-linear refit value: Delta AIC_NL = +1.093 (vs linearised -1.672). The non-linear refit best-fit is DC9_FREE = -1.002 (vs linear -1.340) and A = +1.135 (vs linear +1.594).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:6:$\kappa(q^{2})$ from a finite 2I-equivariant graph (the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:15:$\Delta C_{9}$); the earlier linearised analysis is reported alongside
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:21:\item \textbf{LHCb 2025, four-observable joint fit (non-linear):}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:24:  $k=1$). On AIC the kernel and a constant-$\Delta C_{9}$ shift at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:26:  ($\Delta\mathrm{AIC}=+1.09$, mild preference for the constant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:28:\item \textbf{Cross-dataset (non-linear, 5 fits across 2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:29:  collaborations and 3 channels):} $\Delta\mathrm{AIC}\in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:36:\item \textbf{Cross-dataset amplitude scatter:} non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:42:\item \textbf{Linearisation drift:} on LHCb 2025 the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:43:  $\Delta\mathrm{AIC}$ shifts by $+2.77$ between the linearised and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:44:  non-linear fits, larger than the linearised preference itself; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:45:  non-linear refit is taken as headline.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:49:  pure-geometry-confirmed discrete variant choice
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:50:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:58:  under non-linear refit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:63:  under non-linear refit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:65:  HEPData becomes available) gives $A<0$ under non-linear refit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:69:analysis with non-linear $\Delta C_{9}$ evaluation gives
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:70:$\Delta\mathrm{AIC}_{\mathrm{VFD\,vs\,FREE\_C9}}\geq 0$ on the LHCb
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:75:listed above are independent of, and unaffected by, this AIC tie.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:86:factor; and the unweighted Laplacian variant is selected by a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:87:pure-geometry criterion (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:90:over a constant Wilson-coefficient shift. AIC compares per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:108:including the non-linear refits and Akaike-weight stacking, figure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:113:SM and non-linear-NP values. The non-linear refit scripts
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_likelihood.py:63:    assert a3 > a0  # AIC penalty grows with k
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_likelihood.py:67:    # BIC penalises more harshly than AIC for n>=8
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo015_cross_channel.py:18:       public correlation matrices on HEPData and were skipped in WO-014.
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:1:# WO-009 — Full 2I-equivariant edge-space lift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:8:phi-kernel at correlation r >= 0.95 with no manual shell tuning, only an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:41:| variant | edge weight w_{vw} | meaning |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:48:default; the arithmetic variant is a sanity check.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:50:**Two operator-response modes tested per variant:**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:67:| model | k | chi^2 | A_hat | dAIC vs FREE_C9 | r vs exp | r vs cos |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:69:| FREE_C9 reference         | 1 | 6.70 | DC9 = -0.154 |  0.00 | -     | -     |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:72:| **FULL_LIFT[UNWEIGHTED] GREENS**     | 1 | **6.50** | **+0.178** | **-0.21** | **0.997** | 0.881 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:95:  (r = 0.997) and `PHI_ARITHMETIC_GREENS` (r = 0.899 — fails); marginal for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:96:  `PHI_GEOMETRIC_GREENS` (r = 0.913 — fails). The eigenmode variants do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:98:- **Only amplitude fitted, no shape/width/centre:** YES for all variants.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:99:- **dAIC vs FREE_C9 <= 0:** YES for all GREENS variants (-0.21, -0.10,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:100:  -0.07). FAIL for all EIGENMODE variants (+2.96, +3.28, +1.02).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:103:criterion: r = 0.997 with the continuum Layer-1 kernel, dAIC vs FREE_C9 = -0.21,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:115:Pearson correlation between this discrete Green's response (projected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:117:the continuum exp(-|x|/phi) kernel is r = 0.997 across 8 LHCb bin centres.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:119:beats FREE_C9 on AIC (dAIC = -0.21) and reaches chi^2 = 6.50 (vs 5.90 for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:124:response *too flat* — the correlation with the continuum exp drops to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:145:  the genuine combinatorial-Laplacian-on-edges with 2I-equivariant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:159:The full 2I-equivariant lift of the closure kernel exists at the level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:164:matches the continuum derivation at r = 0.997 with one fitted amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo009_full_lift.md:165:and beats a global C_9 shift on AIC. The proper Hodge-edge-space
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:1:"""WO-009 — Full 2I-equivariant edge-space lift on the 600-cell.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:23:    7. Find the lowest non-constant *even-parity* eigenvector (even = invariant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:35:    - dAIC vs FREE_C9 <= 0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:420:    correlation_with_exp: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:421:    correlation_with_cos: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:422:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:458:    # ---- Step 4-7: variants ----
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:459:    variants: list[tuple[str, np.ndarray]] = [
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:474:    # FREE_C9 reference
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:501:    for name, A_w in variants:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:512:            correlation_with_exp=float(np.corrcoef(psi_eig_bins, bench_exp)[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:513:            correlation_with_cos=float(np.corrcoef(psi_eig_bins, bench_cos)[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:514:            delta_aic_vs_FREE_C9=aic_eig - free_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:529:            correlation_with_exp=float(np.corrcoef(psi_g_bins, bench_exp)[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:530:            correlation_with_cos=float(np.corrcoef(psi_g_bins, bench_cos)[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:531:            delta_aic_vs_FREE_C9=aic_g - free_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:538:        {"model": "FREE_C9", "k_params": 1, "chi2": free_chi2, "amplitude": float(free.x[0]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:539:         "delta_aic_vs_FREE_C9": 0.0, "delta_aic_vs_KAPPA_EXP": free_aic_v - exp_aic_v,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:540:         "correlation_with_exp": np.nan, "correlation_with_cos": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:543:         "delta_aic_vs_FREE_C9": exp_aic_v - free_aic_v, "delta_aic_vs_KAPPA_EXP": 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:544:         "correlation_with_exp": 1.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:545:         "correlation_with_cos": float(np.corrcoef(kappa_exp, bench_cos)[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:551:            "delta_aic_vs_FREE_C9": r.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:553:            "correlation_with_exp": r.correlation_with_exp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:554:            "correlation_with_cos": r.correlation_with_cos,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:572:        "variants": [r.__dict__ for r in results],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:584:    print(res["models"][["model", "k_params", "chi2", "amplitude", "delta_aic_vs_FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:585:                          "delta_aic_vs_KAPPA_EXP", "correlation_with_exp",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:586:                          "correlation_with_cos", "eigenvalue"]].to_string(index=False))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo009_full_lift.py:588:    for v in res["variants"]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.csv:1:variant,corr_with_exp,chi2_vs_lhcb,geometry_rank,data_rank
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.csv:2:FULL_LIFT[UNWEIGHTED]_GREENS,0.996799,13.5554,1,1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:1:"""WO-016c — Non-linear flavio refit on LHCb 2025.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:3:Reviewer concern: the linearised response model (Mode B) extrapolates a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:6:question is whether the headline Delta AIC (-1.67) survives a fully
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:7:non-linear flavio refit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:10:    1. Load LHCb 2025 4-observable joint dataset (32 points).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:11:    2. Evaluate both models in non-linear mode at the linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:13:    3. Re-fit both FREE_C9 (one global Delta C9) and VFD (one A;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:15:       directly. Compare non-linear best-fit Delta AIC to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:16:       linearised value (-1.67).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:17:    4. Report whether the headline Delta AIC survives non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:43:# Linearised best-fit values for the LHCb-2025 row (the linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:46:# repo without rerunning the linearised fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:86:    # ---- FREE_C9 non-linear ----
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:102:    # ---- VFD non-linear ----
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:121:    # ---- Non-linear refits (find best-fit DC9 / A in non-linear model) ----
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:162:        ("FREE_C9_linear", chi2_free_lin, aic_free_lin, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:164:        ("FREE_C9_nonlinear@linear-best-fit", chi2_free_nl, aic_free_nl, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:166:        ("FREE_C9_nonlinear_refit", chi2_free_nl_refit, aic_free_nl_refit, 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:178:        w.writerow(["model", "chi2", "aic", "delta_aic_vs_FREE_C9", "fit_param"])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:186:        "# WO-016c — Non-linear flavio refit on LHCb 2025",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:188:        "Tests whether the linearised Mode-B response is sufficient at the "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:191:        "2. Non-linear evaluation at the linearised best-fit point "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:197:        "| model | chi^2 | AIC | Delta AIC vs FREE_C9 | fit param |",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:205:        f"- Linearised Delta AIC (FREE_C9 vs VFD): {delta_aic_lin:+.3f}"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:208:        f"- Non-linear Delta AIC at linear best-fit: {delta_aic_nl:+.3f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:212:        f"- Non-linear Delta AIC after refit: {delta_aic_nl_refit:+.3f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:216:        f"- Drift in headline Delta AIC: "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:222:    lines.append(f"- FREE_C9 linear: Delta C9 = {DC9_FREE_BEST:+.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:223:    lines.append(f"- FREE_C9 non-linear refit: Delta C9 = {DC9_FREE_NL:+.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:225:    lines.append(f"- VFD non-linear refit: A = {A_VFD_NL:+.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:230:        f"- FREE_C9 at linear best-fit: max = {pred_diff_free.max():.3f} sigma, "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:242:            f"**Conclusion.** |Drift in headline Delta AIC| = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:243:            f"{abs(drift):.3f} <= {threshold} AIC unit. The linearised "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:244:            f"and non-linear fits agree within tolerance; the headline "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:245:            f"Delta AIC is robust to non-linear flavio evaluation."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:249:            f"**Conclusion.** |Drift in headline Delta AIC| = "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:250:            f"{abs(drift):.3f} > {threshold} AIC unit. The headline must be "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:251:            f"updated to the non-linear refit value: "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:252:            f"Delta AIC_NL = {delta_aic_nl_refit:+.3f} (vs linearised "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/scripts/wo016c_nonlinear_refit.py:253:            f"{delta_aic_lin:+.3f}). The non-linear refit best-fit is "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:12:angular observables is determined in bins of the invariant mass squared of the dimuon
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:52:the dimuon invariant mass squared, q2. The dataset used corresponds to an integrated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:61:the first time the invariant mass of the kaon-pion system, m(K+π−), which is also studied
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:99:or tensor amplitudes. Without these assumptions, significant correlations between some
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:143:training sample, candidates with invariant mass 5 .5 < m(K+π−µ+µ−) < 5.7 GeV /c2 are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:160:and vice versa. The vetoes use the invariant mass of the candidates recomputed with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:165:candidates with m(K+π−µ+µ−) > 5.38 GeV /c2 if they have a K+µ+µ− invariant mass
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:215:correlations determined. A model-independent measurement of both the relative branching
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/lhcb_2512_18053.txt:810:[39] S. J¨ ager and J. Martin Camalich,On B→V ℓℓ at small dilepton invariant mass,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:20:       data rejects (i.e. higher dAIC vs FREE_C9 than the rank-1 mode alone).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:85:    correlation_with_full_kernel: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:86:    correlation_with_continuum_exp: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:156:        # Skip if kernel is identically zero (would NaN the correlation)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:165:        # When the truncated kernel is constant, correlation undefined
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:178:            correlation_with_full_kernel=r_full,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:179:            correlation_with_continuum_exp=r_cont,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:195:                "r_vs_full_kernel": r.correlation_with_full_kernel,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:196:                "r_vs_continuum_exp": r.correlation_with_continuum_exp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:199:                "delta_aic_vs_FREE_C9": r.aic_p5p - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:222:                     if not np.isnan(r.correlation_with_full_kernel)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:223:                     and r.correlation_with_full_kernel >= 0.99), None)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:225:                      if not np.isnan(r.correlation_with_full_kernel)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:226:                      and r.correlation_with_full_kernel >= 0.999), None)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:242:        "kernel_continuum_correlation": float(np.corrcoef(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:254:    print(f"FREE_C9 reference chi^2 = {res['free_c9_chi2']:.4f}, AIC = {res['free_c9_aic']:.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo011_spectral.py:255:    print(f"Full kernel correlation with continuum exp: r = {res['kernel_continuum_correlation']:.4f}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:55:    """Sanity: known LHCb 2025 P5' is positive at low q² and negative above ~ 4 GeV²."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:70:        ARCHIVE, config_index=2, observables=("P5p",), correlation_kind="total"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:87:        ARCHIVE, config_index=2, observables=("P5p",), correlation_kind="total"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:94:def test_load_config_with_correlation_none_omits_covariance():
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/test_hepdata_ingest.py:96:        ARCHIVE, config_index=2, observables=("P5p",), correlation_kind="none"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/tests/conftest.py:3:Synthetic data is built by injecting a known ΔC9_true via the linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:6:The section is reorganised relative to the Mode-B-era version to put
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:14:  project iterations (the linearised stress test, the cross-dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:15:  validation, and the cross-channel validation) used a Mode-B
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:16:  linearised response, where every angular observable is approximated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:22:  $\Delta\mathrm{AIC}$ shifts from $-1.67$ (linearised) to $+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:23:  (non-linear refit), reversing the kernel-vs-constant comparison.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:24:  This paper now uses non-linear \texttt{flavio.np\_prediction}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:25:  evaluation throughout for the headline numbers; Mode-B values are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:27:  anomaly should not use a linearised Taylor expansion.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:31:  the best LHCb-data $\chi^{2}$ among the three admissible variants
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:32:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:33:  We subsequently verified that the same variant wins on a pure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:34:  geometry criterion (correlation with the Layer-1 continuum kernel,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:35:  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:36:  this basis. The variant choice therefore does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:44:  The Mode-B stress test (\S\ref{sec:stress}) ruled out $C_{10}$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:45:  the relevant level on the joint LHCb 2025 fit; the broader
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:51:  2I-equivariant graph but is not derived from a first-principles
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:59:  \delta_{1}^{\mathsf T}\delta_{1}$ with 2I-equivariant boundary maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:72:  inter-bin correlation information that the all-data fit exploits.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:86:  inter-observable correlation matrix for the LHCb 2015
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:122:  ($\Delta\chi^{2}=1$ Gaussian approximation or non-parametric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:136:  analysis lacks a public correlation matrix on HEPData; Belle II had
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:145:two isospin partners, and two decay channels. Under non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:147:on AIC; the stacked Akaike weight is $\approx 1.9{:}1$ in favour of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:152:the stronger ``it beats the constant shift on AIC'' claim of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo010_universality.py:10:No new variants, no fitted shape, no fitted centre, no fitted width.
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:1:"""Gaussian chi-squared likelihood for binned observables.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:74:    """Akaike information criterion under Gaussian likelihood (constant terms dropped)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/likelihood.py:79:    """Bayesian information criterion under Gaussian likelihood (constants dropped)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:41:# all three are run and their AIC/BIC are reported so no post-hoc cherry-picking
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:60:# Two further single-amplitude variants in the same one-derivative-correction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:115:# Geometry constants for the fixed-sigma variants. All values are derived from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:251:    sigma : Gaussian width in GeV^2 (threshold mode only).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/vfd_closure.py:376:    # Recompute pure (un-regularised) chi^2 for AIC/BIC reporting.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/sm_baseline.py:10:The linearised model is:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/sm_baseline.py:48:        SMResponse(sm_value=+0.3484, dO_dC9=+0.0003),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:13:       HEPData ins2850101, results_p*.yaml + correlation_matrix_q2_bin_*.yaml.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:14:    4. LHCb 2025 — current dataset (8.4 fb^-1, B0 -> K*0 mumu) — reference.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:28:    - VFD_GREEN_600CELL AIC <= FREE_C9 AIC on every dataset (or comparable).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:120:    """LHCb 2021 (B^+ -> K*+ mumu) data2.yaml + per-bin correlation blocks.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:126:    no cross-bin correlations exposed by HEPData.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:181:    """Per-bin 8x8 correlation block from corr_P_bin*.yaml -> block-diagonal
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:295:    """CMS publishes correlation_matrix_q2_bin_{i}.yaml for some bins. Build
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/wo014_cross_dataset.py:325:        corr_path = base / f"correlation_matrix_q2_bin_{gi}.yaml"
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:8:under three operator variants, projects onto the LHCb bin centres, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:11:Operator variants (all on the 9-vertex symmetric path with shell index
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:21:       all eigenvalues uniformly so eigenvectors equal variant A's,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:32:For each variant: lowest-eigenvalue eigenvector psi_1 (normalised to peak 1),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:34:single-amplitude fit to P5' data. Compare chi^2 / AIC against:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:37:    - FREE_C9 (k = 1)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:44:    - dAIC vs FREE_C9 <= 0 (competitive with global C_9 shift)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:113:    variant: str
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:117:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:121:    correlation_with_exp: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:122:    correlation_with_cos: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:204:def run_variant(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:230:        variant=name,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:234:        delta_aic_vs_FREE_C9=aic_v - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:238:        correlation_with_exp=r_exp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:239:        correlation_with_cos=r_cos,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:258:    # Reference rows. Re-derive FREE_C9 and KAPPA_EXP here so the comparison is local.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:277:    fit_A = run_variant("FREE_DIRICHLET", L_A, data, free_aic, exp_aic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:281:    fit_B = run_variant("PHI_MASS", L_B, data, free_aic, exp_aic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:286:    fit_C = run_variant(f"PHI_COCYCLE[alpha={cocycle_alpha}]", L_C, data, free_aic, exp_aic)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:294:            "delta_aic_vs_FREE_C9": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:296:            "correlation_with_exp": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:297:            "correlation_with_cos": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:302:            "model": "FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:306:            "delta_aic_vs_FREE_C9": 0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:308:            "correlation_with_exp": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:309:            "correlation_with_cos": np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:318:            "delta_aic_vs_FREE_C9": exp_aic - free_aic,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:320:            "correlation_with_exp": 1.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:321:            "correlation_with_cos": float(np.corrcoef(kappa_exp, np.cos(np.pi * vfd_closure.kappa_coordinate(q2) / (2 * vfd_closure.KAPPA_X_MAX)))[0, 1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:328:            "model": f"DISCRETE_LIFT[{f.variant}]",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:332:            "delta_aic_vs_FREE_C9": f.delta_aic_vs_FREE_C9,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:334:            "correlation_with_exp": f.correlation_with_exp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo008_discrete_lift.py:335:            "correlation_with_cos": f.correlation_with_cos,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:14:Under the Mode-B linearised response, the kernel's centre-peaked
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:15:profile and FREE\_C9's flat profile compress the four LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:17:better $\chi^{2}$ ($\Delta\mathrm{AIC}=-1.67$). Under the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:18:non-linear refit the bin-by-bin pattern matters less because the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:19:non-linearity in $\Delta C_{9}$ partly compensates for shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:22:$\Delta\mathrm{AIC}=+1.09$. Across five fits the non-linear stacked
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:33:preferred explanation under AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:37:The angular observables $P_{i}'$ and $S_{i}$ are non-linear in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:44:Empirically the per-bin linearisation residual on LHCb 2025 reaches
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:45:$4\sigma$ at the linearised best-fit $\Delta C_{9}=-1.34$, and refit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:46:under the non-linear model returns $\Delta C_{9}=-1.00$ with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:47:$\Delta\chi^{2}\approx +1.6$ relative to the linearised value.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:57:operator $L_{V_{600}} + \varphi^{-2}I$ to the 2I-equivariant cocycle
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:66:Table~\ref{tab:variant_selection}); the unweighted Laplacian wins on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:72:Across the four $B\to K^{*}$ non-linear fits the amplitude $A$ stays
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:93:The non-linear fitted amplitudes are $5/5$ positive across the five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:103:\item \emph{The kernel is the right object.} The 2I-equivariant graph
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:120:\subsection{What the linearised stress tests rule out}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:122:The Mode-B stress tests (\S\ref{sec:stress}) rule out specific
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:123:alternative explanations of the LHCb 2025 result:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:127:  $A\in[+1.36, +1.85]$ in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:130:  in Mode B, worse than the $+2$ AIC penalty for the extra parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:133:  $A=+1.57\pm 0.16$, $100\,\%$ positive, in Mode B.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:135:These three statements transfer to the non-linear refit qualitatively
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:137:though absolute amplitudes are smaller in the non-linear regime.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:139:What the linearised stress tests do \emph{not} rule out is a free
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:140:centre-peaked Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:141:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9 in Mode B; vs $-1.67$ for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:143:parameter. The geometric kernel and the free Gaussian capture the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:3:The archive layout (as extracted) provides one results JSON + one correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:7:    config_{i}_correlation_{stat,syst,total}.json    (i in 1..6)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:31:Schema (correlation JSON): a flat dict keyed by "{obs}_bin{N}" whose values
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:32:are dicts mapping the same {obs}_bin{N} identifiers to correlation coefficients.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:121:        "correlation_total": Path(f"{base}_correlation_total.json"),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:122:        "correlation_stat": Path(f"{base}_correlation_stat.json"),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:123:        "correlation_syst": Path(f"{base}_correlation_syst.json"),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:235:def parse_config_correlation(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:236:    correlation_path: Path | str,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:239:    """Build a covariance matrix aligned to df row ordering, from a HEPData correlation file.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:244:    cor = _load_json(Path(correlation_path))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:246:        raise ValueError(f"unexpected correlation file structure in {correlation_path}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:258:        raise KeyError(f"correlation matrix missing row keys: {missing_rows}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:267:            # Try both orderings: correlations are symmetric but the JSON
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:297:    correlation_kind: str = "total",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:301:    correlation_kind: 'total' | 'stat' | 'syst' (or 'none' to skip).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:308:    metadata["correlation_kind"] = correlation_kind
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:312:    if correlation_kind == "none":
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:315:    cor_key = f"correlation_{correlation_kind}"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:317:        raise ValueError(f"unknown correlation_kind {correlation_kind!r}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/hepdata_ingest.py:318:    covariance = parse_config_correlation(paths[cor_key], df)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/processed/flavio_cache.json:286: "Bs->phimumu|FL|15.0000|17.0000|dC9=-0.5000": 0.34887540590922045,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_cross_channel/ins1486676/HEPData-ins1486676-v1-yaml/submission.yaml:2:  CERN-LHC.  Measurements of the differential branching fraction and angular moments of the decay $B^0 \to K^+ \pi^- \mu^+ \mu^-$ in the $K^*_{0,2}(1430)^0$ in the $K^+\pi^-$ invariant mass range $1330<m(K^+ \pi^-)<1530~MeV/c^2$ are presented. Proton-proton collision data are used, corresponding to an integrated luminosity of 3 $fb^{-1}$ collected by the LHCb experiment. Differential branching fraction measurements are reported in five bins of the invariant mass squared of the dimuon system, $q^2$, between 0.1 and 8.0 $GeV^2/c^4$. For the first time, an angular analysis sensitive to the S-, P- and D-wave contributions of this rare decay is performed. The set of 40 normalised angular moments describing the decay is presented for the $q^2$ range 1.1--6.0 $GeV^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:17:    FREE_C9       k=1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:88:    delta_aic_vs_FREE_C9: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:110:        delta_aic_vs_FREE_C9=np.nan,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:139:        "FREE_C9", "reference", float(r.fun), 1, len(values),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:224:    free_aic = next(r.aic for r in rows if r.model == "FREE_C9")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/scripts/wo007_eigenmodes.py:227:        r.delta_aic_vs_FREE_C9 = r.aic - free_aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:25:    -   location: config_1_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:28:            table presents the statistical correlation matrix as obtained from the Hessian matrix of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:31:    -   location: config_1_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:34:            table presents the statistical correlation matrix as obtained from the Hessian matrix of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:37:    -   location: config_1_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:40:            table presents the correlation matrix of the systematic uncertainties, without including any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:43:    -   location: config_1_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:46:            table presents the correlation matrix of the systematic uncertainties, without including any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:50:    -   location: config_1_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:53:            table presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:55:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:60:    -   location: config_1_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:63:            table presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:65:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:96:    -   location: config_2_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:99:            used. This table presents the statistical correlation matrix as obtained from the Hessian matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:102:    -   location: config_2_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:105:            used. This table presents the statistical correlation matrix as obtained from the Hessian matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:108:    -   location: config_2_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:111:            used. This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:114:    -   location: config_2_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:117:            used. This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:121:    -   location: config_2_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:124:            used. This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:127:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:131:    -   location: config_2_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:134:            used. This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:137:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:167:    -   location: config_3_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:170:            used. This table presents the statistical correlation matrix as obtained from the Hessian matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:173:    -   location: config_3_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:176:            used. This table presents the statistical correlation matrix as obtained from the Hessian matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:179:    -   location: config_3_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:182:            used. This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:185:    -   location: config_3_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:188:            used. This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:192:    -   location: config_3_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:195:            used. This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:198:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:202:    -   location: config_3_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:205:            used. This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:208:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:238:    -   location: config_4_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:241:            presents the statistical correlation matrix as obtained from the Hessian matrix of the fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:244:    -   location: config_4_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:247:            presents the statistical correlation matrix as obtained from the Hessian matrix of the fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:250:    -   location: config_4_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:253:            presents the correlation matrix of the systematic uncertainties, without including any uncertainties
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:256:    -   location: config_4_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:259:            presents the correlation matrix of the systematic uncertainties, without including any uncertainties
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:262:    -   location: config_4_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:265:            presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:267:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:272:    -   location: config_4_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:275:            presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:277:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:308:    -   location: config_5_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:311:            This table presents the statistical correlation matrix as obtained from the Hessian matrix of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:314:    -   location: config_5_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:317:            This table presents the statistical correlation matrix as obtained from the Hessian matrix of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:320:    -   location: config_5_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:323:            This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:326:    -   location: config_5_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:329:            This table presents the correlation matrix of the systematic uncertainties, without including
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:333:    -   location: config_5_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:336:            This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:339:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:343:    -   location: config_5_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:346:            This table presents the total correlation matrix when summing the statistical and systematic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:349:            correlation matrix and the systematic uncertainties from the Neyman construction are treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:379:    -   location: config_6_correlation_stat.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:382:            table presents the statistical correlation matrix as obtained from the Hessian matrix of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:385:    -   location: config_6_correlation_stat.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:388:            table presents the statistical correlation matrix as obtained from the Hessian matrix of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:391:    -   location: config_6_correlation_syst.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:394:            table presents the correlation matrix of the systematic uncertainties, without including any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:397:    -   location: config_6_correlation_syst.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:400:            table presents the correlation matrix of the systematic uncertainties, without including any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:404:    -   location: config_6_correlation_total.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:407:            table presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:409:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:414:    -   location: config_6_correlation_total.json
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:417:            table presents the total correlation matrix when summing the statistical and systematic covarainces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata/extracted/submission.yaml:419:            When adding the Neyman consrtruction uncertainties, no change is made to the statistical correlation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:19:\subsection{Headline result (non-linear)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:30:model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & params \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:36:\caption{$B_{s}\to\phi\mu\mu$ non-linear frozen-kernel fit on LHCb 2015,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:39:AIC by $0.24$ unit at equal $k=1$. Both fits give a sign-uniform
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:40:negative $\Delta C_{9}^{\mathrm{eff}}$. Mode-B linearised fit gave
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:41:$\Delta\mathrm{AIC}=-0.08$; values are essentially equivalent at this
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:46:The 500-trial bootstrap on bins (run under Mode B, retained as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:49:poorly constrained. Region splits under Mode B give $A=+5.31$ in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:59:is roughly $4\times$ larger than the four $B \to K^{*}$ non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:125:$P$-basis (where LHCb 2025, CMS 2025, LHCb 2015, LHCb 2021 all
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:138:$B\to K^{*}$ (above). Using the non-linear LHCb 2025 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:144:The non-linear refit gives $A^{\mathrm{Bs}\to\phi}_{S, \text{observed}} = +4.98$, a factor of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:167:\subsection{Acceptance gates (cross-channel, non-linear)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:178:VFD AIC competitive with FREE\_C9   & \textsc{observed} (marginal $\Delta\mathrm{AIC}=-0.24$, $w_{\mathrm{VFD}}\approx 0.53$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:185:\caption{The non-linear cross-channel fit is sign-consistent with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:186:four $B\to K^{*}$ fits and AIC-degenerate with FREE\_C9; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:206:analysis lacks a published correlation matrix on HEPData; Belle II had
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/src/vfd_b_anomaly/flavio_predictor.py:5:project's hand-tabulated `sm_baseline` is fixed to the LHCb 2025 8-bin
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_cross_channel/ins1380188/HEPData-ins1380188-v1-yaml/submission.yaml:2:  CERN-LHC.  An angular analysis and a measurement of the differential branching fraction of the decay $B^0_s\to\phi\mu^+\mu^-$ are presented, using data corresponding to an integrated luminosity of $3.0\, {\rm fb^{-1}}$ of $pp$ collisions recorded by the LHCb experiment at $\sqrt{s} = 7$ and $8\, {\rm TeV}$. Measurements are reported as a function of $q^{2}$, the square of the dimuon invariant mass and results of the angular analysis are found to be consistent with the Standard Model. In the range $1<q^2<6\, {\rm GeV}^{2}/c^{4}$, where precise theoretical calculations are available, the differential branching fraction is found to be more than $3\,\sigma$ below the Standard Model predictions.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:8:own $q^{2}$ bin grid, its own published correlation matrix where
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:9:available, and its own per-bin SM and non-linear new-physics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:24:LHCb 2025 (ref)   & $B^{0}\to K^{*0}\mu\mu$  & 2512.18053 & ins3094698 & 8.4 & 8 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:34:CMS 2025 publishes block-diagonal correlation for 6 $q^{2}$ bins
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:37:\subsection{Headline result (non-linear)}\label{subsec:cross_headline_nl}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:40:$P_{5}', P_{4}', P_{1}, P_{2}$, matching the LHCb 2025 reference fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:53:        $\Delta\mathrm{AIC}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:56:LHCb 2021 ($B^{+}\to K^{*+}$) & 32 & 22.77 & $-1.82$ & 22.93 & $\boldsymbol{+2.06}$ & $-1.59$ & $+0.17$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:58:LHCb 2025 (ref)               & 32 & 40.89 & $-1.00$ & 41.98 & $\boldsymbol{+1.14}$ & $-0.86$ & $+1.09$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:63:\caption{Headline non-linear cross-dataset and cross-channel results.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:65:$B_{s}\!\to\!\phi$, both by $\Delta\mathrm{AIC}=-0.24$) and disfavoured
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:66:on $3/5$ (LHCb 2021, CMS 2025 no-$P_{4}'$, LHCb 2025; max
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:67:$\Delta\mathrm{AIC}=+1.09$). $A>0$ in every fit;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:83:$A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:86:non-linear $\Delta\mathrm{AIC}$ marginally favours VFD and orange
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:94:To convert the per-dataset $\Delta\mathrm{AIC}$ values into a single
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:96:dataset, $w_{M,d} = e^{-\Delta\mathrm{AIC}_{M,d}/2} / \sum_{M'}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:97:e^{-\Delta\mathrm{AIC}_{M',d}/2}$, and stack across datasets under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:107:dataset & non-linear $\Delta\mathrm{AIC}$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:113:LHCb 2025                  & $+1.093$ & $0.633$ & $0.367$ & FREE\_C9 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:117:\textbf{0.652} & \textbf{0.348} & \textbf{FREE\_C9 (mild)} \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:143:\paragraph{Cross-dataset amplitude scatter.} The non-linear fitted
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:158:criterion & result (non-linear) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:160:\textbf{$\mathrm{VFD\ AIC} \leq \mathrm{FREE\_C9\ AIC}$ on every dataset}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:161:   & \textbf{\textsc{fail}} (passes on $2/5$; max $\Delta\mathrm{AIC}=+1.09$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:163:   & \textbf{\textsc{fail}} ($w_{\mathrm{VFD}} = 0.348$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:171:\caption{Cross-dataset acceptance gates under the headline non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:172:analysis. The two strict AIC-preference gates (top) \textsc{fail}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:173:under non-linear evaluation; the four direction-consistency and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:176:preferred model on AIC.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:181:Including CMS 2025's published $P_{4}'$ values in the linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:182:Mode-B fit produced $\chi^{2}=169$ over 24 data points — about
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:189:the convention mismatch. Both $\Delta\mathrm{AIC}$ values agree
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:190:qualitatively (FREE\_C9 favoured by $\sim 0.5$ AIC unit either way)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:191:under non-linear refit; the no-$P_{4}'$ result is the one quoted in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:202:AIC criterion at equal parameter cost, the kernel does not improve
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:203:over a constant Wilson-coefficient shift on the headline non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:7:  The reported central values of the angular observables in Table 1 and 2 are evaluated using angular folding techniques. The asymmetric statistical uncertainties are obtained by Feldman-Cousins scans. The correlation between all observables are determined using a bootstrapping method.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:376:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:393:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:410:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:427:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:444:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:461:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:478:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:495:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:512:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:529:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:546:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:563:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:580:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:597:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:614:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:631:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:648:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:665:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:682:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/submission.yaml:699:      analysis, angular observables, correlations]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_regions.csv:1:dataset,region,q2_range,n_bins,n_data,FREE_C9_chi2,FREE_C9_DC9,VFD_chi2,VFD_A,VFD_DC9_eff,delta_aic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:13:linearised Mode-B response (Eq.~\ref{eq:modeB}). The headline non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:14:analysis on LHCb 2025 (\S\ref{subsec:joint_fit}) gives different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:16:$\Delta\mathrm{AIC}$ of opposite sign vs $\mathrm{FREE\_C9}$ (see
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:17:Table~\ref{tab:joint_fit_modes}). What the Mode-B stress tests
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:182:transfer to the non-linear refit.}} \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:185:\caption{Stress-test acceptance summary on the LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:186:multi-observable joint fit, all under the linearised Mode-B response.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:188:to the non-linear regime, but Mode-B AIC numbers do not.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:187:data_file: correlation_matrix_q2_bin_0.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:205:data_file: correlation_matrix_q2_bin_1.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:223:data_file: correlation_matrix_q2_bin_2.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:241:data_file: correlation_matrix_q2_bin_3.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:259:data_file: correlation_matrix_q2_bin_5.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins2850101/HEPData-ins2850101-v1-yaml/submission.yaml:277:data_file: correlation_matrix_q2_bin_7.yaml
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4h.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:5:CMS 2025, LHCb 2025). WO-015 asks: does the same kernel — with no shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:35:data points**, no published correlations on HEPData (diagonal
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:41:| model | k | χ² | AIC | BIC | ΔAIC vs FREE_C9 | params |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:43:| FREE_C9 (k=1)             | 1 | 13.20 | 15.20 | 16.37 |  0.00 | ΔC9 = **−4.37** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:52:| 3. VFD AIC competitive with FREE_C9      | PASS (marginal, ΔAIC = −0.08) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:75:| region | q² range | n_data | FREE_C9 χ² | FREE_C9 ΔC9 | VFD χ² | VFD A | ΔAIC |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:84:FREE_C9 (ΔAIC = 0.00) and gives A = +5.31 (broadly consistent with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:112:1. No published correlation matrix for Bs → φμμ angular (HEPData
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:117:3. Limited statistics (3 fb⁻¹ vs 8.4 fb⁻¹ for LHCb 2025).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:129:- VFD ties or marginally beats FREE_C9 (k=1 vs k=1) on the global fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:161:| dataset | decay | n | A | ΔC9_eff | ΔAIC | source |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:166:| LHCb 2025         | B⁰ → K*⁰ μμ | 32 | +1.59 | −1.37 | −1.67 | WO-014 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.md:174:- **beats or ties FREE_C9 in AIC on every dataset**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4g.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:2:\section{Results on LHCb 2025}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:5:This section reports the kernel fit on the LHCb 2025 dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:8:$(P_{5}', P_{4}', P_{1}, P_{2})$. We report the headline non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:9:result first; the linearised Mode-B numbers are then quoted as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:12:\subsection{Joint fit, four observables (non-linear, headline)}\label{subsec:joint_fit}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:15:LHCb $32{\times}32$ correlation matrix:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:27:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:30:\textbf{FREE\_C9} (non-linear)  & 1 &  \textbf{40.89} &  \textbf{42.89} & $\boldsymbol{0.00}$ & $\Delta C_{9}=-1.00$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:31:VFD\_GREEN\_600CELL (non-linear)& 1 &  41.98 &  43.98 & $+1.09$ & $A=+1.14$, $\Delta C_{9}^{\mathrm{eff}}=-0.86$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:34:\caption{Headline non-linear joint fit on the four LHCb 2025 angular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:37:AIC by $1.09$ units, a marginal preference (Akaike weight ratio
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:48:on the LHCb 2025 four-observable joint fit, evaluated under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:49:non-linear $\mathrm{FREE\_C9}$ best fit ($\Delta C_{9}=-1.00$) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:50:the non-linear VFD best fit ($A=+1.14$). Dashed lines mark the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:58:\subsection{Mode-B linearised fit (diagnostic only)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:60:The earlier project iteration used the Mode-B linearised response of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:71:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:74:FREE\_C9 (Mode B)           & 1 &  39.30 &  41.30 & $0.00$  & $\Delta C_{9}=-1.34$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:75:VFD\_GREEN\_600CELL (Mode B)& 1 &  37.63 &  39.63 & $-1.67$ & $A=+1.59$, $\Delta C_{9}^{\mathrm{eff}}=-1.37$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:78:\caption{Linearised Mode-B fit on the same data. Under the linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:79:model $\mathrm{VFD\_GREEN\_600CELL}$ has lower AIC by $1.67$ units.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:80:This number does not survive non-linear evaluation: see
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:85:\subsection{Linearised vs non-linear: drift diagnostic}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:92:quantity & linearised (Mode B) & non-linear refit & drift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:96:$\Delta\mathrm{AIC}$ (VFD vs FREE) & $-1.67$ & $+1.09$ & $\mathbf{+2.77}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:103:\caption{Comparison of the same fit under Mode-B linearisation vs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:105:$\Delta\mathrm{AIC}$ is $2.77$ units, larger than the Mode-B
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:106:preference itself: the headline flips sign under non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:115:\subsection{Single-observable fit on $P_{5}'$ (linearised, retained as a check)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:118:single-observable $P_{5}'$ fit under the linearised Mode-B response.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:124:($\Delta\mathrm{AIC}=-7.00$ vs FREE\_C9), reflecting that $P_{5}'$ is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:128:not run in non-linear mode because the conclusion (the kernel is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:132:\subsection{Leave-one-observable-out stability (linearised, retained)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:134:Refitting the shared kernel under Mode B after removing one of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:142:dropped & $n$ remaining & $A$ (Mode B) & $\Delta C_{9}^{\mathrm{eff}}$ mean & $\chi^{2}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:149:all (reference, Mode B)  & 32 & 1.594 & $-1.367$ & 37.63 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:153:Mode B (linearised). $A$ varies within $\pm 3\,\%$ across the four
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:155:always negative. The non-linear LOO produces qualitatively the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:157:($A\in[1.05, 1.20]$); we retain the linearised values here for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:166:joint-fit test were stated for the linearised analysis. Under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:167:headline non-linear analysis they read as follows:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:169:\item $\mathrm{VFD\_GREEN\_600CELL}\ \mathrm{AIC} \leq \mathrm{FREE\_C9}\ \mathrm{AIC}$:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:170:  \textsc{fail} (non-linear $\Delta\mathrm{AIC}=+1.09$, marginal in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:175:  on every bin in the headline non-linear fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:181:Acceptance criterion (i) does not pass under the headline non-linear
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:183:indistinguishable from a constant Wilson-coefficient shift on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:188:non-linear analysis.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4f.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015_cross_channel.csv:2:Bs2phi-LHCb-2015,Bs->phimumu,FREE_C9,24,1,13.195107020387567,15.195107020387567,16.373160850735513,0.0,-4.365832398383627,-4.365832398383627,DC9=-4.366
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4e.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:8:2I-equivariant graph realisation on the 600-cell $V_{600}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:11:kernel; the continuum and bounded variants are reported as theoretical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:62:(\ref{eq:dirichlet_mode}) fit the LHCb 2025 $P_{5}'$ data at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:63:$\Delta\mathrm{AIC}\approx -7$ vs $\mathrm{FREE\_C9}$ on $P_{5}'$ alone
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:64:under the linearised \texttt{flavio} response (section~\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:67:AIC penalty: $c_{3}/c_{1} = 0.18$, well below any $\varphi$-rational
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:70:\subsection{Layer 3 — discrete 2I-equivariant lift on $V_{600}$}\label{subsec:layer3}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:129:The empirical correlation between Eqs.~\eqref{eq:greens_continuum} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:130:\eqref{eq:kappa_lift} on the LHCb 2025 bin centres is $r=0.997$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:133:together with the continuum exponential and the LHCb 2025 bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:143:$e^{-|x|/\varphi}$ from Layer 1, with empirical correlation $r=0.997$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:151:\paragraph{Cocycle, edge weighting, and variant selection.} The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:160:for each variant; the shell-mean profile is then compared to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:161:continuum kernel $e^{-|x|/\varphi}$ and to the LHCb 2025 $P_{5}'$ data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:163:criterion (correlation between the discrete shell-mean and the Layer-1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:165:criterion ($\chi^{2}$ against the LHCb 2025 single-observable fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:172:variant & $\mathrm{corr}(\overline{\psi}, e^{-|x|/\varphi})$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:173:        $\chi^{2}$ vs LHCb 2025 $P_{5}'$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:176:unweighted Laplacian          & $\mathbf{0.9968}$ & $\mathbf{13.555}$ & $1$ on both \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:182:pure-geometry criterion (correlation with the Layer-1 continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:184:variant choice is consistent with selection on geometric grounds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:186:Reproducible from \texttt{scripts/wo016b\_variant\_geometry.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:187:(reports/wo016b\_variant\_geometry.csv).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:188:\label{tab:variant_selection}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:192:two-criterion agreement means the variant choice does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:193:extra effective fit parameter: the variant choice would have been the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:194:same if only the geometric criterion had been applied, and the AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:215:(Eq.~\ref{eq:Lphi}), and the variant table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:216:(Table~\ref{tab:variant_selection}). A reader unfamiliar with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:221:with 2I-equivariant boundary maps from the 1200 triangular faces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4d.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:71:LHCb 2025 / CMS 2025 / LHCb 2015 / LHCb 2021 all publish the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:92:1. The Bs→φ 2015 dataset has no published correlation matrix; the WO-015
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:104:the data is most informative), the kernel ties FREE_C9 with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:116:| LHCb 2025 (P-basis)  | P | +1.594 | +1.594 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo015b_basis_diagnostic.md:129:  is sign-uniform, ΔAIC ≤ 0 in every fit; the residual amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:10:\item \textbf{LHCb 2025} — $B^{0}\!\to\!K^{*0}\mu^{+}\mu^{-}$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:13:  systematic, and total correlation matrix; 27 dependent variables in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:28:  $8{\times}8$ correlation blocks across observables (block-diagonal
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:33:  windows excluded). Per-bin correlation matrices for bins 0,1,2,3,5,7.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:44:\subsection{SM and new-physics predictions (non-linear, headline)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:65:that varies by bin; the non-linear evaluation is performed once per
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:70:\subsection{Linearised response (Mode B; reported as diagnostic)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:72:An earlier iteration of this analysis used a linearised first-order
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:87:This `Mode B' analysis is retained for two reasons: (i) it
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:90:(ii) the difference between linearised and non-linear $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:91:quantifies the non-linearity. On the LHCb 2025 joint fit the per-bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:94:$\Delta\mathrm{AIC}$ drifts from $-1.67$ (linearised) to $+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:95:(non-linear refit), a $2.77$-AIC-unit shift that flips the sign of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:98:\emph{The non-linear analysis is the one reported as headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:99:throughout; linearised values appear only as marked
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:105:\texttt{flavio} 2.4 changed the linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:108:\citep{AltmannshoferStraub2013}. The non-linear $\mathrm{FREE\_C9}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:109:best-fit on the LHCb 2025 4-observable joint fit is $-1.00$, lower
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:110:in magnitude than the linearised value precisely because of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:115:We use a Gaussian $\chi^{2}$ likelihood
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:125:$\mathrm{AIC}=\chi^{2}+2k$ \citep{Akaike1974} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:136:  $C_{10}$, $k=2$ (used in the linearised stress test of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:138:\item Charm-loop Gaussian — a free-amplitude, free-width Gaussian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:148:For the headline non-linear analysis, the optimiser is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:150:$\mathrm{xtol}=5\times 10^{-4}$; for Mode B the optimiser is Powell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:164:correlation information used in the all-data fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:179:non-linear optimiser & \texttt{scipy.minimize\_scalar} (Brent), xtol $5\!\times\!10^{-4}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:180:linearised optimiser (Mode B) & \texttt{scipy.minimize} Powell, tol $10^{-7}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:181:non-linear search bracket ($\Delta C_{9}$) & $[-3.0,\,+0.5]$ ($B\!\to\!K^{*}$); $[-6.0,\,+0.5]$ ($B_{s}\!\to\!\phi$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:182:non-linear search bracket ($A$) & $[0.0,\,8.0]$ ($B\!\to\!K^{*}$); $[0.0,\,20.0]$ ($B_{s}\!\to\!\phi$) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4c.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4b.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:34:of a finite 2I-equivariant graph (the 600-cell $V_{600}$, vertices and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:64:This paper reports two analyses of the same data: a linearised fit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:67:non-linear fit using \texttt{flavio.np\_prediction} directly. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:70:comparisons. \emph{We treat the non-linear analysis as the headline;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:71:the linearised analysis is reported as a methodology diagnostic.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:73:We claim the following (non-linear refit):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:75:\item On the LHCb 2025 dataset, the geometry-derived kernel and a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:77:  parameter cost ($k=1$ each), with $\Delta\mathrm{AIC}=+1.09$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:82:  LHCb 2025 (8.4\,fb$^{-1}$), and the cross-channel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:83:  $B_{s}\!\to\!\phi\mu\mu$ — the non-linear $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:102:\item That the kernel beats $\mathrm{FREE\_C9}$ on AIC. It does not,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:103:  on the headline non-linear analysis. A free-width charm-loop
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:104:  Gaussian also fits comparably (\S\ref{sec:stress}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:116:amplitude per dataset is consistent (sign-uniform; AIC-degenerate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:3:**Question.** WO-013 showed the universality result on the LHCb 2025 dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:24:| CMS 2025          | B⁰→K*⁰ μμ  | 2410.18247 | ins2850101 | 140 fb⁻¹   | 6 (results_p*.yaml + correlation_matrix_q2_bin_*.yaml) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:25:| LHCb 2025 (ref.)  | B⁰→K*⁰ μμ  | 2512.18053 | ins3094698 | 8.4 fb⁻¹   | 8 (config_2 — already in repo) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:31:(no inter-bin correlations exposed).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:42:| dataset | n | FREE_C9 χ² | FREE_C9 ΔC9 | VFD χ² | **VFD A** | VFD ΔC9_eff | ΔAIC (VFD−FREE) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:48:| LHCb 2025 (ref)      | 32 |  39.3 | −1.34 |  37.6 | **+1.59** | −1.37 | −1.67 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:57:| VFD AIC ≤ FREE_C9 AIC on every dataset | PASS — ΔAIC < 0 in all 5 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:66:    LHCb 2025:            A = +1.594
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:85:prefers the kernel by 0.55 AIC over a free C9 shift is the relevant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:95:S4-without-the-2-factor variant. With P4' dropped, the CMS amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:99:affects FREE_C9 and VFD identically**, so the *relative* ΔAIC is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:109:  LHCb 2015, LHCb 2021 B⁺→K*⁺, CMS 2025, plus the existing LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:126:- Slopes are linearised at the SM. Large excursions (ΔC9 ~ −2.3 for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:132:  with much larger uncertainties and no published correlation matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:153:> - LHCb 2025 (8.4 fb⁻¹)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:169:  a free 2-parameter centre-peaked Gaussian (charm-loop proxy) fits
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.md:176:  arise from a 2I-equivariant spectral construction; whether the data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig4a.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:1:dataset,decay,model,n_data,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,A_or_DC9,DC9_eff_mean,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:2:LHCb-2015,B0->K*mumu,FREE_C9,32,1,31.59959432998963,33.59959432998963,35.06533023278936,0.0,-1.4793748908390585,-1.4793748908390585,DC9=-1.479
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:4:LHCb-2021-Kstplus,B+->K*+mumu,FREE_C9,32,1,27.11607072037183,29.11607072037183,30.581806623171556,0.0,-2.2437859535603693,-2.2437859535603693,DC9=-2.244
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:6:CMS-2025,B0->K*mumu,FREE_C9,24,1,169.35257876006892,171.35257876006892,172.53063259041687,0.0,-1.4870700145558682,-1.4870700145558682,DC9=-1.487
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:8:CMS-2025-noP4p,B0->K*mumu,FREE_C9,18,1,43.21465711778693,45.21465711778693,46.10502887568309,0.0,-1.3549233139256784,-1.3549233139256784,DC9=-1.355
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo014_cross_dataset.csv:10:LHCb-2025,B0->K*mumu,FREE_C9,32,1,39.30340988916652,41.30340988916652,42.769145791966245,0.0,-1.340331410060973,-1.340331410060973,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/references.bib:6:% --- LHCb 2025 (current B0 -> K*0 mumu, 8.4 fb^-1) ---
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:2:  CERN-LHC. An angular analysis of the $B^{0} \rightarrow K^{*0}(\rightarrow K^{+}\pi^{-})\mu^{+}\mu^{-}$ decay is presented. The dataset corresponds to an integrated luminosity of $3.0$ fb$^{-1}$ of $pp$ collision data collected at the LHCb experiment. The complete angular information from the decay is used to determine $C\!P$-averaged observables and $C\!P$ asymmetries, taking account of possible contamination from decays with the $K^{+}\pi^{-}$ system in an S-wave configuration. The angular observables and their correlations are reported in bins of $q^2$, the invariant mass squared of the dimuon system. The observables are determined both from an unbinned maximum likelihood fit and by using the principal moments of the angular distribution. In addition, by fitting for $q^2$-dependent decay amplitudes in the region $1.1 < q^{2} < 6.0 \mathrm{\,GeV}^{2}/c^{4}$, the zero-crossing points of several angular observables are computed. A global fit is performed to the complete set of $C\!P$-averaged observables obtained from the maximum likelihood fit. This fit indicates differences with predictions based on the Standard Model at the level of 3.4 standard deviations. These differences could be explained by contributions from physics beyond the Standard Model, or by an unexpectedly large hadronic effect that is not accounted for in the Standard Model predictions.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:149:  Likelihood correlation matrix $0.1 < q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:165:  Likelihood correlation matrix $1.1 < q^2 < 2.5~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:181:  Likelihood correlation matrix $2.5 < q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:197:  Likelihood correlation matrix $4.0 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:213:  Likelihood correlation matrix $6.0 < q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:229:  Likelihood correlation matrix $11.0 <q^2< 12.5 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:245:  Likelihood correlation matrix $15.0 < q^2 < 17.0 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:261:  Likelihood correlation matrix $17.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:277:  Likelihood correlation matrix $1.1 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:293:  Likelihood correlation matrix $15.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:309:  Likelihood correlation matrix $0.1 < q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:325:  Likelihood correlation matrix $1.1 < q^2 < 2.5~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:341:  Likelihood correlation matrix $2.5 < q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:357:  Likelihood correlation matrix $4.0 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:373:  Likelihood correlation matrix $6.0 < q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:389:  Likelihood correlation matrix $11.0 <q^2< 12.5 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:405:  Likelihood correlation matrix $15.0 <q^2< 17.0 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:421:  Likelihood correlation matrix $17.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:437:  Likelihood correlation matrix $1.1 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:453:  Likelihood correlation matrix $15.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:469:  Likelihood correlation matrix $0.1 < q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:485:  Likelihood correlation matrix $1.1 < q^2 < 2.5~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:501:  Likelihood correlation matrix $2.5 < q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:517:  Likelihood correlation matrix $4.0 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:533:  Likelihood correlation matrix $6.0 < q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:549:  Likelihood correlation matrix $11.0 <q^2< 12.5 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:565:  Likelihood correlation matrix $15.0 <q^2< 17.0 ~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:581:  Likelihood correlation matrix $17.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:597:  Likelihood correlation matrix $1.1 <q^2< 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:613:  Likelihood correlation matrix $15.0 <q^2< 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:629:  Bootstrap correlation matrix $0.10 < q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:645:  Bootstrap correlation matrix $1.1 < q^2 < 2.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:661:  Bootstrap correlation matrix $2.0 < q^2 < 3.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:677:  Bootstrap correlation matrix $3.0 < q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:693:  Bootstrap correlation matrix $4.0 < q^2 < 5.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:709:  Bootstrap correlation matrix $5.0 < q^2 < 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:725:  Bootstrap correlation matrix $6.0 < q^2 < 7.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:741:  Bootstrap correlation matrix $7.0 < q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:757:  Bootstrap correlation matrix $11.00 <q^2 < 11.75~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:773:  Bootstrap correlation matrix $11.75 <q^2 < 12.50~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:789:  Bootstrap correlation matrix $15.0 <q^2 < 16.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:805:  Bootstrap correlation matrix $16.0 <q^2 < 17.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:821:  Bootstrap correlation matrix $17.0 <q^2 < 18.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:837:  Bootstrap correlation matrix $18.0 <q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:853:  Bootstrap correlation matrix $15.0 <q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:869:  Bootstrap correlation matrix $0.10 < q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:885:  Bootstrap correlation matrix $1.1 < q^2 < 2.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:901:  Bootstrap correlation matrix $2.0 < q^2 < 3.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:917:  Bootstrap correlation matrix $3.0 < q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:933:  Bootstrap correlation matrix $4.0 < q^2 < 5.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:949:  Bootstrap correlation matrix $5.0 < q^2 < 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:965:  Bootstrap correlation matrix $6.0 < q^2 < 7.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:981:  Bootstrap correlation matrix $7.0 < q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:997:  Bootstrap correlation matrix $11.00 <q^2 < 11.75~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1013:  Bootstrap correlation matrix $11.75 <q^2 < 12.50~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1029:  Bootstrap correlation matrix $15.0 <q^2 < 16.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1045:  Bootstrap correlation matrix $16.0 <q^2 < 17.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1061:  Bootstrap correlation matrix $17.0 <q^2 < 18.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1077:  Bootstrap correlation matrix $18.0 <q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1093:  Bootstrap correlation matrix $15.0 <q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1109:  Bootstrap correlation matrix $0.1 <q^2 < 0.98~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1125:  Bootstrap correlation matrix $1.1 <q^2 < 2.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1141:  Bootstrap correlation matrix $2.0 <q^2 < 3.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1157:  Bootstrap correlation matrix $3.0 <q^2 < 4.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1173:  Bootstrap correlation matrix $4.0 <q^2 < 5.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1189:  Bootstrap correlation matrix $5.0 <q^2 < 6.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1205:  Bootstrap correlation matrix $6.0 <q^2 < 7.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1221:  Bootstrap correlation matrix $7.0 <q^2 < 8.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1237:  Bootstrap correlation matrix $11.0 <q^2 < 11.75~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1253:  Bootstrap correlation matrix $11.75 <q^2 < 12.5~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1269:  Bootstrap correlation matrix $15.0 <q^2 < 16.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1285:  Bootstrap correlation matrix $16.0 <q^2 < 17.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1301:  Bootstrap correlation matrix $17.0 < q^2 < 18.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1317:  Bootstrap correlation matrix $18.0 < q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/submission.yaml:1333:  Bootstrap correlation matrix $15.0 < q^2 < 19.0~{\rm GeV}^2/c^4$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3h.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/README.md:72:Round 2 review found that the linearised Mode-B fit's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/README.md:73:$\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 did not survive a non-linear
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:95:joint constraint over all B→K* BSZ form-factor coefficients, correlations
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:116:In every test above, only the amplitude `A` (or, for FREE_C9 / FREE_C9+C10,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:128:| 2. q² region splits | universality across regions, no sign flip | PASS (3/3 regions ΔAIC < 0, all A>0, all ΔC9_eff<0) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:129:| 3. C9 + C10 | adding C10 does not displace VFD | PASS (FREE_C9+C10 ΔAIC = +1.73; VFD wins) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:130:| 3. charm-loop nuisance | VFD competitive at same shape level | PARTIAL — charm-loop ΔAIC = −1.91 (k=2) vs VFD −1.67 (k=1); VFD wins per-parameter |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:139:model that gains over VFD is a 2-parameter centre-peaked Gaussian, and that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:140:gain is below 1 AIC unit — consistent with picking up the same structural
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_stress_test.md:156:- The charm-loop Gaussian is a phenomenological proxy, not a physical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3g.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3f.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_regions.csv:1:region,q2_range,n_bins,n_data,FREE_C9_chi2,FREE_C9_DC9,FREE_C9_aic,VFD_chi2,VFD_amplitude,VFD_DC9_eff,VFD_aic,delta_aic_VFD_vs_FREE
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_regions.csv:2:low_q2,"(0.06, 4.0)",3,12,20.863885005208587,-1.1325436424697062,22.863885005208587,20.771149995718762,1.3974,-1.1241015713252065,22.771149995718762,-0.09273500948982516
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1409497/HEPData-ins1409497-v1-yaml/Table4.yaml:24:    - asymerror: {minus: -0.348, plus: 0.364}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:51:$\Delta\mathrm{AIC}$ values span $[-0.24, +1.09]$ around zero, with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:53:$w_{\mathrm{FREE\_C9}}=0.65$. AIC compares per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:57:independent of, and complementary to, the AIC tie. An earlier
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:58:linearised analysis (Mode B, linear in $\Delta C_{9}$ via
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:60:that does not survive the non-linear refit; the linearised numbers are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:65:derived from a finite 2I-equivariant graph substrate (the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:76:edge-weighting variants, the unweighted Laplacian is selected by a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:77:\emph{pure-geometry criterion} (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:82:non-linear-in-$C_{9}$ predictions on each dataset's own bin grid, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:111:\noindent\emph{(iv) AIC comparison.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:113:$\mathrm{FREE\_C9}$ (also $k=1$), the per-dataset $\Delta\mathrm{AIC}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:117:data the two models are statistically indistinguishable on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:121:claim independent of the AIC tie. AIC measures per-parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:124:unique $q^{2}$ shape consistent with the anomaly: a free-width
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:125:Gaussian charm-loop proxy fits marginally better in $\chi^{2}$ at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:129:$b\to s\ell\ell$ data. An earlier linearised analysis (linear in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:132:non-linear refit; the linearised numbers are retained in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.tex:152:non-linear refit headline of this paper rests entirely on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3e.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3d.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/data2.yaml:467:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3b.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3a.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/data1.yaml:467:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/data/raw/hepdata_legacy/ins1838196/HEPData-ins1838196-v1-yaml/Fig3c.yaml:61:- header: {name: dimuon invariant mass squared, units: GEV**2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:1:model,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,params
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:2:FREE_C9,1,39.31675580142509,41.31675580142509,42.78249170422482,0.0,DC9=-1.340
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:4:FREE_C9 + FREE_C10,2,39.049662892777846,43.049662892777846,45.981134698377296,1.7329070913527573,"DC9=-1.395, DC10=+0.186"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo013_alternatives.csv:5:"Charm-loop Gaussian (free A, sigma)",2,35.41169043468848,39.41169043468848,42.34316224028793,-1.9050653667366078,"A=+1.832, sigma=8.960 GeV^2"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:9:    "delta_aic_vs_FREE_C9":1.4732607826,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:17:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:23:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:37:    "delta_aic_vs_FREE_C9":-0.8006645909,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:51:    "delta_aic_vs_FREE_C9":-0.4368311136,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:65:    "delta_aic_vs_FREE_C9":1.458458039,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.json:80:    "delta_aic_vs_FREE_C9":2.8587929029,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/README.md:20:│   └── wo013_stress_test.py          # linearised stress test (bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/README.md:22:└── reports/                 # outputs of the above + linearised
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/README.md:26:                              # superseded by the non-linear refit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/README.md:33:The paper's headline numbers come from the non-linear flavio refit
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/README.md:35:linearised cross-dataset and stress-test outputs are diagnostic, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.csv:1:model,k_params,chi2,amplitude,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,correlation_with_exp,correlation_with_cos,eigenvalue,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.csv:3:FREE_C9,1,6.704573090964229,-0.15362183379908242,0.0,0.8006645909488093,,,,global C_9 shift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.csv:1:model,role,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,delta_bic_vs_FREE_C9,effective_delta_c9_mean,per_observable_delta_c9,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.csv:3:FREE_C9,reference,1,204.45608467044792,206.45608467044792,207.2286733926877,0.0,0.0,0.1938680707162974,"{'BR': 0.1938680707162974, 'P5p': 0.1938680707162974}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:10:cos(pi x / (2 L))) at correlation > 0.95.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:21:**Operator.** Three variants, all with Dirichlet BC psi(+/-4) = 0:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:23:| variant | operator | meaning |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:34:**Procedure.** For each variant:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:41:5. Report chi^2, AIC, the eigenvalue lambda_1, and Pearson correlations
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:48:| variant | chi^2 | A_hat | lambda_1 | r vs exp | r vs cos | dAIC vs FREE_C9 | dAIC vs KAPPA_EXP |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:50:| FREE_C9            | 6.70 | DC9 = -0.154 | -    | -     | -     |  0.00 | +0.80 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:64:The free / phi-mass variants produce the discrete sine shape sin(pi k / 8)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:66:mode. The phi-cocycle variant is sharply localised at the centre by the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:75:- **dAIC vs FREE_C9 <= 0:** YES, all three variants.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:79:- **No fitted width, no fitted centre, only amplitude A:** YES. Every variant
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:98:3. **Adding the phi-mass term is invariant on eigenvectors.** PHI_MASS and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:104:4. **All three discrete variants beat FREE_C9.** Any of these single-amplitude,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:105:   shape-frozen lifts compresses P5' better than a global C_9 shift on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:106:   The continuum exp kernel still wins by ~0.3-0.5 AIC, but with only 8 bins
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:113:  of the framework, but the full discrete cascade (with 2I-equivariant boundary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:117:- The correlation is high but not 1. The discrete-cocycle eigenvector and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:140:real LHCb P5' data with a single amplitude and beat FREE_C9 on AIC.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md:152:  -> single-amplitude fit, dAIC vs FREE_C9 = -0.28 on real LHCb P5' data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:1:model,role,k_params,chi2,aic,bic,delta_aic_vs_FREE_C9,delta_aic_vs_KAPPA_EXP,coefficients,notes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenmodes.csv:3:FREE_C9,reference,1,6.704573090964229,8.704573090964228,8.784014632644064,0.0,0.8006645909488093,{'delta_c9': -0.15362183379908242},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectrum.csv:77:76,14.0,2.7755575615628914e-17,1.929887443338239e-18,1.929887443338239e-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:19:Compared against the prior champion `kappa_exponential` and the FREE_C9 reference.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:23:`FREE_C9` reference: chi^2 = 6.7046, AIC = 8.7046.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:25:| mode | k | chi^2 | dAIC vs FREE_C9 | eff DC9 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:41:x           : [-2.77 -2.45 -2.08 -1.65 -1.15  0.04  1.10  1.60]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo005_reflective_kernel.md:55:  **WORSE** than the FREE_C9 control (dAIC > +1.9), i.e. worse than a global
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:7:    "delta_aic_vs_FREE_C9":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:9:    "correlation_with_exp":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:10:    "correlation_with_cos":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:15:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:19:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:21:    "correlation_with_exp":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:22:    "correlation_with_cos":null,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:31:    "delta_aic_vs_FREE_C9":-0.8006645909,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:33:    "correlation_with_exp":1.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:34:    "correlation_with_cos":0.8573973265,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:43:    "delta_aic_vs_FREE_C9":-0.4620994693,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:45:    "correlation_with_exp":0.8629405131,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:46:    "correlation_with_cos":0.999905037,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:55:    "delta_aic_vs_FREE_C9":-0.4620994693,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:57:    "correlation_with_exp":0.8629405131,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:58:    "correlation_with_cos":0.999905037,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:67:    "delta_aic_vs_FREE_C9":-0.279376236,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:69:    "correlation_with_exp":0.9827687354,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.json:70:    "correlation_with_cos":0.7643755569,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:6:that compresses the LHCb P5' anomaly with a single amplitude (dAIC = -0.80
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:7:vs FREE_C9). WO-005 ruled out three boundary-anchored variants (sinh,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:36:  partition: a sigma-fixed bulk (invariant under accumulation, Theorem 5.2)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:109:champion, dAIC = -0.80), the empirical kernel is identified as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:117:If `DIRICHLET_M3` adds nothing (dAIC vs M2 around +1 from the AIC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:150:| model | k | chi^2 | AIC | dAIC vs FREE_C9 | dAIC vs KAPPA_EXP |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:153:| FREE_C9        | 1 |  6.70 |  8.70 |  0.00 | +0.80 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:166:1. **The Dirichlet ground state DIRICHLET_M1 beats FREE_C9 (dAIC = -0.44).**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:172:   AIC of each other.** They are the same shape topologically (centre-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:179:   by only 0.10 over DIRICHLET_M1 — far below the 2-AIC threshold for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:268:amplitude k = 1, both peak at the charmonium midpoint, and their AIC values
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:278:P5' alone — both are consistent with the data within 0.4 AIC. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md:309:  with 2I-equivariant boundary projection — would be the proper VFD
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:9:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:20:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:31:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:42:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.json:53:    "delta_aic_vs_FREE_C9":0.0,
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:9:    "delta_aic_vs_FREE_C9":4.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:10:    "delta_bic_vs_FREE_C9":3.5624284566,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:18:    "model":"FREE_C9",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:24:    "delta_aic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:25:    "delta_bic_vs_FREE_C9":0.0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:40:    "delta_aic_vs_FREE_C9":6.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:41:    "delta_bic_vs_FREE_C9":6.3350171788,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:56:    "delta_aic_vs_FREE_C9":4.8317905293,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo006_multi_observable.json:57:    "delta_bic_vs_FREE_C9":5.6043792516,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:19:    - chi^2 / AIC of the amplitude-only fit to LHCb P5'.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:29:FREE_C9 reference: chi^2 = 6.7046, AIC = 8.7046.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:30:Full-kernel correlation with continuum exp(-|x|/phi): r = 0.997.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:32:| N modes | rel. recon. err | r vs full kernel | r vs cont. exp | chi^2 P5' | dAIC vs FREE_C9 | A_hat | lambda_max |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:41:|   100 | ~1e-14 | 1.000 | 0.997 | 6.498 | -0.21 | 0.178 | 14.47 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:42:|   120 (full) | ~1e-14 | 1.000 | 0.997 | 6.498 | -0.21 | 0.178 | 15.71 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:49:chi^2 stays at 6.7046 (= FREE_C9 exactly) and the relative L^2 error stays
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:74:Every truncation level N >= 9 has dAIC vs FREE_C9 strictly negative, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:75:the dAIC monotonically improves as N grows (-0.117 -> -0.129 -> -0.207).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:81:expect chi^2 to *increase* past some N, or the Pearson correlation with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:83:monotonic 0.849 -> 0.944 -> 0.997 as N grows.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.md:88:exp(-|x|/phi) at r = 0.997. This is the WO-009 result re-derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/archive/reports/wo011_spectral.csv:1:n_modes,rel_recon_err,r_vs_full_kernel,r_vs_continuum_exp,chi2_p5p,aic_p5p,delta_aic_vs_FREE_C9,amplitude,lambda_max_used

codex
The local numerics agree with the main reported values so far: vertex/edge/degree counts, shell sizes, spectrum, norm, and all three correlations match `results.json`. The main risks are not arithmetic errors; they are wording and inheritance boundaries.
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/main.tex' | sed -n '1,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/01_introduction.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/02_definition.tex' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/03_substrate.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/04_spectrum.tex' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 240ms:
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
   100	tested variants the unweighted Laplacian wins on the geometry-only
   101	criterion, reproducing the qualitative ranking established
   102	independently by b-anomaly's data $\chi^{2}$ comparison.
   103	
   104	\noindent\emph{(i) Operator definition and properties.}
   105	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   106	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   107	$\Ph^{-2} \approx 0.382$, operator norm
   108	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   109	in one coordinate $x$ is the closed-form Green's function
   110	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   111	
   112	\noindent\emph{(ii) The 600-cell instance.}
   113	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   114	generated by three orbits ($8$~axis, $16$~half-integer,
   115	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   116	on the short-edge graph; the Laplacian has nine eigenvalue classes
   117	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   118	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   119	
   120	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   121	Per-vertex Pearson correlation between the discrete response
   122	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   123	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
   124	vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
   125	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   126	Same source vertex, same fixed shift, no parameter fitting; the
   127	correlation is invariant under choice of source up to numerical
   128	precision (multi-source sweep, \S\ref{sec:limitations}).
   129	
   130	\noindent\emph{(iv) Two independent empirical witnesses.}
   131	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   132	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   133	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   134	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   135	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   136	with one fitted dimensionless amplitude per dataset and the kernel
   137	shape held fixed. (b)~Active regime,
   138	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   139	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   140	condition-dependent self-injection coupling
   141	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   142	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   143	degree, passes eighteen preregistered correspondences (frozen
   144	2026-04-18) and six drug/sleep EEG signatures.
   145	
   146	\noindent\emph{What we do not claim.}
   147	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   148	stability clamp making $\Cph$ strictly positive definite. We do
   149	not claim $\Rsixhundred$ is the unique substrate consistent with
   150	either empirical landing. We do not claim the operator is the
   151	unique kernel shape consistent with the b-anomaly data
   152	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   153	drift caveats are inherited verbatim) nor that the
   154	aria-chess substrate witness establishes a selection theorem on
   155	the adaptive-closure-transport 4-tuple. The structural scope of
   156	this paper is: \emph{one geometry-fixed operator on one fixed
   157	graph appears as the load-bearing object in two independent
   158	empirical works in two distinct regimes, with no shape retuning
   159	between them}.
   160	\end{abstract}
   161	
   162	% =====================================================================
   163	\input{sections/01_introduction.tex}
   164	\input{sections/02_definition.tex}
   165	\input{sections/03_substrate.tex}
   166	\input{sections/04_spectrum.tex}
   167	\input{sections/05_agreement.tex}
   168	\input{sections/06_passive_witness.tex}
   169	\input{sections/07_active_witness.tex}
   170	\input{sections/08_programme_home.tex}
   171	\input{sections/09_limitations.tex}
   172	\input{sections/10_conclusion.tex}
   173	% =====================================================================
   174	
   175	\section*{Reproducibility}
   176	The complete numerical verification (vertex construction,
   177	short-edge graph build, Laplacian spectrum, operator-norm bound,
   178	discrete-to-continuum correlation across three Laplacian variants)
   179	is reproducible from \texttt{repro/verify\_kernel.py} in this
   180	paper's bundle. No randomness, no fitted parameters: all numbers
   181	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   182	\S\ref{sec:agreement} are deterministic outputs of the script.
   183	The two empirical witness preprints
   184	(b-anomaly~\citep{SmartBAnomaly2026},
   185	aria-chess~\citep{SmartAriaChess2026}) carry their own
   186	reproducibility artifacts; this paper does not duplicate them.
   187	
   188	\bibliographystyle{plainnat}
   189	\bibliography{references}
   190	
   191	\end{document}

 succeeded in 230ms:
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

 succeeded in 236ms:
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

 succeeded in 246ms:
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

 succeeded in 228ms:
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

exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/05_agreement.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/06_passive_witness.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/07_active_witness.tex' | sed -n '1,280p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/08_programme_home.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/09_limitations.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 224ms:
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
    22	where $\kappa_{V_{600}}(q^{2})$ is the projection of $\Cph$ on
    23	$\Rsixhundred$ to the flavour-physics $q^{2}$ axis (the b-anomaly
    24	preprint's §3 projection construction, which we do not relitigate
    25	here; this is a projection of the operator, not a derivation of
    26	$\Ph^{-2}$), and $A$ is a single fitted dimensionless amplitude
    27	per dataset. The kernel
    28	shape $\kappa_{V_{600}}$ is held fixed across all five datasets.
    29	This is a \emph{structural} test: same fixed $\Cph$ on the same
    30	$\Rsixhundred$, no shape retuning between datasets.
    31	
    32	\subsection{The five-dataset structural fit}
    33	
    34	The b-anomaly preprint reports the following per-dataset table
    35	(verbatim from~\citep{SmartBAnomaly2026}, also at
    36	\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
    37	
    38	\begin{table}[ht]
    39	\centering
    40	\small
    41	\caption{b-anomaly five-dataset structural fit. Verbatim
    42	from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
    43	dataset, kernel shape held fixed.}
    44	\label{tab:banomaly}
    45	\begin{tabular}{l l r r r r}
    46	\toprule
    47	Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
    48	   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
    49	\midrule
    50	LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
    51	LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
    52	CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
    53	LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
    54	LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
    55	\bottomrule
    56	\end{tabular}
    57	\end{table}
    58	
    59	\subsection{What the structural fit establishes}
    60	
    61	\begin{itemize}\itemsep=2pt
    62	\item \textbf{Universality (5/5).} The same fixed kernel shape
    63	  can be fit to all five datasets with one amplitude $A$ per
    64	  dataset and no shape retuning. The kernel never moves between
    65	  datasets.
    66	\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
    67	  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
    68	  reproduces the established direction of the
    69	  anomaly~\citep{LHCbAngular2020} across all five independent
    70	  measurements.
    71	\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
    72	  $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with
    73	  the predicted Krüger--Matias $P$-basis vs $S$-basis amplification
    74	  ($\sim 2.2$~\citep{KrugerMatias2005}), with a residual
    75	  $\sim 50\%$ overshoot. The b-anomaly preprint reports the
    76	  residual as an open item, not a discharge.
    77	\item \textbf{Geometry-first variant test.} Of three discrete
    78	  Laplacian variants on $\Rsixhundred$ (unweighted,
    79	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    80	  unweighted choice wins on both a pure-geometry criterion
    81	  (correlation $0.997$ with the continuum kernel, b-anomaly
    82	  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
    83	  ($\chi^{2}=13.555$). The two criteria agree on the variant
    84	  ranking — a two-criterion convergence on the same fixed
    85	  operator.
    86	\end{itemize}
    87	
    88	\subsection{What the structural fit does \emph{not} establish}
    89	
    90	The b-anomaly preprint is explicit about the following caveats,
    91	which we inherit verbatim:
    92	
    93	\begin{itemize}\itemsep=2pt
    94	\item \textbf{AIC tie on current data.} On Akaike model comparison,
    95	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
    96	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
    97	  indistinguishable: stacked AIC weights
    98	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
    99	  Current data cannot resolve the model comparison. AIC is blind
   100	  to the universality / shape-prediction claim itself, but it is
   101	  decisive about whether the shape is forced by data: it is not.
   102	\item \textbf{Free-width Gaussian alternative.} A free-width
   103	  Gaussian charm-loop proxy fits the same five datasets comparably
   104	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   105	  is not the unique $q^{2}$ shape consistent with the anomaly.
   106	\item \textbf{Mode-B drift (linearised-vs-nonlinear refit).} An
   107	  earlier linearised analysis gave a stronger preference
   108	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   109	  the non-linear refit; the $+2.77$-AIC-unit drift between
   110	  linearised and Mode-B (non-linear) refits is the largest single
   111	  methodological uncertainty in the b-anomaly project.
   112	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   113	  preprint's limitations section acknowledges that the LHCb~2025
   114	  data was looked at first, and only later was the agreement of
   115	  the data-$\chi^{2}$ ranking with the pure-geometry ranking
   116	  verified. The two-criterion agreement is criterion-independent
   117	  but not historically blind.
   118	\end{itemize}
   119	
   120	\subsection{Reading at the operator level}
   121	
   122	The b-anomaly result is the \emph{passive-regime} empirical
   123	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   124	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   125	fixed discrete-to-momentum projection, gives a sign-uniform
   126	description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
   127	five independent measurements without shape retuning. This does
   128	not establish the kernel as theorem-grade physics on the flavour
   129	side (the AIC tie, the free-width Gaussian alternative, and the
   130	Mode-B linearised-vs-nonlinear refit drift prevent that). It does
   131	establish, at the operator level, that the same fixed $\Cph$ on
   132	the same fixed $\Rsixhundred$ is consistent with one of two
   133	independent empirical landings without parameter retuning. The
   134	second landing is in \S\ref{sec:active_witness}.

 succeeded in 233ms:
     1	% =====================================================================
     2	\section{Discrete-to-continuum agreement}\label{sec:agreement}
     3	% =====================================================================
     4	
     5	This is the load-bearing geometric fact of the paper: the discrete
     6	response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a localised
     7	source agrees per-vertex with the continuum kernel
     8	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
     9	the source. We give the test, the numerical result, and a variant
    10	comparison in which the unweighted Laplacian ranks highest among
    11	the three tested variants (unweighted, $\Ph$-geometric weighted,
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
    94	\textbf{Reading.} Among the three tested variants, the unweighted
    95	Laplacian ranks highest on both reported criteria
    96	($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
    97	This reproduces, on a different test, the qualitative ranking the
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

 succeeded in 206ms:
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

 succeeded in 215ms:
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

 succeeded in 262ms:
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

exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/paper/sections/10_conclusion.tex' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-closure-kernel/repro/results.json' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md' | sed -n '1,80p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md' | sed -n '1,160p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016a_akaike_stack.md' | sed -n '1,80p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 315ms:
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
    12	Laplacian spectrum that numerically resolves to the closed-form
    13	$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
    14	discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
    15	the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
    16	chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
    17	the unweighted Laplacian, above the two $\Ph$-cocycle weighted
    18	variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
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

 succeeded in 304ms:
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

 succeeded in 342ms:
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

 succeeded in 328ms:
     1	# WO-016a — Akaike-weight stack across five fits
     2	
     3	Per-dataset AIC deltas and Akaike weights, plus stacked weight.
     4	Stacking assumes independence under the null hypothesis (the five datasets share no observation-level information).
     5	
     6	| dataset | FREE_C9 ΔAIC | VFD ΔAIC | w(FREE_C9) | w(VFD) |
     7	|---|---:|---:|---:|---:|
     8	| LHCb-2015 | 0.241 | 0.000 | 0.4699 | 0.5301 |
     9	| LHCb-2021-Kstplus | 0.000 | 0.168 | 0.5210 | 0.4790 |
    10	| CMS-2025-noP4p | 0.000 | 0.473 | 0.5589 | 0.4411 |
    11	| LHCb-2025 | 0.000 | 1.093 | 0.6333 | 0.3667 |
    12	| Bs2phi-LHCb-2015 | 0.240 | 0.000 | 0.4701 | 0.5299 |
    13	
    14	## Stacked
    15	
    16	- log-evidence(FREE_C9) − log-evidence(VFD) = 0.627
    17	- Total ΔAIC sum (FREE_C9 vs VFD): -1.253
    18	
    19	| model | stacked Akaike weight |
    20	|---|---:|
    21	| FREE_C9 | 0.6517 |
    22	| VFD_GREEN_600CELL | 0.3483 |
    23	
    24	Auxiliary check: under the null hypothesis P(VFD lower AIC on all 5 fits) = $1/2^{5}$ = 0.0312.

 succeeded in 337ms:
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

exec
/bin/bash -lc "rg -n \"18/18|17/18|P4|0\\.190|0\\.143|0\\.239|0/2000|bounded_topk|k=12|eta|0\\.05|0\\.20|six|drug|sleep|alpha|2\\.252|0\\.463|1\\.83|0\\.066|0\\.33|93\\.8|53\\.1|40\\.6|87\\.5|-4\\.4|1003|11\\.58|79\\.78|6\\.80|selection theorem|600-cell uniqueness|consciousness|single-seed|polytope|substrate witness|2026-04-18|seed\" 'papers/aria-chess-paper/paper/main.tex' 'papers/aria-chess-paper/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/main.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/01_introduction.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/02_method.tex' | sed -n '1,280p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/05_results.tex' | sed -n '1,320p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 316ms:
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

 succeeded in 342ms:
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

 succeeded in 358ms:
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

 succeeded in 349ms:
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

 succeeded in 393ms:
papers/aria-chess-paper/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-chess-paper/paper/main.tex:19:\title{A geometry-fixed substrate witness for cortical signatures:\\
papers/aria-chess-paper/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
papers/aria-chess-paper/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
papers/aria-chess-paper/paper/main.tex:53:trajectory at seed~$42$. No shape parameter is tuned to any neural
papers/aria-chess-paper/paper/main.tex:57:coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
papers/aria-chess-paper/paper/main.tex:62:This paper presents an empirical \emph{substrate witness}: it shows
papers/aria-chess-paper/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
papers/aria-chess-paper/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:67:4-polytopes. The companion adaptive-closure-transport
papers/aria-chess-paper/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
papers/aria-chess-paper/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:85:additionally report six drug/sleep EEG signatures tested on a recurrent
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:100:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
papers/aria-chess-paper/paper/main.tex:101:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
papers/aria-chess-paper/paper/main.tex:104:\noindent\emph{(ii) Drug/sleep state transitions.}
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:120:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
papers/aria-chess-paper/paper/main.tex:121:bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
papers/aria-chess-paper/paper/main.tex:122:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:132:8-dimensional V2 features lifts $+40.6$ percentage points on
papers/aria-chess-paper/paper/main.tex:133:leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
papers/aria-chess-paper/paper/main.tex:134:$\to$ substrate-routed $93.8\%$, with state reset; the
papers/aria-chess-paper/paper/main.tex:138:classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
papers/aria-chess-paper/paper/main.tex:143:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
papers/aria-chess-paper/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
papers/aria-chess-paper/paper/main.tex:156:these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
papers/aria-chess-paper/paper/main.tex:160:is reported on a single deterministic trajectory; cross-seed CIs on
papers/aria-chess-paper/paper/main.tex:165:correspondences and six drug/sleep EEG signatures, with all gaps in
papers/aria-chess-paper/paper/main.tex:174:\input{sections/04_consciousness_chain.tex}
papers/aria-chess-paper/paper/main.tex:199:The complete pipeline (substrate construction, six-signature
papers/aria-chess-paper/paper/main.tex:200:consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
papers/aria-chess-paper/paper/main.tex:204:deterministic given seeds; the substrate's spectral decomposition is
papers/aria-chess-paper/paper/main.tex:205:cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
papers/aria-chess-paper/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
papers/aria-chess-paper/paper/sections/02_method.tex:13:\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
papers/aria-chess-paper/paper/sections/02_method.tex:14:(P1--P18) were locked on 2026-04-18 in
papers/aria-chess-paper/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:27:\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
papers/aria-chess-paper/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
papers/aria-chess-paper/paper/sections/02_method.tex:32:cascade-$\alpha$). They are not part of the P1--P18 preregistration;
papers/aria-chess-paper/paper/sections/02_method.tex:37:2026-04-20 validation reported failures (P3, P4, P13), the documented
papers/aria-chess-paper/paper/sections/02_method.tex:41:(P4, C$\times$P), and
papers/aria-chess-paper/paper/sections/02_method.tex:49:\to (\text{script}, \text{seed range}, \text{dataset/source},
papers/aria-chess-paper/paper/sections/02_method.tex:61:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:63:P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:66:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
papers/aria-chess-paper/paper/sections/02_method.tex:89:the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
papers/aria-chess-paper/paper/sections/02_method.tex:95:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
papers/aria-chess-paper/paper/sections/02_method.tex:112:computational tractability; full-cohort $n=1003$ statistics
papers/aria-chess-paper/paper/sections/02_method.tex:128:\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
papers/aria-chess-paper/paper/sections/02_method.tex:138:\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
papers/aria-chess-paper/paper/sections/02_method.tex:140:preregistered cascade-$\alpha$ tests, 2000 resamples for the
papers/aria-chess-paper/paper/sections/02_method.tex:141:$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
papers/aria-chess-paper/paper/sections/02_method.tex:145:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
papers/aria-chess-paper/paper/sections/02_method.tex:146:$0/2000$ were below the preregistered floor $+0.10$; we report these
papers/aria-chess-paper/paper/sections/02_method.tex:154:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
papers/aria-chess-paper/paper/sections/02_method.tex:155:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
papers/aria-chess-paper/paper/sections/02_method.tex:161:on the full $n=1003$ subject distribution.
papers/aria-chess-paper/paper/sections/02_method.tex:174:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
papers/aria-chess-paper/paper/sections/02_method.tex:186:\item Six drug/sleep signatures:
papers/aria-chess-paper/paper/sections/02_method.tex:187:  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
papers/aria-chess-paper/paper/sections/02_method.tex:197:All scripts are deterministic given seeds. Reruns at seed $42$ on the
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:8:$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:15:confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:25:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:26:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:28:Per-seed paired estimates use the same formula on a single seed's
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:45:$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:46:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:53:($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:60:\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:61:$32000$--$32019$, non-overlapping with original validation seeds in
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:64:seed $42$. Wallclock $1706$\,s on a single CPU
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:72:\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:76:condition & mean $\alpha$ & std & sem \\
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:87:$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:88:$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:95:Bootstrap on the 20-seed sample (2000 resamples):
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:97:\item bootstrap mean $\Delta_{CP} = +0.190$;
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:98:\item 95\% bootstrap CI $[+0.143, +0.239]$;
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:105:\textbf{Per-seed paired distribution.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:106:$19/20$ seeds give a positive paired-interaction estimate (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:107:$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:117:\textbf{Architectural reading (substrate witness).} $C$ creates churn
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:127:architectural claim from the original 3-seed validation that held $C$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:132:(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:133:selected to be non-overlapping with the original $30000$s seeds.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:135:(i) a second independent $N\!=\!20$ run at a different seed range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:137:(ii) an $N\!=\!50$ characterisation of the per-seed sample
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:145:  $C\times P$ coupling among regular 4-polytopes.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:146:\item It does not establish an $\eta$-trajectory derivation; $\eta$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:161:The original 3-seed preregistered validation gave estimates consistent
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:165:per-seed variance, budget the seed count from a power-analysis
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:166:assumption that the per-seed std could be as large as the interaction
papers/aria-chess-paper/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-chess-paper/paper/sections/09_limitations.tex:15:other regular 4-polytopes ($24$-cell, $120$-cell) would produce
papers/aria-chess-paper/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
papers/aria-chess-paper/paper/sections/09_limitations.tex:22:$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
papers/aria-chess-paper/paper/sections/09_limitations.tex:26:\textbf{Single-seed determinism on the recurrent layer.} The v4
papers/aria-chess-paper/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
papers/aria-chess-paper/paper/sections/09_limitations.tex:28:a single deterministic trajectory at seed $42$. Empirical CIs across
papers/aria-chess-paper/paper/sections/09_limitations.tex:29:$10$--$20$ cross-seed runs would strengthen the per-signature claims
papers/aria-chess-paper/paper/sections/09_limitations.tex:31:WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
papers/aria-chess-paper/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
papers/aria-chess-paper/paper/sections/09_limitations.tex:34:overlap with two independent reference $\alpha$ ranges.
papers/aria-chess-paper/paper/sections/09_limitations.tex:35:\emph{Strengthening build:} 10--20 cross-seed runs of
papers/aria-chess-paper/paper/sections/09_limitations.tex:36:\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
papers/aria-chess-paper/paper/sections/09_limitations.tex:59:observables.} While the construction of $\Rsixhundred$ is theorem-
papers/aria-chess-paper/paper/sections/09_limitations.tex:61:polytope as the consciousness-substrate instance is motivated by the
papers/aria-chess-paper/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
papers/aria-chess-paper/paper/sections/09_limitations.tex:65:preregistered correspondences plus six signatures; the H$_4$
papers/aria-chess-paper/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-chess-paper/paper/sections/09_limitations.tex:95:\textbf{The recurrent layer is a method, not a metaphysics claim.}
papers/aria-chess-paper/paper/sections/09_limitations.tex:96:We do not claim the recurrent self-model layer ``is'' consciousness;
papers/aria-chess-paper/paper/sections/09_limitations.tex:97:we claim quantitative consistency with six published biological
papers/aria-chess-paper/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
papers/aria-chess-paper/paper/sections/09_limitations.tex:113:do not claim ``cortex has drifted from an ideal polytope''; we
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
papers/aria-chess-paper/paper/sections/09_limitations.tex:173:  4-polytopes — see~\S\ref{ssec:regime}.
papers/aria-chess-paper/paper/sections/09_limitations.tex:175:  of the six signatures.
papers/aria-chess-paper/paper/sections/09_limitations.tex:187:The result is a substrate witness: a geometry-fixed substrate, with
papers/aria-chess-paper/paper/sections/09_limitations.tex:189:eighteen preregistered correspondences and six companion drug/sleep
papers/aria-chess-paper/paper/sections/09_limitations.tex:192:not claim the substrate \emph{is} consciousness. We do not claim a
papers/aria-chess-paper/paper/sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
papers/aria-chess-paper/paper/sections/09_limitations.tex:194:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
papers/aria-chess-paper/paper/sections/08_discussion.tex:6:theories of consciousness, identifies what is novel here that is not
papers/aria-chess-paper/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
papers/aria-chess-paper/paper/sections/08_discussion.tex:11:not claim the recurrent layer ``is'' consciousness.
papers/aria-chess-paper/paper/sections/08_discussion.tex:15:Three things are claimed novel as a substrate witness:
papers/aria-chess-paper/paper/sections/08_discussion.tex:23:  shape parameter is tuned to neural data); cascade-$\alpha$ matches
papers/aria-chess-paper/paper/sections/08_discussion.tex:25:  on three reference ranges; six drug/sleep signatures pass at
papers/aria-chess-paper/paper/sections/08_discussion.tex:34:  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
papers/aria-chess-paper/paper/sections/08_discussion.tex:38:  original 3-seed validation.
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:42:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
papers/aria-chess-paper/paper/sections/08_discussion.tex:48:\subsection{Comparison to existing theories of consciousness}
papers/aria-chess-paper/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
papers/aria-chess-paper/paper/sections/08_discussion.tex:71:The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
papers/aria-chess-paper/paper/sections/08_discussion.tex:74:Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
papers/aria-chess-paper/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:119:\emph{substrate witness} for the family that ACT names; ACT is not the
papers/aria-chess-paper/paper/sections/08_discussion.tex:142:\emph{a hypothesis the substrate witness raises}, not as a proof.
papers/aria-chess-paper/paper/sections/08_discussion.tex:143:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
papers/aria-chess-paper/paper/sections/08_discussion.tex:153:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
papers/aria-chess-paper/paper/sections/08_discussion.tex:156:  system with unknown per-seed variance, budget for at least this
papers/aria-chess-paper/paper/sections/08_discussion.tex:158:  taken as universal. The original 3-seed plan was the source of two
papers/aria-chess-paper/paper/sections/08_discussion.tex:166:  an explicit reset/equilibration discipline}, not just seed.
papers/aria-chess-paper/paper/sections/08_discussion.tex:188:\subsection{Open questions raised by the substrate witness}
papers/aria-chess-paper/paper/sections/08_discussion.tex:191:\item Do the six drug/sleep signatures replicate across $10$--$20$
papers/aria-chess-paper/paper/sections/08_discussion.tex:192:  cross-seed runs of the recurrent layer? (Single-seed disclosure;
papers/aria-chess-paper/paper/sections/08_discussion.tex:194:\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
papers/aria-chess-paper/paper/sections/08_discussion.tex:198:  independent fresh-seed $N\!=\!20$ replication at a different seed
papers/aria-chess-paper/paper/sections/01_introduction.tex:5:Theories of consciousness divide into mechanism-driven proposals
papers/aria-chess-paper/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
papers/aria-chess-paper/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
papers/aria-chess-paper/paper/sections/01_introduction.tex:28:single condition-dependent self-injection coupling $\eta$ and a
papers/aria-chess-paper/paper/sections/01_introduction.tex:30:against eighteen preregistered correspondences plus six companion
papers/aria-chess-paper/paper/sections/01_introduction.tex:31:drug/sleep EEG signatures.
papers/aria-chess-paper/paper/sections/01_introduction.tex:35:We claim a single \emph{substrate witness}: that a geometry-fixed
papers/aria-chess-paper/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
papers/aria-chess-paper/paper/sections/01_introduction.tex:42:\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:58:\item \textbf{Six drug/sleep signatures.} On a single deterministic
papers/aria-chess-paper/paper/sections/01_introduction.tex:59:  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:63:  recovery deterministically identical to wake; wake cascade-$\alpha$
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:71:  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
papers/aria-chess-paper/paper/sections/01_introduction.tex:72:  conversation $-4.4$pp lift, within preregistered neutrality bounds)
papers/aria-chess-paper/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
papers/aria-chess-paper/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
papers/aria-chess-paper/paper/sections/01_introduction.tex:85:  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
papers/aria-chess-paper/paper/sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
papers/aria-chess-paper/paper/sections/01_introduction.tex:91:  establish that the substrate \emph{is} consciousness, nor that
papers/aria-chess-paper/paper/sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
papers/aria-chess-paper/paper/sections/01_introduction.tex:127:We never write `the substrate \emph{is} cortex' or `derives consciousness'.
papers/aria-chess-paper/paper/sections/01_introduction.tex:130:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:135:polytope'. The claim-boundary rule is summarised in the box below
papers/aria-chess-paper/paper/sections/01_introduction.tex:142:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
papers/aria-chess-paper/paper/sections/01_introduction.tex:144:parameter $\eta$ and one graph-pinned nonlinearity, against published
papers/aria-chess-paper/paper/sections/01_introduction.tex:146:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
papers/aria-chess-paper/paper/sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
papers/aria-chess-paper/paper/sections/01_introduction.tex:156:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
papers/aria-chess-paper/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
papers/aria-chess-paper/paper/sections/01_introduction.tex:161:\S\ref{sec:results} reports the empirical tables: six drug/sleep
papers/aria-chess-paper/paper/sections/01_introduction.tex:163:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
papers/aria-chess-paper/paper/sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
papers/aria-chess-paper/paper/sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
papers/aria-chess-paper/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
papers/aria-chess-paper/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
papers/aria-chess-paper/paper/sections/10_conclusion.tex:10:drug/sleep EEG signatures of conscious vs unconscious states. Once
papers/aria-chess-paper/paper/sections/10_conclusion.tex:15:$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
papers/aria-chess-paper/paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
papers/aria-chess-paper/paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass against their literature-derived
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:25:propofol continuity drop $+0.066$; propofol integrated-information
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:31:$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:42:failure; the closure of the three gaps (P3, P4, P13) is documented
papers/aria-chess-paper/paper/sections/10_conclusion.tex:49:strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
papers/aria-chess-paper/paper/sections/10_conclusion.tex:52:the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
papers/aria-chess-paper/paper/sections/10_conclusion.tex:54:high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
papers/aria-chess-paper/paper/sections/10_conclusion.tex:61:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
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
papers/aria-chess-paper/paper/sections/10_conclusion.tex:81:signatures, alternative-polytope ablations, an independent $N\!=\!20$
papers/aria-chess-paper/paper/sections/10_conclusion.tex:82:C$\times$P replication at a different seed range, cross-parcellation
papers/aria-chess-paper/paper/sections/10_conclusion.tex:91:gathered here is the substrate witness; the broader programme to
papers/aria-chess-paper/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
papers/aria-chess-paper/paper/sections/03_substrate.tex:118:$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
papers/aria-chess-paper/paper/sections/03_substrate.tex:155:cascade is a decomposition of operators on $\Rsixhundred$, and the
papers/aria-chess-paper/paper/sections/03_substrate.tex:156:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
papers/aria-chess-paper/paper/sections/03_substrate.tex:162:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
papers/aria-chess-paper/paper/sections/03_substrate.tex:168:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
papers/aria-chess-paper/paper/sections/03_substrate.tex:171:  ablation against alternative regular 4-polytopes is an open build
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:11:coupling $\eta$, and four trajectory observables. No shape parameter
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:14:This section is method, not metaphysics. We do not claim the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:15:recurrent layer ``is'' consciousness; we report which numerical
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:26:\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:30:with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:39:\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:41:\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:52:gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:53:avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:56:\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:58:geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:59:at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:104:\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:108:drop $+0.066$).
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:125:$\times$ $800$ ticks each at seed $42$:
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:127:\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:131:that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:141:\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:142:$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:169:(coupling $0.05$) cross-orbit pressure averaging that prevents
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:194:($D$ at $0.05$, $P$ at $30\%$ scale saturating at pressure $3.0$,
papers/aria-chess-paper/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
papers/aria-chess-paper/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:9:gives the three-way $\alpha$ overlap. We lift the result map
papers/aria-chess-paper/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:18:\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
papers/aria-chess-paper/paper/sections/05_results.tex:21:$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
papers/aria-chess-paper/paper/sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
papers/aria-chess-paper/paper/sections/05_results.tex:28:seed 42).}
papers/aria-chess-paper/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
papers/aria-chess-paper/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:45:\caption{Six drug/sleep signatures with literature references.}
papers/aria-chess-paper/paper/sections/05_results.tex:46:\label{tab:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:66:6 & Wake cortical-avalanche $\alpha$ &
papers/aria-chess-paper/paper/sections/05_results.tex:68:   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
papers/aria-chess-paper/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:76:on the same deterministic substrate trajectory. The six signatures
papers/aria-chess-paper/paper/sections/05_results.tex:77:are not part of the dated 2026-04-18 P1--P18 preregistration; their
papers/aria-chess-paper/paper/sections/05_results.tex:79:wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
papers/aria-chess-paper/paper/sections/05_results.tex:87:load-bearing for the headline claim. Single-seed disclosure:
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:101:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
papers/aria-chess-paper/paper/sections/05_results.tex:107:P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:109:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:111:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:113:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:115:P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:121:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:122:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:134:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
papers/aria-chess-paper/paper/sections/05_results.tex:142:  $N\!=\!3$ on a high-per-seed-variance interaction term.
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:145:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
papers/aria-chess-paper/paper/sections/05_results.tex:146:  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:152:  without state reset on a state-drifted substrate, and $+40.6$pp
papers/aria-chess-paper/paper/sections/05_results.tex:166:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:168:The substrate's wake cascade-$\alpha$ confidence interval overlaps
papers/aria-chess-paper/paper/sections/05_results.tex:174:\caption{Three-way $\alpha$ overlap on the wake cascade-event power
papers/aria-chess-paper/paper/sections/05_results.tex:176:\label{tab:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:179:Source & $\alpha$ & 95\% CI & $n$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:181:ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
papers/aria-chess-paper/paper/sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
papers/aria-chess-paper/paper/sections/05_results.tex:193:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
papers/aria-chess-paper/paper/sections/05_results.tex:201:$k=12$ is pinned to the substrate's average degree
papers/aria-chess-paper/paper/sections/05_results.tex:208:with event-bootstrap; cross-seed CI is an open build).
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:29:\textbf{Critical methodological detail.} Between successive depth
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:45:$5$    & $53.1\%$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:47:$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:74:$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:77:and P16 (conversation null); both pass. The 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:87:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:90:reset; we report the LOO finding ($+40.6$pp) above as a disclosed
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:95:4-category classification from raw $53.1\%$ (just above $25\%$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:96:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
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
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:172:$n=1003$ descriptive statistics.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:198:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:202:\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:232:\item We do not claim cortex has ``drifted from an ideal polytope'';
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:258:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,

exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex' | sed -n '1,90p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/06_stress_tests.tex' | sed -n '1,175p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/07_cross_domain.tex' | sed -n '1,280p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/09_limitations.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'papers/aria-chess-paper/paper/sections/10_conclusion.tex' | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 381ms:
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

 succeeded in 361ms:
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

 succeeded in 428ms:
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

 succeeded in 436ms:
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

 succeeded in 423ms:
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

codex
The aria-chess inheritance checks line up with its own text: the 17/18 then 18/18 accounting, single-seed EEG disclosure, condition-dependent `eta`, `k=12`, and no-uniqueness/no-selection boundaries are present in the companion. I’m now consolidating this into the requested referee sections and separating must-fix issues from wording improvements.
exec
/bin/bash -lc "rg -n \"historically|blind|look|data was looked|geometry|variant|pure-geometry|LHCb\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_kernel.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg --files '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/CHANGELOG.md' | sed -n '35,85p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba 'docs/aria-closure-kernel.md' | sed -n '70,170p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 264ms:
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

 succeeded in 277ms:
    35	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five independent
    36	datasets covering two collaborations, two isospin partners, and three
    37	decay channels. Only one dimensionless amplitude $A$ is fitted per
    38	dataset.
    39	
    40	What the data shows under non-linear evaluation:
    41	- **Universality.** Same fixed kernel, all five datasets, one
    42	  amplitude per dataset — no shape retuning.
    43	- **Sign uniformity.** $A>0$ in $5/5$ fits and
    44	  $\Delta C_{9}^{\mathrm{eff}}<0$ in $5/5$ fits.
    45	- **Cross-channel ratio.** $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
    46	  amplitudes consistent with the predicted Krüger--Matias
    47	  basis-correction factor $\sim 2.2$, residual $\sim 50\%$ overshoot.
    48	- **Geometry-first variant test.** Of three discrete Laplacian
    49	  variants, the unweighted choice wins on a pure-geometry criterion
    50	  (correlation $0.997$ with the continuum kernel) decided
    51	  independently of LHCb input. The same variant later wins on the
    52	  data $\chi^{2}$.
    53	
    54	### Statistical caveat
    55	On Akaike model comparison vs a constant Wilson-coefficient shift
    56	$\mathrm{FREE\_C9}$ (both at $k=1$), the per-dataset
    57	$\Delta\mathrm{AIC}$ values span $[-0.24, +1.09]$ around zero;
    58	stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs
    59	$w_{\mathrm{FREE\_C9}}=0.652$. On current data the two models are
    60	statistically indistinguishable on AIC — a question current data
    61	cannot resolve and which will require future $b\to s\ell\ell$
    62	measurements.
    63	
    64	### Linearisation diagnostic (methodological correction during this release)
    65	An earlier linearised analysis (Mode B, linear in $\Delta C_{9}$ via
    66	central-difference slopes) had given $\Delta\mathrm{AIC} = -1.67$ in
    67	favour of the kernel on LHCb 2025. The non-linear refit using
    68	`flavio.np_prediction` directly gives $\Delta\mathrm{AIC} = +1.09$ on
    69	the same dataset — a $+2.77$ AIC-unit drift. The per-bin
    70	linearisation residual reaches $4.3\sigma$ at the linearised best-fit
    71	$\Delta C_{9}=-1.34$, well outside the linear regime. The non-linear
    72	numbers are the headline; the linearised numbers are retained in the
    73	paper only as a methodology diagnostic.
    74	
    75	### Changed
    76	- Paper headline reframed from "kernel beats $\mathrm{FREE\_C9}$ on
    77	  AIC" (linearised) to "fixed geometry-derived kernel describes the
    78	  anomaly across five datasets, AIC-tied with $\mathrm{FREE\_C9}$"
    79	  (non-linear).
    80	
    81	---
    82	
    83	## [0.1.0] — 2026-04-28 — Linearised cross-dataset and cross-channel test
    84	
    85	### Added

 succeeded in 336ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex

 exited 2 in 350ms:
rg: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_kernel.tex: No such file or directory (os error 2)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:29:\item \textbf{Variant choice is geometry-confirmed but data-discovered.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:31:  the best LHCb-data $\chi^{2}$ among the three admissible variants
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:32:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:33:  We subsequently verified that the same variant wins on a pure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:34:  geometry criterion (correlation with the Layer-1 continuum kernel,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:35:  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:36:  this basis. The variant choice therefore does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38:  data was looked at first is acknowledged.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:45:  the relevant level on the joint LHCb 2025 fit; the broader
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:51:  2I-equivariant graph but is not derived from a first-principles
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:59:  \delta_{1}^{\mathsf T}\delta_{1}$ with 2I-equivariant boundary maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:69:  the full LHCb covariance, because resampling with replacement
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:86:  inter-observable correlation matrix for the LHCb 2015
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:95:  prediction has theoretical uncertainty larger than the LHCb stat
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:113:  LHCb publication chose the $S$-basis, not the amplified $P$-basis.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:127:  relevant LHCb (1209.4284, 1403.8045, 1804.07167) and CMS PRD 2018
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:143:The geometry-derived kernel describes the angular anomaly with one
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:149:\emph{a single geometry-derived $q^{2}$-shape with no fitted shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:14:analysis on LHCb 2025 (\S\ref{subsec:joint_fit}) gives different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:48:the LHCb 2025 four-observable joint fit, $N=500$ trials. Sign-stable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:71:\caption{Region-split fits on the LHCb 2025 four-observable joint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:103:\caption{Joint-fit comparison on LHCb 2025 four observables.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:185:\caption{Stress-test acceptance summary on the LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:21:LHCb 2015         & $B^{0}\to K^{*0}\mu\mu$  & 1512.04442 & ins1409497 & 3   & 8 (Table 4 P-basis) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:22:LHCb 2021         & $B^{+}\to K^{*+}\mu\mu$  & 2012.13241 & ins1838196 & 9   & 8 exclusive \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:24:LHCb 2025 (ref)   & $B^{0}\to K^{*0}\mu\mu$  & 2512.18053 & ins3094698 & 8.4 & 8 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:31:LHCb 2021 publishes 10 $q^{2}$ bins of which two are wide combined
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:40:$P_{5}', P_{4}', P_{1}, P_{2}$, matching the LHCb 2025 reference fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:55:LHCb 2015                     & 32 & 30.69 & $-1.08$ & 30.45 & $\boldsymbol{+1.24}$ & $-0.96$ & $-0.24$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:56:LHCb 2021 ($B^{+}\to K^{*+}$) & 32 & 22.77 & $-1.82$ & 22.93 & $\boldsymbol{+2.06}$ & $-1.59$ & $+0.17$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:58:LHCb 2025 (ref)               & 32 & 40.89 & $-1.00$ & 41.98 & $\boldsymbol{+1.14}$ & $-0.86$ & $+1.09$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:64:At equal $k=1$ the kernel is favoured on $2/5$ fits (LHCb 2015 and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:66:on $3/5$ (LHCb 2021, CMS 2025 no-$P_{4}'$, LHCb 2025; max
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:83:$A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:110:LHCb 2015                  & $-0.241$ & $0.470$ & $0.530$ & VFD (marginal) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:111:LHCb 2021 ($K^{*+}$)       & $+0.168$ & $0.521$ & $0.479$ & FREE\_C9 (marginal) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:113:LHCb 2025                  & $+1.093$ & $0.633$ & $0.367$ & FREE\_C9 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:196:The same geometry-derived kernel, with one fitted amplitude per
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:199:(LHCb, CMS), two isospin partners ($B^{0}\!\to\!K^{*0}$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:10:geometry-derived kernel imposes a fixed centre-peaked $q^{2}$ shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:15:profile and FREE\_C9's flat profile compress the four LHCb 2025
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:44:Empirically the per-bin linearisation residual on LHCb 2025 reaches
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:57:operator $L_{V_{600}} + \varphi^{-2}I$ to the 2I-equivariant cocycle
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:66:Table~\ref{tab:variant_selection}); the unweighted Laplacian wins on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:67:both the pure-geometry and LHCb-data criteria, with the rankings
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:103:\item \emph{The kernel is the right object.} The 2I-equivariant graph
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:123:alternative explanations of the LHCb 2025 result:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:8:2I-equivariant graph realisation on the 600-cell $V_{600}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:11:kernel; the continuum and bounded variants are reported as theoretical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:62:(\ref{eq:dirichlet_mode}) fit the LHCb 2025 $P_{5}'$ data at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:70:\subsection{Layer 3 — discrete 2I-equivariant lift on $V_{600}$}\label{subsec:layer3}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:130:\eqref{eq:kappa_lift} on the LHCb 2025 bin centres is $r=0.997$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:133:together with the continuum exponential and the LHCb 2025 bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:139:\caption{The geometry-derived response kernel $\kappa(q^{2})$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:140:plotted over the LHCb $q^{2}$ window. Solid blue: the discrete
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:144:to the discrete shell-mean on the LHCb bin centres (red points).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:151:\paragraph{Cocycle, edge weighting, and variant selection.} The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:160:for each variant; the shell-mean profile is then compared to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:161:continuum kernel $e^{-|x|/\varphi}$ and to the LHCb 2025 $P_{5}'$ data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:162:on the LHCb bin grid. Two criteria are used: a \emph{pure-geometry}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:164:continuum kernel, no LHCb data involvement), and a \emph{data}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:165:criterion ($\chi^{2}$ against the LHCb 2025 single-observable fit).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:172:variant & $\mathrm{corr}(\overline{\psi}, e^{-|x|/\varphi})$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:173:        $\chi^{2}$ vs LHCb 2025 $P_{5}'$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:182:pure-geometry criterion (correlation with the Layer-1 continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:183:kernel) and the LHCb-data criterion. The two rankings agree, so the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:184:variant choice is consistent with selection on geometric grounds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:185:independent of the data; the LHCb data only confirms it.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:186:Reproducible from \texttt{scripts/wo016b\_variant\_geometry.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:187:(reports/wo016b\_variant\_geometry.csv).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:188:\label{tab:variant_selection}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:192:two-criterion agreement means the variant choice does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:193:extra effective fit parameter: the variant choice would have been the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:197:\S\ref{sec:limitations}: the data was looked at first, and only later
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:198:verified to agree with the pure-geometry ranking.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:215:(Eq.~\ref{eq:Lphi}), and the variant table
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:216:(Table~\ref{tab:variant_selection}). A reader unfamiliar with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:221:with 2I-equivariant boundary maps from the 1200 triangular faces,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:6:$\kappa(q^{2})$ from a finite 2I-equivariant graph (the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:21:\item \textbf{LHCb 2025, four-observable joint fit (non-linear):}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:42:\item \textbf{Linearisation drift:} on LHCb 2025 the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:49:  pure-geometry-confirmed discrete variant choice
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:50:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:57:  any luminosity, any energy) gives $A<0$ on the geometry-derived kernel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:70:$\Delta\mathrm{AIC}_{\mathrm{VFD\,vs\,FREE\_C9}}\geq 0$ on the LHCb
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:78:This is a structural test of whether a single fixed, geometry-derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:86:factor; and the unweighted Laplacian variant is selected by a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:87:pure-geometry criterion (correlation $0.997$ with the continuum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:88:kernel) decided independently of any LHCb input. \emph{What the data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:29:\item \textbf{Variant choice is geometry-confirmed but data-discovered.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:31:  the best LHCb-data $\chi^{2}$ among the three admissible variants
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:32:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:33:  We subsequently verified that the same variant wins on a pure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:34:  geometry criterion (correlation with the Layer-1 continuum kernel,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:35:  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:36:  this basis. The variant choice therefore does not consume an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38:  data was looked at first is acknowledged.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:45:  the relevant level on the joint LHCb 2025 fit; the broader
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:51:  2I-equivariant graph but is not derived from a first-principles
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:59:  \delta_{1}^{\mathsf T}\delta_{1}$ with 2I-equivariant boundary maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:69:  the full LHCb covariance, because resampling with replacement
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:86:  inter-observable correlation matrix for the LHCb 2015
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:95:  prediction has theoretical uncertainty larger than the LHCb stat
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:113:  LHCb publication chose the $S$-basis, not the amplified $P$-basis.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:127:  relevant LHCb (1209.4284, 1403.8045, 1804.07167) and CMS PRD 2018
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:143:The geometry-derived kernel describes the angular anomaly with one
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:149:\emph{a single geometry-derived $q^{2}$-shape with no fitted shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:6:angular analysis of LHCb 2015 \citep{LHCb2015Bsphimumu,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:7:LHCb2015BsphiHEPData}, the same flavour transition $b\to s\mu\mu$ but
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:12:LHCb 2015 publishes Table 2: $F_{L}, S_{3}, S_{4}, S_{7}$ on 8 $q^{2}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:36:\caption{$B_{s}\to\phi\mu\mu$ non-linear frozen-kernel fit on LHCb 2015,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:121:LHCb 2015 \citep{LHCb2015Bsphimumu} publishes only the $S$-basis for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:125:$P$-basis (where LHCb 2025, CMS 2025, LHCb 2015, LHCb 2021 all
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:138:$B\to K^{*}$ (above). Using the non-linear LHCb 2025 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:139:$A_{P}^{\mathrm{LHCb\,2025}} = +1.14$ as the reference $P$-basis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:194:probed for HEPData submissions covering the LHCb and CMS $B^{+}\to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:201:ins1486676 \citep{LHCb2016Kst0214030HEPData} is available but reports
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:10:\item \textbf{LHCb 2025} — $B^{0}\!\to\!K^{*0}\mu^{+}\mu^{-}$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:11:  $8.4\,\mathrm{fb}^{-1}$ \citep{LHCb2025BKstmumuComp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:12:  LHCb2025BKstmumuHEPData}; 8 exclusive $q^{2}$ bins; full statistical,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:18:\item \textbf{LHCb 2015} — $B^{0}\!\to\!K^{*0}\mu^{+}\mu^{-}$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:19:  $3\,\mathrm{fb}^{-1}$ \citep{LHCb2015BKstmumu, LHCb2015HEPData};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:23:\item \textbf{LHCb 2021} (charged isospin partner) —
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:25:  \citep{LHCb2021BKstpmumu, LHCb2021HEPData}; \texttt{data2.yaml} gives
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:34:\item \textbf{LHCb 2015 $B_{s}\!\to\!\phi\mu^{+}\mu^{-}$} (cross-channel)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:35:  \citep{LHCb2015Bsphimumu, LHCb2015BsphiHEPData}; Table 2 gives
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:91:quantifies the non-linearity. On the LHCb 2025 joint fit the per-bin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:109:best-fit on the LHCb 2025 4-observable joint fit is $-1.00$, lower
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:133:\item $\mathrm{VFD\_GREEN\_600CELL}$ — the geometry-derived kernel of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:2:\section{Results on LHCb 2025}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:5:This section reports the kernel fit on the LHCb 2025 dataset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:6:\citep{LHCb2025BKstmumuComp,LHCb2025BKstmumuHEPData}, both on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:15:LHCb $32{\times}32$ correlation matrix:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:34:\caption{Headline non-linear joint fit on the four LHCb 2025 angular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:38:$\approx 1.7$). The geometry-derived kernel produces a comparable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:48:on the LHCb 2025 four-observable joint fit, evaluated under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:11:\citep{Descotes2013P5p,AltmannshoferStraub2013}. The most recent LHCb
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:12:comprehensive analysis \citep{LHCb2025BKstmumuComp,LHCb2025BKstmumuHEPData}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:34:of a finite 2I-equivariant graph (the 600-cell $V_{600}$, vertices and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:75:\item On the LHCb 2025 dataset, the geometry-derived kernel and a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:79:\item Across five fits — LHCb 2015 (3\,fb$^{-1}$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:80:  $B^{0}\!\to\! K^{*0}$), LHCb 2021 (9\,fb$^{-1}$, $B^{+}\!\to\!K^{*+}$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:82:  LHCb 2025 (8.4\,fb$^{-1}$), and the cross-channel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:93:  effect (the 2015 LHCb publication uses the CP-averaged $S_{i}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:106:  prefers the kernel because of the geometry, or because the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:107:  geometry reproduces a centre-peaked shape, is not decided here.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:109:  submissions for the LHCb and CMS analyses
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:110:  (LHCb 1209.4284, 1403.8045, 1804.07167; CMS PRD 2018) are not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:114:The surviving structural claim is: \emph{one geometry-derived

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex' | sed -n '24,42p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex' | sed -n '151,200p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex' | sed -n '50,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016d_nonlinear_xdataset.md' | sed -n '1,60p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md' | sed -n '1,100p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 383ms:
    24	  This paper now uses non-linear \texttt{flavio.np\_prediction}
    25	  evaluation throughout for the headline numbers; Mode-B values are
    26	  retained only as a methodology diagnostic. Future analyses on this
    27	  anomaly should not use a linearised Taylor expansion.
    28	
    29	\item \textbf{Variant choice is geometry-confirmed but data-discovered.}
    30	  The unweighted Laplacian was originally selected because it gave
    31	  the best LHCb-data $\chi^{2}$ among the three admissible variants
    32	  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
    33	  We subsequently verified that the same variant wins on a pure
    34	  geometry criterion (correlation with the Layer-1 continuum kernel,
    35	  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
    36	  this basis. The variant choice therefore does not consume an
    37	  effective fit parameter, but the historical contingency that the
    38	  data was looked at first is acknowledged.
    39	
    40	\item \textbf{Single Wilson coefficient.} We compare against
    41	  $\mathrm{FREE\_C9}$ and $\mathrm{FREE\_C9 + FREE\_C10}$ but do not
    42	  test against the wider Wilson-coefficient space ($C_{9}'$, $C_{10}'$,

 succeeded in 366ms:
    50	\toprule
    51	dataset & $n$ & FREE $\chi^{2}$ & FREE $\Delta C_{9}$ &
    52	        VFD $\chi^{2}$ & \textbf{VFD $A$} & VFD $\Delta C_{9}^{\mathrm{eff}}$ &
    53	        $\Delta\mathrm{AIC}$ \\
    54	\midrule
    55	LHCb 2015                     & 32 & 30.69 & $-1.08$ & 30.45 & $\boldsymbol{+1.24}$ & $-0.96$ & $-0.24$ \\
    56	LHCb 2021 ($B^{+}\to K^{*+}$) & 32 & 22.77 & $-1.82$ & 22.93 & $\boldsymbol{+2.06}$ & $-1.59$ & $+0.17$ \\
    57	CMS 2025 (no $P_{4}'$)        & 18 & 43.73 & $-0.95$ & 44.21 & $\boldsymbol{+1.05}$ & $-0.81$ & $+0.47$ \\
    58	LHCb 2025 (ref)               & 32 & 40.89 & $-1.00$ & 41.98 & $\boldsymbol{+1.14}$ & $-0.86$ & $+1.09$ \\
    59	\midrule
    60	$B_{s}\!\to\!\phi$ 2015        & 24 & 13.20 & $-4.12$ & 12.96 & $\boldsymbol{+4.98}$ & $-3.85$ & $-0.24$ \\
    61	\bottomrule
    62	\end{tabular}
    63	\caption{Headline non-linear cross-dataset and cross-channel results.
    64	At equal $k=1$ the kernel is favoured on $2/5$ fits (LHCb 2015 and
    65	$B_{s}\!\to\!\phi$, both by $\Delta\mathrm{AIC}=-0.24$) and disfavoured
    66	on $3/5$ (LHCb 2021, CMS 2025 no-$P_{4}'$, LHCb 2025; max
    67	$\Delta\mathrm{AIC}=+1.09$). $A>0$ in every fit;
    68	$\Delta C_{9}^{\mathrm{eff}}<0$ in every fit. Reproducible from
    69	\texttt{scripts/wo016d\_nonlinear\_xdataset.py}
    70	(reports/wo016d\_nonlinear\_xdataset.csv).}
    71	\label{tab:cross_dataset_main}
    72	\end{table}
    73	
    74	\begin{figure}[h]
    75	\centering
    76	\includegraphics[width=0.95\textwidth]{fig_F3_cross_dataset_A.pdf}
    77	\caption{Non-linear best-fit amplitudes $A$ across the five fits.
    78	Left: the four $P$-basis $B\to K^{*}\mu\mu$ fits, range
    79	$A\in[+1.05,+2.06]$, factor-of-$\sim 2$ scatter across two
    80	collaborations and two isospin partners. Right: the $S$-basis
    81	$B_{s}\!\to\!\phi$ fit, $A=+4.98$. The grey dashed line marks the
    82	$P\!\to\!S$ basis-corrected prediction
    83	$A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$;
    84	the observed $S$-basis amplitude exceeds this by a factor of $\sim 2$
    85	(see \S\ref{sec:cross-channel}). Bars are coloured green where the
    86	non-linear $\Delta\mathrm{AIC}$ marginally favours VFD and orange
    87	where it marginally favours $\mathrm{FREE\_C9}$. Reproducible from
    88	\texttt{scripts/wo017\_paper\_figures.py}.}
    89	\label{fig:F3_cross_dataset_A}
    90	\end{figure}
    91	
    92	\subsection{Akaike-weight stack across the five fits}
    93	
    94	To convert the per-dataset $\Delta\mathrm{AIC}$ values into a single
    95	combined statement we compute the Akaike weight of each model on each
    96	dataset, $w_{M,d} = e^{-\Delta\mathrm{AIC}_{M,d}/2} / \sum_{M'}
    97	e^{-\Delta\mathrm{AIC}_{M',d}/2}$, and stack across datasets under the
    98	independence assumption (none of the five datasets shares
    99	observation-level information; theory inputs are shared via
   100	\texttt{flavio} but enter both arms identically).
   101	
   102	\begin{table}[h]
   103	\centering
   104	\small
   105	\begin{tabular}{lcccc}
   106	\toprule
   107	dataset & non-linear $\Delta\mathrm{AIC}$ &
   108	          $w(\mathrm{FREE\_C9})$ & $w(\mathrm{VFD})$ & favoured \\
   109	\midrule
   110	LHCb 2015                  & $-0.241$ & $0.470$ & $0.530$ & VFD (marginal) \\
   111	LHCb 2021 ($K^{*+}$)       & $+0.168$ & $0.521$ & $0.479$ & FREE\_C9 (marginal) \\
   112	CMS 2025 no-$P_{4}'$       & $+0.473$ & $0.559$ & $0.441$ & FREE\_C9 (marginal) \\
   113	LHCb 2025                  & $+1.093$ & $0.633$ & $0.367$ & FREE\_C9 \\
   114	$B_{s}\!\to\!\phi$ 2015    & $-0.240$ & $0.470$ & $0.530$ & VFD (marginal) \\
   115	\midrule
   116	\textbf{stacked}            & $\sum=+1.253$ &
   117	\textbf{0.652} & \textbf{0.348} & \textbf{FREE\_C9 (mild)} \\
   118	\bottomrule
   119	\end{tabular}
   120	\caption{Per-dataset Akaike weights and stacked total. The

 succeeded in 377ms:
   151	\paragraph{Cocycle, edge weighting, and variant selection.} The
   152	framework's pentagonal cocycle
   153	$\kappa(v) = (s(v)-s_{\mathrm{mid}})^{2}\in\{0,1,4,9,16\}$ provides a
   154	vertex potential $\omega_{+}=\varphi^{\kappa(v)}$. Three discrete
   155	edge-weighting schemes are admissible: unweighted ($w_{vw}=1$),
   156	$\varphi$-cocycle geometric mean
   157	($w_{vw}=\sqrt{\omega_{+}(v)\,\omega_{+}(w)}$), and $\varphi$-cocycle
   158	arithmetic mean ($w_{vw}=\tfrac{1}{2}[\omega_{+}(v)+\omega_{+}(w)]$).
   159	The discrete Green's response Eq.~\eqref{eq:psi_discrete} is computed
   160	for each variant; the shell-mean profile is then compared to the
   161	continuum kernel $e^{-|x|/\varphi}$ and to the LHCb 2025 $P_{5}'$ data
   162	on the LHCb bin grid. Two criteria are used: a \emph{pure-geometry}
   163	criterion (correlation between the discrete shell-mean and the Layer-1
   164	continuum kernel, no LHCb data involvement), and a \emph{data}
   165	criterion ($\chi^{2}$ against the LHCb 2025 single-observable fit).
   166	
   167	\begin{table}[h]
   168	\centering
   169	\small
   170	\begin{tabular}{lccc}
   171	\toprule
   172	variant & $\mathrm{corr}(\overline{\psi}, e^{-|x|/\varphi})$ &
   173	        $\chi^{2}$ vs LHCb 2025 $P_{5}'$ &
   174	        ranking \\
   175	\midrule
   176	unweighted Laplacian          & $\mathbf{0.9968}$ & $\mathbf{13.555}$ & $1$ on both \\
   177	$\varphi$-cocycle geometric    & $0.9130$ & $14.713$ & $2$ on both \\
   178	$\varphi$-cocycle arithmetic   & $0.8989$ & $14.782$ & $3$ on both \\
   179	\bottomrule
   180	\end{tabular}
   181	\caption{Variant selection. The unweighted Laplacian wins on both the
   182	pure-geometry criterion (correlation with the Layer-1 continuum
   183	kernel) and the LHCb-data criterion. The two rankings agree, so the
   184	variant choice is consistent with selection on geometric grounds
   185	independent of the data; the LHCb data only confirms it.
   186	Reproducible from \texttt{scripts/wo016b\_variant\_geometry.py}
   187	(reports/wo016b\_variant\_geometry.csv).}
   188	\label{tab:variant_selection}
   189	\end{table}
   190	
   191	The unweighted Laplacian is selected as the primary kernel. The
   192	two-criterion agreement means the variant choice does not consume an
   193	extra effective fit parameter: the variant choice would have been the
   194	same if only the geometric criterion had been applied, and the AIC
   195	counting $k=1$ for VFD\_GREEN\_600CELL is therefore retained
   196	throughout this paper. The historical sequence is acknowledged in
   197	\S\ref{sec:limitations}: the data was looked at first, and only later
   198	verified to agree with the pure-geometry ranking.
   199	
   200	\paragraph{Spectral content.} An eigenvalue decomposition of

 succeeded in 432ms:
     1	# WO-016d — Non-linear cross-dataset refit
     2	
     3	Re-runs the WO-014 cross-dataset and WO-015 cross-channel fits with `flavio.np_prediction` directly (non-linear) instead of the Mode-B Taylor expansion. The linearised values from reports/wo014_cross_dataset.csv and reports/wo015_cross_channel.csv are quoted in parentheses for comparison.
     4	
     5	| dataset | non-linear χ² (FREE) | non-linear χ² (VFD) | ΔAIC (NL) | ΔC9 (NL) | A (NL) |
     6	|---|---:|---:|---:|---:|---:|
     7	| LHCb-2015 | 30.691 | 30.450 | -0.241 | -1.080 | +1.235 |
     8	| LHCb-2021-Kstplus | 22.765 | 22.933 | +0.168 | -1.820 | +2.059 |
     9	| CMS-2025-noP4p | 43.731 | 44.205 | +0.473 | -0.954 | +1.053 |
    10	| LHCb-2025 | 40.891 | 41.983 | +1.093 | -1.003 | +1.135 |
    11	| Bs2phi-LHCb-2015 | 13.201 | 12.962 | -0.240 | -4.122 | +4.984 |
    12	

 succeeded in 438ms:
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
**1. Claim Audit**

- “Operator-norm bound `||C_phi^{-1}|| = phi^2`” is established for the finite connected graph case: [02_definition.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:54)-[02_definition.tex:80](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:80), [04_spectrum.tex:67](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67)-[04_spectrum.tex:78](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78). Good.
- “`phi^{-2}` is a design-level shift” is stated correctly and repeatedly: [02_definition.tex:101](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:101)-[02_definition.tex:121](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:121). Good.
- Must fix: “the operator-norm bound `phi^2` is the same constant as the continuum decay scale” is false as written; the decay scale is `phi`, not `phi^2`: [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107)-[02_definition.tex:109](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:109). Edit to: “both are fixed by the same design-level choice `phi^{-2}`.”
- 600-cell graph facts are numerically established and match `results.json`: [03_substrate.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:58)-[03_substrate.tex:73](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:73). Minor wording issue: H4 transitivity forces uniformity, not the numerical value `12` by itself.
- Spectrum claim is established numerically, not exactly: [04_spectrum.tex:5](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5)-[04_spectrum.tex:14](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:14). The paper correctly says the closed-form identification is algebraic recognition, not exact derivation.
- Discrete-to-continuum agreement is established only as a Pearson-correlation witness, not convergence/equality: [05_agreement.tex:36](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:36)-[05_agreement.tex:55](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:55), [05_agreement.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:111)-[05_agreement.tex:120](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:120). Good.
- Overstatement: “the `$24$-cell, `$120$-cell` ... would give different correlations” is untested: [05_agreement.tex:127](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:127)-[05_agreement.tex:131](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:131). Say “would need to be tested.”
- b-anomaly structural claims are mostly inherited correctly, but “replaces the constant SM shape” is too strong/misleading: [06_passive_witness.tex:12](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12)-[06_passive_witness.tex:16](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:16). It should say it adds/tests a fixed `q^2`-dependent effective shift on top of the SM backend.
- b-anomaly Mode-B caveat is present, but terminology is wrong: [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111). Mode B is the earlier linearised analysis; the later refit is non-linear, not “Mode-B (non-linear).”
- aria-chess claims match the companion text in substance, including `17/18` standard and `18/18` after P4 deep-dive: [07_active_witness.tex:47](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47)-[07_active_witness.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:58), validated against [aria-chess main.tex:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex:81)-[aria-chess main.tex:84](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex:84). The closure paper abstract should inherit this caveat, not just say “passes eighteen.”

**2. Internal Consistency**

The abstract headline numbers match the paper and `results.json`: `120`, `720`, degree `12`, shell sizes, spectrum, norm, and correlations all agree.

Internal issue: b-anomaly variant history is phrased two ways. The closure paper correctly states the historical caveat at [05_agreement.tex:105](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:105)-[05_agreement.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:107) and [09_limitations.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:54)-[09_limitations.tex:64](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:64), matching b-anomaly’s limitation [09_limitations.tex:29](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:29)-[09_limitations.tex:38](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38). But the abstract phrase “established independently” at [main.tex:99](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:99)-[main.tex:102](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:102) should be softened to “separately, with the historical non-blind caveat.”

Cross-channel wording is numerically ambiguous. The closure paper says residual `~50% overshoot`: [06_passive_witness.tex:71](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71)-[06_passive_witness.tex:76](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:76), matching README line [README.md:27](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/README.md:27), but the b-anomaly paper’s arithmetic says `A_P * 2.2 ≈ 2.5` vs observed `4.98`, i.e. a factor `~2` residual: [06_cross_dataset.tex:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:81)-[06_cross_dataset.tex:85](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:85). Use the explicit numbers instead of “50%.”

**3. External Consistency / Numerics**

All requested kernel numerics match `results.json`.

- Vertices/edges/degree: paper [03_substrate.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:58)-[03_substrate.tex:73](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:73); source [results.json:4](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:4)-[results.json:9](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:9).
- Shell sizes: paper [03_substrate.tex:88](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:88)-[03_substrate.tex:97](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:97); source [results.json:15](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:15)-[results.json:25](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:25).
- Spectrum: paper [04_spectrum.tex:28](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:28)-[04_spectrum.tex:38](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:38); source [results.json:43](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:43)-[results.json:79](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:79).
- Operator norm: paper [04_spectrum.tex:67](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67)-[04_spectrum.tex:78](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78); source [results.json:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:81)-[results.json:85](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:85).
- Correlations: paper [05_agreement.tex:87](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:87)-[05_agreement.tex:89](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:89); source [results.json:134](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:134)-[results.json:146](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:146). No disagreement.

**4. Operator-Witness Scope Discipline**

Mostly good. The paper repeatedly denies derivation of `phi^{-2}`, 600-cell uniqueness, kernel uniqueness, and selection theorem: [main.tex:146](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:146)-[main.tex:159](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:159), [09_limitations.tex:150](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:150)-[09_limitations.tex:166](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:166).

Sentences to soften:
- [05_agreement.tex:127](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:127)-[05_agreement.tex:131](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:131): do not predict untested alternative-polytope correlations.
- [10_conclusion.tex:75](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:75)-[10_conclusion.tex:79](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:79): prior-art claim is modest but unsupported by a search protocol; acceptable for preprint, weak for publication.

**5. Tightness**

Suggested one-line edits:

- [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107): “the inverse norm `phi^2` and continuum decay scale `phi` are both fixed by the single design choice `phi^{-2}`.”
- [03_substrate.tex:63](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:63): “H4 transitivity forces uniform degree; the short-edge construction gives degree 12.”
- [06_passive_witness.tex:15](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:15): “tests a fixed `q^2`-dependent effective shift against the SM backend” instead of “replaces the constant SM shape.”
- [07_active_witness.tex:126](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126): “consistent with `17/18` standard, `18/18` after documented P4 deep-dive” in the abstract/headline too.

**6. Surface Issues**

Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are defined and used consistently.

Potential LaTeX/layout issues:
- The two-witness table uses `p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}` plus intercolumn padding, likely overfull: [07_active_witness.tex:147](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147). Reduce widths or use `tabularx`.
- Long b-anomaly table rows may overrun in narrow layouts: [06_passive_witness.tex:45](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:45)-[06_passive_witness.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:54).
- “Mode-B (non-linear)” is a terminology error, not just style: [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111).

**7. Top Three Fixes**

1. Fix the mathematically false “same constant” claim for `phi^2` vs decay scale `phi`: [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107)-[02_definition.tex:109](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:109).
2. Make the b-anomaly inheritance exact: correct “Mode-B (non-linear)” and avoid “replaces the SM shape”: [06_passive_witness.tex:12](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12)-[06_passive_witness.tex:30](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:30), [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111).
3. Carry the aria-chess caveat into the abstract/headline: `17/18` standard, `18/18` after documented `N=20` P4 deep-dive, and six EEG signatures on a single deterministic seed. Current short form at [main.tex:143](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:143)-[main.tex:144](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:144) is too compressed.

**8. Verdict**

Publication ready: no — must-fix list above.

The numerical core is sound against the local reproduction file. The remaining blockers are wording precision and inheritance discipline, not computation.
tokens used
178,326
**1. Claim Audit**

- “Operator-norm bound `||C_phi^{-1}|| = phi^2`” is established for the finite connected graph case: [02_definition.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:54)-[02_definition.tex:80](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:80), [04_spectrum.tex:67](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67)-[04_spectrum.tex:78](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78). Good.
- “`phi^{-2}` is a design-level shift” is stated correctly and repeatedly: [02_definition.tex:101](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:101)-[02_definition.tex:121](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:121). Good.
- Must fix: “the operator-norm bound `phi^2` is the same constant as the continuum decay scale” is false as written; the decay scale is `phi`, not `phi^2`: [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107)-[02_definition.tex:109](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:109). Edit to: “both are fixed by the same design-level choice `phi^{-2}`.”
- 600-cell graph facts are numerically established and match `results.json`: [03_substrate.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:58)-[03_substrate.tex:73](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:73). Minor wording issue: H4 transitivity forces uniformity, not the numerical value `12` by itself.
- Spectrum claim is established numerically, not exactly: [04_spectrum.tex:5](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5)-[04_spectrum.tex:14](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:14). The paper correctly says the closed-form identification is algebraic recognition, not exact derivation.
- Discrete-to-continuum agreement is established only as a Pearson-correlation witness, not convergence/equality: [05_agreement.tex:36](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:36)-[05_agreement.tex:55](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:55), [05_agreement.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:111)-[05_agreement.tex:120](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:120). Good.
- Overstatement: “the `$24$-cell, `$120$-cell` ... would give different correlations” is untested: [05_agreement.tex:127](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:127)-[05_agreement.tex:131](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:131). Say “would need to be tested.”
- b-anomaly structural claims are mostly inherited correctly, but “replaces the constant SM shape” is too strong/misleading: [06_passive_witness.tex:12](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12)-[06_passive_witness.tex:16](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:16). It should say it adds/tests a fixed `q^2`-dependent effective shift on top of the SM backend.
- b-anomaly Mode-B caveat is present, but terminology is wrong: [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111). Mode B is the earlier linearised analysis; the later refit is non-linear, not “Mode-B (non-linear).”
- aria-chess claims match the companion text in substance, including `17/18` standard and `18/18` after P4 deep-dive: [07_active_witness.tex:47](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47)-[07_active_witness.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:58), validated against [aria-chess main.tex:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex:81)-[aria-chess main.tex:84](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex:84). The closure paper abstract should inherit this caveat, not just say “passes eighteen.”

**2. Internal Consistency**

The abstract headline numbers match the paper and `results.json`: `120`, `720`, degree `12`, shell sizes, spectrum, norm, and correlations all agree.

Internal issue: b-anomaly variant history is phrased two ways. The closure paper correctly states the historical caveat at [05_agreement.tex:105](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:105)-[05_agreement.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:107) and [09_limitations.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:54)-[09_limitations.tex:64](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:64), matching b-anomaly’s limitation [09_limitations.tex:29](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:29)-[09_limitations.tex:38](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38). But the abstract phrase “established independently” at [main.tex:99](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:99)-[main.tex:102](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:102) should be softened to “separately, with the historical non-blind caveat.”

Cross-channel wording is numerically ambiguous. The closure paper says residual `~50% overshoot`: [06_passive_witness.tex:71](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71)-[06_passive_witness.tex:76](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:76), matching README line [README.md:27](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/README.md:27), but the b-anomaly paper’s arithmetic says `A_P * 2.2 ≈ 2.5` vs observed `4.98`, i.e. a factor `~2` residual: [06_cross_dataset.tex:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:81)-[06_cross_dataset.tex:85](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:85). Use the explicit numbers instead of “50%.”

**3. External Consistency / Numerics**

All requested kernel numerics match `results.json`.

- Vertices/edges/degree: paper [03_substrate.tex:58](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:58)-[03_substrate.tex:73](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:73); source [results.json:4](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:4)-[results.json:9](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:9).
- Shell sizes: paper [03_substrate.tex:88](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:88)-[03_substrate.tex:97](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:97); source [results.json:15](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:15)-[results.json:25](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:25).
- Spectrum: paper [04_spectrum.tex:28](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:28)-[04_spectrum.tex:38](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:38); source [results.json:43](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:43)-[results.json:79](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:79).
- Operator norm: paper [04_spectrum.tex:67](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67)-[04_spectrum.tex:78](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78); source [results.json:81](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:81)-[results.json:85](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:85).
- Correlations: paper [05_agreement.tex:87](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:87)-[05_agreement.tex:89](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:89); source [results.json:134](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:134)-[results.json:146](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json:146). No disagreement.

**4. Operator-Witness Scope Discipline**

Mostly good. The paper repeatedly denies derivation of `phi^{-2}`, 600-cell uniqueness, kernel uniqueness, and selection theorem: [main.tex:146](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:146)-[main.tex:159](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:159), [09_limitations.tex:150](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:150)-[09_limitations.tex:166](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex:166).

Sentences to soften:
- [05_agreement.tex:127](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:127)-[05_agreement.tex:131](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex:131): do not predict untested alternative-polytope correlations.
- [10_conclusion.tex:75](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:75)-[10_conclusion.tex:79](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex:79): prior-art claim is modest but unsupported by a search protocol; acceptable for preprint, weak for publication.

**5. Tightness**

Suggested one-line edits:

- [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107): “the inverse norm `phi^2` and continuum decay scale `phi` are both fixed by the single design choice `phi^{-2}`.”
- [03_substrate.tex:63](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex:63): “H4 transitivity forces uniform degree; the short-edge construction gives degree 12.”
- [06_passive_witness.tex:15](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:15): “tests a fixed `q^2`-dependent effective shift against the SM backend” instead of “replaces the constant SM shape.”
- [07_active_witness.tex:126](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126): “consistent with `17/18` standard, `18/18` after documented P4 deep-dive” in the abstract/headline too.

**6. Surface Issues**

Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are defined and used consistently.

Potential LaTeX/layout issues:
- The two-witness table uses `p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}` plus intercolumn padding, likely overfull: [07_active_witness.tex:147](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147). Reduce widths or use `tabularx`.
- Long b-anomaly table rows may overrun in narrow layouts: [06_passive_witness.tex:45](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:45)-[06_passive_witness.tex:54](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:54).
- “Mode-B (non-linear)” is a terminology error, not just style: [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111).

**7. Top Three Fixes**

1. Fix the mathematically false “same constant” claim for `phi^2` vs decay scale `phi`: [02_definition.tex:107](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:107)-[02_definition.tex:109](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex:109).
2. Make the b-anomaly inheritance exact: correct “Mode-B (non-linear)” and avoid “replaces the SM shape”: [06_passive_witness.tex:12](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12)-[06_passive_witness.tex:30](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:30), [06_passive_witness.tex:106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106)-[06_passive_witness.tex:111](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111).
3. Carry the aria-chess caveat into the abstract/headline: `17/18` standard, `18/18` after documented `N=20` P4 deep-dive, and six EEG signatures on a single deterministic seed. Current short form at [main.tex:143](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:143)-[main.tex:144](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex:144) is too compressed.

**8. Verdict**

Publication ready: no — must-fix list above.

The numerical core is sound against the local reproduction file. The remaining blockers are wording precision and inheritance discipline, not computation.

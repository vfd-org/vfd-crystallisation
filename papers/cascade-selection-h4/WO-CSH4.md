# WO-CSH4 v4: cascade-selection-h4

**Working title.** *Cascade Selection on the $H_4$ Branch: An Auxiliary
Block Graph Laplacian and a Witnessed $(O1)$ Discharge on $V_{600}$.*

**Status.** v4, after pre-build codex review of v3 caught (a)
spectral-gap notation collision ($\lambda_2(L_N^{\mathrm{block}}) = 0$
because the kernel is $32$-dim; must use $\lambda_+(L_N^{\mathrm{block}})$
for the smallest *positive* eigenvalue), (b) $(O0)$ verification
incomplete (cascade-mechanism §3.4 also requires $C^1$ regularity of
the pushforward bonding map; must cite P3 `def:p0`/`thm:bonding`),
(c) Laplacian convention on labelled-edge multisets must be stated
explicitly. v4 fixes all three plus the line-number
quote at `cascade-mechanism.tex` for the "selection is successor's
task" passage (corrected to lines 637–639).

History: v1→v2 fixed (a) operator mismatch with P4's $A_n$,
(b) $(O1)$-API mismatch (mechanism wants a *witnessed* state, not a
$28$-dim "selected subspace"), (c) attribution errors. v2→v3 fixed
(a) API taxonomy drift, (b) P4 flow over-attribution, (c) "single
tuple" wording, (d) Chung Ch.~1 bound. v3→v4 fixes the remaining
spec-level blockers identified above.

---

## 1. Goal

For each fixed $\xi^* \in (F^0)^{W(H_4)} \setminus \{0\}$, exhibit
a witnessed $(O1)$-tuple
$(\Phi_N, R_N, \Psi_N^t, \phi^\star_N, \phi_N^{(0)})$
that discharges the cascade-mechanism §3.4 obligation $(O1)$
(top-rung fixed-point + convergence) on the $H_4$ branch at finite
top-rung level $N$.

The space $(F^0)^{W(H_4)}$ is an explicit $28$-dimensional real
subspace of $F^0$ (clause (4) below). The freedom in $\xi^*$ is the
*$(O1)$-witness parameter*; reducing to a single ray requires the
named open hypothesis **(H-uniqueness)**, which lies *outside* the
cascade-closure consumer API as defined in cascade-mechanism §3.4
and is the next-paper task.

This paper does **not** discharge $(O2)$, $(O3)$, or the full
$(O0)$–$(O3)$ cascade-closure consumer API; $(O0)$ is verified
only as a standing precondition for the witnessed $(O1)$ tuple
(per cascade-mechanism §3.4 lines 595–608). It does **not** lift
to the inverse limit, address the $D_4$ branch, or identify the
auxiliary operator $L_N^{\mathrm{block}}$ with P4's $A_n^{\mathrm{vertex}}$
or compat's $\widetilde A_n$. Each is an explicit non-claim (§9).

The narrative move: cascade-mechanism §3.4 currently says
"selection of $\phi^\star_N$ itself is not provided by cascade
closure and is the successor paper's own task." This paper *is*
that successor paper for the $(O1)$ slot on the $H_4$ branch at
finite $N$, with one named open hypothesis carried forward.

## 2. The auxiliary operator: $L_N^{\mathrm{block}}$

We introduce a new operator, distinct from P4's $A_n$ (which acts
only on the $V_8$-imaginary direction via the coboundary projection
$\pi_{F^0 \to F^1}$ of P4 `def:coboundary`) and distinct from
cascade-refinement-compat's $\widetilde A_n$ (`def:Atilde`, which
lives in the abstract scalar pure-midpoint model of
`def:abstract-model`).

**Definition (Block graph Laplacian).** *Let $G_N^{H_4} = (V(G_N^{H_4}),
E(G_N^{H_4}))$ be the level-$N$ Schl\"{a}fli-style refined graph of
P3 (`def:refinement`), with base $G_0^{H_4}$ on $V_{600}$
(P3 `def:base-graphs`). Recall (P3 `def:refinement`) that
$E(G_N^{H_4})$ is a* \emph{labelled-edge multiset}: *each generated
edge carries a class tag $\in \{(\mathrm{a}), (\mathrm{b}), (\mathrm{c})\}$
and a parent-face tag where applicable, so two edges with the same
unordered endpoint pair but different tags are distinct elements.
Let $L^{\mathrm{cl}}_N$ be the* \emph{labelled-multiset combinatorial
scalar graph Laplacian} *on the finite vertex set $V(G_N^{H_4})$,
acting on $\R$-valued functions by*
\[
  (L^{\mathrm{cl}}_N f)(v)
  := \sum_{e \in E(G_N^{H_4}),\; v \in e} (f(v) - f(\mathrm{op}_e(v))),
\]
*where each labelled edge $e = \{v, \mathrm{op}_e(v)\}$ in
$E(G_N^{H_4})$ contributes once with multiplicity $1$
(parallel labelled edges with coinciding endpoints are summed
separately). Equivalently, $L^{\mathrm{cl}}_N = D_N - W_N$ where
$D_N(v) := |\{e \in E(G_N^{H_4}) : v \in e\}| = \deg_{G_N^{H_4}}(v)$
in the labelled-multiset degree count and $W_N(v, u)$ is the number
of labelled edges joining $v$ to $u$ (an integer $\geq 0$).
This is the standard convention of \cite[Ch.~1]{Chung} extended to
multigraphs.*

*Define the* \emph{block graph Laplacian} *on
$X_N^{0, H_4} = \ell^2(V(G_N^{H_4}); F^0)$ by acting fibrewise:*
\[
  L_N^{\mathrm{block}}(\phi)(v)
  := \bigl(L^{\mathrm{cl}}_N \phi^{(H_4)}\bigr)(v) \oplus
     \bigl(L^{\mathrm{cl}}_N \phi^{(D_4)}\bigr)(v) \oplus
     \bigl(L^{\mathrm{cl}}_N \phi^{(16)}\bigr)(v) \oplus
     \bigl(L^{\mathrm{cl}}_N \phi^{(8)}\bigr)(v),
\]
*where $\phi(v) = \phi^{(H_4)}(v) \oplus \phi^{(D_4)}(v) \oplus
\phi^{(16)}(v) \oplus \phi^{(8)}(v)$ in the orthogonal decomposition
$F^0 = V_{H_4} \oplus V_{D_4} \oplus V_{16} \oplus V_8$
(P3 `not:fibres`), and $L^{\mathrm{cl}}_N$ acts componentwise via
the same scalar Laplacian on each summand independently.*

**Why a new operator.** Codex round 1 (correctly) flagged that
P4's $A_n^{\mathrm{vertex}} = d_n^* d_n$ is non-trivial only on the
$V_8$-imaginary direction (P4 `def:coboundary` projects $F^0$ to
$F^1 = \mathrm{Im}(\OO)$ before taking the difference). Hence
$\ker A_n^{\mathrm{vertex}} \cong F^0/\mathrm{Im}(\OO)$-valued
functions plus constant $\mathrm{Im}(\OO)$, i.e.\
$\dim \ker A_n^{\mathrm{vertex}} = 25\,|V(G_n^\bullet)| + 7$ for
connected $G_n^\bullet$. That kernel is too large to give a clean
witness for $(O1)$. The simple block-diagonal extension whose
kernel is exactly the $F^0$-valued constants ($\dim = 32$) is
$L_N^{\mathrm{block}}$ defined above. (We do not claim
$L_N^{\mathrm{block}}$ is unique among block-diagonal extensions
with this kernel; the construction is one natural choice.) We use it as the
$(O1)$-witness operator.

**Relation to upstream operators (no identification claimed).**
- P4 has $A_n^{\mathrm{vertex}} = \iota_{F^1 \to F^0} \circ
  L^{\mathrm{cl}}_N \circ \pi_{F^0 \to F^1}$ (informally,
  $L^{\mathrm{cl}}_N$ sandwiched by P4's projection and inclusion
  of `def:coboundary`); this is *not* a restriction of
  $L_N^{\mathrm{block}}$ — it differs by replacing three of the
  four fibre blocks with zero.
- compat's $\widetilde A_n = 2^n A_n^{\mathrm{vertex}}$
  (`def:Atilde`) is the *scaled scalar abstract-model analogue*
  of P4's vertex Laplacian: compat works in the
  abstract scalar pure-midpoint reduction
  (`def:abstract-model`), where the underlying state space is
  scalar-valued (not $F^0$-valued) on a pure-midpoint refinement
  of $V_{600}$. The full-fibre $L_N^{\mathrm{block}}$ on
  $X_N^{0, H_4}$ used in this paper is in a different scope from
  both compat (which has no fibre $F^0$) and P4 (which restricts
  to the $V_8$-imaginary direction).
- $L_N^{\mathrm{block}}$ is **introduced in this paper** for the
  $(O1)$ witness. Theorems about it do not transfer back to P4's
  $A_n$ or compat's $\widetilde A_n$.

## 3. The single named theorem

**Theorem (Witnessed $(O1)$ discharge on the $H_4$ branch at finite
top-rung level $N$, parametrised by $\xi^*$).**
*Let $N \geq 0$, let $X_N^{0, H_4}$ be the finite-level vertex-sector
Hilbert space (P3 `def:Xn-0`), and let $L_N^{\mathrm{block}}$ be the
block graph Laplacian of §2.*

*(Setup.) For each fixed $\xi^* \in (F^0)^{W(H_4)} \setminus \{0\}$,
where $(F^0)^{W(H_4)}$ is the $W(H_4)$-fixed subspace of $F^0$ under
the branchwise Coxeter representation $\rho_{F^0}^{H_4}$ of P3
`def:coxeter` (see clause (4) for explicit $\dim_\R = 28$), set:*

- *$\Phi_N := X_N^{0, H_4}$;*
- *$R_N(\phi) := \tfrac{1}{2} \langle \phi, L_N^{\mathrm{block}}
  \phi \rangle_{X_N^{0, H_4}}$, a continuous symmetric quadratic
  form;*
- *$\Psi_N^t := e^{-t L_N^{\mathrm{block}}}$, the gradient flow of
  $R_N$ (existence and uniqueness by the same finite-dimensional
  matrix-exponential argument as P4 `thm:flow-exists`, applied
  here to the bounded self-adjoint operator
  $L_N^{\mathrm{block}}$ on the finite-dimensional Hilbert space
  $X_N^{0, H_4}$);*
- *$\phi^\star_N := \Psi_N(\xi^*)$, where the $\R$-linear constant-function embedding
  $\Psi_N \colon F^0 \to \ker L_N^{\mathrm{block}}$ is given by
  $\Psi_N(\xi)(v) := \xi$ for all $v \in V(G_N^{H_4})$;*
- *$\phi_N^{(0)} := \phi^\star_N$ (any other $\phi$ with
  $P_{\ker L_N^{\mathrm{block}}} \phi = \phi^\star_N$ also
  works; we pick the simplest representative).*

*Then:*

1. *(Self-adjointness, positive semi-definiteness, boundedness.)
   $L_N^{\mathrm{block}}$ is bounded, self-adjoint, and positive
   semi-definite on $X_N^{0, H_4}$, with operator-norm bound
   $\|L_N^{\mathrm{block}}\|_{\mathrm{op}} \leq 2\,\Delta(G_N^{H_4})$
   where $\Delta(G_N^{H_4}) := \max_v \deg_{G_N^{H_4}}(v)$
   (\cite[Ch.~1]{Chung}; the block-diagonal structure preserves
   the scalar bound).*
2. *(Connectivity of $G_N^{H_4}$ and kernel structure.)
   $G_N^{H_4}$ is connected for every $N \geq 0$ (induction:
   $G_0^{H_4}$ on $V_{600}$ is connected by
   \cite[\S 22.7]{CoxeterRegularPolytopes}; class-(a) and
   class-(b) edges of P3 `def:refinement` keep new midpoints and
   centroids attached). Hence the constant-function embedding
   $\Psi_N \colon F^0 \to \ker L_N^{\mathrm{block}}$ is an
   $\R$-linear isomorphism (kernel of connected scalar Laplacian
   $L^{\mathrm{cl}}_N$ is one-dimensional, \cite[Ch.~1]{Chung};
   the block extension multiplies kernel dimension by $\dim F^0$).
   $\dim_\R \ker L_N^{\mathrm{block}} = 32$.*
3. *(Convergence.) For every $\Phi(0) \in X_N^{0, H_4}$,
   $\lim_{t \to \infty} e^{-t L_N^{\mathrm{block}}} \Phi(0)
   = P_{\ker L_N^{\mathrm{block}}} \Phi(0)$ in
   $X_N^{0, H_4}$-norm, with uniform exponential bound governed by
   the smallest* \emph{positive} *eigenvalue of $L_N^{\mathrm{block}}$,
   which we denote*
   \[
     \lambda_+(L_N^{\mathrm{block}}) \;:=\;
     \min\bigl\{\lambda \in \mathrm{spec}(L_N^{\mathrm{block}}) :
                \lambda > 0\bigr\}
     \;=\; \lambda_+(L^{\mathrm{cl}}_N) \;>\; 0
   \]
   *(the spectral gap; the block extension repeats every scalar
   eigenvalue with multiplicity $\dim F^0 = 32$, so in particular
   $\lambda_+$ is unchanged from the scalar case, and equals the
   smallest positive eigenvalue of $L^{\mathrm{cl}}_N$).
   N.B.\ the standard "second-eigenvalue" notation
   $\lambda_2(L_N^{\mathrm{block}}) = 0$ here because the kernel
   has dimension $32 > 1$; we use $\lambda_+$ throughout to avoid
   ambiguity. The convergence is by spectral theorem on a finite-dim
   PSD operator (\cite[Ch.~VIII.5]{ReedSimonI},
   \cite[Ch.~6.2]{HornJohnson}).*
4. *($W(H_4)$-fixed subspace dimension.) Under the branchwise
   Coxeter representation $\rho_{F^0}^{H_4}$ of P3 `def:coxeter`
   (standard $H_4$-reflection representation on $V_{H_4}$, trivial
   on $V_{D_4}, V_{16}, V_8$),*
   \[
     (F^0)^{W(H_4)}
     = V_{H_4}^{W(H_4)} \oplus V_{D_4} \oplus V_{16} \oplus V_8
     = \{0\} \oplus V_{D_4} \oplus V_{16} \oplus V_8,
   \]
   *so $\dim_\R (F^0)^{W(H_4)} = 0 + 4 + 16 + 8 = 28$.
   ($V_{H_4}^{W(H_4)} = \{0\}$ by irreducibility of the standard
   reflection representation of the finite irreducible Coxeter
   group $H_4$, \cite[Ch.~2]{Humphreys}; the other three summands
   are fully fixed because $W(H_4)$ acts trivially on them in
   P3 `def:coxeter`.)*
5. *($(O1)$ witnessed discharge.) The tuple
   $(\Phi_N, R_N, \Psi_N^t, \phi^\star_N, \phi_N^{(0)})$
   discharges the cascade-mechanism §3.4 obligation $(O1)$
   (top-rung fixed-point and convergence; see
   `cascade-mechanism.tex` lines 609–617):*
   - *$\phi^\star_N \in \Phi_N$ is a top-rung state with
     $R_N(\phi^\star_N) = \tfrac{1}{2}\langle \Psi_N(\xi^*),
     L_N^{\mathrm{block}} \Psi_N(\xi^*) \rangle = 0$, since
     $\Psi_N(\xi^*) \in \ker L_N^{\mathrm{block}}$ by clause (2).*
   - *$\Psi_N^t \phi_N^{(0)} = \phi^\star_N$ for every $t \geq 0$
     when $\phi_N^{(0)} = \phi^\star_N$ (a fixed point of the flow,
     trivially convergent); for any other admissible
     $\phi_N^{(0)}$ with $P_{\ker L_N^{\mathrm{block}}} \phi_N^{(0)}
     = \phi^\star_N$,
     $\lim_{t \to \infty} \Psi_N^t \phi_N^{(0)} = \phi^\star_N$
     by clause (3).*

*$(O0)$ standing analytic preconditions per cascade-mechanism §3.4
(`cascade-mechanism.tex` lines 595–608) are verified separately
in §7 of the .tex; namely:*
- *Finite-dimensional Hilbert structure of $\Phi_N = X_N^{0, H_4}$:
  P3 `prop:Xn-Hilbert` (already a finite-dim Hilbert space);*
- *$R_N \in C^1(\Phi_N)$: continuous symmetric quadratic forms on
  finite-dimensional Hilbert spaces are $C^1$ (in fact $C^\omega$);*
- *Well-posed gradient flow $\Psi_N^t = e^{-t L_N^{\mathrm{block}}}$:
  by the same finite-dim ODE / matrix-exponential argument as
  P4 `thm:flow-exists`;*
- *$C^1$ pushforward bonding maps $\pi^{\sharp}_{k+1, k}$:
  the relevant pushforward in this single-rung discharge of $(O1)$
  is the trivial projection $\Phi_N \to \Phi_N$ (top-rung only,
  no inter-rung pushforward needed for clauses (1)–(3) of
  cascade-mechanism §3.4 $(O1)$). For completeness, when the
  cascade-mechanism API requires an inter-rung pushforward for
  downstream propagation, P3 `def:p0` (vertex restriction) and
  P3 `thm:bonding` (boundedness of $p_{n+1, n}^0$) supply a
  bounded $\R$-linear (hence $C^1$, in fact $C^\omega$)
  pushforward map between adjacent levels; this paper does not
  use it but records its availability.*

*$(O2)$, $(O3)$ are not addressed in this paper and remain in
their current cascade-refinement-compat status (i.e., $(O2)$ as
stated remains false; $(O3)$ holds in compat's abstract scalar
pure-midpoint model).*

## 4. Why this is theorem-grade tractable at finite $N$

- $L_N^{\mathrm{block}}$'s self-adjointness, positive
  semi-definiteness, and bounded operator norm follow from
  the same properties of the scalar combinatorial graph Laplacian
  $L^{\mathrm{cl}}_N$ (\cite[Ch.~1]{Chung}) plus the
  orthogonal-direct-sum structure of $F^0$. **We do not invoke
  P4 `prop:block-bounds`**, which bounds P4's $A_n$, not
  $L_N^{\mathrm{block}}$.
- **Connectivity** of $G_N^{H_4}$ is induction on $N$ from
  base connectivity of the $600$-cell edge graph
  (\cite[\S 22.7]{CoxeterRegularPolytopes}). Inductive step uses
  only class-(a) (subdividing) and class-(b) (midpoint-centroid)
  edges of P3 `def:refinement`; class-(c) midpoint-midpoint
  diagonals are not needed.
- **Kernel of connected scalar graph Laplacian** is $1$-dim
  spanned by the constant function (\cite[Ch.~1]{Chung}). Hence
  $\ker L^{\mathrm{cl}}_N \cong \R$. The block extension
  multiplies dimensions: $\ker L_N^{\mathrm{block}} \cong F^0$,
  $\dim = 32$.
- **Spectral gap** $\lambda_+(L^{\mathrm{cl}}_N) > 0$ (smallest
  positive eigenvalue) from connectivity + finite-dim PSD spectrum.
  Same for $L_N^{\mathrm{block}}$ (block-diagonal preserves
  spectrum multiplicities; the smallest positive eigenvalue is
  unchanged, only its multiplicity becomes $32 \cdot \mu$ where
  $\mu$ is the scalar multiplicity).
- **Flow existence, uniqueness, and convergence**
  $e^{-t L_N^{\mathrm{block}}} \to P_{\ker}$ in operator norm
  with rate $\lambda_+$: the same finite-dim ODE /
  matrix-exponential argument as P4 `thm:flow-exists`, re-applied
  here to the bounded self-adjoint $L_N^{\mathrm{block}}$;
  spectral theorem (\cite[Ch.~VIII.5]{ReedSimonI},
  \cite[Ch.~6.2]{HornJohnson}). **P4's theorem is not literally
  invoked**; it is the same standard finite-dim argument.
- **$W(H_4)$-fixed subspace dimension** is character-theoretic
  bookkeeping using P3 `def:coxeter` plus irreducibility of the
  standard $H_4$-reflection representation
  (\cite[Ch.~2]{Humphreys}). **No P2 character data is invoked**;
  P2's `tab:P2-spectrum` is used only for the worked $N = 0$
  spectral numerics in §8.

**No open analytic hypothesis is needed at finite $N$.** $(L1)$
and $(L3)$ from compat are not used.

## 5. Inputs (label-form citations only)

- **P3 (`cascade-refinement-spaces`):**
  `def:Xn-0`, `def:refinement`, `def:base-graphs`,
  `prop:Xn-Hilbert`, `not:fibres`, `def:coxeter`,
  `lem:coxeter-unitary`.
- **P4 (`cascade-closure-dynamics`):**
  `def:coboundary` (cited only to explain why P4's $A_n^{\mathrm{vertex}}$
  is not the right operator for our witness — see §2);
  `thm:flow-exists` cited for the *style* of the
  finite-dim flow-existence argument, not literally invoked.
- **cascade-refinement-compat:**
  `def:Atilde` (cited only as background context — the
  scaled-curvature convention $\widetilde A_n = 2^n A_n^{\mathrm{vertex}}$
  is *not* used for $L_N^{\mathrm{block}}$; we explain in §2
  the scope difference);
  `def:abstract-model` (cited for the same scope-distinction).
- **cascade-mechanism:** §3.4 obligations $(O0)$ (preconditions) and
  $(O1)$ (top-rung fixed-point + convergence) — the four
  obligations are $(O0)$, $(O1)$, $(O2)$, $(O3)$, separate; this
  paper supplies the witness tuple for $(O1)$ only, and verifies
  $(O0)$ explicitly in §7.
- **P2 (`cascade-algebraic-substrate`):**
  `def:V600`, `def:icosian-ring`, `prop:24-in-600` (background
  for $V_{600}$ as an $H_4$-orbit);
  `tab:P2-spectrum` (for worked $N = 0$ numerics in §8 only:
  $\lambda_+(L^{\mathrm{cl}}_0) = 9 - 3\sqrt{5}$).
- **Classical:**
  Humphreys, *Reflection Groups and Coxeter Groups*, Ch.~2
  (irreducibility of the standard reflection representation of
  finite irreducible Coxeter groups, including $H_4$);
  Chung, *Spectral Graph Theory*, Ch.~1 (graph Laplacian kernel
  and operator-norm bound on connected graphs);
  Reed–Simon I, Ch.~VIII.5 (functional calculus for self-adjoint
  finite-dim operators);
  Horn–Johnson, *Matrix Analysis*, Ch.~6.2 (matrix exponential);
  Coxeter, *Regular Polytopes*, \S 22.7 ($600$-cell edge graph
  connectivity).

## 6. Section structure

1. **Recap and scope.** $(O1)$ as the second of four cascade-mechanism
   §3.4 obligations $(O0)$/$(O1)$/$(O2)$/$(O3)$; finite-$N$ vs.\
   inverse limit; explicit non-claims box matching §9 of this WO.
2. **The auxiliary block graph Laplacian $L_N^{\mathrm{block}}$.**
   Definition; relation to P4's $A_n$ and compat's $\widetilde A_n$
   (this is a *different* operator, introduced for the $(O1)$
   witness).
3. **Self-adjointness, PSD, operator-norm bound (clause 1).**
   Block-diagonal of standard scalar Laplacian; bound from Chung.
4. **Connectivity and kernel theorem (clause 2).**
   Induction from $V_{600}$; $\ker L_N^{\mathrm{block}} \cong F^0$
   via $\Psi_N$.
5. **Convergence theorem (clause 3).**
   Spectral theorem; $\lambda_+(L_N^{\mathrm{block}}) > 0$;
   $e^{-t L_N^{\mathrm{block}}} \to P_{\ker}$ with rate $\lambda_+$.
   Style cite to P4 `thm:flow-exists` for the finite-dim ODE
   argument; not a literal invocation. Notational warning:
   $\lambda_2(L_N^{\mathrm{block}}) = 0$ here because the kernel
   has dimension $32 > 1$; $\lambda_+$ is the smallest *positive*
   eigenvalue (the spectral gap).
6. **$W(H_4)$-fixed subspace count (clause 4).**
   Branchwise Coxeter action from P3 `def:coxeter`;
   $V_{H_4}^{W(H_4)} = \{0\}$ by irreducibility (Humphreys Ch.~2);
   $V_{D_4}, V_{16}, V_8$ fully fixed; $\dim = 28$.
7. **$(O0)$ verification and $(O1)$ witnessed discharge (clause 5).**
   $(O0)$: finite-dim Hilbert $X_N^{0, H_4}$, $C^1$ quadratic $R_N$,
   well-posed flow $e^{-t L_N^{\mathrm{block}}}$ — all immediate
   at finite $N$. $(O1)$: tuple $(\Phi_N, R_N, \Psi_N^t,
   \phi^\star_N, \phi_N^{(0)})$ verified against
   cascade-mechanism §3.4 lines 609–617.
8. **Worked numerics for $N = 0$.**
   $|V_0^{H_4}| = 120$, $|E_0^{H_4}| = 720$, $\Delta(G_0^{H_4}) = 12$
   (uniform), $\dim X_0^{0, H_4} = 120 \cdot 32 = 3840$,
   $\dim \ker L_0^{\mathrm{block}} = 32$,
   $\lambda_+(L^{\mathrm{cl}}_0) = 9 - 3\sqrt{5} \approx 2.2918$
   (from P2 `tab:P2-spectrum`),
   $\|L_0^{\mathrm{block}}\|_{\mathrm{op}} = 9 + 3\sqrt{5}
   \approx 15.708$ (largest eigenvalue from same table),
   $\dim_\R (F^0)^{W(H_4)} = 28$,
   $\dim_\R \Psi_0((F^0)^{W(H_4)}) = 28$. Sim verification
   optional (one-line numpy `linalg.eigvalsh` on the $120 \times
   120$ scalar Laplacian; multiplicities $1, 4, 9, 16, 25, 36,
   9, 16, 4$ from `tab:P2-spectrum`).
9. **What this paper does not do.**
   - **Single-state selection.** $\xi^*$ is freely chosen from
     $(F^0)^{W(H_4)} \setminus \{0\}$ (a $28$-dim cone); a single
     ray requires the named open hypothesis **(H-uniqueness)**
     (§7 below), which lies *outside* the cascade-closure
     consumer API.
   - **$(O0)$, $(O2)$, $(O3)$.** $(O0)$ is verified separately in
     §7 (immediate at finite $N$). $(O2)$ and $(O3)$ are not
     addressed; they remain in their current
     cascade-refinement-compat status.
   - **Inverse-limit $(O1)$.** Needs $(L3)$ spectral-gap
     propagation. Not addressed here.
   - **$D_4$ branch.** Separate paper if needed.
   - **$W(H_4)$-non-equivariant initial data.** Convergence still
     holds by clause (3), but the limit is in the full $32$-dim
     $\ker L_N^{\mathrm{block}}$, not the $28$-dim
     $\Psi_N((F^0)^{W(H_4)})$.
   - **Identification with P4's $A_n$ or compat's $\widetilde A_n$.**
     $L_N^{\mathrm{block}}$ is a *new* auxiliary operator;
     theorems do not transfer back.
   - **Continuum / target-side correspondence theorem.**
   - **Selection mechanism in the strong (philosophical) sense.**
     "Cascade closure as selection mechanism" is overstatement;
     this paper provides a top-rung $(O1)$ witness for a chosen
     $\xi^*$ on the $H_4$ branch at finite $N$, no more.
10. **Citation contract / handoff.**
    What downstream papers may cite (the witnessed $(O1)$ tuple
    for chosen $\xi^*$); what they may not (P4's actual
    closure-dynamics flow, single-state selection,
    inverse-limit, $D_4$-branch witness).

## 7. Named open hypotheses (carried forward, not discharged)

- **(H-uniqueness):** Selection of a single ray in
  $(F^0)^{W(H_4)} \setminus \{0\}$ requires structure beyond the
  cascade-closure flow. Candidates: closure-energy normalisation,
  an additional symmetry beyond $W(H_4)$ (e.g., time-reversal,
  $\sigma$ Galois action on the rationality data), a top-rung
  initial condition tied to a physical observable, or a
  thermodynamic / variational principle. **(H-uniqueness)** is
  named here, not discharged. Per cascade-mechanism §3.4 lines
  637–639, "selection of $\phi^\star_N$ itself is not provided
  by cascade closure and is the successor paper's own task" —
  this paper supplies *a* $\phi^\star_N$ (parametrised by
  $\xi^*$), not the unique one.

- **(H-physical-interpretation):** Whether
  $\Psi_N\bigl((F^0)^{W(H_4)}\bigr) \subset X_N^{0, H_4}$ is
  the *physically correct* selected subspace (vs.\ a mathematical
  artefact of restricting to the $H_4$ branch with the
  constant-function embedding) is a physical-modelling question
  outside this paper's scope.

## 8. Acceptance criteria

The WO is satisfied when:

- **A1.** A single named theorem with all five clauses (1)–(5)
  of §3 above appears in the .tex and is proved using only the
  inputs listed in §5 (no new analytic conjectures introduced).
  Clause (5) explicitly discharges only $(O1)$, not the four-part
  consumer API.
- **A2.** Sections 1–10 of §6 are present in the order listed.
- **A3.** Every cited P1/P2/P3/P4/compat/mechanism result uses
  label-form citation (\texttt{label} syntax), and no nonexistent
  labels (e.g.\ no `def:scaled-curvature`; use `def:Atilde`).
- **A4.** §1 contains an explicit non-claims box matching §9.
- **A5.** §7 (or its tex equivalent) names **(H-uniqueness)** and
  **(H-physical-interpretation)** as open hypotheses;
  **(H-uniqueness)** is explicitly tied to the freedom of $\xi^*$
  choice and to cascade-mechanism §3.4 lines 637–639.
- **A6.** The new operator $L_N^{\mathrm{block}}$ is defined in
  this paper (not imported); §2 of the .tex must clearly
  distinguish it from P4's $A_n$ and compat's $\widetilde A_n$
  with the explicit relation paragraph.
- **A7.** $\dim_\R (F^0)^{W(H_4)} = 28$ is proved using
  irreducibility of the $H_4$-reflection representation
  (\cite[Ch.~2]{Humphreys}), not asserted from P2 character data.
- **A8.** Worked-numerics §8 includes the $N = 0$ case with
  explicit values $|V_0^{H_4}| = 120$, $|E_0^{H_4}| = 720$,
  $\dim X_0^{0, H_4} = 3840$, $\dim \ker L_0^{\mathrm{block}}
  = 32$, and $\lambda_+ = 9 - 3\sqrt{5}$ from
  P2 `tab:P2-spectrum`. Sim is optional.
- **A9.** P4 `thm:flow-exists` is cited as *style*
  (same finite-dim ODE argument), not literally invoked for
  $L_N^{\mathrm{block}}$. P4 `prop:block-bounds` is *not* used
  for $\|L_N^{\mathrm{block}}\|_{\mathrm{op}}$; Chung Ch.~1 is.
- **A10.** Codex hostile-review on the .tex returns "Publication
  ready: yes" within 7 rounds.

## 9. Risks and contingencies

- **R1.** Reviewers may push back that $L_N^{\mathrm{block}}$ is
  *ad hoc* — defined just to make $(O1)$ work. Mitigation:
  honest framing in §2 and §10 of the .tex; citation-contract §10
  forbids transferring theorems to P4's $A_n$. Cascade-mechanism
  §3.4 explicitly allows the successor paper to *supply* $R_N$;
  there is no requirement that $R_N$ be P4's closure functional.
- **R2.** Reviewers may demand a single ray, not a $28$-dim
  freedom. Mitigation: cascade-mechanism §3.4 only requires *a*
  $\phi^\star_N$, not a unique one (lines 637–639 explicitly say
  selection is the successor paper's task). We supply one for
  each $\xi^*$ choice; single-ray selection is named as
  **(H-uniqueness)** out of scope.
- **R3.** Reviewers may demand $D_4$-branch coverage. Mitigation:
  state explicitly as a non-claim and as the next paper's task.
- **R4.** Class-(c) midpoint-midpoint edges may be needed for
  connectivity of $G_N^{H_4}$. Mitigation: examined in §4 of the
  .tex; class-(a) and (b) suffice (the inductive step uses only
  midpoint-to-endpoint and centroid-to-midpoint edges).
- **R5.** $\lambda_+(L^{\mathrm{cl}}_0) = 9 - 3\sqrt{5}$ from
  P2 `tab:P2-spectrum` should be cross-checked numerically.
  Mitigation: optional one-line numpy sim in §8 confirms.

## 10. Bundle and narrative implication

- If this paper lands publication-ready, the
  cascade-refinement-papers bundle becomes a **five-paper
  deposit**: P3 + P4 + compat + mechanism + selection-h4.
- The narrative claim shifts from *"API for cascade closure"* to
  *"API + worked $(O1)$ witness on the $H_4$ branch at finite $N$
  for chosen $\xi^* \in (F^0)^{W(H_4)} \setminus \{0\}$"*.
- The remaining open work for an inverse-limit $(O1)$ theorem is
  isolated to a single named hypothesis $(L3)$ spectral-gap
  propagation; the remaining open work for single-state selection
  is isolated to **(H-uniqueness)**, which lies *outside the
  cascade-closure consumer API* (it is a separate selection
  principle).
- This paper does **not** make "cascade closure as selection
  mechanism" a citable theorem. It makes "top-rung $(O1)$ witness
  for a chosen $\xi^*$ on the $H_4$ branch at finite $N$" a
  citable theorem. The narrative discipline matters.

## 11. Build pipeline

1. **WO codex review** on this v4 file (`scripts/review_wo.sh
   papers/cascade-selection-h4/WO-CSH4.md`) until WO converges
   ("Publication ready: yes" on the WO).
2. **Draft .tex** at
   `papers/cascade-selection-h4/cascade-selection-h4.tex`.
3. **Build** with `tectonic`.
4. **Hostile-review loop** on the .tex
   (`scripts/review_paper.sh ...`) until "Publication ready: yes."
5. **Bundle integration**: copy into
   `release-bundles/cascade-refinement-papers/papers/cascade-selection-h4/`
   and into the flat folder; update bundle README to describe
   the five-paper deposit.

---

**Frozen at v4: 2026-05-09. Codex pre-build review of v4 next.**

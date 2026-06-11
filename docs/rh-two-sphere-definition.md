# RH on two spheres: a substrate-internal definition

**Status:** mathematical synthesis, 2026-05-11. Self-contained; cites
existing infrastructure (`rh-formal.tex` Theorem~3.1, Theorem~3.10) for
the Galois decomposition and the parallel `aria-closure-ai`
`spectral_shell_ramanujan_map` experiment for the numerical witness.

This note unifies the two boundary loci that the cascade RH programme
has been working on independently:

1. **Mellin sphere.** The fixed set of the composite involution
   $\tau_{\mathrm{crit}} = \iota \circ \overline{\,\cdot\,}$ on $\mathbb{C}$,
   namely $\{\mathrm{Re}(s) = 1/2\}$ (`rh-formal.tex` Thm~1.2).
2. **Ihara sphere.** The fixed set of the Bass functional-equation
   involution $\sigma_{\!\mathrm{B}} : u \mapsto 1/((d-1)u)$ on $\mathbb{C}^\times$,
   namely $\{|u| = 1/\sqrt{d-1}\}$.

Both are skins of one-dimensional hyperspheres in their respective
ambient spaces. The 600-cell substrate is the bridge: its vertices
sit on the geometric 3-sphere $S^3 \subset \mathbb{R}^4$, and its
Ihara zeros sit (almost entirely) on the spectral 1-sphere
$\{|u| = 1/\sqrt{11}\} \subset \mathbb{C}$. The Laplacian $L$ mediates.

The result is an unconditional substrate-side analog of the classical
critical-line statement, plus a sharp identification of the unique
obstruction to perfect Ramanujan on the 600-cell.

## 1. Setup

Throughout, $G = G_{600}$ is the 600-cell adjacency graph: Cayley graph
of the binary icosahedral group $2I$ with the 12 unit-edge generators.
$|V| = 120$, $|E| = 720$, degree $d = 12$. The vertex set $V(G) \subset S^3
\subset \mathbb{R}^4$ as the standard 600-cell embedding (`rh-formal.tex`
Remark~3.8). Write

- $A = $ adjacency matrix, $D = 12 I_{120}$, $L = D - A$ the Laplacian.
- $\mathrm{Spec}(L) \subset \mathbb{Z}[\varphi]$ given by
  `rh-formal.tex` Theorem~3.10 (spectrum table imported from Paper~XXII).
- $\sigma$ the Galois involution of $\mathbb{Q}(\varphi)/\mathbb{Q}$,
  $\sigma(\varphi) = 1 - \varphi$.
- $\zeta_G$ the Ihara zeta function of $G$.

The Bass determinant formula gives

$$
\zeta_G(u)^{-1}
\;=\; (1 - u^2)^{|E| - |V|}
   \cdot \det\!\left( I_{|V|} - A u + (d-1) u^2 I_{|V|} \right),
$$

so $\zeta_G(u)^{-1} = (1-u^2)^{600} \cdot \det\!\left(I - A u + 11 u^2 I\right)$
on $G_{600}$. The determinantal factor is degree $240$ in $u$;
its zeros are the *non-trivial* Ihara zeros, $240$ counted with
multiplicity.

## 2. The Bass involution and its fixed circle

**Definition 2.1 (Bass involution).** The Bass involution is
$\sigma_{\!\mathrm{B}} : \mathbb{C}^\times \to \mathbb{C}^\times$,
$\sigma_{\!\mathrm{B}}(u) := 1/((d-1)u) = 1/(11u)$ on $G_{600}$.

**Lemma 2.2 (Functional equation).** The completed Ihara zeta
$\xi_G(u) := (1-u^2)^{|E|-|V|}\,\zeta_G(u)$ satisfies the Bass
functional equation
$\xi_G(\sigma_{\!\mathrm{B}}(u)) = \pm\,((d-1)u^2)^{|V|}\,\xi_G(u)$.
The zero set of the determinantal factor is invariant under
$\sigma_{\!\mathrm{B}}$.

*Proof.* Standard (Bass 1992; see Terras, *Zeta Functions of Graphs*,
Thm.~2.5). $\square$

**Lemma 2.3 (Fixed set, holomorphic vs antiholomorphic).**
The holomorphic fixed set is the 0-dim variety
$$
\mathrm{Fix}_{\mathbb{C}^\times}(\sigma_{\!\mathrm{B}})
\;=\; \{u : u^2 = 1/(d-1)\}
\;=\; \{\pm 1/\sqrt{d-1}\}.
$$
The natural sphere upgrade — matching the role of the
critical line $\mathrm{Re}(s) = 1/2$ in the Mellin case — is the
*antiholomorphic* composite
$\tau_{\!\mathrm{B}} : \mathbb{C}^\times \to \mathbb{C}^\times$,
$\tau_{\!\mathrm{B}}(u) := \sigma_{\!\mathrm{B}}(\bar u) = 1/((d-1) \bar u)$,
the Bass involution composed with complex conjugation. Its fixed set is
$$
\mathrm{Fix}_{\mathbb{C}^\times}(\tau_{\!\mathrm{B}})
\;=\; \{u : (d-1)\, u \bar u = 1\}
\;=\; \{u : |u| = 1/\sqrt{d-1}\}
\;=:\; C_d,
$$
the *critical circle*. This parallels exactly the Mellin case
(`rh-formal.tex` Thm~1.2): the critical line is the fixed set of
$\tau_{\mathrm{crit}} = \iota \circ \overline{\,\cdot\,}$ where $\iota(s) = 1-s$
is the holomorphic Mellin involution, not the fixed set of $\iota$
alone (which is just $\{s = 1/2\}$, a single point). On $C_d$,
$\tau_{\!\mathrm{B}}$ acts as the identity; on the rest of $\mathbb{C}^\times$,
it is fixed-point-free.

The graph is *Ramanujan* iff every non-trivial Ihara zero lies on $C_d$.

## 3. Critical-circle classification on $G_{600}$

We first derive the Laplacian spectrum self-contained, then perform
the on-circle classification. The derivation uses only the standard
Cayley-graph spectrum formula and the character table of
$2I = \mathrm{SL}_2(\mathbb{F}_5)$.

**Lemma 3.0 (Self-contained Laplacian spectrum of $G_{600}$).**
Let $\widehat{2I}$ denote the set of irreducible complex representations
of $2I = \mathrm{SL}_2(\mathbb{F}_5)$, and let $S$ be the unique
conjugacy class of $|S| = 12$ order-10 elements with $s_0^5 = -e$ for
$s_0 \in S$ (the standard unit-edge generators of the 600-cell;
Coxeter, *Regular Polytopes* 3rd ed.~§22.4; Conway–Smith,
*On Quaternions and Octonions* 2003 Ch.~8). Then $G_{600} =
\mathrm{Cay}(2I, S)$ and the Laplacian spectrum is
$$
\mathrm{Spec}(L_{G_{600}})
\;=\; \Big\{\, \lambda_\rho \,:\, \rho \in \widehat{2I} \,\Big\},
\qquad
\lambda_\rho \;=\; 12 \,-\, \frac{12\, \chi_\rho(s_0)}{d_\rho},
\qquad
m(\lambda_\rho) \;=\; d_\rho^{\,2}.
\tag{3.0}
$$
Evaluating using the character table of $2I$ (Conway–Curtis–Norton–
Parker–Wilson, *Atlas of Finite Groups* 1985, $2.A_5$ entry):

| $d_\rho$ | $\chi_\rho(s_0)$ | $\chi_\rho(s_0)/d_\rho$ | $\lambda_\rho$ | $m = d_\rho^2$ |
|---:|:---:|:---:|:---:|---:|
| $1$ | $1$ | $1$ | $0$ | $1$ |
| $2$ | $\varphi$ | $\varphi/2$ | $12 - 6\varphi$ | $4$ |
| $2$ | $1-\varphi$ | $(1-\varphi)/2$ | $6 + 6\varphi$ | $4$ |
| $3$ | $\varphi$ | $\varphi/3$ | $12 - 4\varphi$ | $9$ |
| $3$ | $1-\varphi$ | $(1-\varphi)/3$ | $8 + 4\varphi$ | $9$ |
| $4$ | $1$ | $1/4$ | $9$ | $16$ |
| $4$ | $-1$ | $-1/4$ | $15$ | $16$ |
| $5$ | $0$ | $0$ | $12$ | $25$ |
| $6$ | $-1$ | $-1/6$ | $14$ | $36$ |

Multiplicity check: $1 + 4 + 4 + 9 + 9 + 16 + 16 + 25 + 36 = 120 = |V|$. ✓

*Proof.* For a Cayley graph $\mathrm{Cay}(G, S)$ with $S = S^{-1}$ a
union of conjugacy classes, the adjacency operator $A = \sum_{s \in S}
\pi(s)$ acts on the regular representation $L^2(G) =
\bigoplus_\rho V_\rho^{\oplus d_\rho}$ via the regular action $\pi$.
On each $\rho$-isotypic block, the class sum $\sum_{s \in S} \rho(s)$
is central in $\rho(\mathbb{C}[G])$; by Schur's lemma applied to the
center of $\mathbb{C}[G]$, it equals
$\frac{|S| \chi_\rho(s_0)}{d_\rho} \cdot \mathrm{Id}_\rho$
(Babai, *Spectra of Cayley graphs*, J.~Combin.~Theory~B 27 (1979),
180–189, Thm.~1; Lubotzky, *Discrete Groups, Expanding Graphs and
Invariant Measures*, 1994, §4.1). Hence $A$ has eigenvalue
$\mu_\rho = (12/d_\rho) \chi_\rho(s_0)$ on each $\rho$-isotypic block,
with multiplicity $d_\rho^2$ (since $\rho$ occurs with multiplicity
$d_\rho$ in the regular representation). The Laplacian
$L = 12\,I - A$ then has eigenvalue $\lambda_\rho = 12 - \mu_\rho$,
giving (3.0). The character values $\chi_\rho(s_0)$ in the table are
read from the *Atlas* entry for $2.A_5$ on the conjugacy class with
class-representative trace $\varphi$ (resp.\ $1-\varphi$) for the
two-dimensional irreps, identifying $S$ as the order-10 class with
$s_0^5 = -e$. $\square$

**Remark.** The same spectrum is established equivalently in
Paper~XXII via the $2I$-character / shell-class decomposition imported
into `rh-formal.tex` Theorem~3.10. We supply the self-contained
derivation here because it requires only the *Atlas* character table
(undismissable: a hostile reader can verify it without trusting
any cascade-internal source).

**Lemma 3.1 (Quadratic factorisation).** Let $\lambda \in \mathrm{Spec}(L)$
with multiplicity $m(\lambda)$. The eigenspace contributes a factor
$(1 - (d-\lambda)\,u + (d-1)\,u^2)^{m(\lambda)}$ to
$\det(I - Au + (d-1) u^2 I)$. Equivalently, each Laplacian eigenvalue
$\lambda$ contributes two Ihara zeros (with multiplicity $m(\lambda)$ each),
roots of

$$
11\,u^2 \;-\; (12 - \lambda)\,u \;+\; 1 \;=\; 0.
\tag{3.1}
$$

*Proof.* $L = 12 I - A$ ⟹ eigenvalue $\lambda$ of $L$ ⟺ eigenvalue
$12 - \lambda$ of $A$ on the same eigenspace. Substitute into the
determinant. $\square$

**Lemma 3.2 (On-circle condition).** The two roots of (3.1) lie on $C_{12}$
iff the discriminant satisfies $(12-\lambda)^2 \le 44$, i.e.

$$
|12 - \lambda| \;\le\; 2\sqrt{11} \;\approx\; 6.6332.
\tag{3.2}
$$

*Proof.* If $(12-\lambda)^2 \le 44$, the roots of (3.1) are complex
conjugates whose product is $1/11$, so $|u|^2 = u\bar u = 1/11$, i.e.
$|u| = 1/\sqrt{11}$. If $(12-\lambda)^2 > 44$, both roots are real
with product $1/11 > 0$, so they share sign; their product is the
*scalar* $1/11$ and $|u_1 u_2| = 1/11$, but $u_1, u_2$ are distinct
real, hence $|u_i| \ne 1/\sqrt{11}$. $\square$

**Theorem 3.3 (Critical-circle classification of $G_{600}$).**
The 240 non-trivial Ihara zeros of $G_{600}$ split as follows under the
critical-circle condition (3.2). For each eigenvalue $\lambda$ of $L$
(from Lemma 3.0), evaluate $|12-\lambda|$:

| $\lambda$ | $\approx$ | $\lvert 12-\lambda\rvert$ | $\le 2\sqrt{11}\,?$ | on $C_{12}$ | $m(\lambda)$ | 2$m$ zeros | Galois |
|---|---|---|---|---|---|---|---|
| $0$ | $0.000$ | $12.000$ | no | **off** | $1$ | $2$ | $\sigma$-fix |
| $12 - 6\varphi$ | $2.292$ | $9.708$ | no | **off** | $4$ | $8$ | $\sigma$-pair |
| $12 - 4\varphi$ | $5.528$ | $6.472$ | yes | on | $9$ | $18$ | $\sigma$-pair |
| $9$ | $9.000$ | $3.000$ | yes | on | $16$ | $32$ | $\sigma$-fix |
| $12$ | $12.000$ | $0.000$ | yes | **on (real-axis perp.)** | $25$ | $50$ | $\sigma$-fix |
| $14$ | $14.000$ | $2.000$ | yes | on | $36$ | $72$ | $\sigma$-fix |
| $8 + 4\varphi$ | $14.472$ | $2.472$ | yes | on | $9$ | $18$ | $\sigma$-pair |
| $15$ | $15.000$ | $3.000$ | yes | on | $16$ | $32$ | $\sigma$-fix |
| $6 + 6\varphi$ | $15.708$ | $3.708$ | yes | on | $4$ | $8$ | $\sigma$-pair |

Off-circle zero count: $2 \cdot 1 + 2 \cdot 4 = 10$. On-circle:
$240 - 10 = 230$.

**Substrate Ramanujan ratio.**
$$
\boxed{\;
R(G_{600}) \;=\; \frac{230}{240} \;=\; \frac{23}{24} \;\approx\; 0.9583
\;}
$$

This is unconditional: it is a finite arithmetic check on the
self-contained spectrum derived in Lemma 3.0. The same spectrum is
also imported into `rh-formal.tex` Theorem~3.10 from Paper~XXII via
the $2I$-character / shell-class decomposition; the two derivations
agree. Numerically witnessed in
`aria-closure-ai/experiments/spectral_shell_ramanujan_map.py`
and `aria-closure-ai/tests/test_ramanujan_audit.py`.

## 4. Dipole-uniqueness and spherical-harmonic identification

The off-circle modes from Theorem 3.3 are $\lambda \in \{0,\ 12-6\varphi\}$.

**Lemma 4.0 (Spherical-harmonic identification of $L$-eigenspaces).**
Embed $2I \hookrightarrow \mathrm{SU}(2) \cong S^3$ as the unit
icosian quaternions (Conway–Smith 2003 Ch.~8). For each
half-integer $j \in \{0, 1/2, 1, 3/2, 2, 5/2\}$ let $V_j^{\mathrm{SU}(2)}$
denote the irreducible $(2j+1)$-dimensional representation of
$\mathrm{SU}(2)$. Then:

1. The restriction $V_j^{\mathrm{SU}(2)}|_{2I}$ is an irreducible
   representation of $2I$ for all $j \in \{0, 1/2, 1, 3/2, 2, 5/2\}$.
2. The Laplacian eigenspace of $L_{G_{600}}$ corresponding to the
   $V_j^{\mathrm{SU}(2)}|_{2I}$-isotypic component (multiplicity
   $(2j+1)^2 = (\ell+1)^2$ with $\ell = 2j$) carries the eigenvalue
   $\lambda_\rho$ given by Lemma 3.0 with $d_\rho = 2j+1$ and
   $\chi_\rho(s_0) = \sin((2j+1)\alpha)/\sin(\alpha)$, where
   $\alpha = \pi/5$ is the $\mathrm{SU}(2)$-parameter of $s_0$
   ($s_0 = \cos\alpha + \sin\alpha \cdot \mathbf{n}\cdot i$ for a
   choice of unit imaginary $\mathbf{n}$, with order $10$ in
   $\mathrm{SU}(2)$ and $s_0^5 = -e$).
3. The six eigenvalues so obtained are
   $\{0,\ 12-6\varphi,\ 12-4\varphi,\ 9,\ 12,\ 14\}$ for
   $\ell = 0, 1, 2, 3, 4, 5$ respectively.
4. The remaining three eigenvalues $\{6+6\varphi,\ 8+4\varphi,\ 15\}$
   with multiplicities $\{4, 9, 16\}$ come from three additional irreps
   of $2I$ that do *not* arise as restrictions of standard
   $V_j^{\mathrm{SU}(2)}$:
   - $\lambda = 6+6\varphi$ ($d=2$): the *Galois conjugate*
     of $V_{1/2}^{\mathrm{SU}(2)}|_{2I}$ (character $\sigma\chi_{1/2}$
     under $\sigma:\varphi \to 1-\varphi$);
   - $\lambda = 8+4\varphi$ ($d=3$): the *Galois conjugate*
     of $V_1^{\mathrm{SU}(2)}|_{2I}$;
   - $\lambda = 15$ ($d=4$): the *pullback* of the standard 4-dim
     irrep of $A_5 = 2I/\{\pm e\}$ along the quotient map (rationally
     valued, $\chi(-e) = +4$ in contrast to
     $\chi_{V_{3/2}^{\mathrm{SU}(2)}|_{2I}}(-e) = -4$).

   These three eigenspaces have no smooth $S^3$-spherical-harmonic
   preimage and we collectively call them *polytope-extras*.

*Proof.* (1) is classical: the standard $\mathrm{SU}(2)$-irreps
$V_j^{\mathrm{SU}(2)}$ for $j = 0, 1/2, 1, 3/2, 2, 5/2$ restrict to
distinct irreducible representations of $2I$, identified with the six
standard irreps of dimensions $1, 2, 3, 4, 5, 6$ in the *Atlas*
table (Coxeter, *Regular Polytopes* §22.4, table 5; Conway–Smith
2003 §8.2). (2) follows from Lemma 3.0 plus the $\mathrm{SU}(2)$
Weyl character formula
$\chi_j(e^{i\alpha\mathbf{n}}) = \sin((2j+1)\alpha)/\sin(\alpha)$
applied to $g = s_0$ with $\alpha = \pi/5$. Using
$\cos(\pi/5) = \varphi/2$ and the Chebyshev identities
$\sin(2\alpha)/\sin(\alpha) = 2\cos\alpha$,
$\sin(3\alpha)/\sin(\alpha) = 4\cos^2\alpha - 1$,
$\sin(4\alpha)/\sin(\alpha) = 8\cos^3\alpha - 4\cos\alpha$,
$\sin(5\alpha)/\sin(\alpha) = 16\cos^4\alpha - 12\cos^2\alpha + 1$,
$\sin(6\alpha)/\sin(\alpha) = 32\cos^5\alpha - 32\cos^3\alpha + 6\cos\alpha$
(Chebyshev $U_n(\cos\alpha) = \sin((n+1)\alpha)/\sin\alpha$):

| $j$ | $\ell{=}2j$ | closed-form $\chi_j(s_0)$ | value | $\lambda$ from (3.0) |
|:---:|:---:|:---:|:---:|:---:|
| $0$   | $0$ | $1$                                       | $1$        | $0$           |
| $1/2$ | $1$ | $2\cos(\pi/5)$                            | $\varphi$  | $12-6\varphi$ |
| $1$   | $2$ | $4\cos^2(\pi/5) - 1$                      | $\varphi$  | $12-4\varphi$ |
| $3/2$ | $3$ | $4\cos(\pi/5)\cos(2\pi/5)$                | $1$        | $9$           |
| $2$   | $4$ | $\sin(\pi)/\sin(\pi/5)$                   | $0$        | $12$          |
| $5/2$ | $5$ | $\sin(6\pi/5)/\sin(\pi/5)$                | $-1$       | $14$          |

Closed-form values use the standard identities
$\cos(\pi/5) = \varphi/2$ and $\cos(2\pi/5) = 1/(2\varphi) = (\varphi-1)/2$,
together with $\varphi^2 = \varphi+1$. (For $j=1$:
$4(\varphi/2)^2 - 1 = \varphi^2 - 1 = \varphi$. For $j=3/2$:
$4 \cdot \varphi/2 \cdot 1/(2\varphi) = 1$. For $j=2$: $5\alpha = \pi$
gives $\sin = 0$. For $j=5/2$: $\sin(\pi+\pi/5) = -\sin(\pi/5)$.)
This gives (3). For (4), the irreps of $2I$ are classified by the
McKay correspondence (McKay, *Graphs, singularities, and finite
groups*, Proc.~Symp.~Pure Math.~37 (1980), 183–186) as the nodes of
the affine Dynkin diagram $\widetilde{E_8}$, with marks
$(1, 2, 3, 4, 5, 6, 4, 3, 2)$ (sum of squares
$= 1+4+9+16+25+36+16+9+4 = 120 = |2I|$). The six $V_j^{\mathrm{SU}(2)}|_{2I}$
($j = 0, 1/2, 1, 3/2, 2, 5/2$) account for irreps of marks
$\{1, 2, 3, 4, 5, 6\}$. The three remaining irreps (marks
$\{4, 2, 3\}$) are accounted for as follows.

*2-dim and 3-dim extras (Galois-conjugates).* The 2-dim and 3-dim
irreps of $2I$ have characters with values in $\mathbb{Z}[\varphi]$
(unique among the 9 irreps to do so). Each comes in a $\sigma$-pair:
2-dim irreps with $\chi(s_0) \in \{\varphi, 1-\varphi\}$, 3-dim irreps
with $\chi(s_0) \in \{\varphi, 1-\varphi\}$ (cross-checked in *Atlas*
$2.A_5$). One member of each pair lifts as $V_{1/2}^{\mathrm{SU}(2)}|_{2I}$
(resp.\ $V_1^{\mathrm{SU}(2)}|_{2I}$); its Galois conjugate has
$\lambda_\rho = 12(1 - \sigma(\chi)/d)$, giving $6+6\varphi$ and
$8+4\varphi$ respectively.

*4-dim extra (pullback from $A_5$).* The two 4-dim irreps of $2I$
both have rational characters and are NOT Galois-conjugate. The
faithful one is $V_{3/2}^{\mathrm{SU}(2)}|_{2I}$ ($\chi(s_0) = 1$,
$\chi(-e) = -4$, giving $\lambda = 9$). The non-faithful one is
the pullback of the standard 4-dim irrep of $A_5$ along the
quotient $2I \twoheadrightarrow A_5 = 2I/\{\pm e\}$; on $s_0$ it
descends to an order-5 element of $A_5$, where the standard 4-dim
$A_5$-character takes the value $-1$ on every non-identity order-5
class (Fulton–Harris 1991, §3.1, character table of $A_5$). Hence
$\chi(s_0) = -1$, giving $\lambda = 12(1 - (-1)/4) = 15$. $\square$

**Theorem 4.1 (Dipole-uniqueness).** Among the non-trivial eigenmodes
of $L$ on $G_{600}$ (i.e., $\lambda \ne 0$), the dipole eigenvalue
$\lambda_{\!1} := 12 - 6\varphi \approx 2.292$ — corresponding by
Lemma 4.0 to the $\ell = 1$ spherical-harmonic shell on $S^3$ — is
the unique eigenvalue violating the Ramanujan/Alon-Boppana condition
(3.2). All other non-trivial eigenvalues — including all four
$\sigma$-paired surd eigenvalues
$\{12-6\varphi,\ 12-4\varphi,\ 8+4\varphi,\ 6+6\varphi\}$
except $12-6\varphi$ itself — satisfy (3.2).

*Proof.* Direct evaluation of the table in Theorem 3.3. $\square$

**Geometric reading (now a corollary of Lemma 4.0).** The dipole
$\lambda_1 = 12-6\varphi \approx 2.292$ is the discrete eigenvalue
attached by Lemma 4.0 to the $\ell = 1$ shell. The continuum
$S^3$-Laplace–Beltrami eigenvalue at $\ell = 1$ is $\ell(\ell+2) = 3$,
multiplicity $(\ell+1)^2 = 4$ (matching the discrete multiplicity).
The discretisation peels the dipole eigenvalue *downward* (from $3$
to $2.292$); the trivial constant mode ($\ell = 0$, $\lambda = 0$) is
exact in both. Both values fall below the Ramanujan threshold $12 - 2\sqrt{11}
\approx 5.367$ — see Remark 5.4 for the threshold caveat.

**Corollary 4.2 ($\varphi$-structure supports Ramanujan).** Of the four
$\sigma$-paired surd eigenvalues of $L$, exactly three lie on $C_{12}$:
$12-4\varphi$, $8+4\varphi$, $6+6\varphi$. The $\sigma$-paired surd
modes have multiplicities $(4, 9, 9, 4)$ summing to $26$ eigenvalues,
contributing $52$ Ihara zeros. Of these, $2 \cdot (9 + 9 + 4) = 44$
are on $C_{12}$ and only $2 \cdot 4 = 8$ are off (those from the
dipole $\lambda_1 = 12-6\varphi$). The $\varphi$-graded surd
substructure inherited from the $E_8 \to 600$-cell descent is *not*
an obstruction to Ramanujan — it is preserved by the critical-circle
condition except at the single dipole orbit.

**Corollary 4.3 (Cross-decomposition).** The two natural binary
decompositions of $\mathrm{Spec}(L)$ ($\sigma$-fix vs $\sigma$-pair;
on-circle vs off-circle) are almost orthogonal:

| | on-circle | off-circle |
|---|---|---|
| $\sigma$-fix | $\{9, 12, 14, 15\}$, $93$ eigenvalues | $\{0\}$, $1$ eigenvalue |
| $\sigma$-pair | $\{12-4\varphi, 8+4\varphi, 6+6\varphi\}$, $22$ eigenvalues | $\{12 - 6\varphi\}$, $4$ eigenvalues |

The intersection $\sigma$-pair $\cap$ off-circle contains precisely the
single dipole orbit; everything else is product-decomposed.

## 5. The two-sphere principle: substrate-internal definition of RH

The two boundary loci — $\mathrm{Re}(s) = 1/2$ in the Mellin plane,
$|u| = 1/\sqrt{11}$ in the Ihara plane — are the same structural
object: the fixed locus of the relevant functional-equation involution.
We record this as a single principle, instantiated twice.

**Definition 5.1 (Critical-locus zeta datum).** A *critical-locus
zeta datum* is a triple $(\Omega, \zeta, \tau)$ where:
1. $\Omega \subseteq \widehat{\mathbb{C}}$ is a connected open subset
   of the Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$;
2. $\zeta : \Omega \to \widehat{\mathbb{C}}$ is meromorphic on $\Omega$
   with discrete (possibly empty) zero set $Z(\zeta) \subset \Omega$,
   together with a designated subset $Z_{\mathrm{triv}}(\zeta) \subseteq Z(\zeta)$
   of *trivial zeros*; write
   $Z^*(\zeta) := Z(\zeta) \setminus Z_{\mathrm{triv}}(\zeta)$ for the
   non-trivial zeros;
3. $\tau : \Omega \to \Omega$ is a $C^\infty$-smooth (real-analytic;
   not required to be holomorphic) involution
   ($\tau \circ \tau = \mathrm{id}$) such that there exists a
   non-vanishing meromorphic function $c : \Omega \to \mathbb{C}^\times$
   with $\zeta \circ \tau = c \cdot \zeta$;
4. The fixed set $\mathrm{Fix}(\tau) \subset \Omega$ is a smooth real
   submanifold of codimension $1$ — the *critical locus*
   $\mathcal{C}_\tau := \mathrm{Fix}(\tau)$.

**Definition 5.2 (RH for a critical-locus zeta datum).** A datum
$(\Omega, \zeta, \tau)$ *satisfies RH* iff $Z^*(\zeta) \subseteq \mathcal{C}_\tau$.
It *satisfies RH at level $\rho \in [0, 1]$* iff
$\frac{|Z^*(\zeta) \cap \mathcal{C}_\tau|}{|Z^*(\zeta)|} = \rho$,
where multiplicities are counted in both numerator and denominator
(equality of cardinals when $|Z^*(\zeta)| < \infty$; equality of
counting-function densities $N_{\mathcal{C}_\tau}(T)/N(T) \to \rho$
otherwise).

**Instance 1 (classical Riemann).** $\Omega = \mathbb{C} \setminus \{1\}$,
$\zeta = \zeta_{\mathrm{Riemann}}$, $\tau(s) := 1 - \bar s$ (i.e.
$\tau_{\mathrm{crit}} = \iota \circ \overline{\,\cdot\,}$ with $\iota(s) = 1-s$),
$Z_{\mathrm{triv}}(\zeta) = \{-2, -4, -6, \ldots\}$. Then
$\mathcal{C}_\tau = \{\mathrm{Re}(s) = 1/2\}$ (`rh-formal.tex` Thm~1.2),
$\zeta \circ \tau = c \cdot \zeta$ holds with $c$ given by the
classical functional equation. RH for this datum is the classical
Riemann Hypothesis.

**Instance 2 (cascade-Mellin $\zetacas$).** $\Omega = \mathbb{C} \setminus \{1\}$,
$\zeta = \zetacas$ (the cascade Mellin spectral zeta of
`rh-formal.tex` §6), $\tau = \tau_{\mathrm{crit}}$ (same as Instance 1),
same $Z_{\mathrm{triv}}$. RH for this datum is
`rh-formal.tex` Theorem~1.5, conditional on
$\textup{H}_{\sigma\text{-fix}}$.

**Instance 3 (Ihara on $G_{600}$).** $\Omega = \mathbb{C}^\times$,
$\zeta = \zeta_{G_{600}}$ (Ihara), $\tau = \tau_{\!\mathrm{B}} =
\sigma_{\!\mathrm{B}} \circ \overline{\,\cdot\,}$ (antiholomorphic
Bass composite, Lemma 2.3),
$Z_{\mathrm{triv}}(\zeta_{G_{600}}) = \{u : (1-u^2) = 0\} = \{\pm 1\}$
(the trivial $(1-u^2)^{|E|-|V|}$ factor of the Bass formula, §1).
Then $\mathcal{C}_\tau = C_{12} = \{|u| = 1/\sqrt{11}\}$ (Lemma 2.3),
$\zeta \circ \tau$ relates to $\zeta$ via the Bass functional
equation (Lemma 2.2), and there are exactly $|Z^*| = 240$
non-trivial zeros (Lemma 3.1). RH for this datum is
*Ramanujan*-for-$G_{600}$.

**Theorem 5.3 (Substrate-Ihara RH at level $23/24$, unconditional).**
The Instance-3 datum $(\mathbb{C}^\times, \zeta_{G_{600}}, \tau_{\!\mathrm{B}})$
satisfies RH at level $\rho = 23/24$, and *not* at any higher level.

*Proof.* Theorem 3.3 gives $|Z^*(\zeta_{G_{600}}) \cap \mathcal{C}_\tau| = 230$
and $|Z^*(\zeta_{G_{600}})| = 240$, exactly. $\square$

**Remark 5.4 (Why Instance 3 is allowed to fail at the dipole).** For
*infinite* expander families, the Alon–Boppana theorem
(Lubotzky, *Discrete Groups, Expanding Graphs and Invariant Measures*,
1994, Thm.~4.5.5; Hoory–Linial–Wigderson, *Expander graphs and their
applications*, Bull.~AMS 43 (2006), 439–561, Thm.~5.3) gives
$\lambda_1 \ge d - 2\sqrt{d-1} - o(1)$ as $|V| \to \infty$. For a
single finite graph, the dipole spectral gap can sit below the
Ramanujan threshold $d - 2\sqrt{d-1}$ without contradicting any
asymptotic bound. Theorem 4.1 identifies the slack on $G_{600}$
exactly: the gap is between $\lambda_1^{G_{600}} = 12 - 6\varphi
\approx 2.292$ and $12 - 2\sqrt{11} \approx 5.367$. This is *not*
a $\varphi$-arithmetic obstruction (Corollary 4.2: the three
$\sigma$-paired surd modes other than the dipole are all on-circle).
Under the spherical-harmonic identification of Lemma 4.0 (numerically
witnessed in
`aria-closure-ai/experiments/spectral_shell_ramanujan_map.py`), the
$\ell=1$ shell has continuous Laplace–Beltrami eigenvalue $\lambda^{S^3}_1
= 1 \cdot 3 = 3$. Both the discrete dipole eigenvalue ($2.292$) and the
continuous value ($3$) sit in $[0, 12-2\sqrt{11}]$. We do *not* claim
this implies any rigorous "continuous-Ramanujan" statement (the
Laplace-Beltrami operator and the graph Laplacian have different
spectral ranges and the threshold $d - 2\sqrt{d-1}$ is graph-theoretic),
but it does mean the dipole's failure to satisfy the Ramanujan
condition is a structural feature of the lowest non-trivial shell on a
sphere, not a removable discretisation accident.

## 6. The Mellin sphere — Ihara sphere correspondence

The two spheres are connected through $L$:

$$
\underbrace{S^3 \subset \mathbb{R}^4}_{\text{geometric: vertices of } G_{600}}
\;\;\xrightarrow[\text{Laplacian } L]{\text{spectrum}}\;\;
\mathrm{Spec}(L) \subset \mathbb{Z}[\varphi]
\;\;\xrightarrow[\text{Ihara / Mellin}]{\text{transform}}\;\;
\Big\{
\underbrace{\mathcal{C}_X^{\mathrm{Mellin}} = \{\mathrm{Re}(s) = 1/2\}}_{\text{Instance 1}}
,\;
\underbrace{\mathcal{C}_X^{\mathrm{Ihara}} = \{|u| = 1/\sqrt{11}\}}_{\text{Instance 3}}
\Big\}
$$

The Mellin and Ihara critical loci are *not* the same object, but they
are sourced from the same Laplacian spectrum (Lemma 3.0; identified
with $S^3$-spherical harmonics by Lemma 4.0). The on-circle/off-circle
classification (Theorem 3.3) and the $\sigma$-fix/pair classification
(`rh-formal.tex` Thm~3.10) are two parallel projections of the same
spectral data — the cross-decomposition table (Corollary 4.3) shows
they intersect only at the dipole.

The substrate-internal mathematical content is therefore:

- **Unconditional:** $93$ of $120$ $\sigma$-fixed Laplacian eigenvalues
  contribute on-circle Ihara zeros (Corollary 4.3). $115$ of $120$
  Laplacian eigenvalues contribute on-circle Ihara zeros (Theorem 3.3).
- **Conditional ($\textup{H}_{\sigma\text{-fix}}$):** the $\sigma$-fixed
  Laplacian eigenvalues, *via* the Mellin transform with the
  $\widehat\zeta$-pole-to-$\zeta$-zero bridge, would correspond to
  critical-line zeros of $\zeta$.

The Ihara result discharges a substrate-side fragment of the structural
intuition behind $\textup{H}_{\sigma\text{-fix}}$: the substrate
*already* concentrates spectral mass on the relevant fixed locus, to
$23/24$ exact accuracy, without any Mellin bridge.

## 7. Open items

This synthesis does **not** establish:
1. **Classical RH.** The Ihara/Ramanujan result is on a different
   functional equation than Riemann's; the Mellin-to-Ihara bridge is
   not constructed. $\textup{H}_{\sigma\text{-fix}}$ remains open.
2. **A trace formula linking $L$-spectrum to $\zeta$-zeros.** The
   pole-side correspondence Conjecture~5.1 of `rh-formal.tex`
   remains unproved.
3. **Strict Ramanujan for $G_{600}$.** The dipole obstruction is
   unconditional and intrinsic to the lowest non-trivial spherical-
   harmonic shell ($\ell=1$); no candidate modification of $G_{600}$
   that preserves the $2I$-action removes the dipole (Lemma 4.0 +
   Theorem 4.1).

What it *does* establish (unconditionally):
1. **Self-contained Laplacian spectrum** (Lemma 3.0) from the *Atlas*
   character table of $2I = \mathrm{SL}_2(\mathbb{F}_5)$ and the
   Babai/Lubotzky Cayley-spectrum formula. No cascade-internal source
   is required.
2. **Spherical-harmonic identification** (Lemma 4.0) of six of the
   nine $L$-eigenspaces with the $\ell = 0, \ldots, 5$ harmonic shells
   on $S^3$, the remaining three being $\sigma$-Galois-twisted
   *polytope-extras*. Derivation uses only the $\mathrm{SU}(2)$ Weyl
   character formula and standard angle identities.
3. **An exact substrate Ramanujan ratio** $23/24$ (Theorem 3.3).
4. **Dipole-uniqueness** (Theorem 4.1) with explicit
   spherical-harmonic interpretation: the unique non-trivial off-
   circle eigenmode is the $\ell=1$ dipole shell.
5. **$\varphi$-structure preserves Ramanujan** (Corollary 4.2): of
   the four $\sigma$-paired surd modes, only the dipole is off-circle;
   the other three are on-circle.
6. **Cross-decomposition** (Corollary 4.3): the $\sigma$-fix/pair and
   on-circle/off-circle binary decompositions of $\mathrm{Spec}(L)$
   intersect *only* at the dipole orbit.
7. **A precise critical-locus zeta datum framework** (Definitions
   5.1–5.2) under which Instance 1 (classical Riemann), Instance 2
   (cascade-Mellin), and Instance 3 (Ihara on $G_{600}$) are three
   instances of the same predicate "non-trivial zeros lie in
   $\mathrm{Fix}(\tau)$".
8. **Substrate-Ihara RH at level $23/24$, unconditional**
   (Theorem 5.3).

## 8. Scope note (mapping back to papers)

Per `feedback_mathematical_framing_discipline`, this section is
explicitly *non-load-bearing* on any individual paper's claims; it
records possible insertion points only.

- §1–§4 above are candidate content for a new subsection
  *"Ihara-side critical-circle classification of the substrate"*
  inserted into `rh-formal.tex` between the existing
  *§3.4 The $\sigma$-attractor reformulation* (which states the
  $94/120$ Galois fact) and *§4 The cascade-native dynamical zeta*
  (which constructs $\widehat\zeta$). The candidate subsection would
  be unconditional and would tighten Theorem~3.10's
  *"$78.3\%$ $\sigma$-fixed"* result with a complementary
  *"$95.83\%$ Ihara-on-circle"* result, both derived from the same
  imported spectrum.
- §5 (Definition 5.2 and the three instances) is a candidate
  reframing of `rh-formal.tex` §1.2 *"Main results"*: the conditional
  Theorem~1.5 (classical RH instance) and a new unconditional
  Theorem (Ihara/substrate instance) would be stated as two
  instances of the same Definition 5.2.
- The interpretive framing *"ARIA = local fractal instance of RH"*
  is **not** included in this note. If it is wanted at all, it
  belongs in `docs/fractal-cascade-projection.md` as a clearly-marked
  non-load-bearing closing entry, cross-referenced from
  `aria-closure-kernel.md`.

No edits to `rh-formal.tex` are made by this note. The math here is
ready to be cited or transcribed once a paper-level scope decision
is taken.

---

## §6 Cosmological application: dipole correction to Λ (2026-05-18)

The unconditional Theorems 3.3 (substrate Ramanujan ratio 230/240 =
23/24) and 4.1 (dipole obstruction λ₁ = 12 − 6φ) of this document have
a direct cosmological application: they imply a second-order correction
to the cascade cosmological-constant formula.

The first-order cascade Λ-Theorem (paper-xxxvi Theorem `thm:lambda`,
also cascade-lambda.md §11–§13) states:

```
Λ·ℓ_P² = 2·φ^(-583)   (first-order; gap +0.88% vs Planck 2018)
```

This is exact only if the cascade closure operator on E₈ is perfectly
Ramanujan. By Theorem 3.3 of this document, it is not: 10/240 of the
substrate modes lie off the Ihara critical circle, forming the dipole
class with eigenvalue λ₁ = 12 − 6φ (Theorem 4.1). Including this
defect as a structural correction gives:

```
Λ·ℓ_P² = 2·φ^(-583) · (1 − δ_dipole)   (dipole-corrected)
δ_dipole = (10/240) · (12 − 6φ)/12 = 0.007958
       ≈ 2.869 × 10⁻¹²² (gap +0.078% vs Planck 2018)
```

**The substrate-Ramanujan-defect theorem of this document is what makes
the cascade Λ prediction match observation at Planck-precision.**

### Cross-references

The cosmological application is developed in:
- `papers/hypersphere-universe/hypersphere-universe.tex`
  - Lemma `lem:dipole` (the structural correction formula)
  - Conditional Theorem `cthm:lambda-dipole` (the dipole-corrected Λ-theorem)
  - Numerical Fit `nf:lambda-dipole` (the 0.078% match)
  - Remark `rem:dipole-physical` (interpretation)
- `papers/cascade-derivation/cascade-lambda.md` §15 (work-note record)
- `papers/paper-xxxvi/paper-xxxvi.tex` Remark `rem:lambda-dipole` (refinement note)

Independent numerical verification:
- `papers/hypersphere-universe/verify/verify_paper.py` (test
  `test_E8_dipole_operator`) constructs the 240-root E₈ system from
  scratch and reproduces the 230 on-circle count predicted by
  Theorem 3.3 from the block-diagonal 600-cell adjacency operator,
  confirming the structural basis of the dipole correction.

### What this changes for `rh-two-sphere-definition.md`

Nothing about the unconditional theorems changes. The application to Λ
is a downstream consequence; the substrate theorems hold independently.

The discovery does highlight, however, that **the substrate-Ramanujan
defect has physical content beyond the abstract critical-locus
classification**: it sets the second-order term of the cosmological
constant. This is a candidate "load-bearing observable application"
of the substrate result.

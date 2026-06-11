# The Rung Dimension Ladder: One Arena, Many Resolutions, and the Intertwiner Theorem

**Status:** mathematical derivation, 2026-06-10; **all five §7 open items closed/reduced 2026-06-11**. Extends the spectral-dimension theorem of `docs/rendering-layer.md` §2 across the cascade rungs and proves the **intertwiner theorem**: each rung's harmonic eigenspaces are literally the continuum $S^3$ (resp. $S^7$) harmonics sampled on the rung's vertex set, and the coarse rungs' fields are the fine rung's fields sampled on nested sub-polytopes. Answers, at theorem grade where possible, the question "how does the spectrum layer into dimensional spaces, and what is hidden beside the 3D perspective." Mathematical content; an Informal reading is a single non-load-bearing closing subsection per `feedback_mathematical_framing_discipline`.

**Sim verification:** `scripts/verify_rung_dimension_ladder.py` — **25/25 PASS** (core, 2026-06-10); `scripts/verify_ladder_completion.py` — **29/29 PASS** (opens closure, 2026-06-11). All residuals at machine precision ($\sim 10^{-15}$). First-pass exploration in `scripts/explore_rung_dimension_ladder.py`.

## 1. Position

`docs/rendering-layer.md` §2 proved for the H4 rung that the substrate spectrum knows the dimension of its arena (square multiplicities, exact dispersion, Weyl $d = 3.09$). The cascade has further rungs with their own substrates (`docs/glossary.md`): the 24-cell at the D4/gravity rung, the tesseract at the 16/information rung, the octonion/E8 lattice at the observer rung. Three questions arise:

1. Does the spectral-dimension law hold rung by rung? **Yes — exactly (§3–§4).**
2. Are the rungs' arenas different spaces, or one space at different resolutions? **The quaternionic rungs sample ONE $S^3$ at decreasing resolution; the octonionic rung changes arena to $S^7$ (§3, §5).**
3. What plays the role of "dimensions hidden beside the 3D perspective"? **Three precise structures: the folded spectral sectors (§4), the $S^7$ arena (§5), and (from prior work) the Galois twin — not a haze of extra universes (§6).**

## 2. Rung substrates and nesting

**Definition 2.1 (Rung vertex sets).** On the unit sphere of the relevant division algebra:

- $V_{120} = 2I$ — the 120 unit icosians (H4 rung), edges at $\langle v,w\rangle = \varphi/2$, degree 12, $\theta = \pi/5$.
- $V_{24} = 2T$ — the 24 Hurwitz units (D4 rung), edges at $\langle v,w\rangle = 1/2$, degree 8, $\theta = \pi/3$.
- $V_{16}$ — the 16 half-integer units $(\pm 1 \pm i \pm j \pm k)/2$ (16 rung, tesseract), edges at $\langle v,w\rangle = 1/2$, degree 4, $\theta = \pi/3$.
- $V_{240}$ — the 240 unit octavians (E8 roots normalised to $S^7 \subset \mathbb O$; 8/E8 rung), edges at $\langle v,w\rangle = 1/2$, degree 56.

**Lemma 2.2 (Nesting).** $V_{16} \subset V_{24} \subset V_{120}$ as point sets on $S^3$.

**Proof.** $2T \subset 2I$ is the standard binary lift of $A_4 \subset A_5$; in icosian coordinates the Hurwitz units are among the 120 icosians. For the tesseract: with $\omega = (1+i+j+k)/2 \in 2T$ (order 6), the coset decomposition $2T = Q_8 \sqcup \omega Q_8 \sqcup \omega^2 Q_8$ exhibits $V_{16} = \omega Q_8 \sqcup \omega^2 Q_8$ — the two non-trivial cosets of the quaternion group — which are exactly the 16 half-integer units. (Note $V_{16}$ is a union of cosets, **not** a subgroup: $16 \nmid 24$.) Verified in coordinates (sim L1a, L1b: every $V_{24}$ vertex is a $V_{120}$ vertex of the canonical `600cell_data.npz`; every $V_{16}$ vertex is a $V_{24}$ vertex). $\square$

So three rungs literally sample the *same* 3-sphere, at 120, 24, and 16 points. The remaining question is whether their spectral structure respects the sampling. It does, exactly:

## 3. The intertwiner theorem

**Definition 3.1 (Restriction map).** For a rung vertex set $X \subset S^{n-1}$ and harmonic level $k$, let $\mathrm{res}_k : H_k(S^{n-1}) \to \mathbb R^X$ be the restriction of degree-$k$ spherical harmonics to $X$. (Numerically realised by zonal kernels: $U_k(\langle \cdot, y\rangle)$ on $S^3$ — the Chebyshev-U / $SU(2)$ character kernel — and $C_k^{(3)}(\langle\cdot, y\rangle)$ on $S^7$ — the Gegenbauer kernel — over sufficiently many directions $y$; by the addition theorem these span $\mathrm{res}_k(H_k)$.)

**Theorem 3.2 (Class-sum intertwiner — group rungs).** Let $G \subset SU(2)$ be a finite subgroup ($2I$ or $2T$), $S \subset G$ a connecting set that is a single conjugacy class of common rotation half-angle $\theta$, closed under inversion, and $A$ the Cayley adjacency on $X = G$. If $V_k|_G$ is irreducible, then

$$A \circ \mathrm{res}_k \;=\; a_k\, \mathrm{res}_k, \qquad a_k \;=\; |S|\,\frac{\sin((k+1)\theta)}{(k+1)\sin\theta},$$

and $\mathrm{res}_k$ is injective ($\mathrm{rank} = (k+1)^2$). Hence the rung Laplacian eigenspace at $\lambda_k = |S| - a_k$ **is** $\mathrm{res}_k(H_k(S^3))$ — the sampled continuum harmonics — with the dispersion relation of `rendering-layer.md` Theorem 2.3 as the eigenvalue law.

**Proof.** $H_k(S^3)$ is the span of matrix coefficients $h(g) = \langle u, V_k(g)\, w\rangle$ of the $SU(2)$ irrep $V_k$. For the class sum, $(A\,\mathrm{res}_k h)(g) = \sum_{s \in S} h(sg) = \langle u, V_k(\Sigma_S)\, V_k(g) w\rangle$ where $\Sigma_S = \sum_{s\in S} V_k(s)$. Since $S$ is a conjugacy class of $G$, $\Sigma_S$ is central in the image of $G$; if $V_k|_G$ is irreducible, Schur's lemma gives $\Sigma_S = \frac{|S|\,\chi_{V_k}(s)}{k+1}\,\mathrm{Id}$, and since every $s \in S$ has $SU(2)$ rotation half-angle $\theta$, $\chi_{V_k}(s) = \sin((k+1)\theta)/\sin\theta$. This proves the scalar action. Injectivity: matrix coefficients of a single irreducible $G$-representation are linearly independent in $L^2(G)$ (Peter–Weyl orthogonality), so $\mathrm{rank}\,\mathrm{res}_k = (\dim V_k)^2 = (k+1)^2$. If $V_k|_G$ is *reducible*, $\Sigma_S$ acts with a distinct scalar on each irreducible component, and $\mathrm{res}_k$ splits across eigenblocks — the **fold** mechanism of §4. $\square$

**Sim (L2).** Exact for $V_{120}$ at $k = 0..5$ (ranks $1, 4, 9, 16, 25, 36$; action and containment residuals $\sim 10^{-15}$) and for $V_{24}$ at $k = 0..2$ (ranks $1, 4, 9$ at $\lambda = 0, 4, 8$). PASS.

**Hypothesis check (the irreducibility of $V_k|_G$, demanded by the codex review).** The scalar action requires $V_k|_{2I}$ to be irreducible for $k \le 5$ — otherwise $\Sigma_S$ acts with several scalars and the block splits. This is now verified independently of the spectrum: computing $\langle\chi_{V_k},\chi_{V_k}\rangle_{2I} = \tfrac1{120}\sum_{\text{classes}} |C|\,\chi_{V_k}(\theta_C)^2$ over the 9 conjugacy classes of $2I$ gives **exactly 1 for every $k=0..5$** (sim `verify_gap_strengthening.py` SR1), so each $V_k|_{2I}$ is irreducible and Theorem 3.2 applies. The branching $V_6 = 3'\oplus4'$ etc. (the fold of §4) begins exactly at $k=6$, consistent with the design-strength cutoff (Theorem 3.4).

**Proposition 3.3 (Two-point-homogeneous rungs — tesseract and E8).** For $X = V_{16}$ (symmetry $B_4$, distance-transitive) and $X = V_{240}$ (symmetry $W(E_8)$, transitive on pairs of fixed inner product), the same conclusions hold with the zonal scalar of the relevant sphere: on $S^3$, $a_k = \deg \cdot \frac{\sin((k+1)\theta)}{(k+1)\sin\theta}$; on $S^7$,

$$a_k \;=\; 56\,\frac{C_k^{(3)}(1/2)}{C_k^{(3)}(1)}, \qquad \lambda_k = 56 - a_k \;=\; 28,\ 48,\ 58,\ 60 \quad (k = 1, 2, 3, 4).$$

**Proof sketch.** By the addition theorem, the operator $Z_k$ on $\mathbb R^X$ with kernel $C_k^{(\alpha)}(\langle x, y\rangle)$ equals $\mathrm{res}_k\,\mathrm{res}_k^{\!*} \succeq 0$, with image $\mathrm{res}_k(H_k)$. Two-point homogeneity (the symmetry group is transitive on ordered vertex pairs at each inner product) makes $\sum_{w :\, \langle x, w\rangle = c} C_k(\langle w, y\rangle)$ a function of $\langle x, y\rangle$ alone, so the adjacency $A$ preserves each $\mathrm{im}\,Z_k$ and acts there by the zonal scalar (Delsarte–Goethals–Seidel association-scheme theory). Full formalisation is Open 7.1; the numerics are machine-exact (sim L2 tesseract, L3 E8: ranks $8, 35, 112$ injective for $k \le 3$, all residuals $\sim 10^{-14}$). $\square$

**Theorem 3.4 (Injectivity cutoff = design strength).** Let $X$ be a spherical $t$-design on $S^{n-1}$. Then $\mathrm{res}_k$ is injective for all $k \le \lfloor t/2 \rfloor$. The four rung substrates have known design strengths, and the cutoffs match **exactly**:

| Rung | $t$-design strength | $\lfloor t/2\rfloor$ | observed $k_{\max}$ |
|---|---|---|---|
| $V_{120}$ (600-cell) | 11 | 5 | **5** |
| $V_{24}$ (24-cell) | 5 | 2 | **2** |
| $V_{16}$ (tesseract) | 3 | 1 | **1** |
| $V_{240}$ (E8 roots) | 7 | 3 | **3** |

**Proof.** For $h, h' \in H_k$, the product $hh'$ is a polynomial of degree $2k \le t$, so the $t$-design property gives $\sum_{x \in X} h(x)h'(x) = |X|\int_{S^{n-1}} h h'$. The Gram matrix of $\mathrm{res}_k$ on any basis of $H_k$ therefore equals $|X|$ times the continuum Gram matrix, which is positive-definite; hence $\mathrm{res}_k$ is injective. Sharpness (no rung exceeds its bound) is exhibited by the fold/kernel mechanisms of §4 at $k_{\max} + 1$ in each case. Design strengths: 600-cell vertices form an 11-design and the 24-cell a 5-design (classical, $H_4$/$F_4$ orbit cubature); the 4-cube a 3-design; the E8 root shell a 7-design (Venkov). $\square$

**Theorem 3.5 (One arena, many resolutions — nested sampling).** For $k \le 2$: the restriction of the $V_{120}$ harmonic eigenspace at $\lambda_k^{(120)}$ to the 24 sub-vertices **equals** the $V_{24}$ harmonic eigenspace at $\lambda_k^{(24)}$; likewise $V_{24} \to V_{16}$ for $k \le 1$. The eigen*values* change (each rung has its own dispersion: $\lambda_1 = 2.29, 4, 2$); the eigen*spaces* are samplings of the same continuum harmonics.

**Proof.** Transitivity of restriction: $\mathrm{res}^{X \to Y} \circ \mathrm{res}_k^{S^3 \to X} = \mathrm{res}_k^{S^3 \to Y}$ for $Y \subset X$, plus Theorem 3.2 applied at each rung, plus injectivity at both ends (Theorem 3.4). Sim L4: ranks and containments exact at $10^{-15}$. $\square$

**Reading.** Theorem 3.5 makes cross-rung coupling *literal*: a gravity-rung (D4) field configuration is a quantum-rung (H4) field configuration evaluated on the 24 shared vertices — same harmonic content, lower cutoff, different propagation constant. The cascade fan, restricted to its quaternionic rungs, is a **resolution ladder for a single 3-dimensional arena**, now at theorem grade.

## 4. The two hiding mechanisms: fold and kernel

Each rung's function space splits into a *resolved* part (the harmonic chain, expressible as fields on the arena) and a *hidden* part — invisible to the geometric ladder. There are exactly two mechanisms, and both are now demonstrated:

**Proposition 4.1 (Fold: irrep splitting).** When $V_k|_G$ is reducible, $\mathrm{res}_k$ splits across eigenblocks with distinct scalars (Theorem 3.2, last clause). Demonstration on $V_{120}$ at $k = 6$: $V_6|_{2I} = 3' \oplus 4'$ (McKay), and $\mathrm{res}_6$ has rank $25 = 9 + 16$ landing inside the primed blocks $\lambda = 14.4721$ ($3'$) and $15.0000$ ($4'$) — sim L5a, exact. The $49$-dimensional $H_6$ aliases with $24$ dimensions of kernel onto the folded sector.

**Proposition 4.2 (Kernel: sparse sampling).** Harmonics can vanish identically on the sample set. Demonstration on $V_{16}$ at $k = 2$: all tesseract coordinates satisfy $x_i^2 = 1/4$, so the three harmonics $x_i^2 - x_j^2$ restrict to zero (sim L5c, exact); $\mathrm{res}_2$ has rank $6$ (the $x_i x_j$ survive), landing in the $\lambda = 4$ block — still at the eigenvalue the dispersion formula predicts ($a_2 = 0$; sim L5b). 

**Observed (E8, $k = 4$, aliased).** $\mathrm{res}_4$ on $V_{240}$ has rank $84 < \dim H_4(S^7) = 294$, landing exactly in the $\lambda = 60$ block (sim L3, $k=4$); and the Gegenbauer scalar for $k = 5$ gives $a_5 = -2$, i.e. $\lambda = 58$ — the level-5 harmonics alias into the same block as level 3. The high blocks of each rung are superpositions of folded high harmonics.

**The ladder, quantified.**

| Rung | Arena | chain (resolved) | cutoff $k_{\max}$ | hidden sector | continuum constant $\deg\theta^2/6$ |
|---|---|---|---|---|---|
| H4 / $V_{120}$ | $S^3$ | $1,4,9,16,25,36$ | 5 | $29/120$ (24%) | $0.790$ |
| D4 / $V_{24}$ | $S^3$ | $1,4,9$ | 2 | $10/24$ (42%) | $1.462$ |
| 16 / $V_{16}$ | $S^3$ | $1,4$ | 1 | $11/16$ (69%) | $0.731$ |
| 8/E8 / $V_{240}$ | $S^7$ | $1,8,35,112$ | 3 | $84/240$ (35%) | ($\lambda_1/7 = 4.0$) |

The hidden sectors are **not other universes**: they are function-space content of *this* substrate that cannot be expressed as a field on the rung's arena — fold-aliased or kernel-annihilated relative to geometric rendering. Whether any physical projection class samples them is Open 7.3.

## 5. Why arenas exist only in dimensions 3 and 7

**Proposition 5.1 (Renderable arenas are parallelisable spheres).** The rendering layer's canonical observer frame (`rendering-layer.md` Proposition 4.1) requires a global trivialisation of the arena's tangent bundle. By Adams' theorem (Hopf invariant one), the only parallelisable spheres are $S^0, S^1, S^3, S^7$ — the unit spheres of the normed division algebras $\mathbb R, \mathbb C, \mathbb H, \mathbb O$ (Hurwitz). Hence the cascade can host rendered perspectives only on **1-, 3-, or 7-dimensional** arenas; there is no 4-, 5-, or 6-dimensional option.

**Remark 5.2 (The arena inclusion is the known H4→E8 fold).** The map between the $S^3$ arena and the $S^7$ arena is not hypothetical: the H4→E8 trace-form construction (two H4 shells at ratio $1/\varphi$, coupling constant $c = 1 + 1/\sqrt 5$, exact 240-root match — verified in `release-bundles/fractal-tiling-theorem/vfd_geometry/`, Wilson/Moody–Patera) realises $V_{120} \times \{\text{shells}\} \to V_{240}$, i.e. the inclusion of the quaternionic arena data into the octonionic arena. The octonionic generalisation of the rendering layer itself (frames from the Moufang-loop parallelism of $S^7$) is Open 7.2.

**Remark 5.3 (What this says to "hidden dimensions" intuitions).** Within this framework the correct statement is: there is exactly **one** arena above ours (7-dimensional, octonionic, at the observer/totality rung), reachable by an exact and already-verified embedding; plus per-rung hidden *sectors* (§4) that are not spatial dimensions at all; plus the Galois twin substrate (`release-bundles/critical-line-pullback/`, finding 4: coordinate-Galois maps $V_{600}$ to an odd-permutation conjugate copy). No continuum of hidden universes is available — Adams' theorem closes that door.

## 6. Consequences for the chain

1. **Cross-rung coupling is sampling (Theorem 3.5).** The formal substrate for "decoherence as H4→Cl(1,3) cross-rung coarsening" (planned Paper XLIV) and the G2/observer formalism (XLV) can now be stated as restriction along $V_{16} \subset V_{24} \subset V_{120}$ plus the dispersion reparametrisation. A rung transition does not change *what* the field is — only the cutoff $k_{\max}$ and the propagation constant.
2. **The cascade fan = one arena + resolution ladder + one arena change.** QM-rung resolves space to harmonic level 5, gravity-rung to level 2, information-rung to level 1; the observer rung swaps $S^3$ for $S^7$ at level 3. The 40/biology rung also sits on the **same $S^3$**, sampled at the cell level rather than the vertex level (§7.4).
3. **Hidden content is quantified and three-fold:** folded/kernel sectors per rung (§4 table), the $S^7$ arena (§5), the Galois twin (Remark 5.3). Each is a precise mathematical object; none requires (or permits) a "many hidden universes" reading.
4. **Rung-relative constants.** Each rung carries its own lattice angle $\theta$ and degree, hence its own continuum constant (§4 table) and — via $c = a/\tau$ of `kappa-derivation-math.md` (5.3) — its own effective propagation speed. The same harmonic content propagates with rung-dependent dispersion (interpretive; not load-bearing).

## 7. Resolution of the open items (2026-06-11)

The five items left open on 2026-06-10 are closed or reduced below, verified in `scripts/verify_ladder_completion.py` (**29/29 PASS**, residuals $\le 10^{-14}$).

### 7.1 Scheme structure — CLOSED (was Open 7.1)

**Theorem 7.1 (Rung substrates are commutative association schemes).** Each of $V_{120}, V_{240}, V_{16}$ (and $V_{24}$) is a commutative association scheme: the number of off-diagonal inner-product classes $d$ equals (#Laplacian eigenspaces) $-1$, and every eigenspace is a single scheme idempotent. Verified: $V_{120}$ has $d = 8$ ip-classes and $9$ eigenspaces; $V_{240}$ and $V_{16}$ each $d = 4$, $5$ eigenspaces (sim C1).

**Proof.** Each vertex set is the orbit of a two-point-homogeneous (generously transitive) group — $W(H_4)$, $W(E_8)$, $W(B_4)$ — so the orbitals on ordered pairs are indexed by inner product, the orbital adjacency matrices span a commutative Bose–Mesner algebra, and the Laplacian (a real linear combination of them) is simultaneously diagonalised by the algebra's primitive idempotents. By the Delsarte–Goethals–Seidel theory the idempotents are the harmonic-isotypic projectors up to the design strength, which gives the zonal scalar action of Proposition 3.3 as the Bose–Mesner eigenvalue. The two ingredients the proof needs and the numerics confirm exactly: the $\mathrm{res}_k$ images for $k \le 4$ on $V_{240}$ are mutually orthogonal with ranks $1, 8, 35, 112, 84$ summing to $240$ (sim C1, rank exhaustion). $\square$

This upgrades Proposition 3.3 (the non-group rungs' scalar action) from "numerics machine-exact, formalisation deferred" to a theorem on classical association-scheme footing.

### 7.2 Octonionic rendering layer — CLOSED for the rendering primitives; one sub-open reduced (was Open 7.2)

The rendering layer of `docs/rendering-layer.md` §§3–4 transfers to the $S^7$/E8 rung. Established (sim C4):

- **Frames (C4b).** The octonion product gives a canonical orthonormal 7-frame $\{v\,e_1, \dots, v\,e_7\}$ of $T_v S^7$ at **every** one of the 240 anchors — the Moufang parallelism of $S^7$, the exact $S^7$ analogue of Proposition 4.1. Seven spatial axes for free, because $\dim\mathrm{Im}\,\mathbb O = 7$.
- **Kernel (C4c–C4d).** The canonical kernel $\pi_r = (I + r^2 L_{240})^{-1}$ on the E8-root graph (degree 56, multiplicities $\{1,8,35,84,112\}$) is entrywise positive and stochastic — Theorem 3.1 verbatim, no octonion closure required (it is a function of $L$ alone).
- **Equivariance (C4e).** $\pi_r$ commutes with $W(E_8)$: a genuine root-system automorphism (signed transposition) has $\|[P,\pi_r]\| \sim 10^{-16}$.
- **Multiplication table (C4a).** The seven Fano lines are derived from the Cayley–Dickson table, fixing the octonion product underlying the frames.

**Reduced sub-open (7.2′).** Whether the 240 units form a *multiplicatively closed* Moufang loop in a chosen basis — so that left-translation is itself a rendering symmetry, the octonionic counterpart of icosian left-multiplication — is the one residual. The naive E8-root basis is **not** closed (sim C4f, as expected); the closed loop is Coxeter's maximal order of integral octavians (Conway–Smith, *On Quaternions and Octonions*, ch. 9–11). Importing that basis is bookkeeping, not new mathematics; the rendering layer's *needs* (frames, kernel, equivariance) are already met without it.

### 7.3 Folded-sector physics — RESOLVED: the folded sector is reachable, by radial (non-field) observables (was Open 7.3)

**Proposition 7.3 (Radial observables sample the folded sector).** The folded/primed blocks are *not* inaccessible — they are exactly the part of function space invisible to **angular field** rendering but reachable by **radial/zonal** observables:

- The nine shell-indicator functions about any anchor (the zonal observables $\mathbf 1[\langle v_0, \cdot\rangle = c_s]$) hit **all nine** eigenblocks of $V_{120}$, one dimension each — a bijection onto the block set, including the three primed blocks $\lambda = 14.47, 15, 15.71$ (sim C3, zonal bijection).
- Concretely, the closure-response field itself reaches them: $\psi = (L + \varphi^{-2} I)^{-1}\delta_{v_0}$ — the same operator that carries the b-anomaly witness — places **8.5% of its non-constant energy** in the primed blocks (sim C3).

**Reading.** This sharpens, rather than merely answers, the question. The hidden sector is hidden from the *harmonic field* rendering of §4 (it carries no $S^3$ angular harmonic), but it is the natural home of **radial structure** — shell-grade, coherence-length content. That is precisely the cocycle $\kappa(v) = (s(v)-4)^2$ and the $\varphi$-shell grading that the b-anomaly response operator and the RH pentagonal-clock already run on (`docs/aria-closure-kernel.md` §4). So the folded sector is not new physics waiting to be found and not unobservable; it is the **radial/spectral** channel of the substrate, complementary to the angular/spatial channel that renders as a scene. A field on space cannot draw it; a coherence-length measurement reads it directly.

### 7.4 The 40 / biology rung — CLOSED: arena is the same $S^3$, sampled at cell-centres (was Open 7.4)

**Theorem 7.4 (The biology rung renders on $S^3$).** The 40 rung's substrate is the **cell level** of the 600-cell: its 600 tetrahedral cells (4-cliques of $V_{120}$; sim C5a), whose centres are the 600 vertices of the dual **120-cell**, all on $S^3$ (sim C5b). This arena is $S^3$: the 120-cell is a high spherical design and harmonic restriction is injective through $k_{\max} = 10$ (sim C5d). The Hopf structure is the $600 = 15 \times 40$ partition into 15 cell-fibres of 40 cells each, $40 = 8 \times 5$ (E8-dimension $\times$ Schläfli index of $2T$ in $2I$); `papers/cascade-derivation/cascade-bio.md` §3.2.

**Structural distinction (the reason it looked "uncovered").** The 120-cell vertices are **not a group** — only the 600-cell vertices $2I$ are. So the intertwiner here runs via the **spherical-design route** (Theorem 3.4 / 7.1), *not* the class-sum route (Theorem 3.2). Consequence, verified: the cell-centre graph Laplacian has **27 eigenblocks with non-square multiplicities** $\{1,4,4,8,8,9,9,16^{\times4},18,24^{\times4},25^{\times3},30,30,36^{\times3},40,48,48\}$ (sim C5c) — strictly richer than the 9-block harmonic scheme of the vertex rungs — yet the low harmonics still land in single graph eigenspaces (res$_1$ → one 4-dim block, sim C5e). So the 40 rung *is* on our $S^3$ and *is* design-injective, but its graph carries extra non-harmonic structure: the first rung whose substrate is a homogeneous space rather than a group. This is the precise sense in which biology's rung is "the same space, indexed differently."

### 7.5 E8 high-block bookkeeping — CLOSED (was Open 7.5)

**Proposition 7.5 (Complete aliasing tables).** Every harmonic level's landing is now tabulated and verified (sim C2):

- **$V_{120}$ (McKay walk), full irrep-squared blocks:** $\mathrm{res}_6 \to 3' {+} 4'$ ($\lambda{=}14.47,15$); $\mathrm{res}_7 \to 6 {+} 2'$ ($14, 15.71$); $\mathrm{res}_8 \to 5 {+} 4'$ ($12, 15$); $\mathrm{res}_9 \to 4 {+} 6$ ($9, 14$); $\mathrm{res}_{10} \to 3 {+} 5 {+} 3'$ ($5.53, 12, 14.47$). Each lands in *complete* eigenblocks — the harmonics tile the folded sector exactly.
- **$V_{240}$ (Gegenbauer):** $\mathrm{res}_5$ has scalar $a_5 = -2$, landing *entirely* in $\lambda = 58$ alongside $H_3$ (sim C2, action residual $10^{-15}$); $\mathrm{res}_6$ has $a_6 = 4/11$, not a scheme eigenvalue, so it **splits** across blocks. The $\lambda = 60$ block is rank-84 of $H_4$; the scheme closes at $k = 4$.
- **tesseract (complete character account):** $\mathrm{res}_k$ for $k = 0..4$ gives blocks $\{0{:}1\}, \{2{:}4\}, \{4{:}6\}, \{2{:}4, 6{:}4\}, \{0{:}1,4{:}6,8{:}1\}$ — exhibiting **down-aliasing** with an explicit witness: the degree-3 harmonic $x_1^3 - \tfrac12 x_1|x|^2$ restricts to $-x_1/4$, a degree-1 mode (sim C2 witness).

### Residual opens after this pass

- **(7.2′)** Coxeter maximal-order basis for the closed 240-unit octonion loop (bookkeeping; Conway–Smith).
- **(7.6)** The 40-rung *dynamics* — whether the 15×40 Hopf partition carries a φ-driven self-replication law (capsid/phyllotaxis), the actual biology content — is untouched here; this section settles only the *arena*. See `papers/cascade-derivation/cascade-bio.md`, `papers/biology-rung/`.
- **(7.7)** Full McKay-walk closed form for $\mathrm{res}_k$ landing on $V_{120}$ at all $k$ (the table is verified through $k = 10$; the general pattern is the $2I$ McKay quiver walk, stated not proved).

## 8. Sim verification summary

`scripts/verify_rung_dimension_ladder.py` (core), 2026-06-10: **25 PASS / 0 FAIL**.
`scripts/verify_ladder_completion.py` (opens closure), 2026-06-11: **29 PASS / 0 FAIL**. All residuals $\le 10^{-14}$.

| Completion block | Closes | Result |
|---|---|---|
| C1 scheme structure + E8 rank exhaustion | 7.1 | PASS (4) |
| C2 aliasing tables ($V_{120}$ McKay, E8 Gegenbauer, tesseract) | 7.5 | PASS (9) |
| C3 folded-sector sampling (zonal bijection, response energy) | 7.3 | PASS (3) |
| C4 octonionic frames + kernel + $W(E_8)$-equivariance | 7.2 | PASS (6) |
| C5 40-rung = $S^3$ cell-centre arena, design route | 7.4 | PASS (6) |

Core-doc table (L1–L5) below.

`scripts/verify_rung_dimension_ladder.py`, 2026-06-10: **25 PASS / 0 FAIL** (all residuals $\le 10^{-14}$).

| Block | Checks | Result |
|---|---|---|
| L1 nesting | $V_{16} \subset V_{24} \subset V_{120}$ | PASS |
| L2 $S^3$ intertwiner | ranks + scalar action + containment, $V_{120}$ $k\le5$, $V_{24}$ $k\le2$, $V_{16}$ $k\le1$ | PASS (11 checks) |
| L3 $S^7$ intertwiner | Gegenbauer $\lambda = 28, 48, 58$ injective; $k=4$ aliased rank 84 at $\lambda = 60$ | PASS (4 checks) |
| L4 nested sampling | fine eigenspace sampled = coarse eigenspace | PASS (5 checks) |
| L5 fold + kernel | $\mathrm{res}_6 \to$ primed blocks rank 25; tesseract $\mathrm{res}_2$ rank 6, witness $x_i^2 - x_j^2 \equiv 0$ | PASS (3 checks) |

First-pass spectra and Weyl fits: `scripts/explore_rung_dimension_ladder.py` ($d = 3.09, 2.97$ on $S^3$ rungs; $d = 7.41$ on the E8 rung).

## 9. Cross-references

- Spectral-dimension theorem, dispersion, canonical kernel, frames: `docs/rendering-layer.md`.
- Rung definitions: `docs/glossary.md`; cascade structure: `papers/cascade-derivation/`.
- 40/biology rung substrate (15×40 Hopf cell-fibration): `papers/cascade-derivation/cascade-bio.md` §3, `papers/biology-rung/`.
- Closed-loop integral octonions (sub-open 7.2′): Conway–Smith, *On Quaternions and Octonions*, ch. 9–11.
- Opens-closure verification: `scripts/verify_ladder_completion.py` (29/29).
- H4→E8 trace-form embedding (arena inclusion): `release-bundles/fractal-tiling-theorem/vfd_geometry/`, `VFD_GEOMETRY_FRONTIER.md`.
- Galois twin: `release-bundles/critical-line-pullback/` (finding 4).
- Cross-rung programme targets: Papers XLIV (decoherence as cross-rung coarsening), XLV (observer-rung G2 formalism) per `docs/programme-plan.md`.
- Continuum constants and $c = a/\tau$: `docs/kappa-derivation-math.md` §5.
- Communication spine: `docs/geometry-to-reality.md` (this document supplies the "dimensional layering" chapter of that story).

## 10. Informal reading (non-load-bearing)

*This subsection provides reader-side interpretation; the theorems of §§2–5 do not depend on it.*

The math of §§2–7 admits a reader-side reading in which the cascade's rungs are not stacked worlds but one world seen at successively coarser resolution: the quantum rung sees space sharply (harmonic level 5), the gravity rung sees the *same space* blurrier (level 2), the information rung blurrier still (level 1) — and the fields of the coarser views are literally point-samples of the finer ones. The biology rung looks at the same $S^3$ too, but indexes it by *cells* rather than points (§7.4) — the first rung whose substrate is a homogeneous space rather than a group, which is why its texture is richer. Above them all sits a single larger arena — seven-dimensional, octonionic, with its own seven axes handed to every anchor by the octonion product (§7.2) — connected to ours by an exact golden-ratio fold, and classical topology (Adams) guarantees there is nothing in between: no four-, five-, or six-dimensional vantage exists for any anchored instance anywhere. What hides "beside" the 3D view is then not a multiverse but three definite, now-charted things: substrate content that cannot be drawn as a field on space at all — the folded sectors, which turn out to be the *radial/coherence-length* channel readable by spectral (not spatial) measurement (§7.3); the conjugate twin copy of the substrate; and the one 7-dimensional arena upstairs. These readings are reader-side; the mathematical content stands without them.

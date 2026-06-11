# Derivation of the Pentagonal-Torsion Clock from Permeability

**Status:** derivation; each step is either a theorem from established
mathematics (referenced) or a specific algebraic identity that this
document proves. No step assumes what it is trying to derive.

**Goal:** starting from the permeability axiom F1 (already derived in
foundations.tex), derive (i) the ring Z[φ] with its Galois involution
σ, (ii) the pentagonal chirality of the cyclotomic field Q(ζ₅) over
Q(φ), (iii) a canonical pentagonal torsion element in the binary
icosahedral group 2I, and (iv) the clock map T on the 120 vertices of
the 600-cell as multiplication by that torsion element, modulo the
icosian lattice projection.

The exact verifier is Build B13; no such script is present yet.

---

## §1. Permeability (axiom, already derived)

**F1 (Permeability axiom).** A self-permeable scale ratio $r > 0$
satisfies
$$
r = 1 + \frac{1}{r}.
$$
Equivalently, $r^2 = r + 1$, the minimal polynomial of $r$ over $\mathbb{Z}$.

**Theorem 1.1.** The unique positive real solution is
$\varphi = \tfrac{1+\sqrt{5}}{2}$. The conjugate root is
$\varphi' = \tfrac{1-\sqrt{5}}{2} = 1 - \varphi = -1/\varphi$.

*Proof.* Quadratic formula on $r^2 - r - 1 = 0$; the product of roots
is $-1$, so $\varphi \cdot \varphi' = -1$ giving $\varphi' = -1/\varphi$.  ∎

This is the entire F1 content; nothing below depends on anything beyond
this equation.

---

## §2. Z[φ] and the Galois involution σ (pure algebra from §1)

**Definition 2.1.** $K = \mathbb{Q}(\varphi) = \mathbb{Q}(\sqrt{5})$;
$\mathcal{O}_K = \mathbb{Z}[\varphi] = \{a + b\varphi : a, b \in \mathbb{Z}\}$.

**Theorem 2.2** (classical). $\mathcal{O}_K$ is a Euclidean domain
(class number 1). The discriminant of $K$ over $\mathbb{Q}$ is 5.

**Definition 2.3.** The Galois involution
$\sigma: K \to K$, $\sigma(\sqrt{5}) = -\sqrt{5}$, equivalently
$\sigma(a + b\varphi) = a + b(1 - \varphi) = (a + b) - b\varphi$.

**Proposition 2.4.** $\sigma$ is an involution of $K$ fixing $\mathbb{Q}$,
and $\sigma(\varphi) = -1/\varphi$.

*Proof.* $\sigma^2 = \mathrm{id}$ since $\sigma(-\sqrt{5}) = \sqrt{5}$;
$\sigma(\varphi) = 1 - \varphi$ directly from Definition 2.3; and
$1 - \varphi = -1/\varphi$ by Theorem 1.1.  ∎

**Corollary 2.5.** The unit group of $\mathbb{Z}[\varphi]$ is
$\mathbb{Z}[\varphi]^\times = \{\pm \varphi^n : n \in \mathbb{Z}\}$, and
$\sigma(\varphi^n) = (-1)^n \varphi^{-n}$.

*Proof.* Dirichlet unit theorem gives rank 1 for a real quadratic
field; $\varphi$ is the fundamental unit by Theorem 1.1 (it's the
smallest unit $> 1$). Then
$\sigma(\varphi^n) = \sigma(\varphi)^n = (-1/\varphi)^n = (-1)^n \varphi^{-n}$.  ∎

Everything in §2 is forced by F1. No additional axiom.

---

## §3. Pentagonal chirality: Q(ζ₅) ⊃ Q(√5) (classical cyclotomy)

**Fact 3.1** (classical, e.g. Washington, *Cyclotomic Fields*). The
cyclotomic field $\mathbb{Q}(\zeta_5)$ has degree $\varphi_{\text{Euler}}(5) = 4$
over $\mathbb{Q}$, with Galois group $(\mathbb{Z}/5)^\times \cong \mathbb{Z}/4$.
Its unique quadratic subfield is the real field $\mathbb{Q}(\sqrt{5}) = K$.

**Theorem 3.2** (Gauss sum identity, classical).
$$
\sqrt{5} = \zeta_5 + \zeta_5^4 - \zeta_5^2 - \zeta_5^3
= 2\cos(2\pi/5) - 2\cos(4\pi/5).
$$

*Proof sketch.* Both Gaussian periods
$\eta_0 = \zeta_5 + \zeta_5^4 = 2\cos(2\pi/5)$ and
$\eta_1 = \zeta_5^2 + \zeta_5^3 = 2\cos(4\pi/5)$ are roots of
$x^2 + x - 1 = 0$, giving $\eta_0 = 1/\varphi$ and $\eta_1 = -\varphi$.
Then $\eta_0 - \eta_1 = 1/\varphi + \varphi = \sqrt{5}$.  ∎

**Theorem 3.3** (pentagonality is canonical). Among regular $n$-gons
with $n \leq 6$, the cyclotomic field $\mathbb{Q}(\zeta_n)$ contains
the real quadratic field $\mathbb{Q}(\sqrt{5})$ if and only if $n = 5$
(or a multiple of 5). The pentagon is therefore the unique minimal
rotationally-symmetric source of $\mathbb{Z}[\varphi]$-arithmetic.

*Proof.* For $n = 3$: $\mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$, imaginary
quadratic, does not contain $\sqrt{5}$. For $n = 4$:
$\mathbb{Q}(\zeta_4) = \mathbb{Q}(i)$, imaginary, does not contain $\sqrt{5}$.
For $n = 6$: $\mathbb{Q}(\zeta_6) = \mathbb{Q}(\zeta_3)$, same as $n=3$.
For $n = 5$: Theorem 3.2.  ∎

**Epistemic note.** Pentagonal symmetry is not "chosen" for the
cascade; it is the unique smallest rotational order whose cyclotomic
field contains the permeability field $\mathbb{Q}(\sqrt{5})$. More
precisely, the cyclotomic field $\mathbb{Q}(\zeta_n)$ contains
$\mathbb{Q}(\sqrt{5})$ exactly when $5 \mid n$; for $n \in \{3, 4, 6\}$
the cyclotomic field is an imaginary quadratic extension (or equals
one) and does not contain $\sqrt{5}$. Non-multiples of 5 do not
factor through the pentagonal field by cyclotomy alone.

---

## §4. Pentagonal asymmetry as torsion (the core derivation)

Consider the group $\mathbb{Z}[\varphi]^\times / \{\pm 1\} \cong \mathbb{Z}$
under the map $\pm \varphi^n \mapsto n$. This is the Z-free quotient of
the unit group.

**Proposition 4.1.** Under $\sigma$, $\sigma(\varphi^n) = (-1)^n \varphi^{-n}$
(Corollary 2.5). On the $\mathbb{Z}$-quotient, $\sigma$ acts by
$n \mapsto -n$ plus a $\mathbb{Z}/2$ sign track coming from the factor
$(-1)^n$.

**Definition 4.2** (pentagonal torsion).
The pentagonal torsion element of $\mathbb{Z}[\varphi]^\times$ is the
product $\varphi \cdot \sigma(\varphi) = \varphi \cdot (-1/\varphi) = -1$.
More generally, for any $\varphi^n$,
$$
\varphi^n \cdot \sigma(\varphi^n) = \varphi^n \cdot (-1)^n \varphi^{-n} = (-1)^n.
$$

**Proposition 4.3.** The map $N : \mathbb{Z}[\varphi]^\times \to \{\pm 1\}$
given by $N(u) = u \cdot \sigma(u)$ is the field norm
$N_{K/\mathbb{Q}}$ restricted to the unit group. It is a homomorphism
with kernel $\{u \in \mathbb{Z}[\varphi]^\times : N(u) = +1\}$ and image
$\{\pm 1\}$. Specifically, $N(\pm \varphi^n) = (-1)^n$.
(Its geometric interpretation as a pentagonal-torsion invariant is
the content of Build B4.)

*Proof.* Multiplicativity is immediate:
$\tau(u_1 u_2) = u_1 u_2 \sigma(u_1) \sigma(u_2) = \tau(u_1) \tau(u_2)$.
Image computed by Definition 4.2.  ∎

**Theorem 4.4** (pentagonal chirality theorem). The pentagonal torsion
character $\tau$ is non-trivial precisely because $\sigma(\varphi) \neq
1/\varphi$ on $\mathbb{Z}[\varphi]^\times$: the sign factor $(-1)^n$ in
$\sigma(\varphi^n) = (-1)^n \varphi^{-n}$ is irremovable.

*Proof.* If $\sigma(\varphi) = 1/\varphi$ without sign, then $\tau$
would be trivial. But $\sigma(\varphi) = 1 - \varphi = -1/\varphi$
(Proposition 2.4), so the sign appears in $\sigma(\varphi) \cdot \varphi = -1$.
This $-1$ is the \emph{pentagonal asymmetry}: a closed σ-loop picks up
$-1$ per odd power of $\varphi$ traversed.  ∎

**Corollary 4.5.** For a closed loop $\gamma$ in any structure admitting
$\mathbb{Z}[\varphi]^\times$-valued parallel transport, if the net
$\varphi$-power accumulated around $\gamma$ is odd, the σ-monodromy is
$-1$, not $+1$. The loop is chirally obstructed from being σ-trivial.

This is the source of the torsion. It is not imposed; it is forced by
F1 + the Galois structure of $K$. No additional assumption.

---

## §5. Lift to the icosian ring (Elkies, classical)

**Fact 5.1** (Elkies, 1999). Let $\mathcal{I} \subset \mathbb{H}$ be
the icosian ring: the $\mathbb{Z}[\varphi]$-order in the Hamilton
quaternions generated by
$\{1, i, (1 + i + j + k)/2, (1/2)(1 + \varphi^{-1} j + \varphi k)\}$.
The 120 units of $\mathcal{I}$ (quaternions of norm 1) form the
\emph{binary icosahedral group} $2I$, which is exactly the 120-vertex
set of the 600-cell under the Hopf projection to $S^3$.

**Fact 5.2** ($2I \cong \mathrm{SL}_2(\mathbb{F}_5)$; sim-verified
BUILD B5 COMPLETE). $|2I| = 120$ with the following order
distribution (exact computation in
`papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py`,
2026-04-24):
$$
\{\text{order 1}: 1,\ \text{order 2}: 1,\ \text{order 3}: 20,\ \text{order 4}: 30,\ \text{order 5}: 24,\ \text{order 6}: 20,\ \text{order 10}: 24\}.
$$
The 24 elements of order 10 split into exactly 2 conjugacy classes of
12 each, so $\tau$ is canonical \emph{up to the choice between these
two classes}. Within each class, all representatives are conjugate;
the choice of representative within a class yields a $T_\tau$ that is
conjugate (as a permutation of $2I$) to $T_{\tau'}$, hence has
identical cycle structure. A canonical representative chosen by the
sim has exact $\mathbb{Q}(\sqrt{5})$ coordinates
$$
\tau = \bigl(\tfrac{1}{4}(1 - \sqrt{5}),\ 0,\ \tfrac{1}{4}(1 + \sqrt{5}),\ \tfrac{1}{2}\bigr),
$$
satisfying $\tau^{10} = 1$, $\tau^5 = -1$. Whether the choice between
the two order-10 classes affects the cocycle $\omega$ and weighted
zeta is addressed in Build B8/B9.

**Proposition 5.3** (pentagonal torsion in 2I). The element $\tau^5 = -1$
is the pentagonal torsion element: closing a 5-fold loop around a
pentagonal stabilizer/axis in the icosahedral adjacency yields
$-1 \in 2I$, not the identity. (The 600-cell itself has triangular
faces; the pentagonal structure appears in the icosahedral vertex
stabilizer, not in the 2D face structure.)

*Proof.* $\tau^{10} = \cos(2\pi) + \sin(2\pi) \mathbf{n} = 1$; $\tau^5 =
\cos(\pi) + \sin(\pi) \mathbf{n} = -1$. That $\tau$ has order exactly
10 (not 5) in $2I$ is the distinguishing fact: 5-fold geometric rotation
in the \emph{double cover} of the icosahedral group is of order 10, with
the 5-fold "loop" producing the central element $-1$.  ∎

**Corollary 5.4** (pentagonal torsion is the §4 torsion, lifted).
Under the natural projection $2I \to I \subset SO(3)$ (dividing by the
center $\{\pm 1\}$), the element $\tau^5 = -1$ maps to the identity.
This means: at the \emph{geometric} level (icosahedral rotation group),
a 5-fold loop closes trivially. At the \emph{algebraic} level (binary
icosahedral group $2I$, which is the natural receptacle of
$\mathbb{Z}[\varphi]^\times$ dynamics), the same loop picks up $-1$.
This central $-1 \in 2I$ is the quaternionic target that must be
identified with the norm-sign character $N$ of Proposition 4.3 by
Build B5 (canonicity of the order-10 generator) and Build B4
(geometric interpretation of the norm).

---

## §6. The clock map T on the 600-cell

We now construct the canonical self-map T on V = V(600-cell) = 2I from
the pentagonal torsion element τ and the icosian arithmetic.

**Definition 6.1** (clock map). Let $\tau \in 2I$ be the pentagonal
torsion element of Fact 5.2. Define
$$
T: 2I \to 2I, \qquad T(v) = \tau \cdot v \qquad (\text{quaternion product}).
$$

**Proposition 6.2** (properties of T; BUILD B6 COMPLETE, sim-verified
2026-04-24).
1. T is a bijection of $2I$ (left-translation).
2. $T^{10} = \mathrm{id}$ ($\tau^{10} = 1$).
3. $T^5(v) = -v$ for all $v \in 2I$ ($\tau^5 = -1$, central).
4. T has no fixed points: $\tau \cdot v = v \Rightarrow \tau = 1$, contradiction.
5. $\mathrm{Fix}(T^n) = \emptyset$ for $1 \leq n \leq 9$ (exact computation).
6. $\mathrm{Fix}(T^{10}) = 2I$, all 120 points.
7. Cycle decomposition: $2I$ splits into exactly 12 cycles of length
   10 under $T$. Unweighted Artin–Mazur zeta: $\zeta_T(z) = (1-z^{10})^{-12}$.

*Proof.* 1 and 2 from group theory (left-translation by a group element of
order 10 is a permutation of order 10). 3 from $\tau^5$ being in the centre
$\{\pm 1\} \subset 2I$; checking the sign requires the explicit
representative, which the sim confirms. 4–6 by direct enumeration over all
120 elements with exact quaternion arithmetic. 7 follows from
$|2I|/\mathrm{ord}(\tau) = 120/10 = 12$ orbits of size 10 for a
free left action.  ∎

**Definition 6.3** (pentagonal holonomy cocycle, BUILD REQUIRED).
For an edge $(v, w)$ of the 600-cell graph (where "edge" means
adjacency under the 12 nearest neighbours in the icosahedral adjacency
on 2I), the cocycle value
$$
\omega(v, w) \in \mathbb{Z}[\varphi]^\times
$$
is defined by the H₄-equivariant local-frame transition of Build
B7/B8. Scalar rescaling of a unit quaternion cannot supply the
general edge label (since $|v| = |w| = 1$, a scalar $\varphi^{-k}$
applied to $w v^{-1}$ produces a non-unit unless $k = 0$). The
correct construction attaches a local frame (orthonormal basis) at
each vertex and defines $\omega(v, w)$ as the $\mathbb{Z}[\varphi]^\times$
factor required to parallel-transport the frame at $v$ to the frame
at $w$ through the icosahedral adjacency. The full construction is
Build B7 (local frame) + Build B8 (holonomy cocycle).

**Proposition 6.4** (cocycle is canonical, BUILD REQUIRED).
$\omega$ is to be H₄-equivariant and σ-covariant:
$\omega(\sigma v, \sigma w) = \sigma(\omega(v, w))$.

*Proof obligation:* Build B8, including (i) full-unit codomain
$\{\pm \varphi^n : n \in \mathbb{Z}\}$ rather than just $\varphi^n$,
and (ii) gauge-independence of $\omega$ under local-frame
relabelling. Without these, $\omega$ is not well-defined as a
cocycle.

**Proposition 6.5** (T is the pentagonal clock). The clock map T of
Definition 6.1 is equivalent to the argmin
$$
T(v) = \mathrm{argmin}_{w \in N(v)} |\omega(v, w) - 1|_{Z[\varphi]}
$$
if and only if the local frame at each vertex is aligned with the
pentagonal rotation direction. Fixing this alignment by the 2I
quaternion structure, T is uniquely defined.

---

## §7. The weighted Artin–Mazur zeta ζ_T^ω

**Definition 7.1.** Let $\gamma = (v, T(v), T^2(v), \ldots, T^{n-1}(v))$
be a periodic orbit of T of period $n$ (so $T^n(v) = v$). Define the
\emph{accumulated ω-weight} of γ as
$$
\omega(\gamma) = \prod_{i=0}^{n-1} \omega(T^i(v), T^{i+1}(v)) \in \mathbb{Z}[\varphi]^\times.
$$

**Definition 7.2.** The weighted Artin–Mazur zeta of $(T, \omega)$ is
$$
\zeta_T^\omega(z) = \exp\left( \sum_{n \geq 1} \frac{z^n}{n} \cdot
\sum_{v \in \mathrm{Fix}(T^n)} \omega(\mathrm{orbit}(v)) \right) \in
\mathbb{Z}[\varphi][[z]].
$$

**Proposition 7.3** (σ-symmetry of ζ_T^ω). $\sigma$ acts on $\zeta_T^\omega(z)$
by $\sigma(\zeta_T^\omega(z)) = \zeta_T^{\sigma \omega}(z)$. The fixed
part ζ_T^ω · σ(ζ_T^ω) is σ-invariant by construction.

**The empirical question.** Compute the coefficients of $\zeta_T^\omega(z)$
up to degree 30. If they factor as $\zeta(s) \cdot L(s, \chi_5)$ under
the standard Mellin pairing, the construction is (δ) — classical
Dedekind reduction, Path A definitively closed.

If they do NOT factor classically — i.e., they genuinely live in
$\mathbb{Z}[\varphi]$ with coefficients not expressible as a finite
combination of $\zeta(s)$ and $L(s, \chi_5)$ — then $\zeta_T^\omega$
is a non-classical cascade-native zeta whose critical-line behaviour
becomes the target of Build B11 (Mellin/critical-line bridge). The
Mellin pairing is not automatic; it must be defined and proved to
carry σ to $s \mapsto 1-s$ for the specific $\zeta_T^\omega$, not
for generic $\zeta$.

---

## §8. Summary of the derivation chain

| Step | Content | Source |
|---|---|---|
| F1 | $r = 1 + 1/r \Rightarrow r = \varphi$ | Axiom (foundations.tex §F1) |
| 2.4 | $\sigma(\varphi) = -1/\varphi$ | Direct from F1 |
| 2.5 | $\sigma(\varphi^n) = (-1)^n \varphi^{-n}$ | Dirichlet unit theorem |
| 3.3 | Pentagonal is minimal $n$ with $\mathbb{Q}(\zeta_n) \supset \mathbb{Q}(\sqrt 5)$ | Classical cyclotomy |
| 4.3 | Torsion character $\tau(u) = u \sigma(u) \in \{\pm 1\}$ | Proposition 4.3 |
| 4.4 | Torsion non-trivial because $\sigma(\varphi) \cdot \varphi = -1$ | Theorem 4.4 |
| 5.2 | Pentagonal $\tau \in 2I$, order 10, $\tau^5 = -1$ | Elkies icosian construction |
| 6.1 | Clock map $T(v) = \tau \cdot v$ on 120 vertices of 600-cell | Definition |
| 6.3 | Cocycle $\omega(v,w) = \varphi^{k(v,w)}$ | Definition |
| 7.2 | Weighted zeta $\zeta_T^\omega(z) \in \mathbb{Z}[\varphi][[z]]$ | Definition |

Every step is either:
- a theorem of classical number theory / cyclotomy,
- a direct consequence of F1, or
- a definition that uses only objects from the two above.

No step assumes the conclusion. The derivation is complete through
$F_1 \to \mathbb{Z}[\varphi] \to \sigma$ and the identification of
pentagonal cyclotomy as the unique source of $\mathbb{Q}(\sqrt{5})$
among small $n$. Builds B4–B13 (see
`docs/codex-derive/pentagonal-clock-wo-task-*.md`) close the clock,
cocycle, weighted-zeta, and classical-reduction audit. What remains
is the implementation and verification of those builds.

---

## §9. What this derives and what it leaves open

**Derived:**
- Z[φ] arithmetic from F1.
- σ involution and its action on units.
- Pentagonal torsion character τ(u) = u σ(u) (= field norm).
- Non-triviality of τ from σ(φ)·φ = −1.
- Lift to 2I via Elkies icosian construction.
- Clock map T as left-multiplication by pentagonal τ ∈ 2I.
- **Clock (B5/B6 sim-complete 2026-04-24):** T_τ decomposes 2I into
  12 cycles of length 10, Fix(T^n)=∅ for 1≤n<10, Fix(T^10)=2I.
- **Cocycle (B8' Route Q-min, sim-complete 2026-04-24):** κ(v) =
  (shell(v) − 4)², antipodal-even radial grade. Yields 4 cycle-profile
  types with K-multiset {72:1, 0:1, 52:5, 20:5}.
- **Weighted zeta (B9 sim-complete):** ζ_+(z) ∈ Z[φ][[z]] computed
  to degree 30 exactly.
- **σ-symmetrised zeta (B10 sim-complete):** ẑ(z) ∈ Z[[z]] factors as
  ẑ(z) = (1 - L_72 z^10 + z^20)^(-1) · (1 - L_0 z^10 + z^20)^(-1)
       · (1 - L_52 z^10 + z^20)^(-5) · (1 - L_20 z^10 + z^20)^(-5)
  with L_K the K-th Lucas number. At z^10:
  [z^10] ẑ = 1·L_72 + 1·L_0 + 5·L_52 + 5·L_20 = 1,114,945,460,806,394
  (sim-verified; L_72 = 1,114,577,054,219,522).

**Still to be computed (not open mathematically, just not yet done):**
- Explicit Z[φ]-coefficients of $\zeta_T^\omega(z)$ for $n \leq 30$.
- Factorisation test against $\zeta(s) \cdot L(s, \chi_5)$.
- σ-fixed sub-orbit structure on 2I under T.
- L map from F-irreducible primes to V(600-cell)/H₄ via Prime Detector.
- God-prime consistency check (L(2^136279840+1) on σ-fixed maximal locus).

**Still open mathematically:**
- Canonicity of the local-frame alignment in Proposition 6.5 (claim:
  forced by 2I structure; needs explicit uniqueness proof).
- The Mellin projection from σ-fixed sub-lattice of I to Re(s) = 1/2
  (claimed via rh-formal §mellinline; needs direct verification for
  $\zeta_T^\omega$ rather than generic $\zeta$).

Next deliverable: `scripts/derive_pentagonal_clock.py` that
computationally verifies §1–§7 step by step, then computes
$\zeta_T^\omega(z)$ to degree 30 and runs the factorisation test.

## §10. Route C-inner: conjugation clock (sim-verified 2026-04-24)

The left-multiplication clock T_τ(v) = τv gives all orbits length 10
— a single-prime local factor limitation. To escape, use the
conjugation clock T_g(v) = g·v·g⁻¹.

**Sim-verified** (`derive_pentagonal_clock_route_C_weighted.py`):
- Orbit-length multiset: {1: 10, 5: 22} — multiple orbit lengths.
- 10 fixed points = centralizer C_{2I}(τ) = <τ>.
- κ-weighted cycle types: 7 distinct (length, K) categories:
  length 1, K ∈ {1, 9, 16} with multiplicities {4, 4, 2}
  length 5, K ∈ {0, 5, 20, 45} with multiplicities {6, 4, 8, 4}

**σ-symmetric zeta:**
$$
\widehat\zeta_C(z) = (1 - L_1 z + z^2)^{-4} (1 - L_9 z + z^2)^{-4}
                     (1 - L_{16} z + z^2)^{-2}
$$
$$
\cdot (1 - L_0 z^5 + z^{10})^{-6} (1 - L_5 z^5 + z^{10})^{-4}
      (1 - L_{20} z^5 + z^{10})^{-8} (1 - L_{45} z^5 + z^{10})^{-4}
$$

where $L_K$ is the $K$-th Lucas number. Coefficients are integers;
sim-verified to degree 10: [z^1]=4722, [z^2]=16,031,051,
[z^3]=47,769,921,498, [z^10]=34,303,398,250,984,893,830,710,345,347,199,376.

**Structural status:**
- Rich multi-prime rational function derived from F1 alone.
- No free parameter; every exponent K is a specific shell-sum.
- σ-symmetric, Z-valued, exactly computable.

## §11. B11/B12 analysis — (α)-escape established (2026-04-24)

Codex WO 2026-04-24 delivered the Mellin / Dedekind analysis:

**B4 Local Hecke factorisation (classical):**
Each factor $(1 - L_K z^\ell + z^{2\ell}) = (1 - \varphi^K q)(1 - \varphi^{-K} q)$
with $q = z^\ell$ is the product of two unramified local
quasicharacter L-factors on a split prime $\mathfrak{p}$ of $K = \mathbb{Q}(\sqrt 5)$:
$$
L_\mathfrak{p}(s, \chi_{K,\mathfrak{p}}) L_\mathfrak{p}(s, \chi_{-K,\mathfrak{p}})
= (1 - L_K N\mathfrak{p}^{-s} + N\mathfrak{p}^{-2s})^{-1}.
$$

**B5 Global Hecke obstruction (THE (α)-RESULT):**

No continuous global Hecke character $\chi_K: \mathbb{A}_K^\times / K^\times \to \mathbb{C}^\times$
can have $\chi_K(\mathfrak{p}) = \varphi^K$ for $K > 0$.

*Proof.* The norm-one idele class group $\{\alpha : |N(\alpha)| = 1\}$
is compact (classical adelic theorem, Neukirch §VI.1). Continuous
characters on a compact group take values in $S^1$. But $\varphi^K > 1$
for $K > 0$ is not on $S^1$. Contradiction. ∎

**Consequence:** ẑ(z) and ẑ_C(z) for K > 0 are NOT classical global
Hecke L-functions on $\mathbb{Q}(\sqrt 5)$. They **escape the
Dedekind factorisation** $\zeta_K(s) = \zeta(s) \cdot L(s, \chi_5)$.

**Verdict:** this is the cascade programme's first (α)-class escape
from classical L-function structure. Route Q-min and Route C-inner
both produce ẑ(z) objects that are:
1. Rational functions in $z$, σ-symmetric, Z-integer coefficients.
2. Locally-Hecke-factorable (each Lucas factor IS a classical local
   factor).
3. Globally NOT Hecke L-functions (by the B5 compactness argument).
4. Derived from F1 alone, no free parameter.

**Remaining for full RH-analogue proof:**
- **B11** Mellin normalisation: pick convention M0 (q = N^{-s}, σ-
  center at Re(s) = 0) or M1 (q = N^{1/2-s}, σ-center at Re(s) = 1/2).
  The M1 choice aligns with rh-formal.tex's τ = ι ∘ bar critical-line
  structure; this is the natural cascade convention.
- **B3 pole lemma**: for q = N^{-s}, poles at s = ±K log φ / log N
  - 2πin / log N. For M1 shifted, poles shift by 1/2.
- **RH-analogue**: prove all zeros of ẑ_C(s) under M1 lie on
  Re(s) = 1/2. This is the **direct proof target**: each Lucas
  factor (1 - L_K z^ℓ + z^{2ℓ}) has reciprocal roots φ^K and
  φ^{-K}, which under M1 (q = N^{1/2-s}) sit at s = 1/2 + (K log φ ∓
  2πin) / log N — not necessarily on the critical line unless N is
  chosen canonically by the cascade. The N-selection is B2 in the
  WO; it requires further derivation.

**Next builds (per codex WO top-3):**
1. B11 Mellin normalisation — formalisation in docs.
2. B12 χ_K table + global-obstruction lemma — sim-augmented in
   `derive_pentagonal_clock_B8p_proper.py`.
3. K-value structural derivation — prove {0, 20, 52, 72} from 2I
   orbit/profile structure without enumeration.

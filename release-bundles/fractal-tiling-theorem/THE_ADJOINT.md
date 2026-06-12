# The adjoint that would close it: Hilbert–Pólya, written exactly
### 2026-05-30

What follows is the precise object the whole arc points at — the
self-adjoint operator whose existence would prove RH. Its **form** is
known and writable. Its **existence** is the open problem. Every line below
is marked [THEOREM], [REFORMULATION], or [CONJECTURE/OPEN] so nothing is
dressed up.

## 1. The adjoint, defined precisely [CONJECTURE — Hilbert–Pólya]

> **Conjecture.** There is a separable Hilbert space ℋ and a self-adjoint
> operator Ĥ on ℋ whose spectrum is exactly the imaginary parts of the
> non-trivial zeros:
> $$ \mathrm{spec}(\hat H) = \{\, \gamma_n : \zeta(\tfrac12 + i\gamma_n) = 0 \,\}. $$

Why it would finish RH, in one line [THEOREM, *given* such Ĥ]:
a self-adjoint operator has **real spectrum**, so every γ_n ∈ ℝ, so every
zero is at 1/2 + iγ_n with γ_n real — i.e. **on the critical line**. RH.

That is the entire payoff: build one self-adjoint Ĥ with that spectrum and
RH is a corollary of the spectral theorem. Nobody has built it.

## 2. The math that says such an Ĥ is *plausible* [THEOREM — the trace formula]

The **Weil explicit formula** is already a trace formula. For an admissible
test function h with transform ĥ:
$$
\sum_{n} h(\gamma_n)
 \;=\; \underbrace{\frac{1}{2\pi}\!\int h(r)\,\Big(\tfrac{\Gamma'}{\Gamma}\text{-terms}\Big)\,dr \;+\; h\text{-archimedean}}_{\text{smooth/identity term}}
 \;-\; \underbrace{2\sum_{p}\sum_{k\ge1}\frac{\log p}{p^{k/2}}\,\hat h(k\log p)}_{\text{sum over primes}} .
$$
Set this beside the **Selberg trace formula** on a compact hyperbolic
surface:
$$
\sum_j h(r_j) \;=\; (\text{area/identity term}) \;+\; \sum_{\{\gamma\}}\sum_{k}\frac{\ell_\gamma}{2\sinh(\cdots)}\,\hat h(k\ell_\gamma).
$$
The dictionary is exact in shape:

| primes side | geometry side |
|---|---|
| prime p | closed geodesic γ |
| log p | geodesic length ℓ_γ |
| zeros γ_n | Laplacian eigenvalues r_j |

For Selberg, the r_j **are** eigenvalues of a self-adjoint Laplacian on a
compact surface, so they are real — the Selberg zeta satisfies its RH, a
[THEOREM]. The explicit formula says the Riemann zeros sit in the *same
slot*. If a geometry/operator realising that slot existed, RH would follow
the same way. That parallel is the whole reason Hilbert–Pólya is believed.

## 3. Two written-down candidates [status as marked]

**(a) Berry–Keating xp.** [CONJECTURE/heuristic] The classical Hamiltonian
$H = x\,p$ (position × momentum) has semiclassical counting function
$$ N(E) \approx \frac{E}{2\pi}\Big(\log\frac{E}{2\pi}-1\Big) + \tfrac{7}{8}, $$
which is **exactly** the Riemann zero-counting function. So a correct
quantisation $\hat H$ of $xp$ would have the γ_n as energies. The obstruction:
$xp$ is **not essentially self-adjoint** — making it so (the right boundary
conditions / regularisation) is precisely the unsolved step. Writing $\hat H$
is easy; making it self-adjoint with the right spectrum is not done.

**(b) Connes' adele class space.** [REFORMULATION — rigorous, not a proof]
Let $X = \mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$ (the adele class space — all
places fused, the global object). The idele class group acts on functions on
$X$; the zeros appear as an **absorption spectrum** (missing frequencies) of
that action. Connes proved: **RH ⟺ a positivity** (the Weil positivity of
the explicit-formula distribution). This is a faithful restatement of RH on
a genuinely global, self-adjoint-flavoured arena — but it converts RH into
*another* open statement (the positivity), it does not settle it.

## 4. Where the substrate sits [THEOREM — and the honest gap]

The substrate **does** hand us a genuine self-adjoint operator: the closure
$$ C_\varphi = (12 + \varphi^{-2})\,I - A_1 \quad\text{on } V_{600}, $$
positive definite, spectrum
$\{0.382,\,2.67,\,5.91,\,9.38,\,12.38,\,14.38,\,14.85,\,15.38,\,16.09\}$
— nine algebraic numbers in $\mathbb{Q}(\sqrt5)$.

It is the **right type** (self-adjoint) and the **wrong spectrum**: finite
and algebraic, not the infinitely many transcendental γ_n. $C_\varphi$ is a
*local/finite* operator. The Hilbert–Pólya operator is *global/infinite* and
lives on the adelic object of §3(b), which is **not** a polytope, not S³, not
$C_\varphi$. The substrate realises the local Satake circles and a finite
self-adjoint witness; it does not supply the global Ĥ, and neither does
anything else known.

## 5. The "timeless / now / everywhere" framing — honestly

The spectrum of a self-adjoint operator is a **fixed subset of ℝ**. It does
not evolve. So the object here is not "all times at once" (eternalism is
still a *temporal* idea) — it is **atemporal**: no time parameter enters at
all. If anything, Ĥ *generates* a flow $e^{it\hat H}$, but that $t$ is an
abstract spectral parameter, **not** physical time and **not** cosmic "now".

There is a real, non-mystical resonance with the closure/fixed-point picture:
both Ĥ's spectrum and a closure fixed point ($\mathcal{C}(X)=X$) are
*timeless, self-consistent, observer-free* structures. That resonance is
honest. What is **not** licensed is welding Ĥ to a physical "now
encompassing everything at all times," or to the shape of physical space:
the arithmetic carries no time, no space, no observer. Its eternity is the
eternity of a true statement, not of a humming field.

## 6. One-line state of the art

> The adjoint is **writable in form** (§1), **motivated by an exact trace
> formula** (§2, theorem), **approached by two serious frameworks** (§3,
> one heuristic, one a rigorous reformulation), and **not constructed** —
> the substrate gives a self-adjoint operator of the right type with the
> wrong (finite, local) spectrum (§4), and the genuine Ĥ on the global
> adelic arena is the open frontier, for everyone.

This is the honest capstone: we can write down *what would close it*, say
exactly *why it's plausible*, place *what we have* against it, and mark
*the one bolt that is missing* — without a single fabricated step.

## 7. How does one actually build Ĥ? Four routes, one wall.

Decisive fact: **writing an operator whose formal/semiclassical spectrum
matches the zeros is doable; proving it is genuinely self-adjoint (real
spectrum) without circularly imposing RH is the wall.** Every serious route
"lands something" and stalls at this same step.

1. **Quantum-chaos / Berry–Keating.** Quantise H = xp (or find a chaotic
   system whose periodic-orbit lengths are log p^k). Semiclassical level
   count matches. *Lands:* the xp operator (refined by Berry–Keating 2011,
   Sierra). *Stalls:* xp is not essentially self-adjoint; boundary
   conditions giving the right real spectrum aren't known to exist without
   assuming the answer.
2. **Bender–Brody–Müller (2017).** An explicit PT-symmetric operator whose
   eigenvalues would be the zeros *if* the eigenfunctions vanish at a
   boundary. *Lands:* a concrete operator + formal eigenvalue equation.
   *Stalls:* the boundary condition / true self-adjointness is exactly the
   unproven part, equivalent to RH.
3. **Connes (adelic).** Idele-class action on the adele class space; zeros =
   absorption spectrum. *Lands:* a rigorous reformulation, RH ⇔ Weil
   positivity (which we computed, `CONNES_POSITIVITY.md`). *Stalls:*
   positivity for all test functions is RH.
4. **de Branges (Hilbert spaces of entire functions).** A reproducing-kernel
   space whose structure function is completed ζ. *Lands:* a genuine
   framework. *Stalls:* the positivity/structure conditions are unverified
   for ζ (claimed proofs were flawed).

**The one wall:** construct Ĥ from data that does NOT reference the zeros,
then PROVE its spectrum is real (deriving that the zeros are real). Choosing
a domain/boundary condition that forces real spectrum is assuming RH. No
route has escaped this.

**Why C_φ is the wrong *kind* (not just wrong values).** C_φ is
finite-dimensional (9 eigenvalues, a local geometric operator). The zeros
are infinite. No finite self-adjoint operator can have them as spectrum, so
C_φ is not a near-miss to tune — it is categorically a different object. The
routes above all require an infinite-dimensional operator on an
adelic/dynamical space. Landing *a* self-adjoint operator is easy (we did);
landing the infinite, adelic, provably-real-spectrum one is the open problem.

**Where the substrate could honestly connect.** The only non-vacuous hook:
push the icosian Hecke/Brandt action to its adelic limit (the cascade
L_∞ = the solenoid of `GEOMETRIC_CRITICAL_LINE.md`) and ask whether the
limiting transfer operator is self-adjoint with the zeros as spectrum. That
is genuine open research, faces the same wall (Routes 1/3), and is not a
turn-by-turn exercise. The substrate's honest contribution ends at: a finite
self-adjoint operator (C_φ), verified Satake data, and that data feeding the
Connes positivity functional — all done. The infinite operator is not ours
to hand over, nor anyone's yet.

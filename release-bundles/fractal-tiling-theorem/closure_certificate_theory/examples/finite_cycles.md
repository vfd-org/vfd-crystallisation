# Example: finite cycles — the isometric certificate

**System.** $X=\mathbb R^d$, $T=$ the $k$-cycle permutation matrix ($T^k=I$).

**Mode.** ISOMETRIC. Eigenvalues are the $k$-th roots of unity $\{e^{2\pi i j/k}\}$ — on
the unit circle, off the real axis (for $k\ge3$), so **not** self-adjoint.

**Certificate (exact, finite).** The Weyl average
$$B=\frac1k\sum_{j=0}^{k-1}(T^{\mathsf T})^j T^j$$
satisfies $T^{\mathsf T}BT=B$ exactly and $B\succ0$ (Lemma 2). For a permutation $T$,
$B=I$ already works. This is a single $d\times d$ matrix + one equality check: a finite
object certifying that **all** powers $T^n$ preserve $\|\cdot\|_B$ — the phase returns.

**Why it matters.** This is the cleanest realisation of the corrected hypothesis: triad
/ cyclic closure is *isometric*, not self-adjoint. The certificate for "the phase comes
back" is an invariant inner product, not a symmetrizer.

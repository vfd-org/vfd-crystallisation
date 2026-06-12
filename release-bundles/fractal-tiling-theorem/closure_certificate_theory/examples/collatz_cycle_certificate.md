# Example: Collatz — the cycle certificate (and the wall)

**System.** Shortcut map $T_3(n)=(3n+1)/2^{a(n)}$ on odd $n$, $a(n)=v_2(3n+1)$.

**The finite certificate (Lemma 4 + Proposition 1).** A $k$-cycle forces the exact
Diophantine identity
$$n_1\,(2^{A}-3^{k})=\sum_{i=1}^{k}3^{\,k-i}\,2^{\,s_{i-1}},\qquad 2^A>3^k .$$
For $k=1$: $n_1(2^a-3)=1\Rightarrow 2^a-3=1\Rightarrow a=2,\ n_1=1$. **Only the trivial
cycle $1\mapsto1$.** This single equation eliminates the entire infinite family of
hypothetical one-step cycles — and recovers Steiner (1977) by the closure route.
Exhaustive check (`verify_certificates.py`) finds no nontrivial odd cycle for $k\le6$.

**The wall (OPEN).** The cycle certificate controls **periodic** escape. The Collatz
conjecture also requires excluding **aperiodic** unbounded trajectories: no admissible
*infinite* braid keeps cumulative capacity $Q=\sum (a_i\ln2-\ln3)\le0$ forever. The mean
drift is $+ (2\ln2-\ln3)>0$ (DIAGNOSTIC), but the mean does not certify every individual
braid. **That missing infinite certificate is the conjecture itself.** The framework
sharpens *where* the wall is; it does not remove it.

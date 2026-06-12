# Example: Markov chains — self-adjoint vs dissipative certificates

**System.** $X=$ probability simplex, $T=P$ a stochastic matrix, stationary measure $\pi$.

**Reversible case (detailed balance $\pi_iP_{ij}=\pi_jP_{ji}$).**
- Mode: SELF_ADJOINT in $\ell^2(\pi)$.
- Certificate: $B=\operatorname{diag}(\pi)$ gives $BP=P^{\mathsf T}B$ (Corollary 1).
  Finite, checkable, and forces **real spectrum**.

**Ergodic non-reversible case (e.g. a noisy directed cycle).**
- Mode: DISSIPATIVE on the mean-zero subspace $\mathbf 1^\perp$ (complex spectrum, but
  $\rho(P|_{\mathbf 1^\perp})<1$).
- Certificate: the spectral gap $1-|\lambda_2|>0$; $\operatorname{diag}(\pi)$ is a
  contraction certificate there (Lemma 1). The chain **closes onto $\pi$**.

**Reading.** Both chains close; reversibility is exactly the extra fact that the
dissipative closure is *also* self-adjoint (real spectrum). The certificate distinguishes
the two — a worked instance of the mode taxonomy.

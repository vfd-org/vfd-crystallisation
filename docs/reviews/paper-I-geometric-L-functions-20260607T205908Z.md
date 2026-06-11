**Claim Audit**
- “icosian theta series … realizes `ζ_K(s)ζ_K(s-1)`” (ll. 32-33, 106-121): not established as stated. The proof sketch suppresses the Hilbert theta definition, level, character, local factors, and normalization. With the paper’s line-80 classical one-variable theta definition, the underlying `E_8` lattice would instead suggest the classical `E_4` theta series, not this Hilbert/Dedekind product.
- “24-cell … realizes `ζ(s)ζ(s-1)`” (ll. 33-35, 141-145): not proved. It is plausible for a normalized Hurwitz quaternion theta series, but the unnormalized theta has a unit-count factor, e.g. coefficient 24 at norm 1. The paper never states the normalization.
- “Galois twin … carries `L(s,χ_5)`” (ll. 36-38, 165-168): not established. No mathematical construction of the shell-to-Dirichlet-`L` map is given; the local verification engine uses precomputed target zero lists.
- “icosian ring is a maximal order … associated lattice is `E_8`” (ll. 45-49): standard and plausibly correct, but only cited, not used carefully. `E_8` uniqueness does not imply quaternion ideal class number one.
- Dedekind factorization `ζ_K(s)=ζ(s)L(s,χ_5)` (ll. 64-71): correct.
- Lemma 3.1, “`Icos` has class number one” (ll. 89-94): the claim is likely correct. Kirschmer-Voight do list the class-number-one definite Eichler case over `Q(√5)` with finite discriminant/level `(D,N)=(1,1)`; cite their Table 8.2/Proposition 8.1 explicitly. But the proof’s Conway-Sloane route (ll. 100-103) is invalid for quaternion ideal classes: uniqueness of the even unimodular rank-8 `Z`-lattice does not prove one left-ideal class of the maximal order.
- “single left-ideal class, equivalently one class in its genus” (ll. 93-94): too compressed. Which genus: underlying `Z`-quadratic lattice, `O_K` norm lattice, or locally principal ideal genus? These are not interchangeable.
- Proposition 3, “`L(Θ_Icos,s)=ζ_K(s)ζ_K(s-1)`” (ll. 106-121): not proved. Siegel-Weil plus one class can kill the cusp contribution only after specifying the exact genus, measure/weighting, Hilbert modular theta series, and normalized Eisenstein series. The paper gives none of these.
- Remark, “would acquire cuspidal `L`-factors beyond…” (ll. 123-127): mathematically sloppy. An individual theta series decomposes into Eisenstein plus cusp forms; its Dirichlet series is a sum/linear combination, not literally a product acquiring extra factors.
- Numerical corroboration “all `K`-primes of norm ≤ 200” (ll. 130-133, 177-185): not verified from Paper I. Local `vfd_math_engine/run_programme.py` builds the icosian spectrum as `sorted(RIEMANN+LCHI5)` directly. `route_b/short_vectors.py` only checks small norms `4,5,9,11`. The norm-≤200 material I found belongs mainly to a separate level-31 cuspidal Brandt project.
- Proposition 4/6, “zeros of `ζ(s)ζ(s-1)` on `Re(s)=1/2` are exactly the nontrivial zeros of `ζ`” (ll. 147-155): intended statement is true only if read as “the zeros of `ζ` that lie on that line.” As written it sounds like all nontrivial zeta zeros. The proof also ignores trivial zeros of `ζ(s-1)` and possible pole/zero cancellation, though neither affects the conclusion.
- “disjoint from the Riemann zeros” for `L(s,χ_5)` (ll. 167-168): finite-precision numerics cannot prove disjointness of zero sets.
- Verification table/GUE claims (ll. 190-201): overclaimed. The numbers are consistent with target `L`-functions already fed into the computation; they are not independent evidence of geometric realization, and “independent spectra” is not proved.

**Internal Consistency**
- The line-80 theta definition is a classical lattice theta series, but Section 3 needs a Hilbert theta series over `K`. This is the central notation conflict.
- `L(Θ,s)` is undefined: standard/Hecke/Mellin? completed or finite? normalized or raw coefficient series?
- `Result~\ref{res:icosian}` refers to a proposition (ll. 140, 170, 205). Harmless but sloppy.
- Line 171 says the icosian object carries `ζ_K ζ_K(s-1)`, but line 214 says it realizes `ζ_K`; Paper II also labels it “icosian -> ζ_K.” Product vs single factor is inconsistent.
- Line 172 writes `L(χ_5,s-1)`; standard notation is `L(s-1,χ_5)`.
- Cross-references resolve in the existing `.aux`. LaTeX compiles, but hyperref warns about math in section titles at lines 84, 138, 162; use `\texorpdfstring`.

**External Consistency**
- Kirschmer-Voight: verified at the invariant level from their paper [arXiv:0808.3833](https://arxiv.org/abs/0808.3833) / [PDF](https://jvoight.github.io/articles/quatideal-fixed-errata-111614.pdf). The citation should identify Table 8.2 and the `(n,d_F,D,N)=(2,5,1,1)` entry. The current generic citation is too vague.
- Conway-Sloane: supports `E_8` uniqueness, not quaternionic ideal class number one. Do not present it as an independent proof of Lemma 3.1.
- Companion Paper II: it claims certificates for the same correspondences, but locally `run_programme.py` sets builders to `RIEMANN`, `LCHI5`, or their union. This verifies labels against themselves, not geometry against arithmetic.
- `icosian_brandt_cuspidal_geometry`: locally supports a separate level-31 cuspidal Brandt computation and an enumerator anchor, not the Section 3 level-one Siegel-Weil identity as written.

**Tightness**
- ll. 34-35: replace with “whose zeros on `Re(s)=1/2` are exactly the zeros of `ζ(s)` lying on that line.”
- ll. 98-103: replace with “Kirschmer-Voight Table 8.2 gives class number one for `(K,D,N)=(Q(√5),1,1)`; the icosian order is a maximal order in this algebra.” Delete the Conway-Sloane sentence.
- ll. 110-121: add “after normalizing the first nonzero Fourier coefficient” or include the missing unit factor.
- ll. 118-121: replace “hence” with “provided this is the one-class genus for the Hilbert norm lattice…”
- ll. 167-168: replace “are disjoint” with “no coincidences were observed in the tested range.”
- ll. 198-201: replace “show” and “characteristic of” with “are consistent with.”

**Surface Issues**
- `fp` in the table (l. 190) is not defined in Paper I.
- Bibliography entries are too imprecise for load-bearing claims: no theorem/table/page numbers.
- `\renewcommand{\Theta}{\vartheta}` is legal but confusing; the paper then uses both theta-function and theorem/proposition language loosely.
- The user’s “Proposition 4.5” does not exist in this file; the zero proposition is theorem-counter number 6.
- Several phrases use “critical line” for different products without defining the completed/function-specific normalization.

**Top Three Fixes**
1. Fix Section 3 (ll. 80, 106-121): define the Hilbert theta series over `K`, specify normalization, level, character, and finite/completed `L`-function. Then prove or cite the exact Eisenstein `L`-series computation.
2. Fix Lemma 3.1 (ll. 89-103): cite Kirschmer-Voight precisely and remove the false Conway-Sloane-to-class-number argument.
3. Downgrade the verification/RH-adjacent language (ll. 34-35, 147-160, 165-185, 198-201): distinguish exact theorem, finite numerical check, and hardcoded target comparison. Overclaiming here is the paper’s main failure mode.

# Does the zero-side tile? Yes — it is a quasicrystal. (2026-05-30)

Testing the "fractal and tiles" intuition for the outside (zero) structure,
via Dyson's quasicrystal picture. `route_b/diffraction_quasicrystal.py`.

## The test
A point set is a quasicrystal iff its diffraction (Fourier transform of the
point measure) has sharp Bragg peaks. We form, from the first 40 Riemann
zeros,
$$ D(t) = \sum_n \cos(\gamma_n t) \quad(\text{windowed}), $$
and ask whether its extrema land on $t=\log(p^k)$ for prime powers.

## The result (verified)
Every prime-power position up to $t\approx2.83$ is matched by a diffraction
extremum, to offset $<0.003$:

| $p^k$ | $\log(p^k)$ | nearest $D$ extremum | offset |
|---|---|---|---|
| 2 | 0.6931 | 0.6938 | 0.0007 |
| 3 | 1.0986 | 1.0995 | 0.0009 |
| $2^2$ | 1.3863 | 1.3865 | 0.0002 |
| 5 | 1.6094 | 1.6103 | 0.0009 |
| 7 | 1.9459 | 1.9454 | 0.0005 |
| $2^3$ | 2.0794 | 2.0767 | 0.0028 |
| $3^2$ | 2.1972 | 2.1961 | 0.0012 |
| 11 | 2.3979 | 2.3986 | 0.0007 |
| 13 | 2.5649 | 2.5655 | 0.0006 |
| $2^4$ | 2.7726 | 2.7737 | 0.0011 |
| 17 | 2.8332 | 2.8325 | 0.0007 |

**11/11 matched.** The zeros diffract into the primes: the OUTSIDE (zeros)
is a quasicrystal whose Bragg peaks are the INSIDE (prime powers). This is,
exactly, the explicit formula seen as a diffraction pattern.

## The bigger picture this revises
Zeros and primes are **one self-dual object** seen two ways: the prime
"tiling" (multiplicative atoms) and the zero "tiling" (quasicrystal) are
Fourier-dual. For our substrate L-function the identical picture holds with
the **substrate primes** (the Satake norms $N\mathfrak{q}$) as the Bragg
peaks of its zeros. So the substrate's verified prime data and the zero-side
quasicrystal are the same structure, inside-out.

## Why this is not (yet) a proof — the honest line
- **Peak LOCATIONS = prime powers regardless of RH.** The diffraction peaks
  sit at $\log p^k$ whether or not the zeros are on the line. So matching
  them confirms the duality, not RH.
- **Peak SHARPNESS is what RH controls.** Pure-point (perfectly sharp)
  diffraction $\Leftrightarrow$ all $\gamma_n$ real $\Leftrightarrow$ RH.
  Off-line zeros would smear the peaks. But a *finite* sample of (on-line)
  zeros cannot certify that sharpness holds *forever*.
- Hence this is **Kind-1 texture evidence**: it reveals and confirms the
  structure (and is a genuinely good intuition-builder), but the closing
  step is still **Kind-2** — proving pure-point sharpness for all zeros,
  equivalently constructing the self-adjoint operator (`THE_ADJOINT.md`).

## Do we have the full shape / how it tiles / where it closes?

A precise trichotomy:

1. **Full shape?** Half of it, exactly. The **Fourier side** (the diffraction)
   is known in closed form — it is the explicit formula: Bragg peaks at
   $t=\pm\log(p^k)$ with weights $(\log p)/p^{k/2}$, plus a smooth
   archimedean background. (So: quasicrystal-*like*, pure-point on the primes
   $+$ a continuous part — not a strict pure-point quasicrystal.) The
   **real-space side** (the actual positions $\gamma_n$) has **no closed
   form** — known only numerically.
2. **How it tiles?** In frequency, the tiling rule **is the primes** (known
   exactly). In real space, a generating/substitution rule that *produces*
   the zeros is **unknown** — having one is equivalent to a formula for the
   zeros.
3. **Where does it close?** A genuine quasicrystal is **aperiodic** — it
   never closes in its own dimension. The only way it closes is as a
   **cut-and-project** shadow of a *periodic lattice in higher dimension*
   (as Penrose tiles project from a 5D cubic lattice). That higher lattice
   is where it would close — but we do **not** know the zeros are a
   cut-and-project set, nor the lattice; finding it would essentially *be*
   the Hilbert–Pólya structure (it would give the zeros). So "where it
   closes" = the missing higher-dimensional periodic structure = the same
   open wall, in cut-and-project form.

**The substrate sits on the half we have:** it produces the primes (Satake
data) = the Bragg peaks = the Fourier-side shape, known in closed form. It
does not give the real-space positions or the closing higher lattice.

## Net
The outside structure does tile — as a quasicrystal dual to the primes, now
verified (11/11) and visualised (`outputs/30_quasicrystal_diffraction.png`).
We have exactly its Fourier half in closed form (peaks = primes); the
real-space half (positions / the higher-dimensional lattice where the tiling
closes) is the unknown, equivalent to the missing self-adjoint operator. The
substrate sits on the known half. This sharpens the picture and is the right
object to reason about; it does not prove RH.

# Hardening pass (pre-paper) — results

## B — split-prime hedge RESOLVED (the key one)
For each split prime q, the two totally-positive generators varpi and sigma(varpi)
(Galois conjugate) give the two Hecke eigenvalues; the geometric set {a(varpi),a(sigma varpi)}
equals the full point-count target set {a_q, a_q'} EXACTLY:

  q=11 {-4,4}=tgt ; 19 {-4,4} ; 29 {-2} ; 41 {-6} ; 59 {-4,12} ; 61 {-2,6} ;
  71 {-8,0} ; 79 {0,16} ; 89 {-6,10}   -- FULL MATCH all 9, self-adjoint gate held.

=> The earlier "match up to the global Galois involution" hedge is REMOVED. The geometry
reproduces the COMPLETE eigenvalue set at every split prime. (29,41 give a single value =
a_q=a_q', matching the singleton target.) Reviewer attack closed.

## M — Eichler mass-formula consistency
orbit sizes (12,20) -> stabilisers (5,3) -> mass = 1/5+1/3 = 8/15 = (1/60)(N(p)+1).
Holds (automatically, by orbit-stabiliser: Sum 1/stab = (q+1)/60). Confirms h is the genuine
Brandt dimension. Sanity check, not an independent proof.

## A, C — need EXTERNAL data (the "one form vs family" question, eigenvalue level)
- A (full dimension-table cross-check): our orbit-count cuspidal-dimension sequence
  (0,0,0,1,1,2,3,...) matches the FAMOUS threshold (first form at norm 31, Dembele). The full
  cross-check needs the LMFDB / Dembele dimension table for S_2(Gamma_0(p)) over Q(sqrt5).
- C (second-form eigenvalue verification): needs (i) generalising the Hecke build to a second
  level (e.g. norm 41, cuspidal dim 1) and (ii) that form's independent target (its elliptic
  curve's Weierstrass equation over Q(sqrt5), or LMFDB eigenvalues). Equation for 31.1-a1 we
  have; a second curve's data we do not.

## Honest scope now
VERIFIED, no external data: full eigenvalue set of ONE form (level 31, both primes, all
in-/out-of-sample primes), dimension SEQUENCE across many levels (threshold matches), W_31,
self-adjoint single common eigenform. This is already a solid, honest, modest paper.
UPGRADE to "family at eigenvalue level" requires the LMFDB Q(sqrt5) data (A,C).

## A — DIMENSION SEQUENCE CONFIRMED vs Dembele (decisive "family" evidence)
Cross-checked our geometric orbit-count cuspidal-dimension sequence against Dembele
(Experimental Math 14(4), 2005), the authoritative source, at every prime level he tabulates:

  level(prime norm)  our geom   Dembele                                   match
  31                 1          dim 1 elliptic (Ex 3.4, smallest cusp form)  YES
  41                 1          dim 1 elliptic                               YES
  59                 0          0  (Ex 3.6: only Eisenstein at wt (2,2);     YES
                                    NO elliptic curve of conductor norm 59)
  61                 2          dim 2 GENUS-2, irrational eigenvalues in     YES (***)
                                Q(sqrt5) (Rem 4.4: "smallest norm with a
                                form with coefficients in a field bigger
                                than Q"; abelian surface, RM by Q(sqrt5))
  71                 1          dim 1 elliptic                               YES
  79                 1          dim 1 elliptic                               YES
  89                 1          dim 1 elliptic                               YES

=> 7/7 over the full prime range Dembele covers. The geometry independently reproduces the
ENTIRE prime-level Hilbert-newform dimension sequence over Q(sqrt5), including the two SUBTLE
cases: the 59 gap (no (2,2) cusp form) and the 61 jump to a non-rational genus-2 form
(confirmed directly: level-61 column in Dembele Table 3 has eigenvalues 2w5-2, -3w5+1, ...).
LMFDB cross-check consistent: smallest EC conductor norm = 31; 0 elliptic curves at 59 and 61;
71,79,89 each have 1 isogeny class per prime. "One form vs family": FAMILY (at dimension level).
HONEST: this reproduces KNOWN results (Dembele 2005) by an independent geometric route — a strong
validation, not new mathematics.

## C — now UNBLOCKED (second-form eigenvalues)
Dembele Table 3 publishes the genuine Hecke eigenvalues a_p,f for the elliptic levels
(41,71,79,89). These are ready-made out-of-sample TARGETS for a second-form eigenvalue
verification. Remaining work = generalise the level-31 Brandt-Hecke build to a second level
(real code, ~ the bundle's machinery re-pointed). No longer blocked on data.

## C — SECOND FORM verified out-of-sample (family at the EIGENVALUE level) -- DONE
Re-pointed the Brandt-Hecke build to level 41 (compute_orbits_p(41); P^1(F_41)=42 pts, h=2,
cuspidal dim 1 -> matches Dembele 41=elliptic). The level-41 cuspidal eigenform is genuine:
self-adjoint + integral + Ramanujan |a_q|<=2sqrt(N(q)) at 9 primes. Then OUT-OF-SAMPLE vs the
brute-force point count of Dembele's curve E_41: y^2 + phi y = x^3 - phi x^2 (Table 4
[0,-phi,phi,0,0]): full eigenvalue SETS {a_q,a_q'} match at q=11,19,29,31,59,61,71,79,89 (9/9),
NO fitting. => The geometry reproduces a SECOND independent Q(sqrt5) Hilbert newform
eigenvalue-for-eigenvalue. Family confirmed at the eigenvalue level (forms 31 AND 41).
Script: route_b/second_form_level41.py.

## FLOURISH — genus-2 form at level 61 reconstructed (the non-rational form) -- DONE
compute_orbits_p(61): P^1(F_61)=62, h=3, orbit sizes [12,20,30] -> cuspidal dim 2 = genus-2
abelian surface (Dembele Rem 4.4). From the 3x3 Brandt matrix B(varpi), eigenvalues are
{N+1, a_q, sigma a_q}; read Tr(a_q)=trace(B)-(N+1), N(a_q)=det(B)/(N+1).
RESULT at primes N(q)=4,9,11,19,29,49: discriminant Tr^2-4N(a) = 5*(perfect square) at EVERY
prime => a_q in Z[phi], IRRATIONAL (real multiplication by Q(sqrt5) -- the "first form with
coefficients in a field bigger than Q"). Inert primes match Dembele's published eigenvalues
EXACTLY: a_4=2w-2 (Tr,N)=(-2,-4); a_9=-w-2 (-5,5); a_49=-4w+2 (0,-20). Ramanujan holds on both
embeddings. => Geometry reconstructs not just the dim-2 count but the genus-2 form's actual
irrational Hecke eigenvalues. Script route_b/genus2_form_level61.py.

## HARDENING SUMMARY (B,M,A,C,flourish all PASS)
The icosian/600-cell geometry reproduces, parameter-free and out-of-sample:
 - the FULL eigenvalue set of TWO rational forms (levels 31 & 41), both primes;
 - the ENTIRE prime-level dimension sequence over Q(sqrt5) (7/7 vs Dembele, incl. 59-gap, 61-jump);
 - the genus-2 form at level 61, including its irrational (RM-by-Q(sqrt5)) eigenvalues.
Family confirmed at dimension AND eigenvalue level, rational AND non-rational forms.
HONEST: independent geometric reproduction of KNOWN results (Dembele 2005); strong validation,
not new mathematics; RH wall untouched.

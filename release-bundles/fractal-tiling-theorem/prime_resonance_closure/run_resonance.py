"""
WO-RH-PRIME-RESONANCE-CLOSURE-001 — test harness (faithful to the spec).

Prime phase field:   P_sigma(t) = sum_{p<=X} p^{-sigma} e^{-i t log p}
Mirror field:        P_{1-sigma}(t)
Leakage:             L_X(sigma,t) = | P_sigma(t) - conj(P_{1-sigma}(t)) |

Claim under test:  L is uniquely small / vanishes at sigma=1/2, and zero-heights gamma_n
show distinguished (low-leakage) behaviour vs controls (Gram points, random t, off-axis).
This is the honest probe: does the resonance principle have real content, or is the metric
a near-tautology with no special structure at the critical line / at zeros?
"""
import mpmath as mp, math, statistics
mp.mp.dps = 20

X = 200000
# primes up to X (sieve)
sieve = bytearray([1])*(X+1); sieve[0]=sieve[1]=0
for i in range(2,int(X**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
primes=[i for i in range(2,X+1) if sieve[i]]
logp=[math.log(p) for p in primes]
print(f"primes up to {X}: {len(primes)}")

import cmath
def P(sigma,t):
    s=0j
    for p,lp in zip(primes,logp):
        s += p**(-sigma) * cmath.exp(-1j*t*lp)
    return s
def leak(sigma,t):
    return abs(P(sigma,t) - (P(1-sigma,t)).conjugate())

# first 10 nontrivial zero heights
gammas=[float(mp.im(mp.zetazero(n))) for n in range(1,11)]
# controls: Gram-ish points (midway-ish), random t, all in same range
import random; random.seed(0)
gram=[g+ (gammas[i+1]-g)/2 if i+1<len(gammas) else g+2.5 for i,g in enumerate(gammas)]
rnd=[random.uniform(14,52) for _ in range(10)]

print("\n[sigma=1/2]  leakage at zero heights vs controls:")
print(f"  {'gamma_n (zero)':>16} {'L(1/2)':>10}   {'Gram pt':>10} {'L(1/2)':>10}   {'random t':>10} {'L(1/2)':>10}")
Lz=[]; Lg=[]; Lr=[]
for i in range(10):
    lz=leak(0.5,gammas[i]); lg=leak(0.5,gram[i]); lr=leak(0.5,rnd[i])
    Lz.append(lz); Lg.append(lg); Lr.append(lr)
    print(f"  {gammas[i]:16.4f} {lz:10.4f}   {gram[i]:10.4f} {lg:10.4f}   {rnd[i]:10.4f} {lr:10.4f}")
print(f"\n  mean L at zeros={statistics.mean(Lz):.4f}  Gram={statistics.mean(Lg):.4f}  random={statistics.mean(Lr):.4f}")
print(f"  -> zeros distinguished by low leakage? {'YES' if statistics.mean(Lz) < 0.5*statistics.mean(Lr) else 'NO'}")

print("\n[sigma scan]  does sigma=1/2 minimise leakage at a zero height (gamma_1)?")
for sg in [0.30,0.40,0.50,0.60,0.70]:
    print(f"  sigma={sg:.2f}:  L={leak(sg,gammas[0]):.4f}")
print("  (analytic note: at sigma=1/2, P_{1-sigma}=P_{1/2}=P_sigma, so")
print("   L(1/2,t)=|P - conj P| = 2|Im P_{1/2}(t)|  -- generically NONZERO, not a node.)")
print(f"  check: 2*|Im P(1/2,gamma_1)| = {2*abs(P(0.5,gammas[0]).imag):.4f}  vs L = {leak(0.5,gammas[0]):.4f}")

"""WO-RH-PHI-BOUNDARY-001 — Cayley/Li coordinate test (honest).

Real kernel: z = 1 - 1/rho maps the critical line Re=1/2 to the unit circle
|z|=1; off-line zeros leak radially (Re>1/2 -> inside, Re<1/2 -> outside).
This is the geometry behind Li's criterion. We test it, test the negative
(off-line) case, and check the two extra claims:
  * does log_phi(|z|) ('phi-radial') do anything log(|z|) doesn't?  (no: it is
    a constant rescale)
  * the pasted diagnostic (eps=0.1 -> negative at n~89) -- recompute honestly.
"""
import math, cmath
import mpmath as mp
mp.mp.dps = 25
PHI = (1+5**0.5)/2

def zeros(n):
    return [float(mp.im(mp.zetazero(k))) for k in range(1,n+1)]

# --- A. Cayley map: critical line -> unit circle ---
print("="*66)
print("[A] Cayley map  z = 1 - 1/rho   (critical line -> |z|=1?)")
print("="*66)
g = zeros(8)
devs = [abs(abs(1 - 1/complex(0.5, gi)) - 1) for gi in g]
print(f"  on-line zeros rho=1/2+i*gamma: max ||z|-1| over 8 zeros = {max(devs):.2e}  (=> on the unit boundary)")
for eps in [+0.2, +0.1, -0.1, -0.2]:
    r = abs(1 - 1/complex(0.5+eps, g[0]))
    side = "inside" if r<1 else "outside"
    print(f"  off-line Re={0.5+eps:.1f}: |z| = {r:.5f}  ({side} the boundary)")

# --- B. phi-radial coordinate is just a constant rescale ---
print("\n"+"="*66)
print("[B] is log_phi(|z|) structurally different from log(|z|)?")
print("="*66)
for r in [1.0005, 1.05, 1.2, 0.8]:
    lr, lpr = math.log(r), math.log(r)/math.log(PHI)
    print(f"  |z|={r}:  log={lr:+.5f}  log_phi={lpr:+.5f}  ratio={lpr/lr if lr else float('nan'):.4f}")
print(f"  -> ratio is the CONSTANT 1/log(phi)={1/math.log(PHI):.4f} for every |z|.")
print("     log_phi is log times a fixed constant: a units change, NO structural")
print("     effect. 'phi-scaling makes it cleaner' is false (linearity is rescale-invariant).")

# --- C. honest recompute of the off-line Li negativity onset ---
print("\n"+"="*66)
print("[C] Li negativity onset -- recompute the pasted numbers honestly")
print("="*66)
M=150
gam=zeros(M)
online=[]
for gi in gam: online += [complex(0.5,gi), complex(0.5,-gi)]
def li(extra, nmax):
    base=[1-1/r for r in online+extra]
    return [ (sum(1-b**n for b in base)).real for n in range(1,nmax+1)]
def onset(extra,nmax):
    L=li(extra,nmax)
    neg=next((n for n,v in enumerate(L,1) if v<0),None)
    return neg, min(L)
for eps,gg in [(0.1,14.13),(0.2,14.13),(0.4,14.13),(0.4,2.0)]:
    q=[complex(0.5+eps,gg),complex(0.5+eps,-gg),complex(0.5-eps,gg),complex(0.5-eps,-gg)]
    # radial leakage of the outside partner
    zr=abs(1-1/complex(0.5-eps,gg))
    neg,mn=onset(q,300)
    print(f"  eps={eps}, gamma={gg}: outside-partner |z|={zr:.5f}; "
          f"first negative n = {neg if neg else '>300'}, min λ={mn:+.3f}")
print("  (pasted claim was eps=0.1->n~89; honest result differs: at gamma=14 the")
print("   leakage |z|~1.0005 is far too small to flip λ_n by n~89. Negativity needs")
print("   large n OR small-gamma off-line zeros, where |z| leaks substantially.)")

# --- D. 'shape of the violation' = radial escape ---
print("\n"+"="*66)
print("[D] shape of the violation: |z^n| vs n (on-line stays on boundary)")
print("="*66)
z_on  = 1-1/complex(0.5, 14.13)
z_off = 1-1/complex(0.1, 14.13)   # strongly off-line partner
for n in [1,10,50,100]:
    print(f"  n={n:>3}: |z^n| on-line={abs(z_on**n):.4f}   off-line(Re=0.1)={abs(z_off**n):.4f}")
print("  -> on-line modes stay on the boundary (|z^n|=1, pure phase = standing wave);")
print("     off-line modes spiral OUT (|z^n| grows) = the radial-leakage 'violation'.")

print("""
----------------------------------------------------------------------
HONEST SUMMARY (WO-RH-PHI-BOUNDARY-001)
----------------------------------------------------------------------
REAL & TRUE: z=1-1/rho sends the critical line to the unit circle |z|=1
(machine precision); off-line zeros leak radially (Re>1/2 inside, Re<1/2
outside); on-line modes are pure boundary phase (standing waves), off-line
modes spiral outward (the 'violation' is radial escape). This is the genuine
geometry of Li's criterion -- a clean reformulation: RH <=> all zeros on |z|=1.

PHI OVERREACH (declined by data): log_phi(|z|) is log(|z|) times the constant
1/log(phi); it has NO structural effect. phi does not enter the Cayley map and
gives no advantage. The 'phi-tension operator' inherits this: the phi is a
rescalable coupling constant, not structure.

PASTED NUMBERS CORRECTED: the claimed 'eps=0.1 -> negative at n~89' is wrong
at gamma=14 (leakage too small); negativity needs large n or small-gamma
(large-leakage) off-line zeros, consistent with the earlier detector.

SCOPE: this is a clean coordinate reformulation of Li's criterion (classical),
not a new operator and not a proof. RH still = positivity for all n (all zeros
on |z|=1). The Cayley boundary picture is the nicest way to SEE it; it does not
cross the wall.
""")

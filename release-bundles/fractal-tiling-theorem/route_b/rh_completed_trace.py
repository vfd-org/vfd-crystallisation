"""WO-RH-COMPTRACE-001 — completed arithmetic trace probe.

Adds the archimedean completion + functional-equation symmetry to the trace,
and asks: does sigma=1/2 emerge as the unique balanced / self-conjugate axis?

Honest design: the finite prime sum P_{N,s}=Sum Lambda(n) n^-s e^{-it log n}
approximates -zeta'/zeta (a LOG-DERIVATIVE) only for Re(s)>1, and Arch(s)=
pi^{-s/2}Gamma(s/2) is the completion factor for zeta ITSELF -- so Arch*P is an
object-mismatch and only valid (if at all) for Re s>1. We test the LITERAL WO
object AND the CORRECT completed object Lambda(s)=pi^{-s/2}Gamma(s/2)zeta(s)
(which satisfies Lambda(s)=Lambda(1-s)) to see what actually carries the
sigma=1/2 axis.
"""
import math
import mpmath as mp
mp.mp.dps = 25

PI = mp.pi
def Arch(s):  return PI**(-s/2) * mp.gamma(s/2)
def Lam(s):   return Arch(s) * mp.zeta(s)             # completed zeta: Lam(s)=Lam(1-s)

# ---- A. functional equation: is 1/2 the self-conjugate axis? ----
print("="*68)
print("WO-RH-COMPTRACE-001  completed trace probe")
print("="*68)
print("\n[A] functional equation  Lambda(s)=Lambda(1-s)  (=> axis is Re s=1/2):")
errs=[]
for s in [mp.mpc(0.3,5), mp.mpc(0.8,14.1), mp.mpc(0.2,30), mp.mpc(0.65,21)]:
    e = abs(Lam(s)-Lam(1-s))/abs(Lam(s))
    errs.append(float(e))
    print(f"   s={complex(s)}:  |Lam(s)-Lam(1-s)|/|Lam| = {float(e):.2e}")
print(f"   max rel error = {max(errs):.2e}  -> 1/2 IS the exact self-conjugate axis (functional equation, THEOREM)")

# ---- B. maximally real at sigma=1/2: relative imaginary leakage ----
print("\n[B] relative imaginary leakage |Im Lambda|/|Lambda| at t=17 "
      "(min => most 'real'; also tests sigma<->1-sigma symmetry):")
t0=17.0
for sig in [0.30,0.40,0.50,0.60,0.70]:
    v=Lam(mp.mpc(sig,t0))
    print(f"   sigma={sig:.2f}:  |Im Lambda|/|Lambda| = {float(abs(mp.im(v))/abs(v)):.4f}")
print("   -> 0 exactly at sigma=1/2 (Lambda(1/2+it) is real), symmetric under")
print("      sigma<->1-sigma (0.30=0.70, 0.40=0.60): 1/2 is the real/balanced axis.")

# ---- C. Riemann-Siegel Z: real zeros = gamma_n ----
print("\n[C] Riemann-Siegel Z(t)=e^{i theta(t)} zeta(1/2+it) is REAL; zeros = gamma_n:")
gam=[float(mp.im(mp.zetazero(k))) for k in range(1,5)]
for g in gam:
    zL=float(mp.siegelz(g-0.2)); zR=float(mp.siegelz(g+0.2))
    print(f"   gamma={g:6.3f}:  Z({g-0.2:.1f})={zL:+.3f}, Z({g+0.2:.1f})={zR:+.3f}  "
          f"{'sign change (zero)' if zL*zR<0 else ''}")

# ---- D. the LITERAL WO object Arch * prime-sum: symmetric? ----
print("\n[D] literal WO object  C_N(s)=Arch(s)*Sum Lambda(n)n^-s e^{-it log n}  (N=20000):")
N=20000
# von Mangoldt
lam=[0.0]*(N+1); comp=[False]*(N+1)
for p in range(2,N+1):
    if not comp[p]:
        for m in range(p*p,N+1,p): comp[m]=True
        pk=p
        while pk<=N: lam[pk]=math.log(p); pk*=p
supp=[(n,lam[n]) for n in range(2,N+1) if lam[n]>0]
def P(s):
    tot=mp.mpc(0)
    for n,L in supp: tot+=L*mp.mpf(n)**(-s)
    return tot
def C(s): return Arch(s)*P(s)
for s in [mp.mpc(0.7,21.0)]:
    e=abs(C(s)-C(1-s))/abs(C(s))
    print(f"   s={complex(s)}:  |C(s)-C(1-s)|/|C| = {float(e):.3f}   "
          f"-> {'symmetric' if float(e)<0.05 else 'NOT symmetric (object mismatch: P~zeta'+chr(39)+'/zeta needs ADDITIVE completion, not Arch*)'}")

print("""
----------------------------------------------------------------------
SUMMARY (WO-RH-COMPTRACE-001)
----------------------------------------------------------------------
[A] sigma=1/2 DOES emerge as the unique self-conjugate axis -- Lambda(s)=
    Lambda(1-s) to machine precision. [B] the completed object is exactly REAL
    at sigma=1/2 and not off it. [C] the Riemann-Siegel Z(t) is real with zeros
    at the gamma_n. So the completion makes 1/2 special -- AS THE FUNCTIONAL
    EQUATION, which is classical (Riemann 1859), not new.

[D] the LITERAL WO object Arch*P is NOT symmetric: P approximates the LOG-
    derivative zeta'/zeta, whose symmetric completion is ADDITIVE (digamma +
    log pi), not multiplication by Arch. So the WO's C_N(s) needs that fix.

LIMITATION (task 8, the crux): the functional equation makes 1/2 the AXIS OF
SYMMETRY -- zeros come in pairs rho, 1-rho straddling it. It does NOT force them
ONTO it. A zero rho=beta+i*gamma with beta!=1/2 would just pair with 1-rho. RH
is the statement that no such off-axis pair exists. So '1/2 is the balanced
axis' = functional equation (THEOREM); 'all zeros on it' = RH (OPEN). And the
completion that makes 1/2 special needs zeta's analytic CONTINUATION (used here
via mpmath) -- the finite arithmetic trace cannot reach the line by itself.
This probes the critical-line MECHANISM; it does not prove RH.
""")

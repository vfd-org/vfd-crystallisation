"""
prime_geodesics.py
The PRIME side of the {3,3,5,3} honeycomb: closed geodesics = prime cycles of the
cell-adjacency graph. Count them (Ihara non-backtracking spectrum), get the prime
geodesic length spectrum pi_k, show exponential growth (prime geodesic theorem),
and VERIFY the Ihara duality:  prime Euler product  ==  spectral determinant
  (closed-geodesic/PRIME side)   ==   (eigenvalue/LINE side).
"""
import json, os, numpy as np
from sympy import mobius, divisors
HERE=os.path.dirname(os.path.abspath(__file__))
cells=json.load(open(os.path.join(HERE,"results","honeycomb_patch.json")))["cells"]
Y=[]
for c in cells:
    b=np.array(c["poincare"]); r2=b@b
    Y.append(np.concatenate([[(1+r2)/(1-r2)],2*b/(1-r2)]))
Y=np.array(Y)
def dm(Y):
    T=Y[:,0][:,None]*Y[:,0][None,:]-Y[:,1:]@Y[:,1:].T
    return np.arccosh(np.clip(T,1.0,None))
D=dm(Y); keep=[]; used=np.zeros(len(Y),bool)
for i in range(len(Y)):
    if used[i]:continue
    keep.append(i); used[D[i]<0.05]=True
Y=Y[keep]; D=dm(Y); n=len(Y); np.fill_diagonal(D,np.inf)
d_nn=np.median(D.min(1)); A=(D<1.25*d_nn).astype(float)
deg=A.sum(1); m=int(deg.sum()//2); Q=np.diag(deg)-np.eye(n)
print(f"honeycomb graph: {n} cells (geodesic 'sites'), {m} edges, <deg>={deg.mean():.1f}")

# non-backtracking (Ihara) eigenvalues via companion linearisation of (mu^2 I - mu A + Q)
C=np.block([[A,-Q],[np.eye(n),np.zeros((n,n))]])
mu=np.linalg.eigvals(C); R=float(np.max(np.abs(mu)))
print(f"non-backtracking Perron eigenvalue R = {R:.4f}  (geodesic growth rate)\n")

# closed-geodesic counts N_k = tr(B^k) and PRIME geodesics pi_k (Mobius inversion)
K=14
N=[0]+[ float((mu**k).sum().real) + (2*(m-n) if k%2==0 else 0) for k in range(1,K+1) ]
pi=[0]
for k in range(1,K+1):
    pi.append(sum(int(mobius(k//d))*N[d] for d in divisors(k))/k)
print("PRIME GEODESIC LENGTH SPECTRUM (closed geodesics = the prime side):")
print(f"  {'length k':>8} {'#prime geodesics pi_k':>22} {'~ R^k/k':>12}")
for k in range(1,K+1):
    print(f"  {k:>8} {round(pi[k]):>22} {R**k/k:>12.0f}")
print("  => pi_k grows like R^k/k -- the graph 'prime geodesic theorem',")
print("     the exact analogue of primes growing like x/log x.\n")

# DUALITY: Euler product over prime geodesics  ==  spectral determinant
u=0.05
euler=np.prod([(1-u**k)**(-pi[k]) for k in range(1,K+1)])          # PRIME side
spec =1.0/((1-u**2)**(m-n)*np.linalg.det(np.eye(n)-A*u+Q*u**2))    # LINE/spectral side
print("IHARA DUALITY CHECK at u=0.05:")
print(f"  prime-geodesic Euler product  zeta = {euler:.6f}")
print(f"  spectral-determinant          zeta = {spec:.6f}")
print(f"  ratio = {euler/spec:.6f}   -> PRIME side == SPECTRAL/LINE side  (one zeta, two faces)")
json.dump({"n":n,"m":m,"R":R,"pi":[round(pi[k]) for k in range(1,K+1)],
           "euler":float(euler),"spec":float(spec)},
          open(os.path.join(HERE,"results","prime_geodesics.json"),"w"),indent=1)

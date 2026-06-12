"""
render_tessellation.py  (WO-RH-D2 visual): the FAITHFUL picture of X = SL(2,Z)\H^2.
Tessellates H^2 by SL(2,Z)-images of the fundamental domain F, in both the
upper-half-plane and the Poincare-disk model, marking the cusp and the two cone
points (i order 2, rho order 3). Pure geometry, no stylization.
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
HERE=os.path.dirname(os.path.abspath(__file__))
FIG=os.path.join(HERE,"..","figures")

# --- enumerate SL(2,Z) (mod +/-I) by BFS on S, T, T^{-1} ---
def matmul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def canon(M):                       # canonical sign rep in PSL(2,Z)
    a,b,c,d=M[0][0],M[0][1],M[1][0],M[1][1]
    key=(a,b,c,d)
    if (a,b,c,d) < (-a,-b,-c,-d): key=(-a,-b,-c,-d)
    return key
S=((0,-1),(1,0)); T=((1,1),(0,1)); Ti=((1,-1),(0,1)); I=((1,0),(0,1))
seen={canon(I)}; frontier=[I]; elems=[I]
gens=[S,T,Ti]
while frontier and len(elems)<400:
    nf=[]
    for M in frontier:
        for g in gens:
            N=matmul(M,g); k=canon(N)
            if k not in seen:
                seen.add(k); nf.append(N); elems.append(N)
    frontier=nf
print(f"enumerated {len(elems)} SL(2,Z) elements (mod +/-I)")

# --- boundary of F: two verticals Re=+/-1/2 and the arc |z|=1 (theta 60..120) ---
def F_boundary(N=200, Ytop=4.0):
    s3=np.sqrt(3)/2
    yL=np.linspace(s3,Ytop,N); left =-0.5+1j*yL
    th=np.linspace(np.pi/3,2*np.pi/3,N); arc=np.exp(1j*th)
    yR=np.linspace(Ytop,s3,N); right= 0.5+1j*yR
    return np.concatenate([left[::-1],arc,right])    # one open path along the boundary
B=F_boundary()
def mob(M,z):
    a,b,c,d=M[0][0],M[0][1],M[1][0],M[1][1]
    return (a*z+b)/(c*z+d)

# ================= panel 1: upper half-plane =================
fig,ax=plt.subplots(figsize=(11,6))
for M in elems:
    w=mob(M,B)
    ax.plot(w.real,w.imag,color="#2a4d7a",lw=0.5,alpha=0.7)
# cone points + cusp
ax.plot([0],[1],'o',color="crimson",ms=8,zorder=5,label="cone point i  (order 2)")
ax.plot([-0.5,0.5],[np.sqrt(3)/2]*2,'s',color="darkorange",ms=7,zorder=5,
        label=r"cone point $\rho=e^{2\pi i/3}$  (order 3)")
ax.annotate("cusp  (z → i∞)",xy=(0,3.6),ha="center",color="green",fontsize=11)
ax.plot([0],[3.9],'^',color="green",ms=9,zorder=5)
ax.set_xlim(-2.2,2.2); ax.set_ylim(0,4); ax.set_aspect("equal")
ax.set_title(r"$X=\mathrm{SL}(2,\mathbb{Z})\backslash\mathbb{H}^2$  —  tessellation of the upper half-plane by images of $F$")
ax.set_xlabel("Re z  (phase / position)"); ax.set_ylabel("Im z  (scale / depth)")
ax.legend(loc="upper right",fontsize=9)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"modular_tessellation_halfplane.png"),dpi=140)
print("saved modular_tessellation_halfplane.png")

# ================= panel 2: Poincare disk =================
# Cayley w=(z-i)/(z+i): H^2 -> unit disk; cusp z=i*inf -> w=1.
def cayley(z): return (z-1j)/(z+1j)
fig,ax=plt.subplots(figsize=(7,7))
circ=np.exp(1j*np.linspace(0,2*np.pi,400))
ax.plot(circ.real,circ.imag,color="black",lw=1.2)
for M in elems:
    w=cayley(mob(M,F_boundary(N=200,Ytop=60.0)))
    ax.plot(w.real,w.imag,color="#6a2a7a",lw=0.5,alpha=0.75)
ci=cayley(1j); cr=cayley(np.exp(1j*np.pi/3)); cr2=cayley(np.exp(2j*np.pi/3)); cusp=cayley(1e6j)
ax.plot([ci.real],[ci.imag],'o',color="crimson",ms=8,zorder=5,label="i (order 2)")
ax.plot([cr.real,cr2.real],[cr.imag,cr2.imag],'s',color="darkorange",ms=7,zorder=5,label=r"$\rho$ (order 3)")
ax.plot([cusp.real],[cusp.imag],'^',color="green",ms=10,zorder=5,label="cusp")
ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05); ax.set_aspect("equal"); ax.axis("off")
ax.set_title(r"Poincaré-disk view: SL(2,$\mathbb{Z}$) tessellation; cusp on the boundary")
ax.legend(loc="lower right",fontsize=9)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"modular_tessellation_disk.png"),dpi=140)
print("saved modular_tessellation_disk.png")

"""
render_geometry_and_spectrum.py  (WO-RH-D2 visual, honest two-plane version).
LEFT  = z-plane: the modular tessellation (the GEOMETRY / surface points).
RIGHT = s-plane: the SPECTRAL PARAMETER, where the scattering resonances live.
These are DIFFERENT complex planes (z = a point of H^2; s = the Eisenstein
parameter). The resonances = Riemann zeros sit at s = 1/4 + i*gamma/2 -- they are
NOT points of the surface, so they belong on the right panel, not overlaid on z.
"""
import numpy as np, matplotlib, os
matplotlib.use("Agg"); import matplotlib.pyplot as plt
import mpmath as mp
HERE=os.path.dirname(os.path.abspath(__file__)); FIG=os.path.join(HERE,"..","figures")

# ---- SL(2,Z) elements (BFS, mod +/-I) ----
def matmul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def canon(M):
    a,b,c,d=M[0][0],M[0][1],M[1][0],M[1][1]
    return (a,b,c,d) if (a,b,c,d)<(-a,-b,-c,-d) else (-a,-b,-c,-d)
S=((0,-1),(1,0)); T=((1,1),(0,1)); Ti=((1,-1),(0,1)); I=((1,0),(0,1))
seen={canon(I)}; fr=[I]; elems=[I]
while fr and len(elems)<460:
    nf=[]
    for M in fr:
        for g in (S,T,Ti):
            N=matmul(M,g); k=canon(N)
            if k not in seen: seen.add(k); nf.append(N); elems.append(N)
    fr=nf
def Fbd(N=200,Ytop=4.0):
    s3=np.sqrt(3)/2
    L=-0.5+1j*np.linspace(s3,Ytop,N); A=np.exp(1j*np.linspace(np.pi/3,2*np.pi/3,N))
    R=0.5+1j*np.linspace(Ytop,s3,N); return np.concatenate([L[::-1],A,R])
def mob(M,z):
    a,b,c,d=M[0][0],M[0][1],M[1][0],M[1][1]; return (a*z+b)/(c*z+d)

fig,(axz,axs)=plt.subplots(1,2,figsize=(15,7))

# ============ LEFT: z-plane (the geometry) ============
B=Fbd()
for M in elems:
    w=mob(M,B); axz.plot(w.real,w.imag,color="#2a4d7a",lw=0.5,alpha=0.7)
axz.plot([0],[1],'o',color="crimson",ms=8,zorder=5)
axz.plot([-0.5,0.5],[np.sqrt(3)/2]*2,'s',color="darkorange",ms=7,zorder=5)
axz.plot([0],[3.85],'^',color="green",ms=10,zorder=5)
axz.annotate("cusp z→i∞",xy=(0,3.55),ha="center",color="green",fontsize=10)
axz.annotate("i (order 2)",xy=(0.06,1.0),color="crimson",fontsize=9)
axz.annotate(r"$\rho$ (order 3)",xy=(0.55,0.83),color="darkorange",fontsize=9)
axz.set_xlim(-2.2,2.2); axz.set_ylim(0,4); axz.set_aspect("equal")
axz.set_title("z-plane: the GEOMETRY\n$X=\\mathrm{SL}(2,\\mathbb{Z})\\backslash\\mathbb{H}^2$  (waves enter / scatter at the cusp)")
axz.set_xlabel("Re z"); axz.set_ylabel("Im z")

# ============ RIGHT: s-plane (spectral parameter) ============
zeros=[float(mp.im(mp.zetazero(n))) for n in range(1,9)]
# critical line Re(s)=1/2 (modular line, Eisenstein continuous spectrum)
axs.axvline(0.5,color="navy",lw=2,label="Re(s)=½  modular line\n(Eisenstein continuous spectrum)")
# resonances Re(s)=1/4 (= Riemann zeros rho/2)
axs.axvline(0.25,color="crimson",lw=1,ls="--",alpha=0.7)
res_im=[g/2 for g in zeros]
axs.plot([0.25]*len(res_im),res_im,'o',color="crimson",ms=9,zorder=5,
         label="scattering RESONANCES\n s=¼+iγ/2  (=Riemann zeros ρ/2)")
for g,y in zip(zeros,res_im):
    axs.annotate(f"γ={g:.2f}",xy=(0.27,y),fontsize=8,color="crimson",va="center")
# zeros of phi at Re(s)=3/4 (the conjugate set)
axs.axvline(0.75,color="gray",lw=1,ls=":",alpha=0.6)
axs.plot([0.75]*len(res_im),res_im,'x',color="gray",ms=6,alpha=0.7,label="zeros of φ  (Re=¾)")
# pole at s=1 (constant eigenfunction)
axs.plot([1.0],[0.0],'^',color="green",ms=11,zorder=5,label="pole s=1 (constant eigenfn)")
axs.set_xlim(0,1.2); axs.set_ylim(-1,22); axs.set_aspect("auto")
axs.set_title("s-plane: the SPECTRAL PARAMETER\nφ(s)=ξ(2s−1)/ξ(2s);  zeros of ζ = resonances at Re(s)=¼")
axs.set_xlabel("Re s"); axs.set_ylabel("Im s")
axs.legend(loc="upper right",fontsize=8,framealpha=0.95)
axs.grid(alpha=0.2)

fig.suptitle("The d=2 modular surface: geometry (z) and its scattering spectrum (s) are DIFFERENT planes",
             fontsize=12)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"geometry_and_resonances.png"),dpi=140)
print("saved geometry_and_resonances.png")
print(f"resonances (Im s = gamma/2): {[round(y,2) for y in res_im]}")

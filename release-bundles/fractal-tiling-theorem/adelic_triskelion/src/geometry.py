"""Adelic Triskelion geometry (WO-VFD-ADELIC-TRISKELION-GEOMETRY-001).
A DIAGRAM (not a proof) of the completed-zeta local-global architecture:
 Arm A finite p-adic places (primes/Euler), Arm B archimedean Gamma completion
 (Gaussian e^{-pi u^2}, the verified completion kernel), Arm C scale action /
 involution (u=log t, u<->-u <=> t<->1/t <=> s<->1-s), around the fixed witness
 axis Re(s)=1/2 (u=0, t=1). Three arms at phases 0, 2pi/3, 4pi/3."""
import numpy as np
PHASES = {"A_finite": 0.0, "B_archimedean": 2*np.pi/3, "C_scale": 4*np.pi/3}
R0, A_R, B_Z, OMEGA = 1.0, 0.55, 0.45, 1.7
def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    i=3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True
def primes_up_to(P): return [n for n in range(2,P+1) if is_prime(n)]
def prime_arm(P=200):
    ps=primes_up_to(P); phi=PHASES["A_finite"]; out=[]
    for p in ps:
        u=np.log(np.log(p)) if p>2 else 0.0          # log log p (>=2)
        r=R0+A_R*np.log(p); th=OMEGA*np.log(p)+phi; z=B_Z*np.log(np.log(p)) if p>2 else 0.0
        out.append(dict(p=p, u=float(u), x=float(r*np.cos(th)), y=float(r*np.sin(th)),
                        z=float(z), size=float(np.log(p))))   # node size = Lambda(p)=log p
    return out
def archimedean_arm(U=2.5, n=400):
    u=np.linspace(-U,U,n); phi=PHASES["B_archimedean"]
    r=R0+A_R*np.abs(u); th=OMEGA*u+phi; z=B_Z*u
    profile=np.exp(-np.pi*u**2)                         # Gaussian = the Gamma-completion heat kernel
    return dict(u=u, x=r*np.cos(th), y=r*np.sin(th), z=z, profile=profile, phase=phi)
def scale_arm(U=2.5, n=400):
    u=np.linspace(-U,U,n); phi=PHASES["C_scale"]
    r=R0+A_R*np.abs(u)            # r even in u  -> r(u)=r(-u)
    th=OMEGA*u+phi               # th odd-ish about phi
    z=B_Z*u                      # z odd in u   -> z(u)=-z(-u): the involution realised as z->-z
    return dict(u=u, x=r*np.cos(th), y=r*np.sin(th), z=z, phase=phi)
def witness_axis(U=2.5): return dict(x=[0,0], y=[0,0], z=[-B_Z*U, B_Z*U], label="Re(s)=1/2  (u=0, t=1)")

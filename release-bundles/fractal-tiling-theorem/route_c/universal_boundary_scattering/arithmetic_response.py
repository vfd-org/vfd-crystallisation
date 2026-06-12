"""Arithmetic instance: the zeta scattering system.
determinant = xi(s); response = -zeta'/zeta(1/2+i xi) (poles at zeros);
boundary/greybody = archimedean factor pi^{-s/2}Gamma(s/2), boundary response = (1/2)psi(s/2).
Resonances = zeros (VALIDATION ONLY via mpmath.zetazero; never used to construct response).
"""
import mpmath as mp
mp.mp.dps=25
def response(xi):              # -zeta'/zeta(1/2+i xi): log-derivative, poles at zeros
    s=mp.mpc(0.5,xi); return -mp.zeta(s,derivative=1)/mp.zeta(s)
def archimedean_boundary_response(xi):   # (1/2) psi(1/4 + i xi/2)  -- the route_b capacity multiplier
    return 0.5*mp.digamma(mp.mpc(0.25,xi/2))
def zeros(n=6):                # VALIDATION ONLY
    return [float(mp.im(mp.zetazero(k))) for k in range(1,n+1)]
def resonance_amplification(near, width=0.4, npts=9):
    # |response| at +- width around a target xi vs at the midpoint baseline far away
    import numpy as np
    grid=[near+width*(k/(npts-1)-0.5) for k in range(npts)]
    return max(abs(complex(response(x))) for x in grid)

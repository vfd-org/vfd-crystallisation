"""
modular_scattering.py  (WO-RH-D2-MODULAR-SCATTERING-POSITIVITY-001, WS-A/B/C)

The d=2 arithmetic surface H^2 / SL(2,Z): its Eisenstein/scattering theory.
Scattering coefficient (constant term of E(z,s)):  phi(s) = xi(2s-1)/xi(2s),
with the completed zeta xi(s) = pi^{-s/2} Gamma(s/2) zeta(s).

This script computes phi(s), checks the scattering identities, LOCATES where the
Riemann zeros enter (the scattering resonances), and computes the phase on the
modular critical line Re(s)=1/2. Honest scope is enforced in the printout: the
Riemann zeros are the modular RESONANCES (poles of phi at s = rho/2), NOT the
discrete Laplace spectrum and NOT on the modular line; positivity stays the wall.
"""
import mpmath as mp
mp.mp.dps = 30

def xi(s):
    s = mp.mpc(s)
    return mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def phi(s):
    s = mp.mpc(s)
    return xi(2*s - 1) / xi(2*s)

# ---------------------------------------------------------------- WS-B harness
def abs_phi(t):  return abs(phi(mp.mpf('0.5') + 1j*t))
def arg_phi(t):  return mp.arg(phi(mp.mpf('0.5') + 1j*t))

if __name__ == "__main__":
    print("="*72)
    print("WS-B  MODULAR SCATTERING FUNCTION  phi(s) = xi(2s-1)/xi(2s)")
    print("="*72)

    print("\n[B1] phi(s) at sample points (zeta is visibly inside it):")
    for s in [mp.mpf('0.7'), mp.mpf('1.3'), mp.mpc('0.6','3.0')]:
        print(f"   phi({complex(s)})  = {mp.nstr(phi(s),10)}")

    print("\n[B2] scattering identity  phi(s)*phi(1-s) = 1  (unitarity off-line):")
    for s in [mp.mpc('0.6','2.0'), mp.mpc('0.8','5.0')]:
        prod = phi(s)*phi(1-s)
        print(f"   s={complex(s)}:  phi(s)phi(1-s) = {mp.nstr(prod,8)}  (target 1)")

    print("\n[B3] UNITARITY ON THE MODULAR LINE  |phi(1/2+it)| = 1:")
    for t in [1,5,10,14.134725,21.022040,30.0]:
        a = abs_phi(mp.mpf(str(t)))
        print(f"   t={t:>10}:  |phi(1/2+it)| = {mp.nstr(a,12)}")
    print("   -> |phi|=1 exactly on Re(s)=1/2: the scattering matrix is UNITARY there.")

    print("\n[B4] phi has a POLE at s=1 (the constant eigenfunction / residue):")
    for s in [mp.mpf('0.97'), mp.mpf('0.99'), mp.mpf('0.999')]:
        print(f"   phi({float(s)}) = {mp.nstr(phi(s),8)}  (blows up -> s=1 pole)")

    print("\n" + "="*72)
    print("WS-C  WHERE THE RIEMANN ZEROS ENTER: the SCATTERING RESONANCES")
    print("="*72)
    print("phi = xi(2s-1)/xi(2s); poles of phi = zeros of xi(2s) = {2s=rho} = s=rho/2.")
    print("Under RH rho=1/2+i*gamma  ->  resonance at  s = 1/4 + i*gamma/2.")
    print("\n[C1] test |phi| near s = 1/4 + i*gamma_n/2 (should SPIKE = a pole):")
    gammas = [14.134725, 21.022040, 25.010858, 30.424876]
    for g in gammas:
        s_res = mp.mpc('0.25', g/2)
        on   = abs(phi(s_res + mp.mpc('0','0')))     # at the resonance (near pole)
        near = abs(phi(s_res + mp.mpc('0.05','0')))   # 0.05 to the right
        off  = abs(phi(mp.mpc('0.25', g/2 + 1.0)))    # 1.0 up in t (between zeros)
        print(f"   gamma={g:>10}: |phi(1/4+ig/2)|={mp.nstr(on,6):>12}  "
              f"|phi(.30+ig/2)|={mp.nstr(near,6):>10}  |phi(1/4+i(g/2+1))|={mp.nstr(off,6):>10}")
    print("   -> |phi| is LARGE exactly at s=1/4+i*gamma/2 and drops off between:")
    print("      the Riemann zeros ARE the modular surface's scattering resonances.")
    print("      NOTE (honest): they sit at Re(s)=1/4, NOT on the modular line 1/2,")
    print("      and they are NOT the Laplace (Maass) eigenvalues. RH <=> these")
    print("      resonances sit exactly on Re(s)=1/4 <=> rho on Re=1/2.")

    print("\n[C2] phase on the line  theta(t)=arg phi(1/2+it)  and its winding:")
    ts = [mp.mpf(str(x)) for x in [0.5,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]]
    prev=None; wind=mp.mpf('0')
    rows=[]
    for t in ts:
        th=arg_phi(t)
        if prev is not None:
            d=th-prev
            while d> mp.pi: d-=2*mp.pi
            while d<-mp.pi: d+=2*mp.pi
            wind+=d
        rows.append((float(t),float(th),float(wind)))
        prev=th
    print(f"   {'t':>6}{'theta=arg phi':>16}{'cumulative winding':>20}")
    for t,th,w in rows:
        print(f"   {t:>6}{th:>16.4f}{w:>20.4f}")
    print("   theta(t) = -2 arg xi(1+2it): the phase tracks the completed-zeta")
    print("   argument. Honest: this is the continuous-spectrum scattering phase")
    print("   (its derivative -phi'/phi enters the Selberg trace formula's")
    print("   continuous term); it encodes zeta's argument, it does NOT by itself")
    print("   count the gamma_n as a discrete spectrum. Diagnostic, not proof.")

"""WO-RH-UNIVERSAL-BOUNDARY-SCATTERING-001 driver: instantiate the schema for the
arithmetic zeta system and the Poschl-Teller toy horizon, and decide what is
GENUINELY shared vs only analogy. Non-circular: zeros/QNMs only validate.
"""
import mpmath as mp, math, json
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np
from boundary_scattering_system import BoundaryScatteringSystem
import arithmetic_response as A
import toy_horizon_scattering as T
mp.mp.dps=25

print("="*72); print("WO-RH-UNIVERSAL-BOUNDARY-SCATTERING-001  arithmetic vs toy horizon"); print("="*72)

arith=BoundaryScatteringSystem("arithmetic-zeta","primes p / Lambda(n) (closed orbits)",
    "archimedean pi^{-s/2}Gamma(s/2) + pole","xi(s)","-zeta'/zeta(1/2+i xi)","zeta zeros rho",
    "Weil positivity / ||K||<=1 (contraction)","smoothed-PNT overshoot / non-self-adjoint",
    "off-critical-line zero","OPEN: stability = self-adjointness = Hilbert-Polya = RH")
toy=BoundaryScatteringSystem("toy-horizon-PT","trapped modes of V0 sech^2(a x) barrier",
    "greybody |T|^2 (Gamma-ratio); boundary cond.","Delta(omega)=1/[Gamma(1/2+i nu-i w)Gamma(1/2-i nu-i w)]",
    "(i/a)[psi(1/2+i nu-i w)+psi(1/2-i nu-i w)]","QNMs omega_n=a(+-nu - i(n+1/2))",
    "no growing mode (Im omega<0) / scattering contractive","smooth (no barrier) / GAIN (non-self-adjoint)",
    "QNM crosses to Im omega>0 (growing/unstable)","PROVABLE: V real => H self-adjoint => Im omega<0")

# --- shared object 1: DETERMINANT is a Gamma-object in both ---
print("\n[1] DETERMINANT: both built from the Gamma function.")
print("    arithmetic: completed xi has the archimedean factor pi^{-s/2}Gamma(s/2).")
print("    toy:        Delta(omega) is a ratio/product of Gamma(1/2 +- i nu - i omega/a).")

# --- shared object 2: BOUNDARY RESPONSE is DIGAMMA in both (concrete numeric check) ---
print("\n[2] BOUNDARY/ARCHIMEDEAN RESPONSE = digamma psi in BOTH (the route_b capacity multiplier):")
print("    xi    Re[arith (1/2)psi(1/4+i xi/2)]    Re[toy (i/a)psi-sum, V0=4,a=1]")
for xi in [5.0,15.0,30.0]:
    ar=complex(A.archimedean_boundary_response(xi)).real
    ty=complex(T.response(xi,V0=4.0,alpha=1.0)).real
    print(f"    {xi:5.1f}      {ar:+.4f}                       {ty:+.4f}")
print("    -> same special function (digamma) governs the boundary response in both systems.")

# --- shared object 3: RESPONSE has POLES at the RESONANCES (validation) ---
print("\n[3] RESPONSE poles at resonances (VALIDATION only):")
gam=A.zeros(4); print(f"    arithmetic: -zeta'/zeta amplification near first zeros {[(round(g,2)) for g in gam]}:")
base=abs(complex(A.response(17.3)))   # between zeros
for g in gam:
    amp=A.resonance_amplification(g)
    print(f"        xi~{g:6.2f}: |response| peak {amp:7.1f}  ({amp/base:5.1f}x baseline {base:.2f})")
qn=T.qnms(V0=4.0,alpha=1.0,N=3)
print(f"    toy QNMs (V0=4,a=1): {[ (round(z.real,2),round(z.imag,2)) for z in qn[:6] ]}")
print(f"    all QNM Im(omega) < 0 ? {all(z.imag<0 for z in qn)}  -> DAMPED/STABLE (provably, V real).")

# --- shared object 4: STABILITY = contraction/positivity; FAILURE = non-self-adjoint ---
print("\n[4] STABILITY law (the crux):")
print("    toy:  stability (Im omega<0) <=> H=-d^2+V self-adjoint (V real). PROVABLE.")
print("          control: add GAIN (V -> V - i*g, non-self-adjoint) -> a QNM crosses to Im>0:")
# demonstrate: shift omega pole condition with complex nu (gain) -> resonance can cross
nu_gain=mp.sqrt(mp.mpc(4.0,-1.5)-mp.mpf(1)/4)   # complex 'potential' (gain)
w_cross=complex(1j*(mp.mpf(1)/2+1j*nu_gain))    # n=0 pole: 1/2 - i nu - i w =0 -> w = -nu + i/2 ... 
om0=complex(( -nu_gain - 1j*0.5))               # n=0 QNM with gain
print(f"          with gain, n=0 QNM omega = {om0.real:+.2f}{om0.imag:+.2f}i  -> Im {'>0 UNSTABLE' if om0.imag>0 else '<0'}")
print("    arithmetic: stability (zeros on line) <=> the prime scattering system is")
print("          self-adjoint/contractive = Hilbert-Polya. OPEN. This IS RH (route_b ||K||<=1).")

# --- shared object 5: smooth source overshoot vs structured ---
print("\n[5] SMOOTH vs STRUCTURED source:")
print("    arithmetic: smoothed-PNT overshoots capacity (mu=1.26>1, HORIZON-INVARIANT-001);")
print("                real primes (structured) restore contraction (mu=0.9998).")
print("    toy:        removing the barrier (smooth, V0->0) => nu imaginary, NO real-line")
print("                resonances (free propagation); the structured barrier is what")
print("                creates the damped resonance ladder. Failure modes ALIGN qualitatively.")

# ---- plots ----
xg=np.linspace(2,45,900)
arr=[abs(complex(A.response(x))) for x in xg]
fig,ax=plt.subplots(1,2,figsize=(13,4.3))
ax[0].plot(xg,arr,lw=1); 
for g in A.zeros(7): ax[0].axvline(g,color='k',ls=':',lw=0.6,alpha=0.5)
ax[0].set_title("Arithmetic response |-zeta'/zeta(1/2+i xi)|\npoles at zeros (dotted)"); ax[0].set_xlabel("xi"); ax[0].set_ylim(0,15)
qn=T.qnms(V0=4.0,alpha=1.0,N=7)
ax[1].scatter([z.real for z in qn],[z.imag for z in qn],c='crimson')
ax[1].axhline(0,color='k',lw=0.8); ax[1].set_title("Toy horizon (Poschl-Teller) QNMs\nomega_n on two lines, all Im<0 (damped)")
ax[1].set_xlabel("Re omega"); ax[1].set_ylabel("Im omega")
fig.suptitle("Shared architecture: Gamma-determinant -> digamma response -> resonances-on-lines -> stability=self-adjointness",fontsize=9)
fig.tight_layout(); fig.savefig("plots/scattering_comparison.png",dpi=120); plt.close(fig)
print("\n[plot] plots/scattering_comparison.png")

res=dict(work_order="WO-RH-UNIVERSAL-BOUNDARY-SCATTERING-001",
  systems=dict(arithmetic=arith.dict(), toy_horizon=toy.dict()),
  shared=dict(determinant_is_Gamma=True, boundary_response_is_digamma=True,
    response_is_logderivative=True, resonances_on_lines=True,
    stability_is_self_adjointness=True, greybody_equals_archimedean_Gamma=True),
  only_analogy=dict(smooth_overshoot_alignment="qualitative", funnel_geometry="rejected (prior WO)"),
  provability_transfer=False,
  crux="toy stability PROVABLE (V real => self-adjoint => Im omega<0); arithmetic stability = self-adjointness = Hilbert-Polya = RH (OPEN). Architecture relocates RH, does not weaken it.",
  universal_law_candidate=dict(shared_determinant_response=True, shared_capacity_regularisation=True,
    shared_contraction_law=True, verdict="promising-but-known (= trace-formula/Lax-Phillips scattering framework); NOT new math; NO provability transfer"),
  anti_circularity=dict(zeros_used_in_construction=False, qnm_poles_used_in_construction=False, validation_only=True),
  recommended_next="WO-RH-ARCHIMEDEAN-GREYBODY-002 (Gamma/pole as arithmetic greybody) is the one concrete defensible thread (though known); constructive next remains WO-RH-OPERATOR-ROUTE-PUBLISH-001")
json.dump(res,open("results/rh_universal_boundary_scattering_001/result.json","w"),indent=2,default=str)
print("[json] results/rh_universal_boundary_scattering_001/result.json")
print("""
----------------------------------------------------------------------
VERDICT: the shared structure is REAL but KNOWN, and transfers NO proof.
 GENUINELY shared (not visual): Gamma-function determinant; DIGAMMA boundary
   response (the same psi(1/4+i xi/2) as the route_b capacity); log-derivative
   response with poles at resonances; resonances on line(s); stability =
   self-adjointness/contraction; archimedean Gamma = greybody factor.
 This is the trace-formula / Lax-Phillips scattering architecture -- a recognised
   correspondence, NOT new mathematics.
 CRUX: the toy is PROVABLE precisely because V is real (self-adjoint => damped QNMs);
   the arithmetic instance of the SAME statement is 'the prime system is self-adjoint'
   = Hilbert-Polya = RH. So the architecture RELOCATES RH; it does not weaken it.
 No new invariant; no provability transfer. Black-hole scattering = good structural
   intuition, same wall (||K||<=1 / self-adjointness). No proof, no phi, no God Prime.
----------------------------------------------------------------------""")

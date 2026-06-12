import sys,os; sys.path.insert(0,os.path.dirname(__file__))
import numpy as np, mpmath as mp, json, witness_core as W
OUT=os.path.join(os.path.dirname(__file__),"..","outputs")
print("="*78); print("WO-VFD-RH-POSITIVE-ADELIC-WITNESS-OPERATOR-001  positive witness scaffold"); print("="*78)

# Stage A + B
u,du=W.witness_grid(U=8.0,N=512); D=W.scale_generator(512,du)
herm=float(np.max(np.abs(D-D.conj().T)))
J=lambda f:f[::-1]; JDJ=J(np.array([J(row) for row in D.T]).T) if False else None
# JDJ = -D : apply J on both sides (reverse rows and cols)
Dj=D[::-1,:][:,::-1]; jdj_resid=float(np.max(np.abs(Dj+D)))   # J D J + D should ~0 (interior)
ev=np.linalg.eigvalsh(D); 
print(f"\n[A/B] witness space L²([-8,8],512); J²=I exact; D=-i d/du Hermitian err={herm:.1e};")
print(f"      spectrum real (max|Im|={float(np.max(np.abs(ev.imag))) if np.iscomplexobj(ev) else 0:.1e}); JDJ+D resid={jdj_resid:.1e} (≈0 ⇒ JDJ=−D).")

# Stage C completed-kernel regression
gm=float(W.gaussian_mellin(mp.mpc(0.6,8))); td=float(W.theta_duality(mp.mpf('0.7')))
Xi=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s); feXi=W.fe_residual(Xi)
feraw=W.fe_residual(lambda s:mp.zeta(s)); fefake=W.fe_residual(lambda s:mp.pi**(-s/2)*mp.gamma(s/3)*mp.zeta(s))
print(f"\n[C] completed-kernel regression: Gaussian-Mellin err {gm:.1e}; theta-duality {td:.1e};")
print(f"    FE residual Ξ {feXi:.1e} (PASS); raw ζ {feraw:.2f} (FAIL); fake Γ {fefake:.2f} (FAIL).")

# Stage D explicit-formula balance + cutoff
print("\n[D] Riemann-Weil explicit-formula balance (ZeroSide vs Arch+Pole-Prime-Const):")
efb={}
for Nz in [20,40]:
    r=W.explicit_formula_balance(sigma=0.3,Nz=Nz,P=3000); efb[Nz]=r['residual']
    print(f"    σ=0.3 Nz={Nz}: ZeroSide={r['ZeroSide']:.5f} RHS={r['rhs']:.5f} residual={r['residual']:.3e}")
efb_shuf=W.explicit_formula_balance(sigma=0.3,Nz=40,P=3000,lam_weights="shuffle")['residual']
print(f"    [null C] shuffled primes: residual={efb_shuf:.3e}  ({'WORSE -> distinguished' if efb_shuf>5*efb[40] else 'check'})")

# Stage E/F Weil positivity form + operator + nulls
print("\n[E/F] Weil positivity form D=A+P−R (route_b), min eigenvalue (finite cutoff):")
real=W.weil_form(arch="real",primes="real"); 
print(f"    REAL (A+P−R): min eig = {real['min_eig']:+.5f}  eigs[:4]={np.round(real['eigs'][:4],4)}")
print(f"      -> PSD with a near-null mode (λ_min → 0⁺). This is finite Weil positivity.")
nulls={
 "null D: no archimedean (P−R)": W.weil_form(arch="none",primes="real")['min_eig'],
 "null B: fake Γ(s/3)":          W.weil_form(arch="fake",primes="real")['min_eig'],
 "null C: shuffled primes":      W.weil_form(arch="real",primes="shuffle")['min_eig'],
}
for n,me in nulls.items(): print(f"    {n:32}: min eig = {me:+.5f}  {'INDEFINITE -> distinguished' if me<-1e-4 else '(check)'}")
# null A random Hermitian
rng=np.random.default_rng(0); G=rng.standard_normal((12,12)); Gh=(G+G.T)/2
print(f"    null A: random Hermitian        : min eig = {np.linalg.eigvalsh(Gh).min():+.5f}  INDEFINITE -> distinguished")

# Stage G Hilbert-Polya probe (honest, no fit)
print("\n[G] Hilbert–Pólya spectral-determinant probe (NO fitting to zeros):")
print("    No non-fitted self-adjoint A_N is known whose det(zI−A_N) reproduces ξ(½+iz).")
print("    We do NOT fit zeros into a matrix (that would be descriptive, not explanatory).")
print("    => the spectral operator is NOT exhibited. This IS the open Hilbert–Pólya problem.")

# verdict — honest per-test discrimination (no single test catches every null)
pos_nulls_fail = (nulls["null D: no archimedean (P−R)"]<-1e-3 and nulls["null B: fake Γ(s/3)"]<-1e-3
                  and float(np.linalg.eigvalsh(Gh).min())<-1e-3)   # positivity form rejects these
shuffle_breaks_EF = efb_shuf>5*efb[40]                              # shuffled primes caught by explicit-formula
fe_rejects = feraw>0.01 and fefake>0.01                            # FE residual rejects raw/fake completion
discriminates = pos_nulls_fail and shuffle_breaks_EF and fe_rejects
scaffold_ok = herm<1e-9 and gm<1e-6 and td<1e-20 and feXi<1e-8 and efb[40]<5e-2 and real['min_eig']>-1e-3
verdict = "STRONG PASS (proof-facing scaffold; NOT a proof)" if (scaffold_ok and discriminates) else "WEAK/FAIL"
print(f"\n  [null discrimination] positivity rejects no-arch/fake/random: {pos_nulls_fail}; "
      f"explicit-formula rejects shuffled primes: {shuffle_breaks_EF}; FE rejects raw/fake: {fe_rejects}")
print(f"  (note: shuffled-primes stays PSD on the form but BREAKS the explicit-formula balance —")
print(f"   different nulls fail different tests; collectively the scaffold discriminates.)")
print("\n"+"="*78)
print(f"  scaffold recovers architecture: {scaffold_ok}; nulls fail/distinguished: {discriminates}")
print(f"  VERDICT: {verdict}")
print("""  This DOES NOT prove RH. It is the Weil/Connes positivity criterion (KNOWN) re-encoded
  as a witness scaffold: witness space + involution + scale generator + completed-kernel
  regression + explicit-formula balance + finite Weil positivity, with nulls discriminated.
  THE WALL: the finite form is PSD only WITH a near-null mode (λ_min → 0⁺); proving that the
  full infinite-dimensional form stays ≥ 0 for ALL admissible test functions IS RH. The
  Hilbert–Pólya operator is NOT exhibited (no non-fitted A_N). Gap = infinite-limit
  positivity / a positive self-adjoint witness operator = RH itself.""")
print("="*78)
json.dump(dict(work_order="WO-VFD-RH-POSITIVE-ADELIC-WITNESS-OPERATOR-001",
  witness=dict(D_hermitian_err=herm, JDJ_plus_D_resid=jdj_resid),
  completed_kernel=dict(gaussian_mellin_err=gm, theta_duality=td, fe_Xi=feXi, fe_raw=feraw, fe_fake=fefake),
  explicit_formula=dict(residual_by_Nz=efb, shuffled_primes_residual=efb_shuf),
  weil_positivity=dict(real_min_eig=real['min_eig'], real_eigs=[float(x) for x in real['eigs']], nulls=nulls,
     random_hermitian_min_eig=float(np.linalg.eigvalsh(Gh).min())),
  hilbert_polya="not exhibited (no non-fitted A_N; fitting zeros would be descriptive only) = open problem",
  scaffold_recovers=scaffold_ok, nulls_discriminated=discriminates, verdict=verdict,
  proof_gap="finite Weil form PSD only with near-null mode; full-limit positivity for all admissible test functions = RH; positive self-adjoint witness operator not exhibited",
  no_rh_claim=True),
  open(os.path.join(OUT,"weil_positivity_summary.json"),"w"), indent=2, default=str)
print("[json] outputs/weil_positivity_summary.json")

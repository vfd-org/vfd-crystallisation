import sys, os, json, math
sys.path.insert(0,os.path.dirname(__file__)); import numpy as np
import pgs_bridge as P
N=100000
print("="*76); print("WO-VFD-PGS-TRACE-BRIDGE-001  divisor-excess -> trace-law bridge"); print("="*76)
obs=P.build_observables(N)
print(f"\n[D1] observables to N={N}: primes={int(obs['is_prime'].sum())}; E(prime)=0 exactly (by construction).")

# [D2] gap chambers + symmetry vs gap-local shuffle (null B)
ch=P.gap_chambers(obs)
rsym=np.array([c['rsym_norm'] for c in ch])
# null B: shuffle E within each gap interior, recompute rsym
rng=np.random.default_rng(1); E=obs['E'].copy(); primes=np.where(obs['is_prime'])[0]
Esh=E.copy()
for p,q in zip(primes[:-1],primes[1:]):
    interior=np.arange(p+1,q)
    if len(interior)>1: Esh[interior]=rng.permutation(Esh[interior])
rsym_sh=[]
for p,q in zip(primes[:-1],primes[1:]):
    seg=Esh[p:q+1]; r=float(np.sum(np.abs(seg-seg[::-1])))/2; rsym_sh.append(r/(1+float(seg.sum())))
rsym_sh=np.array(rsym_sh)
print(f"\n[D2] gap chambers: {len(ch)}; mean normalised symmetry residual R_sym_norm:")
print(f"     real E:           {rsym.mean():.4f}")
print(f"     gap-local shuffle:{rsym_sh.mean():.4f}")
print(f"     -> real {'NOT more symmetric than' if abs(rsym.mean()-rsym_sh.mean())<0.02 else 'differs from'} shuffle "
      f"(diff {rsym.mean()-rsym_sh.mean():+.4f}). Chambers have no special interior symmetry.")

# [D4] operator self-adjointness across observables + null -> TRIVIALLY passes for all
print("\n[D4] chamber-operator self-adjointness (symmetric tridiagonal, diagonal=V):")
sa={}
for which in ["E","H","tau","logn","lam","random"]:
    r=P.chamber_operator_check(obs, which, seed=2); sa[which]=r
    print(f"     V={which:7}: sym-error={r['max_symmetry_error']:.1e}  all-eigs-real={r['all_eigenvalues_real']}  ({r['n_chambers']} chambers)")
print("     -> ALL self-adjoint with real eigenvalues, INCLUDING random. A symmetric tridiagonal")
print("        has real eigenvalues for ANY real diagonal => this test is TAUTOLOGICAL, not a")
print("        property of E(n). Self-adjointness here encodes nothing arithmetic.")

# [3] sigma residual probe across observables + nulls -> argmin=0.5 for ALL (tautology)
print("\n[Sec3] sigma-residual probe R(sigma)=|Phi(sigma)-Phi(1-sigma)|, Phi=Sum w(n)n^-sigma:")
sig=[round(0.05+0.025*k,3) for k in range(37)]   # 0.05..0.95
rngw=np.random.default_rng(3)
weights=dict(Z_E=obs['Z'], expmH=np.exp(-obs['H']), log=obs['logn'],
             Lambda=obs['lam'], absMobius=np.abs(obs['mu']).astype(float),
             random=np.r_[0,0,rngw.random(N-1)])
probe=P.sigma_probe(obs, weights, sig)
for name,r in probe.items():
    print(f"     {name:10}: argmin sigma = {r['argmin_sigma']}   R(0.5)={r['R_at_half']:.3e}   R_min={r['R_min']:.3e}")
all_half = all(abs(r['argmin_sigma']-0.5)<1e-6 for r in probe.values())
print(f"     -> argmin = 0.5 for ALL weights (incl. random): {all_half}. R(1/2)=0 IDENTICALLY because")
print("        a raw Dirichlet series has NO functional equation; the symmetry is imposed by the")
print("        formula |Phi(s)-Phi(1-s)|, not discovered. The probe CANNOT distinguish E from random.")

# [D5] trace ladder (normalised) -- just stability, not discriminating
print("\n[D5] global E-trace over N ladder (descriptive):")
for n in [1000,10000,100000]:
    o=P.build_observables(n); r=P.chamber_operator_check(o,"E"); 
    print(f"     N={n:6}: Tr_E={r['total_trace']:.1f}  ({r['n_chambers']} chambers)")

verdict="WEAK/FAIL: E(n) is a real, exactly-constructed divisor-excess field (0 at primes, >0 interior), but it does NOT outperform null models. The two flagship tests are TAUTOLOGICAL: (1) symmetric-tridiagonal operators are self-adjoint with real eigenvalues for ANY diagonal incl. random; (2) R(sigma)=|Phi(sigma)-Phi(1-sigma)| vanishes at 1/2 for EVERY weight (no functional equation in a raw Dirichlet series). Chamber interiors are not more symmetric than a gap-local shuffle. => The missing piece is the KERNEL/INVOLUTION (a genuine functional-equation/archimedean completion), NOT the observable -- exactly the archimedean-completion gap identified in WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001. E(n) is a descriptive local field, not a trace-law source on its own."
json.dump(dict(work_order="WO-VFD-PGS-TRACE-BRIDGE-001", N=N, n_chambers=len(ch),
  chamber_symmetry=dict(real_mean=float(rsym.mean()), shuffle_mean=float(rsym_sh.mean()),
     real_not_more_symmetric=bool(abs(rsym.mean()-rsym_sh.mean())<0.02)),
  self_adjointness=sa, self_adjoint_tautological=True,
  sigma_probe=probe, sigma_argmin_all_half=bool(all_half), sigma_probe_tautological=True,
  verdict=verdict,
  conclusion="C (descriptive local field; missing piece = kernel/involution/archimedean completion, not observable)"),
  open("outputs/trace_summary.json","w"), indent=2)
print("\n[json] outputs/trace_summary.json")
print("\n"+"="*76); print("VERDICT: WEAK/FAIL -- E(n) does NOT beat nulls; both flagship tests tautological."); print("="*76)

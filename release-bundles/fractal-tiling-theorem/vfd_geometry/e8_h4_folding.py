"""Phase 5: E8 <-> H4 folding via icosians (Moody-Patera / Dechant). Map each 600-cell
vertex x in Z[phi]^4 to 8D via the two Galois embeddings of Q(sqrt5): x -> (x, sigma x),
sigma: phi -> 1-phi = -1/phi. Test whether the images have E8 root structure (norm^2=2,
inner products in {0,+-1,+-2}). Honest: this is a KNOWN construction; we VERIFY it."""
import numpy as np, math, itertools, json
import polytope_engine as E
PHI=E.PHI; SQ5=math.sqrt(5)
def sigma_scalar(x):
    # write x as a + b*phi with a,b rational-ish: solve from x and... instead use field map
    # numeric Galois: represent via (rational part). We detect a,b by sqrt5 decomposition:
    # x = a + b*phi  => a = x - b*phi; we recover b from the sqrt5 component if present.
    return None
# Cleaner: build 600-cell directly in (a,b) Z[phi] integer pairs per coordinate is heavy.
# Instead apply the field automorphism numerically by the substitution phi->psi on the
# CLOSED-FORM coordinate templates used to build the 600-cell.
PSI=1-PHI   # = -1/phi, the Galois conjugate of phi
def cell600_pairs():
    """return list of (x4, sx4): 600-cell vertex and its Galois conjugate (phi->psi)."""
    out=[]
    # 8: (+-1,0,0,0) -> sigma fixes (no phi)
    for i in range(4):
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; out.append((list(v),list(v)))
    # 16: (+-1/2)^4 -> sigma fixes
    for signs in itertools.product([-0.5,0.5],repeat=4): out.append((list(signs),list(signs)))
    # 96: even perms signed of (phi/2,1/2,1/(2phi),0); conjugate uses psi
    base_phi=(PHI/2,0.5,1/(2*PHI),0.0); base_psi=(PSI/2,0.5,1/(2*PSI),0.0)
    A4=[p for p in itertools.permutations(range(4)) if E._parity(p)==0]
    seen=set()
    for p in A4:
        vp=[0,0,0,0]; vs=[0,0,0,0]
        for pos,(bp,bs) in zip(p,zip(base_phi,base_psi)): vp[pos]=bp; vs[pos]=bs
        nz=[k for k in range(4) if abs(vp[k])>1e-12]
        for sgn in itertools.product([1,-1],repeat=len(nz)):
            a=list(vp); b=list(vs)
            for k,s in zip(nz,sgn): a[k]*=s; b[k]*=s
            key=tuple(np.round(a,9))
            if key in seen: continue
            seen.add(key); out.append((a,b))
    return out
pairs=cell600_pairs()
# build 8D images (x, sigma x) with the symmetric Q(sqrt5) Euclidean norm: weight so norm^2=2
imgs=[]
for a,b in pairs:
    v=np.array(a+b)            # (x, sigma x) in R^8
    imgs.append(v)
imgs=np.array(imgs)
n2=np.round((imgs*imgs).sum(1),6)
print("="*68); print("E8 <-> H4 FOLDING via icosians  (x -> (x, sigma x))"); print("="*68)
print(f"600-cell vertices mapped: {len(imgs)}")
print(f"unique norm^2 of 8D images: {np.unique(n2)}")
G=imgs@imgs.T
ips=np.unique(np.round(G[np.triu_indices(len(imgs),1)],4))
print(f"unique inner products: {ips}")
# Compare with genuine E8
E8=E.e8_roots(); 
print(f"\ngenuine E8: {len(E8)} roots, norm^2={np.unique(np.round((E8*E8).sum(1),4))}, "
      f"ips={np.unique(np.round((E8@E8.T)[np.triu_indices(len(E8),1)],4))}")
# honest check: norm uniform AND inner products in the E8 set?
match = set(np.round((imgs*imgs).sum(1),4))=={2.0}
ip_ok = set(ips.tolist()).issubset({-2.0,-1.0,0.0,1.0,2.0})
print(f"\n[result] all 120 images have norm^2 = 2 (E8 root norm): {match}")
print(f"         inner products lie in the E8 set {{0,+-1,+-2}}: {ip_ok}")
print( "         -> PARTIAL: the naive symmetric (x, sigma x) map gives UNIFORM norm^2=2 and a")
print( "            golden-doubled H4 structure, but its inner products include +-1/2, so it is")
print( "            NOT exactly the E8 root system. The exact icosian E8 = H4 + phi*H4 realization")
print( "            needs the properly WEIGHTED Q(sqrt5) trace form (Moody-Patera/Dechant), which")
print( "            we CITE rather than re-derive here. Confirmed: golden-doubled 8D structure with")
print( "            E8 norm; NOT confirmed: exact E8 inner-product lattice from the naive embedding.")
json.dump(dict(images=len(imgs), unique_norm2=np.unique(n2).tolist(),
   inner_products=ips.tolist(), all_norm2_is_2=bool(match),
   ip_subset_E8=bool(set(ips.tolist()).issubset({-2.0,-1.0,0.0,1.0,2.0})),
   note="naive (x,sigma x) of 600-cell -> 120 vectors, uniform norm^2=2 (golden-doubled H4) but ips include +-1/2 => NOT exactly E8; exact E8=H4+phiH4 needs weighted trace form (cited)"),
   open("results/polytype_transformation_engine_001/e8_h4_folding.json","w"), indent=2)

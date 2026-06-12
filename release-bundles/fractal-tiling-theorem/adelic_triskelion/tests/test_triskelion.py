import sys, os; sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
import numpy as np, geometry as G
def test_T1_threefold():
    ph=list(G.PHASES.values())
    d01=(ph[1]-ph[0])%(2*np.pi); d12=(ph[2]-ph[1])%(2*np.pi)
    assert abs(d01-2*np.pi/3)<1e-12 and abs(d12-2*np.pi/3)<1e-12, "arms not 2pi/3 apart"
    return "T1 threefold 2pi/3 separation: PASS"
def test_T3_prime_arm_only_primes():
    pa=G.prime_arm(200); assert all(G.is_prime(d['p']) for d in pa), "non-prime on finite arm"
    return f"T3 prime arm ({len(pa)} nodes) all prime: PASS"
def test_T4_archimedean_gaussian():
    ar=G.archimedean_arm(); err=np.max(np.abs(ar['profile']-np.exp(-np.pi*ar['u']**2)))
    assert err<1e-12, f"gaussian profile err {err}"
    # peak at u=0
    assert abs(ar['u'][np.argmax(ar['profile'])])<0.02, "gaussian not peaked at u=0"
    return "T4 archimedean profile = exp(-pi u^2), peaked at u=0: PASS"
def test_T2_scale_inversion():
    sc=G.scale_arm(U=2.5,n=401)   # odd n -> includes u=0, symmetric pairs
    u=sc['u']; n=len(u)
    # pair i <-> n-1-i has u <-> -u; check r(u)=r(-u) and z(u)=-z(-u) (involution as z->-z)
    maxr=0; maxz=0
    for i in range(n//2):
        j=n-1-i
        ri=np.hypot(sc['x'][i],sc['y'][i]); rj=np.hypot(sc['x'][j],sc['y'][j])
        maxr=max(maxr,abs(ri-rj)); maxz=max(maxz,abs(sc['z'][i]+sc['z'][j]))
    assert maxr<1e-9 and maxz<1e-9, f"scale inversion broken r{maxr} z{maxz}"
    return f"T2 scale inversion u<->-u (r even, z odd): PASS (r-err {maxr:.1e}, z-err {maxz:.1e})"
def test_T5_axis_invariant():
    ax=G.witness_axis(); assert all(x==0 for x in ax['x']) and all(y==0 for y in ax['y'])
    return "T5 witness axis x=y=0 invariant: PASS"
if __name__=="__main__":
    for t in [test_T1_threefold,test_T2_scale_inversion,test_T3_prime_arm_only_primes,
              test_T4_archimedean_gaussian,test_T5_axis_invariant]:
        print("  "+t())
    print("ALL TESTS PASS")

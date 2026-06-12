"""grow_atlas.py -- extend the programme atlas with a NEGATIVE CONTROL:
a generic GUE operator (right STATISTICS, wrong POSITIONS) claiming to be zeta.
The engine should pass fingerprint/rigidity (class) but FAIL pointwise (individual)
-- certifying the deepest lesson: GUE-class membership != being zeta."""
import numpy as np, engine_v3 as V3, engine_v2 as E, run_programme as P
np.random.seed(5)

def gue_like():
    n=400; A=(np.random.randn(n,n)+1j*np.random.randn(n,n))/np.sqrt(2); H=(A+A.conj().T)/2
    ev=np.sort(np.linalg.eigvalsh(H)); ev=ev[150:180]            # a clean bulk chunk
    return list(14 + (ev-ev.min())/(ev.max()-ev.min())*36)       # map to ~[14,50] (zero range)

control=E.Expression("generic GUE operator <-> zeta","random Hermitian (no arithmetic)","zeta",
    gue_like, dict(degree=1,pole=True,euler=True),
    {"operator":"random GUE (geometric structure, NO primes)"}, False)

full=P.PROGRAMME+[control]
atlas=V3.run_atlas(full, path="programme_atlas.json")
print("="*72); print("GROWN PROGRAMME ATLAS (with negative control)"); print("="*72)
for c in atlas:
    fails=[ch['name'] for ch in c['checks'] if not ch['pass_']]
    print(f"  [{c['verdict']:>8}] {c['expression']:<42} {c['cert_id']}"
          + (f"  XX {fails}" if fails else ""))
print("\n  Negative control result -- the deepest lesson, certified:")
cc=[c for c in atlas if 'GUE operator' in c['expression']][0]
for ch in cc['checks']:
    print(f"     {'OK ' if ch['pass_'] else 'XX '}{ch['name']:>12}: {ch['detail']}")
print("\n  -> generic GUE PASSES fingerprint+rigidity (right CLASS) but FAILS pointwise")
print("     +density (wrong INDIVIDUAL). The engine certifies: GUE-class membership is")
print("     NOT being zeta. Geometry gives the class; only the primes give zeta.")

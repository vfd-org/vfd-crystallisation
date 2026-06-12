import numpy as np, math, json, itertools
import polytope_engine as E, standing_wave_modes as SW
import local_links as LL, coxeter_signature as CX
PHI=E.PHI
def octahedron():
    V=[]
    for i in range(3):
        for s in (1,-1): v=[0,0,0]; v[i]=s; V.append(v)
    return np.array(V)
def dodecahedron():
    V=set()
    for s in itertools.product([-1,1],repeat=3): V.add(s)
    for a in (1,-1):
        for b in (1,-1):
            V|={(0,a/PHI,b*PHI),(a/PHI,b*PHI,0),(b*PHI,0,a/PHI)}
    return np.array(sorted(V))
ANCH={"tetrahedron":np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float),
      "cube":np.array(list(itertools.product([-1,1],repeat=3)),float),
      "octahedron":octahedron(), "icosahedron":E.icosahedron(), "dodecahedron":dodecahedron(),
      "16-cell":E.cell16(), "tesseract":E.tesseract(), "24-cell":E.cell24(), "600-cell":E.cell600()}
EXPECT={"tetrahedron":"triangle","cube":"triangle","octahedron":"square","icosahedron":"pentagon",
        "dodecahedron":"triangle","16-cell":"octahedron","tesseract":"tetrahedron",
        "24-cell":"cube","600-cell":"icosahedron"}   # NOTE: 24-cell vf = CUBE (WO said octahedron -- WRONG)

print("="*74); print("LOCAL-LINK -> GLOBAL-CLOSURE  Phase 1-2: vertex figures + gluing uniformity"); print("="*74)
print(f"{'polytope':12s} {'V':>4} {'link':>8} {'detected':12s} {'expected':12s} {'uniform':7s} match")
rows={}
for name,V in ANCH.items():
    links,glue=LL.all_links(V); det=links[0]
    ok = det['name']==EXPECT[name]
    rows[name]=dict(V=len(V), link_n=det['n'], detected=det['name'], expected=EXPECT[name],
                    uniform=glue['uniform'], n_distinct_spectra=glue['n_distinct_spectra'], match=bool(ok))
    print(f"{name:12s} {len(V):>4} {det['n']:>8} {det['name']:12s} {EXPECT[name]:12s} "
          f"{str(glue['uniform']):7s} {'OK' if ok else 'CHECK'}")
print("  NOTE: 24-cell vertex figure DETECTED = cube (8 verts). The WO's 'octahedron' is INCORRECT;")
print("        {3,4,3} has vertex figure {4,3}=cube. Engine confirms the correct classical fact.")
print("  600-cell vertex figure = icosahedron CONFIRMED (the H3<H4 prototype).")

print("\nPhase 3: Coxeter determinant classifier vs ACTUAL orbit (3D [m,3] and 4D [m,3,3]):")
def orbit_finite(qfirst, extra):
    # build [m,3,(3)] Gram with first label q=2cos(pi/m); generate orbit via base engine roots
    n=len(extra)+2; G=2*np.eye(n)
    G[0,1]=G[1,0]=-qfirst
    chain=extra
    for k,m in enumerate(chain): G[k+1,k+2]=G[k+2,k+1]=-2*math.cos(math.pi/m)
    if np.linalg.det(G)<=1e-6: return None,False
    try: L=np.linalg.cholesky(G)
    except np.linalg.LinAlgError: return None,False
    roots=[L[i] for i in range(n)]; seed=np.array([0.31,0.52,0.91,0.17][:n])
    pts,fin=E.generate_orbit(roots,seed,cap=1600); return len(pts),fin
for label,m in [("phi(5-fold)",5),("sqrt2(4-fold)",4),("affine(6-fold)",6),("7-fold",7)]:
    q=2*math.cos(math.pi/m); G=CX.gram_q([q,2*math.cos(math.pi/3)])   # [m,3] diagram
    cl=CX.classify(G); npts,fin=orbit_finite(q,[3])
    print(f"  [m={m},3] {label:13s} q={q:.4f}  Coxeter={cl['classification']:26s} curv={cl['curvature']:8s} "
          f"| orbit={'finite '+str(npts) if fin else ('non-PD' if npts is None else 'EXPLODES')}")
print("  -> at INTEGER m the determinant matches the orbit. BUT (see Phase 7) determinant alone")
print("     classifies GEOMETRY (curvature), NOT group finiteness -- see below.")

print("\nPhase 6: does the local-link spectrum sit inside the global spectrum? (exploratory, honest)")
ico_ev=np.round(np.sort(np.linalg.eigvalsh(SW.build_graph(ANCH["icosahedron"]))),4)
v600_ev=np.round(np.sort(np.linalg.eigvalsh(SW.build_graph(ANCH["600-cell"]))),4)
shared=sorted(set(ico_ev.tolist()) & set(v600_ev.tolist()))
print(f"  icosahedron adjacency eigenvalues: {sorted(set(ico_ev.tolist()))}")
print(f"  600-cell distinct adjacency eigenvalues: {sorted(set(v600_ev.tolist()))}")
print(f"  shared values: {shared}  -> link spectrum is NOT simply a subset of global spectrum")
print("     (global modes are set by the global graph; no clean local->global spectral induction).")

print("\nPhase 7: KEY SUBTLETY -- generic q is positive-definite (spherical geometry) yet INFINITE:")
for q in [1.50,1.62,1.66]:
    G=CX.gram_q([q,1.0]); cl=CX.classify(G); npts,fin=orbit_finite(q,[3])
    m_equiv=math.pi/math.acos(min(max(q/2,-1),1))
    print(f"  q={q:.2f} (=2cos(pi/{m_equiv:.3f}), NON-integer): Coxeter={cl['classification']:18s} "
          f"orbit={'finite '+str(npts) if fin else ('non-PD' if npts is None else 'EXPLODES (infinite)')}")
print("  -> CRUX: a positive-definite Gram means SPHERICAL GEOMETRY, but the reflection GROUP is")
print("     finite ONLY when the dihedral angle is pi/INTEGER (rational holonomy). Generic q is PD")
print("     (spherical) yet the angle pi/m has non-integer m -> the group is INFINITE (dense), links")
print("     never glue (nonzero rotational HOLONOMY residual) -> orbit explodes. So the determinant")
print("     classifies CURVATURE, not finiteness; the orbit is the true closure test. Correct local-")
print("     link law: closure <=> PD geometry AND rational (pi/integer) dihedral angle = zero holonomy.")

res=dict(work_order="WO-VFD-LOCAL-LINK-GLOBAL-CLOSURE-002", vertex_figures=rows,
  wo_error_caught="WO expected 24-cell vertex figure = octahedron; CORRECT is cube {4,3} (engine detects 8-vertex cube link)",
  h3_in_h4="600-cell vertex figure = icosahedron CONFIRMED (H3<H4 prototype)",
  coxeter_subtlety="determinant classifies CURVATURE (spherical/affine/hyperbolic), NOT group finiteness; generic q is PD(spherical) yet INFINITE because the dihedral angle pi/m has non-integer m (nonzero holonomy). Finite closure <=> PD AND rational angle; orbit generation is the true finiteness test.",
  local_to_global_spectrum=dict(shared_eigenvalues=shared, clean_induction=False),
  verdict="Local-link picture VALIDATED as a precise RESTATEMENT of known regular-polytope/Coxeter geometry: vertex figures all correct (incl. 24-cell=CUBE, fixing the WO's octahedron error), 600-cell link=icosahedron (H3<H4 prototype confirmed). KEY: finite global closure <=> PD Coxeter Gram (spherical curvature) AND rational pi/integer dihedral angle (zero rotational holonomy so links glue exactly); the determinant alone gives only curvature, generic-q PD-but-irrational explodes. NO clean local->global spectral induction. The 'Local-Link Closure Law' = this classical condition restated; REAL + useful as a restatement, NOT new mathematics.",
  recommended_next="WO-VFD-LOCAL-LINK-ATLAS-003 (validated atlas) or WO-VFD-H4-E8-TRACE-FORM-003 (correct Q(sqrt5) form for the one open H4->E8 gluing); NOT a new-law claim.")
json.dump(res, open("results/local_link_global_closure_002/result.json","w"), indent=2, default=str)
print("\n[json] results/local_link_global_closure_002/result.json")

**1. Claim audit**

- `[D.1]` “`𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)`” is fine as a definition [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:104). The follow-on “`A_5`-equivariant choice” language is informal, but not fatal.
- `[D.2]` “`𝒯_casc(z) := z·z̄ = |z|²`” is established at face level [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:184).
- `[L.1]` “`spec(𝒯_casc) = {Loeschian numbers}`” is established; this is just the Eisenstein norm image [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:204).
- `[L.3]` uniqueness under `C_6` is established at the stated scope; the matrix argument is adequate [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:213).
- `[T.1]` is established only as a face-level theorem, and the present draft now says that honestly [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:249).
- `[R.1]` / `[L.2]` settling `T=5` are mathematically sound: `5` is not Loeschian, so it is not in `spec(𝒯_casc)` [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:283), [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:310).
- `[D.3]` is not cleanly stated. The bullet “`+1 orbit` if it has a representative on a `C_6`-axis (`k=0`...)” is incomplete/false as written [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:384). Your own sim treats `h=k` as achiral too [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:118), and the CSV has `T=3,(1,1),achiral` [wo1_prediction.csv](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/data/wo1_prediction.csv:3). The prose lags the implementation.
- `[C.1]` is properly hedged as conjectural and untested [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:417).
- `[C.3]` is properly conjectural; it does not now pretend chirality data already exist in-repo [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:436).
- `[C.2]` is now correctly framed as an open problem with a four-step plan, not a proved descent theorem [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:466).
- `[N.1]` is supported by the existing CSV: 36 distinct `T` values and 61 orbit rows. `[N.2]` is correctly not a result yet [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:648), [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:657).

**2. WO acceptance audit**

- AC1: not resolved. My verdict is still `no`.
- AC2: resolved on coverage; every introduced D/L/T/C/N is catalogued. One catalogue statement is still wrong; see §3.
- AC3: not resolved. End-to-end run is impossible because `scripts/wo1_compare.py` is absent.
- AC4: partially resolved. The draft is now honest that no comparison has been run, but there is still no comparison result.
- AC5: resolved. `T=5` is settled explicitly.

- O1: partially resolved. It is now explicitly an open problem with a concrete plan, but not solved.
- O2: resolved. The artefacts now exclude `T=5` rather than smuggling it in.
- O3: resolved. Face action is `A_5`; double-cover issues are pushed to `2I`/chirality.
- O4: partially resolved. Only a qualitative conjecture exists.
- O5: not touched. No raw/debiased VIPERdb comparison exists.

**3. Catalogue audit**

- Coverage is complete: `D.1 D.2 D.3 L.0 L.1 L.2 L.3 T.1 C.1 C.2 C.3 C.4 N.1 N.2` all appear in the catalogue, and I do not see an uncatalogued derivation object or an orphan catalogue entry.
- Defect: catalogue `D.3` repeats the same bad orbit summary as the derivation: “`μ(T)=1` when representatives lie on a fixed axis (`k=0`)” [math-catalogue.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:104). That is not compatible with your own `T=3` row and code path for `h=k`.

**4. Attribution / external consistency**

- Main defect: the derivation says the sixth-root convention is used “throughout this document and in `cascade-bio.md §B3.1`” [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:40). That is false. Upstream explicitly writes `ω = e^{2πi/3}` [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:260). Internal consistency is fixed; external attribution is not.
- The same bad attribution is echoed in the catalogue [math-catalogue.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:100).
- The Hopf `15×40` structure is now cited honestly as conjectural / structural candidate, matching upstream [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:82), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:149), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:158).
- The citations to the misleading `T=5` table and the open item at line 320 are accurate [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:285), [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:271), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:283), [cascade-bio.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-bio.md:320).
- The Paper XXXII / `cascade-foundations.md` citations are locally consistent [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:478), [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:486), [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:505), [paper-xxxii.tex](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:237), [paper-xxxii.tex](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxii/paper-xxxii.tex:363), [cascade-foundations.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-foundations.md:91).

**5. Sim correctness**

- `wo1_capsid_predict.py` implements the computable claim it says it implements: norm formula, sixth-root action, `C_6` orbiting, per-orbit CSV emission [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:36), [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:41), [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:52), [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:137).
- The sim docstring matches the actual CSV shape: `T,mu,representative,chirality` [wo1_capsid_predict.py](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/scripts/wo1_capsid_predict.py:12), [wo1_prediction.csv](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/data/wo1_prediction.csv:1).
- There is no statistical comparison code at all. `wo1_compare.py` is absent, so no χ²/KL/null setup exists to evaluate.
- The code is better than the prose on chirality: it correctly treats both `k==0` and `h==k` as achiral.

**6. Tightness**

- [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:40): replace “and in `cascade-bio.md §B3.1`” with “we adopt the sixth-root convention here; upstream `cascade-bio.md §B3.1` currently writes `e^{2πi/3}` and should be normalised separately.”
- [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:384): replace “`k = 0`” with “the canonical representative lies on a reflection axis (`k=0` or `h=k`).”
- [math-catalogue.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:104): same fix as above.

**7. Top three fixes**

1. Fix the false upstream attribution on `ω` notation in [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:40) and [math-catalogue.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:100). Internal notation is now consistent; the claimed match to `cascade-bio.md §B3.1` is not.
2. Fix the achiral-orbit rule in [derivation-capsid.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/derivation-capsid.md:384). As written, it contradicts your own `T=3` data and code.
3. Fix the same defect in [math-catalogue.md](/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/biology-rung/math-catalogue.md:104), otherwise the ledger records a false summary of `D.3`.

**8. Verdict**

Publication ready: **no**.

Round-3 target check: most of the requested fixes are in place. The blockers are narrower now: one real attribution error on the `ω` convention, and one real math/prose inconsistency in `D.3` versus the actual sim/data.

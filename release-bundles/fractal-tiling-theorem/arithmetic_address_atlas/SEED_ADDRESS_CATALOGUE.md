# Seed Address Catalogue

The seed families fed to `atlas_builder.py`. Full machine output in
`atlas_entries.json` / `.csv`. Grade histogram (this run): **B:3, C:18, D:14, E:1, F:0**.

## B1 — God/portal composites → Grade **B**
`2^136279840+1`, `2^136279856+1`, M52 `2^136279841−1`. Composite Fermat-type
(forced factors `2^32+1`, `2^16+1`); calibration objects. See `GOD_PORTAL_CALIBRATION.md`.

## B2 — golden cyclotomic atoms (`5∣d`) → Grade **C–D**
`Φ_d(2)` for `d=5,10,15,20,25,30,40,50,60`. All factors split in `Q(√5)`
(split-fraction 1.000). First atoms `31,11,151,41,331` = icosian levels/Hecke
primes (Grade D). See `GOLDEN_CYCLOTOMIC_ATOMS.md`.

## B3 — non-golden controls (`5∤d`) → Grade **C**
`Φ_d(2)` for `d=3,7,8,9,11,13,16,32,64`. Mixed/inert factors; no forced split.
(`Φ_8=17`, `Φ_16=257`, `Φ_32=65537` all inert; `Φ_64=641·6700417` mixed.)

## B4 — icosian level/Hecke primes → Grade **D** (+ form at **E**)
`11, 31, 41, 151, 331` → prime ideals + Hecke operators. The level-31 Hilbert
newform itself → Grade **E** (coherent global L-function).

## B5 — random split primes + boundary → Grade **D**
`89,109,131,139,149,179,191,199` (split coordinates) + the order-sector/Hecke
decoupling test. See `HECKE_RESPONSE_BOUNDARY.md`.

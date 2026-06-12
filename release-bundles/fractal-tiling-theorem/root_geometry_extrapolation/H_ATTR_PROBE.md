# H_attr probe on the 26-dim σ-paired block — result

**H_attr (our conjecture):** a closure-flow suppresses the 26-mode σ-paired residue onto
the critical line. Closure operator `C_φ = (12+φ⁻²)I − A`; flow `e^{−tC_φ}` (smaller C_φ
eigenvalue ⇒ persists longer). Tested on the explicit block.

## Result: REFUTED (naive form)

**1. The σ-paired block STRADDLES the decay spectrum — it is not suppressed.**

| A-eig | C_φ (decay rate) | class |
|---|---|---|
| 12 | 0.382 | σ-fixed (Perron, slowest) |
| **6φ = 9.708** | **2.674** | **σ-PAIRED — 2nd slowest, PERSISTS** |
| **4φ = 6.472** | **5.910** | **σ-PAIRED — 3rd slowest, persists** |
| 3 | 9.382 | σ-fixed |
| 0 | 12.382 | σ-fixed |
| −2 | 14.382 | σ-fixed |
| **4−4φ = −2.472** | **14.854** | **σ-PAIRED — fast decay** |
| −3 | 15.382 | σ-fixed |
| **6−6φ = −3.708** | **16.090** | **σ-PAIRED — fastest decay** |

The flow PERSISTS the {6φ, 4φ} half and rapidly damps the {6−6φ, 4−4φ} half. It does not
suppress the residue — it breaks the σ-pair, growing the asymmetry.

**2. DECISIVE: σ-conjugate eigenvalues are distinct REAL numbers.**
`6φ = 9.708` vs `6−6φ = −3.708`; `4φ = 6.472` vs `4−4φ = −2.472`. Any real-spectral flow
(heat / closure / gradient) treats them differently. **The Galois (σ) pairing is an
ARITHMETIC symmetry invisible to real dynamics** — a flow sees real numbers, not Galois
orbits. So no real closure-flow can drive the residue onto Fix(τ) *as a Galois pair*.
H_attr cannot work via a real-spectral flow.

## Consequence (sharpens the residue map)
The 26-dim residue's openness is **not closable by an attractor / dynamical flow**. It
requires genuinely **arithmetic (Galois-aware)** structure — which loops straight back to
the root geometry (the arithmetic site), not a heat-flow suppression. This is an honest
NEGATIVE that explains WHY the residue stays open: closure-flow (real-analytic) and the
σ-pairing (arithmetic) do not see each other. Not a proof of anything; a refinement.

(Note: the paired-norm-fraction simulation in h_attr_probe.py is degenerate for the
all-ones seed — that vector is the σ-fixed Perron mode with zero paired content. The two
findings above are seed-independent.)

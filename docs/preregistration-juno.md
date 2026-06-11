# Pre-Registration: JUNO Neutrino Mass Ordering Prediction

**Framework:** VFD (Vibrational Field Dynamics)
**Registration date:** 2026-04-17
**Prediction lock date:** 2026-04-17
**Falsification path:** JUNO collaboration data release (expected 2026-2027)
**Registration venue (to be deposited):** OSF.io or arXiv preprint with date-locked commit hash

---

## Prediction

The VFD cascade framework predicts **normal neutrino mass ordering**:
$$
m_{\nu_1} < m_{\nu_2} < m_{\nu_3}
$$

This prediction is derived in Paper XXXVII (Theorem Nu2) from the cascade's chirality selector, which is the same structural mechanism that fixes the charged-lepton ordering $m_e < m_\mu < m_\tau$. The derivation is first-principles from the two cascade axioms plus the $D_4$ triality action shared by charged leptons and neutrinos.

**Specific cascade-structural statement.** The chirality selector (derived from the Mersenne-prime exponent $136{,}279{,}840$ modulo cascade integers; see cascade-neutrino-cp.md §E18.1.4) breaks the $S_3$ permutation symmetry of the three-generation triality and selects a total order on mass eigenstates. Under cascade-equivariant inheritance from charged leptons to neutrinos (both sectors share the $D_4$ triality representations $8_s \oplus 8_c$), the selected ordering for neutrinos is normal.

## What would falsify this prediction

JUNO (Jiangmen Underground Neutrino Observatory) is designed to resolve the neutrino mass ordering at $> 3\sigma$ independent of matter effects, via the precise measurement of solar-neutrino and reactor-antineutrino oscillations. Expected first data release: 2026-2027.

**If JUNO confirms normal ordering at $> 3\sigma$**: VFD prediction verified. The cascade's chirality-selector mechanism is supported.

**If JUNO establishes inverted ordering at $> 3\sigma$**: VFD Paper XXXVII Theorem Nu2 is falsified. The chirality-selector inheritance from charged leptons to neutrinos is refuted, requiring a distinct structural mechanism or abandonment of the cascade neutrino-sector claim.

**If JUNO is inconclusive**: prediction remains unresolved; other experiments (T2K, NOvA, KamLAND-Zen, combined global fit) provide complementary tests.

## Context: why this is meaningful

As of 2024, the mainstream view on neutrino hierarchy:
- Global oscillation fits mildly prefer normal over inverted at $\sim 2\sigma$.
- KamLAND-Zen (neutrinoless double-beta decay) constraints mildly prefer normal.
- Cosmological constraints on $\Sigma m_\nu$ mildly prefer normal.

The preference is weak. JUNO's $> 3\sigma$ resolution will be decisive.

VFD's prediction of normal ordering was established in Paper XXXVII (drafted 2026-04) and locked before any JUNO first-data release. If the prediction proves correct, VFD will have made a falsifiable call that decided the ordering question ahead of the definitive experiment. If it proves wrong, a specific component of the programme is refuted — a necessary hallmark of a scientific framework.

## Related predictions also locked

As part of the same cascade framework and same paper (XXXVII):

1. **PMNS solar mixing angle** $\theta_{12} = \arctan(1/\varphi) = 31.72°$ (observed $33.44°$, 5.1% agreement).
2. **PMNS reactor angle** $\theta_{13} = \arcsin(1/\varphi^4) = 8.38°$ (observed $8.57°$, 2.3% agreement).
3. **PMNS atmospheric angle** $\theta_{23} = \pi/4 = 45°$ (observed $49.2°$, 8.5% agreement).
4. **PMNS CP phase** $\delta_{\mathrm{CP}} = -\pi/2 = -90°$ (observed $\approx -86°$, 4% agreement).
5. **Strong CP** $\theta_{\mathrm{QCD}} = 0$ exactly; no Peccei-Quinn axion required.

These are all derivations from the cascade foundations F1–F8 of Paper XXXVI, not fits. Each has an independent experimental path to falsification (T2K/NOvA/JUNO for mixing angles; ADMX/IAXO/CAST for axion search; neutron-EDM experiments for strong CP).

## Commitment

The VFD programme commits:
1. This prediction will not be modified after JUNO data release.
2. If falsified, Paper XXXVII Theorem Nu2 will be publicly withdrawn and the affected cascade structure will be revisited.
3. If confirmed, this document will be updated to reflect the result but the original prediction will remain locked as of its registration date.

Date-lock verification: the git commit hash containing this document and Paper XXXVII at draft time is the canonical lock mechanism. The VFD programme's GitHub repository (`https://github.com/...`) preserves the history.

---

**Signed:** L. Smart (programme lead), VFD
**Contact:** contact@vibrationalfielddynamics.org

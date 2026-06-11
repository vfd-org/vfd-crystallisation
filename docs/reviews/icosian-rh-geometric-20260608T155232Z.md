Third-pass confirmation: the main repairs landed in the TeX: \(C_c^\infty\) Weil class, finite prime sums, \(Q_A\) as a quadratic form only, no RH assumption in the zero-side identification, Weil-equivalence not positivity proof, corrected zeta calibration scale, \(L_\infty=\Gamma_\mathbb C(s)^2\), and GRH-for-one-cuspidal-\(L\) scope. Remaining issues only:

**1. Claim Audit**

- [line 210](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:210>): “Let \(L=L(s,\pi)\) be the completed ... \(L\)-function, with completed form \(\Lambda(s)=...\).” This uses \(L\) as both completed and uncompleted. Edit: “Let \(L(s,\pi)\) be the finite/standard cuspidal \(L\)-function ... with completion \(\Lambda(s)=...\).”

- [lines 217-250](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:217>): \(C_c^\infty\) is adequate, and Paley-Wiener gives the needed entire extension. But “entire” alone does not state convergence of the zero sum. Add: “\(\widehat g\) is rapidly decreasing in every fixed horizontal strip, so the zero sum converges absolutely by standard zero-density bounds.”

- [lines 247-259](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:247>): \(h^*\) is not defined, and the real/even assumption is implicit. Without it, the symmetric translation formula gives \(\operatorname{Re} g(a)\), not necessarily \(g(a)\). Edit line 216 to “real-valued, even...” and define \(h^*(t)=h(-t)\), or use the Hermitian convention explicitly.

- [line 270](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:270>): “for all \(h\) of positive type” is wrong notation. \(g=h*h^*\) is positive type; \(h\) need not be. Edit: “for all admissible \(h\), equivalently for all positive-type \(g=h*h^*\) in Weil’s criterion.”

- [lines 277-283](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:277>): the numerical harness uses Gaussians/truncations, outside the compact-support theorem. Edit: “In a separate Gaussian, truncated numerical harness...” The corrected \(10^{-2}\) to \(2.4\times10^{-6}\) range is locally verified.

**2. Internal Consistency**

- Stale operator language remains at [line 75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:75>): “witness operator.” Edit to “witness form.”

- Figure source contradicts the form-only repair: [make_figures.py line 272](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/figures/make_figures.py:272>) says “\(A=A^\dagger\) self-adjoint”; [line 305](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/figures/make_figures.py:305>) says “OURS: \(A\ge0\)”. Edit to “form symmetric” and “\(Q_A\ge0\).”

- Unqualified “RH” remains in figure text: [make_figures.py lines 43, 55, 287](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/figures/make_figures.py:43>) and TeX caption [line 82](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:82>). Edit all to “RH\((L)\)” or “GRH for this cuspidal \(L\).”

**3. External Consistency**

- `Triad` verifies the exact \(\zeta_K(s)\zeta_K(s-1)\), \(C_2=1\), and \(r(\pi)=120(1+N\pi)\) claims.

- `Closure` verifies the “contains \(\zeta\) but does not isolate it” gate.

- `Witness` plus `weil_wall_results.json` verifies the zeta calibration range. I could not verify the precise “discretised convolution matrix symmetric to \(\le10^{-15}\)” claim in the cited Witness paper or shipped result files; only Boolean Brandt self-adjointness is present. Either cite the actual log/output or delete the \(10^{-15}\) number.

**4. Tightness**

- [line 41](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:41>): “Every step is exact, proved, or recalled” is too strong while figure/source labels still assert self-adjoint \(A\). After figure edits it is acceptable.

- [line 232](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:232>): “the \(k=1\) coefficient is \(a_\fq\)” ignores the \(\log N\fq\). Edit: “the \(k=1\) Satake trace is \(a_\fq\)” or “\(\Lambda_\pi(\fq)/\log N\fq=a_\fq\).”

**5. Surface Issues**

- `make_figures.py` docstring [line 11](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/figures/make_figures.py:11>) still says “operator reproduces known zeros.” Not visible in paper, but stale.

- No unresolved `\ref`/`\eqref` issue found in the TeX. No undefined TeX macro found by inspection.

**6. Top Three Fixes**

1. Regenerate roadmap/witness/landscape figures with \(Q_A\), not \(A\), and RH\((L)\)/GRH scope, not bare RH: TeX [line 82](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:82>), figure source [lines 272, 287, 305](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/figures/make_figures.py:272>).

2. Fix the witness proof notation: define \(h^*\), specify real-valued/Hermitian convention, and replace “\(h\) of positive type” with “\(g=h*h^*\) positive type”: [lines 216-270](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:216>).

3. Separate the compact-support theorem from Gaussian numerical checks: [lines 277-283](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-rh-geometric/papers/icosian-rh-geometric.tex:277>).

Publication-readiness: **No**. The core mathematical scoping is now mostly correct, but the stale figure text and the proof-notation gaps are still publication-blocking because they directly reintroduce the operator/RH over-claim the revision was meant to remove.

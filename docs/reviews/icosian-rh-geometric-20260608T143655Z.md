**Claim Audit**

- **MUST-RETREAT + alternative route**: “\(\langle h,Ah\rangle=\sum_\rho|\widehat h(\gamma_\rho)|^2\)” [line 220] is false off RH as written. For complex \(\gamma_\rho\), \(\widehat{h*h^*}(\gamma_\rho)\neq|\widehat h(\gamma_\rho)|^2\).  
  Alternative: state \(\langle h,Ah\rangle=\sum_\rho \widehat{(h*h^*)}(\gamma_\rho)\), and add “under RH this becomes \(\sum_\rho|\widehat h(\gamma_\rho)|^2\).” Then prove Theorem 12 by the Weil criterion, not by positivity of a non-real modulus expression.

- **MUST-RETREAT + alternative route**: The main equivalence “\(A\ge0\iff\mathrm{RH}(L)\)” [lines 230-237] is not established until the previous lemma, the test-function class, the completed \(L\)-function, and the bad local factors are made precise.  
  Alternative: define \(L\) as the completed level-\(\mathfrak p_{31}\) Hilbert cuspidal \(L\)-function, define \(Q_A(h)\) as the Weil explicit-formula quadratic form, then state \(Q_A(h)\ge0\ \forall h\) iff GRH for that \(L\).

- **MUST-RETREAT + alternative route**: “\(A=A_\infty-A_P\), self-adjoint on \(C_c^\infty(\mathbb R)\) (convergence by Ramanujan)” [lines 209-216] is not a valid operator statement. \(C_c^\infty\) is a test domain, not a self-adjoint Hilbert-space domain; the prime sum is locally finite against compact supports, not “convergent by Ramanujan.”  
  Alternative: first define a symmetric quadratic form/distribution on an admissible Weil test space. Only call it a self-adjoint operator after proving a closure/domain theorem.

- **OVERCLAIM-TO-CUT**: The archimedean theorem [lines 201-206] has undefined \(N\), undefined \(L_\infty\), and says “the archimedean place” although \(K=\mathbb Q(\sqrt5)\) has two real places. The Tate “scale-axis boundary” language is interpretive, not proved.  
  Edit: “The archimedean contribution in the explicit formula is represented by the Fourier multiplier with symbol …; this is the standard gamma/conductor term of the completed \(L\)-function.”

- **OVERCLAIM-TO-CUT**: “Complete short-vector enumeration … gives \(r(\pi)=120(1+N(\pi))\) at every prime” [lines 138-141]. The local Triad paper supports the universal statement via Eichler-Hijikata/Eichler-Brandt, while computation checks samples and the inert powers.  
  Edit: “The classical formula gives …; complete enumeration verifies the stated prime types and inert powers.”

- **OVERCLAIM-TO-CUT**: “the two \(L\)-factors are exactly the two terms” [lines 150-153]. The proof establishes the divisor-sum convolution globally and the two summands \(1+N(\pi)\) at prime ideals. For prime powers/composites there are more divisor terms.  
  Edit: “At a prime ideal, the two divisor choices \((1)\) and \(\pi\) give the two summands \(1\) and \(N(\pi)\); globally the product is the divisor-sum convolution.”

- **OVERCLAIM-TO-CUT**: “the shifted pair has zeros on \(\mathrm{Re}(s)=3/2\)” [lines 172-173]. That is GRH for the shifted factors. What is unconditional is that shifted nontrivial zeros lie in \(1<\mathrm{Re}(s)<2\), hence not on \(\mathrm{Re}(s)=1/2\).  
  Edit: “Under GRH they lie on \(\mathrm{Re}(s)=3/2\); unconditionally they contribute none on \(\mathrm{Re}(s)=1/2\).”

- **OVERCLAIM-TO-CUT**: Numerical corroboration “\(\sim10^{-7}\)” [lines 243-244, 251] is not supported by the cited Witness paper, which reports roughly \(10^{-2}\) to \(10^{-6}\). The figure script only attains \(\sim10^{-7}\) for some plotted Gaussian widths, not uniformly.  
  Edit: report the actual range and identify the truncations/zero count used.

- **Mostly OK**: Class number one [lines 99-102], Siegel-Weil identity [lines 128-135], Eisenstein face rejection [lines 183-188], and Brandt/cuspidal face [lines 190-195] are locally supported, but they should be labelled “recalled” or “imported” unless proofs are added.

**Internal Consistency**

- The paper says the equivalence is proved [lines 230-237], but later says the “one open step” is the boxed equivalence [lines 278-282]. That undersells the main theorem and confuses the ledger. The open frontier is \(A\ge0\), not the equivalence.

- \(N\) is overloaded: conductor in \(\log N\) [line 203] and norm in \(N(\mathfrak q)\) [lines 210-214]. Define the conductor as \(Q\) or \(\mathcal N\).

- \(\Lambda_\pi(N\mathfrak q^k)\) [line 210] is ambiguous because different prime ideals can have the same norm. Use \(\Lambda_\pi(\mathfrak q^k)\).

- Cross-references resolve; the build log shows no undefined refs/cites. Only an underfull hbox appears in the bibliography.

**External Consistency**

- `Triad` supports \(r(\pi)=120(1+N\pi)\), no local-2 correction, and \(L(\Theta,s)=\zeta_K(s)\zeta_K(s-1)\) via lines 633-658 and 734-757 of `icosian-triad.tex`. Caveat: that source has a normalization conflict at its line 710, where \(\widetilde r\) is written as \(r/8\), contradicting its own \(r/120\) convention.

- `Closure` supports the “\(\zeta\) not isolated” boundary: degree/factorization and gate rejection are at lines 156-187 and 235-237 of `the-closure-object.tex`. It also correctly avoids RH and cosmology claims.

- `Witness` supports the parameter-free Brandt prime side and the GRH-for-one-cuspidal-\(L\) scope [lines 28-35, 73-80, 103-108, 146-160]. It does **not** verify the new preprint’s explicit scale-axis operator \(A\), the claimed identification lemma, or the \(\sim10^{-7}\) numerical statement.

- The Brandt bundle locally supports self-adjoint Brandt operators and level-\(31\) coefficient recovery: see `icosian-realization.tex` lines 226-255, 267-282, and 469-489. It explicitly says finite Brandt data do not supply analytic positivity [lines 517-524].

**Overclaims To Cut**

- Title/abstract “Riemann Hypothesis” [lines 29, 51-52] should be qualified as “GRH/RH for the specific icosian cuspidal \(L\)-function.” The body mostly holds the scope; the headline does not.

- “Everything but the last step is exact” [lines 71-72] is too strong until the operator/test-space proof is repaired.

- “forced by norm-2 and integrality” [lines 106-107] is not proved here. Either prove uniqueness or say “chosen/standard in the Wilson--Moody--Patera construction.”

- “Hilbert--Pólya / Connes” among “proven-equivalent criteria” [lines 255-258] is too loose. Connes/HP are programmes/frameworks; Weil/Li/Jensen are criteria.

**Undersells To Strengthen**

- [lines 278-282] Strengthen the ledger: “The equivalence \(A\ge0\iff\mathrm{RH}(L)\) is Theorem 12; the open assertion is \(A\ge0\).”

- [lines 144-158] The divisor theorem can be stronger but cleaner: prove the full ideal divisor-sum convolution, then separately highlight the prime coefficient \(1+N(\pi)\).

- [lines 183-188] The structural degree-four factorization already rules out “object \(=\zeta\)” as an \(L\)-function identity; the numerical gate is secondary corroboration.

**Surface Issues**

- \(C_2\) appears [line 133] without definition.

- Bibliography entries for Wilson/Siegel/Weil are too incomplete for a publication draft.

- “Riemann zeros” in the witness figure/corroboration [lines 243, 251] invites confusion with the target cuspidal \(L\). Say “zeta calibration zeros.”

- “archimedean place” should be plural or replaced by “archimedean contribution.”

**Top Three Fixes**

1. Fix Lemma 11 and Theorem 12 [lines 219-237]. This is the load-bearing mathematical defect.
2. Replace the informal operator definition with a precise completed \(L\)-function, test space, quadratic form, bad-prime convention, and conductor/gamma data [lines 190-216].
3. Cut the unconditional shifted-zero and numerical-precision overclaims [lines 169-173, 240-244].

**Publication Readiness**

No. The narrative scope is mostly correct, but the main operator equivalence is not publication-ready until the Weil-form identification is stated correctly and the operator/domain claims are made precise.

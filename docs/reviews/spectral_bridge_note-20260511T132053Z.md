Publication ready: **no**. One substantive must-fix remains.

**1. Claim Audit**
All main mathematical claims now look established except the revised spectrum exactness claim.

Must-fix: [spectral_bridge_note.tex:221](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:221>) claims “the integer entries of both spectra below additionally agree with exact SymPy nullspace computations … at every integer λ in the relevant range,” and [line 238](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:238>) says these dimensions are computed by `closure_transform_engine.keystone`.

I cannot verify that locally. The keystone code certifies exact rational nullspaces for λ=12 only: `exact_certify_lambda12_lift` is λ=12-specific ([keystone.py:548](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/closure_transform_engine/keystone.py:548>)), and `exact_a5_characters` builds `L_global - 12I` and local `L_C - 12I` only ([keystone.py:284](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/closure_transform_engine/keystone.py:284>), [keystone.py:309](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/closure_transform_engine/keystone.py:309>)). The tests likewise check exactness only for λ=12 and A5 data, not every integer spectral entry.

**2. Internal Consistency**
The line-221 exact-spectrum claim is inconsistent with the reproducibility section: [spectral_bridge_note.tex:481](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:481>) lists what the runner verifies, but does not include all-integer exact spectrum nullities. Cross-references otherwise resolve coherently.

**3. External Consistency**
Paper V supports the floating-point spectrum comparison and gives the 600-cell exact spectral forms locally ([paper-v.tex:104](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-v/paper-v.tex:104>), [paper-v.tex:117](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-v/paper-v.tex:117>)). Paper XXXV supports the left-coset Schläfli decomposition and A5 action ([paper-xxxv.tex:284](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxv/paper-xxxv.tex:284>), [paper-xxxv.tex:416](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxxv/paper-xxxv.tex:416>)); the right-coset transfer by inversion is mathematically sound. No other attribution blocker found.

**4. Tightness**
Replace [line 221](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:221>) with either:
“the λ=12 integer multiplicities used below are certified by exact SymPy nullspace computations”
or add a checked artifact/test that computes all stated integer nullities exactly.

**5. Surface Issues**
No surface issue rises to substantive must-fix level.

**6. Top Three Fixes**
1. Fix or substantiate the all-integer exact SymPy spectrum claim at [line 221](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:221>).
2. No second substantive math/attribution must-fix found.
3. No third substantive math/attribution must-fix found.

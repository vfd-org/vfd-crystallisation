# God / Portal Calibration (family B1)

Preserved honestly as **calibration objects**, not RH keys.

| object | grade | finding |
|---|---|---|
| God `2^136279840+1` | **B** | composite; `n=2^5·5·851749`; forced factor `2^32+1=641·6700417`; 4 active `+1` sectors (smallest `d=64`) |
| Portal `2^136279856+1` | **B** | composite; `n=2^4·19·61·7349`; forced factor `2^16+1=65537`; 8 active sectors (smallest `d=32`) |
| M52 `2^136279841−1` | (prime) | the genuine largest-known Mersenne (exponent prime); the `−1` sibling |

## Plus/minus separation (Test 2 — prevents the earlier sign confusion)
- `31 ∣ 2^136279840 − 1` ✅ (because `5 ∣ n`, via `Φ₅(2)=31`, Theorem 3)
- `31 ∤ 2^136279840 + 1` ✅ (the `+1` side activates `v₂(d)=6`, Theorem 4)

So the golden atom `31` is reached only through the **minus sibling**, never the
`+1` mega-number. The `+1` objects route into the 2-power Fermat tower (`2^32+1`,
`2^16+1`), which is *not* the golden field.

## Verdict
God/portal `+1` numbers stop at **Grade B** (cyclotomic address, composite). They
carry no resonance above noise (null-tested elsewhere) and no RH relevance. Their
only value is as the **signpost** that led to the golden split law (Theorem 2).
Guardrail: `VFD_Field_Calculator/vfd_prime_irreducibility_sanity_test.py`.

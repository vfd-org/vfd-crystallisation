# Capacity object — summary (with a labeling correction)

The verified finite centre (route_b / capacity-limit WOs) is the Weil positivity form
`Q_W = A + P − R`, with `H = A + P` (capacity), `K = H^{−1/2} R H^{−1/2}`, `‖K_N‖→1`
from below, stable non-escaping near-null mode, nulls failing.

**Correction to this WO's labeling.** The WO writes `H = A∞ + P_F` (archimedean +
*prime* capacity) and `R_S` = scale reflection. The **verified operators say otherwise**:
- `A` = **archimedean** local factor (digamma `Re ψ(¼+ir/2)`) — *sign-indefinite alone*.
- `P` = the **pole** term (the `s=1` pole of ζ, with `−log π`) — *lifts `A` to PSD*.
- `R` = the **finite-prime / von Mangoldt** term `2Σ Λ(n)n^{−1/2}g(log n)`.

So `H = A + P` = **archimedean + pole** (the capacity), and **`R` = the primes** = the
**reflection**. The primes are *not* a capacity; they are the pressure the capacity must
dominate. (This is exactly the Weil explicit formula `zeros = arch + pole − primes`.)

**Corrected geometry / dictionary:**
> capacity `H` = archimedean place + pole;  reflection `R` = finite primes;
> RH ⟺ `R ≤ H` ⟺ `‖K‖≤1` ⟺ prime reflection never exceeds archimedean+pole capacity.

Nulls confirm this: removing `A` (archimedean) makes `H` non-PSD (capacity destroyed,
−4.99); a fake Γ over-reflects (`‖K‖=1.67>1`); shuffling the primes changes `R` (the
reflection), not the capacity.

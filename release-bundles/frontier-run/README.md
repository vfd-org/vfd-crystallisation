# frontier-run — extend the icosian Brandt eigenvalues, resolve the cuspidal L's own zeros

A self-contained background job for a many-core machine (built for the ARIA PC:
Ryzen 9950X3D, 64 GB). It pushes the **math frontier** of the icosian programme one
concrete step: it computes the geometric Brandt cuspidal eigenvalues `a_q` far past the
shipped baseline (norm ≤ 150), then uses them to find the **icosian cuspidal
L-function's own non-trivial zeros out-of-sample** and runs the Weil explicit-formula
identity against *those* zeros.

> **This does not prove RH.** `RH(L)` here means GRH for this one cuspidal `L`-function,
> not classical RH. Positivity (the actual hard inequality) is untouched. What this run
> *can* deliver is a clean, falsifiable out-of-sample check: the zeros the L-data
> predicts must satisfy `lfuncheckfeq ≈ 0` (functional equation self-consistent) and the
> explicit formula `ARCH(g) − PRIME(g) = 2·Σ h(γ)` must close on the found zeros. If it
> doesn't, the geometric eigenvalues are wrong somewhere — that's the value.

---

## What it is, in two stages

**Stage A — geometric eigenvalues (parallel, checkpointed, resumable).**
For every prime ideal of `K = ℚ(√5)` with norm ≤ `--norm-bound`, compute the cuspidal
Brandt eigenvalue `a_q` with the verified `BrandtEngine`. Embarrassingly parallel across
prime ideals. Writes `out/a_q_extended.json` every 25 ideals; on restart it **skips
everything already done** and resumes. Validates as it goes: the ≤150 baseline must match
**exactly** (0 mismatches), and every eigenvalue must satisfy Ramanujan
`|a_q| ≤ 2√N` and (away from the level prime) self-adjointness.

**Stage B — the L-function's zeros (single process, needs Stage A output).**
Builds the degree-4 Dirichlet coefficients `λ(n)` from the local Euler factors
(split / inert / ramified-5 / the bad level prime 𝔭₃₁ which splits into a Steinberg
degree-1 factor × a good degree-2 factor), hands the L-data to **PARI/GP**
(`lfuncheckfeq` self-validates the functional equation; `lfunzeros` finds the zeros),
then runs the out-of-sample explicit-formula check. Writes `out/zeros_result.json`.

---

## Requirements

- **Python 3** with **numpy** (`pip install numpy`). `mpmath` optional (not needed for
  the PARI path). No other Python deps; the engine is pure Python and vendored in
  `engine/`.
- **PARI/GP** for Stage B — the `gp` binary must be on PATH.
  - Linux: `sudo apt install pari-gp`
  - Windows: install from <https://pari.math.u-bordeaux.fr/download.html> and either add
    `gp.exe` to PATH or pass its full path (edit the `gp=` default in `stage_b`).
  - Stage A needs **no** PARI — you can run Stage A now and Stage B later.

---

## How to run it (take as long as it takes)

Everything is resumable, so the pattern is: **set a high norm bound, launch it in the
background, walk away.** Re-launching the same command picks up where it left off.

```bash
cd frontier-run

# Full run, all cores but two, default norm-bound 50000, then zeros:
python3 run_frontier.py --stage both --procs 30

# Or split it. Stage A first (the long part), as high as you have patience for:
python3 run_frontier.py --stage a --norm-bound 100000 --procs 30
# ...later, after A finishes (or even partway), find the zeros:
python3 run_frontier.py --stage b --nmax 8000
```

**Windows PowerShell**, run detached so you can close the terminal:
```powershell
Start-Process -NoNewWindow python "run_frontier.py --stage a --norm-bound 100000 --procs 30" `
  -RedirectStandardOutput frontier.log -RedirectStandardError frontier.err
```
**Linux/WSL**, same idea:
```bash
nohup python3 run_frontier.py --stage a --norm-bound 100000 --procs 30 > frontier.log 2>&1 &
```
Then `tail -f frontier.log`. Kill it any time (Ctrl-C / close); the checkpoint in
`out/a_q_extended.json` is safe and the next launch resumes.

### Flags
| flag | default | meaning |
|------|---------|---------|
| `--stage` | `both` | `a`, `b`, or `both` |
| `--norm-bound` | `50000` | Stage A: include every prime ideal with norm ≤ this. **This is the knob.** |
| `--procs` | cpu−2 | Stage A worker processes. On the 9950X3D use `30`. |
| `--nmax` | `4000` | Stage B: build λ(n) up to this n (raise it if coverage allows). |

---

## How far to push the norm bound (coverage → zeros)

Stage B needs a long run of **consecutive** clean coefficients `λ(1..Ncov)` — coverage
breaks at the first prime whose ideal(s) Stage A hasn't computed yet. Roughly:

```
Ncov  ≈  norm_bound        (split/ramified primes p ≤ norm_bound are covered;
                            inert primes need p² ≤ norm_bound, i.e. p ≤ √norm_bound,
                            so the first gap is the smallest inert prime above √norm_bound)
```

For the degree-4, conductor-775 L-function, resolving the **first few honest zeros**
wants on the order of a few hundred clean coefficients. Practical targets:

| `--norm-bound` | rough `Ncov` | what you get |
|----------------|-------------|--------------|
| 2,000          | ~40         | too low — Stage B will say "coverage too low" and stop cleanly |
| 50,000         | ~220        | first zeros start to resolve |
| 100,000        | ~310        | comfortable for the low zeros + explicit-formula check |
| 250,000+       | ~500        | tighter explicit-formula closure at the larger σ |

Stage A cost grows faster than linearly (inert primes cost ~p² of enumeration), so
100,000 is a sensible first target on the ARIA PC — likely a several-hour-to-overnight
run on 30 cores. If you have the patience, point it at 250,000 and let it sit. Stage B
itself is fast (PARI does the heavy lifting in seconds–minutes).

Stage B is **safe to run early and often**: if coverage is too low it writes a small
`zeros_result.json` noting the first missing prime and exits without error. Re-run it
after Stage A has climbed higher.

---

## What to send back

When it's had a good run, send me these two files:

- `out/a_q_extended.json` — all the geometric eigenvalues (this is the real new data;
  it extends the programme's baseline and is independently useful).
- `out/zeros_result.json` — the L-zeros PARI found, `lfuncheckfeq` value, and the
  out-of-sample explicit-formula numbers.

The log (`frontier.log`) is handy too — it shows the live `[A] N=… a_q=…` stream and the
`[B]` coverage / zeros / functional-equation lines.

### Reading the result
- `lfuncheckfeq_log2` **very negative** (e.g. −20 or below) ⇒ the L-data is functional-
  equation-consistent and the zeros are trustworthy. Near 0 ⇒ something's off in the
  coefficients (a wrong/missing local factor) — that's a real finding, not a failure.
- `explicit_formula_out_of_sample[*].rel_err` should shrink as more zeros come in below
  the height the chosen σ probes. It is only expected to be tight when the found zeros
  reach high enough for that σ; the note field flags this.

---

## Layout
```
run_frontier.py                  the driver (Stage A parallel + Stage B PARI)
engine/                          vendored verified BrandtEngine (pure Python, no SAGE)
  ok_arithmetic.py  quaternion_order.py  brandt_matrices.py
  ideal_classes.py  geometric_aP.py
out/
  geometric_aP_baseline.json     the shipped ≤150 baseline (Stage A validates against it)
  a_q_extended.json              (created) the extended eigenvalues — resume lives here
  zeros_result.json              (created) Stage B output
```

## Scope / honesty
Geometry-first. The eigenvalues are point-counted from the icosian Brandt operator at
level 𝔭₃₁ — **no fitting**. This run explores the icosian cuspidal `L`'s own zeros; it
says nothing about classical `ζ`, and nothing about positivity. It's the
"push the math frontier" step, run at scale.

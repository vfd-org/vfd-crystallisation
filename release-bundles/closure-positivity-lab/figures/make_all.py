#!/usr/bin/env python3
"""Regenerate the whole closure-positivity-lab visual suite, reproducibly.

    python3 make_all.py            # builds every figure + animation from the data

All figures are GEOMETRY-ONLY (point-counted eigenvalues; NO zero data enters any
reconstruction). The 33 PARI-computed zeros appear only as an external overlay/check.
Prereqs: numpy, matplotlib (ffmpeg optional, for the .mp4; falls back to .gif).
Needs ../out/curve_zeros.json (run `python3 -m lab.curve_stage_b` first if missing).
"""
import os, sys, time

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))


def _ensure_zeros():
    zp = os.path.join(H, "..", "out", "curve_zeros.json")
    if not os.path.exists(zp):
        print("[make_all] curve_zeros.json missing -> running Stage B (point counts + PARI)")
        from lab.curve_stage_b import main as stageb
        stageb(nmax=3000, height=25.0)


def main():
    t0 = time.time()
    _ensure_zeros()
    steps = [
        ("diffraction (primes -> zeros, static)", "make_diffraction", "make"),
        ("hologram fractions (a fragment -> the whole)", None, None),  # via lab.prime_wave
        ("diffraction animation (cells build the spectrum)", "make_diffraction_anim", "make"),
    ]
    # 1 + 3: figure scripts in this dir
    import importlib
    for label, mod, fn in steps:
        if mod is None:
            continue
        print(f"\n=== {label} ===", flush=True)
        m = importlib.import_module(mod)
        getattr(m, fn)()
    # 2: hologram demo lives in lab.prime_wave
    print("\n=== hologram fractions (a fragment -> the whole) ===", flush=True)
    from lab.prime_wave import hologram_demo
    hologram_demo()
    print(f"\n[make_all] done in {time.time()-t0:.0f}s -> figures in {H}")
    for f in ("fig_diffraction.png", "fig_hologram.png", "anim_diffraction.mp4",
              "anim_diffraction.gif"):
        p = os.path.join(H, f)
        if os.path.exists(p):
            print(f"   {f}  ({os.path.getsize(p)//1024} KB)")


if __name__ == "__main__":
    main()

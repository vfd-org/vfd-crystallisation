"""Closure-positivity laboratory -- core.

One question, computed exactly on finite objects:

    when does a closure object's structure operator T, self-adjoint under its
    INVARIANT trace form B, actually become POSITIVE under that form?

The programme's trace-form law already established: the right form B is NECESSARY
(it is what makes T self-adjoint, hence real-spectrum) but NOT SUFFICIENT for
positivity.  This lab hunts the missing sufficient ingredient by tabulating, over
many finite closure objects where BOTH sides are exactly computable:

    (is it a closure fixed point?)   x   (is T positive under B?)   x   structural features

and searching for the structural feature that separates the positive from the
non-positive.  That feature is the candidate "VFD positivity law"; RH is the
instance where it is asymptotic (all-places) and therefore open.

A ClosureObject ships two matrices, B (the invariant form) and T (the structure
operator), plus optional metadata.  Everything downstream is uniform linear algebra.
The GATE (see verdict()) refuses to call an object "positive" unless the right form
is actually present (T self-adjoint under B) -- so a fitted/wrong-form map cannot
sneak a positive verdict.  Same discipline as the verification engine.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np

TOL = 1e-9


def _sym(M):
    return 0.5 * (M + M.T)


def _eigs_sym(M):
    return np.sort(np.linalg.eigvalsh(_sym(M)))


@dataclass
class ClosureObject:
    name: str
    family: str
    B: np.ndarray                      # invariant trace form (symmetric)
    T: np.ndarray                      # structure operator (closure / mult / Brandt / Gram)
    # closure status: is this object a fixed point of its closure (complete / stable)?
    is_fixed_point: bool = True
    fixed_point_reason: str = ""
    # asymptotic-positivity escape hatch: finite face is positive but the
    # all-places (Weil) positivity is the genuinely open question (the RH instance).
    asymptotic_open: bool = False
    notes: str = ""
    extra: dict = field(default_factory=dict)

    # ---- the two faces -------------------------------------------------------
    def self_adjoint(self) -> bool:
        """Right form present:  B T symmetric  <=>  T self-adjoint w.r.t. B."""
        BT = self.B @ self.T
        return np.allclose(BT, BT.T, atol=1e-7)

    def form_posdef(self) -> bool:
        """Is the invariant form B itself positive-definite?"""
        return bool(_eigs_sym(self.B)[0] > TOL)

    def T_spectrum(self):
        """Eigenvalues of T = its values at the 'places' / conjugates."""
        return np.sort(np.linalg.eigvals(self.T).real
                       if np.allclose(np.linalg.eigvals(self.T).imag, 0, atol=1e-6)
                       else np.linalg.eigvals(self.T))

    def real_spectrum(self) -> bool:
        return bool(np.allclose(np.linalg.eigvals(self.T).imag, 0, atol=1e-6))

    def totally_positive(self) -> bool:
        """All places positive: every eigenvalue of T (its conjugates) > 0."""
        ev = np.linalg.eigvals(self.T)
        return bool(np.all(ev.real > TOL) and np.allclose(ev.imag, 0, atol=1e-6))

    def B_positive(self) -> bool:
        """T positive under B:  the form  x -> x^T (B T) x  is positive-definite.
        Requires self-adjointness for this to be a real symmetric form at all."""
        if not self.self_adjoint():
            return False
        return bool(_eigs_sym(self.B @ self.T)[0] > TOL)

    # ---- the gated verdict ---------------------------------------------------
    def verdict(self) -> dict:
        sa = self.self_adjoint()
        tp = self.totally_positive()
        bp = self.B_positive()
        # GATE: without the right form, no positive verdict is allowed.
        if not sa:
            pos = "REJECTED_WRONG_FORM"
        elif self.asymptotic_open:
            pos = "FINITE_POSITIVE_ASYMPTOTIC_OPEN"
        else:
            pos = "POSITIVE" if bp else "NOT_POSITIVE"
        return {
            "name": self.name, "family": self.family, "dim": int(self.B.shape[0]),
            "is_fixed_point": self.is_fixed_point,
            "self_adjoint": sa, "form_posdef": self.form_posdef(),
            "real_spectrum": self.real_spectrum(),
            "totally_positive": tp, "B_positive": bp,
            "positivity": pos,
            "T_spectrum": [round(float(x), 4) for x in
                           (self.T_spectrum() if self.real_spectrum()
                            else np.linalg.eigvals(self.T))][:12],
            "notes": self.notes, **self.extra,
        }


def features(o: ClosureObject) -> dict:
    """The structural features the discriminator search ranges over."""
    return {
        "self_adjoint": o.self_adjoint(),       # right form present (necessary)
        "form_posdef": o.form_posdef(),         # B itself positive
        "real_spectrum": o.real_spectrum(),     # T has real conjugates
        "totally_positive": o.totally_positive(),  # candidate sufficient ingredient
    }


def discriminator_search(objs):
    """Across all objects that have the right form (self-adjoint, finite-decidable),
    find which single feature exactly predicts B_positive.  Returns each feature's
    agreement rate with the positive/not-positive label."""
    pool = [o for o in objs if o.self_adjoint() and not o.asymptotic_open]
    labels = [o.B_positive() for o in pool]
    feats = ["form_posdef", "real_spectrum", "totally_positive"]
    out = {}
    for f in feats:
        vals = [features(o)[f] for o in pool]
        agree = sum(1 for v, l in zip(vals, labels) if v == l)
        out[f] = {"agreement": agree, "of": len(pool),
                  "exact_match": agree == len(pool)}
    return {"n_decidable": len(pool), "n_positive": sum(labels), "by_feature": out,
            "objects": [o.name for o in pool]}

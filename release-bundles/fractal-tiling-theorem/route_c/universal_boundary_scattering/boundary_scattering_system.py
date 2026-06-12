"""Abstract BoundaryScatteringSystem schema (WO-RH-UNIVERSAL-BOUNDARY-SCATTERING-001).

A closed boundary-scattering system is the 7-tuple:
  (impulse_source, capacity_term, determinant, response, resonances, stability, failure_mode)
with response(z) = d/dz log determinant(z), resonances = zeros/poles of the determinant,
and stability = (resonances lie in/on the allowed boundary domain) <=> normalised response
is contractive. This is the trace-formula / scattering-determinant architecture (Selberg/
Weil; Lax-Phillips/Faddeev-Pavlov for zeta). The schema is shared; the INSTANCES decide
whether it yields new math.
"""
from dataclasses import dataclass, field, asdict
from typing import Any
@dataclass
class BoundaryScatteringSystem:
    name: str
    impulse_source: str       # closed orbits / source quanta
    capacity_term: str        # boundary / greybody / archimedean completion
    determinant: str          # xi / Jost / scattering det
    response: str             # d log det = log-derivative
    resonances: str           # zeros / QNM poles
    stability_form: str       # contraction / no-growing-mode / positivity
    control_model: str        # smooth / non-self-adjoint failure
    failure_mode: str         # off-line zero / growing QNM
    provable: str             # is stability provable in THIS instance, and why
    def dict(self): return asdict(self)

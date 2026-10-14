"""Part B: physics check. TODO 3."""
from __future__ import annotations

import math

G = 9.81


def is_feasible(p: dict) -> bool:
    """TODO 3. False for scenarios no real road user could produce. Reject if ANY of:

    - the lane change needs more sideways grip than the road has: the cosine lane change of 3.5 m over
      p["cutDur"] seconds peaks at a_lat = (pi / cutDur)^2 * 3.5 / 2; reject if a_lat > mu * g;
    - the post-merge braking p["cutBrake"] exceeds mu * g;
    - the pedestrian runs: p["pedV"] > 2.5 m/s;
    - the cut-in speed p["cutV"] is not in (0, 22] m/s.
    mu is p["mu"]. A search that keeps infeasible scenarios reports failures that cannot happen.
    """
    mu = p["mu"]
    mu_g = mu * G

    # 1. Lane change sideways grip
    a_lat = ((math.pi / p["cutDur"]) ** 2) * 3.5 / 2.0
    if a_lat > mu_g:
        return False

    # 2. Post-merge braking exceeds mu * g
    if p["cutBrake"] > mu_g:
        return False

    # 3. Pedestrian runs: pedV > 2.5 m/s
    if p["pedV"] > 2.5:
        return False

    # 4. Cut-in speed not in (0, 22]
    if not (0.0 < p["cutV"] <= 22.0):
        return False

    return True

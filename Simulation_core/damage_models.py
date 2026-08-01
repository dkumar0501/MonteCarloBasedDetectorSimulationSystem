"""
Physics-based models to compute radiation-induced damage and dose.
"""

import numpy as np

def compute_displacement_damage(energy_dep, fluence, E_disp):
    """
    Computes displacement damage (DPA-equivalent).
    """
    constant = 1e-18
    return (energy_dep / E_disp) * fluence * constant

def compute_dose(energy_dep, density):
    """
    Converts energy deposition (MeV) into dose (Gray).
    1 MeV = 1.602e-13 Joules.
    """
    joule_per_MeV = 1.60218e-13
    return (energy_dep * joule_per_MeV) / (density * 1e-3)

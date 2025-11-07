"""
Defines the physical and radiation parameters of materials
used for radiation-hard sensor simulations.
"""

MATERIALS = {
    "Silicon": {
        "density": 2.33,                 # g/cm^3
        "stopping_power": 1.0,           # relative scaling
        "displacement_energy": 25,       # eV
        "light_yield": 0,                # photons/MeV
    },
    "GaN": {
        "density": 6.15,
        "stopping_power": 0.85,
        "displacement_energy": 20,
        "light_yield": 12000,
    },
    "Diamond": {
        "density": 3.52,
        "stopping_power": 1.2,
        "displacement_energy": 43,
        "light_yield": 15000,
    },
    "Scintillating_Fibre": {
        "density": 1.05,
        "stopping_power": 0.7,
        "displacement_energy": 15,
        "light_yield": 8000,
    },
}

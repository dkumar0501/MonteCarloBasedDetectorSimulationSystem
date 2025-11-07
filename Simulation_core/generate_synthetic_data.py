"""
Generates synthetic irradiation datasets mimicking Geant4 output.
Includes deposited energy, fluence, dose, and damage metrics.
"""

import numpy as np
import pandas as pd
from material_properties import MATERIALS
from damage_models import compute_displacement_damage, compute_dose

np.random.seed(42)
NUM_SAMPLES = 20000
BEAM_ENERGY_MEV = 60

def generate_data():
    all_data = []

    for material, props in MATERIALS.items():
        fluence = np.random.uniform(1e10, 5e12, NUM_SAMPLES)
        deposited_energy = np.random.exponential(scale=props["stopping_power"], size=NUM_SAMPLES)
        damage = compute_displacement_damage(deposited_energy, fluence, props["displacement_energy"])
        dose = compute_dose(deposited_energy, props["density"])

        df = pd.DataFrame({
            "Material": material,
            "BeamEnergy_MeV": BEAM_ENERGY_MEV,
            "Fluence_cm2": fluence,
            "DepositedEnergy_MeV": deposited_energy,
            "Dose_Gray": dose,
            "DamageIndex": damage,
            "LightYield_photons": props["light_yield"] * deposited_energy
        })
        all_data.append(df)

    combined = pd.concat(all_data, ignore_index=True)

    # Write results
    combined.to_csv("data/energy_deposition.csv", index=False)
    combined.groupby("Material")[["Dose_Gray", "DamageIndex"]].mean().to_csv("data/dose_response.csv")
    combined.sample(2000).to_csv("data/fluence_map.csv", index=False)
    print("✅ Synthetic irradiation data generated successfully.")

if __name__ == "__main__":
    generate_data()

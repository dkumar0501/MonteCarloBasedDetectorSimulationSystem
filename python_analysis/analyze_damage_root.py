"""
Robust analysis script that auto-detects file paths
and generates synthetic data if missing.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import sys

# --- Step 1: Auto-detect directories ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))          # /python_analysis
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))   # /Radiation-Sensor-Simulation
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "energy_deposition.csv")

# --- Step 2: If file doesn't exist, generate it automatically ---
if not os.path.exists(DATA_PATH):
    print("⚠️ Data file not found. Generating synthetic data...")
    simulation_script = os.path.join(PROJECT_ROOT, "simulation_core", "main_simulation.py")
    if not os.path.exists(simulation_script):
        print("❌ Simulation script not found at:", simulation_script)
        sys.exit(1)
    # Run the simulation to generate data
    subprocess.run([sys.executable, simulation_script], check=True)

# --- Step 3: Read the generated data ---
df = pd.read_csv(DATA_PATH)
print("✅ Data loaded successfully:", DATA_PATH)

# --- Step 4: Compute summary statistics ---
summary = df.groupby("Material")[["DepositedEnergy_MeV", "Dose_Gray", "DamageIndex"]].mean()
print("\n📊 Average Energy, Dose, and Damage per Material:")
print(summary)

# --- Step 5: Plot histogram of energy deposition ---
plt.figure(figsize=(8,5))
for material in df["Material"].unique():
    subset = df[df["Material"] == material]
    plt.hist(subset["DepositedEnergy_MeV"], bins=60, alpha=0.6, label=material)

plt.xlabel("Energy Deposition (MeV)")
plt.ylabel("Counts")
plt.title("Energy Deposition Spectrum by Material")
plt.legend()
plt.tight_layout()

OUTPUT_PLOT = os.path.join(PROJECT_ROOT, "data", "energy_distribution.png")
plt.savefig(OUTPUT_PLOT, dpi=200)
print(f"📈 Plot saved to: {OUTPUT_PLOT}")

plt.show()

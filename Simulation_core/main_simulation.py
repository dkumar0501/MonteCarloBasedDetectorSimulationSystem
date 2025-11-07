"""
Main orchestrator for the simulation.
Calls synthetic data generator and simulates a Geant4-style workflow.
"""

import os
from generate_synthetic_data import generate_data

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    print("🚀 Starting Monte Carlo-style synthetic simulation...")
    generate_data()
    print("✅ Simulation complete. Data saved in /data/")

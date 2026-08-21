<h1 align="left">Monte Carlo Based Detector Simulation System</h1>
 
<p align="left">  
  <strong>Detector Physics • Python • Monte Carlo Simulation • Radiation Modeling • Geant4</strong> 
</p>             
            
<!-- Badges -->      
<p align="left">       
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">    
  <img src="https://img.shields.io/badge/Monte%20Carlo-Simulation-orange" alt="Monte Carlo">  
  <img src="https://img.shields.io/badge/Detector%20Modeling-Enabled-success" alt="Detector Modeling">  
  <img src="https://img.shields.io/badge/CERN-IRRAD%20Inspired-9cf" alt="CERN IRRAD">
</p> 

 

## 📘 Overview

This project is a **Python based Monte Carlo style simulation framework** that models how radiation interacts with detector materials   (e.g., Silicon, GaN, Diamond). It computes **energy deposition, dose accumulation, and damage indices**, producing synthetic datasets and visualizations that replicate detector behavior in extreme radiation environments.  The system mirrors **radiation hardness studies at most IRRAD facility**, serving as a computational twin for sensor development and material evaluation.
 


## 🚀 Features

- Monte Carlo style simulation of particle material interactions  
- Energy deposition, dose, fluence, and damage index computation  
- Material wise comparison (Si, GaN, Diamond, Scintillating Fibre)  
- Synthetic dataset export to CSV (ROOT-ready workflow compatible)  
- Clear visualizations: dose–response curves & energy spectra



## 🧠 Technical Overview

| Component | Description |
|------------|-------------| 
| **Programming Language** | Python (NumPy, Pandas, Matplotlib, SciPy) |
| **Simulation Core** | Randomized particle–material energy transfer model |
| **Physics Modeling** | Dose and displacement-damage estimation by material |
| **Data Output** | CSV files: `energy_deposition.csv`, `fluence_map.csv`, `dose_response.csv` |
| **Visualization** | Histograms, dose–response plots, and material comparisons |



## 📷 Project Live Working


https://github.com/user-attachments/assets/7bec9282-503c-47e1-86de-2cf2ac4ba63a


## 🧩 Future Enhancements

- Integration with **Geant4** / **FLUKA** for high fidelity radiation transport  
- Validation against **experimental IRRAD datasets**  
- Inclusion of **temperature** and **dose rate** effects  
- Optional **ROOT/PyROOT** analysis notebooks



## 👨‍💻 Author

**Developed by [D Kumar](https://github.com/dkumar0501)** **[IIT Patna]**

---

<p align="center">
  <em>“Simulating sensor–radiation interactions to accelerate novel detector R&amp;D.”</em>
</p>

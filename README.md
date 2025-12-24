# Reaction Dynamics: The Jigsaw Course

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Open Dashboard](https://img.shields.io/badge/Launch-Interactive_Dashboard-blue?style=for-the-badge&logo=githubpages)](https://mcbadlon31.github.io/CHM172-Reaction-Dynamics/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/00_Setup_and_Introduction.ipynb)

**A professional, interactive curriculum for advanced physical chemistry.**

This repository contains the complete course materials for a "Jigsaw" style learning module on **Chemical Reaction Dynamics**. Students are divided into 5 specialist groups, each investigating a unique chemical system using a shared suite of computational tools.

---

## 🚀 Quick Start

**[Click here to open the Interactive Dashboard](https://mcbadlon31.github.io/CHM172-Reaction-Dynamics/)**

Access all student guides, notebooks, and simulations from the central project hub.

---

## 🧩 The 5 Student Groups

The core of this course is differentiated instruction. Every student learns the same API, but applies it to a drastically different physical regime.

| Group | Name | System | Focus |
| :--- | :--- | :--- | :--- |
| **1** | **The Baseline** | F + H₂ | Exothermic, Fast, Chemical Lasers |
| **2** | **Heavy Metal** | F + D₂ | Kinetic Isotope Effects (KIE), ZPE |
| **3** | **Endothermic** | Cl + H₂ | Late Barriers, Vibrational Efficacy |
| **4** | **High-T** | O + N₂ | Combustion, Hypersonic Re-entry |
| **5** | **Solution** | I + I | Viscosity, Diffusion Control, Caging |

---

## 💻 Courseware Structure

### 1. Interactive Notebooks (Colab Ready)
*   **[01 Collision Theory](notebooks/01_Collision_Theory.ipynb)**: Hard spheres vs real molecules.
*   **[02 Diffusion Controlled](notebooks/02_Diffusion_Controlled.ipynb)**: Random walks and viscosity.
*   **[03 Transition State](notebooks/03_Transition_State_Theory.ipynb)**: PES visualization and Eyring equation.
*   **[04 Molecular Dynamics](notebooks/04_Molecular_Dynamics.ipynb)**: Trajectory simulations (Polanyi's Rules).
*   **[06 Capstone Projects](notebooks/06_Integration_Projects.ipynb)**: Reactor Design, Laser Simulation, Atmospheric Models.

### 2. Instructor Resources
*   **Presentation**: 178-slide LaTeX/Beamer deck with embedded QR codes.
*   **Master Keys**: Located in `instructor_resources/` (Hidden/Ignored by git).

---

## 🛠️ Local Installation

If you prefer to run locally instead of Google Colab:

```bash
# Clone the repo
git clone https://github.com/mcbadlon31/CHM172-Reaction-Dynamics.git
cd CHM172-Reaction-Dynamics

# Install requirements
pip install -r requirements.txt

# Run Jupyter
jupyter lab
```

## ❓ Frequently Asked Questions

### General Questions

**Q: Do I need to know Python to use these notebooks?**  
A: Basic Python familiarity is helpful but not required. The notebooks are designed to be self-contained with clear instructions. Focus on understanding the chemistry - the code will handle the calculations.

**Q: Can I run these notebooks on my own computer?**  
A: Yes! Follow the local installation instructions above. However, Google Colab is recommended for the best experience (no setup required).

**Q: How long does each notebook take?**  
A: Plan for 1.5-2 hours per notebook. The capstone project (Notebook 06) may take 3-4 hours.

**Q: I'm in Group X - do I only do certain notebooks?**  
A: No! All groups complete all Core Notebooks (01-05). Your group determines which **system parameters** you use and which **capstone project** you complete in Notebook 06.

### Technical Questions

**Q: The Colab setup cell fails with "repository already exists"**  
A: This is normal if you rerun the cell. The setup is smart enough to skip cloning if it already exists.

**Q: I get "ModuleNotFoundError" errors**  
A: Make sure you ran the setup cell at the top of each notebook. If using local Jupyter, verify the `modules/` directory is in your Python path.

**Q: My plots look different from the examples**  
A: Check that you're using the correct parameters for your group. Minor visual differences are OK - focus on the physical interpretation.

**Q: Can I modify the code?**  
A: Absolutely! Experimentation is encouraged. Just keep a backup copy in case you need to revert.

---

## 🐛 Troubleshooting

### Installation Issues

**Problem**: `pip install -r requirements.txt` fails  
**Solution**:
```bash
# Try installing packages individually
pip install numpy matplotlib scipy ipywidgets plotly seaborn
```

**Problem**: Jupyter Lab won't start  
**Solution**:
```bash
# Reinstall Jupyter
pip install --upgrade jupyterlab
# Or use classic Jupyter
jupyter notebook
```

### Runtime Issues

**Problem**: Notebook kernel keeps crashing  
**Solution**:
- Restart the kernel: Kernel → Restart
- Clear outputs: Cell → All Output → Clear
- If using Colab, try Runtime → Factory Reset Runtime

**Problem**: Widgets don't display  
**Solution**:
```python
# Enable widget extension (local Jupyter only)
jupyter nbextension enable --py widgetsnbextension
```

**Problem**: Animations don't play  
**Solution**:
- Ensure you have `ffmpeg` installed (for saving animations)
- In Colab, animations should work automatically
- Try refreshing the page

### Getting Help

1. **Check Student Guides**: Your group-specific guide has detailed troubleshooting
2. **GitHub Discussions**: [Ask questions here](https://github.com/mcbadlon31/CHM172-Reaction-Dynamics/discussions)
3. **Issues**: [Report bugs](https://github.com/mcbadlon31/CHM172-Reaction-Dynamics/issues)
4. **Office Hours**: Contact your TA

---

## 📄 License
Content is licensed under **CC BY-NC-SA 4.0**. You are free to adapt this for your own classroom with attribution.

### Citation
If you use these materials in your research or teaching, please cite:
```
McBadlon, et al. (2024). CHM172 Reaction Dynamics: An Interactive Computational Curriculum.
GitHub. https://github.com/mcbadlon31/CHM172-Reaction-Dynamics
```

---

*Developed for CHM172 at UC Berkeley (Fictional/Template).*

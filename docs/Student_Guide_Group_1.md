# Student Project Guide - Group 1
## The Baseline Team: Exothermic Dynamics

**System**: $\text{F} \cdot + \text{H}_2 \rightarrow \text{HF} + \text{H} \cdot$

---

## 📋 Table of Contents
- [Your Mission](#-your-mission)
- [Critical Parameters](#-critical-parameters)
- [Notebook Walkthroughs](#-notebook-walkthroughs)
  - [NB01: Collision Theory](#-notebook-01-collision-theory)
  - [NB02: Diffusion Controlled](#-notebook-02-diffusion-controlled-reactions)
  - [NB03: Transition State Theory](#-notebook-03-transition-state-theory)
  - [NB04: Molecular Dynamics](#-notebook-04-molecular-dynamics)
  - [NB05: Electron Transfer](#-notebook-05-electron-transfer)
  - [NB06: Capstone Project](#-notebook-06-capstone-project)
- [Troubleshooting](#-troubleshooting)
- [Final Report Checklist](#-final-report)

**Estimated Time**: 6-8 hours total across all notebooks

---

### 🧪 Your Mission
You are the **Baseline Team**. Your system, the reaction of fluorine atoms with hydrogen gas, is the "gold standard" of reaction dynamics. It is highly exothermic, fast, and famously powered the first chemical lasers. Your data will serve as the reference point against which all other groups (Isotope, Endothermic, etc.) will be compared.

### 💡 Chemical Laser Background

The F + H₂ reaction was used in the first **chemical lasers** because:

1. **Population Inversion**: The reaction preferentially populates high vibrational states of HF (v=2,3)
2. **Fast Pumping**: The exothermic reaction continuously "pumps" excited HF molecules
3. **Clean Emission**: HF emits at 2.7-3.0 μm (infrared)

```
F + H₂ → HF(v=3) + H     (most probable)
       → HF(v=2) + H     (less probable)
       → HF(v=1) + H     (least probable)
```

> **Key Insight**: The "early barrier" means reactant kinetic energy is converted to product vibration!

### 🔑 Critical Parameters
Keep these numbers handy. You will need to input them into the notebooks.

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| Activation Energy (E_a) | 5.0 | kJ/mol | Very low - fast reaction |
| Cross-section (σ) | 0.30 | nm² | Physical size |
| ΔH (reaction) | -133 | kJ/mol | Highly exothermic |
| Barrier Type | Early | — | In entrance channel |
| K_sato | 0.15 | — | For LEPS surface |

---

## 📘 Notebook Walkthroughs

## 📘 Notebook 01: Collision Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

### Your Mission
Understand why F + H₂ is one of the fastest atom-diatom reactions known.

### Step-by-Step
1.  **Setup Cell**: Run the Colab setup cell at the top
2.  **Section 2 (Maxwell-Boltzmann)**:
    *   Explore the speed distribution at T = 300 K
    *   Note: H₂ molecules are FAST (mean speed ~1800 m/s)
3.  **Section 3 (Collision Frequency)**:
    *   Input cross-section σ = 0.30 nm²
    *   Set masses for F (19 g/mol) and H₂ (2.016 g/mol)
4.  **Section 4 (Arrhenius)**:
    *   Input your **E_a = 5.0 kJ/mol**
    *   **Observation**: With low E_a, the reactive fraction is high (>10%)
    *   **Prediction**: Your reaction is FAST
5.  **Section 5 (Harpoon Mechanism)**:
    *   Read this section. F + H₂ does NOT follow the harpoon mechanism
    *   Your cross-section is just the physical size (0.30 nm²)

> **✅ Expected Outcome**: You should calculate k ≈ 10¹¹ M⁻¹s⁻¹, near the collision limit. This confirms F+H₂ is extremely fast.

---

## 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

### Your Mission
Compare your fast gas-phase reaction to what would happen if you put it in a beaker of water.

### Step-by-Step
1.  **Section 2 (Stokes-Einstein)**:
    *   Set **T = 300 K**.
    *   Set Viscosity **$\eta \approx 0.89$ cP** (Water).
    *   Set **Radius = 0.15 nm**.
    *   **Record**: The Diffusion Coefficient $D$.
2.  **Section 3 (Smoluchowski Limit)**:
    *   Calculate the maximum diffusion-limited rate $k_{diff}$.
    *   **Comparison**: Compare this $k_{diff}$ ($\sim 10^{10}$ M⁻¹s⁻¹) with your Arrhenius rate from NB01.
    *   **Hypothesis**: Since your reaction is very fast ($E_a$ is low), it might actually be *slowed down* by the solvent (Collision rate drops from $10^{12}$ to $10^{10}$).

> **✅ Expected Outcome**: $k_{diff} \approx 7 \times 10^{9}$ M⁻¹s⁻¹ in water. This is ~100× slower than gas phase - the solvent is a bottleneck!

---

## 📘 Notebook 03: Transition State Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

### Your Mission
Visualize the "landscape" (Potential Energy Surface) of your reaction.

### Step-by-Step
1.  **Investigation 1 (Eyring Equation)**:
    *   Input your parameters ($T=300, E_a=5.0$).
2.  **Investigation 4 (LEPS Surface)**:
    *   Find the code cell that defines the surface.
    *   Ensure it is set for **F + H2**:
        ```python
        surface = LEPSSurface('H2', 'F', 'HF', K_sato=0.15)
        ```
    *   **Run the Plot**: Look at the contour plot.
    *   **Analysis**:
        *   Locate the "Saddle Point" (Transition State).
        *   Is it in the **Entrance Channel** (Reactants close, Products far)? This is an **EARLY BARRIER**.
        *   **Record**: Verify the barrier height is $\sim 5$ kJ/mol.

> **✅ Expected Outcome**: The saddle point should appear close to the reactant valley (lower-left of contour plot). This "early barrier" is why translational energy promotes reaction.

---

## 📘 Notebook 04: Molecular Dynamics
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

### Your Mission
Watch the atoms move! Confirm the "Stripping Mechanism" and Polanyi's Rules.

### Step-by-Step
1.  **Exercise 1.1 (Scattering)**:
    *   Plot the scattering data.
    *   Look for **Reaction A** (F+H₂).
    *   **Observe**: Use the polar plot. Is the intensity peaked at 0° (Forward)?
    *   **Conclusion**: This confirms the **Stripping Mechanism**. The F atom grabs an H atom as it flies by, barely changing direction.
2.  **Exercise 2.1 (Polanyi's Rules)**:
    *   You found an **EARLY BARRIER** in NB03.
    *   **Rule**: For early barriers, **Translational Energy** is more effective than Vibrational Energy.
    *   **Simulation**: Run the trajectory code with high velocity ($v$) vs high vibration. Confirm that velocity helps you cross the barrier.
3.  **Laser Implication**: Since the PES is attractive (Early Barrier), the energy released goes into **Product Vibration** (HF*). This is why F+H₂ works as a chemical laser!

---

## 📘 Notebook 05: Electron Transfer
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

### Your Mission
Explore the Marcus Inverted Region (General Class Activity).

### Step-by-Step
1.  **Exercise 3.1**:
    *   Use the "Marcus Parabola Explorer".
    *   Set Reorganization Energy $\lambda = 1.0$ eV.
    *   Vary $\Delta G^\circ$ from 0 to -2.0 eV.
    *   **Find the Peak**: Find the exact $\Delta G^\circ$ where the activation energy barrier disappears (Rate is max).
    *   **Verify**: Does this happen when $-\Delta G^\circ = \lambda$?

---

## 🏆 Notebook 06: Capstone Project
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

### Your Mission
**Design a Chemical Reactor for HF Production.**

1.  **Select Templates**: Choose **Template 4: Chemical Reactor Design** and **Template 8: HF Chemical Laser**.
2.  **Scenario**: You are designing a continuous reactor to produce HF (industrial chemical and laser fuel).
3.  **Tasks**:
    *   Input your rate constants $k$ calculated in NB01/NB03.
    *   Simulate a **PFR** (Plug Flow Reactor) vs **CSTR**.
    *   **Optimization**:
        *   Since the reaction is Exothermic ($E_a=5$), heat is released.
        *   If T increases too much, does the rate increase dangerously? (Runaway reaction risk?)
        *   Recommend an optimal residence time $\tau$ to get 90% yield.

---

## 🔧 Troubleshooting

### Common Issues and Solutions

**Problem**: "ModuleNotFoundError: No module named 'leps_surface'"
- **Solution**: Make sure you ran the Colab setup cell at the top of the notebook. The modules directory needs to be in your path.
- **Check**: Run `import sys; print(sys.path)` and verify that the modules directory is listed.

**Problem**: "My LEPS surface plot looks different from the example"
- **Solution**: Check that you're using `K_sato=0.15` as specified. Different values create different surfaces.
- **Expected**: You should see a saddle point (transition state) in the entrance channel for F+H₂.

**Problem**: "The trajectory simulation runs forever / crashes"
- **Solution**: High initial velocities can cause numerical instability. Keep collision energy < 100 kJ/mol.
- **Tip**: If a trajectory doesn't finish in 500 fs, it's likely non-reactive. That's OK!

**Problem**: "I don't understand what 'Early Barrier' means"
- **Solution**: Look at the LEPS contour plot. The saddle point (highest energy along the reaction path) should be close to the reactant valley, not the product valley.
- **Visual Aid**: Imagine climbing a mountain pass - an "early" barrier means the steep climb happens right at the start of your journey.

**Problem**: "My calculated k doesn't match the experimental value"
- **Solution**: That's expected! Collision theory is approximate. Differences of 2-10× are normal due to the steric factor (P).
- **What to report**: Calculate P = k_experimental / k_theory and discuss whether it's < 1 (steric hindrance) or > 1 (harpoon mechanism).

### Getting Help
- Check the [Course Discussion Forum](https://github.com/mcbadlon31/CHM172-Reaction-Dynamics/discussions)
- Review the main [README](../README.md) for installation help
- Contact your TA during office hours

---

## 📝 Final Report

Combine your findings into the Executive Summary. Focus on how the **Early Barrier** and **Exothermicity** define the unique behavior of the F+H₂ system compared to others.

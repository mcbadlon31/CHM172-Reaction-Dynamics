# 🟢 Group 1: The Baseline Team (Fluorine + Hydrogen)

## 🔬 System Identity
*   **Reaction**: **F + H₂ → HF + H**
*   **Context**: This is the "classic" reaction dynamics case study. It is highly exothermic, fast, and famously used in HF chemical lasers. Your data will serve as the "Standard Model" for the class.

## 🧪 Your Parameters
**Use these EXACT values for all calculations in the notebooks.**

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (F)** | 19.0 | amu | Fluorine atom |
| **Mass B (H₂)** | 2.016 | amu | Hydrogen molecule |
| **Radius A** | 0.15 | nm | Estimated Van der Waals radius |
| **Radius B** | 0.15 | nm | Estimated Van der Waals radius |
| **Collision Cross-section (σ)** | 0.30 | nm² | Derived from radii ($\pi (r_A+r_B)^2$) |
| **Activation Energy (Eₐ)** | 5.0 | kJ/mol | Low barrier (Exothermic) |
| **Temperature (T)** | 300 | K | Room temperature |

---

## 📘 Notebook 00: Setup & Introduction
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/00_Setup_and_Introduction.ipynb)

1.  **Launch**: Click the badge above.
2.  **Save**: Go to `File > Save a copy in Drive`. This is YOUR logbook.
3.  **Setup**: Run the "GOOGLE COLAB SETUP" cell. Wait for `[SUCCESS] Colab setup complete!`.
4.  **Practice**: Run the Python Basics cells to ensure you can execute code.

---

## 📘 Notebook 01: Collision Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

### Your Mission
Determine the "theoretical maximum" rate of your reaction if it were purely a simple collision process.

### Step-by-Step
1.  **Setup**: Run setup cells.
2.  **Section 1 (Collision Frequency)**:
    *   Find the calculator cell (usually labeled "Interact" or "Calculate").
    *   Input **Mass A = 19.0**, **Mass B = 2.016**.
    *   Input **Radius A = 0.15**, **Radius B = 0.15**.
    *   Set **T = 300 K**.
    *   **Record**: What is $Z_{AB}$ (Collision Frequency)? It should be huge ($\sim 10^{10}$ or more).
3.  **Section 2 (Maxwell-Boltzmann)**:
    *   Input **Temperature = 300 K**.
    *   Observe the "Sensitive Tail": A small fraction of molecules have high energy.
4.  **Section 3 (Arrhenius)**:
    *   Input your **Eₐ = 5.0 kJ/mol**.
    *   **Observation**: Since 5.0 kJ/mol is small (approx $2 \times RT$ at 300K), your "Reactive Fraction" should be quite high (maybe >10%).
    *   **Prediction**: Your reaction is FAST.
5.  **Section 4 (Harpoon Mechanism)**:
    *   Read this section. F + H₂ DOES NOT follow the harpoon mechanism (unlike K + Br₂), so your cross-section is just the physical size (0.30 nm²).

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

1.  **Select Template**: Choose **Template 4: Chemical Reactor Design**.
2.  **Scenario**: You are designing a continuous reactor to produce HF (industrial chemical and laser fuel).
3.  **Tasks**:
    *   Input your rate constants $k$ calculated in NB01/NB03.
    *   Simulate a **PFR** (Plug Flow Reactor) vs **CSTR**.
    *   **Optimization**:
        *   Since the reaction is Exothermic ($E_a=5$), heat is released.
        *   If T increases too much, does the rate increase dangerously? (Runaway reaction risk?)
        *   Recommend an optimal residence time $\tau$ to get 90% yield.

### Final Report
Combine your findings into the Executive Summary. Focus on how the **Early Barrier** and **Exothermicity** define the unique behavior of the F+H₂ system compared to others.

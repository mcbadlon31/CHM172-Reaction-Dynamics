# 🔴 Group 3: The Endothermic Team (Chlorine + Hydrogen)

## 🔬 System Identity
*   **Reaction**: **Cl + H₂ → HCl + H**
*   **Context**: This reaction is the opposite of the "easy" ones. It is **Endothermic** (uphill in energy). It doesn't want to happen. You have to force it with heat.

## 🧪 Your Parameters
**Use these EXACT values for all calculations in the notebooks.**

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (Cl)** | 35.45 | amu | Chlorine atom |
| **Mass B (H₂)** | 2.016 | amu | Hydrogen molecule |
| **Radius A** | 0.18 | nm | Larger than Fluorine |
| **Radius B** | 0.15 | nm | Standard H₂ |
| **Collision Cross-section (σ)** | 0.35 | nm² | Larger target |
| **Activation Energy (Eₐ)** | 23.0 | kJ/mol | **Endothermic** Barrier! |
| **Temperature (T)** | 600 | K | Needs heat to run |

---

## 📘 Notebook 00: Setup & Introduction
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/00_Setup_and_Introduction.ipynb)

1.  **Launch**: Click the badge above.
2.  **Save**: `File > Save a copy in Drive`.
3.  **Setup**: Run the "GOOGLE COLAB SETUP" cell.
4.  **Practice**: Run the Python Basics cells.

---

## 📘 Notebook 01: Collision Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

### Your Mission
Find the temperature required to make this reaction go.

### Step-by-Step
1.  **Section 1 (Collision Frequency)**:
    *   Input your Masses and Radii.
    *   Set **T = 300 K**. Record $Z_{coll}$.
2.  **Section 2 (Maxwell-Boltzmann)**:
    *   Input **Eₐ = 23.0 kJ/mol**.
    *   **Observation**: At 300K, what is the "Reactive Fraction"? It should be tiny!
    *   **Task**: Increase the Temperature slider. At what T does the fraction cross 1%? (Answer is likely > 500K).
    *   **Conclusion**: This is why we assigned you **600 K** as your standard temperature. At room temperature, this reaction is dead.
3.  **Section 3 (Arrhenius)**:
    *   Use the Arrhenius Plot widget. Notice how steep the slope is compared to $E_a=5$. High barrier means high sensitivity to Temperature.

---

## 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

### Your Mission
Confirm that diffusion is NOT your problem.

### Step-by-Step
1.  **Section 3 (Smoluchowski Limit)**:
    *   Calculate $k_{diff} \approx 10^{10}$ M⁻¹s⁻¹.
    *   Calculate your Arrhenius rate $k_{chem}$ using $E_a=23$ at 300K. It will be very small ($10^6$ or less).
    *   **Comparison**: $k_{chem} \ll k_{diff}$.
    *   **Conclusion**: Your reaction is strictly **Activation Controlled**. The solvent doesn't matter because the chemistry is the bottleneck.

---

## 📘 Notebook 03: Transition State Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

### Your Mission
Visualize the **Late Barrier**.

### Step-by-Step
1.  **Investigation 4 (LEPS Surface)**:
    *   **Code Update**: In the LEPS cell, change the system definition:
        ```python
        # CHANGE THIS LINE in the code:
        surface = LEPSSurface('H2', 'Cl', 'HCl', K_sato=0.15)
        # Note: 'H2' is AB, 'Cl' is C.
        ```
    *   **Run Plot**: Look at the Saddle Point.
    *   **Observation**:
        *   Reactant Valley (Bottom) is low.
        *   Product Valley (Left) is *higher* in energy (Endothermic).
        *   The Saddle Point is shifted into the "Product Valley" (Exit channel). This is a **LATE BARRIER**.
    *   **Polanyi's Prediction**: For late barriers, **Vibrational Energy** is required to cross it.

---

## 📘 Notebook 04: Molecular Dynamics
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

### Your Mission
Observe the "Rebound" Mechanism.

### Step-by-Step
1.  **Exercise 1.1 (Scattering)**:
    *   Look for **Reaction C** (Cl + HBr → HCl + Br... similar kinematics to yours).
    *   **Observe**: Peaked at 180° (Backward Scattering).
    *   **Mechanism**: The Cl atom hits the H, and they bounce back the way they came (Rebound). It's a "hard" collision.
2.  **Exercise 2.1 (Polanyi's Rules)**:
    *   **Test**: Compare the effect of Velocity vs Vibration.
    *   **Expectation**: Since you have a **Late Barrier**, speeding up the Cl atom (Velocity) just makes it bounce off the wall. Exciting the H₂ bond (Vibration) helps it stretch and break when Cl arrives.
    *   **Conclusion**: To make this reaction go, you want **Hot H₂** (Vibrational excitation), not just fast Cl.

---

## 📘 Notebook 05: Electron Transfer
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

1.  **Exercise 3.1**: Same task as everyone else. Find the peak of the Marcus parabola. Note that for your endothermic chemical reaction, you are effectively on the "Normal" side of the curve, "uphill".

---

## 🏆 Notebook 06: Capstone Project
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

### Your Mission
**Reactor Design for an Endothermic Process.**

1.  **Select Template**: Choose **Template 4: Chemical Reactor Design**.
2.  **Scenario**: You are designing a reactor to make HCl.
3.  **Challenge**:
    *   The reaction *consumes* heat ($\Delta H > 0$).
    *   As the reaction proceeds, the temperature drops.
    *   If T drops, the rate ($k$) crashes because $E_a$ is high (23 kJ/mol).
4.  **Task**:
    *   Modify the code to model "Adiabatic Cooling". (Or simply explain it in text).
    *   Compare PFR vs CSTR.
    *   **Recommendation**: A CSTR might be better because you can easily jacket it with a heater to maintain T=600K. A PFR might get cold at the end!

### Final Report
Focus on the difficulty of **Endothermic** reactions. You need high T (NB01), you need vibrational energy (NB04), and you need to supply heat in the reactor (NB06).

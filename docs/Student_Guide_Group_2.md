# 🔵 Group 2: The Heavy Metal Team (Isotope Effect)

## 🔬 System Identity
*   **Reaction**: **F + D₂ → DF + D**
*   **Context**: You are investigating the **Kinetic Isotope Effect (KIE)**. By replacing Hydrogen (H) with its heavier isotope Deuterium (D), you can probe the quantum mechanical nature of chemical bonds.

## 🧪 Your Parameters
**Use these EXACT values for all calculations in the notebooks.**

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (F)** | 19.0 | amu | Fluorine atom |
| **Mass B (D₂)** | 4.028 | amu | Deuterium molecule (**2x heavier than H₂!**) |
| **Radius A** | 0.15 | nm | Same as Group 1 |
| **Radius B** | 0.15 | nm | Electronic size is identical to H₂ |
| **Collision Cross-section (σ)** | 0.30 | nm² | Identical to Group 1 |
| **Activation Energy (Eₐ)** | 6.8 | kJ/mol | **Higher** than H₂ (due to ZPE) |
| **Temperature (T)** | 300 | K | Room temperature |

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
Determine how **Mass** affects collision frequency.

### Step-by-Step
1.  **Section 1 (Collision Frequency)**:
    *   Find the calculator cell.
    *   Input **Mass A = 19.0**, **Mass B = 4.028**.
    *   **Compare**: Ask a friend in Group 1 for their $Z_{AB}$.
    *   **Analysis**: Since $v_{avg} \propto \sqrt{1/m}$, your molecules move slower. Is your collision frequency lower than Group 1?
2.  **Section 3 (Arrhenius)**:
    *   Input your **Eₐ = 6.8 kJ/mol**.
    *   **Observation**: Compare the "Reactive Fraction" to Group 1 ($E_a=5.0$).
    *   **Math**: Calculate $e^{-6800/RT} / e^{-5000/RT}$. This is the "Arrhenius Factor" difference.
    *   **Conclusion**: Does the reaction slow down more because of Mass (collisions) or Energy (barrier)?

---

## 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

### Your Mission
Check if mass affects diffusion.

### Step-by-Step
1.  **Section 2 (Stokes-Einstein)**:
    *   Use the calculator. Change the "Radius".
    *   **Wait!** The equation is $D = k_B T / 6 \pi \eta R$. Does **Mass** appear in this equation?
    *   **Answer**: No! In the simple Stokes-Einstein model, D₂ diffuses at the same rate as H₂ because they have the same *size* (Radius).
    *   **Nuance**: In reality, mass has a small effect, but for this course, we assume diffusion is size-dependent only.
2.  **Section 3**: Calculate $k_{diff}$. It should be the same as Group 1.

---

## 📘 Notebook 03: Transition State Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

### Your Mission
Calculate the **Kinetic Isotope Effect (KIE)**. This is the most important module for your group.

### Step-by-Step
1.  **Investigation 1 (Eyring Equation)**:
    *   **Step A**: Calculate $k$ for the H₂ reaction (Mass=2, $E_a=5.0$).
    *   **Step B**: Calculate $k$ for the D₂ reaction (Mass=4, $E_a=6.8$).
    *   **Step C**: Calculate the ratio $k_H / k_D$.
    *   **Analysis**:
        *   Primary KIE is usually around 2-7.
        *   Why is $E_a$ higher for D₂? **Zero Point Energy**. D₂ has a lower ZPE than H₂, so it sits deeper in the well. It needs effectively more energy to reach the transition state.
2.  **Investigation 4 (LEPS Surface)**:
    *   Visualize the surface. It will look identical to Group 1's surface because the *electronic* potential doesn't change with isotopes. Only the nuclear *motion* on that surface changes.

---

## 📘 Notebook 04: Molecular Dynamics
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

### Your Mission
Observe trajectory differences due to mass.

### Step-by-Step
1.  **Exercise 1.1 (Scattering)**:
    *   Look for F + D₂ data (Reaction B).
    *   It should still show **Forward Scattering** (Stripping), but maybe slightly broader than H₂.
2.  **Exercise 2.1 (Polanyi)**:
    *   Run the trajectory simulation.
    *   **Inputs**: Use Mass B = 4.0 (approx).
    *   **Compare**: Does the heavier D₂ molecule move slower?
    *   **Momentum**: Momentum $p = mv$. For the same energy, D₂ has more momentum ($\sqrt{2mE}$). Does this help it punch through the barrier?

---

## 📘 Notebook 05: Electron Transfer
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

1.  **Exercise 3.1**: Find the "Inverted Region" peak, same as Group 1.
2.  **Think**: Since electrons have tiny mass, does replacing H with D affect *Electron* Transfer? (Usually no, unless the H/D motion is coupled to the transfer).

---

## 🏆 Notebook 06: Capstone Project
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

### Your Mission
**visualize the ZPE Origin of the Isotope Effect.**

1.  **Select Template**: Choose **Template 6: Build Your Own Reaction**.
2.  **Tasks**:
    *   We want to create a 1D slice of the potential.
    *   Use the `PESConstructor`. Add a single "well" (representing the Reactant bond).
    *   **Draw Lines**: Manually draw horizontal lines to represent the ZPE levels.
        *   $E_{ZPE} = \frac{1}{2} h \nu = \frac{1}{2} \hbar \sqrt{k/\mu}$.
        *   Since $\mu_D \approx 2\mu_H$, the ZPE of D₂ is lower by factor $1/\sqrt{2}$.
    *   **Show**: Draw the arrow to the Transition State. Show physically that the D₂ arrow is longer (requires more activation energy).

### Final Report
Your Executive Summary should focus on the **KIE**. Explain that the reaction is slower not just because D₂ moves slower (collisions), but primarily because it is thermodynamically more stable (lower ZPE), creating a higher effective barrier.

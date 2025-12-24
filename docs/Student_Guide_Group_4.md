# 🟣 Group 4: The High-T Engineers (Combustion)

## 🔬 System Identity
*   **Reaction**: **O + N₂ → NO + N**
*   **Context**: This is the rate-limiting step of the "Zeldovich Mechanism". It is responsible for creating NO (Nitric Oxide) pollution in jet engines, lightning strikes, and spacecraft re-entry.
*   **Challenge**: The nitrogen triple bond (N≡N) is one of the strongest in nature. Breaking it requires immense energy.

## 🧪 Your Parameters
**Use these EXACT values for all calculations in the notebooks.**

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (O)** | 16.00 | amu | Oxygen atom |
| **Mass B (N₂)** | 28.01 | amu | Nitrogen molecule |
| **Radius A** | 0.14 | nm | Oxygen |
| **Radius B** | 0.18 | nm | Nitrogen |
| **Collision Cross-section (σ)** | 0.32 | nm² | Average size |
| **Activation Energy (Eₐ)** | 315.0 | kJ/mol | **MASSIVE BARRIER** |
| **Temperature (T)** | 2000-5000 | K | Only runs at extreme heat |

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
Prove why NO is only formed in hot engines.

### Step-by-Step
1.  **Section 1 (Collision Frequency)**:
    *   Set **T = 2000 K**.
    *   **Note**: Density drops at high T ($PV=nRT \to n/V = P/RT$).
    *   **Task**: Assume pressure is **1 atm**. Calculate $Z_{coll}$.
    *   **Task 2**: Assume pressure is **30 atm** (Jet Engine). How much does $Z_{coll}$ increase? (It should be linear with P).
2.  **Section 2 (Maxwell-Boltzmann)**:
    *   Input **Eₐ = 315 kJ/mol**.
    *   Set **T = 300 K** (Room Temp). Reactive Fraction = 0.
    *   Set **T = 2000 K** (Combustion). Even here, the fraction is small!
    *   Set **T = 5000 K** (Lightning). Now you see a tail.
    *   **Conclusion**: This reaction *only* happens in the hottest parts of the flame or arc.

---

## 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

### Your Mission
Understanding flow.

### Step-by-Step
1.  **Context**: In a jet engine, gases are moving at 1000 m/s. Diffusion is irrelevant compared to convection (flow).
2.  **Task**: Skip the solvent calculations.
3.  **Section 4 (Material Balance)**:
    *   Read about the "Continuous Stirred Tank Reactor" (CSTR).
    *   **Thought Experiment**: If the residence time in the engine is 1 millisecond ($10^{-3}$ s), and your reaction rate $k$ is slow (due to high $E_a$), will any NO form?
    *   **Answer**: Yes, but only a tiny amount. This "tiny amount" is still enough to violate EPA pollution standards!

---

## 📘 Notebook 03: Transition State Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

### Your Mission
Calculate the rate at 2000K.

### Step-by-Step
1.  **Investigation 1 (Eyring)**:
    *   Calculate $k_{TST}$ at 2000K with $E_a = 315$ kJ/mol.
    *   Compare this to Group 1's rate at 300K. Yours is vastly slower, despite the high T.
2.  **Investigation 4 (PES)**:
    *   Use the generic 'H2 + H' surface but imagine the barrier is 315 kJ/mol.
    *   The barrier is so high it looks like a wall.

---

## 📘 Notebook 04: Molecular Dynamics
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

### Your Mission
Overcoming the Wall.

### Step-by-Step
1.  **Exercise 2.1 (Polanyi)**:
    *   You have an **Endothermic** reaction (breaking N≡N costs energy), so likely a **Late Barrier**.
    *   **Simulation**: Try to get a reaction with low velocity. (Impossible).
    *   **Simulation**: Try with high Vibrational Energy.
    *   **Real World**: In a plasma (lightning), N₂ is vibrationally excited. This makes the reaction $O + N_2^* \to NO + N$ proceed much faster than thermal equilibrium predicts. This is "Good Polanyi Physics".

---

## 📘 Notebook 05: Electron Transfer
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

1.  **Exercise 3.1**: Find the "Inverted Region" peak.
2.  **Connection**: Electron transfer reactions (like in lightning) are often the "trigger" that creates the initial O atoms and N₂* states for your neutral reaction to proceed.

---

## 🏆 Notebook 06: Capstone Project
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

### Your Mission
**Atmospheric Pollution Model.**

1.  **Select Template**: Choose **Template 1: Atmospheric Chemistry**.
2.  **Context**: The template is set up for Ozone (Chapman Cycle).
3.  **Task**:
    *   Add your reaction: `O + N2 -> NO + N` (k1).
    *   Add the second Zeldovich step: `N + O2 -> NO + O` (k2).
    *   **Goal**: Simulate the "Thermal NO" production.
    *   **Run**: Start with high T (2000K). Watch NO concentration rise.
    *   **Cool Down**: Simulate the gas exiting the engine (T drops to 300K). Does NO go back to N₂+O₂?
    *   **Result**: No! The reaction "freezes out". The reverse reaction has a high barrier too. The NO is trapped. This is why engines pollute.

### Final Report
Focus on the concept of **Kinetic Trapping**. The high barrier makes NO hard to form, but also hard to destroy once the gas cools down.

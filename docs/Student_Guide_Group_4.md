# Student Project Guide - Group 4
## The High-T Engineers: Combustion & Space

**System**: $\text{O}(^3\text{P}) + \text{N}_2 \rightarrow \text{NO} + \text{N}$

### 🧪 Your Mission
You are the **High-T Engineers**. Your reaction is the rate-limiting step of the Zeldovich mechanism, responsible for producing thermal NOx in car engines and during spacecraft re-entry. It has a massive activation barrier. At room temperature, it effectively *never* happens. You operate at the extremes of physical chemistry: 2000K to 5000K.

### 🔑 Critical Parameters
Keep these numbers handy.

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (O)** | 16.00 | g/mol | Oxygen atom |
| **Mass B (N₂)** | 28.01 | g/mol | Nitrogen molecule (Triple bond!) |
| **Diameter A** | 0.15 | nm | Standard |
| **Diameter B** | 0.36 | nm | N₂ is slightly bulky |
| **Activation Energy ($E_a$)** | 315 | kJ/mol | **EXTREME**. Breaking N≡N is hard. |
| **Enthalpy ($\Delta H$)** | +180 | kJ/mol | Highly Endothermic |
| **Temp Range** | 2000 - 5000 | K | Hypersonic/Combustion regime |

---

## 📘 Notebook Walkthroughs

### 📘 Notebook 01: Collision Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

**Goal**: The "Zero Rate" Paradox.

1.  **Exercise 1.1**:
    *   Set **T = 300 K**.
    *   Calculate $Z_{AB}$ (Collsion Freq). It's huge ($10^9$).
2.  **Exercise 2.2**:
    *   Input your **$E_a = 315$ kJ/mol**.
    *   **Result**: The reactive fraction is essentially `0.0`.
    *   **Action**: Move the Temperature slider. How hot do you have to get before the fraction reaches even 0.001% ($10^{-5}$)?
    *   **Answer**: You probably need T > 2000 K.
3.  **Insight**: This is good! If this reaction happened at 300K, our atmosphere (O2 + N2) would slowly turn into nitric acid oceans. The high barrier protects life on Earth.

### 📘 Notebook 03: Transition State Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

**Goal**: The "Brick Wall" Barrier.

1.  **Investigation 4**:
    *   Visualize the LEPS surface.
    *   Imagine a mountain range where the pass (Saddle Point) is almost as high as the peaks.
    *   **Analysis**: This is a classic "Late Barrier" (like Group 3, but more extreme). The N-N bond must practically break before the N-O bond forms.

### 📘 Notebook 04: Molecular Dynamics
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

**Goal**: Battering Ram Kinetics.

1.  **Trajectory Simulation**:
    *   Set **Energy = 320 kJ/mol** (Just above barrier).
    *   **Vibration vs Translation**: Since N₂ has a triple bond, it is a very "stiff spring" (high frequency).
    *   **Task**: Run a trajectory where you put energy into N₂ vibration. Does it help snap the bond?
    *   Compare with just throwing the O atom at it really fast (Transformation).
    *   **Hypothesis**: At 4000K (Re-entry), both modes are excited.

### 📘 Notebook 06: Capstone Project
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

**Goal**: Hypersonic Vehicle Shield Design.

1.  **Select Template**: **Template 1: Atmospheric Chemistry** or **Template 4: Chemical Reactor Design**.
2.  **Scenario**: You are designing the heat shield logic for a Mars probe.
3.  **The Zeldovich Problem**:
    *   During re-entry, the shockwave heats air to 10,000 K.
    *   Reaction: O + N₂ → NO + N.
    *   This consumes energy (Endothermic) which actually *cools* the shock layer (Good for the ship!).
    *   **Simulation**: Calculate the rate of heat absorption at T = 5000 K.
    *   **Deliverable**: Plot Rate vs T from 1000K to 6000K. Identify the "Ignition Temperature" where NO production explodes.

---

### 📝 Final Report Checklist
1.  **The Safety Barrier**: Explain why N₂ and O₂ coexist safely at room temp using your calculation from NB01.
2.  **The Switch**: At what temperature does the reaction become significant?
3.  **Mechanism**: Does the O atom attack the N₂ "end-on" or "side-on"? (Hint: TST geometry).

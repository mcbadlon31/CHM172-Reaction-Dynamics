# 🟠 Group 5: The Solution Phase Team (Viscous Dynamics)

## 🔬 System Identity
*   **Reaction**: **I + I → I₂ (in Solvent)**
*   **Context**: You are the "Odd Ones Out". Groups 1-4 are studying gas-phase collisions where atoms fly freely. You are studying atoms swimming through "treacle" (solvent). Your reaction has NO barrier. If the atoms meet, they react. The only problem is... getting them to meet.

## 🧪 Your Parameters
**Use these EXACT values for all calculations in the notebooks.**

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (I)** | 126.9 | amu | Iodine atom (Heavy!) |
| **Mass B (I)** | 126.9 | amu | Iodine atom |
| **Radius A** | 0.22 | nm | Large atom |
| **Radius B** | 0.22 | nm | Large atom |
| **Collision Cross-section** | 0.60 | nm² | Large target |
| **Activation Energy (Eₐ)** | 0.5 | kJ/mol | **Effectively Zero** |
| **Viscosity (η)** | **Variable** | cP | Your main variable! |

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
Establish the "Gas Phase Limit".

### Step-by-Step
1.  **Section 1 (Collision Frequency)**:
    *   Calculate $Z_{coll}$ for Iodine gas at 300K.
    *   **Result**: It's huge ($\sim 10^{11}$).
2.  **Section 3 (Arrhenius)**:
    *   Input **Eₐ = 0.5 kJ/mol**.
    *   **Result**: The Reactive Fraction is nearly 100%. Carbon (or Iodine) radicals *always* react if they touch.
    *   **Concept**: This establishes your **Maximum Possible Rate**. The solvent can only slow you down from here.

---

## 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

### Your Mission
**THIS IS YOUR MAIN NOTEBOOK.** Prove the Stokes-Einstein relation.

### Step-by-Step
1.  **Section 2 (Stokes-Einstein)**:
    *   **Task 1**: Calculate Diffusion Coefficient $D$ for Iodine in:
        *   **Hexane** ($\eta = 0.3$ cP).
        *   **Water** ($\eta = 0.89$ cP).
        *   **Glycerol** ($\eta = 1000$ cP).
    *   **Record**: Note how $D$ drops by 4 orders of magnitude!
2.  **Section 3 (Smoluchowski Limit)**:
    *   Calculate $k_{diff} = 4 \pi (R_A+R_B) (D_A+D_B)$.
    *   **Comparison**: The experimental rate constant in Hexane is $7 \times 10^9$ M⁻¹s⁻¹. Does your calculation match? (Use proper units!).
    *   **Graph**: Create a plot of $k_{obs}$ vs $1/\eta$.
        *   If it is a straight line through zero, you have proven Diffusion Control ($k \propto D \propto 1/\eta$).

---

## 📘 Notebook 03: Transition State Theory
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

### Your Mission
Understand "Viscosity Activation".

### Step-by-Step
1.  **Concept**: Usually $k$ increases with T because more molecules gain $E_a$.
2.  **Your Case**: Your $E_a \approx 0$. But your rate *still* increases with T. Why?
    *   **Reason**: Because Viscosity ($\eta$) decreases as T increases! (Hot oil is thinner than cold oil).
3.  **Task**:
    *   Look at the "Eyring Plot".
    *   For diffusion reactions, the slope of $\ln(k)$ vs $1/T$ gives the **Activation Energy of Viscous Flow**, not the bond breaking energy.

---

## 📘 Notebook 04: Molecular Dynamics
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

### Your Mission
Visualize the Cage Effect.

### Step-by-Step
1.  **Section 4.1 (Cage Effect)**:
    *   Watch the animation of the particle in the box of solvent.
    *   **Observe**: The Iodine atom bounces back and forth many times before escaping the "solvent cage".
    *   **Recombination**: If another Iodine atom was in the same cage, they would hit each other 100 times in a picosecond. Reaction is guaranteed (Geminate Recombination).
    *   **Separation**: If they are in *different* cages, they might wander for seconds before finding each other. This is diffusion control.

---

## 📘 Notebook 05: Electron Transfer
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

1.  **Exercise 3.1**: Find the "Inverted Region" peak.
2.  **Solvent Role**: Note that "Reorganization Energy" $\lambda$ comes mainly from the **Solvent** rearranging around the charge. For Group 5, the solvent is everything!

---

## 🏆 Notebook 06: Capstone Project
**Link**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

### Your Mission
**Enzyme Kinetics in Viscous Media.**

1.  **Select Template**: Choose **Template 2: Enzyme Kinetics**.
2.  **Context**: Enzymes are big proteins. Substrates must diffuse to them.
3.  **Task**:
    *   The code simulates Michaelis-Menten Kinetics: $E + S \rightleftharpoons ES \to E + P$.
    *   The formation step ($k_1$) is **Diffusion Controlled**.
    *   **Modify**: Introduce a `viscosity` parameter. Make $k_1 = k_{base} / \eta$.
    *   **Predict**: As you increase viscosity (like in a crowded cell cytoplasm), does the reaction rate saturate?
    *   **Scenario**: What happens if the cytoplasm "freezes" (Glass transition)?

### Final Report
Focus on the **Power of the Medium**. Chemical reactivity isn't just about the intrinsic nature of the reactants (Group 1-4 view), but about the environment they swim in.

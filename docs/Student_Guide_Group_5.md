# Student Project Guide - Group 5
## The Solution Phase Team: Viscous Dynamics

**System**: $\text{I} \cdot + \text{I} \cdot \rightarrow \text{I}_2$ (in Solvent)

---

## 📋 Table of Contents
- [Your Mission](#-your-mission)
- [Critical Parameters](#-critical-parameters)
- [Notebook Walkthroughs](#-notebook-walkthroughs)
- [Troubleshooting](#-troubleshooting)
- [Final Report Checklist](#-final-report-checklist)

**Estimated Time**: 6-8 hours | **Unique Challenge**: Diffusion-limited kinetics

---

### 🧪 Your Mission
You are the **Solution Team**. While everyone else is flying around in the gas phase, you are dealing with the real world of wet chemistry. Your reaction (Iodine recombination) is barrierless ($E_a \approx 0$). In the gas phase, it would occur at every collision. But in solution, the solvent molecules cage you in. You are **Diffusion Controlled**.

### 🔑 Critical Parameters
Keep these numbers handy.

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (I)** | 126.9 | g/mol | Heavy! |
| **Mass B (I)** | 126.9 | g/mol | Symmetric reaction |
| **Radius A (I)** | 0.22 | nm | Large atom |
| **Solvent** | CCl₄ / Hexane | - | The "Third Body" |
| **Viscosity ($\eta$)** | 0.9 | cP | Standard solvent viscosity |
| **Activation Energy ($E_a$)** | ~0 | kJ/mol | Barrierless |
| **Enthalpy ($\Delta H$)** | -151 | kJ/mol | Bond formation |

---

## 📘 Notebook Walkthroughs

### 📘 Notebook 01: Collision Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

**Goal**: The Gas Phase Baseline.

1.  **Exercise 1.1**:
    *   Calculate $Z_{AA}$ for Iodine gas at 300K.
    *   **Result**: It will be huge ($10^{11}$).
    *   **Question**: Since $E_a \approx 0$, the gas phase rate should be $10^{11}$. But wait! If two iodine atoms hit, they form a vibrationally hot $I_2^*$ molecule that immediately flies apart unless a **third body** ($M$) takes away the energy.
    *   **Conclusion**: Simple bimolecular collision theory FAILS for gas-phase recombination. You need 3-body collision theory.

### 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

**Goal**: **YOUR MAIN NOTEBOOK**.

1.  **Investigation 1 (Random Walk)**:
    *   This is your visual. Watch the particle "jitter".
    *   **Task**: Run the simulation with "Steps = 1000".
    *   Calculate the RMS displacement.
2.  **Investigation 2 (Stokes-Einstein)**:
    *   **Formula**: $k_{diff} = \frac{8RT}{3\eta}$ (Smoluchowski-Stokes-Einstein).
    *   **Observe**: The variable is **Viscosity ($\eta$)**, NOT temperature (mostly), and NOT mass!
    *   **Task**:
        *   Calculate $k_{diff}$ for Hexane ($\eta = 0.3$ cP).
        *   Calculate $k_{diff}$ for CCl$_4$ ($\eta = 0.9$ cP).
        *   Calculate $k_{diff}$ for Glycerol ($\eta = 900$ cP).
    *   **Record**: Plot Rate $k$ vs Viscosity $\eta$. It should be linear ($1/\eta$).

> **✅ Expected Outcome**: Your plot should show k_diff inversely proportional to η. In glycerol, reaction is ~1000× slower than hexane!

### 📘 Notebook 04: Molecular Dynamics
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

**Goal**: The Cage Effect.

1.  **Scenario**: The notebook simulates gas phase. Imagine it filled with inert balls.
2.  **Thought Experiment**:
    *   In gas phase, if I-I separate, they are gone forever.
    *   In solution, if I-I separate, they hit a solvent wall and might bounce back!
    *   This is **Geminate Recombination**.
    *   **Result**: This actually *helps* recombination (unlike diffusion which slows the approach).

### 📘 Notebook 05: Electron Transfer
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/05_Electron_Transfer.ipynb)

**Goal**: Solvent Reorganization.

1.  **Relevance**: While you aren't doing electron transfer, the **Solvent Reorganization Energy ($\lambda$)** discussed here is analogous to the "viscous drag" you study.
2.  **Task**: Read the section on how solvents rearrange around a charge. This is similar to how solvents must move out of the way for I and I to meet.

### 📘 Notebook 06: Capstone Project
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

**Goal**: Solvent Optimization.

1.  **Select Template**: **Template 7: Solvent Cage Effect**.
2.  **Scenario**: Industrial synthesis of $I_2$.
3.  **Optimization**:
    *   You need to check if the reaction is **faster** in a low-viscosity solvent (Hexane) or high-viscosity (Medical Oil).
    *   **Trade-off**: Low viscosity = Fast diffusion (Good). High viscosity = High cage effect (Good for keeping them together once met).
    *   Which effect wins? (Hint: Usually Diffusion wins).

---

## 🔧 Troubleshooting

**Problem**: "The Stokes-Einstein equation doesn't have mass in it - is that right?"
- **Yes!** In the overdamped limit (high viscosity), friction dominates inertia.
- **Analogy**: Swimming in honey - your mass doesn't matter much, only your size and the honey's thickness.
- **Key Insight**: This is why solution-phase rates differ from gas-phase even for identical reactions.

**Problem**: "My k_diff calculation gives ~10¹⁰ M⁻¹s⁻¹ but that seems too fast"
- **It's correct!** Diffusion-limited rates are the speed limit for solution reactions.
- **Context**: Enzyme-substrate binding often reaches this limit (called 'perfect' enzymes).

**Problem**: "Does the cage effect speed up or slow down the reaction?"
- **Complex!** It prevents immediate separation (good for recombination) but slows initial approach (bad).
- **Net effect**: For barrierless recombination like I + I → I₂, cage helps because it prevents geminate separation.
- **Compare**: Gas phase I + I needs a third body (M) to remove energy. Solvent acts as that third body!

**Problem**: "I can't find viscosity data for my chosen solvent"
- **Resources**: CRC Handbook, NIST Chemistry WebBook
- **Typical values**: Water (1.0 cP), Hexane (0.3 cP), Ethanol (1.2 cP), Glycerol (1000 cP)

**Problem**: "What's the difference between η (eta) and μ (mu)?"
- **η**: Dynamic viscosity (Pa·s or cP), resistance to flow
- **μ**: Reduced mass (kg), used in collision theory
- **Don't confuse them!** They're unfortunately both Greek letters but totally different quantities.

---

### 📝 Final Report Checklist
1.  **The Viscosity Plot**: Show your plot of $k$ vs $\eta$.
2.  **Gas vs Liquid**: Compare your $k_{diff}$ to the Group 1 gas phase rate. Is solution chemistry slower? (Usually yes, by 10-100x).
3.  **The Third Body**: Explain why the solvent acts as the "Third Body" to remove excess energy.

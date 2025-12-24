# Student Project Guide - Group 3
## The Endothermic Team: Uphill Dynamics

**System**: $\text{Cl} \cdot + \text{H}_2 \rightarrow \text{HCl} + \text{H} \cdot$

---

## 📋 Table of Contents
- [Your Mission](#-your-mission)
- [Critical Parameters](#-critical-parameters)
- [Notebook Walkthroughs](#-notebook-walkthroughs)
- [Troubleshooting](#-troubleshooting)
- [Final Report Checklist](#-final-report-checklist)

**Estimated Time**: 6-8 hours | **Challenge Level**: High (thermally demanding system)

---

### 🧪 Your Mission
You are the **Endothermic Team**. Unlike the easy, downhill reactions of Group 1, your reaction is **uphill**. It consumes heat ($\Delta H > 0$). This makes your reaction slow and sensitive. You must study the "Late Barrier" effect, a concept crucial for understanding enzyme catalysis and difficult chemical syntheses.

### 🔑 Critical Parameters
Keep these numbers handy.

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (Cl)** | 35.45 | g/mol | Chlorine atom |
| **Mass B (H₂)** | 2.016 | g/mol | Hydrogen molecule |
| **Diameter A (Cl)** | 0.35 | nm | Much larger than F |
| **Diameter B (H₂)** | 0.29 | nm | Kinetic diameter |
| **Activation Energy ($E_a$)** | 23.0 | kJ/mol | High barrier (Very Slow at RT) |
| **Enthalpy ($\Delta H$)** | +5.0 | kJ/mol | **Endothermic** (Uphill) |
| **Temp Range** | 400 - 800 | K | Requires heating to run |

---

## 📘 Notebook Walkthroughs

### 📘 Notebook 01: Collision Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

**Goal**: Why is it so slow?

1.  **Exercise 1.1 (Collision Freq)**:
    *   Set **T = 300 K**.
    *   Set **Mass** and **Sigmas** for Cl + H₂.
    *   **Record**: $Z_{AB}$ is likely similar to Group 1.
2.  **Exercise 2.2 (Reactive Fraction)**:
    *   **Crucial Step**: Input your $E_a = 23$ kJ/mol.
    *   **Observe**: At 300K, the fraction $\exp(-E_a/RT)$ is tiny! ($e^{-9.2} \approx 0.0001$).
    *   **Action**: Increase T to 800 K. How much does the rate increase? This demonstrates why endothermic reactions **require heat**.

> **✅ Expected Outcome**: At 300K, fraction ≈ 0.01%. At 800K, fraction ≈ 5%. Rate increases ~500× with temperature doubling!

### 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

**Goal**: Viscosity check.

1.  **Hypothesis**: Since your reaction is chemically slow (high $E_a$), diffusion is likely **not** the rate-limiting step. Even in a thick solvent, the reagents will collide many times before reaction occurs.
2.  **Simulation**: Run the random walk. Confirm that $k_{diff} \gg k_{chem}$.

### 📘 Notebook 03: Transition State Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

**Goal**: The Late Barrier.

1.  **Investigation 4 (LEPS Surface)**:
    *   Find the LEPS code.
    *   The notebook defaults to HI (which is related to your Cl system).
    *   **Visual Analysis**: Look at the Saddle Point.
    *   **The Difference**: Unlike Group 1 (Early), your Saddle Point is in the **Exit Channel**.
    *   This means the bond is already stretched, and the H-Cl bond is forming *before* you reach the top of the hill.
    *   This is a **Late Barrier**.

### 📘 Notebook 04: Molecular Dynamics
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

**Goal**: Polanyi's Rules for Endothermic Reactions.

1.  **Exercise 2.1 (Polanyi Rules)**:
    *   This is the most important simulation for your group.
    *   **Scenario A**: High Translational Kinetic Energy (Fast collision).
    *   **Scenario B**: High Vibrational Energy (H₂ is vibrating wildly).
    *   **Prediction**: Polanyi's Rules state that for a **Late Barrier**, **VIBRATION** is more effective than translation.
    *   **Task**: Run both scenarios. Count the reactions using the `reac_count` variable. Confirm if vibrating H₂ reacts more often than fast H₂.

### 📘 Notebook 06: Capstone Project
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

**Goal**: Reactor Heating Design.

1.  **Select Template**: **Template 4: Chemical Reactor Design**.
2.  **Scenario**: You are designing a reactor to make HCl.
3.  **Optimization**:
    *   You have a cost function: Heating is expensive ($), but your reaction needs T > 600K.
    *   Find the "Sweet Spot": The temperature where the reaction is fast enough to make reasonable profit, but not so hot that fuel costs zero out your revenue.
    *   **Safety**: Unlike Group 1, you don't have a runaway risk (reaction consumes heat). Your risk is the fire going out!

---

## 🔧 Troubleshooting

**Problem**: "My reaction rate at 300K is basically zero"
- **Expected!** With E_a = 23 kJ/mol, exp(-23000/(8.314×300)) ≈ 0.0001
- **Solution**: Increase temperature to 600-800 K to see meaningful rates.
- **Real World**: This is why Cl + H₂ reactions only occur in flames or photochemical conditions.

**Problem**: "The reactor optimization shows I lose money at all temperatures"
- **Check**: Are you including the product value correctly? HCl is valuable.
- **Economic Reality**: Endothermic reactions often need energy subsidies. Consider solar or waste heat integration.

**Problem**: "I don't see why vibration helps more than translation for late barriers"
- **Visual Aid**: Draw energy along reaction coordinate. For late barriers, the bond is already stretched at the TS.
- **Analogy**: It's like trying to break a stick - it's easier if it's already flexing (vibrating) than if you just hit it fast.

**Problem**: "My PES shows an early barrier, not late"
- **Check System**: Make sure you're using Cl + H₂ parameters, not F + H₂.
- **K_sato value**: Try K_sato = 0.0-0.1 for this system (different from Group 1).

---

### 📝 Final Report Checklist
1.  **Polanyi confirmation**: Did vibration help more than translation? Show the data.
2.  **Barrier Position**: Sketch the PES along the reaction coordinate. Mark "Late Barrier".
3.  **Temperature**: What is the minimum T required to get 1% yield?

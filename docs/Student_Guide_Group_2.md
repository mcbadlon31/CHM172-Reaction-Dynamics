# Student Project Guide - Group 2
## The Heavy Metal Team: Isotope Effects

**System**: $\text{F} \cdot + \text{D}_2 \rightarrow \text{DF} + \text{D} \cdot$

### 🧪 Your Mission
You are the **Isotope Team**. Your system is chemically identical to Group 1 (Fluorine + Hydrogen), but physically heavier. You are using **Deuterium** ($^2\text{H}$ or $\text{D}$), the heavy isotope of hydrogen. Your goal is to measure the **Kinetic Isotope Effect (KIE)**—the change in reaction rate caused purely by mass differences.

### 🔑 Critical Parameters
Keep these numbers handy.

| Parameter | Value | Unit | Notes |
| :--- | :--- | :--- | :--- |
| **Mass A (F)** | 19.00 | g/mol | Fluorine atom |
| **Mass B (D₂)** | 4.028 | g/mol | Deuterium molecule (2x heavier!) |
| **Diameter A (F)** | 0.14 | nm | Same as H (Electronic structure identical) |
| **Diameter B (D₂)** | 0.29 | nm | Same as H₂ |
| **Activation Energy ($E_a$)** | 5.2 | kJ/mol | Slightly higher than H₂ (ZPE effect) |
| **Enthalpy ($\Delta H$)** | -135 | kJ/mol | Similar to H₂ |
| **Temp Range** | 200 - 400 | K | Standard operating range |

---

## 📘 Notebook Walkthroughs

### 📘 Notebook 01: Collision Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/01_Collision_Theory.ipynb)

**Goal**: How does mass affect collision frequency?

1.  **Setup**: Run Google Colab Setup.
2.  **Exercise 1.1 (Collision Calculator)**:
    *   Set **T = 300 K**.
    *   Set **Mass B = 4.03** (D₂).
    *   **Observe**: The Mean Speed ($v_{mean}$) will be **lower** than for H₁.
    *   **Record**: Calculate the ratio $\frac{v_{H2}}{v_{D2}}$. Is it $\sqrt{2} \approx 1.41$?
3.  **Exercise 1.2**:
    *   Calculate your Collision Frequency $Z_{F,D2}$.
    *   It should be lower than Group 1's $Z_{F,H2}$ by a factor of $\sqrt{2}$.

### 📘 Notebook 02: Diffusion Controlled Reactions
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/02_Diffusion_Controlled.ipynb)

**Goal**: Does mass matter in solution?

1.  **Section 2 (Stokes-Einstein)**:
    *   The formula is $D = \frac{k_B T}{6\pi \eta r}$.
    *   **Critical Thinking**: Does mass ($m$) appear in this equation?
    *   **Answer**: No! In the overdamped (viscous) limit, diffusion depends on *size* ($r$), not *mass*.
    *   **Prediction**: Your diffusion rate in solution should be **identical** to Group 1, unlike in the gas phase.

### 📘 Notebook 03: Transition State Theory
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/03_Transition_State_Theory.ipynb)

**Goal**: The core of your project - The KIE.

1.  **Investigation 2 (KIE Analysis)**:
    *   The notebook uses Prodrug data, but the concept is the same.
    *   **Task**: Read the section on **Zero Point Energy (ZPE)** carefully.
    *   **Calculation**: In your report, calculate the theoretical KIE for your system:
        $$ \frac{k_H}{k_D} \approx \exp\left( \frac{\Delta E_{ZPE}}{RT} \right) $$
    *   Given that $E_a(D_2)$ is $\sim 0.4$ kJ/mol higher than $E_a(H_2)$, compute this ratio at 300K.
2.  **Investigation 4 (LEPS Surface)**:
    *   The Potential Energy Surface (electronic energy) is **identical** for F+H₂ and F+D₂. (Electrons don't care about nuclear mass).
    *   However, the **dynamics** on that surface change.

### 📘 Notebook 04: Molecular Dynamics
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/04_Molecular_Dynamics.ipynb)

**Goal**: Visualize the "Sluggish" trajectory.

1.  **Exercise 1.1**:
    *   Run a trajectory with F+H₂ (Group 1 params).
    *   Run a trajectory with F+D₂ (Change mass parameter).
    *   **Observe**: The D atoms move slower. The F-D vibration frequency is lower.
2.  **Tunneling**:
    *   Does your system show tunneling?
    *   Usually, H tunnels, but D is too heavy. This "Tunneling" difference creates massive isotope effects ($k_H/k_D > 100$).
    *   Since your temp is high (300K), tunneling is minor. You are observing a **Primary KIE** due to ZPE.

### 📘 Notebook 06: Capstone Project
**Link**: [Open Notebook](https://colab.research.google.com/github/mcbadlon31/CHM172-Reaction-Dynamics/blob/main/notebooks/06_Integration_Projects.ipynb)

**Goal**: Isotope Separation.

1.  **Select Template**: **Template 8: PES Constructor**.
2.  **Scenario**: You are enriching Deuterium for a fusion reactor.
3.  **Task**:
    *   Design a "Competitive Reaction" simulation where F atoms attack a mix of H₂ and D₂.
    *   Count how many HF vs DF molecules form.
    *   **Separation Factor**: $\alpha = \frac{[HF]/[H_2]}{[DF]/[D_2]}$.
    *   Can you find a temperature that maximizes this separation? (Hint: Lower T typically increases selectivity).

---

### 📝 Final Report Checklist
1.  **The KIE Value**: What is your calculated $k_H / k_D$ at 300K?
2.  **Mechanism**: Does the mass difference affect the *Collision Frequency* or the *Activation Barrier* more?
3.  **Application**: Explain how this effect (KIE) is used to study reaction mechanisms in organic chemistry (as seen in NB03).

# 📝 Equation Cheat Sheet

**CHM172 Reaction Dynamics - Quick Reference**

Print this page for your exams and problem sets!

---

## 1. Collision Theory

| Quantity | Equation | Units |
|----------|----------|-------|
| Mean relative speed | $\bar{v}_{rel} = \sqrt{\frac{8k_BT}{\pi\mu}}$ | m/s |
| Reduced mass | $\mu = \frac{m_A m_B}{m_A + m_B}$ | kg |
| Collision cross-section | $\sigma = \pi d^2 = \pi\left(\frac{d_A + d_B}{2}\right)^2$ | m² |
| Collision frequency (single) | $z = \sigma \bar{v}_{rel} \mathcal{N}_B$ | s⁻¹ |
| Collision density | $Z_{AB} = \sigma \bar{v}_{rel} \mathcal{N}_A \mathcal{N}_B$ | m⁻³s⁻¹ |
| Number density | $\mathcal{N} = \frac{p}{k_BT}$ | m⁻³ |

### Arrhenius Equation
$$k = A \exp\left(-\frac{E_a}{RT}\right)$$

- **A**: Pre-exponential factor (M⁻¹s⁻¹)
- **E_a**: Activation energy (J/mol)
- **R**: Gas constant = 8.314 J/(mol·K)

---

## 2. Diffusion-Controlled Reactions

| Quantity | Equation | Units |
|----------|----------|-------|
| Diffusion coefficient | $D = \frac{k_BT}{6\pi\eta r}$ | m²/s |
| RMS displacement | $\langle x^2 \rangle = 2Dt$ (1D) | m² |
| Smoluchowski limit | $k_{diff} = 4\pi N_A (D_A + D_B) R^*$ | M⁻¹s⁻¹ |
| Simplified form | $k_{diff} \approx \frac{8RT}{3\eta}$ | M⁻¹s⁻¹ |

**Typical Values:**
- Water viscosity η ≈ 0.001 Pa·s (1 cP)
- k_diff ≈ 10¹⁰ M⁻¹s⁻¹ in water at 298K

---

## 3. Transition State Theory

### Eyring Equation
$$k = \kappa \frac{k_BT}{h} K^\ddagger = \kappa \frac{k_BT}{h} \exp\left(-\frac{\Delta G^\ddagger}{RT}\right)$$

| Symbol | Meaning |
|--------|---------|
| κ | Transmission coefficient (usually ≈ 1) |
| h | Planck's constant = 6.626×10⁻³⁴ J·s |
| K‡ | Equilibrium constant for TS formation |
| ΔG‡ | Free energy of activation |

### Connection to Arrhenius
$$E_a \approx \Delta H^\ddagger + RT$$
$$A \approx \frac{k_BT}{h} e^{\Delta S^\ddagger/R}$$

### LEPS Potential
$$V_{LEPS} = Q_{AB} + Q_{BC} + Q_{AC} - \sqrt{J_{AB}^2 + J_{BC}^2 + J_{AC}^2 - J_{AB}J_{BC} - J_{BC}J_{AC} - J_{AB}J_{AC}}$$

---

## 4. Molecular Dynamics

### Velocity Verlet Integration
$$\vec{r}(t+\Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + \frac{1}{2}\vec{a}(t)\Delta t^2$$
$$\vec{v}(t+\Delta t) = \vec{v}(t) + \frac{1}{2}[\vec{a}(t) + \vec{a}(t+\Delta t)]\Delta t$$

### Polanyi's Rules

| Barrier Type | Location | Favored Energy |
|--------------|----------|----------------|
| Early | Entrance channel | Translational |
| Late | Exit channel | Vibrational |

---

## 5. Electron Transfer (Marcus Theory)

### Marcus Rate Equation
$$k_{ET} = A \exp\left[-\frac{(\Delta G^\circ + \lambda)^2}{4\lambda k_BT}\right]$$

| Symbol | Meaning |
|--------|---------|
| ΔG° | Standard free energy of reaction |
| λ | Reorganization energy |

### Key Relationships
- **Maximum rate** when: $-\Delta G^\circ = \lambda$
- **Inverted region**: $-\Delta G^\circ > \lambda$ (rate decreases!)

### Reorganization Energy
$$\lambda = \lambda_{inner} + \lambda_{outer}$$

- λ_inner: Bond length changes
- λ_outer: Solvent reorganization

---

## Constants

| Constant | Symbol | Value |
|----------|--------|-------|
| Boltzmann | k_B | 1.381 × 10⁻²³ J/K |
| Avogadro | N_A | 6.022 × 10²³ mol⁻¹ |
| Gas constant | R | 8.314 J/(mol·K) |
| Planck | h | 6.626 × 10⁻³⁴ J·s |
| Speed of light | c | 2.998 × 10⁸ m/s |

---

## Unit Conversions

| From | To | Multiply by |
|------|----| ------------|
| kJ/mol | J/mol | 1000 |
| eV | kJ/mol | 96.485 |
| cm⁻¹ | kJ/mol | 0.01196 |
| Å | nm | 0.1 |
| Å | m | 10⁻¹⁰ |
| cP | Pa·s | 0.001 |

---

*CHM172 Reaction Dynamics | [Back to Dashboard](index.html)*

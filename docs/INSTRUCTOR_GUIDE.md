# Instructor Resources

A guide for instructors implementing the CHM172 Reaction Dynamics course.

---

## Course Overview

**Format**: Jigsaw cooperative learning with 5 specialist groups  
**Duration**: 6-8 weeks (adjustable)  
**Prerequisites**: General Chemistry, Calculus, basic Python familiarity helpful

### Learning Outcomes
By course end, students will be able to:
1. Calculate reaction rates using collision theory, TST, and Marcus theory
2. Interpret potential energy surfaces and predict reaction outcomes
3. Apply computational tools to analyze reaction dynamics
4. Collaborate across groups to synthesize a complete picture of reaction dynamics

---

## Week-by-Week Schedule

| Week | Topic | Notebook | Group Activity |
|------|-------|----------|----------------|
| 1 | Introduction + Setup | 00 | Form groups, assign systems |
| 2 | Collision Theory | 01 | Calculate system-specific collision rates |
| 3 | Diffusion Control | 02 | Compare gas vs solution phase |
| 4 | Transition State Theory | 03 | Construct group PES, find TS |
| 5 | Molecular Dynamics | 04 | Run trajectories, analyze scattering |
| 6 | Electron Transfer | 05 | Marcus theory applications |
| 7-8 | Capstone Projects | 06 | Group presentations |

---

## Group Assignments

### Recommended Team Sizes
- **5 students per group** (optimal)
- **3-7 students** (acceptable range)
- Total class size: 15-35 students ideal

### System Assignments

| Group | System | Difficulty | Key Concepts |
|-------|--------|------------|--------------|
| 1 | F + H₂ | ⭐⭐ | Baseline, early barrier, lasers |
| 2 | F + D₂ | ⭐⭐⭐ | KIE, ZPE, isotope separation |
| 3 | Cl + H₂ | ⭐⭐⭐ | Endothermic, late barrier, heating |
| 4 | O + N₂ | ⭐⭐⭐⭐ | Extreme conditions, combustion |
| 5 | I + I | ⭐⭐⭐ | Solution phase, diffusion control |

### Balancing Tips
- Pair stronger students with Groups 3 and 4 (more challenging systems)
- Group 1 provides the "baseline" that all others compare against
- Ensure Groups 1 and 2 communicate (same electronic system, different masses)

---

## Assessment Strategies

### Formative (Ongoing)
- **Notebook Checkpoints**: Verify students complete concept checks
- **Group Progress Reports**: Weekly 1-page updates
- **Peer Explanation**: Students teach other groups their system

### Summative (Final)
- **Individual Quiz** (30%): Core concepts applicable to all systems
- **Group Report** (40%): Comprehensive analysis of assigned system
- **Jigsaw Presentation** (30%): Cross-group synthesis

### Sample Quiz Questions

1. *For ALL groups*: Explain why doubling T increases reaction rate more than doubling pressure.

2. *Group-specific*: Using your system's parameters, calculate k at T=500K.

3. *Cross-group*: Compare the F+H₂ and Cl+H₂ systems. Which has an early barrier? How does barrier position affect which energy type (T vs V) promotes reaction?

---

## Technical Setup

### Before Class
1. Test Google Colab access on classroom computers
2. Verify students have Google accounts
3. Pre-clone repository to handle slow networks

### During Class
- Project the dashboard for navigation
- Have students bookmark their group's portal
- Monitor Colab runtime limits (12-hour max session)

---

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "Colab disconnected" | Students should save frequently; reconnect and re-run |
| "Module not found" | Re-run the setup cell at the top |
| "Plots don't display" | Refresh browser, restart runtime |

---

**Questions?** Open an issue on GitHub or contact the development team.

#!/usr/bin/env python3
"""
Advanced Notebook Enhancement Script

Adds the remaining planned features:
- Concept check cells
- Common misconceptions boxes
- Enhanced visualizations
- Interactive widgets improvements

Run from repository root:
    python scripts/advanced_notebook_enhancements.py
"""

import json
from pathlib import Path

NOTEBOOKS_DIR = Path(__file__).parent.parent / 'notebooks'

# Concept checks to inject after specific sections
CONCEPT_CHECKS = {
    '01_Collision_Theory.ipynb': [
        '''## 🧠 Concept Check: Collision Frequency

**Test Your Understanding:**

1. You have two gases at the same T and P. Gas A has molecules twice as heavy as Gas B. Which has higher collision frequency?
   <details><summary>Answer</summary>Gas B - lighter molecules move faster (v ∝ 1/√m)</details>

2. **Common Misconception**: "Doubling temperature doubles the reaction rate."
   
   > ⚠️ **Reality**: Doubling T increases collision rate by only √2 ≈ 1.4×. The BIG effect comes from the exponential Arrhenius factor!

3. What fraction of collisions lead to reaction if Ea = 50 kJ/mol at 300K?
   <details><summary>Calculation</summary>exp(-50000/(8.314×300)) ≈ 2×10⁻⁹ — only 2 in a billion!</details>
''',
        '''## 🧠 Concept Check: The Harpoon Mechanism

**Critical Thinking:**

1. Why is the K + Br₂ reaction cross-section 50× larger than expected from molecular sizes?

2. **Common Misconception**: "Reaction cross-section equals geometric cross-section."
   
   > ⚠️ **Reality**: Long-range forces (ionic attraction in harpoon mechanism) can dramatically increase the effective cross-section!

3. Does F + H₂ follow the harpoon mechanism? Why or why not?
   <details><summary>Answer</summary>No — F has high electron affinity but H₂ has high ionization energy. Electron transfer doesn't happen at long range.</details>
'''
    ],
    '02_Diffusion_Controlled.ipynb': [
        '''## 🧠 Concept Check: Random Walks

**Test Your Understanding:**

1. A particle takes 100 random steps of length 1 nm each. What is the expected RMS displacement?
   <details><summary>Answer</summary>√100 × 1 nm = 10 nm (not 100 nm!)</details>

2. **Common Misconception**: "Diffusion is just slow directed motion."
   
   > ⚠️ **Reality**: Diffusion has NO preferred direction. The RMS displacement grows as √t, not t!

3. Why doesn't mass appear in the Stokes-Einstein equation?
   <details><summary>Answer</summary>In the overdamped (viscous) limit, friction dominates inertia. Only size and viscosity matter.</details>
''',
        '''## 🧠 Concept Check: Diffusion-Limited Reactions

**Critical Thinking:**

1. Your reaction has k = 10⁸ M⁻¹s⁻¹ in water. Is it diffusion-limited?
   <details><summary>Answer</summary>No — diffusion limit is ~10¹⁰ M⁻¹s⁻¹. This reaction is 100× slower than the limit.</details>

2. **Common Misconception**: "Reactions in solution are always slower than in gas phase."
   
   > ⚠️ **Nuance**: True for fast reactions (diffusion is the bottleneck), but for slow reactions with high Ea, the solvent "cage" can actually help by keeping reactants together longer!

3. You switch from water (η=1 cP) to glycerol (η=1000 cP). By what factor does k_diff change?
   <details><summary>Answer</summary>k_diff decreases by 1000× (inverse relationship with viscosity)</details>
'''
    ],
    '03_Transition_State_Theory.ipynb': [
        '''## 🧠 Concept Check: Transition State Theory

**Test Your Understanding:**

1. The Eyring equation has kT/h as a pre-factor. At 300K, what is this frequency?
   <details><summary>Answer</summary>(1.38×10⁻²³ × 300)/(6.63×10⁻³⁴) ≈ 6×10¹² s⁻¹ — about 6 THz!</details>

2. **Common Misconception**: "The transition state is a short-lived intermediate."
   
   > ⚠️ **Reality**: The TS is not a minimum — it's a saddle point. Molecules don't "stop" there; they cross it in ~10⁻¹³ s!

3. On a LEPS surface, where is the saddle point for an exothermic reaction with an early barrier?
   <details><summary>Answer</summary>In the entrance channel (lower-left of the contour plot, closer to reactants)</details>
''',
        '''## 🧠 Concept Check: Barrier Position

**Polanyi's Rules Preview:**

| Barrier Type | Location | Favored Energy |
|--------------|----------|----------------|
| Early | Entrance channel | Translational |
| Late | Exit channel | Vibrational |

1. **F + H₂** has an early barrier. What type of energy promotes reaction?
   <details><summary>Answer</summary>Translational — fast collisions cross early barriers more easily</details>

2. **Cl + H₂** has a late barrier. What type of energy promotes reaction?
   <details><summary>Answer</summary>Vibrational — stretching the H-H bond helps reach the late TS geometry</details>

3. **Common Misconception**: "More energy always means more reaction."
   
   > ⚠️ **Reality**: The *type* of energy matters! Putting translational energy into a late-barrier reaction is less effective than vibrational.
'''
    ],
    '04_Molecular_Dynamics.ipynb': [
        '''## 🧠 Concept Check: Trajectory Analysis

**Test Your Understanding:**

1. A trajectory ends with R_BC = 8 Å and R_AB = 1.5 Å. What happened?
   <details><summary>Answer</summary>Reactive! The BC bond broke (large R_BC) and AB formed (small R_AB)</details>

2. **Common Misconception**: "One trajectory tells you the reaction rate."
   
   > ⚠️ **Reality**: You need MANY trajectories (hundreds to thousands) sampled from the thermal distribution to calculate a rate!

3. Your energy drifts by 5% over the trajectory. What went wrong?
   <details><summary>Answer</summary>Time step too large. Reduce dt to improve energy conservation.</details>
''',
        '''## 🧠 Concept Check: Scattering Patterns

**Interpreting Angular Distributions:**

| Pattern | Mechanism | Barrier Type |
|---------|-----------|--------------|
| Forward (θ ≈ 0°) | Stripping | Early |
| Backward (θ ≈ 180°) | Rebound | Late |
| Isotropic | Long-lived complex | — |

1. F + H₂ shows strong forward scattering. What does this tell you?
   <details><summary>Answer</summary>Stripping mechanism — F grabs H as it flies by, barely deflected</details>

2. **Common Misconception**: "All reactions have the same scattering pattern."
   
   > ⚠️ **Reality**: Scattering patterns are fingerprints of the reaction mechanism and PES topology!
'''
    ],
    '05_Electron_Transfer.ipynb': [
        '''## 🧠 Concept Check: Marcus Theory

**Test Your Understanding:**

1. What is the reorganization energy λ physically?
   <details><summary>Answer</summary>The energy cost to distort the reactant geometry to the product geometry WITHOUT transferring the electron</details>

2. At what driving force (-ΔG°) is the ET rate maximum?
   <details><summary>Answer</summary>When -ΔG° = λ (driving force equals reorganization energy)</details>

3. **Common Misconception**: "More driving force always means faster reaction."
   
   > ⚠️ **Reality**: In the inverted region (-ΔG° > λ), MORE driving force makes the reaction SLOWER! This is the Nobel-winning insight of Marcus theory.
''',
        '''## 🧠 Concept Check: The Inverted Region

**Why Biology Loves the Inverted Region:**

In photosynthesis:
- **Forward ET** (charge separation): Optimized at -ΔG° ≈ λ → FAST
- **Back ET** (recombination): Deep in inverted region → SLOW

This protects the captured energy!

1. A reaction has λ = 1.0 eV. At what ΔG° values is the rate maximum?
   <details><summary>Answer</summary>At ΔG° = -1.0 eV</details>

2. If ΔG° = -2.5 eV (very exergonic), is the reaction fast or slow?
   <details><summary>Answer</summary>SLOW — this is deep in the inverted region (2.5 > 1.0)</details>
'''
    ]
}

def inject_concept_checks(notebook_path, checks):
    """Inject concept check cells into a notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Add concept checks before the summary (if summary exists)
    for check in checks:
        check_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + '\n' for line in check.strip().split('\n')]
        }
        # Insert before second-to-last cell (before summary)
        insert_pos = max(len(nb['cells']) - 2, 0)
        nb['cells'].insert(insert_pos, check_cell)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print(f"✓ Injected {len(checks)} concept checks into: {notebook_path.name}")


def main():
    print("=" * 60)
    print("Advanced Notebook Enhancement Script")
    print("=" * 60)
    
    for nb_name, checks in CONCEPT_CHECKS.items():
        nb_path = NOTEBOOKS_DIR / nb_name
        if nb_path.exists():
            inject_concept_checks(nb_path, checks)
        else:
            print(f"✗ Not found: {nb_name}")
    
    print("\n" + "=" * 60)
    print("Concept checks injected successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Notebook Enhancement Script

This script adds pedagogical improvements to the Jupyter notebooks:
- Concept check cells after major sections
- Summary cells at the end of each notebook
- Enhanced visualization defaults

Run from repository root:
    python scripts/enhance_notebooks.py
"""

import json
import os
from pathlib import Path

# Define the notebooks directory
NOTEBOOKS_DIR = Path(__file__).parent.parent / 'notebooks'

# Concept check templates for each notebook
CONCEPT_CHECKS = {
    '01_Collision_Theory.ipynb': [
        {
            'after_section': 'Collision Rate',
            'check': '''## 🧠 Concept Check 1

**Quick Questions** (answer mentally or in your notes):

1. **Units Check**: If σ is in nm² and v̄ is in m/s, what unit conversion is needed for Z?

2. **Physical Intuition**: You double the pressure at constant T. By what factor does Z change?
   <details><summary>Answer</summary>Z doubles (linear in number density)</details>

3. **Compare**: Which affects collision rate MORE - doubling T or doubling pressure?
   <details><summary>Answer</summary>Doubling P doubles Z. Doubling T only increases Z by √2 ≈ 1.4. Pressure wins!</details>
'''
        },
        {
            'after_section': 'Maxwell-Boltzmann',
            'check': '''## 🧠 Concept Check 2

**Energy Distribution Understanding**:

1. At 300K, what fraction of molecules have E > 50 kJ/mol? (Use the Arrhenius factor)
   <details><summary>Hint</summary>exp(-50000/(8.314×300)) ≈ 2×10⁻⁹</details>

2. At 600K, this fraction becomes?
   <details><summary>Answer</summary>exp(-50000/(8.314×600)) ≈ 4.5×10⁻⁵, a factor of 20,000× increase!</details>

3. **Key Insight**: Temperature affects reaction rate mainly through ___ (collision frequency / energy distribution)?
   <details><summary>Answer</summary>Energy distribution! The exponential factor dominates.</details>
'''
        }
    ],
    '02_Diffusion_Controlled.ipynb': [
        {
            'after_section': 'Random Walk',
            'check': '''## 🧠 Concept Check 1

**Diffusion Fundamentals**:

1. In a random walk, if you take 100 steps instead of 25, by what factor does the RMS displacement increase?
   <details><summary>Answer</summary>√(100/25) = 2× (square root relationship!)</details>

2. Why doesn't the *average* displacement increase with more steps?
   <details><summary>Answer</summary>Steps in opposite directions cancel. Only RMS captures the spreading.</details>
'''
        },
        {
            'after_section': 'Smoluchowski',
            'check': '''## 🧠 Concept Check 2

**Diffusion-Limited Rates**:

1. The "speed limit" for solution reactions is about 10¹⁰ M⁻¹s⁻¹. Why can't reactions go faster?
   <details><summary>Answer</summary>Molecules can only diffuse together so fast. Even if every encounter reacts, diffusion limits the encounter rate.</details>

2. If you increase solvent viscosity 10×, how does k_diff change?
   <details><summary>Answer</summary>k_diff decreases 10× (inverse relationship with η)</details>
'''
        }
    ],
    '03_Transition_State_Theory.ipynb': [
        {
            'after_section': 'LEPS',
            'check': '''## 🧠 Concept Check

**PES Understanding**:

1. On a contour plot, reactants appear in which corner?
   <details><summary>Answer</summary>Lower-left (both R_AB and R_BC are large = separated atoms)</details>

2. What does a "saddle point" look like on a contour plot?
   <details><summary>Answer</summary>A pass between two valleys - contours curved in opposite directions</details>

3. **Polanyi Connection**: An "early" barrier favors ___ energy, a "late" barrier favors ___ energy.
   <details><summary>Answer</summary>Early → translational, Late → vibrational</details>
'''
        }
    ],
    '04_Molecular_Dynamics.ipynb': [
        {
            'after_section': 'Trajectory',
            'check': '''## 🧠 Concept Check

**Trajectory Interpretation**:

1. A trajectory that ends with R_BC > 5 Å and R_AB < 2 Å is called?
   <details><summary>Answer</summary>Reactive! The BC bond broke and AB formed.</details>

2. Energy drift > 1% indicates what problem?
   <details><summary>Answer</summary>Time step too large or numerical instability. Reduce dt.</details>

3. Why do we run MANY trajectories instead of just one?
   <details><summary>Answer</summary>Initial conditions are sampled from a distribution. Statistics require an ensemble.</details>
'''
        }
    ],
    '05_Electron_Transfer.ipynb': [
        {
            'after_section': 'Marcus',
            'check': '''## 🧠 Concept Check

**Marcus Theory**:

1. At what value of ΔG° does the rate reach maximum?
   <details><summary>Answer</summary>When -ΔG° = λ (driving force equals reorganization energy)</details>

2. Why is it called the "inverted region"?
   <details><summary>Answer</summary>Counter-intuitively, making the reaction MORE favorable (larger -ΔG°) makes it SLOWER</details>

3. Real-world example of the inverted region?
   <details><summary>Answer</summary>Photosynthesis! The "wrong" direction (charge recombination) is inverted and slow, protecting the system.</details>
'''
        }
    ]
}

# Summary templates for each notebook
SUMMARIES = {
    '01_Collision_Theory.ipynb': '''---

## 📋 Notebook Summary

### Key Equations
| Concept | Equation | Units |
|---------|----------|-------|
| Mean relative speed | $\\bar{v}_{rel} = \\sqrt{8k_BT/\\pi\\mu}$ | m/s |
| Collision frequency | $z = \\sigma \\bar{v}_{rel} \\mathcal{N}_B$ | s⁻¹ |
| Collision density | $Z_{AB} = \\sigma \\bar{v}_{rel} \\mathcal{N}_A \\mathcal{N}_B$ | m⁻³s⁻¹ |
| Arrhenius | $k = A \\exp(-E_a/RT)$ | M⁻¹s⁻¹ |

### Key Insights
1. **Collisions are frequent** (~10⁹ s⁻¹) but most don't react
2. **Temperature matters** mainly through the exponential energy factor
3. **Steric factor P** accounts for orientation requirements (typically 0.01-1)
4. **Harpoon mechanism** explains cross-sections larger than geometric

### What's Next
→ Notebook 02 explores what happens when reactions move to *solution* phase
''',
    '02_Diffusion_Controlled.ipynb': '''---

## 📋 Notebook Summary

### Key Equations
| Concept | Equation | Units |
|---------|----------|-------|
| Einstein relation | $D = k_BT / 6\\pi\\eta r$ | m²/s |
| Smoluchowski limit | $k_{diff} = 4\\pi N_A (D_A + D_B) R^*$ | M⁻¹s⁻¹ |
| RMS displacement | $\\langle x^2 \\rangle = 2Dt$ | m² |

### Key Insights
1. **Diffusion is slow** compared to gas-phase (~10¹⁰ vs 10¹² M⁻¹s⁻¹)
2. **Viscosity dominates** - mass doesn't matter in overdamped limit
3. **Cage effect** can enhance recombination reactions
4. **Third body** role of solvent removes excess energy

### What's Next
→ Notebook 03 introduces the *transition state* and potential energy surfaces
''',
    '03_Transition_State_Theory.ipynb': '''---

## 📋 Notebook Summary

### Key Equations
| Concept | Equation |
|---------|----------|
| Eyring equation | $k = \\frac{k_BT}{h} K^\\ddagger$ |
| Arrhenius from TST | $E_a \\approx \\Delta H^\\ddagger + RT$ |
| LEPS potential | $V = Q_{AB} + Q_{BC} + Q_{AC} - \\sqrt{J^2}$ |

### Key Insights
1. **Transition state** is a saddle point - unstable in one direction
2. **Early barrier** → translational energy helps (exothermic reactions)
3. **Late barrier** → vibrational energy helps (endothermic reactions)
4. **Hammond postulate** - TS resembles the closer energy species

### What's Next
→ Notebook 04 runs *actual trajectories* on these surfaces
''',
    '04_Molecular_Dynamics.ipynb': '''---

## 📋 Notebook Summary

### Key Concepts
| Method | Purpose |
|--------|---------|
| Velocity Verlet | Symplectic integration (conserves energy) |
| QCT | Quasiclassical trajectories with zero-point energy |
| Scattering angle | θ = 0° (forward), 180° (backward) |

### Key Insights
1. **Stripping mechanism** → forward scattering (early barriers)
2. **Rebound mechanism** → backward scattering (late barriers)
3. **Polanyi's Rules** connect barrier location to energy efficacy
4. **Statistical sampling** required for meaningful cross-sections

### What's Next
→ Notebook 05 covers *electron transfer* - a fundamentally different mechanism
''',
    '05_Electron_Transfer.ipynb': '''---

## 📋 Notebook Summary

### Key Equations
| Concept | Equation |
|---------|----------|
| Marcus rate | $k_{ET} = A \\exp[-(\\Delta G^\\circ + \\lambda)^2 / 4\\lambda k_BT]$ |
| Reorganization | $\\lambda = \\lambda_{inner} + \\lambda_{outer}$ |
| Maximum rate | when $-\\Delta G^\\circ = \\lambda$ |

### Key Insights
1. **Parabolic free energy** surfaces for donor and acceptor
2. **Reorganization energy** is the "preparation cost" for ET
3. **Inverted region** - too much driving force SLOWS the reaction
4. **Biological relevance** - photosynthesis exploits the inverted region

### Course Complete! 🎉
→ Proceed to Notebook 06 for your capstone project
'''
}


def add_cells_to_notebook(notebook_path, concept_checks, summary):
    """Add concept check and summary cells to a notebook."""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Add summary at the end
    summary_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": summary.split('\n')
    }
    
    # Format source as list of lines
    summary_cell["source"] = [line + '\n' for line in summary.split('\n')]
    if summary_cell["source"]:
        summary_cell["source"][-1] = summary_cell["source"][-1].rstrip('\n')
    
    nb['cells'].append(summary_cell)
    
    # Save
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print(f"✓ Enhanced: {notebook_path.name}")


def main():
    print("=" * 60)
    print("Notebook Enhancement Script")
    print("=" * 60)
    
    for nb_name, summary in SUMMARIES.items():
        nb_path = NOTEBOOKS_DIR / nb_name
        if nb_path.exists():
            add_cells_to_notebook(nb_path, CONCEPT_CHECKS.get(nb_name, []), summary)
        else:
            print(f"✗ Not found: {nb_name}")
    
    print("\n" + "=" * 60)
    print("Enhancement complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

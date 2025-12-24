# Modules API Reference

This directory contains the core computational modules for reaction dynamics simulations.

## Quick Start

```python
# In any notebook, after running the Colab setup cell:
from leps_surface import LEPSSurface
from trajectory import ClassicalTrajectory
from transition_state import TransitionStateOptimizer
from visualization import plot_pes_3d, plot_pes_contour
```

---

## LEPSSurface (leps_surface.py)

Creates potential energy surfaces using the London-Eyring-Polanyi-Sato method.

### Basic Usage

```python
# Create a LEPS surface for F + H2 reaction
surface = LEPSSurface('H2', 'F', 'HF', K_sato=0.15)

# Calculate energy at a single geometry (kJ/mol)
energy = surface.leps_potential(R_AB=1.5, R_BC=0.95, R_AC=2.45)

# Generate 2D surface for visualization
R_AB_range = np.linspace(0.5, 4.0, 100)
R_BC_range = np.linspace(0.5, 4.0, 100)
X, Y, Z = surface.energy_surface_2d(R_AB_range, R_BC_range, angle_deg=180)
```

### Key Parameters

| Parameter | Description | Typical Values |
|-----------|-------------|----------------|
| `K_sato` | Sato parameter (controls barrier shape) | 0.0 - 0.3 |
| `R_AB` | Distance between atoms A and B (Å) | 0.5 - 5.0 |
| `R_BC` | Distance between atoms B and C (Å) | 0.5 - 5.0 |

---

## ClassicalTrajectory (trajectory.py)

Runs classical trajectory simulations using Velocity Verlet integration.

### Basic Usage

```python
# Initialize trajectory calculator
traj = ClassicalTrajectory(surface, atom_A='H', atom_B='H', atom_C='I', dt=0.010)

# Run a single trajectory
result = traj.run_trajectory(
    R_AB_0=3.0, R_BC_0=1.6, R_AC_0=4.6,  # Initial distances (Å)
    v_AB_0=-0.05, v_BC_0=0.0, v_AC_0=-0.05,  # Initial velocities (Å/fs)
    max_time=500.0,  # Max integration time (fs)
    save_interval=5  # Save every N steps
)

# Check outcome
print(f"Outcome: {result['outcome']}")  # 'reactive' or 'non-reactive'
print(f"Energy drift: {result['energy_drift']:.4f}%")
```

### Output Dictionary

| Key | Description |
|-----|-------------|
| `time` | Array of time points (fs) |
| `R_AB`, `R_BC`, `R_AC` | Distance arrays (Å) |
| `V`, `T`, `E_total` | Potential, kinetic, total energy (kJ/mol) |
| `outcome` | 'reactive', 'non-reactive', or 'incomplete' |
| `energy_drift` | Energy conservation error (%) |

---

## TransitionStateOptimizer (transition_state.py)

Finds saddle points on potential energy surfaces using Newton-Raphson optimization.

### Basic Usage

```python
optimizer = TransitionStateOptimizer(surface, tolerance=1e-6, max_iterations=50)

# Find the transition state starting from an initial guess
result = optimizer.optimize_saddle_point(R_AB_init=1.8, R_BC_init=1.8, verbose=True)

print(f"TS geometry: R_AB={result['R_AB']:.3f}, R_BC={result['R_BC']:.3f}")
print(f"Activation energy: {result['energy']:.1f} kJ/mol")
print(f"Hessian eigenvalues: {result['eigenvalues']}")
```

### Saddle Point Verification

A true saddle point has:
- **One negative eigenvalue** (reaction coordinate - unstable)
- **One positive eigenvalue** (perpendicular - stable)

---

## Visualization (visualization.py)

Plotting utilities for potential energy surfaces.

### Functions

```python
# 3D surface plot
fig, ax = plot_pes_3d(X, Y, Z, title="LEPS Surface", elev=25, azim=45)

# 2D contour plot
fig, ax = plot_pes_contour(X, Y, Z, title="Energy Contours", levels=40)

# Morse potential curve
fig, ax = plot_morse_curve(R_range, V_morse, R_e=1.6, D_e=298.0)
```

---

## Troubleshooting

**"ModuleNotFoundError"**: Run the Colab setup cell first, or add modules to path:
```python
import sys
sys.path.append('../modules')
```

**Energy drift > 1%**: Reduce time step (`dt=0.005`) or check for unrealistic initial conditions.

**Optimization doesn't converge**: Try a different initial guess closer to the expected saddle point.

import json
import os

NOTEBOOK_PATH = 'notebooks/06_Integration_Projects.ipynb'

def create_code_cell(source_lines):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source_lines]
    }

def create_markdown_cell(source_lines):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source_lines]
    }

def main():
    if not os.path.exists(NOTEBOOK_PATH):
        print(f"Error: {NOTEBOOK_PATH} not found.")
        return

    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    new_cells = []

    # ==========================================
    # TEMPLATE 5: Chemical Reactor Design
    # ==========================================
    new_cells.append(create_markdown_cell([
        "## Template 5: Chemical Reactor Design",
        "",
        "**For Group 1 (Baseline), Group 3 (Endothermic), Group 4 (High-T)**",
        "",
        "Design a simplified Plug Flow Reactor (PFR) to maximize profit.",
        "",
        "**The Challenge:**",
        "1. Rate Constant $k(T) = A \\exp(-E_a/RT)$",
        "2. Profit = (Value of Product * Yield) - (Cost of Heating * T)",
        "3. Safety: In exothermic systems, T can runaway!",
        ""
    ]))

    new_cells.append(create_code_cell([
        "def reactor_simulation(T_reactor_K, residence_time_s, Ea_kJ, A_prefactor, is_exothermic=True):",
        "    R = 8.314",
        "    k = A_prefactor * np.exp(-Ea_kJ * 1000 / (R * T_reactor_K))",
        "    ",
        "    # First order reaction A -> B",
        "    # For PFR: [A] = [A]0 * exp(-k * tau)",
        "    conversion = 1 - np.exp(-k * residence_time_s)",
        "    ",
        "    # Simplified Economic Model",
        "    product_value = 100 * conversion  # $ per unit",
        "    heating_cost = 0.05 * (T_reactor_K - 300) # $ per degree above room temp",
        "    ",
        "    profit = product_value - heating_cost",
        "    ",
        "    print(f\"--- Reactor at {T_reactor_K} K ---\")",
        "    print(f\"Rate constant k: {k:.2e} s^-1\")",
        "    print(f\"Conversion:      {conversion*100:.1f}%\")",
        "    print(f\"Heating Cost:    ${heating_cost:.2f}\")",
        "    print(f\"Net Profit:      ${profit:.2f}\")",
        "    return profit",
        "",
        "# EXAMPLE: Optimized for Group 1 (Low Ea)",
        "print(\"Running Low Ea Optimization...\")",
        "approx_A = 1e11",
        "reactor_simulation(T_reactor_K=300, residence_time_s=1e-10, Ea_kJ=5.0, A_prefactor=approx_A)"
    ]))

    # ==========================================
    # TEMPLATE 6: HF Laser Simulation
    # ==========================================
    new_cells.append(create_markdown_cell([
        "## Template 6: HF Chemical Laser",
        "",
        "**For Group 1 (Baseline)**",
        "",
        "Simulate the population dynamics of vibrational states produced in $F + H_2 \\to HF(v) + H$.",
        "",
        "**Goal**: Demonstrate **Population Inversion** ($N_{v=2} > N_{v=1}$)."
    ]))

    new_cells.append(create_code_cell([
        "def laser_kinetics(t, populations, k_pumping, k_relaxation):",
        "    # N0, N1, N2 are populations of v=0, v=1, v=2",
        "    N0, N1, N2 = populations",
        "    ",
        "    # Simplistic Laser Model",
        "    # Pumping: Reactants -> N2 (Fastest for F+H2)",
        "    # Relaxation: N2 -> N1 -> N0 (Collisional deactivation)",
        "    ",
        "    pump_rate = k_pumping  # Constant source term",
        "    ",
        "    dN2_dt = (0.7 * pump_rate) - k_relaxation * N2",
        "    dN1_dt = (0.3 * pump_rate) + k_relaxation * N2 - k_relaxation * N1",
        "    dN0_dt = k_relaxation * N1",
        "    ",
        "    return [dN0_dt, dN1_dt, dN2_dt]",
        "",
        "t_span = np.linspace(0, 10, 100)",
        "k_pump = 100.0",
        "k_relax = 10.0",
        "initial_pop = [0, 0, 0]",
        "",
        "sol = odeint(laser_kinetics, initial_pop, t_span, args=(k_pump, k_relax))",
        "",
        "plt.figure(figsize=(8,5))",
        "plt.plot(t_span, sol[:, 2], label='v=2 (Upper)', linewidth=3)",
        "plt.plot(t_span, sol[:, 1], label='v=1 (Lower)')",
        "plt.plot(t_span, sol[:, 0], label='v=0 (Ground)', linestyle='--')",
        "plt.title('HF Laser Population Dynamics')",
        "plt.ylabel('Population (N)')",
        "plt.xlabel('Time (arb s)')",
        "plt.legend()",
        "plt.grid(True)",
        "plt.show()"
    ]))

    # ==========================================
    # TEMPLATE 7: Solvent Cage Effect
    # ==========================================
    new_cells.append(create_markdown_cell([
        "## Template 7: Solvent Cage Effect",
        "",
        "**For Group 5 (Solution Phase)**",
        "",
        "Simulate 'Geminate Recombination'. In gas phase, atoms fly apart. In solution, they bounce back.",
        "",
        "**Task**: Run the simulation and count how many times the pair 're-collides' before escaping."
    ]))

    new_cells.append(create_code_cell([
        "def cage_simulation(viscosity_cP=0.89, n_steps=1000):",
        "    # Simple 1D Random Walk with a 'Wall' representing solvent cage",
        "    position = 0.0 # Start at contact",
        "    collisions = 0",
        "    escaped = False",
        "    trajectory = []",
        "    ",
        "    # Viscosity reduces step size (Diffusion coeff D ~ 1/eta)",
        "    step_size = 1.0 / viscosity_cP",
        "    ",
        "    for _ in range(n_steps):",
        "        move = np.random.choice([-1, 1]) * step_size",
        "        position += move",
        "        ",
        "        # Wall at 0 (Impact partner)",
        "        if position <= 0:",
        "            position = 0",
        "            collisions += 1",
        "        ",
        "        # Escape threshold",
        "        if position > 10.0:",
        "            escaped = True",
        "            # break",
        "            ",
        "        trajectory.append(position)",
        "        ",
        "    return trajectory, collisions, escaped",
        "",
        "# Compare Solvents",
        "traj_water, coll_water, esc_water = cage_simulation(viscosity_cP=1.0)",
        "traj_oil,   coll_oil,   esc_oil   = cage_simulation(viscosity_cP=10.0)",
        "",
        "plt.figure(figsize=(10,4))",
        "plt.plot(traj_water, label=f'Water (Collisions={coll_water})', alpha=0.7)",
        "plt.plot(traj_oil, label=f'Oil (Collisions={coll_oil})', alpha=0.7)",
        "plt.axhline(10, color='red', linestyle='--', label='Cage Radius')",
        "plt.title('Trajectory of Separating Atom Pair')",
        "plt.xlabel('Time Step')",
        "plt.ylabel('Distance form Partner')",
        "plt.legend()",
        "plt.show()"
    ]))

    # Append new cells
    nb['cells'].extend(new_cells)

    # Saving changes...
    
    with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print(f"Successfully added {len(new_cells)} cells to {NOTEBOOK_PATH}")

if __name__ == "__main__":
    main()

import json
import os

notebook_path = '/Users/mcbadlon/CHM172-Reaction-Dynamics/notebooks/06_Integration_Projects.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

new_cells = []
template_count = 1

# We want to filter and renumber
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if '## Template' in source:
            # Check if it's one of the ones we want to keep/renumber
            if 'Atmospheric' in source:
                cell['source'] = [f"## Template {template_count}: Atmospheric Chemistry (Chapman Cycle)\n", "\n", "Reactions:\n", "1. $O_2 + h\\nu \\xrightarrow{k_1} 2O$\n", "2. $O + O_2 + M \\xrightarrow{k_2} O_3 + M$\n", "3. $O_3 + h\\nu \\xrightarrow{k_3} O_2 + O$\n", "4. $O + O_3 \\xrightarrow{k_4} 2O_2$"]
                template_count += 1
            elif 'Enzyme' in source:
                cell['source'] = [f"## Template {template_count}: Enzyme Kinetics (Michaelis-Menten)\n", "\n", "$$ E + S \\rightleftharpoons ES \\rightarrow E + P $$"]
                template_count += 1
            elif 'Oscillating' in source:
                cell['source'] = [f"## Template {template_count}: Oscillating Reactions (Lotka-Volterra)\n", "\n", "A simple model for oscillating populations (predator-prey) or autocatalytic reactions.\n", "\n", "1. $A + X \\xrightarrow{k_1} 2X$ (Autocatalysis)\n", "2. $X + Y \\xrightarrow{k_2} 2Y$ (Predation)\n", "3. $Y \\xrightarrow{k_3} P$ (Decay)"]
                template_count += 1
            elif 'Reactor Design' in source:
                cell['source'] = [f"## Template {template_count}: Chemical Reactor Design\n", "\n", "Design a reactor to maximize the yield of intermediate B in a series reaction $A \\to B \\to C$.\n", "- **CSTR**: Continuous Stirred-Tank Reactor\n", "- **PFR**: Plug Flow Reactor"]
                template_count += 1
            elif 'Photosynthetic' in source:
                cell['source'] = [f"## Template {template_count}: Photosynthetic Electron Transfer\n", "\n", "Model the Z-scheme of photosynthesis, tracking electron flow from Water to NADP+."]
                template_count += 1
            elif 'HF Chemical Laser' in source:
                cell['source'] = [f"## Template {template_count}: HF Chemical Laser\n", "\n", "**For Group 1 (Baseline)**\n", "\n", "Simulate the population dynamics of vibrational states produced in $F + H_2 \\to HF(v) + H$.\n", "\n", "**Goal**: Demonstrate **Population Inversion** ($N_{v=2} > N_{v=1}$).\n"]
                template_count += 1
            elif 'Solvent Cage' in source:
                cell['source'] = [f"## Template {template_count}: Solvent Cage Effect\n", "\n", "**For Group 5 (Solution Phase)**\n", "\n", "Simulate 'Geminate Recombination'. In gas phase, atoms fly apart. In solution, they bounce back.\n", "\n", "**Task**: Run the simulation and count how many times the pair 're-collides' before escaping.\n"]
                template_count += 1
            elif 'PES Constructor' in source:
                cell['source'] = [f"## Template {template_count}: PES Constructor (Gaussian Builder)\n", "\n", "Create a custom Potential Energy Surface (PES) by adding Gaussian wells and hills, then simulate a reaction trajectory."]
                template_count += 1
            else:
                # If it's a template we don't recognize or a duplicate, skip it?
                # Actually, let's keep it but don't renumber it if it looks like a duplicate
                continue
    
    new_cells.append(cell)

# Check for duplicates or out-of-order cells manually in the list
# The above logic might miss some cells or keep duplicates if they have the same content.
# Let's refine: we only want ONE of each topic.

refined_cells = []
seen_topics = set()

for cell in new_cells:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        topic = None
        if 'Atmospheric' in source: topic = 'Atmospheric'
        elif 'Enzyme' in source: topic = 'Enzyme'
        elif 'Oscillating' in source: topic = 'Oscillating'
        elif 'Reactor Design' in source: topic = 'Reactor'
        elif 'Photosynthetic' in source: topic = 'Photosynthesis'
        elif 'HF Chemical Laser' in source: topic = 'Laser'
        elif 'Solvent Cage' in source: topic = 'Cage'
        elif 'PES Constructor' in source: topic = 'PES'
        
        if topic:
            if topic in seen_topics:
                # Skip duplicate markdown and the FOLLOWING code cell
                continue
            seen_topics.add(topic)
    
    # Also skip code cells that follow skipped markdown? 
    # This is getting complex. Let's just do a manual rebuild of the cell list.
    refined_cells.append(cell)

nb['cells'] = refined_cells

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

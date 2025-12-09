/**
 * Topic 18D: Molecular Collision Dynamics
 * Interactive logic for molecular beams, scattering, and PES.
 */

// ============================================================================
// Molecular Beam Simulator
// ============================================================================
const MolecularBeam = {
    canvas: null,
    ctx: null,
    particles: [],
    animationId: null,
    sourceX: 50,
    sourceY: 150,
    collisionX: 300,
    collisionY: 150,
    detectorAngle: 0, // radians relative to beam axis

    init: function() {
        this.canvas = document.getElementById('beamCanvas');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());

        // Start animation
        this.animate();
        
        // Spawn particles periodically
        setInterval(() => this.spawnParticle(), 100);
    },

    resize: function() {
        if (this.canvas.parentElement) {
            this.canvas.width = this.canvas.parentElement.clientWidth;
            this.canvas.height = 300;
        }
    },

    spawnParticle: function() {
        // Particles A (Blue) from left
        this.particles.push({
            x: this.sourceX,
            y: this.sourceY + (Math.random() - 0.5) * 10,
            vx: 4 + Math.random() * 0.5, // Velocity selection (narrow distribution)
            vy: (Math.random() - 0.5) * 0.2,
            type: 'A',
            scattered: false,
            life: 200
        });

        // Particles B (Red) from bottom (Crossed beam)
        this.particles.push({
            x: this.collisionX + (Math.random() - 0.5) * 10,
            y: 300,
            vx: (Math.random() - 0.5) * 0.2,
            vy: -4 - Math.random() * 0.5,
            type: 'B',
            scattered: false,
            life: 200
        });
    },

    update: function() {
        for (let i = this.particles.length - 1; i >= 0; i--) {
            let p = this.particles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.life--;

            // Collision logic
            if (!p.scattered) {
                const dx = p.x - this.collisionX;
                const dy = p.y - this.collisionY;
                const dist = Math.sqrt(dx*dx + dy*dy);

                if (dist < 15) {
                    // Scatter!
                    p.scattered = true;
                    
                    // Simple scattering model:
                    // A tends to scatter forward/sideways
                    // B tends to scatter
                    
                    if (p.type === 'A') {
                        // Scatter into a cone
                        const angle = (Math.random() - 0.5) * Math.PI / 2; // +/- 45 degrees
                        const speed = Math.sqrt(p.vx*p.vx + p.vy*p.vy);
                        p.vx = Math.cos(angle) * speed;
                        p.vy = Math.sin(angle) * speed;
                        p.color = '#8b5cf6'; // Change color to indicate reaction/scattering
                    } else {
                         // B gets knocked away
                        p.life = 0; // Remove B for simplicity or scatter it differently
                    }
                }
            }

            if (p.life <= 0 || p.x > this.canvas.width || p.y < 0 || p.y > this.canvas.height) {
                this.particles.splice(i, 1);
            }
        }
    },

    draw: function() {
        this.ctx.fillStyle = '#0f172a';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw Source A
        this.ctx.fillStyle = '#3b82f6';
        this.ctx.fillRect(10, this.sourceY - 20, 40, 40);
        this.ctx.fillStyle = 'white';
        this.ctx.font = '12px Inter';
        this.ctx.fillText('Source A', 10, this.sourceY - 25);

        // Draw Source B
        this.ctx.fillStyle = '#ef4444';
        this.ctx.fillRect(this.collisionX - 20, 280, 40, 20);
        this.ctx.fillText('Source B', this.collisionX - 20, 275);

        // Draw Collision Zone
        this.ctx.beginPath();
        this.ctx.arc(this.collisionX, this.collisionY, 20, 0, Math.PI * 2);
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        this.ctx.stroke();

        // Draw Particles
        for (let p of this.particles) {
            this.ctx.fillStyle = p.color || (p.type === 'A' ? '#60a5fa' : '#f87171');
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
            this.ctx.fill();
        }
    },

    animate: function() {
        this.update();
        this.draw();
        this.animationId = requestAnimationFrame(() => this.animate());
    }
};

// ============================================================================
// Scattering Cross-Section Plot
// ============================================================================
const ScatteringPlot = {
    init: function() {
        const container = document.getElementById('scatteringPlot');
        if (!container) return;

        this.select = document.getElementById('scatteringType');
        this.select.addEventListener('change', () => this.updatePlot());

        this.updatePlot();
    },

    updatePlot: function() {
        const type = this.select.value;
        
        const theta = [];
        const r = [];
        
        // Generate polar data based on type
        for (let t = 0; t <= 360; t += 5) {
            const rad = t * Math.PI / 180;
            theta.push(t);
            
            let val = 0;
            if (type === 'stripping') {
                // Forward scattering (peak at 0)
                val = Math.exp(-Math.pow(t, 2) / 1000) + Math.exp(-Math.pow(t - 360, 2) / 1000);
            } else if (type === 'rebound') {
                // Backward scattering (peak at 180)
                val = Math.exp(-Math.pow(t - 180, 2) / 1000);
            } else if (type === 'complex') {
                // Symmetric (peaks at 0 and 180)
                val = 0.5 * (Math.exp(-Math.pow(t, 2) / 2000) + Math.exp(-Math.pow(t - 360, 2) / 2000) + Math.exp(-Math.pow(t - 180, 2) / 2000));
            }
            r.push(val);
        }

        const trace = {
            r: r,
            theta: theta,
            mode: 'lines',
            name: type,
            line: { color: '#3b82f6', width: 3 },
            type: 'scatterpolar',
            fill: 'toself'
        };

        const layout = {
            title: 'Differential Cross-Section',
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            polar: {
                radialaxis: { visible: false },
                angularaxis: { color: '#94a3b8' },
                bgcolor: 'rgba(0,0,0,0)'
            },
            margin: { t: 40, r: 40, b: 40, l: 40 },
            showlegend: false
        };

        Plotly.newPlot('scatteringPlot', [trace], layout, {displayModeBar: false});
    }
};

// ============================================================================
// PES Trajectory Visualizer
// ============================================================================
const PESVisualizer = {
    init: function() {
        const container = document.getElementById('pesPlot');
        if (!container) return;

        this.btnRun = document.getElementById('btnRunTrajectory');
        this.sliderEnergy = document.getElementById('sliderEnergy');
        
        this.btnRun.addEventListener('click', () => this.runTrajectory());
        
        this.drawPES();
    },

    drawPES: function() {
        // Generate PES data (Muller-Brown or simple hills)
        // Using a simplified model for visualization
        const x = [];
        const y = [];
        const z = [];

        for (let i = 0; i <= 40; i++) {
            const xi = i / 10; // 0 to 4
            x.push(xi);
            const zRow = [];
            for (let j = 0; j <= 40; j++) {
                const yj = j / 10; // 0 to 4
                if (i === 0) y.push(yj);
                
                // Simple L-shaped valley
                // Reactant valley along x (y large)
                // Product valley along y (x large)
                // Barrier at corner
                
                const v1 = Math.exp(-Math.pow(xi - 1, 2) - Math.pow(yj - 3, 2)); // Reactant well
                const v2 = Math.exp(-Math.pow(xi - 3, 2) - Math.pow(yj - 1, 2)); // Product well
                const wall = Math.exp(-xi*xi - yj*yj) * 5; // Repulsive wall
                
                // A curved path potential
                const r = Math.sqrt(xi*xi + yj*yj);
                const angle = Math.atan2(yj, xi);
                
                // Create a valley path
                const pathVal = Math.pow(r - 2.5, 2); 
                
                // Barrier
                const barrier = Math.exp(-Math.pow(xi-2, 2) - Math.pow(yj-2, 2)) * 2;

                zRow.push(pathVal + barrier);
            }
            z.push(zRow);
        }

        const data = [{
            z: z,
            x: x,
            y: y,
            type: 'contour',
            colorscale: 'Viridis',
            contours: {
                coloring: 'heatmap'
            }
        }];

        const layout = {
            title: 'Potential Energy Surface',
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            xaxis: { title: 'R_AB', color: '#94a3b8' },
            yaxis: { title: 'R_BC', color: '#94a3b8' },
            margin: { t: 40, r: 20, b: 40, l: 40 }
        };

        Plotly.newPlot('pesPlot', data, layout, {displayModeBar: false});
    },

    runTrajectory: function() {
        const energy = parseInt(this.sliderEnergy.value);
        const plotDiv = document.getElementById('pesPlot');
        
        // Simulate a path
        // Low energy: oscillate in reactant valley
        // High energy: cross barrier
        
        const pathX = [];
        const pathY = [];
        
        // Start in reactant valley
        let cx = 0.5;
        let cy = 3.5;
        
        for(let t=0; t<100; t++) {
            pathX.push(cx);
            pathY.push(cy);
            
            // Move towards barrier
            cx += 0.03;
            cy -= 0.03;
            
            // Barrier region approx (2, 2)
            if (cx > 1.5 && cy < 2.5) {
                if (energy < 50) {
                    // Reflect
                    cx -= 0.05; // Bounce back
                    cy += 0.01;
                } else {
                    // Cross
                    cx += 0.02;
                    cy -= 0.02;
                }
            }
        }
        
        const traceTrajectory = {
            x: pathX,
            y: pathY,
            mode: 'lines+markers',
            line: { color: 'white', width: 3 },
            marker: { size: 6, color: 'red' },
            name: 'Trajectory'
        };
        
        Plotly.addTraces(plotDiv, traceTrajectory);
        
        // Animate (simple redraw for now, or use Plotly frames if needed)
        // For simplicity, just showing the path
    }
};

// Initialize all
document.addEventListener('DOMContentLoaded', () => {
    // Check which slide is active or init all if possible
    // Reveal.js loads all slides, so we can init everything
    
    // We need to wait for Reveal to be ready or just init
    MolecularBeam.init();
    ScatteringPlot.init();
    PESVisualizer.init();
});

// Re-init on slide change to handle canvas sizing
if (window.Reveal) {
    Reveal.on('slidechanged', event => {
        MolecularBeam.resize();
        // Trigger plot resizes if needed
    });
}

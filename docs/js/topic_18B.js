/**
 * Topic 18B: Diffusion-Controlled Reactions
 * Interactive elements script
 */

// ==========================================================================
// 1. Cage Effect Simulation
// ==========================================================================
const CageEffect = {
    canvas: null,
    ctx: null,
    particles: [],
    animationId: null,
    mode: 'gas', // 'gas' or 'liquid'
    width: 0,
    height: 0,

    init: function() {
        this.canvas = document.getElementById('cageCanvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        
        // Event listeners for controls
        document.getElementById('btnGas').addEventListener('click', () => this.setMode('gas'));
        document.getElementById('btnLiquid').addEventListener('click', () => this.setMode('liquid'));
        
        window.addEventListener('resize', () => this.resize());
        
        this.setMode('gas');
        this.animate();
    },

    resize: function() {
        if (!this.canvas) return;
        const rect = this.canvas.parentElement.getBoundingClientRect();
        this.canvas.width = rect.width;
        this.canvas.height = 300; // Fixed height
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        this.initParticles();
    },

    setMode: function(mode) {
        this.mode = mode;
        
        // Update UI buttons
        document.getElementById('btnGas').classList.toggle('active', mode === 'gas');
        document.getElementById('btnLiquid').classList.toggle('active', mode === 'liquid');
        
        this.initParticles();
    },

    initParticles: function() {
        this.particles = [];
        const isLiquid = this.mode === 'liquid';
        const numParticles = isLiquid ? 300 : 50;
        const speed = isLiquid ? 0.5 : 3;
        const radius = isLiquid ? 6 : 4;

        // Create "solvent" particles
        for (let i = 0; i < numParticles; i++) {
            this.particles.push({
                x: Math.random() * this.width,
                y: Math.random() * this.height,
                vx: (Math.random() - 0.5) * speed,
                vy: (Math.random() - 0.5) * speed,
                radius: radius,
                color: isLiquid ? 'rgba(100, 116, 139, 0.3)' : 'rgba(100, 116, 139, 0.1)',
                type: 'solvent'
            });
        }

        // Add two "reactant" particles
        this.particles.push({
            x: this.width / 2 - 20,
            y: this.height / 2,
            vx: (Math.random() - 0.5) * speed,
            vy: (Math.random() - 0.5) * speed,
            radius: isLiquid ? 8 : 6,
            color: '#ef4444', // Red
            type: 'reactant'
        });
        this.particles.push({
            x: this.width / 2 + 20,
            y: this.height / 2,
            vx: (Math.random() - 0.5) * speed,
            vy: (Math.random() - 0.5) * speed,
            radius: isLiquid ? 8 : 6,
            color: '#3b82f6', // Blue
            type: 'reactant'
        });
    },

    update: function() {
        // Simple physics update
        for (let p of this.particles) {
            p.x += p.vx;
            p.y += p.vy;

            // Wall collisions
            if (p.x < p.radius || p.x > this.width - p.radius) p.vx *= -1;
            if (p.y < p.radius || p.y > this.height - p.radius) p.vy *= -1;
            
            // Keep in bounds
            p.x = Math.max(p.radius, Math.min(this.width - p.radius, p.x));
            p.y = Math.max(p.radius, Math.min(this.height - p.radius, p.y));
        }

        // Particle-Particle collisions (Simplified for visual effect)
        // In liquid mode, we just want them to crowd each other
        if (this.mode === 'liquid') {
            for (let i = 0; i < this.particles.length; i++) {
                for (let j = i + 1; j < this.particles.length; j++) {
                    const p1 = this.particles[i];
                    const p2 = this.particles[j];
                    const dx = p2.x - p1.x;
                    const dy = p2.y - p1.y;
                    const dist = Math.sqrt(dx*dx + dy*dy);
                    const minDist = p1.radius + p2.radius;

                    if (dist < minDist) {
                        // Simple elastic collision response
                        const angle = Math.atan2(dy, dx);
                        const tx = Math.cos(angle);
                        const ty = Math.sin(angle);
                        
                        // Separate
                        const overlap = minDist - dist;
                        p1.x -= tx * overlap * 0.5;
                        p1.y -= ty * overlap * 0.5;
                        p2.x += tx * overlap * 0.5;
                        p2.y += ty * overlap * 0.5;

                        // Bounce (exchange velocities roughly)
                        const tempVx = p1.vx;
                        const tempVy = p1.vy;
                        p1.vx = p2.vx;
                        p1.vy = p2.vy;
                        p2.vx = tempVx;
                        p2.vy = tempVy;
                    }
                }
            }
        }
    },

    draw: function() {
        this.ctx.clearRect(0, 0, this.width, this.height);

        // Draw particles
        for (let p of this.particles) {
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = p.color;
            this.ctx.fill();
            
            if (p.type === 'reactant') {
                this.ctx.strokeStyle = 'white';
                this.ctx.lineWidth = 2;
                this.ctx.stroke();
            }
        }
        
        // Draw label
        this.ctx.fillStyle = 'white';
        this.ctx.font = '14px Inter';
        this.ctx.fillText(this.mode === 'gas' ? 'Gas Phase: Free Motion' : 'Liquid Phase: Caged Motion', 10, 20);
    },

    animate: function() {
        this.update();
        this.draw();
        this.animationId = requestAnimationFrame(() => this.animate());
    }
};

// ==========================================================================
// 2. Smoluchowski Calculator
// ==========================================================================
const SmoluchowskiCalc = {
    init: function() {
        const container = document.getElementById('smoluchowski-calc');
        if (!container) return;

        // Inputs
        this.inputT = document.getElementById('inputT');
        this.inputEta = document.getElementById('inputEta');
        this.displayT = document.getElementById('displayT');
        this.displayEta = document.getElementById('displayEta');
        this.resultKd = document.getElementById('resultKd');

        // Listeners
        this.inputT.addEventListener('input', () => this.update());
        this.inputEta.addEventListener('input', () => this.update());

        this.update();
    },

    update: function() {
        const T = parseFloat(this.inputT.value); // K
        const eta = parseFloat(this.inputEta.value) * 1e-3; // mPa.s to Pa.s
        
        // Update displays
        this.displayT.textContent = T;
        this.displayEta.textContent = parseFloat(this.inputEta.value).toFixed(2);

        // Constants
        const R = 8.314; // J/(mol K)

        // Calculate kd = 8RT / 3eta
        // Result in m^3 mol^-1 s^-1
        let kd_SI = (8 * R * T) / (3 * eta);
        
        // Convert to M^-1 s^-1 (dm^3 mol^-1 s^-1)
        // 1 m^3 = 1000 dm^3
        let kd_M = kd_SI * 1000;

        // Format result (scientific notation)
        const exponent = Math.floor(Math.log10(kd_M));
        const mantissa = (kd_M / Math.pow(10, exponent)).toFixed(2);

        this.resultKd.innerHTML = `${mantissa} &times; 10<sup>${exponent}</sup>`;
    }
};

// ==========================================================================
// 3. Viscosity Plot (Diffusion vs Activation Control)
// ==========================================================================
const ViscosityPlot = {
    init: function() {
        const container = document.getElementById('viscosityPlot');
        if (!container) return;

        this.sliderKa = document.getElementById('sliderKa');
        this.displayKa = document.getElementById('displayKa');

        this.sliderKa.addEventListener('input', () => this.updatePlot());

        this.updatePlot();
    },

    updatePlot: function() {
        const ka_exp = parseFloat(this.sliderKa.value); // Exponent for ka
        const ka = Math.pow(10, ka_exp); // Actual ka value
        
        this.displayKa.innerHTML = `10<sup>${ka_exp}</sup>`;

        // Generate data
        // x-axis: 1/eta (Fluidity)
        // y-axis: k_obs
        
        const xValues = [];
        const yValues = [];
        const yDiff = []; // Pure diffusion limit
        const yAct = [];  // Pure activation limit

        // Constants
        const T = 298;
        const R = 8.314;
        const C = (8 * R * T) / 3; // Constant for kd = C * (1/eta) (SI units)
        // C approx 6600 J/mol

        // We want k in M^-1 s^-1
        // kd = (8RT/3eta) * 1000
        const C_M = C * 1000; 

        // Range of viscosity: 0.1 to 10 cP (mPa.s)
        // 1/eta range: 0.1 to 10 (units of 1/cP roughly)
        // Let's use arbitrary units for x to make it clean
        
        for (let fluidity = 0; fluidity <= 10; fluidity += 0.5) {
            xValues.push(fluidity);
            
            // Model: kd proportional to fluidity
            // Let's say at fluidity=1, kd = 1e9
            const kd = fluidity * 1e9; 
            
            // k_obs = (ka * kd) / (ka + kd) (assuming k-d is small or included in K)
            // Or simpler: 1/k = 1/kd + 1/ka
            
            const k_obs = 1 / (1/kd + 1/ka);
            
            yValues.push(k_obs);
            yDiff.push(kd);
            yAct.push(ka);
        }

        const trace1 = {
            x: xValues,
            y: yValues,
            mode: 'lines',
            name: 'Observed Rate',
            line: { color: '#8b5cf6', width: 4 }
        };

        const trace2 = {
            x: xValues,
            y: yDiff,
            mode: 'lines',
            name: 'Diffusion Limit',
            line: { color: '#3b82f6', dash: 'dash' }
        };

        const trace3 = {
            x: xValues,
            y: yAct,
            mode: 'lines',
            name: 'Activation Limit',
            line: { color: '#ef4444', dash: 'dash' }
        };

        const layout = {
            title: 'Rate Constant vs. Fluidity (1/&eta;)',
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            xaxis: { title: 'Fluidity (1/&eta;)', gridcolor: '#334155' },
            yaxis: { 
                title: 'Rate Constant k (M⁻¹s⁻¹)', 
                type: 'log',
                gridcolor: '#334155',
                exponentformat: 'e'
            },
            margin: { t: 40, r: 20, b: 40, l: 60 },
            legend: { x: 0.05, y: 1 }
        };

        Plotly.newPlot('viscosityPlot', [trace2, trace3, trace1], layout, {displayModeBar: false});
    }
};

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Check if we are on the right slide or just init everything
    // Reveal.js might load slides lazily, but elements should exist
    CageEffect.init();
    SmoluchowskiCalc.init();
    ViscosityPlot.init();
});

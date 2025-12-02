/**
 * Topic 18A: Collision Theory - Interactive Logic
 */

// Global Chart Instance
let mbChart = null;
let collisionSim = null;

document.addEventListener('DOMContentLoaded', () => {
    console.log("Topic 18A JS Loaded");

    // Initialize Components if elements exist
    if (document.getElementById('mbChart')) initMBExplorer();
    if (document.getElementById('collisionCanvas')) initCollisionSim();
    if (document.getElementById('steric-game')) initStericGame();
});

// ==========================================================================
// 1. Maxwell-Boltzmann Explorer
// ==========================================================================
function initMBExplorer() {
    const ctx = document.getElementById('mbChart').getContext('2d');
    const sliderT = document.getElementById('mb-temp');
    const sliderEa = document.getElementById('mb-ea');
    const dispT = document.getElementById('disp-mb-temp');
    const dispEa = document.getElementById('disp-mb-ea');
    const dispF = document.getElementById('disp-mb-fraction');

    // Initial Data
    const generateData = (T, Ea) => {
        const R = 8.314;
        const dataPoints = [];
        const labels = [];
        const reactiveColor = [];

        // Energy range 0 to 50 kJ/mol (scaled)
        for (let E = 0; E <= 50000; E += 500) {
            // Maxwell-Boltzmann Energy Distribution
            // f(E) = 2*sqrt(E/pi) * (1/kT)^1.5 * exp(-E/kT)
            // Simplified for visualization shape: E^0.5 * exp(-E/RT)
            const term1 = Math.sqrt(E);
            const term2 = Math.exp(-E / (R * T));
            const prob = term1 * term2; // Not normalized, just for shape

            labels.push(E / 1000); // kJ/mol
            dataPoints.push(prob);

            if (E >= Ea) {
                reactiveColor.push('rgba(239, 68, 68, 0.6)'); // Red for reactive
            } else {
                reactiveColor.push('rgba(59, 130, 246, 0.4)'); // Blue for non-reactive
            }
        }
        return { labels, dataPoints, reactiveColor };
    };

    const updateChart = () => {
        const T = parseInt(sliderT.value);
        const Ea = parseInt(sliderEa.value) * 1000; // Convert kJ to J

        dispT.textContent = T;
        dispEa.textContent = sliderEa.value;

        // Calculate Fraction f = exp(-Ea/RT)
        const R = 8.314;
        const f = Math.exp(-Ea / (R * T));
        dispF.innerHTML = `Fraction with $E \\ge E_a$: <strong>${f.toExponential(2)}</strong>`;

        // Re-render MathJax if needed (optional, might be heavy)
        if (window.MathJax) MathJax.typesetPromise([dispF]);

        const { labels, dataPoints, reactiveColor } = generateData(T, Ea);

        if (mbChart) {
            mbChart.data.labels = labels;
            mbChart.data.datasets[0].data = dataPoints;
            mbChart.data.datasets[0].backgroundColor = reactiveColor;
            mbChart.update('none');
        } else {
            mbChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Probability Density',
                        data: dataPoints,
                        backgroundColor: reactiveColor,
                        barPercentage: 1.0,
                        categoryPercentage: 1.0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: {
                            title: { display: true, text: 'Energy (kJ/mol)', color: '#94a3b8' },
                            ticks: { maxTicksLimit: 10, color: '#cbd5e1' },
                            grid: { display: false }
                        },
                        y: { display: false }
                    },
                    animation: { duration: 0 }
                }
            });
        }
    };

    sliderT.addEventListener('input', updateChart);
    sliderEa.addEventListener('input', updateChart);
    updateChart();
}

// ==========================================================================
// 2. 2D Collision Simulator
// ==========================================================================
function initCollisionSim() {
    const canvas = document.getElementById('collisionCanvas');
    const ctx = canvas.getContext('2d');
    const sliderCount = document.getElementById('sim-count');
    const sliderSpeed = document.getElementById('sim-speed');

    let particles = [];
    let animationId;
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = 300;

    class Particle {
        constructor() {
            this.r = 5;
            this.x = Math.random() * (width - 2 * this.r) + this.r;
            this.y = Math.random() * (height - 2 * this.r) + this.r;
            const speedBase = parseInt(sliderSpeed.value);
            const angle = Math.random() * Math.PI * 2;
            this.vx = Math.cos(angle) * speedBase;
            this.vy = Math.sin(angle) * speedBase;
            this.mass = 1;
            this.color = '#60a5fa'; // Default Blue
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            // Wall Collisions
            if (this.x - this.r < 0 || this.x + this.r > width) this.vx *= -1;
            if (this.y - this.r < 0 || this.y + this.r > height) this.vy *= -1;

            // Constrain
            this.x = Math.max(this.r, Math.min(width - this.r, this.x));
            this.y = Math.max(this.r, Math.min(height - this.r, this.y));

            // Color based on speed
            const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
            if (speed > 4) this.color = '#ef4444'; // Red (Fast)
            else this.color = '#60a5fa'; // Blue (Slow)
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
            ctx.strokeStyle = 'rgba(255,255,255,0.2)';
            ctx.stroke();
        }
    }

    function checkCollisions() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const p1 = particles[i];
                const p2 = particles[j];
                const dx = p2.x - p1.x;
                const dy = p2.y - p1.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < p1.r + p2.r) {
                    // Elastic Collision Logic
                    const angle = Math.atan2(dy, dx);
                    const sin = Math.sin(angle);
                    const cos = Math.cos(angle);

                    // Rotate velocities
                    const vx1 = p1.vx * cos + p1.vy * sin;
                    const vy1 = p1.vy * cos - p1.vx * sin;
                    const vx2 = p2.vx * cos + p2.vy * sin;
                    const vy2 = p2.vy * cos - p2.vx * sin;

                    // Swap x velocities (masses equal)
                    const vx1Final = vx2;
                    const vx2Final = vx1;

                    // Rotate back
                    p1.vx = vx1Final * cos - vy1 * sin;
                    p1.vy = vy1 * cos + vx1Final * sin;
                    p2.vx = vx2Final * cos - vy2 * sin;
                    p2.vy = vy2 * cos + vx2Final * sin;

                    // Separate particles to prevent sticking
                    const overlap = (p1.r + p2.r - dist) / 2;
                    p1.x -= overlap * Math.cos(angle);
                    p1.y -= overlap * Math.sin(angle);
                    p2.x += overlap * Math.cos(angle);
                    p2.y += overlap * Math.sin(angle);
                }
            }
        }
    }

    function initParticles() {
        particles = [];
        const count = parseInt(sliderCount.value);
        for (let i = 0; i < count; i++) {
            particles.push(new Particle());
        }
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        particles.forEach(p => {
            p.update();
            p.draw();
        });

        checkCollisions();

        animationId = requestAnimationFrame(animate);
    }

    // Listeners
    sliderCount.addEventListener('input', initParticles);
    sliderSpeed.addEventListener('input', () => {
        // Update speed of existing particles proportionally
        const newSpeed = parseInt(sliderSpeed.value);
        particles.forEach(p => {
            const angle = Math.atan2(p.vy, p.vx);
            p.vx = Math.cos(angle) * newSpeed;
            p.vy = Math.sin(angle) * newSpeed;
        });
    });

    initParticles();
    animate();
}

// ==========================================================================
// 3. Steric Factor Game
// ==========================================================================
function initStericGame() {
    const container = document.getElementById('steric-game');
    const molecule = document.getElementById('rotatable-molecule');
    const target = document.getElementById('target-site');
    const feedback = document.getElementById('steric-feedback');
    const btnCheck = document.getElementById('check-orientation');

    let rotation = 0;

    // Simple rotation control
    container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        const angle = Math.atan2(e.clientY - centerY, e.clientX - centerX);
        rotation = angle * (180 / Math.PI);
        molecule.style.transform = `rotate(${rotation}deg)`;
    });

    btnCheck.addEventListener('click', () => {
        // Normalize rotation to 0-360
        let normRot = (rotation % 360 + 360) % 360;

        // Target is at 0 degrees (right side)
        // Molecule reactive site is assumed to be at 0 degrees of the image
        // So we want the molecule to be pointing LEFT (180) to hit the target on the left? 
        // Let's assume target is fixed on the right. Molecule is on the left.
        // Molecule needs to point RIGHT (0 deg) to hit.

        // Let's simplify: Target is a "Dock". Molecule needs to align.
        // Let's say correct angle is 0 +/- 15 deg.

        if (normRot < 15 || normRot > 345) {
            feedback.innerHTML = "<span style='color:#4ade80'>Success! Reaction Occurred!</span>";
            feedback.style.animation = "pulse 0.5s";
        } else {
            feedback.innerHTML = "<span style='color:#ef4444'>Failed! Steric Hindrance.</span>";
        }
    });
}

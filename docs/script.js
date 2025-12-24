// =========================================
// INTERACTIVITY & CALCULATIONS
// =========================================

document.addEventListener('DOMContentLoaded', () => {
    initCalculator();
    initScrollSpy();
    initMobileMenu();
});

// --- 1. Rate Constant Calculator ---
function initCalculator() {
    const inputs = {
        A: document.getElementById('pre-exponential'),
        Ea: document.getElementById('activation-energy'),
        T: document.getElementById('temperature')
    };

    const displays = {
        temp: document.getElementById('temp-display'),
        result: document.getElementById('rate-result')
    };

    const canvas = document.getElementById('rateChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const R = 8.314; // Gas constant J/(mol K)

    // Initialize Chart
    let chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Reaction Rate k(T)',
                data: [],
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointRadius: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Temperature (K)', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#64748b' }
                },
                y: {
                    title: { display: true, text: 'Rate Constant k', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#64748b' }
                }
            }
        }
    });

    function calculateK(A, Ea, T) {
        // Ea in kJ/mol -> J/mol
        return A * Math.exp(-(Ea * 1000) / (R * T));
    }

    function update() {
        const A = parseFloat(inputs.A.value) || 0;
        const Ea = parseFloat(inputs.Ea.value) || 0;
        const currentT = parseFloat(inputs.T.value) || 298;

        // Update Text
        displays.temp.textContent = `${currentT} K`;
        const k = calculateK(A, Ea, currentT);
        displays.result.textContent = k.toExponential(2);

        // Update Graph (Curve from 200K to 1000K)
        const temps = [];
        const rates = [];
        for (let t = 200; t <= 1000; t += 20) {
            temps.push(t);
            rates.push(calculateK(A, Ea, t));
        }

        chart.data.labels = temps;
        chart.data.datasets[0].data = rates;
        chart.update();
    }

    // Listeners
    Object.values(inputs).forEach(input => input.addEventListener('input', update));
    update(); // Initial run
}

// --- 2. Scroll Spy (Navbar Highlight) ---
function initScrollSpy() {
    const sections = document.querySelectorAll('section, header');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let current = '';
        const scrollY = window.scrollY;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            // logic: if scrolled past start of section (minus offset for header)
            if (scrollY >= (sectionTop - 150)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });
}

// --- 3. Mobile Menu ---
function initMobileMenu() {
    const btn = document.querySelector('.btn-mobile-menu');
    const links = document.querySelector('.nav-links');

    if (btn) {
        btn.addEventListener('click', () => {
            // Simple toggle for now, in real app needs animation class
            const display = window.getComputedStyle(links).display;
            links.style.display = (display === 'none') ? 'flex' : 'none';
            if (links.style.display === 'flex') {
                links.style.flexDirection = 'column';
                links.style.position = 'absolute';
                links.style.top = '80px';
                links.style.left = '0';
                links.style.width = '100%';
                links.style.background = 'rgba(15, 17, 26, 0.95)';
                links.style.padding = '20px';
            }
        });
    }
}

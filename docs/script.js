document.addEventListener('DOMContentLoaded', () => {
    // --- Search Functionality ---
    const searchInput = document.getElementById('search-input');
    const notebookGrid = document.getElementById('notebook-grid');
    const cards = notebookGrid.getElementsByClassName('card');

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();

        Array.from(cards).forEach(card => {
            const title = card.getAttribute('data-title').toLowerCase();
            const topic = card.getAttribute('data-topic').toLowerCase();

            if (title.includes(searchTerm) || topic.includes(searchTerm)) {
                card.style.display = 'flex';
                // Reset animation
                card.style.animation = 'none';
                card.offsetHeight; /* trigger reflow */
                card.style.animation = 'fadeInDown 0.5s ease-out';
            } else {
                card.style.display = 'none';
            }
        });
    });

    // --- Rate Calculator & Chart ---
    const preExpInput = document.getElementById('pre-exponential');
    const activationEnergyInput = document.getElementById('activation-energy');
    const temperatureInput = document.getElementById('temperature');
    const tempDisplay = document.getElementById('temp-display');
    const rateResult = document.getElementById('rate-result');
    const ctx = document.getElementById('rateChart').getContext('2d');

    const R = 8.314; // Gas constant in J/(mol*K)

    // Initialize Chart
    let rateChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Rate Constant k (s⁻¹)',
                data: [],
                borderColor: '#60a5fa',
                backgroundColor: 'rgba(96, 165, 250, 0.2)',
                borderWidth: 3,
                pointBackgroundColor: '#3b82f6',
                pointRadius: 0,
                pointHoverRadius: 6,
                fill: true,
                tension: 0.4
            }, {
                label: 'Current T',
                data: [],
                pointBackgroundColor: '#fff',
                pointBorderColor: '#8b5cf6',
                pointBorderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8,
                showLine: false // Only show the point
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: { color: '#cbd5e1' }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    backgroundColor: 'rgba(15, 23, 42, 0.9)',
                    titleColor: '#fff',
                    bodyColor: '#cbd5e1',
                    borderColor: 'rgba(255, 255, 255, 0.1)',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    type: 'linear',
                    title: { display: true, text: 'Temperature (K)', color: '#94a3b8' },
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#cbd5e1' }
                },
                y: {
                    title: { display: true, text: 'Rate Constant k (s⁻¹)', color: '#94a3b8' },
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#cbd5e1' },
                    type: 'linear' // Can switch to 'logarithmic' if needed
                }
            },
            interaction: {
                mode: 'nearest',
                axis: 'x',
                intersect: false
            }
        }
    });

    function calculateRate() {
        const A = parseFloat(preExpInput.value);
        const Ea_kJ = parseFloat(activationEnergyInput.value);
        const T = parseFloat(temperatureInput.value);

        if (isNaN(A) || isNaN(Ea_kJ) || isNaN(T)) {
            rateResult.textContent = "Invalid Input";
            return;
        }

        // Update Display
        tempDisplay.textContent = T + " K";
        const Ea = Ea_kJ * 1000;
        const k = A * Math.exp(-Ea / (R * T));
        rateResult.textContent = k.toExponential(3) + " s⁻¹";

        updateChart(A, Ea, T);
    }

    function updateChart(A, Ea, currentT) {
        // Generate data points for T from 200K to 1000K
        const temps = [];
        const rates = [];
        const currentPoint = [];

        for (let t = 200; t <= 1000; t += 10) {
            const k_val = A * Math.exp(-Ea / (R * t));
            temps.push(t);
            rates.push({ x: t, y: k_val });
        }

        // Current T point
        const currentK = A * Math.exp(-Ea / (R * currentT));

        // Update Chart Data
        rateChart.data.labels = temps;
        rateChart.data.datasets[0].data = rates;

        // Update "Current T" point dataset
        // We need to make it an array of same length or just one point?
        // For scatter/line mix, we can just provide one point if x-axis is linear
        rateChart.data.datasets[1].data = [{ x: currentT, y: currentK }];

        rateChart.update('none'); // 'none' mode for performance
    }

    // Add event listeners
    preExpInput.addEventListener('input', calculateRate);
    activationEnergyInput.addEventListener('input', calculateRate);
    temperatureInput.addEventListener('input', calculateRate);

    // Initial calculation
    calculateRate();
});

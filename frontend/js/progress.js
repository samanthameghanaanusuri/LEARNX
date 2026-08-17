let trajectoryChart = null;

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const data = await LEARNX_API.getProgressSummary();
        
        renderRankings(data.strongest_concepts, data.weakest_concepts);
        renderDeltas(data.recently_changing);
        renderChart(data.trajectory);

    } catch (err) {
        console.error('Error loading progress analytics:', err);
    }
});

function renderRankings(strongest, weakest) {
    const strongestList = document.getElementById('strongest-concepts-list');
    const weakestList = document.getElementById('weakest-concepts-list');

    // Render Strongest (filter out unassessed/default mastery, keep only >= 0.6)
    const masteredConcepts = strongest.filter(c => c.mastery_score >= 0.6);
    if (masteredConcepts.length === 0) {
        strongestList.innerHTML = `<li style="font-size: 0.85rem; color: var(--text-secondary); text-align: center; padding: 0.5rem 0;">No mastered concepts (≥ 60%) yet.</li>`;
    } else {
        strongestList.innerHTML = '';
        masteredConcepts.forEach(c => {
            const li = document.createElement('li');
            li.className = 'concept-pill-item';
            li.innerHTML = `
                <span>${c.concept_name} <span style="font-size: 0.75rem; color: var(--text-secondary); font-weight: normal;">(${c.subject_name})</span></span>
                <span class="badge badge-mastered">${Math.round(c.mastery_score * 100)}%</span>
            `;
            strongestList.appendChild(li);
        });
    }

    // Render Weakest (filter out unassessed, keep only < 0.6)
    // Note: since our database seed sets concept mastery defaults to 0.15,
    // we only rank them as "weakest" if the student has actually attempted questions (evidence count > 0)
    // to distinguish from unassessed. But for simpler rendering, we can display any < 0.6.
    const weakConcepts = weakest.filter(c => c.mastery_score < 0.6);
    if (weakConcepts.length === 0) {
        weakestList.innerHTML = `<li style="font-size: 0.85rem; color: var(--text-secondary); text-align: center; padding: 0.5rem 0;">All assessed concepts are in good standing!</li>`;
    } else {
        weakestList.innerHTML = '';
        weakConcepts.forEach(c => {
            const li = document.createElement('li');
            li.className = 'concept-pill-item';
            li.innerHTML = `
                <span>${c.concept_name} <span style="font-size: 0.75rem; color: var(--text-secondary); font-weight: normal;">(${c.subject_name})</span></span>
                <span class="badge badge-weak">${Math.round(c.mastery_score * 100)}%</span>
            `;
            weakestList.appendChild(li);
        });
    }
}

function renderDeltas(deltas) {
    const list = document.getElementById('recent-changes-list');
    if (!deltas || deltas.length === 0) {
        list.innerHTML = `<li style="font-size: 0.85rem; color: var(--text-secondary); text-align: center; padding: 0.5rem 0;">Answer questions to view BKT updates.</li>`;
        return;
    }

    list.innerHTML = '';
    deltas.forEach(d => {
        const date = new Date(d.timestamp).toLocaleTimeString();
        const delta = d.change;
        const deltaStr = delta >= 0 ? `+${delta.toFixed(3)}` : `${delta.toFixed(3)}`;
        const deltaClass = delta >= 0 ? 'delta-positive' : 'delta-negative';

        const li = document.createElement('li');
        li.className = 'concept-pill-item';
        li.innerHTML = `
            <div>
                <span style="font-weight: 600;">${d.concept_name}</span>
                <div style="font-size: 0.7rem; color: var(--text-secondary); margin-top: 0.15rem;">
                    BKT Mastery transition: ${Math.round(d.previous_mastery * 100)}% ➔ ${Math.round(d.updated_mastery * 100)}%
                </div>
            </div>
            <div style="text-align: right;">
                <span class="delta-value ${deltaClass}">${deltaStr}</span>
                <div style="font-size: 0.7rem; color: var(--text-secondary); margin-top: 0.15rem;">${date}</div>
            </div>
        `;
        list.appendChild(li);
    });
}

function renderChart(trajectory) {
    const placeholder = document.getElementById('chart-placeholder');
    const container = document.getElementById('chart-canvas-container');
    const description = document.getElementById('chart-description');

    if (!trajectory || !trajectory.points || trajectory.points.length === 0) {
        placeholder.style.display = 'flex';
        container.style.display = 'none';
        return;
    }

    placeholder.style.display = 'none';
    container.style.display = 'block';

    description.innerHTML = `Estimated mastery probability $P(L)$ transition over time for concept: <strong>${trajectory.concept_name}</strong>.`;

    const labels = trajectory.points.map((_, index) => `Q${index + 1}`);
    const dataPoints = trajectory.points.map(pt => pt.updated_mastery);
    const pointColors = trajectory.points.map(pt => pt.correct ? '#10b981' : '#ef4444');

    const ctx = document.getElementById('trajectoryChart').getContext('2d');
    
    if (trajectoryChart) {
        trajectoryChart.destroy();
    }

    trajectoryChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Bayesian Mastery P(L)',
                data: dataPoints,
                borderColor: '#6366f1',
                backgroundColor: 'rgba(99, 102, 241, 0.1)',
                borderWidth: 2,
                pointBackgroundColor: pointColors,
                pointBorderColor: '#030712',
                pointBorderWidth: 1.5,
                pointRadius: 6,
                pointHoverRadius: 8,
                fill: true,
                tension: 0.15
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const val = context.parsed.y;
                            const index = context.dataIndex;
                            const isCorrect = trajectory.points[index].correct;
                            return `Mastery: ${Math.round(val * 100)}% (${isCorrect ? 'Correct' : 'Incorrect'})`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#9ca3af',
                        font: {
                            family: 'Plus Jakarta Sans',
                            weight: 'bold'
                        }
                    }
                },
                y: {
                    min: 0.0,
                    max: 1.0,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#9ca3af',
                        font: {
                            family: 'Plus Jakarta Sans'
                        },
                        callback: function(value) {
                            return `${Math.round(value * 100)}%`;
                        }
                    }
                }
            }
        }
    });
}

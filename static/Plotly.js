async function update() {
    const text = document.getElementById('inp').value;
    
    // Only run if there is actual content to analyze
    if(text.trim().length < 5) return;

    try {
        const res = await fetch('/predict', {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({complaint: text})
        });
        
        const d = await res.json();

        // 1. Update Word Features (Impact Weights)
        document.getElementById('featList').innerHTML = d.features.map(f => 
            `<div class="feature-item">${f.word} <span class="float-end text-success">${f.score}</span></div>`
        ).join('');

        // 2. Generate the Live Heatmap
        const trace = [{
            z: d.matrix,         // Probability data from Python
            x: d.categories,     // Class labels (Credit Card, etc.)
            y: d.models,         // Model names (LR, SVM, NB)
            type: 'heatmap',
            colorscale: 'Viridis',
            hoverongaps: false
        }];

        const layout = {
            title: 'REAL-TIME PROBABILITY DENSITY',
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#adbac7', size: 11 },
            margin: { t: 50, b: 100, l: 150, r: 20 },
            xaxis: { tickangle: 45, fixedrange: true },
            yaxis: { fixedrange: true }
        };

        Plotly.react('heatmap', trace, layout); // Use .react for faster real-time updates
    } catch (err) {
        console.error("Analysis Error:", err);
    }
}
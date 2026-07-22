document.addEventListener('DOMContentLoaded', () => {
    const areaInput = document.getElementById('area');
    const areaValueDisplay = document.getElementById('areaValue');
    const form = document.getElementById('predictionForm');
    
    const placeholderState = document.getElementById('placeholderState');
    const loadingState = document.getElementById('loadingState');
    const outputState = document.getElementById('outputState');

    const predictedPriceEl = document.getElementById('predictedPrice');
    const priceRangeEl = document.getElementById('priceRange');

    // Update live area label on slider change
    if (areaInput && areaValueDisplay) {
        areaInput.addEventListener('input', (e) => {
            areaValueDisplay.textContent = `${Number(e.target.value).toLocaleString()} sq ft`;
        });
    }

    // AJAX Form Submission
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Toggle visual states
            placeholderState.classList.add('hidden');
            outputState.classList.add('hidden');
            loadingState.classList.remove('hidden');

            const formData = new FormData(form);
            const payload = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();

                if (result.success) {
                    setTimeout(() => {
                        loadingState.classList.add('hidden');
                        outputState.classList.remove('hidden');

                        predictedPriceEl.textContent = result.formatted_price;
                        priceRangeEl.textContent = result.range;
                    }, 400);
                } else {
                    alert("Model Error: " + result.error);
                    loadingState.classList.add('hidden');
                    placeholderState.classList.remove('hidden');
                }
            } catch (error) {
                console.error("Prediction Error:", error);
                alert("Server Connection Error. Ensure app.py is running.");
                loadingState.classList.add('hidden');
                placeholderState.classList.remove('hidden');
            }
        });
    }
});
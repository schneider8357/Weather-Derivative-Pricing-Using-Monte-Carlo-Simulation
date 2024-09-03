document.getElementById('input-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const weatherParam = document.getElementById('weather-param').value;
    
    fetch('/api/simulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ weather_param: weatherParam }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Simulation Result: ${data.result.toFixed(2)}`;
    })
    .catch(error => {
        document.getElementById('result').innerText = `Error: ${error}`;
    });
});

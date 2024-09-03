import pandas as pd
from flask import Flask, render_template, request, jsonify
from src.monte_carlo_simulation import MonteCarloSimulation
from src.weather_derivative_pricing import WeatherDerivativePricing

app = Flask(__name__)

def run_simulation(weather_param, days_to_simulate=30, strike_price=50, payout_rate=100, derivative_type='HDD'):
    # Load historical weather data
    historical_data = pd.read_csv('data/historical_weather_data.csv')

    # Initialize Monte Carlo Simulation
    mc_simulation = MonteCarloSimulation(historical_data)
    simulations = mc_simulation.simulate_future_temperatures(days=days_to_simulate)

    # Initialize Weather Derivative Pricing
    pricing_model = WeatherDerivativePricing(strike_price, payout_rate)

    # Price the derivative
    derivative_price = pricing_model.price_derivative(simulations, derivative_type)
    
    return derivative_price

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/simulation', methods=['POST'])
def api_simulation():
    data = request.get_json()
    weather_param = data.get('weather_param', None)
    if weather_param is None:
        return jsonify({'error': 'Invalid input'}), 400
    
    # You can adjust these parameters as needed or pass them through the POST request
    days_to_simulate = 30
    strike_price = 50
    payout_rate = 100
    derivative_type = 'HDD'  # or 'CDD' depending on your use case

    try:
        derivative_price = run_simulation(weather_param, days_to_simulate, strike_price, payout_rate, derivative_type)
        return jsonify({'result': derivative_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd
from flask import Flask, render_template, request, jsonify
from monte_carlo_simulation import MonteCarloSimulation
from weather_derivative_pricing import WeatherDerivativePricing

app = Flask(__name__)

def run_simulation(weather_param, days_to_simulate=30, strike_price=50, payout_rate=100, derivative_type='HDD'):
    # Load historical weather data
    historical_data = pd.read_csv('../data/historical_weather_data_novo.csv')

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

    result = []
    for i in range(100):
        days_to_simulate = 91
        strike_price = 800 + i * 10
        payout_rate = 1
        derivative_type = 'CDD'  # or 'CDD' depending on your use case
        derivative_price = run_simulation(weather_param, days_to_simulate, strike_price, payout_rate, derivative_type)
        result.append(derivative_price)
    return jsonify({'result': result})
    # except Exception as e:
        # return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

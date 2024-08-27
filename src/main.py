import pandas as pd
from src.monte_carlo_simulation import MonteCarloSimulation
from src.weather_derivative_pricing import WeatherDerivativePricing

def main():
    # Load historical weather data
    historical_data = pd.read_csv('data/historical_weather_data.csv')

    # Initialize Monte Carlo Simulation
    mc_simulation = MonteCarloSimulation(historical_data)
    days_to_simulate = 30  # Example: simulate the next 30 days
    simulations = mc_simulation.simulate_future_temperatures(days=days_to_simulate)

    # Initialize Weather Derivative Pricing
    strike_price = 50  # Example strike price
    payout_rate = 100  # Example payout rate per degree day
    pricing_model = WeatherDerivativePricing(strike_price, payout_rate)

    # Price the derivative
    derivative_price = pricing_model.price_derivative(simulations, derivative_type='HDD')
    
    print(f"Estimated price for the weather derivative: ${derivative_price:.2f}")

if __name__ == "__main__":
    main()

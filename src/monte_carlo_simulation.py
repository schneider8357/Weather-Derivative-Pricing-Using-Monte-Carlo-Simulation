import numpy as np
import pandas as pd

class MonteCarloSimulation:
    def __init__(self, historical_data, n_simulations=10000):
        self.historical_data = historical_data
        self.n_simulations = n_simulations
    
    def simulate_future_temperatures(self, days):
        """Simulate future temperatures based on historical data."""
        mean_temp = self.historical_data['Temperature'].mean()
        std_temp = self.historical_data['Temperature'].std()
        
        simulations = np.random.normal(loc=mean_temp, scale=std_temp, size=(self.n_simulations, days))
        return simulations

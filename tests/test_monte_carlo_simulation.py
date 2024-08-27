import unittest
from src.monte_carlo_simulation import MonteCarloSimulation
import numpy as np

class TestMonteCarloSimulation(unittest.TestCase):
    def setUp(self):
        # Sample historical data
        self.historical_data = pd.DataFrame({
            'Temperature': np.random.normal(15, 5, 365)  # Simulating one year of daily temperatures
        })

    def test_simulate_future_temperatures(self):
        mc_sim = MonteCarloSimulation(self.historical_data)
        simulations = mc_sim.simulate_future_temperatures(30)  # Simulate 30 days
        
        # Check that the simulation has the correct shape
        self.assertEqual(simulations.shape, (mc_sim.n_simulations, 30))

if __name__ == '__main__':
    unittest.main()

import unittest
import numpy as np
from src.weather_derivative_pricing import WeatherDerivativePricing

class TestWeatherDerivativePricing(unittest.TestCase):
    def setUp(self):
        self.pricing_model = WeatherDerivativePricing(strike_price=50, payout_rate=100)

    def test_calculate_hdd(self):
        temperatures = np.array([[10, 15, 20], [5, 12, 18]])  # Simulated temperatures
        hdd = self.pricing_model.calculate_hdd(temperatures)
        self.assertEqual(hdd[0], 16)  # HDD for first scenario
        self.assertEqual(hdd[1], 29)  # HDD for second scenario

    def test_price_derivative(self):
        temperatures = np.array([[10, 15, 20], [5, 12, 18]])
        price = self.pricing_model.price_derivative(temperatures, derivative_type='HDD')
        expected_payout = np.mean([16 * 100, 29 * 100])
        self.assertAlmostEqual(price, expected_payout)

if __name__ == '__main__':
    unittest.main()

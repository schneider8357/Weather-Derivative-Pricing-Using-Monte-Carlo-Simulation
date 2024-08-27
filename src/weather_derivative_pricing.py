import numpy as np

class WeatherDerivativePricing:
    def __init__(self, strike_price, payout_rate):
        self.strike_price = strike_price
        self.payout_rate = payout_rate

    def calculate_hdd(self, temperatures, base_temp=18):
        """Calculate Heating Degree Days (HDD)"""
        hdd = np.maximum(base_temp - temperatures, 0).sum(axis=1)
        return hdd

    def calculate_cdd(self, temperatures, base_temp=18):
        """Calculate Cooling Degree Days (CDD)"""
        cdd = np.maximum(temperatures - base_temp, 0).sum(axis=1)
        return cdd

    def price_derivative(self, temperature_simulations, derivative_type='HDD'):
        """Price the derivative based on the simulations."""
        if derivative_type == 'HDD':
            payouts = self.calculate_hdd(temperature_simulations) * self.payout_rate
        elif derivative_type == 'CDD':
            payouts = self.calculate_cdd(temperature_simulations) * self.payout_rate
        else:
            raise ValueError("Unsupported derivative type. Use 'HDD' or 'CDD'.")

        return np.mean(payouts)

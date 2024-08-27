# tests/__init__.py

# Importing the test modules explicitly (if needed)
from .test_monte_carlo_simulation import TestMonteCarloSimulation
from .test_weather_derivative_pricing import TestWeatherDerivativePricing

# Define what is available for import when importing the tests package
__all__ = [
    'TestMonteCarloSimulation',
    'TestWeatherDerivativePricing'
]

# Optional: setup code for the test suite
def setup_test_environment():
    """
    Function to set up the environment for tests, if needed.
    For example, initializing variables, setting environment variables, etc.
    """
    pass

# Optionally, run the setup when the tests package is imported
setup_test_environment()

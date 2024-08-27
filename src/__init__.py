# src/__init__.py

# Importing the key classes and functions from the modules
from .monte_carlo_simulation import MonteCarloSimulation
from .weather_derivative_pricing import WeatherDerivativePricing

# Define what is available for import when importing the src package
__all__ = [
    'MonteCarloSimulation',
    'WeatherDerivativePricing'
]

# Optional: setup code or configuration for the src package
def setup_src_environment():
    """
    Function to set up the environment or configuration for the src package.
    For example, configuring logging, setting up default parameters, etc.
    """
    pass

# Optionally, run the setup when the src package is imported
setup_src_environment()

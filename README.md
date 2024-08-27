# Weather Derivative Pricing Using Monte Carlo Simulation

## Overview

This project implements a Monte Carlo simulation model for pricing weather derivatives, specifically focusing on temperature-based contracts such as Heating Degree Days (HDD) or Cooling Degree Days (CDD). The model simulates future weather scenarios based on historical temperature data and calculates the expected payout of the derivative.

## Project Structure

```plaintext
WeatherDerivativePricing/
│
├── data/
│   ├── historical_weather_data.csv       # Historical temperature data (10 years of synthetic data)
│   └── README.md                         # Explanation of data files
│
├── src/
│   ├── __init__.py                       # Init file for the source code directory
│   ├── monte_carlo_simulation.py         # Monte Carlo simulation model
│   ├── weather_derivative_pricing.py     # Weather derivative pricing model
│   └── main.py                           # Main script to run the simulation and pricing
│
├── tests/
│   ├── __init__.py                       # Init file for the test directory
│   ├── test_monte_carlo_simulation.py    # Unit tests for the Monte Carlo simulation model
│   └── test_weather_derivative_pricing.py # Unit tests for the weather derivative pricing model
│
├── README.md                             # Project overview and instructions
├── requirements.txt                      # List of required Python packages
└── .gitignore                            # Files and directories to be ignored by Git


## Features

- **Monte Carlo Simulation**: Simulates future temperature scenarios based on historical data.
- **Weather Derivative Pricing**: Prices temperature-based derivatives like HDD and CDD.
- **Historical Data**: Uses 10 years of synthetic daily temperature data for simulations.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/WeatherDerivativePricing.git
    cd WeatherDerivativePricing
    ```

2. **Install dependencies**:
    Make sure you have Python installed. Install the required Python packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the main script**:
    Execute the main script to simulate weather data and price the derivative:
    ```sh
    python src/main.py
    ```

## Usage

- **Simulate Future Temperatures**: The `MonteCarloSimulation` class simulates future temperature scenarios using historical data.
- **Price Weather Derivatives**: The `WeatherDerivativePricing` class calculates the expected payout of a weather derivative based on simulated temperatures.
- **Custom Parameters**: You can modify parameters like `n_simulations`, `strike_price`, and `payout_rate` in the `main.py` script to customize the simulations and pricing.

## Data

The `data/historical_weather_data.csv` file contains 10 years of synthetic daily temperature data, which is used as input for the simulations. The data includes the following columns:

- **Date**: The date for each temperature reading.
- **Temperature**: The recorded temperature in degrees Celsius.

## Tests

Unit tests are provided in the `tests/` directory to validate the functionality of the Monte Carlo simulation and weather derivative pricing models. Run the tests using:
```sh
python -m unittest discover -s tests

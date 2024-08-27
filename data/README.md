# Data Directory

## Overview

This directory contains the data files used for the Monte Carlo simulation and weather derivative pricing project. The data includes historical temperature data, which is essential for simulating future weather scenarios and pricing weather derivatives like Heating Degree Days (HDD) or Cooling Degree Days (CDD).

## Files

### 1. `historical_weather_data.csv`

- **Description**: This file contains synthetic daily temperature data for a period of 10 years, generated to simulate realistic weather patterns. The data is used as input for the Monte Carlo simulations that forecast future temperatures and calculate derivative payouts.
  
- **Columns**:
  - **Date**: The date for each temperature reading.
  - **Temperature**: The recorded temperature in degrees Celsius.

- **Data Generation**: The temperature data was generated using a normal distribution with a mean temperature of 15°C and a standard deviation of 10°C. This allows for a realistic spread of daily temperatures over the years.

- **Usage**:
  - The data is loaded by the `MonteCarloSimulation` class in the project to simulate future weather scenarios.
  - The simulated temperature scenarios are then used by the `WeatherDerivativePricing` class to calculate the expected payouts of weather derivatives.

## How to Use

- **Loading Data**: The data can be loaded into a pandas DataFrame using the following code:
    ```python
    import pandas as pd

    historical_data = pd.read_csv('data/historical_weather_data.csv')
    ```

- **Modifying Data**: If you need to use real-world data instead of the synthetic data provided, replace `historical_weather_data.csv` with your dataset, ensuring it follows the same format.

## Additional Notes

- **Synthetic Data**: The data provided is synthetic and may not perfectly represent real-world weather conditions. If using this project for financial or operational decisions, it is recommended to replace the synthetic data with actual historical weather data.
  
- **Data Sources**: For real-world applications, consider obtaining historical weather data from reliable sources like national meteorological agencies or climate data repositories.


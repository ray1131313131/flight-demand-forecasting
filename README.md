# Flight Demand Forecasting

## Overview
This repository contains a demonstration of time series forecasting for predicting flight demand. Using a synthetic dataset that emulates daily passenger volumes, the project trains an ARIMA model to forecast future demand. The objective is to illustrate how statistical forecasting techniques can be applied to anticipate passenger numbers and inform capacity planning.

## Features
- **Synthetic time series data**: The script generates a mock dataset representing daily flight demand over a period of time.
- **Exploratory analysis**: Includes basic statistics and a line plot to visualize demand trends.
- **ARIMA model**: Implements an AutoRegressive Integrated Moving Average model using the statsmodels library to forecast future demand.
- **Forecast visualization**: Produces a plot comparing historical demand with forecasted values, saved as an image file (`flight_demand_forecast.png`).
- **Reusable script**: All code is contained in `flight_demand_forecasting.py` and can be adapted to real datasets.

## Repository Structure
- `flight_demand_forecasting.py`: Generates synthetic demand data, fits an ARIMA model, and plots the forecast.
- `flight_demand_forecast.png`: Output plot comparing historical and forecasted demand.

## Technologies Used
- Python 3 (Pandas, NumPy, Statsmodels, Matplotlib)
- Git and GitHub for version control and collaboration

## Getting Started
1. **Clone the repository**:
   git clone https://github.com/ray1131313131/flight-demand-forecasting
   cd flight-demand-forecasting
2. **Install dependencies**:
   pip install pandas numpy statsmodels matplotlib
3. **Run the script**:
   python flight_demand_forecasting.py
   The script will generate the `flight_demand_forecast.png` image in the project directory.

## Why This Project
Forecasting flight demand helps airlines and airports make informed decisions about capacity, scheduling, and resource allocation. This project provides a simple, reproducible example of applying time series modeling to predict demand patterns.

## License
This project is released under the MIT License.

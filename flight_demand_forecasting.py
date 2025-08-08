import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

"""
Flight Demand Forecasting

This script creates a synthetic monthly time series representing flight demand over several
years. It fits an ARIMA(1,1,1) model to the data and forecasts the next six months.
The script prints the forecast values and saves a plot comparing historical data with the
forecast.

To run this script:
    python flight_demand_forecasting.py

It will print the forecast and save a plot called `flight_demand_forecast.png` in the
current directory.
"""

def main():
    # Create synthetic monthly flight demand data
    dates = pd.date_range('2021-01-01', '2024-06-01', freq='MS')
    np.random.seed(0)
    trend = np.linspace(100, 200, len(dates))
    seasonality = 20 * np.sin(np.linspace(0, 4 * np.pi, len(dates)))
    noise = np.random.normal(0, 5, len(dates))
    demand = trend + seasonality + noise
    series = pd.Series(demand, index=dates)

    # Fit ARIMA model
    model = ARIMA(series, order=(1, 1, 1))
    result = model.fit()

    # Forecast the next 6 months
    forecast = result.forecast(steps=6)
    print("Next 6 months forecast:")
    print(forecast)

    # Plot historical data and forecast
    plt.figure()
    series.plot(label='Historical')
    forecast.plot(label='Forecast', style='--')
    plt.legend()
    plt.title('Flight Demand Forecast')
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.tight_layout()
    plt.savefig('flight_demand_forecast.png')
    plt.close()

if __name__ == '__main__':
    main()

"""
services/forecasting.py

Placeholder for the month-end spend forecasting model.

Real implementation plan
------------------------
This module will train a scikit-learn LinearRegression model on the last
N days of historical spend data, then extrapolate to the end of the current
calendar month.

Steps to implement:
1. Fetch historical daily-spend series via cloud_cost_client.py.
2. Build feature matrix X (day-of-month, day-of-week, rolling 7-day avg).
3. Fit sklearn.linear_model.LinearRegression on the training window.
4. Predict remaining days; sum actuals + predictions for month-end estimate.
5. Return forecast dict matching the shape used in /spend/forecast.

Validation: hold out the last 7 days, compare RMSE to a naive persistence
baseline before shipping.
"""

from __future__ import annotations

from typing import Any


def forecast_spend(historical_data: list[dict[str, Any]]) -> dict[str, Any]:
    """Forecast month-end spend from historical daily spend data.

    Parameters
    ----------
    historical_data:
        List of dicts with keys ``day`` (int) and ``spend`` (float),
        representing each day's total cloud spend so far this month.

    Returns
    -------
    dict
        {
            "forecast_month_end": float,   # predicted total for the month
            "daily_trend": list[dict],     # actuals + forecasted days
        }

    Raises
    ------
    NotImplementedError
        Until the linear regression model is implemented.
    """
    raise NotImplementedError(
        "forecast_spend is not yet implemented. "
        "See module docstring for the planned sklearn LinearRegression approach."
    )

"""
CloudBudget FastAPI backend.

Endpoints return mock data today. Real AWS/Azure integrations will be
wired through services/cloud_cost_client.py once credentials are configured.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CloudBudget API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# GET /spend/current
# ---------------------------------------------------------------------------
# Shape mirrors the response that will eventually come from the AWS Cost
# Explorer GetCostAndUsage API and the Azure Cost Management Query API,
# grouped by service category.
# ---------------------------------------------------------------------------
@app.get("/spend/current")
def get_current_spend():
    """Return mock current-month spend broken down by cloud service."""
    return {
        "currency": "USD",
        "period": "2026-08",
        "services": [
            {"name": "Compute", "spend": 4_821.50},
            {"name": "Storage", "spend": 1_203.75},
            {"name": "Networking", "spend": 892.20},
            {"name": "Database", "spend": 2_145.00},
            {"name": "AI/ML", "spend": 650.30},
            {"name": "Other", "spend": 317.25},
        ],
        "total": 10_030.00,
    }


# ---------------------------------------------------------------------------
# GET /spend/forecast
# ---------------------------------------------------------------------------
# The `forecast` value and `daily_trend` array will eventually be produced
# by a scikit-learn linear regression model defined in
# services/forecasting.py → forecast_spend(historical_data).
# ---------------------------------------------------------------------------
@app.get("/spend/forecast")
def get_spend_forecast():
    """Return mock month-end spend forecast and daily trend."""
    return {
        "currency": "USD",
        "period": "2026-08",
        "forecast_month_end": 12_500.00,
        "daily_trend": [
            {"day": d, "actual": round(320 + d * 12.5 + (d % 3) * 15, 2)}
            for d in range(1, 26)
        ]
        + [
            # days 26-31: forecast (no actuals yet)
            {"day": d, "forecast": round(320 + d * 12.5, 2)}
            for d in range(26, 32)
        ],
    }


# ---------------------------------------------------------------------------
# GET /spend/anomalies
# ---------------------------------------------------------------------------
# Anomaly detection will eventually use a z-score / rolling-window deviation
# approach implemented in services/anomaly_detection.py →
# detect_anomalies(spend_series).  Spikes beyond ±2 standard deviations of
# the rolling 7-day mean will be flagged.
# ---------------------------------------------------------------------------
@app.get("/spend/anomalies")
def get_spend_anomalies():
    """Return mock anomaly flags for the current period."""
    return {
        "period": "2026-08",
        "anomalies": [
            {
                "day": 7,
                "service": "Compute",
                "expected": 310.00,
                "actual": 820.00,
                "severity": "high",
                "description": "Unexpected compute spike — possible runaway job",
            },
            {
                "day": 14,
                "service": "Storage",
                "expected": 42.00,
                "actual": 115.00,
                "severity": "medium",
                "description": "Storage egress unusually high",
            },
            {
                "day": 21,
                "service": "Networking",
                "expected": 30.00,
                "actual": 78.50,
                "severity": "low",
                "description": "Minor networking cost deviation",
            },
        ],
    }

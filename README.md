# ☁️ CloudBudget

> Cloud cost visibility, forecasting, and anomaly-detection — scaffolded and ready for real integrations.

## Architecture

```
CloudBudget/
├── backend/                  # Python FastAPI service
│   ├── main.py               # API routes (/spend/current, /forecast, /anomalies)
│   ├── requirements.txt
│   └── services/
│       ├── cloud_cost_client.py   # AWS Cost Explorer + Azure Cost Mgmt stubs
│       ├── forecasting.py         # sklearn LinearRegression stub
│       ├── anomaly_detection.py   # z-score / rolling-window stub
│       └── slack_alerts.py        # Slack Incoming Webhook stub
└── frontend/                 # React + TypeScript + Tailwind + Recharts
    └── src/
        ├── api/client.ts          # typed fetch helpers
        ├── components/
        │   ├── SpendByServiceChart.tsx
        │   ├── ForecastChart.tsx
        │   └── AnomalyList.tsx
        └── App.tsx                # Dashboard page
```

All endpoints currently return **mock data** so the dashboard renders immediately. Real integrations will replace each stub incrementally (see Roadmap below).

## Setup

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
# API available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

Optional env vars:
| Variable | Purpose |
|---|---|
| `SLACK_WEBHOOK_URL` | Slack Incoming Webhook URL for cost alerts |

### Frontend

```bash
cd frontend
npm install
npm run dev
# Dashboard at http://localhost:5173
```

Make sure the backend is running first (the frontend proxies to `http://localhost:8000`).

## API Reference

| Endpoint | Description |
|---|---|
| `GET /spend/current` | Current-month spend by service (compute, storage, networking, …) |
| `GET /spend/forecast` | Month-end forecast + daily trend array |
| `GET /spend/anomalies` | List of flagged spend anomalies with severity |

## Roadmap

- [ ] Connect real AWS Cost Explorer API (`services/cloud_cost_client.py → get_aws_cost_data`)
- [ ] Connect real Azure Cost Management API (`services/cloud_cost_client.py → get_azure_cost_data`)
- [ ] Implement linear regression forecasting model and validate against held-out days (`services/forecasting.py → forecast_spend`)
- [ ] Implement anomaly detection thresholding (z-score / rolling window) (`services/anomaly_detection.py → detect_anomalies`)
- [ ] Wire real Slack webhook alerts (`services/slack_alerts.py → send_alert`)
- [ ] Add cost-saving recommendation logic (rightsizing, reserved instance suggestions)
- [ ] Add historical trend persistence (Postgres / SQLite with daily snapshots)

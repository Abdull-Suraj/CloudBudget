import { useEffect, useState } from "react";
import {
  fetchCurrentSpend,
  fetchForecast,
  fetchAnomalies,
} from "./api/client";
import type { CurrentSpend, SpendForecast, AnomalyResponse } from "./api/client";
import { SpendByServiceChart } from "./components/SpendByServiceChart";
import { ForecastChart } from "./components/ForecastChart";
import { AnomalyList } from "./components/AnomalyList";

export default function App() {
  const [spend, setSpend] = useState<CurrentSpend | null>(null);
  const [forecast, setForecast] = useState<SpendForecast | null>(null);
  const [anomalies, setAnomalies] = useState<AnomalyResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([fetchCurrentSpend(), fetchForecast(), fetchAnomalies()])
      .then(([s, f, a]) => {
        setSpend(s);
        setForecast(f);
        setAnomalies(a);
      })
      .catch(() =>
        setError(
          "Could not connect to the CloudBudget API. Make sure the backend is running on http://localhost:8000."
        )
      );
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-indigo-700 text-white px-8 py-5 flex items-center gap-3 shadow">
        <span className="text-2xl">☁️</span>
        <div>
          <h1 className="text-xl font-bold tracking-tight">CloudBudget</h1>
          <p className="text-indigo-200 text-xs">Cloud Cost Optimization Dashboard</p>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-6 py-8 space-y-6">
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 rounded-xl p-4 text-sm">
            {error}
          </div>
        )}

        {!spend && !error && (
          <p className="text-gray-400 text-sm text-center py-16">Loading data…</p>
        )}

        {spend && (
          <SpendByServiceChart
            services={spend.services}
            total={spend.total}
            currency={spend.currency}
            period={spend.period}
          />
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {forecast && (
            <div className="lg:col-span-2">
              <ForecastChart data={forecast} />
            </div>
          )}
          {anomalies && (
            <div className="lg:col-span-1">
              <AnomalyList anomalies={anomalies.anomalies} period={anomalies.period} />
            </div>
          )}
        </div>
      </main>

      <footer className="text-center text-xs text-gray-400 py-6">
        CloudBudget · mock data · real integrations coming soon
      </footer>
    </div>
  );
}

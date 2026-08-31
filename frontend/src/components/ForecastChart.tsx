import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend,
  ReferenceLine,
} from "recharts";
import type { SpendForecast } from "../api/client";

interface Props {
  data: SpendForecast;
}

export function ForecastChart({ data }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h2 className="text-lg font-semibold text-gray-700 mb-1">
        Daily Spend &amp; Month-End Forecast
      </h2>
      <p className="text-sm text-gray-400 mb-4">
        {data.period} · Forecast end-of-month:{" "}
        <span className="text-indigo-600 font-medium">
          {data.currency} {data.forecast_month_end.toLocaleString()}
        </span>
      </p>
      <ResponsiveContainer width="100%" height={260}>
        <LineChart
          data={data.daily_trend}
          margin={{ top: 4, right: 16, left: 0, bottom: 4 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis dataKey="day" label={{ value: "Day", position: "insideBottomRight", offset: -4, fontSize: 11 }} tick={{ fontSize: 11 }} />
          <YAxis tickFormatter={(v) => `$${v}`} tick={{ fontSize: 11 }} />
          <Tooltip formatter={(v, name) => [`$${Number(v)}`, String(name)]} />
          <Legend />
          <Line
            type="monotone"
            dataKey="actual"
            stroke="#6366f1"
            strokeWidth={2}
            dot={false}
            name="Actual"
            connectNulls
          />
          <Line
            type="monotone"
            dataKey="forecast"
            stroke="#f59e0b"
            strokeWidth={2}
            strokeDasharray="5 5"
            dot={false}
            name="Forecast"
            connectNulls
          />
          <ReferenceLine x={25} stroke="#d1d5db" strokeDasharray="4 4" label={{ value: "today", fontSize: 10 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";
import type { ServiceSpend } from "../api/client";

interface Props {
  services: ServiceSpend[];
  total: number;
  currency: string;
  period: string;
}

export function SpendByServiceChart({ services, total, currency, period }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h2 className="text-lg font-semibold text-gray-700 mb-1">
        Current Spend by Service
      </h2>
      <p className="text-sm text-gray-400 mb-4">
        {period} · Total: {currency} {total.toLocaleString()}
      </p>
      <ResponsiveContainer width="100%" height={260}>
        <BarChart data={services} margin={{ top: 4, right: 16, left: 0, bottom: 4 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis dataKey="name" tick={{ fontSize: 12 }} />
          <YAxis
            tickFormatter={(v) => `$${(v / 1000).toFixed(1)}k`}
            tick={{ fontSize: 12 }}
          />
          <Tooltip formatter={(v) => [`$${Number(v).toLocaleString()}`, "Spend"]} />
          <Bar dataKey="spend" fill="#6366f1" radius={[4, 4, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

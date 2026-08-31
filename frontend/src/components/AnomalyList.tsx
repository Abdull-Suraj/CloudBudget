import type { Anomaly } from "../api/client";

const severityColors: Record<string, string> = {
  high: "bg-red-100 text-red-700 border-red-200",
  medium: "bg-amber-100 text-amber-700 border-amber-200",
  low: "bg-yellow-50 text-yellow-700 border-yellow-200",
};

interface Props {
  anomalies: Anomaly[];
  period: string;
}

export function AnomalyList({ anomalies, period }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h2 className="text-lg font-semibold text-gray-700 mb-1">
        Spend Anomalies
      </h2>
      <p className="text-sm text-gray-400 mb-4">{period}</p>
      {anomalies.length === 0 ? (
        <p className="text-sm text-gray-400">No anomalies detected.</p>
      ) : (
        <ul className="space-y-3">
          {anomalies.map((a) => (
            <li
              key={`${a.day}-${a.service}`}
              className={`border rounded-xl px-4 py-3 ${severityColors[a.severity]}`}
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-medium text-sm">
                  Day {a.day} · {a.service}
                </span>
                <span className="text-xs uppercase font-semibold tracking-wide">
                  {a.severity}
                </span>
              </div>
              <p className="text-xs">{a.description}</p>
              <p className="text-xs mt-1 opacity-80">
                Expected ${a.expected.toLocaleString()} · Actual $
                {a.actual.toLocaleString()}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

const BASE = "http://localhost:8000";

export interface ServiceSpend {
  name: string;
  spend: number;
}

export interface CurrentSpend {
  currency: string;
  period: string;
  services: ServiceSpend[];
  total: number;
}

export interface TrendDay {
  day: number;
  actual?: number;
  forecast?: number;
}

export interface SpendForecast {
  currency: string;
  period: string;
  forecast_month_end: number;
  daily_trend: TrendDay[];
}

export interface Anomaly {
  day: number;
  service: string;
  expected: number;
  actual: number;
  severity: "high" | "medium" | "low";
  description: string;
}

export interface AnomalyResponse {
  period: string;
  anomalies: Anomaly[];
}

export async function fetchCurrentSpend(): Promise<CurrentSpend> {
  const res = await fetch(`${BASE}/spend/current`);
  return res.json();
}

export async function fetchForecast(): Promise<SpendForecast> {
  const res = await fetch(`${BASE}/spend/forecast`);
  return res.json();
}

export async function fetchAnomalies(): Promise<AnomalyResponse> {
  const res = await fetch(`${BASE}/spend/anomalies`);
  return res.json();
}

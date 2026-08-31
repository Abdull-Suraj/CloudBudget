"""
services/anomaly_detection.py

Placeholder for the spend anomaly detection logic.

Real implementation plan
------------------------
Algorithm: z-score anomaly detection with a rolling window baseline.

Steps to implement:
1. Accept a pandas Series of daily spend values indexed by date.
2. Compute the rolling 7-day mean (μ) and standard deviation (σ).
3. For each day, calculate z = (actual − μ) / σ.
4. Flag days where |z| > threshold (default 2.0) as anomalies.
5. Enrich each flag with the affected service, severity tier
   (|z| > 3 → high, > 2 → medium, else low), and a human-readable
   description to feed into Slack alerts via slack_alerts.py.

Alternative: an Isolation Forest model (sklearn.ensemble.IsolationForest)
may be used instead if the spend distribution is multi-modal.
"""

from __future__ import annotations

from typing import Any


def detect_anomalies(
    spend_series: list[dict[str, Any]],
    threshold: float = 2.0,
) -> list[dict[str, Any]]:
    """Detect anomalous spend days using z-score / rolling-window deviation.

    Parameters
    ----------
    spend_series:
        List of dicts with keys ``day`` (int), ``service`` (str), and
        ``spend`` (float) for each day in the current period.
    threshold:
        Number of standard deviations above which a day is flagged.
        Defaults to 2.0.

    Returns
    -------
    list[dict]
        Each dict contains: ``day``, ``service``, ``expected``, ``actual``,
        ``severity`` ("high" | "medium" | "low"), and ``description``.

    Raises
    ------
    NotImplementedError
        Until the rolling z-score implementation is complete.
    """
    raise NotImplementedError(
        "detect_anomalies is not yet implemented. "
        "See module docstring for the planned z-score / rolling-window approach."
    )

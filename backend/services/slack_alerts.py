"""
services/slack_alerts.py

Sends cost alert notifications via Slack Incoming Webhooks.

Real implementation plan
------------------------
Set the environment variable SLACK_WEBHOOK_URL to your Slack Incoming
Webhook URL (https://api.slack.com/messaging/webhooks).  When implemented,
this module will POST a JSON payload to that URL using the `requests`
library (or `httpx` for async support).

For now, messages are printed to the console so the rest of the app works
without credentials.
"""

from __future__ import annotations

import logging
import os

logger = logging.getLogger(__name__)


def send_alert(message: str) -> None:
    """Send a cost-alert message to the configured Slack channel.

    Parameters
    ----------
    message:
        Human-readable alert text, e.g.
        "⚠️ Compute spend spiked to $820 on Aug 7 (expected ~$310)."

    Implementation notes
    --------------------
    * Reads ``SLACK_WEBHOOK_URL`` from the environment.
    * Will use ``requests.post(webhook_url, json={"text": message})``
      with error handling and retry logic (max 3 attempts, exponential
      back-off) once the real integration is wired.
    * Currently logs to console instead of making an HTTP call.
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        logger.warning(
            "SLACK_WEBHOOK_URL is not set — alert not sent to Slack. "
            "Message: %s",
            message,
        )
    else:
        # TODO: replace with real HTTP POST once integration is ready.
        logger.info(
            "[SLACK ALERT — stub, not sent] webhook=%s message=%s",
            webhook_url,
            message,
        )

    # Always echo to stdout so local dev surfaces the alert.
    print(f"[CloudBudget Alert] {message}")

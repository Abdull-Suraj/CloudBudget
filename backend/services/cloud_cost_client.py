"""
services/cloud_cost_client.py

Placeholder for cloud provider cost data retrieval.

Real implementation plan
------------------------
AWS
~~~
Use the boto3 Cost Explorer client (``boto3.client("ce")``) with
``get_cost_and_usage()``.  Group results by SERVICE, filtered to the
current calendar month.  Requires the ``ce:GetCostAndUsage`` IAM
permission and valid AWS credentials (env vars or instance profile).

Azure
~~~~~
Use ``azure.mgmt.costmanagement.CostManagementClient`` with
``query.usage()`` scoped to the target subscription/resource-group.
Requires a service principal with ``Cost Management Reader`` role and
credentials configured via ``DefaultAzureCredential``.
"""

from __future__ import annotations

from typing import Any


def get_aws_cost_data() -> list[dict[str, Any]]:
    """Fetch current-month spend grouped by service from AWS Cost Explorer.

    Returns
    -------
    list[dict]
        Each dict has keys ``name`` (str) and ``spend`` (float), mirroring
        the shape returned by /spend/current.

    Implementation notes
    --------------------
    * Client: ``boto3.client("ce", region_name="us-east-1")``
    * API call: ``client.get_cost_and_usage(TimePeriod=..., Granularity="MONTHLY",
      GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}], Metrics=["UnblendedCost"])``
    * Parse ``ResultsByTime[0]["Groups"]`` for service names and amounts.

    Raises
    ------
    NotImplementedError
        Until the boto3 integration is implemented.
    """
    raise NotImplementedError(
        "get_aws_cost_data is not yet implemented. "
        "See module docstring for the planned boto3 Cost Explorer approach."
    )


def get_azure_cost_data() -> list[dict[str, Any]]:
    """Fetch current-month spend grouped by service from Azure Cost Management.

    Returns
    -------
    list[dict]
        Each dict has keys ``name`` (str) and ``spend`` (float), mirroring
        the shape returned by /spend/current.

    Implementation notes
    --------------------
    * Client: ``CostManagementClient(credential, subscription_id)``
    * API call: ``client.query.usage(scope, QueryDefinition(type="ActualCost",
      timeframe="MonthToDate", dataset=QueryDataset(...)))``
    * Parse ``result.rows`` for service names and cost values.

    Raises
    ------
    NotImplementedError
        Until the azure-mgmt-costmanagement integration is implemented.
    """
    raise NotImplementedError(
        "get_azure_cost_data is not yet implemented. "
        "See module docstring for the planned Azure Cost Management API approach."
    )

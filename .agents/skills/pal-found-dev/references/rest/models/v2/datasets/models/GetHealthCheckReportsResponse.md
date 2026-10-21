# foundry_sdk.v2.datasets.models.GetHealthCheckReportsResponse


GetHealthCheckReportsResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.Dict[core_models.CheckRid, typing.Optional[data_health_models.CheckReport]] | required; no default | A map from Check RID to the most recent report for that check. If a check is configured<br>    but has not yet produced a report, the value will be absent. |

```python
class GetHealthCheckReportsResponse(core.ModelBase):
    """GetHealthCheckReportsResponse"""

    data: typing.Dict[core_models.CheckRid, typing.Optional[data_health_models.CheckReport]]
    """
    A map from Check RID to the most recent report for that check. If a check is configured
    but has not yet produced a report, the value will be absent.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CheckRid](../../core/models/CheckRid.md)
- [foundry_sdk.v2.data_health.models.CheckReport](../../data_health/models/CheckReport.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetHealthCheckReportsResponse.md)

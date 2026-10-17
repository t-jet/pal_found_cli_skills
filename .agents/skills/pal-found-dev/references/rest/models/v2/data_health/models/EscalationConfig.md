# foundry_sdk.v2.data_health.models.EscalationConfig


The configuration for when the severity of the failing health check should be escalated to CRITICAL – after a given number of failures, possibly within a time interval.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| failures_to_critical | failuresToCritical | int | required; no default | No additional field description in SDK source. |
| time_interval_in_seconds | timeIntervalInSeconds | typing.Optional[core.Long] | default None | No additional field description in SDK source. |

```python
class EscalationConfig(core.ModelBase):
    """The configuration for when the severity of the failing health check should be escalated to CRITICAL – after a given number of failures, possibly within a time interval."""

    failures_to_critical: int = pydantic.Field(alias=str("failuresToCritical"))  # type: ignore[literal-required]
    time_interval_in_seconds: typing.Optional[core.Long] = pydantic.Field(alias=str("timeIntervalInSeconds"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EscalationConfig.md)

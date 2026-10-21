# foundry_sdk.v2.orchestration.models.TimeTrigger


Trigger on a time based schedule.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| cron_expression | cronExpression | CronExpression | required; no default | No additional field description in SDK source. |
| time_zone | timeZone | core_models.ZoneId | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['time'] | 'time' | No additional field description in SDK source. |

```python
class TimeTrigger(core.ModelBase):
    """Trigger on a time based schedule."""

    cron_expression: CronExpression = pydantic.Field(alias=str("cronExpression"))  # type: ignore[literal-required]
    time_zone: core_models.ZoneId = pydantic.Field(alias=str("timeZone"))  # type: ignore[literal-required]
    type: typing.Literal["time"] = "time"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ZoneId](../../core/models/ZoneId.md)
- [foundry_sdk.v2.orchestration.models.CronExpression](CronExpression.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeTrigger.md)

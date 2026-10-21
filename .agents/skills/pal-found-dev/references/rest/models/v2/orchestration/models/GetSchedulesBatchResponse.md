# foundry_sdk.v2.orchestration.models.GetSchedulesBatchResponse


GetSchedulesBatchResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.Dict[core_models.ScheduleRid, Schedule] | required; no default | No additional field description in SDK source. |

```python
class GetSchedulesBatchResponse(core.ModelBase):
    """GetSchedulesBatchResponse"""

    data: typing.Dict[core_models.ScheduleRid, Schedule]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.models.Schedule](Schedule.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetSchedulesBatchResponse.md)

# foundry_sdk.v2.orchestration.models.ScheduleSucceededTrigger


Trigger whenever the specified schedule completes its action
successfully.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| schedule_rid | scheduleRid | core_models.ScheduleRid | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['scheduleSucceeded'] | 'scheduleSucceeded' | No additional field description in SDK source. |

```python
class ScheduleSucceededTrigger(core.ModelBase):
    """
    Trigger whenever the specified schedule completes its action
    successfully.
    """

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    type: typing.Literal["scheduleSucceeded"] = "scheduleSucceeded"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScheduleSucceededTrigger.md)

# foundry_sdk.v2.orchestration.models.ScheduleRunError


An error occurred attempting to run the schedule.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| error_name | errorName | ScheduleRunErrorName | required; no default | No additional field description in SDK source. |
| description | description | str | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['error'] | 'error' | No additional field description in SDK source. |

```python
class ScheduleRunError(core.ModelBase):
    """An error occurred attempting to run the schedule."""

    error_name: ScheduleRunErrorName = pydantic.Field(alias=str("errorName"))  # type: ignore[literal-required]
    description: str
    type: typing.Literal["error"] = "error"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunErrorName](ScheduleRunErrorName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScheduleRunError.md)

# foundry_sdk.v2.orchestration.errors.RunSchedulePermissionDeniedParameters


Could not run the Schedule.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| scheduleRid | scheduleRid | core_models.ScheduleRid | TypedDict key required | No additional field description in SDK source. |

```python
class RunSchedulePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not run the Schedule."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheduleRid: core_models.ScheduleRid
```

## Referenced definitions

- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RunSchedulePermissionDeniedParameters.md)

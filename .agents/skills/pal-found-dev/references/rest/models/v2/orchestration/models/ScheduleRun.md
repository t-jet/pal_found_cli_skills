# foundry_sdk.v2.orchestration.models.ScheduleRun


ScheduleRun

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ScheduleRunRid | required; no default | The RID of a schedule run |
| schedule_rid | scheduleRid | core_models.ScheduleRid | required; no default | No additional field description in SDK source. |
| schedule_version_rid | scheduleVersionRid | ScheduleVersionRid | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core_models.CreatedTime | required; no default | The time at which the schedule run was created. |
| created_by | createdBy | typing.Optional[core_models.CreatedBy] | default None | The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to<br>    empty. |
| result | result | typing.Optional[ScheduleRunResult] | None | The result of triggering the schedule. If empty, it means the service<br>    is still working on triggering the schedule. |

```python
class ScheduleRun(core.ModelBase):
    """ScheduleRun"""

    rid: ScheduleRunRid
    """The RID of a schedule run"""

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    schedule_version_rid: ScheduleVersionRid = pydantic.Field(alias=str("scheduleVersionRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time at which the schedule run was created."""

    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    """
    The Foundry user who manually invoked this schedule run. Automatic trigger runs have this field set to
    empty.
    """

    result: typing.Optional[ScheduleRunResult] = None
    """
    The result of triggering the schedule. If empty, it means the service
    is still working on triggering the schedule.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunResult](ScheduleRunResult.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunRid](ScheduleRunRid.md)
- [foundry_sdk.v2.orchestration.models.ScheduleVersionRid](ScheduleVersionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScheduleRun.md)

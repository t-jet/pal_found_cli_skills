# foundry_sdk.v2.orchestration.models.Schedule


Schedule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.ScheduleRid | required; no default | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[str] | default None | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| current_version_rid | currentVersionRid | ScheduleVersionRid | required; no default | The RID of the current schedule version |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |
| created_by | createdBy | core_models.CreatedBy | required; no default | No additional field description in SDK source. |
| updated_time | updatedTime | core_models.UpdatedTime | required; no default | No additional field description in SDK source. |
| updated_by | updatedBy | core_models.UpdatedBy | required; no default | No additional field description in SDK source. |
| paused | paused | SchedulePaused | required; no default | No additional field description in SDK source. |
| trigger | trigger | typing.Optional[Trigger] | None | The schedule trigger. If the requesting user does not have<br>    permission to see the trigger, this will be empty. |
| action | action | Action | required; no default | No additional field description in SDK source. |
| scope_mode | scopeMode | ScopeMode | required; no default | No additional field description in SDK source. |

```python
class Schedule(core.ModelBase):
    """Schedule"""

    rid: core_models.ScheduleRid
    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    current_version_rid: ScheduleVersionRid = pydantic.Field(alias=str("currentVersionRid"))  # type: ignore[literal-required]
    """The RID of the current schedule version"""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    paused: SchedulePaused
    trigger: typing.Optional[Trigger] = None
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    action: Action
    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../core/models/UpdatedTime.md)
- [foundry_sdk.v2.orchestration.models.Action](Action.md)
- [foundry_sdk.v2.orchestration.models.SchedulePaused](SchedulePaused.md)
- [foundry_sdk.v2.orchestration.models.ScheduleVersionRid](ScheduleVersionRid.md)
- [foundry_sdk.v2.orchestration.models.ScopeMode](ScopeMode.md)
- [foundry_sdk.v2.orchestration.models.Trigger](Trigger.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Schedule.md)

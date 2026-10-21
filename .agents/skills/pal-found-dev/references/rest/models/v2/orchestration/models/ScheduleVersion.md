# foundry_sdk.v2.orchestration.models.ScheduleVersion


ScheduleVersion

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ScheduleVersionRid | required; no default | The RID of a schedule version |
| schedule_rid | scheduleRid | core_models.ScheduleRid | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core_models.CreatedTime | required; no default | The time the schedule version was created |
| created_by | createdBy | core_models.CreatedBy | required; no default | The Foundry user who created the schedule version |
| trigger | trigger | typing.Optional[Trigger] | None | No additional field description in SDK source. |
| action | action | Action | required; no default | No additional field description in SDK source. |
| scope_mode | scopeMode | ScopeMode | required; no default | No additional field description in SDK source. |

```python
class ScheduleVersion(core.ModelBase):
    """ScheduleVersion"""

    rid: ScheduleVersionRid
    """The RID of a schedule version"""

    schedule_rid: core_models.ScheduleRid = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the schedule version was created"""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The Foundry user who created the schedule version"""

    trigger: typing.Optional[Trigger] = None
    action: Action
    scope_mode: ScopeMode = pydantic.Field(alias=str("scopeMode"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.models.Action](Action.md)
- [foundry_sdk.v2.orchestration.models.ScheduleVersionRid](ScheduleVersionRid.md)
- [foundry_sdk.v2.orchestration.models.ScopeMode](ScopeMode.md)
- [foundry_sdk.v2.orchestration.models.Trigger](Trigger.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScheduleVersion.md)

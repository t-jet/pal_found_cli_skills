# foundry_sdk.v2.orchestration.models.CreateScheduleRequest


CreateScheduleRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | typing.Optional[str] | default None | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| action | action | CreateScheduleRequestAction | required; no default | No additional field description in SDK source. |
| trigger | trigger | typing.Optional[Trigger] | None | The schedule trigger. If the requesting user does not have<br>    permission to see the trigger, this will be empty. |
| scope_mode | scopeMode | typing.Optional[CreateScheduleRequestScopeMode] | default None | No additional field description in SDK source. |

```python
class CreateScheduleRequest(core.ModelBase):
    """CreateScheduleRequest"""

    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    action: CreateScheduleRequestAction
    trigger: typing.Optional[Trigger] = None
    """
    The schedule trigger. If the requesting user does not have
    permission to see the trigger, this will be empty.
    """

    scope_mode: typing.Optional[CreateScheduleRequestScopeMode] = pydantic.Field(alias=str("scopeMode"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.orchestration.models.CreateScheduleRequestAction](CreateScheduleRequestAction.md)
- [foundry_sdk.v2.orchestration.models.CreateScheduleRequestScopeMode](CreateScheduleRequestScopeMode.md)
- [foundry_sdk.v2.orchestration.models.Trigger](Trigger.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateScheduleRequest.md)

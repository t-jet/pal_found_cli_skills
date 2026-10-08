# foundry_sdk.v2.orchestration.models.CreateScheduleRequestAction


CreateScheduleRequestAction

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| abort_on_failure | abortOnFailure | typing.Optional[AbortOnFailure] | default None | No additional field description in SDK source. |
| force_build | forceBuild | typing.Optional[ForceBuild] | default None | No additional field description in SDK source. |
| retry_backoff_duration | retryBackoffDuration | typing.Optional[RetryBackoffDuration] | default None | No additional field description in SDK source. |
| retry_count | retryCount | typing.Optional[RetryCount] | default None | No additional field description in SDK source. |
| fallback_branches | fallbackBranches | typing.Optional[FallbackBranches] | default None | No additional field description in SDK source. |
| branch_name | branchName | typing.Optional[core_models.BranchName] | default None | The target branch the schedule should run on. |
| notifications_enabled | notificationsEnabled | typing.Optional[NotificationsEnabled] | default None | No additional field description in SDK source. |
| target | target | CreateScheduleRequestBuildTarget | required; no default | No additional field description in SDK source. |

```python
class CreateScheduleRequestAction(core.ModelBase):
    """CreateScheduleRequestAction"""

    abort_on_failure: typing.Optional[AbortOnFailure] = pydantic.Field(alias=str("abortOnFailure"), default=None)  # type: ignore[literal-required]
    force_build: typing.Optional[ForceBuild] = pydantic.Field(alias=str("forceBuild"), default=None)  # type: ignore[literal-required]
    retry_backoff_duration: typing.Optional[RetryBackoffDuration] = pydantic.Field(alias=str("retryBackoffDuration"), default=None)  # type: ignore[literal-required]
    retry_count: typing.Optional[RetryCount] = pydantic.Field(alias=str("retryCount"), default=None)  # type: ignore[literal-required]
    fallback_branches: typing.Optional[FallbackBranches] = pydantic.Field(alias=str("fallbackBranches"), default=None)  # type: ignore[literal-required]
    branch_name: typing.Optional[core_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The target branch the schedule should run on."""

    notifications_enabled: typing.Optional[NotificationsEnabled] = pydantic.Field(alias=str("notificationsEnabled"), default=None)  # type: ignore[literal-required]
    target: CreateScheduleRequestBuildTarget
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.CreateScheduleRequestBuildTarget](CreateScheduleRequestBuildTarget.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.ForceBuild](ForceBuild.md)
- [foundry_sdk.v2.orchestration.models.NotificationsEnabled](NotificationsEnabled.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](RetryCount.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateScheduleRequestAction.md)

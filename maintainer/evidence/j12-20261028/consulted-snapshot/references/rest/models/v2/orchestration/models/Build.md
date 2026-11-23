# foundry_sdk.v2.orchestration.models.Build


Build

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.BuildRid | required; no default | The RID of a Build. |
| branch_name | branchName | core_models.BranchName | required; no default | The branch that the build is running on. |
| created_time | createdTime | core_models.CreatedTime | required; no default | The timestamp that the build was created. |
| created_by | createdBy | core_models.CreatedBy | required; no default | The user who created the build. |
| fallback_branches | fallbackBranches | FallbackBranches | required; no default | No additional field description in SDK source. |
| job_rids | jobRids | typing.List[core_models.JobRid] | required; no default | No additional field description in SDK source. |
| retry_count | retryCount | RetryCount | required; no default | No additional field description in SDK source. |
| retry_backoff_duration | retryBackoffDuration | RetryBackoffDuration | required; no default | No additional field description in SDK source. |
| abort_on_failure | abortOnFailure | AbortOnFailure | required; no default | No additional field description in SDK source. |
| status | status | BuildStatus | required; no default | No additional field description in SDK source. |
| finished_time | finishedTime | typing.Optional[core.AwareDatetime] | default None | The time the build finished processing. Will be empty while the build is still running. |
| schedule_rid | scheduleRid | typing.Optional[core_models.ScheduleRid] | default None | Schedule RID of the Schedule that triggered this build. If a user triggered the build, Schedule RID will be empty. |

```python
class Build(core.ModelBase):
    """Build"""

    rid: core_models.BuildRid
    """The RID of a Build."""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    """The branch that the build is running on."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp that the build was created."""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The user who created the build."""

    fallback_branches: FallbackBranches = pydantic.Field(alias=str("fallbackBranches"))  # type: ignore[literal-required]
    job_rids: typing.List[core_models.JobRid] = pydantic.Field(alias=str("jobRids"))  # type: ignore[literal-required]
    retry_count: RetryCount = pydantic.Field(alias=str("retryCount"))  # type: ignore[literal-required]
    retry_backoff_duration: RetryBackoffDuration = pydantic.Field(alias=str("retryBackoffDuration"))  # type: ignore[literal-required]
    abort_on_failure: AbortOnFailure = pydantic.Field(alias=str("abortOnFailure"))  # type: ignore[literal-required]
    status: BuildStatus
    finished_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("finishedTime"), default=None)  # type: ignore[literal-required]
    """The time the build finished processing. Will be empty while the build is still running."""

    schedule_rid: typing.Optional[core_models.ScheduleRid] = pydantic.Field(alias=str("scheduleRid"), default=None)  # type: ignore[literal-required]
    """Schedule RID of the Schedule that triggered this build. If a user triggered the build, Schedule RID will be empty."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.BuildRid](../../core/models/BuildRid.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.JobRid](../../core/models/JobRid.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](BuildStatus.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](RetryCount.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Build.md)

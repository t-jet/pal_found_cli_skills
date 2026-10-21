# foundry_sdk.v2.orchestration.models.Job


Job

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.JobRid | required; no default | The RID of a Job. |
| build_rid | buildRid | core_models.BuildRid | required; no default | The RID of the Build that the Job belongs to. |
| started_time | startedTime | JobStartedTime | required; no default | The time this job started waiting for the dependencies to be resolved. |
| latest_attempt_start_time | latestAttemptStartTime | typing.Optional[core.AwareDatetime] | default None | The time this job's latest attempt started running. This field may be empty or outdated if the job failed to start. |
| finished_time | finishedTime | typing.Optional[core.AwareDatetime] | default None | The time this job was finished. |
| job_status | jobStatus | JobStatus | required; no default | No additional field description in SDK source. |
| outputs | outputs | typing.List[JobOutput] | required; no default | Outputs of the Job. Only outputs with supported types are listed here; unsupported types are omitted.<br>    Currently supported types are Dataset and Media Set outputs. |

```python
class Job(core.ModelBase):
    """Job"""

    rid: core_models.JobRid
    """The RID of a Job."""

    build_rid: core_models.BuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of the Build that the Job belongs to."""

    started_time: JobStartedTime = pydantic.Field(alias=str("startedTime"))  # type: ignore[literal-required]
    """The time this job started waiting for the dependencies to be resolved."""

    latest_attempt_start_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("latestAttemptStartTime"), default=None)  # type: ignore[literal-required]
    """The time this job's latest attempt started running. This field may be empty or outdated if the job failed to start."""

    finished_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("finishedTime"), default=None)  # type: ignore[literal-required]
    """The time this job was finished."""

    job_status: JobStatus = pydantic.Field(alias=str("jobStatus"))  # type: ignore[literal-required]
    outputs: typing.List[JobOutput]
    """
    Outputs of the Job. Only outputs with supported types are listed here; unsupported types are omitted.
    Currently supported types are Dataset and Media Set outputs.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.core.models.BuildRid](../../core/models/BuildRid.md)
- [foundry_sdk.v2.core.models.JobRid](../../core/models/JobRid.md)
- [foundry_sdk.v2.orchestration.models.JobOutput](JobOutput.md)
- [foundry_sdk.v2.orchestration.models.JobStartedTime](JobStartedTime.md)
- [foundry_sdk.v2.orchestration.models.JobStatus](JobStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Job.md)

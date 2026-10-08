# foundry_sdk.v2.models.models.ModelStudioRun


ModelStudioRun

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| run_id | runId | RunId | required; no default | A unique identifier for this run, derived from the studio, config, and build. |
| build_rid | buildRid | ModelStudioRunBuildRid | required; no default | The RID of the build associated with this run. |
| job_rid | jobRid | ModelStudioRunJobRid | required; no default | The RID of the job associated with this run. |
| config_version | configVersion | ModelStudioConfigVersionNumber | required; no default | The configuration version used for this run. |
| started_by | startedBy | core_models.CreatedBy | required; no default | The user who started this run. |
| started_time | startedTime | core_models.CreatedTime | required; no default | When this run was started. |
| build_status | buildStatus | typing.Optional[orchestration_models.BuildStatus] | default None | Status of the build. |
| resolved_outputs | resolvedOutputs | typing.Dict[OutputAlias, ModelStudioRunOutput] | required; no default | Map of alias to resolved output details (e.g., for models, contains the version RID and experiment). |

```python
class ModelStudioRun(core.ModelBase):
    """ModelStudioRun"""

    run_id: RunId = pydantic.Field(alias=str("runId"))  # type: ignore[literal-required]
    """A unique identifier for this run, derived from the studio, config, and build."""

    build_rid: ModelStudioRunBuildRid = pydantic.Field(alias=str("buildRid"))  # type: ignore[literal-required]
    """The RID of the build associated with this run."""

    job_rid: ModelStudioRunJobRid = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]
    """The RID of the job associated with this run."""

    config_version: ModelStudioConfigVersionNumber = pydantic.Field(alias=str("configVersion"))  # type: ignore[literal-required]
    """The configuration version used for this run."""

    started_by: core_models.CreatedBy = pydantic.Field(alias=str("startedBy"))  # type: ignore[literal-required]
    """The user who started this run."""

    started_time: core_models.CreatedTime = pydantic.Field(alias=str("startedTime"))  # type: ignore[literal-required]
    """When this run was started."""

    build_status: typing.Optional[orchestration_models.BuildStatus] = pydantic.Field(alias=str("buildStatus"), default=None)  # type: ignore[literal-required]
    """Status of the build."""

    resolved_outputs: typing.Dict[OutputAlias, ModelStudioRunOutput] = pydantic.Field(alias=str("resolvedOutputs"))  # type: ignore[literal-required]
    """Map of alias to resolved output details (e.g., for models, contains the version RID and experiment)."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionNumber](ModelStudioConfigVersionNumber.md)
- [foundry_sdk.v2.models.models.ModelStudioRunBuildRid](ModelStudioRunBuildRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRunJobRid](ModelStudioRunJobRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRunOutput](ModelStudioRunOutput.md)
- [foundry_sdk.v2.models.models.OutputAlias](OutputAlias.md)
- [foundry_sdk.v2.models.models.RunId](RunId.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](../../orchestration/models/BuildStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelStudioRun.md)

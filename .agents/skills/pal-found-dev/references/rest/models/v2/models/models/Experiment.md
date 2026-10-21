# foundry_sdk.v2.models.models.Experiment


Experiment

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ExperimentRid | required; no default | No additional field description in SDK source. |
| model_rid | modelRid | ModelRid | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |
| created_by | createdBy | core_models.CreatedBy | required; no default | No additional field description in SDK source. |
| source | source | ExperimentSource | required; no default | No additional field description in SDK source. |
| status | status | ExperimentStatus | required; no default | No additional field description in SDK source. |
| status_message | statusMessage | typing.Optional[str] | default None | No additional field description in SDK source. |
| branch | branch | core_models.BranchName | required; no default | No additional field description in SDK source. |
| parameters | parameters | typing.List[Parameter] | required; no default | No additional field description in SDK source. |
| series | series | typing.List[SeriesAggregations] | required; no default | No additional field description in SDK source. |
| summary_metrics | summaryMetrics | typing.List[SummaryMetric] | required; no default | No additional field description in SDK source. |
| artifacts | artifacts | typing.Dict[ExperimentArtifactName, ExperimentArtifactMetadata] | required; no default | No additional field description in SDK source. |
| tags | tags | typing.List[ExperimentTagText] | required; no default | No additional field description in SDK source. |
| linked_model_version | linkedModelVersion | typing.Optional[ModelVersionRid] | default None | No additional field description in SDK source. |
| job_rid | jobRid | typing.Optional[core_models.JobRid] | default None | No additional field description in SDK source. |

```python
class Experiment(core.ModelBase):
    """Experiment"""

    rid: ExperimentRid
    model_rid: ModelRid = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    source: ExperimentSource
    status: ExperimentStatus
    status_message: typing.Optional[str] = pydantic.Field(alias=str("statusMessage"), default=None)  # type: ignore[literal-required]
    branch: core_models.BranchName
    parameters: typing.List[Parameter]
    series: typing.List[SeriesAggregations]
    summary_metrics: typing.List[SummaryMetric] = pydantic.Field(alias=str("summaryMetrics"))  # type: ignore[literal-required]
    artifacts: typing.Dict[ExperimentArtifactName, ExperimentArtifactMetadata]
    tags: typing.List[ExperimentTagText]
    linked_model_version: typing.Optional[ModelVersionRid] = pydantic.Field(alias=str("linkedModelVersion"), default=None)  # type: ignore[literal-required]
    job_rid: typing.Optional[core_models.JobRid] = pydantic.Field(alias=str("jobRid"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.JobRid](../../core/models/JobRid.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactMetadata](ExperimentArtifactMetadata.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactName](ExperimentArtifactName.md)
- [foundry_sdk.v2.models.models.ExperimentRid](ExperimentRid.md)
- [foundry_sdk.v2.models.models.ExperimentSource](ExperimentSource.md)
- [foundry_sdk.v2.models.models.ExperimentStatus](ExperimentStatus.md)
- [foundry_sdk.v2.models.models.ExperimentTagText](ExperimentTagText.md)
- [foundry_sdk.v2.models.models.ModelRid](ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](ModelVersionRid.md)
- [foundry_sdk.v2.models.models.Parameter](Parameter.md)
- [foundry_sdk.v2.models.models.SeriesAggregations](SeriesAggregations.md)
- [foundry_sdk.v2.models.models.SummaryMetric](SummaryMetric.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Experiment.md)

# foundry_sdk.v2.orchestration.models.GetJobsBatchRequestElement


GetJobsBatchRequestElement

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| job_rid | jobRid | core_models.JobRid | required; no default | The RID of a Job. |

```python
class GetJobsBatchRequestElement(core.ModelBase):
    """GetJobsBatchRequestElement"""

    job_rid: core_models.JobRid = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]
    """The RID of a Job."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.JobRid](../../core/models/JobRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetJobsBatchRequestElement.md)

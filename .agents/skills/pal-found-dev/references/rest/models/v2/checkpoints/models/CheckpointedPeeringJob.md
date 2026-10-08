# foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJob


A peering job that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| job_id | jobId | str | required; no default | Identifier of the peering job. |
| relationship_rid | relationshipRid | core.RID | required; no default | Resource identifier of the peering relationship. |
| type | type | typing.Literal['checkpointedPeeringJob'] | 'checkpointedPeeringJob' | No additional field description in SDK source. |

```python
class CheckpointedPeeringJob(core.ModelBase):
    """A peering job that was captured as part of a checkpoint."""

    job_id: str = pydantic.Field(alias=str("jobId"))  # type: ignore[literal-required]
    """Identifier of the peering job."""

    relationship_rid: core.RID = pydantic.Field(alias=str("relationshipRid"))  # type: ignore[literal-required]
    """Resource identifier of the peering relationship."""

    type: typing.Literal["checkpointedPeeringJob"] = "checkpointedPeeringJob"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedPeeringJob.md)

# foundry_sdk.v2.checkpoints.models.CheckpointedActionType


An ontology action type that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| action_type_rid | actionTypeRid | core.RID | required; no default | No additional field description in SDK source. |
| ontology | ontology | CheckpointedOntology | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['checkpointedActionType'] | 'checkpointedActionType' | No additional field description in SDK source. |

```python
class CheckpointedActionType(core.ModelBase):
    """An ontology action type that was captured as part of a checkpoint."""

    action_type_rid: core.RID = pydantic.Field(alias=str("actionTypeRid"))  # type: ignore[literal-required]
    ontology: CheckpointedOntology
    type: typing.Literal["checkpointedActionType"] = "checkpointedActionType"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntology](CheckpointedOntology.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedActionType.md)

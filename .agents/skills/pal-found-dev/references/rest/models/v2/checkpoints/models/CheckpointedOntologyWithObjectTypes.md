# foundry_sdk.v2.checkpoints.models.CheckpointedOntologyWithObjectTypes


An ontology with its associated object types that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ontology | ontology | CheckpointedOntology | required; no default | No additional field description in SDK source. |
| object_type_rids | objectTypeRids | typing.List[core.RID] | required; no default | No additional field description in SDK source. |

```python
class CheckpointedOntologyWithObjectTypes(core.ModelBase):
    """An ontology with its associated object types that was captured as part of a checkpoint."""

    ontology: CheckpointedOntology
    object_type_rids: typing.List[core.RID] = pydantic.Field(alias=str("objectTypeRids"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntology](CheckpointedOntology.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedOntologyWithObjectTypes.md)

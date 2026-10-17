# foundry_sdk.v2.checkpoints.models.CheckpointedVersionedObjectSet


A versioned object set that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| versioned_object_set_rid | versionedObjectSetRid | core.RID | required; no default | No additional field description in SDK source. |
| object_set_version | objectSetVersion | core.UUID | required; no default | No additional field description in SDK source. |
| object_types | objectTypes | typing.List[CheckpointedOntologyWithObjectTypes] | required; no default | No additional field description in SDK source. |

```python
class CheckpointedVersionedObjectSet(core.ModelBase):
    """A versioned object set that was captured as part of a checkpoint."""

    versioned_object_set_rid: core.RID = pydantic.Field(alias=str("versionedObjectSetRid"))  # type: ignore[literal-required]
    object_set_version: core.UUID = pydantic.Field(alias=str("objectSetVersion"))  # type: ignore[literal-required]
    object_types: typing.List[CheckpointedOntologyWithObjectTypes] = pydantic.Field(alias=str("objectTypes"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntologyWithObjectTypes](CheckpointedOntologyWithObjectTypes.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedVersionedObjectSet.md)

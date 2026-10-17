# foundry_sdk.v2.checkpoints.models.CheckpointedOntology


An ontology snapshot that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ontology_rid | ontologyRid | core.RID | required; no default | No additional field description in SDK source. |
| ontology_version | ontologyVersion | core.UUID | required; no default | No additional field description in SDK source. |
| namespace_rid | namespaceRid | typing.Optional[NamespaceRid] | default None | No additional field description in SDK source. |

```python
class CheckpointedOntology(core.ModelBase):
    """An ontology snapshot that was captured as part of a checkpoint."""

    ontology_rid: core.RID = pydantic.Field(alias=str("ontologyRid"))  # type: ignore[literal-required]
    ontology_version: core.UUID = pydantic.Field(alias=str("ontologyVersion"))  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)
- [foundry_sdk.v2.checkpoints.models.NamespaceRid](NamespaceRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedOntology.md)

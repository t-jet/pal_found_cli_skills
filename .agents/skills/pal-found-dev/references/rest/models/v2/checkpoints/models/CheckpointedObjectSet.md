# foundry_sdk.v2.checkpoints.models.CheckpointedObjectSet


Represents the object set that was checkpointed.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| versioned | versioned | typing.Optional[CheckpointedVersionedObjectSet] | None | No additional field description in SDK source. |
| types_proxy | typesProxy | typing.Optional[CheckpointedObjectSetTypesProxy] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['checkpointedObjectSet'] | 'checkpointedObjectSet' | No additional field description in SDK source. |

```python
class CheckpointedObjectSet(core.ModelBase):
    """Represents the object set that was checkpointed."""

    versioned: typing.Optional[CheckpointedVersionedObjectSet] = None
    types_proxy: typing.Optional[CheckpointedObjectSetTypesProxy] = pydantic.Field(alias=str("typesProxy"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["checkpointedObjectSet"] = "checkpointedObjectSet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetTypesProxy](CheckpointedObjectSetTypesProxy.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedVersionedObjectSet](CheckpointedVersionedObjectSet.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedObjectSet.md)

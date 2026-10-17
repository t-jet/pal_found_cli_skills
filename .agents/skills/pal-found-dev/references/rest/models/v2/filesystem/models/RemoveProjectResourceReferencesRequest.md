# foundry_sdk.v2.filesystem.models.RemoveProjectResourceReferencesRequest


RemoveProjectResourceReferencesRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resources | resources | typing.List[core.RID] | required; no default | The resource identifiers to remove as references. These may be either filesystem or external resource identifiers. |

```python
class RemoveProjectResourceReferencesRequest(core.ModelBase):
    """RemoveProjectResourceReferencesRequest"""

    resources: typing.List[core.RID]
    """The resource identifiers to remove as references. These may be either filesystem or external resource identifiers."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RemoveProjectResourceReferencesRequest.md)

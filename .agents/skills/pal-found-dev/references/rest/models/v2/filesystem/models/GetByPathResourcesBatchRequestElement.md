# foundry_sdk.v2.filesystem.models.GetByPathResourcesBatchRequestElement


GetByPathResourcesBatchRequestElement

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| path | path | ResourcePath | required; no default | The path to the resource. The leading slash is optional. |

```python
class GetByPathResourcesBatchRequestElement(core.ModelBase):
    """GetByPathResourcesBatchRequestElement"""

    path: ResourcePath
    """The path to the resource. The leading slash is optional."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](ResourcePath.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetByPathResourcesBatchRequestElement.md)

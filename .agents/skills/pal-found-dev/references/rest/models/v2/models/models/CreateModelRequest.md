# foundry_sdk.v2.models.models.CreateModelRequest


CreateModelRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | ModelName | required; no default | No additional field description in SDK source. |
| parent_folder_rid | parentFolderRid | filesystem_models.FolderRid | required; no default | No additional field description in SDK source. |

```python
class CreateModelRequest(core.ModelBase):
    """CreateModelRequest"""

    name: ModelName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)
- [foundry_sdk.v2.models.models.ModelName](ModelName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateModelRequest.md)

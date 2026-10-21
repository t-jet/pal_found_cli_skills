# foundry_sdk.v1.datasets.models.CreateDatasetRequest


CreateDatasetRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | DatasetName | required; no default | No additional field description in SDK source. |
| parent_folder_rid | parentFolderRid | core_models.FolderRid | required; no default | No additional field description in SDK source. |

```python
class CreateDatasetRequest(core.ModelBase):
    """CreateDatasetRequest"""

    name: DatasetName
    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.FolderRid](../../core/models/FolderRid.md)
- [foundry_sdk.v1.datasets.models.DatasetName](DatasetName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateDatasetRequest.md)

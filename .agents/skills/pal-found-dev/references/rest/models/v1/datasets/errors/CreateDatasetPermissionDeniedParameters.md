# foundry_sdk.v1.datasets.errors.CreateDatasetPermissionDeniedParameters


The provided token does not have permission to create a dataset in this folder.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parentFolderRid | parentFolderRid | core_models.FolderRid | TypedDict key required | No additional field description in SDK source. |
| name | name | datasets_models.DatasetName | TypedDict key required | No additional field description in SDK source. |

```python
class CreateDatasetPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a dataset in this folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid
    name: datasets_models.DatasetName
```

## Referenced definitions

- [foundry_sdk.v1.core.models.FolderRid](../../core/models/FolderRid.md)
- [foundry_sdk.v1.datasets.models.DatasetName](../models/DatasetName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateDatasetPermissionDeniedParameters.md)

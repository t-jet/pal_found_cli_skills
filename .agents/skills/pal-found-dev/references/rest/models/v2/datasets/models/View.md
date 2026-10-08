# foundry_sdk.v2.datasets.models.View


View

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| view_name | viewName | DatasetName | required; no default | No additional field description in SDK source. |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The rid of the View. |
| parent_folder_rid | parentFolderRid | filesystem_models.FolderRid | required; no default | No additional field description in SDK source. |
| branch | branch | typing.Optional[core_models.BranchName] | None | The branch name of the View. If not specified, defaults to `master` for most enrollments. |
| backing_datasets | backingDatasets | typing.List[ViewBackingDataset] | required; no default | No additional field description in SDK source. |
| primary_key | primaryKey | typing.Optional[ViewPrimaryKey] | default None | No additional field description in SDK source. |

```python
class View(core.ModelBase):
    """View"""

    view_name: DatasetName = pydantic.Field(alias=str("viewName"))  # type: ignore[literal-required]
    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The rid of the View."""

    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    branch: typing.Optional[core_models.BranchName] = None
    """The branch name of the View. If not specified, defaults to `master` for most enrollments."""

    backing_datasets: typing.List[ViewBackingDataset] = pydantic.Field(alias=str("backingDatasets"))  # type: ignore[literal-required]
    primary_key: typing.Optional[ViewPrimaryKey] = pydantic.Field(alias=str("primaryKey"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.datasets.models.DatasetName](DatasetName.md)
- [foundry_sdk.v2.datasets.models.ViewBackingDataset](ViewBackingDataset.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKey](ViewPrimaryKey.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](View.md)

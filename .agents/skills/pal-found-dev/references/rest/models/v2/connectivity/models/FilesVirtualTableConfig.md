# foundry_sdk.v2.connectivity.models.FilesVirtualTableConfig


Pointer to the table in cloud object storage (e.g., Azure Data Lake Storage, Google Cloud Storage, S3).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | FileFormat | required; no default | No additional field description in SDK source. |
| path | path | str | required; no default | Storage path for the data in the underlying file system, i.e. paths like `/foo/bar`. The scheme is not <br>    included. May be either a folder or file. A non-partitioned table will have a single location. A <br>    partitioned table can have multiple locations, one for each partition. |
| type | type | typing.Literal['files'] | 'files' | No additional field description in SDK source. |

```python
class FilesVirtualTableConfig(core.ModelBase):
    """Pointer to the table in cloud object storage (e.g., Azure Data Lake Storage, Google Cloud Storage, S3)."""

    format: FileFormat
    path: str
    """
    Storage path for the data in the underlying file system, i.e. paths like `/foo/bar`. The scheme is not 
    included. May be either a folder or file. A non-partitioned table will have a single location. A 
    partitioned table can have multiple locations, one for each partition.
    """

    type: typing.Literal["files"] = "files"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.FileFormat](FileFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FilesVirtualTableConfig.md)

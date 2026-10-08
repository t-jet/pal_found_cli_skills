# foundry_sdk.v2.connectivity.models.FileChangedSinceLastUploadFilter


Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| file_properties | fileProperties | typing.List[FileProperty] | required; no default | The criteria on which to determine whether a file has been changed or not since the last import. <br>    If any of the specified criteria have changed, the file is consider changed. The criteria include:<br><br>    LAST_MODIFIED: The file's last modified timestamp has changed since the last import.<br>    SIZE: The file's size has changed since the last import.<br><br>    If no criteria are specified, only newly added files will be imported. |
| type | type | typing.Literal['changedSinceLastUploadFilter'] | 'changedSinceLastUploadFilter' | No additional field description in SDK source. |

```python
class FileChangedSinceLastUploadFilter(core.ModelBase):
    """
    Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
    This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.
    """

    file_properties: typing.List[FileProperty] = pydantic.Field(alias=str("fileProperties"))  # type: ignore[literal-required]
    """
    The criteria on which to determine whether a file has been changed or not since the last import. 
    If any of the specified criteria have changed, the file is consider changed. The criteria include:

    LAST_MODIFIED: The file's last modified timestamp has changed since the last import.
    SIZE: The file's size has changed since the last import.

    If no criteria are specified, only newly added files will be imported.
    """

    type: typing.Literal["changedSinceLastUploadFilter"] = "changedSinceLastUploadFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.FileProperty](FileProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileChangedSinceLastUploadFilter.md)

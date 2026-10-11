# foundry_sdk.v2.connectivity.models.FileImportFilter


Filters select which source files enter an import. Apply them in the configured order and test representative paths against the source before executing the import; order can affect efficiency. A filter changes selection, not the Connection's file access permission.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FileImportFilter: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "FilePathNotMatchesFilter",
        "FileAnyPathMatchesFilter",
        "FilesCountLimitFilter",
        "FileChangedSinceLastUploadFilter",
        "FileImportCustomFilter",
        "FileLastModifiedAfterFilter",
        "FilePathMatchesFilter",
        "FileAtLeastCountFilter",
        "FileSizeFilter",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.FileAnyPathMatchesFilter](FileAnyPathMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FileAtLeastCountFilter](FileAtLeastCountFilter.md)
- [foundry_sdk.v2.connectivity.models.FileChangedSinceLastUploadFilter](FileChangedSinceLastUploadFilter.md)
- [foundry_sdk.v2.connectivity.models.FileImportCustomFilter](FileImportCustomFilter.md)
- [foundry_sdk.v2.connectivity.models.FileLastModifiedAfterFilter](FileLastModifiedAfterFilter.md)
- [foundry_sdk.v2.connectivity.models.FilePathMatchesFilter](FilePathMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FilePathNotMatchesFilter](FilePathNotMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FileSizeFilter](FileSizeFilter.md)
- [foundry_sdk.v2.connectivity.models.FilesCountLimitFilter](FilesCountLimitFilter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileImportFilter.md)

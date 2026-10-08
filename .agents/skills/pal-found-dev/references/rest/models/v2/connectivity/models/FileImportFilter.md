# foundry_sdk.v2.connectivity.models.FileImportFilter



[Filters](https://palantir.com/docs/foundry/data-connection/file-based-syncs/#filters) allow you to filter source files
before they are imported into Foundry.


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

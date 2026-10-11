# foundry_sdk.v2.connectivity.models.ReplaceFileImportRequest


Choose the import mode, display name, source subfolder and ordered file filters for the replacement. An omitted subfolder means the source root. Preview representative included and excluded paths, then read back the import configuration before executing it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| import_mode | importMode | FileImportMode | required; no default | No additional field description in SDK source. |
| display_name | displayName | FileImportDisplayName | required; no default | No additional field description in SDK source. |
| subfolder | subfolder | typing.Optional[str] | None | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. |
| file_import_filters | fileImportFilters | typing.List[FileImportFilter] | required; no default | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. Learn more about optimizing file imports. |

```python
class ReplaceFileImportRequest(core.ModelBase):
    """ReplaceFileImportRequest"""

    import_mode: FileImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]
    display_name: FileImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    subfolder: typing.Optional[str] = None
    """A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system."""

    file_import_filters: typing.List[FileImportFilter] = pydantic.Field(alias=str("fileImportFilters"))  # type: ignore[literal-required]
    """Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](https://palantir.com/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.FileImportDisplayName](FileImportDisplayName.md)
- [foundry_sdk.v2.connectivity.models.FileImportFilter](FileImportFilter.md)
- [foundry_sdk.v2.connectivity.models.FileImportMode](FileImportMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceFileImportRequest.md)

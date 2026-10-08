# foundry_sdk.v2.connectivity.models.FileAtLeastCountFilter


Import all filtered files only if there are at least the specified number of files remaining.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| min_files_count | minFilesCount | int | required; no default | The minimum number of files remaining expected.<br>    The value specified must be greater than 0. |
| type | type | typing.Literal['atLeastCountFilter'] | 'atLeastCountFilter' | No additional field description in SDK source. |

```python
class FileAtLeastCountFilter(core.ModelBase):
    """Import all filtered files only if there are at least the specified number of files remaining."""

    min_files_count: int = pydantic.Field(alias=str("minFilesCount"))  # type: ignore[literal-required]
    """
    The minimum number of files remaining expected.
    The value specified must be greater than 0.
    """

    type: typing.Literal["atLeastCountFilter"] = "atLeastCountFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileAtLeastCountFilter.md)

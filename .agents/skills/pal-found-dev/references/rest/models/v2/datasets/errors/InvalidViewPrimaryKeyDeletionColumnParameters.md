# foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyDeletionColumnParameters


The deletion column must be a boolean.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| deletionColumn | deletionColumn | str | TypedDict key required | No additional field description in SDK source. |
| deletionColumnType | deletionColumnType | core_models.SchemaFieldType | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidViewPrimaryKeyDeletionColumnParameters(typing_extensions.TypedDict):
    """The deletion column must be a boolean."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    deletionColumn: str
    deletionColumnType: core_models.SchemaFieldType
```

## Referenced definitions

- [foundry_sdk.v2.core.models.SchemaFieldType](../../core/models/SchemaFieldType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidViewPrimaryKeyDeletionColumnParameters.md)

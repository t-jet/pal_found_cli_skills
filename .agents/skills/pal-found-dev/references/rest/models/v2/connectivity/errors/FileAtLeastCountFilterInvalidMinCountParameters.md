# foundry_sdk.v2.connectivity.errors.FileAtLeastCountFilterInvalidMinCountParameters


The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| minFilesCount | minFilesCount | int | TypedDict key required | No additional field description in SDK source. |

```python
class FileAtLeastCountFilterInvalidMinCountParameters(typing_extensions.TypedDict):
    """The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    minFilesCount: int
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileAtLeastCountFilterInvalidMinCountParameters.md)

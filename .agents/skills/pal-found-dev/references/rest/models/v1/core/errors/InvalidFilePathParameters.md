# foundry_sdk.v1.core.errors.InvalidFilePathParameters


The provided file path is not valid.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| filePath | filePath | core_models.FilePath | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidFilePathParameters(typing_extensions.TypedDict):
    """The provided file path is not valid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    filePath: core_models.FilePath
```

## Referenced definitions

- [foundry_sdk.v1.core.models.FilePath](../models/FilePath.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidFilePathParameters.md)

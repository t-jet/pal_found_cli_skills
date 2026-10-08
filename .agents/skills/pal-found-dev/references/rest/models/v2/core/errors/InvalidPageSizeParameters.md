# foundry_sdk.v2.core.errors.InvalidPageSizeParameters


The provided page size was zero or negative. Page sizes must be greater than zero.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| pageSize | pageSize | core_models.PageSize | TypedDict key required | The page size to use for the endpoint. |

```python
class InvalidPageSizeParameters(typing_extensions.TypedDict):
    """The provided page size was zero or negative. Page sizes must be greater than zero."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageSize: core_models.PageSize
    """The page size to use for the endpoint."""
```

## Referenced definitions

- [foundry_sdk.v2.core.models.PageSize](../models/PageSize.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidPageSizeParameters.md)

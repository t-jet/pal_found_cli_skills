# foundry_sdk.v2.connectivity.errors.FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters


The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever
satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| gt | gt | core_models.SizeBytes | TypedDict key required | No additional field description in SDK source. |
| lt | lt | core_models.SizeBytes | TypedDict key required | No additional field description in SDK source. |

```python
class FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters(typing_extensions.TypedDict):
    """
    The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever
    satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    gt: core_models.SizeBytes
    lt: core_models.SizeBytes
```

## Referenced definitions

- [foundry_sdk.v2.core.models.SizeBytes](../../core/models/SizeBytes.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters.md)

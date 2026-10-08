# foundry_sdk.v1.datasets.errors.CreateTransactionPermissionDeniedParameters


The provided token does not have permission to create a transaction on this dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | datasets_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| branchId | branchId | datasets_models.BranchId | TypedDict key required | No additional field description in SDK source. |

```python
class CreateTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to create a transaction on this dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchId: datasets_models.BranchId
```

## Referenced definitions

- [foundry_sdk.v1.datasets.models.BranchId](../models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateTransactionPermissionDeniedParameters.md)

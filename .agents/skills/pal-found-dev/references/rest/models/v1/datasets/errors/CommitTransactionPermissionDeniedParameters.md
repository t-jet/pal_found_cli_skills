# foundry_sdk.v1.datasets.errors.CommitTransactionPermissionDeniedParameters


The provided token does not have permission to commit the given transaction on the given dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | datasets_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| transactionRid | transactionRid | datasets_models.TransactionRid | TypedDict key required | No additional field description in SDK source. |

```python
class CommitTransactionPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to commit the given transaction on the given dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
```

## Referenced definitions

- [foundry_sdk.v1.datasets.models.DatasetRid](../models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../models/TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CommitTransactionPermissionDeniedParameters.md)

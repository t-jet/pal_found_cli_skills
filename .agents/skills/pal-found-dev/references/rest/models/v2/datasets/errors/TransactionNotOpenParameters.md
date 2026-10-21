# foundry_sdk.v2.datasets.errors.TransactionNotOpenParameters


The given transaction is not open.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | core_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| transactionRid | transactionRid | datasets_models.TransactionRid | TypedDict key required | No additional field description in SDK source. |
| transactionStatus | transactionStatus | datasets_models.TransactionStatus | TypedDict key required | No additional field description in SDK source. |

```python
class TransactionNotOpenParameters(typing_extensions.TypedDict):
    """The given transaction is not open."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: core_models.DatasetRid
    transactionRid: datasets_models.TransactionRid
    transactionStatus: datasets_models.TransactionStatus
```

## Referenced definitions

- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../models/TransactionRid.md)
- [foundry_sdk.v2.datasets.models.TransactionStatus](../models/TransactionStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TransactionNotOpenParameters.md)

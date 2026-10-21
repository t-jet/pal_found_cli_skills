# foundry_sdk.v1.datasets.errors.FileNotFoundOnTransactionRangeParameters


The requested file could not be found on the given transaction range, or the client token does not have access to it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | datasets_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| startTransactionRid | startTransactionRid | typing_extensions.NotRequired[datasets_models.TransactionRid] | TypedDict key may be omitted | No additional field description in SDK source. |
| endTransactionRid | endTransactionRid | datasets_models.TransactionRid | TypedDict key required | No additional field description in SDK source. |
| path | path | core_models.FilePath | TypedDict key required | No additional field description in SDK source. |

```python
class FileNotFoundOnTransactionRangeParameters(typing_extensions.TypedDict):
    """The requested file could not be found on the given transaction range, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    startTransactionRid: typing_extensions.NotRequired[datasets_models.TransactionRid]
    endTransactionRid: datasets_models.TransactionRid
    path: core_models.FilePath
```

## Referenced definitions

- [foundry_sdk.v1.core.models.FilePath](../../core/models/FilePath.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../models/TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileNotFoundOnTransactionRangeParameters.md)

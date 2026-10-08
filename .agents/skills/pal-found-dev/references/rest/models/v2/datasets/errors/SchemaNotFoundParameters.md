# foundry_sdk.v2.datasets.errors.SchemaNotFoundParameters


A schema could not be found for the given dataset and branch, or the client token does not have access to it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | core_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| branchName | branchName | core_models.BranchName | TypedDict key required | No additional field description in SDK source. |
| transactionRid | transactionRid | typing_extensions.NotRequired[datasets_models.TransactionRid] | TypedDict key may be omitted | No additional field description in SDK source. |

```python
class SchemaNotFoundParameters(typing_extensions.TypedDict):
    """A schema could not be found for the given dataset and branch, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: core_models.DatasetRid
    branchName: core_models.BranchName
    transactionRid: typing_extensions.NotRequired[datasets_models.TransactionRid]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../models/TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SchemaNotFoundParameters.md)

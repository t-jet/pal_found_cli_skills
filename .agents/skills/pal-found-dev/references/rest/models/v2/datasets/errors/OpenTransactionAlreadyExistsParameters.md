# foundry_sdk.v2.datasets.errors.OpenTransactionAlreadyExistsParameters


A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | core_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| branchName | branchName | core_models.BranchName | TypedDict key required | No additional field description in SDK source. |

```python
class OpenTransactionAlreadyExistsParameters(typing_extensions.TypedDict):
    """A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: core_models.DatasetRid
    branchName: core_models.BranchName
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OpenTransactionAlreadyExistsParameters.md)

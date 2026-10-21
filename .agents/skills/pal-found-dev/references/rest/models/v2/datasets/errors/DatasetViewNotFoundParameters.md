# foundry_sdk.v2.datasets.errors.DatasetViewNotFoundParameters


The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset
for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not
exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | core_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| branch | branch | core_models.BranchName | TypedDict key required | No additional field description in SDK source. |

```python
class DatasetViewNotFoundParameters(typing_extensions.TypedDict):
    """
    The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset
    for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not
    exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: core_models.DatasetRid
    branch: core_models.BranchName
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DatasetViewNotFoundParameters.md)

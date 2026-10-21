# foundry_sdk.v2.streams.errors.InvalidStreamNoSchemaParameters


The requested stream exists but is invalid, as it does not have a schema.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| datasetRid | datasetRid | core_models.DatasetRid | TypedDict key required | No additional field description in SDK source. |
| branchName | branchName | core_models.BranchName | TypedDict key required | No additional field description in SDK source. |
| viewRid | viewRid | typing_extensions.NotRequired[streams_models.ViewRid] | TypedDict key may be omitted | No additional field description in SDK source. |

```python
class InvalidStreamNoSchemaParameters(typing_extensions.TypedDict):
    """The requested stream exists but is invalid, as it does not have a schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: core_models.DatasetRid
    branchName: core_models.BranchName
    viewRid: typing_extensions.NotRequired[streams_models.ViewRid]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.streams.models.ViewRid](../models/ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidStreamNoSchemaParameters.md)

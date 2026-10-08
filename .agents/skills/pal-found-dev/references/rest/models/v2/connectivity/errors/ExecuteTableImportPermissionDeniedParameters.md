# foundry_sdk.v2.connectivity.errors.ExecuteTableImportPermissionDeniedParameters


Could not execute the TableImport.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| tableImportRid | tableImportRid | connectivity_models.TableImportRid | TypedDict key required | No additional field description in SDK source. |
| connectionRid | connectionRid | connectivity_models.ConnectionRid | TypedDict key required | No additional field description in SDK source. |

```python
class ExecuteTableImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the TableImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportRid: connectivity_models.TableImportRid
    connectionRid: connectivity_models.ConnectionRid
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.ConnectionRid](../models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.TableImportRid](../models/TableImportRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteTableImportPermissionDeniedParameters.md)

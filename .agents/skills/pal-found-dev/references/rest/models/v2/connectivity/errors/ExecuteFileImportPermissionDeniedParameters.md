# foundry_sdk.v2.connectivity.errors.ExecuteFileImportPermissionDeniedParameters


Could not execute the FileImport.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| fileImportRid | fileImportRid | connectivity_models.FileImportRid | TypedDict key required | No additional field description in SDK source. |
| connectionRid | connectionRid | connectivity_models.ConnectionRid | TypedDict key required | No additional field description in SDK source. |

```python
class ExecuteFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.ConnectionRid](../models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.FileImportRid](../models/FileImportRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteFileImportPermissionDeniedParameters.md)

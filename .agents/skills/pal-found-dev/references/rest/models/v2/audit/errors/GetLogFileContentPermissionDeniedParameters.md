# foundry_sdk.v2.audit.errors.GetLogFileContentPermissionDeniedParameters


Could not content the LogFile.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| organizationRid | organizationRid | core_models.OrganizationRid | TypedDict key required | No additional field description in SDK source. |
| logFileId | logFileId | audit_models.FileId | TypedDict key required | No additional field description in SDK source. |

```python
class GetLogFileContentPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not content the LogFile."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRid: core_models.OrganizationRid
    logFileId: audit_models.FileId
```

## Referenced definitions

- [foundry_sdk.v2.audit.models.FileId](../models/FileId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetLogFileContentPermissionDeniedParameters.md)

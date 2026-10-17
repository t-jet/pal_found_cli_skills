# foundry_sdk.v2.admin.errors.ListGroupMembersPermissionDeniedParameters


The provided token does not have permission to view the members of the given group.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| groupId | groupId | core_models.GroupId | TypedDict key required | No additional field description in SDK source. |

```python
class ListGroupMembersPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to view the members of the given group."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.GroupId
```

## Referenced definitions

- [foundry_sdk.v2.core.models.GroupId](../../core/models/GroupId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ListGroupMembersPermissionDeniedParameters.md)

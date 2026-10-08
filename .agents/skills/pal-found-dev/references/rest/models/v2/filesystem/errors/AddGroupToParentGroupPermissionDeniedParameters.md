# foundry_sdk.v2.filesystem.errors.AddGroupToParentGroupPermissionDeniedParameters


The user is not authorized to add a a group to the parent group required to create the project from template.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parentGroupsWithoutPermission | parentGroupsWithoutPermission | typing.List[core_models.GroupRid] | TypedDict key required | No additional field description in SDK source. |

```python
class AddGroupToParentGroupPermissionDeniedParameters(typing_extensions.TypedDict):
    """The user is not authorized to add a a group to the parent group required to create the project from template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentGroupsWithoutPermission: typing.List[core_models.GroupRid]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.GroupRid](../../core/models/GroupRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AddGroupToParentGroupPermissionDeniedParameters.md)

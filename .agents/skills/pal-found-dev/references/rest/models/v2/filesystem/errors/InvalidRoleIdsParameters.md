# foundry_sdk.v2.filesystem.errors.InvalidRoleIdsParameters


A roleId referenced in either default roles or role grants does not exist in the project role set for the space.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| requestedRoleIds | requestedRoleIds | typing.List[core_models.RoleId] | TypedDict key required | All referenced role ids in the create project request. |

```python
class InvalidRoleIdsParameters(typing_extensions.TypedDict):
    """A roleId referenced in either default roles or role grants does not exist in the project role set for the space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestedRoleIds: typing.List[core_models.RoleId]
    """All referenced role ids in the create project request."""
```

## Referenced definitions

- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidRoleIdsParameters.md)

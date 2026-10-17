# foundry_sdk.v2.filesystem.errors.CreateProjectNoOwnerLikeRoleGrantParameters


The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| grantedRoleIds | grantedRoleIds | typing.List[core_models.RoleId] | TypedDict key required | No additional field description in SDK source. |
| roleSetOwnerLikeRoleIds | roleSetOwnerLikeRoleIds | typing.List[core_models.RoleId] | TypedDict key required | No additional field description in SDK source. |

```python
class CreateProjectNoOwnerLikeRoleGrantParameters(typing_extensions.TypedDict):
    """The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    grantedRoleIds: typing.List[core_models.RoleId]
    roleSetOwnerLikeRoleIds: typing.List[core_models.RoleId]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateProjectNoOwnerLikeRoleGrantParameters.md)

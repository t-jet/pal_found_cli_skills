# foundry_sdk.v2.admin.models.Role


Role

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | core_models.RoleId | required; no default | No additional field description in SDK source. |
| display_name | displayName | RoleDisplayName | required; no default | No additional field description in SDK source. |
| description | description | RoleDescription | required; no default | No additional field description in SDK source. |
| operations | operations | typing.List[str] | required; no default | A list of permissions that this role has. |
| can_assigns | canAssigns | typing.List[core_models.RoleId] | required; no default | A list of roles that this role inherits. |

```python
class Role(core.ModelBase):
    """Role"""

    id: core_models.RoleId
    display_name: RoleDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: RoleDescription
    operations: typing.List[str]
    """A list of permissions that this role has."""

    can_assigns: typing.List[core_models.RoleId] = pydantic.Field(alias=str("canAssigns"))  # type: ignore[literal-required]
    """A list of roles that this role inherits."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.RoleDescription](RoleDescription.md)
- [foundry_sdk.v2.admin.models.RoleDisplayName](RoleDisplayName.md)
- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Role.md)

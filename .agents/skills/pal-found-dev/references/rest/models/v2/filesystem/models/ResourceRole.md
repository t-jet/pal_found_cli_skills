# foundry_sdk.v2.filesystem.models.ResourceRole


ResourceRole

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resource_role_principal | resourceRolePrincipal | ResourceRolePrincipal | required; no default | No additional field description in SDK source. |
| role_id | roleId | core_models.RoleId | required; no default | No additional field description in SDK source. |

```python
class ResourceRole(core.ModelBase):
    """ResourceRole"""

    resource_role_principal: ResourceRolePrincipal = pydantic.Field(alias=str("resourceRolePrincipal"))  # type: ignore[literal-required]
    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)
- [foundry_sdk.v2.filesystem.models.ResourceRolePrincipal](ResourceRolePrincipal.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResourceRole.md)

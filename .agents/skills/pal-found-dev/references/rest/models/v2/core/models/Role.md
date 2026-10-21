# foundry_sdk.v2.core.models.Role


A set of permissions that can be assigned to a principal for a specific resource type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | RoleId | required; no default | No additional field description in SDK source. |
| role_set_id | roleSetId | RoleSetId | required; no default | No additional field description in SDK source. |
| name | name | str | required; no default | No additional field description in SDK source. |
| description | description | str | required; no default | No additional field description in SDK source. |
| is_default | isDefault | bool | required; no default | Default roles are provided by Palantir and cannot be edited or modified by administrators. |
| type | type | RoleContext | required; no default | The type of resource that is valid for this role. |
| operations | operations | typing.List[Operation] | required; no default | The operations that a principal can perform with this role on the assigned resource. |

```python
class Role(core.ModelBase):
    """A set of permissions that can be assigned to a principal for a specific resource type."""

    id: RoleId
    role_set_id: RoleSetId = pydantic.Field(alias=str("roleSetId"))  # type: ignore[literal-required]
    name: str
    description: str
    is_default: bool = pydantic.Field(alias=str("isDefault"))  # type: ignore[literal-required]
    """Default roles are provided by Palantir and cannot be edited or modified by administrators."""

    type: RoleContext
    """The type of resource that is valid for this role."""

    operations: typing.List[Operation]
    """The operations that a principal can perform with this role on the assigned resource."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.Operation](Operation.md)
- [foundry_sdk.v2.core.models.RoleContext](RoleContext.md)
- [foundry_sdk.v2.core.models.RoleId](RoleId.md)
- [foundry_sdk.v2.core.models.RoleSetId](RoleSetId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Role.md)

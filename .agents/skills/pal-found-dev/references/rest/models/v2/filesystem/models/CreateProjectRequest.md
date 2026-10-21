# foundry_sdk.v2.filesystem.models.CreateProjectRequest


CreateProjectRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | ResourceDisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| space_rid | spaceRid | SpaceRid | required; no default | No additional field description in SDK source. |
| role_grants | roleGrants | typing.Dict[core_models.RoleId, typing.List[PrincipalWithId]] | required; no default | No additional field description in SDK source. |
| default_roles | defaultRoles | typing.List[core_models.RoleId] | required; no default | No additional field description in SDK source. |
| organization_rids | organizationRids | typing.List[core_models.OrganizationRid] | required; no default | No additional field description in SDK source. |
| resource_level_role_grants_allowed | resourceLevelRoleGrantsAllowed | typing.Optional[bool] | default None | Whether role grants should be allowed on individual resources within the Project.<br>    When not specified, defaults to true. |

```python
class CreateProjectRequest(core.ModelBase):
    """CreateProjectRequest"""

    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    role_grants: typing.Dict[core_models.RoleId, typing.List[PrincipalWithId]] = pydantic.Field(alias=str("roleGrants"))  # type: ignore[literal-required]
    default_roles: typing.List[core_models.RoleId] = pydantic.Field(alias=str("defaultRoles"))  # type: ignore[literal-required]
    organization_rids: typing.List[core_models.OrganizationRid] = pydantic.Field(alias=str("organizationRids"))  # type: ignore[literal-required]
    resource_level_role_grants_allowed: typing.Optional[bool] = pydantic.Field(alias=str("resourceLevelRoleGrantsAllowed"), default=None)  # type: ignore[literal-required]
    """
    Whether role grants should be allowed on individual resources within the Project.
    When not specified, defaults to true.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)
- [foundry_sdk.v2.filesystem.models.PrincipalWithId](PrincipalWithId.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](SpaceRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateProjectRequest.md)

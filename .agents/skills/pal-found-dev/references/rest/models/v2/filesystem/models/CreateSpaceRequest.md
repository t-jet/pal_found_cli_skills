# foundry_sdk.v2.filesystem.models.CreateSpaceRequest


CreateSpaceRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| enrollment_rid | enrollmentRid | core_models.EnrollmentRid | required; no default | The RID of the Enrollment that this Space belongs to. |
| usage_account_rid | usageAccountRid | typing.Optional[UsageAccountRid] | default None | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
| file_system_id | fileSystemId | typing.Optional[FileSystemId] | default None | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used. |
| display_name | displayName | ResourceDisplayName | required; no default | No additional field description in SDK source. |
| organizations | organizations | typing.List[core_models.OrganizationRid] | required; no default | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations. |
| description | description | typing.Optional[str] | None | The description of the Space. |
| deletion_policy_organizations | deletionPolicyOrganizations | typing.List[core_models.OrganizationRid] | required; no default | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here. |
| default_role_set_id | defaultRoleSetId | typing.Optional[core_models.RoleSetId] | default None | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used. |

```python
class CreateSpaceRequest(core.ModelBase):
    """CreateSpaceRequest"""

    enrollment_rid: core_models.EnrollmentRid = pydantic.Field(alias=str("enrollmentRid"))  # type: ignore[literal-required]
    """The RID of the Enrollment that this Space belongs to."""

    usage_account_rid: typing.Optional[UsageAccountRid] = pydantic.Field(alias=str("usageAccountRid"), default=None)  # type: ignore[literal-required]
    """The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used."""

    file_system_id: typing.Optional[FileSystemId] = pydantic.Field(alias=str("fileSystemId"), default=None)  # type: ignore[literal-required]
    """The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used."""

    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    organizations: typing.List[core_models.OrganizationRid]
    """The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations."""

    description: typing.Optional[str] = None
    """The description of the Space."""

    deletion_policy_organizations: typing.List[core_models.OrganizationRid] = pydantic.Field(alias=str("deletionPolicyOrganizations"))  # type: ignore[literal-required]
    """By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here."""

    default_role_set_id: typing.Optional[core_models.RoleSetId] = pydantic.Field(alias=str("defaultRoleSetId"), default=None)  # type: ignore[literal-required]
    """The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.RoleSetId](../../core/models/RoleSetId.md)
- [foundry_sdk.v2.filesystem.models.FileSystemId](FileSystemId.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.UsageAccountRid](UsageAccountRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateSpaceRequest.md)

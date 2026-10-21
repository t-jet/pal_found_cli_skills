# foundry_sdk.v2.admin.models.MarkingCategoryPermissions


MarkingCategoryPermissions

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| organization_rids | organizationRids | typing.List[core_models.OrganizationRid] | required; no default | Users must be members of at least one of the Organizations in this list to view Markings in the category, regardless of their assigned roles. |
| roles | roles | typing.List[MarkingCategoryRoleAssignment] | required; no default | No additional field description in SDK source. |
| is_public | isPublic | MarkingCategoryPermissionsIsPublic | required; no default | If true, all users who are members of at least one of the Organizations from organizationRids can view the Markings in the category. If false, only users who are explicitly granted the VIEW role can view the Markings in the category. |

```python
class MarkingCategoryPermissions(core.ModelBase):
    """MarkingCategoryPermissions"""

    organization_rids: typing.List[core_models.OrganizationRid] = pydantic.Field(alias=str("organizationRids"))  # type: ignore[literal-required]
    """Users must be members of at least one of the Organizations in this list to view Markings in the category, regardless of their assigned roles."""

    roles: typing.List[MarkingCategoryRoleAssignment]
    is_public: MarkingCategoryPermissionsIsPublic = pydantic.Field(alias=str("isPublic"))  # type: ignore[literal-required]
    """If true, all users who are members of at least one of the Organizations from organizationRids can view the Markings in the category. If false, only users who are explicitly granted the VIEW role can view the Markings in the category."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryPermissionsIsPublic](MarkingCategoryPermissionsIsPublic.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryRoleAssignment](MarkingCategoryRoleAssignment.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingCategoryPermissions.md)

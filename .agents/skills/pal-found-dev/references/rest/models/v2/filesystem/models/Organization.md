# foundry_sdk.v2.filesystem.models.Organization


An Organization is an access requirement on a Project. Each user belongs to one Organization and may be a guest member of several. To meet a Project's access requirements, the user must belong to or be a guest member of at least one Organization applied to that Project. Organizations are inherited through the file hierarchy and direct dependencies. `organization_rid` identifies the Organization; `is_directly_applied` records direct application.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| marking_id | markingId | core_models.MarkingId | required; no default | No additional field description in SDK source. |
| organization_rid | organizationRid | core_models.OrganizationRid | required; no default | No additional field description in SDK source. |
| is_directly_applied | isDirectlyApplied | IsDirectlyApplied | required; no default | No additional field description in SDK source. |

```python
class Organization(core.ModelBase):
    """
    [Organizations](https://palantir.com/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to
    Projects that enforce strict silos between groups of users and resources. Every user is a member of only
    one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements,
    users must be a member or guest member of at least one Organization applied to a Project.
    Organizations are inherited via the file hierarchy and direct dependencies.
    """

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    organization_rid: core_models.OrganizationRid = pydantic.Field(alias=str("organizationRid"))  # type: ignore[literal-required]
    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias=str("isDirectlyApplied"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.filesystem.models.IsDirectlyApplied](IsDirectlyApplied.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Organization.md)

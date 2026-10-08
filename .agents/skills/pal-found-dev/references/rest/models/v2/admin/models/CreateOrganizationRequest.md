# foundry_sdk.v2.admin.models.CreateOrganizationRequest


CreateOrganizationRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| administrators | administrators | typing.List[core_models.PrincipalId] | required; no default | The initial administrators of the Organization. At least one principal must be provided. |
| enrollment_rid | enrollmentRid | core_models.EnrollmentRid | required; no default | The RID of the Enrollment that this Organization belongs to. This must be provided. |
| name | name | OrganizationName | required; no default | No additional field description in SDK source. |
| host | host | typing.Optional[HostName] | None | The primary host name of the Organization. This should be used when constructing URLs for users of this<br>    Organization. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |

```python
class CreateOrganizationRequest(core.ModelBase):
    """CreateOrganizationRequest"""

    administrators: typing.List[core_models.PrincipalId]
    """The initial administrators of the Organization. At least one principal must be provided."""

    enrollment_rid: core_models.EnrollmentRid = pydantic.Field(alias=str("enrollmentRid"))  # type: ignore[literal-required]
    """The RID of the Enrollment that this Organization belongs to. This must be provided."""

    name: OrganizationName
    host: typing.Optional[HostName] = None
    """
    The primary host name of the Organization. This should be used when constructing URLs for users of this
    Organization.
    """

    description: typing.Optional[str] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.HostName](HostName.md)
- [foundry_sdk.v2.admin.models.OrganizationName](OrganizationName.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../core/models/PrincipalId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateOrganizationRequest.md)

# foundry_sdk.v2.admin.errors.OrganizationMarkingAdministerRoleNotSupportedParameters


The ADMINISTER role on Organization markings cannot be managed through the Marking Role Assignments
endpoints. To manage administrator roles for an Organization, use the Organization Role Assignment endpoints
instead.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| markingId | markingId | core_models.MarkingId | TypedDict key required | No additional field description in SDK source. |
| organizationRid | organizationRid | core_models.OrganizationRid | TypedDict key required | No additional field description in SDK source. |

```python
class OrganizationMarkingAdministerRoleNotSupportedParameters(typing_extensions.TypedDict):
    """
    The ADMINISTER role on Organization markings cannot be managed through the Marking Role Assignments
    endpoints. To manage administrator roles for an Organization, use the Organization Role Assignment endpoints
    instead.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId
    organizationRid: core_models.OrganizationRid
```

## Referenced definitions

- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OrganizationMarkingAdministerRoleNotSupportedParameters.md)

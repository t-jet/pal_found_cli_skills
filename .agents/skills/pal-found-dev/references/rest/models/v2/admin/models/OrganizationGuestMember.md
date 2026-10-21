# foundry_sdk.v2.admin.models.OrganizationGuestMember


OrganizationGuestMember

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| principal_type | principalType | core_models.PrincipalType | required; no default | No additional field description in SDK source. |
| principal_id | principalId | core_models.PrincipalId | required; no default | No additional field description in SDK source. |

```python
class OrganizationGuestMember(core.ModelBase):
    """OrganizationGuestMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../core/models/PrincipalType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OrganizationGuestMember.md)

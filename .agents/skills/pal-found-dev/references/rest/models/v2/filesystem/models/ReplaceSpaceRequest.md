# foundry_sdk.v2.filesystem.models.ReplaceSpaceRequest


ReplaceSpaceRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| usage_account_rid | usageAccountRid | typing.Optional[UsageAccountRid] | default None | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
| display_name | displayName | ResourceDisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the Space. |
| default_role_set_id | defaultRoleSetId | typing.Optional[core_models.RoleSetId] | default None | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used. |

```python
class ReplaceSpaceRequest(core.ModelBase):
    """ReplaceSpaceRequest"""

    usage_account_rid: typing.Optional[UsageAccountRid] = pydantic.Field(alias=str("usageAccountRid"), default=None)  # type: ignore[literal-required]
    """The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used."""

    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the Space."""

    default_role_set_id: typing.Optional[core_models.RoleSetId] = pydantic.Field(alias=str("defaultRoleSetId"), default=None)  # type: ignore[literal-required]
    """The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.RoleSetId](../../core/models/RoleSetId.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.UsageAccountRid](UsageAccountRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceSpaceRequest.md)

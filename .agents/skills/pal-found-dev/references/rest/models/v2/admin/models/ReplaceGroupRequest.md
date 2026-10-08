# foundry_sdk.v2.admin.models.ReplaceGroupRequest


ReplaceGroupRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | GroupName | required; no default | The name of the Group. |
| organizations | organizations | typing.List[core_models.OrganizationRid] | required; no default | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed. |
| description | description | typing.Optional[str] | None | A description of the Group. |
| attributes | attributes | typing.Dict[AttributeName, AttributeValues] | required; no default | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |

```python
class ReplaceGroupRequest(core.ModelBase):
    """ReplaceGroupRequest"""

    name: GroupName
    """The name of the Group."""

    organizations: typing.List[core_models.OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    description: typing.Optional[str] = None
    """A description of the Group."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.AttributeName](AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValues](AttributeValues.md)
- [foundry_sdk.v2.admin.models.GroupName](GroupName.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceGroupRequest.md)

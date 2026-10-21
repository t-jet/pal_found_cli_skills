# foundry_sdk.v2.admin.models.ReplaceOrganizationRequest


ReplaceOrganizationRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | OrganizationName | required; no default | No additional field description in SDK source. |
| host | host | typing.Optional[HostName] | None | The primary host name of the Organization. This should be used when constructing URLs for users of this<br>    Organization. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |

```python
class ReplaceOrganizationRequest(core.ModelBase):
    """ReplaceOrganizationRequest"""

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

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceOrganizationRequest.md)

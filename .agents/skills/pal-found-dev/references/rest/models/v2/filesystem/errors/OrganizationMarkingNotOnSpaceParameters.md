# foundry_sdk.v2.filesystem.errors.OrganizationMarkingNotOnSpaceParameters


At least one of the organization markings associated with a passed organization is not applied on the requested space.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| spaceRid | spaceRid | filesystem_models.SpaceRid | TypedDict key required | No additional field description in SDK source. |
| organizationRids | organizationRids | typing.List[core_models.OrganizationRid] | TypedDict key required | No additional field description in SDK source. |

```python
class OrganizationMarkingNotOnSpaceParameters(typing_extensions.TypedDict):
    """At least one of the organization markings associated with a passed organization is not applied on the requested space."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    spaceRid: filesystem_models.SpaceRid
    organizationRids: typing.List[core_models.OrganizationRid]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../models/SpaceRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OrganizationMarkingNotOnSpaceParameters.md)

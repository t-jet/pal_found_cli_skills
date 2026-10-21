# foundry_sdk.v2.filesystem.errors.InvalidOrganizationHierarchyParameters


Organizations on a project must also exist on the parent space. This error is thrown if the configuration
of a project's organizations (on creation or subsequently) results in the project being marked with either
no organizations in a marked space, or with an organization that is not present on the parent space.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| organizationRids | organizationRids | typing.List[core_models.OrganizationRid] | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidOrganizationHierarchyParameters(typing_extensions.TypedDict):
    """
    Organizations on a project must also exist on the parent space. This error is thrown if the configuration
    of a project's organizations (on creation or subsequently) results in the project being marked with either
    no organizations in a marked space, or with an organization that is not present on the parent space.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizationRids: typing.List[core_models.OrganizationRid]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidOrganizationHierarchyParameters.md)

# foundry_sdk.v2.admin.models.PreregisterUserRequest


PreregisterUserRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| username | username | UserUsername | required; no default | The new user's username. This must match one of the provider's supported username patterns. |
| organization | organization | core_models.OrganizationRid | required; no default | The RID of the user's primary Organization. This may be changed when the user logs in for the first<br>    time depending on any configured Organization assignment rules. |
| given_name | givenName | typing.Optional[str] | default None | No additional field description in SDK source. |
| family_name | familyName | typing.Optional[str] | default None | No additional field description in SDK source. |
| email | email | typing.Optional[str] | None | No additional field description in SDK source. |
| attributes | attributes | typing.Optional[typing.Dict[AttributeName, AttributeValues]] | None | No additional field description in SDK source. |

```python
class PreregisterUserRequest(core.ModelBase):
    """PreregisterUserRequest"""

    username: UserUsername
    """The new user's username. This must match one of the provider's supported username patterns."""

    organization: core_models.OrganizationRid
    """
    The RID of the user's primary Organization. This may be changed when the user logs in for the first
    time depending on any configured Organization assignment rules.
    """

    given_name: typing.Optional[str] = pydantic.Field(alias=str("givenName"), default=None)  # type: ignore[literal-required]
    family_name: typing.Optional[str] = pydantic.Field(alias=str("familyName"), default=None)  # type: ignore[literal-required]
    email: typing.Optional[str] = None
    attributes: typing.Optional[typing.Dict[AttributeName, AttributeValues]] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.AttributeName](AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValues](AttributeValues.md)
- [foundry_sdk.v2.admin.models.UserUsername](UserUsername.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PreregisterUserRequest.md)

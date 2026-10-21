# foundry_sdk.v2.admin.models.User


User

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | core_models.UserId | required; no default | No additional field description in SDK source. |
| username | username | UserUsername | required; no default | The Foundry username of the User. This is unique within the realm. |
| given_name | givenName | typing.Optional[str] | default None | The given name of the User. |
| family_name | familyName | typing.Optional[str] | default None | The family name (last name) of the User. |
| email | email | typing.Optional[str] | None | The email at which to contact a User. Multiple users may have the same email address. |
| realm | realm | core_models.Realm | required; no default | No additional field description in SDK source. |
| organization | organization | typing.Optional[core_models.OrganizationRid] | None | The RID of the user's primary Organization. This will be blank for third-party application service users. |
| status | status | core_models.UserStatus | required; no default | The current status of the user. |
| attributes | attributes | typing.Dict[AttributeName, AttributeValues] | required; no default | A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by<br>    Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in <br>    Control Panel and populated by the User's SSO provider upon login. |

```python
class User(core.ModelBase):
    """User"""

    id: core_models.UserId
    username: UserUsername
    """The Foundry username of the User. This is unique within the realm."""

    given_name: typing.Optional[str] = pydantic.Field(alias=str("givenName"), default=None)  # type: ignore[literal-required]
    """The given name of the User."""

    family_name: typing.Optional[str] = pydantic.Field(alias=str("familyName"), default=None)  # type: ignore[literal-required]
    """The family name (last name) of the User."""

    email: typing.Optional[str] = None
    """The email at which to contact a User. Multiple users may have the same email address."""

    realm: core_models.Realm
    organization: typing.Optional[core_models.OrganizationRid] = None
    """The RID of the user's primary Organization. This will be blank for third-party application service users."""

    status: core_models.UserStatus
    """The current status of the user."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """
    A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by
    Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in 
    Control Panel and populated by the User's SSO provider upon login.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.AttributeName](AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValues](AttributeValues.md)
- [foundry_sdk.v2.admin.models.UserUsername](UserUsername.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.Realm](../../core/models/Realm.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)
- [foundry_sdk.v2.core.models.UserStatus](../../core/models/UserStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](User.md)

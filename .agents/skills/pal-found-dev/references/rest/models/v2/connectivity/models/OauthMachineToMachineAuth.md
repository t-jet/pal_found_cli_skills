# foundry_sdk.v2.connectivity.models.OauthMachineToMachineAuth


Authenticate as a service principal using OAuth. Create a service principal in Databricks and generate an OAuth secret to obtain a client ID and secret.
Read the [official Databricks documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) for more information about OAuth machine-to-machine
authentication.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| client_id | clientID | str | required; no default | The client ID for the service principal. |
| client_secret | clientSecret | EncryptedProperty | required; no default | The value of the client secret. |
| type | type | typing.Literal['oauthM2M'] | 'oauthM2M' | No additional field description in SDK source. |

```python
class OauthMachineToMachineAuth(core.ModelBase):
    """
    Authenticate as a service principal using OAuth. Create a service principal in Databricks and generate an OAuth secret to obtain a client ID and secret.
    Read the [official Databricks documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) for more information about OAuth machine-to-machine
    authentication.
    """

    client_id: str = pydantic.Field(alias=str("clientID"))  # type: ignore[literal-required]
    """The client ID for the service principal."""

    client_secret: EncryptedProperty = pydantic.Field(alias=str("clientSecret"))  # type: ignore[literal-required]
    """The value of the client secret."""

    type: typing.Literal["oauthM2M"] = "oauthM2M"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OauthMachineToMachineAuth.md)

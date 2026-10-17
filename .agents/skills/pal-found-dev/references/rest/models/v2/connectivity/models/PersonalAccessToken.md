# foundry_sdk.v2.connectivity.models.PersonalAccessToken


Supply a Databricks personal access token already issued to the intended user or service principal as an `EncryptedProperty`. Keep its owner, expiry and workspace permissions aligned with the Connection. This model cannot generate or renew the external token.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| personal_access_token | personalAccessToken | EncryptedProperty | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['personalAccessToken'] | 'personalAccessToken' | No additional field description in SDK source. |

```python
class PersonalAccessToken(core.ModelBase):
    """
    Authenticate as a user or service principal using a personal access token.
    Read the [official Databricks documentation](https://docs.databricks.com/aws/en/dev-tools/auth/pat) for information on generating a personal access token.
    """

    personal_access_token: EncryptedProperty = pydantic.Field(alias=str("personalAccessToken"))  # type: ignore[literal-required]
    type: typing.Literal["personalAccessToken"] = "personalAccessToken"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PersonalAccessToken.md)

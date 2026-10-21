# foundry_sdk.v2.connectivity.models.SnowflakeExternalOauth


External OAuth uses an authorization server trusted by Snowflake. Configure a Snowflake External OAuth security integration before using this connection. Its issuer and audience must match the token's `iss` and `aud` claims; `subject` is the Foundry Connection RID. The authorization server and Snowflake integration must agree on token signature validation, user mapping and authorized scopes. A malformed or unmatched token cannot be repaired by changing the Connection RID. The SDK model stores identifiers, not an access token or the Snowflake integration itself.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| audience | audience | str | required; no default | Identifies the recipients that the access token is intended for as a string URI. |
| issuer_url | issuerUrl | str | required; no default | Identifies the principal that issued the access token as a string URI. |
| subject | subject | ConnectionRid | required; no default | The RID of the Connection that is connecting to the external system. |
| type | type | typing.Literal['externalOauth'] | 'externalOauth' | No additional field description in SDK source. |

```python
class SnowflakeExternalOauth(core.ModelBase):
    """
    Use an External OAuth security integration to connect and authenticate to Snowflake.

    See https://docs.snowflake.com/en/user-guide/oauth-ext-custom
    """

    audience: str
    """Identifies the recipients that the access token is intended for as a string URI."""

    issuer_url: str = pydantic.Field(alias=str("issuerUrl"))  # type: ignore[literal-required]
    """Identifies the principal that issued the access token as a string URI."""

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: typing.Literal["externalOauth"] = "externalOauth"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](ConnectionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SnowflakeExternalOauth.md)

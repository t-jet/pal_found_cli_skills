# foundry_sdk.v2.connectivity.models.SnowflakeKeyPairAuthentication


Key-pair authentication uses the Snowflake user in `user` and its matching private key in `private_key`. Register the corresponding public key on that Snowflake user first. Supply the private key through the `EncryptedProperty` variant chosen for a write: plaintext is encrypted and stored by Foundry, while an existing secret name retains its encrypted value. Never substitute the public key for this private-key field. If authentication fails, compare user identity and public-key fingerprint with the intended key before rotating or resubmitting a secret.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| user | user | str | required; no default | No additional field description in SDK source. |
| private_key | privateKey | EncryptedProperty | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['keyPair'] | 'keyPair' | No additional field description in SDK source. |

```python
class SnowflakeKeyPairAuthentication(core.ModelBase):
    """
    Use a key-pair to connect and authenticate to Snowflake.

    See https://docs.snowflake.com/en/user-guide/key-pair-auth
    """

    user: str
    private_key: EncryptedProperty = pydantic.Field(alias=str("privateKey"))  # type: ignore[literal-required]
    type: typing.Literal["keyPair"] = "keyPair"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SnowflakeKeyPairAuthentication.md)

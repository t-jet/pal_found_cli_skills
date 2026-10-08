# foundry_sdk.v2.connectivity.models.EncryptedProperty



When reading an encrypted property, the secret name representing the encrypted value will be returned.
When writing to an encrypted property:
- If a plaintext value is passed as an input, the plaintext value will be encrypted and saved to the property.
- If a secret name is passed as an input, the secret name must match the existing secret name of the property
  and the property will retain its previously encrypted value.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
EncryptedProperty: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["AsSecretName", "AsPlaintextValue"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.AsPlaintextValue](AsPlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.AsSecretName](AsSecretName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EncryptedProperty.md)

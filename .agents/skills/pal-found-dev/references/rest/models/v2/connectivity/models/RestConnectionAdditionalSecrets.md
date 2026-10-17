# foundry_sdk.v2.connectivity.models.RestConnectionAdditionalSecrets



When creating or updating additional secrets, use SecretsWithPlaintextValues.
When fetching the RestConnectionConfiguration, SecretsNames will be provided.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
RestConnectionAdditionalSecrets: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SecretsWithPlaintextValues", "SecretsNames"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.SecretsNames](SecretsNames.md)
- [foundry_sdk.v2.connectivity.models.SecretsWithPlaintextValues](SecretsWithPlaintextValues.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RestConnectionAdditionalSecrets.md)

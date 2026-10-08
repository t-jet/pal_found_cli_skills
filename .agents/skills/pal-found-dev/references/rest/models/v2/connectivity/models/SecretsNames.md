# foundry_sdk.v2.connectivity.models.SecretsNames


A list of secret names that can be referenced in code and webhook configurations.
This will be provided to the client when fetching the RestConnectionConfiguration.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| secret_names | secretNames | typing.List[SecretName] | required; no default | The names of the additional secrets that can be referenced in code and webhook configurations. |
| type | type | typing.Literal['asSecretsNames'] | 'asSecretsNames' | No additional field description in SDK source. |

```python
class SecretsNames(core.ModelBase):
    """
    A list of secret names that can be referenced in code and webhook configurations.
    This will be provided to the client when fetching the RestConnectionConfiguration.
    """

    secret_names: typing.List[SecretName] = pydantic.Field(alias=str("secretNames"))  # type: ignore[literal-required]
    """The names of the additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsNames"] = "asSecretsNames"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.SecretName](SecretName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SecretsNames.md)

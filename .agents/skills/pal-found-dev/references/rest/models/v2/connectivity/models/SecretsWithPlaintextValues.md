# foundry_sdk.v2.connectivity.models.SecretsWithPlaintextValues


A map representing secret name to plaintext secret value pairs.
This should be used when creating or updating additional secrets for a REST connection.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| secrets | secrets | typing.Dict[SecretName, PlaintextValue] | required; no default | The additional secrets that can be referenced in code and webhook configurations. |
| type | type | typing.Literal['asSecretsWithPlaintextValues'] | 'asSecretsWithPlaintextValues' | No additional field description in SDK source. |

```python
class SecretsWithPlaintextValues(core.ModelBase):
    """
    A map representing secret name to plaintext secret value pairs.
    This should be used when creating or updating additional secrets for a REST connection.
    """

    secrets: typing.Dict[SecretName, PlaintextValue]
    """The additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsWithPlaintextValues"] = "asSecretsWithPlaintextValues"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.PlaintextValue](PlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.SecretName](SecretName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SecretsWithPlaintextValues.md)

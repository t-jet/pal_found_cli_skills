# foundry_sdk.v2.ontologies.models.EncryptionResult


The result of a CipherText encryption. If successful, the encrypted ciphertext value will be returned. Otherwise, an error will be thrown.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ciphertext | ciphertext | CipherText | required; no default | No additional field description in SDK source. |

```python
class EncryptionResult(core.ModelBase):
    """The result of a CipherText encryption. If successful, the encrypted ciphertext value will be returned. Otherwise, an error will be thrown."""

    ciphertext: CipherText
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.CipherText](CipherText.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EncryptionResult.md)

# foundry_sdk.v1.core.models.CipherTextType


CipherTextType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| default_cipher_channel | defaultCipherChannel | typing.Optional[str] | default None | An optional Cipher Channel RID which can be used for encryption updates to empty values. |
| type | type | typing.Literal['cipherText'] | 'cipherText' | No additional field description in SDK source. |

```python
class CipherTextType(core.ModelBase):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[str] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"] = "cipherText"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CipherTextType.md)

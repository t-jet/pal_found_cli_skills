# foundry_sdk.v2.connectivity.models.BearerToken


The bearer token used to authenticate to the external system.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| bearer_token | bearerToken | EncryptedProperty | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['bearerToken'] | 'bearerToken' | No additional field description in SDK source. |

```python
class BearerToken(core.ModelBase):
    """The bearer token used to authenticate to the external system."""

    bearer_token: EncryptedProperty = pydantic.Field(alias=str("bearerToken"))  # type: ignore[literal-required]
    type: typing.Literal["bearerToken"] = "bearerToken"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BearerToken.md)

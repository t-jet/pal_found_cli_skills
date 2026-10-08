# foundry_sdk.v2.core.models.FieldSchema


The specification of the type of a Foundry schema field.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| nullable | nullable | bool | required; no default | No additional field description in SDK source. |
| custom_metadata | customMetadata | typing.Optional[CustomMetadata] | default None | No additional field description in SDK source. |
| data_type | dataType | FieldDataType | required; no default | No additional field description in SDK source. |

```python
class FieldSchema(core.ModelBase):
    """The specification of the type of a Foundry schema field."""

    nullable: bool
    custom_metadata: typing.Optional[CustomMetadata] = pydantic.Field(alias=str("customMetadata"), default=None)  # type: ignore[literal-required]
    data_type: FieldDataType = pydantic.Field(alias=str("dataType"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CustomMetadata](CustomMetadata.md)
- [foundry_sdk.v2.core.models.FieldDataType](FieldDataType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FieldSchema.md)

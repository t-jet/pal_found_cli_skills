# foundry_sdk.v2.core.models.Field


A Foundry schema field pairs `name` with a `FieldSchema` under wire key `schema`. Use the referenced FieldSchema definition for its supported type and nullability. A field name must match the columns or stream records it describes.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | FieldName | required; no default | No additional field description in SDK source. |
| schema_ | schema | FieldSchema | required; no default | No additional field description in SDK source. |

```python
class Field(core.ModelBase):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](https://palantir.com/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    name: FieldName
    schema_: FieldSchema = pydantic.Field(alias=str("schema"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.FieldName](FieldName.md)
- [foundry_sdk.v2.core.models.FieldSchema](FieldSchema.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Field.md)

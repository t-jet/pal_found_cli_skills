# foundry_sdk.v2.core.models.DatasetFieldSchema


A field in a Foundry dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | SchemaFieldType | required; no default | No additional field description in SDK source. |
| name | name | typing.Optional[FieldName] | None | The name of a column. May be absent in nested schema objects. |
| nullable | nullable | bool | required; no default | Indicates whether values of this field may be null. |
| user_defined_type_class | userDefinedTypeClass | typing.Optional[str] | default None | Canonical classname of the user-defined type for this field. This should be a subclass of Spark's `UserDefinedType`. |
| custom_metadata | customMetadata | typing.Optional[CustomMetadata] | default None | User-supplied custom metadata about the column, such as Foundry web archetypes, descriptions, etc. |
| array_subtype | arraySubtype | typing.Optional[DatasetFieldSchema] | default None | Only used when field type is array. |
| precision | precision | typing.Optional[int] | None | Only used when field type is decimal. |
| scale | scale | typing.Optional[int] | None | Only used when field type is decimal. |
| map_key_type | mapKeyType | typing.Optional[DatasetFieldSchema] | default None | Only used when field type is map. |
| map_value_type | mapValueType | typing.Optional[DatasetFieldSchema] | default None | Only used when field type is map. |
| sub_schemas | subSchemas | typing.Optional[typing.List[DatasetFieldSchema]] | default None | Only used when field type is struct. |

```python
class DatasetFieldSchema(core.ModelBase):
    """A field in a Foundry dataset."""

    type: SchemaFieldType
    name: typing.Optional[FieldName] = None
    """The name of a column. May be absent in nested schema objects."""

    nullable: bool
    """Indicates whether values of this field may be null."""

    user_defined_type_class: typing.Optional[str] = pydantic.Field(alias=str("userDefinedTypeClass"), default=None)  # type: ignore[literal-required]
    """Canonical classname of the user-defined type for this field. This should be a subclass of Spark's `UserDefinedType`."""

    custom_metadata: typing.Optional[CustomMetadata] = pydantic.Field(alias=str("customMetadata"), default=None)  # type: ignore[literal-required]
    """User-supplied custom metadata about the column, such as Foundry web archetypes, descriptions, etc."""

    array_subtype: typing.Optional[DatasetFieldSchema] = pydantic.Field(alias=str("arraySubtype"), default=None)  # type: ignore[literal-required]
    """Only used when field type is array."""

    precision: typing.Optional[int] = None
    """Only used when field type is decimal."""

    scale: typing.Optional[int] = None
    """Only used when field type is decimal."""

    map_key_type: typing.Optional[DatasetFieldSchema] = pydantic.Field(alias=str("mapKeyType"), default=None)  # type: ignore[literal-required]
    """Only used when field type is map."""

    map_value_type: typing.Optional[DatasetFieldSchema] = pydantic.Field(alias=str("mapValueType"), default=None)  # type: ignore[literal-required]
    """Only used when field type is map."""

    sub_schemas: typing.Optional[typing.List[DatasetFieldSchema]] = pydantic.Field(alias=str("subSchemas"), default=None)  # type: ignore[literal-required]
    """Only used when field type is struct."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CustomMetadata](CustomMetadata.md)
- [foundry_sdk.v2.core.models.FieldName](FieldName.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](SchemaFieldType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DatasetFieldSchema.md)

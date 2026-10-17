# foundry_sdk.v2.data_health.models.SchemaComparisonConfig


Configuration for schema comparison validation with severity settings.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| expected_schema | expectedSchema | SchemaInfo | required; no default | No additional field description in SDK source. |
| schema_comparison_type | schemaComparisonType | SchemaComparisonType | required; no default | No additional field description in SDK source. |
| severity | severity | SeverityLevel | required; no default | No additional field description in SDK source. |

```python
class SchemaComparisonConfig(core.ModelBase):
    """Configuration for schema comparison validation with severity settings."""

    expected_schema: SchemaInfo = pydantic.Field(alias=str("expectedSchema"))  # type: ignore[literal-required]
    schema_comparison_type: SchemaComparisonType = pydantic.Field(alias=str("schemaComparisonType"))  # type: ignore[literal-required]
    severity: SeverityLevel
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.SchemaComparisonType](SchemaComparisonType.md)
- [foundry_sdk.v2.data_health.models.SchemaInfo](SchemaInfo.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](SeverityLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SchemaComparisonConfig.md)

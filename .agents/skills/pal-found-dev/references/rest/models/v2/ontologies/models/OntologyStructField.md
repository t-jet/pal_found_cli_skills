# foundry_sdk.v2.ontologies.models.OntologyStructField


OntologyStructField

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | core_models.StructFieldName | required; no default | No additional field description in SDK source. |
| field_type | fieldType | OntologyDataType | required; no default | No additional field description in SDK source. |
| required | required | bool | required; no default | No additional field description in SDK source. |

```python
class OntologyStructField(core.ModelBase):
    """OntologyStructField"""

    name: core_models.StructFieldName
    field_type: OntologyDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    required: bool
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.StructFieldName](../../core/models/StructFieldName.md)
- [foundry_sdk.v2.ontologies.models.OntologyDataType](OntologyDataType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyStructField.md)

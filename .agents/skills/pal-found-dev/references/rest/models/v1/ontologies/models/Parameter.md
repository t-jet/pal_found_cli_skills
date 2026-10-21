# foundry_sdk.v1.ontologies.models.Parameter


Details about a parameter of an action or query.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| base_type | baseType | ValueType | required; no default | No additional field description in SDK source. |
| data_type | dataType | typing.Optional[OntologyDataType] | default None | No additional field description in SDK source. |
| required | required | bool | required; no default | No additional field description in SDK source. |

```python
class Parameter(core.ModelBase):
    """Details about a parameter of an action or query."""

    description: typing.Optional[str] = None
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    data_type: typing.Optional[OntologyDataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    required: bool
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.OntologyDataType](OntologyDataType.md)
- [foundry_sdk.v1.ontologies.models.ValueType](ValueType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Parameter.md)

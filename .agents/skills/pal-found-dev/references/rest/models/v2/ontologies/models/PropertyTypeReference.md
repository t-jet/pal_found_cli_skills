# foundry_sdk.v2.ontologies.models.PropertyTypeReference


PropertyTypeReference

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| property_api_name | propertyApiName | str | required; no default | The API name of the PropertyType |
| type | type | typing.Literal['propertyType'] | 'propertyType' | No additional field description in SDK source. |

```python
class PropertyTypeReference(core.ModelBase):
    """PropertyTypeReference"""

    property_api_name: str = pydantic.Field(alias=str("propertyApiName"))  # type: ignore[literal-required]
    """The API name of the PropertyType"""

    type: typing.Literal["propertyType"] = "propertyType"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyTypeReference.md)

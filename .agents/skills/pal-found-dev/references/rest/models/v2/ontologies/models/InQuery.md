# foundry_sdk.v2.ontologies.models.InQuery


Returns objects where the specified field equals any of the provided values. Allows you to
specify a property to query on by a variety of means. If an empty array is provided as the value, then the filter will match all objects
in the object set. Either `field` or `propertyIdentifier` must be supplied, but not both.

For string properties, full term matching only works when **Selectable** is enabled for the property in Ontology Manager.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | typing.Optional[PropertyApiName] | None | No additional field description in SDK source. |
| property_identifier | propertyIdentifier | typing.Optional[PropertyIdentifier] | default None | No additional field description in SDK source. |
| value | value | typing.List[PropertyValue] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['in'] | 'in' | No additional field description in SDK source. |

```python
class InQuery(core.ModelBase):
    """
    Returns objects where the specified field equals any of the provided values. Allows you to
    specify a property to query on by a variety of means. If an empty array is provided as the value, then the filter will match all objects
    in the object set. Either `field` or `propertyIdentifier` must be supplied, but not both.

    For string properties, full term matching only works when **Selectable** is enabled for the property in Ontology Manager.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: typing.List[PropertyValue]
    type: typing.Literal["in"] = "in"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InQuery.md)

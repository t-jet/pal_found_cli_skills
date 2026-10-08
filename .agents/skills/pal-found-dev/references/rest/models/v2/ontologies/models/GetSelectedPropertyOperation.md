# foundry_sdk.v2.ontologies.models.GetSelectedPropertyOperation


Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
explode the cardinality.

Use collectList or collectSet which will return a list of values in that case.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| selected_property_api_name | selectedPropertyApiName | PropertyApiName | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['get'] | 'get' | No additional field description in SDK source. |

```python
class GetSelectedPropertyOperation(core.ModelBase):
    """
    Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
    explode the cardinality.

    Use collectList or collectSet which will return a list of values in that case.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["get"] = "get"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetSelectedPropertyOperation.md)

# foundry_sdk.v2.ontologies.models.CreateEdit


CreateEdit

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| properties | properties | typing.Dict[PropertyApiName, PropertyValue] | required; no default | The property values of the object at the time of creation.<br>    Maps property API names to their values. |
| type | type | typing.Literal['createEdit'] | 'createEdit' | No additional field description in SDK source. |

```python
class CreateEdit(core.ModelBase):
    """CreateEdit"""

    properties: typing.Dict[PropertyApiName, PropertyValue]
    """
    The property values of the object at the time of creation.
    Maps property API names to their values.
    """

    type: typing.Literal["createEdit"] = "createEdit"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateEdit.md)

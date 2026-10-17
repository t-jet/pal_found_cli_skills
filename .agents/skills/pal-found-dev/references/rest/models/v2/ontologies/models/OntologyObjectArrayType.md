# foundry_sdk.v2.ontologies.models.OntologyObjectArrayType


OntologyObjectArrayType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sub_type | subType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| reducers | reducers | typing.List[OntologyObjectArrayTypeReducer] | required; no default | If non-empty, this property can be reduced to a single value of the subtype. The reducers are applied in<br>    order to determine a winning value. The array can be loaded as a reduced value or as the full array in an<br>    object set. |
| type | type | typing.Literal['array'] | 'array' | No additional field description in SDK source. |

```python
class OntologyObjectArrayType(core.ModelBase):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    reducers: typing.List[OntologyObjectArrayTypeReducer]
    """
    If non-empty, this property can be reduced to a single value of the subtype. The reducers are applied in
    order to determine a winning value. The array can be loaded as a reduced value or as the full array in an
    object set.
    """

    type: typing.Literal["array"] = "array"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayTypeReducer](OntologyObjectArrayTypeReducer.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyObjectArrayType.md)

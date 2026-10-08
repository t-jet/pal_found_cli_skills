# foundry_sdk.v2.ontologies.models.ObjectSetIntersectionType


ObjectSetIntersectionType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_sets | objectSets | typing.List[ObjectSet] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['intersect'] | 'intersect' | No additional field description in SDK source. |

```python
class ObjectSetIntersectionType(core.ModelBase):
    """ObjectSetIntersectionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["intersect"] = "intersect"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](ObjectSet.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetIntersectionType.md)

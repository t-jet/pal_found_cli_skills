# foundry_sdk.v2.geo.models.Polygon


Polygon

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| coordinates | coordinates | typing.List[LinearRing] | required; no default | No additional field description in SDK source. |
| bbox | bbox | typing.Optional[BBox] | None | No additional field description in SDK source. |
| type | type | typing.Literal['Polygon'] | 'Polygon' | No additional field description in SDK source. |

```python
class Polygon(core.ModelBase):
    """Polygon"""

    coordinates: typing.List[LinearRing]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Polygon"] = "Polygon"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.geo.models.BBox](BBox.md)
- [foundry_sdk.v2.geo.models.LinearRing](LinearRing.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Polygon.md)

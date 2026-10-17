# foundry_sdk.v2.ontologies.models.SpatialFilterMode



The spatial relation operator for a GeoShapeV2Query. INTERSECTS matches objects that intersect the provided
geometry, DISJOINT matches objects that do not intersect the provided geometry, WITHIN matches objects that
lie within the provided geometry, and CONTAINS matches objects that contain the provided geometry.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SpatialFilterMode: typing_extensions.TypeAlias = typing.Literal[
    "INTERSECTS", "DISJOINT", "WITHIN", "CONTAINS"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SpatialFilterMode.md)

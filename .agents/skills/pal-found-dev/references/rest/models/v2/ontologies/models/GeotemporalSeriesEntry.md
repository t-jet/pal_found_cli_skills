# foundry_sdk.v2.ontologies.models.GeotemporalSeriesEntry



A single geotemporal data point. Each entry is a map from property API names to property values. Standard
entries include "time" (ISO 8601 timestamp) and "position" (GeoPoint), and may include additional geotemporal
series metadata fields such as speed, heading, or altitude.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
GeotemporalSeriesEntry: typing_extensions.TypeAlias = typing.Dict[
    "PropertyApiName", "PropertyValue"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GeotemporalSeriesEntry.md)

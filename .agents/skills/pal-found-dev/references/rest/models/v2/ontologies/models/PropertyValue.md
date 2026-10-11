# foundry_sdk.v2.ontologies.models.PropertyValue


An Ontology property value uses the JSON encoding for its declared property type. The SDK source table below lists arrays, primitives, date/time, GeoJSON, Cipher, attachment, media and time-series examples. Match the target property metadata and use the referenced typed model for structured values; do not pass a display string for an attachment or media reference.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyValue: typing_extensions.TypeAlias = typing.Any
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyValue.md)

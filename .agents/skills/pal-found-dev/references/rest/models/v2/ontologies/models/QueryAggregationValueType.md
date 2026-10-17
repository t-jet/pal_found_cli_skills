# foundry_sdk.v2.ontologies.models.QueryAggregationValueType


Use this union for `TwoDimensionalAggregation.value_type`. It accepts `DateType`, `DoubleType`, or `TimestampType`, selected by the `type` discriminator. `QueryAggregationKeyType` is a separate union for `key_type` and supports more alternatives. The SDK description calls this a key type; its field use and definition identify it as the value type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
QueryAggregationValueType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[core_models.DateType, core_models.DoubleType, core_models.TimestampType],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](QueryAggregationValueType.md)

# foundry_sdk.v2.core.models.TimeSeriesItemType


A union of the types supported by time series properties.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TimeSeriesItemType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StringType", "DoubleType", "NumericOrNonNumericType"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.DoubleType](DoubleType.md)
- [foundry_sdk.v2.core.models.NumericOrNonNumericType](NumericOrNonNumericType.md)
- [foundry_sdk.v2.core.models.StringType](StringType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeSeriesItemType.md)

# foundry_sdk.v2.data_health.models.ColumnValue


A column value that can be of different types.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ColumnValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DateColumnValue", "BooleanColumnValue", "StringColumnValue", "NumericColumnValue"
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.data_health.models.BooleanColumnValue](BooleanColumnValue.md)
- [foundry_sdk.v2.data_health.models.DateColumnValue](DateColumnValue.md)
- [foundry_sdk.v2.data_health.models.NumericColumnValue](NumericColumnValue.md)
- [foundry_sdk.v2.data_health.models.StringColumnValue](StringColumnValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ColumnValue.md)

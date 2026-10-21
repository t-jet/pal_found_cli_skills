# foundry_sdk.v2.ontologies.models.PrimaryKeyValueV2


PrimaryKeyValueV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PrimaryKeyValueV2: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DateValue",
        "StringValue",
        "TimestampValue",
        "BooleanValue",
        "IntegerValue",
        "DoubleValue",
        "LongValue",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.BooleanValue](BooleanValue.md)
- [foundry_sdk.v2.ontologies.models.DateValue](DateValue.md)
- [foundry_sdk.v2.ontologies.models.DoubleValue](DoubleValue.md)
- [foundry_sdk.v2.ontologies.models.IntegerValue](IntegerValue.md)
- [foundry_sdk.v2.ontologies.models.LongValue](LongValue.md)
- [foundry_sdk.v2.ontologies.models.StringValue](StringValue.md)
- [foundry_sdk.v2.ontologies.models.TimestampValue](TimestampValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PrimaryKeyValueV2.md)

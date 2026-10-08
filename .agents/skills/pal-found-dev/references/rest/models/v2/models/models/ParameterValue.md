# foundry_sdk.v2.models.models.ParameterValue


A parameter value logged for an experiment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DatetimeParameter",
        "BooleanParameter",
        "StringParameter",
        "DoubleParameter",
        "IntegerParameter",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.BooleanParameter](BooleanParameter.md)
- [foundry_sdk.v2.models.models.DatetimeParameter](DatetimeParameter.md)
- [foundry_sdk.v2.models.models.DoubleParameter](DoubleParameter.md)
- [foundry_sdk.v2.models.models.IntegerParameter](IntegerParameter.md)
- [foundry_sdk.v2.models.models.StringParameter](StringParameter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterValue.md)

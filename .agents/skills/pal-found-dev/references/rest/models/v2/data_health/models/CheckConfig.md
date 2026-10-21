# foundry_sdk.v2.data_health.models.CheckConfig


Configuration of a check.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckConfig: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "NumericColumnRangeCheckConfig",
        "JobStatusCheckConfig",
        "NumericColumnMeanCheckConfig",
        "DateColumnRangeCheckConfig",
        "JobDurationCheckConfig",
        "ApproximateUniquePercentageCheckConfig",
        "BuildStatusCheckConfig",
        "ColumnTypeCheckConfig",
        "AllowedColumnValuesCheckConfig",
        "TimeSinceLastUpdatedCheckConfig",
        "NullPercentageCheckConfig",
        "TotalColumnCountCheckConfig",
        "NumericColumnMedianCheckConfig",
        "BuildDurationCheckConfig",
        "SchemaComparisonCheckConfig",
        "PrimaryKeyCheckConfig",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.data_health.models.AllowedColumnValuesCheckConfig](AllowedColumnValuesCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ApproximateUniquePercentageCheckConfig](ApproximateUniquePercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.BuildDurationCheckConfig](BuildDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.BuildStatusCheckConfig](BuildStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ColumnTypeCheckConfig](ColumnTypeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.DateColumnRangeCheckConfig](DateColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.JobDurationCheckConfig](JobDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.JobStatusCheckConfig](JobStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NullPercentageCheckConfig](NullPercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnMeanCheckConfig](NumericColumnMeanCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnMedianCheckConfig](NumericColumnMedianCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnRangeCheckConfig](NumericColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.PrimaryKeyCheckConfig](PrimaryKeyCheckConfig.md)
- [foundry_sdk.v2.data_health.models.SchemaComparisonCheckConfig](SchemaComparisonCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TimeSinceLastUpdatedCheckConfig](TimeSinceLastUpdatedCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TotalColumnCountCheckConfig](TotalColumnCountCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckConfig.md)

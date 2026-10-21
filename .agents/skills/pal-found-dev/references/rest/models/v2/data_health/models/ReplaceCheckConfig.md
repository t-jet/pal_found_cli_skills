# foundry_sdk.v2.data_health.models.ReplaceCheckConfig


Configuration of a check.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ReplaceCheckConfig: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ReplaceNumericColumnRangeCheckConfig",
        "ReplaceJobStatusCheckConfig",
        "ReplaceNumericColumnMeanCheckConfig",
        "ReplaceDateColumnRangeCheckConfig",
        "ReplaceJobDurationCheckConfig",
        "ReplaceApproximateUniquePercentageCheckConfig",
        "ReplaceBuildStatusCheckConfig",
        "ReplaceColumnTypeCheckConfig",
        "ReplaceAllowedColumnValuesCheckConfig",
        "ReplaceTimeSinceLastUpdatedCheckConfig",
        "ReplaceNullPercentageCheckConfig",
        "ReplaceTotalColumnCountCheckConfig",
        "ReplaceNumericColumnMedianCheckConfig",
        "ReplaceBuildDurationCheckConfig",
        "ReplaceSchemaComparisonCheckConfig",
        "ReplacePrimaryKeyCheckConfig",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.data_health.models.ReplaceAllowedColumnValuesCheckConfig](ReplaceAllowedColumnValuesCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceApproximateUniquePercentageCheckConfig](ReplaceApproximateUniquePercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceBuildDurationCheckConfig](ReplaceBuildDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceBuildStatusCheckConfig](ReplaceBuildStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceColumnTypeCheckConfig](ReplaceColumnTypeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceDateColumnRangeCheckConfig](ReplaceDateColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceJobDurationCheckConfig](ReplaceJobDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceJobStatusCheckConfig](ReplaceJobStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceNullPercentageCheckConfig](ReplaceNullPercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceNumericColumnMeanCheckConfig](ReplaceNumericColumnMeanCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceNumericColumnMedianCheckConfig](ReplaceNumericColumnMedianCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceNumericColumnRangeCheckConfig](ReplaceNumericColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplacePrimaryKeyCheckConfig](ReplacePrimaryKeyCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceSchemaComparisonCheckConfig](ReplaceSchemaComparisonCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceTimeSinceLastUpdatedCheckConfig](ReplaceTimeSinceLastUpdatedCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ReplaceTotalColumnCountCheckConfig](ReplaceTotalColumnCountCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceCheckConfig.md)

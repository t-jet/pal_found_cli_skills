# foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRuleType


PropertyNumberFormattingRuleType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyNumberFormattingRuleType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "NumberFormatStandard",
        "NumberFormatDuration",
        "NumberFormatFixedValues",
        "NumberFormatAffix",
        "NumberFormatScale",
        "NumberFormatCurrency",
        "NumberFormatStandardUnit",
        "NumberFormatCustomUnit",
        "NumberFormatRatio",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.NumberFormatAffix](NumberFormatAffix.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCurrency](NumberFormatCurrency.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCustomUnit](NumberFormatCustomUnit.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatDuration](NumberFormatDuration.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatFixedValues](NumberFormatFixedValues.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatRatio](NumberFormatRatio.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatScale](NumberFormatScale.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatStandard](NumberFormatStandard.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatStandardUnit](NumberFormatStandardUnit.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyNumberFormattingRuleType.md)

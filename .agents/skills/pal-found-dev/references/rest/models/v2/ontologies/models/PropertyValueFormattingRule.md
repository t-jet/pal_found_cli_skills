# foundry_sdk.v2.ontologies.models.PropertyValueFormattingRule



This feature is experimental and may change in a future release.
Comprehensive formatting configuration for displaying property values in user interfaces. 
Supports different value types including numbers, dates, timestamps, booleans, and known Foundry types.

Each formatter type provides specific options tailored to that data type:
- Numbers: Support for percentages, currencies, units, scaling, and custom formatting
- Dates/Timestamps: Localized and custom formatting patterns
- Booleans: Custom true/false display text
- Known types: Special formatting for Foundry-specific identifiers


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyValueFormattingRule: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PropertyDateFormattingRule",
        "PropertyNumberFormattingRule",
        "PropertyBooleanFormattingRule",
        "PropertyKnownTypeFormattingRule",
        "PropertyTimestampFormattingRule",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PropertyBooleanFormattingRule](PropertyBooleanFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyDateFormattingRule](PropertyDateFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyKnownTypeFormattingRule](PropertyKnownTypeFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRule](PropertyNumberFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyTimestampFormattingRule](PropertyTimestampFormattingRule.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyValueFormattingRule.md)

# foundry_sdk.v2.ontologies.models.IntervalQueryRule


Sub-rule used for evaluating an IntervalQuery

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
IntervalQueryRule: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["AllOfRule", "MatchRule", "AnyOfRule", "PrefixOnLastTokenRule", "FuzzyRule"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.AllOfRule](AllOfRule.md)
- [foundry_sdk.v2.ontologies.models.AnyOfRule](AnyOfRule.md)
- [foundry_sdk.v2.ontologies.models.FuzzyRule](FuzzyRule.md)
- [foundry_sdk.v2.ontologies.models.MatchRule](MatchRule.md)
- [foundry_sdk.v2.ontologies.models.PrefixOnLastTokenRule](PrefixOnLastTokenRule.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](IntervalQueryRule.md)

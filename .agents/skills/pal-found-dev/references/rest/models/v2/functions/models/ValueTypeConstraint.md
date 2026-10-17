# foundry_sdk.v2.functions.models.ValueTypeConstraint


ValueTypeConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ValueTypeConstraint: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "StructConstraint",
        "StructV1Constraint",
        "RegexConstraint",
        "NullableConstraint",
        "ArrayConstraint",
        "LengthConstraint",
        "RangesConstraint",
        "RidConstraint",
        "MapConstraint",
        "UuidConstraint",
        "EnumConstraint",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.functions.models.ArrayConstraint](ArrayConstraint.md)
- [foundry_sdk.v2.functions.models.EnumConstraint](EnumConstraint.md)
- [foundry_sdk.v2.functions.models.LengthConstraint](LengthConstraint.md)
- [foundry_sdk.v2.functions.models.MapConstraint](MapConstraint.md)
- [foundry_sdk.v2.functions.models.NullableConstraint](NullableConstraint.md)
- [foundry_sdk.v2.functions.models.RangesConstraint](RangesConstraint.md)
- [foundry_sdk.v2.functions.models.RegexConstraint](RegexConstraint.md)
- [foundry_sdk.v2.functions.models.RidConstraint](RidConstraint.md)
- [foundry_sdk.v2.functions.models.StructConstraint](StructConstraint.md)
- [foundry_sdk.v2.functions.models.StructV1Constraint](StructV1Constraint.md)
- [foundry_sdk.v2.functions.models.UuidConstraint](UuidConstraint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValueTypeConstraint.md)

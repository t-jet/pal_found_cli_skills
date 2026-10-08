# foundry_sdk.v2.ontologies.models.ValueTypeConstraint


ValueTypeConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ValueTypeConstraint: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "StructConstraint",
        "RegexConstraint",
        core_models.UnsupportedType,
        "ArrayConstraint",
        "LengthConstraint",
        "RangesConstraint",
        "RidConstraint",
        "UuidConstraint",
        "EnumConstraint",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.UnsupportedType](../../core/models/UnsupportedType.md)
- [foundry_sdk.v2.ontologies.models.ArrayConstraint](ArrayConstraint.md)
- [foundry_sdk.v2.ontologies.models.EnumConstraint](EnumConstraint.md)
- [foundry_sdk.v2.ontologies.models.LengthConstraint](LengthConstraint.md)
- [foundry_sdk.v2.ontologies.models.RangesConstraint](RangesConstraint.md)
- [foundry_sdk.v2.ontologies.models.RegexConstraint](RegexConstraint.md)
- [foundry_sdk.v2.ontologies.models.RidConstraint](RidConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructConstraint](StructConstraint.md)
- [foundry_sdk.v2.ontologies.models.UuidConstraint](UuidConstraint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValueTypeConstraint.md)

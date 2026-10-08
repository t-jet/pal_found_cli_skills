# foundry_sdk.v2.ontologies.models.DerivedPropertyDefinition


Definition of a derived property.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DerivedPropertyDefinition: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "AddPropertyExpression",
        "AbsoluteValuePropertyExpression",
        "ExtractPropertyExpression",
        "SelectedPropertyExpression",
        "NegatePropertyExpression",
        "SubtractPropertyExpression",
        "PropertyApiNameSelector",
        "LeastPropertyExpression",
        "DividePropertyExpression",
        "MultiplyPropertyExpression",
        "GreatestPropertyExpression",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.AbsoluteValuePropertyExpression](AbsoluteValuePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.AddPropertyExpression](AddPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.DividePropertyExpression](DividePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.ExtractPropertyExpression](ExtractPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.GreatestPropertyExpression](GreatestPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.LeastPropertyExpression](LeastPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.MultiplyPropertyExpression](MultiplyPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.NegatePropertyExpression](NegatePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiNameSelector](PropertyApiNameSelector.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyExpression](SelectedPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.SubtractPropertyExpression](SubtractPropertyExpression.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DerivedPropertyDefinition.md)

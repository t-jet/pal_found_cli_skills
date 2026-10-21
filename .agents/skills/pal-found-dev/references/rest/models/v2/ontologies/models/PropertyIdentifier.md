# foundry_sdk.v2.ontologies.models.PropertyIdentifier


An identifier used to select properties or struct fields.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyIdentifier: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PropertyApiNameSelector",
        "StructFieldSelector",
        "PropertyWithLoadLevelSelector",
        "TitlePropertySelector",
        "PrimaryKeyPropertySelector",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PrimaryKeyPropertySelector](PrimaryKeyPropertySelector.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiNameSelector](PropertyApiNameSelector.md)
- [foundry_sdk.v2.ontologies.models.PropertyWithLoadLevelSelector](PropertyWithLoadLevelSelector.md)
- [foundry_sdk.v2.ontologies.models.StructFieldSelector](StructFieldSelector.md)
- [foundry_sdk.v2.ontologies.models.TitlePropertySelector](TitlePropertySelector.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyIdentifier.md)

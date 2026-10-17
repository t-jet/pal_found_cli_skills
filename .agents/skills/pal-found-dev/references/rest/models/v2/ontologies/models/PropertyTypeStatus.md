# foundry_sdk.v2.ontologies.models.PropertyTypeStatus


The status to indicate whether the PropertyType is either Experimental, Active, Deprecated, or Example.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyTypeStatus: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DeprecatedPropertyTypeStatus",
        "ActivePropertyTypeStatus",
        "ExperimentalPropertyTypeStatus",
        "ExamplePropertyTypeStatus",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ActivePropertyTypeStatus](ActivePropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.DeprecatedPropertyTypeStatus](DeprecatedPropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.ExamplePropertyTypeStatus](ExamplePropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.ExperimentalPropertyTypeStatus](ExperimentalPropertyTypeStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyTypeStatus.md)

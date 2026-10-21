# foundry_sdk.v2.ontologies.models.StructFieldArgument


Represents an argument used for an individual struct field.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
StructFieldArgument: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StructListParameterFieldArgument", "StructParameterFieldArgument"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.StructListParameterFieldArgument](StructListParameterFieldArgument.md)
- [foundry_sdk.v2.ontologies.models.StructParameterFieldArgument](StructParameterFieldArgument.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructFieldArgument.md)

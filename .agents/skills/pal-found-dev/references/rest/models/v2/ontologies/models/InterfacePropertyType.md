# foundry_sdk.v2.ontologies.models.InterfacePropertyType



The definition of an interface property type on an interface. An interface property can either be backed by a
shared property type or defined on the interface directly.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfacePropertyType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["InterfaceDefinedPropertyType", "InterfaceSharedPropertyType"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.InterfaceDefinedPropertyType](InterfaceDefinedPropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceSharedPropertyType](InterfaceSharedPropertyType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfacePropertyType.md)

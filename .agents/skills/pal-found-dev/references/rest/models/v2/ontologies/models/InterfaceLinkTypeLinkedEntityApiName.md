# foundry_sdk.v2.ontologies.models.InterfaceLinkTypeLinkedEntityApiName


A reference to the linked entity. This can either be an object or an interface type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfaceLinkTypeLinkedEntityApiName: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["LinkedObjectTypeApiName", "LinkedInterfaceTypeApiName"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.LinkedInterfaceTypeApiName](LinkedInterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkedObjectTypeApiName](LinkedObjectTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceLinkTypeLinkedEntityApiName.md)

# foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappingsV2


Map from object type to the interface property implementations of that object type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfaceToObjectTypeMappingsV2: typing_extensions.TypeAlias = typing.Dict[
    "ObjectTypeApiName", "InterfaceToObjectTypeMappingV2"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappingV2](InterfaceToObjectTypeMappingV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceToObjectTypeMappingsV2.md)

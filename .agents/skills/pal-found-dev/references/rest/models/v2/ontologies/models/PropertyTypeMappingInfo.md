# foundry_sdk.v2.ontologies.models.PropertyTypeMappingInfo



Describes how a single object type property is bound to its backing tabular datasource. A property may be backed
by a single column, by a struct (with nested field mappings), or be edit-only (no backing column even though it
is permissioned to the tabular datasource).


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyTypeMappingInfo: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StructPropertyMapping", "ColumnPropertyMapping", "EditOnlyPropertyMapping"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ColumnPropertyMapping](ColumnPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.EditOnlyPropertyMapping](EditOnlyPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.StructPropertyMapping](StructPropertyMapping.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyTypeMappingInfo.md)

# foundry_sdk.v2.ontologies.models.ObjectPrimaryKeyV2


ObjectPrimaryKeyV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ObjectPrimaryKeyV2: typing_extensions.TypeAlias = typing.Dict[
    "PropertyApiName", "PrimaryKeyValueV2"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PrimaryKeyValueV2](PrimaryKeyValueV2.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectPrimaryKeyV2.md)

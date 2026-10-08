# foundry_sdk.v2.ontologies.models.ActionTypeFuzziness



Fuzziness setting applied to `contains` full-text string predicates in the search query. If not provided,
`auto` is used.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionTypeFuzziness: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["FuzzinessAuto", "FuzzinessOff"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.FuzzinessAuto](FuzzinessAuto.md)
- [foundry_sdk.v2.ontologies.models.FuzzinessOff](FuzzinessOff.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeFuzziness.md)

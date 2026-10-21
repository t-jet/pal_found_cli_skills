# foundry_sdk.v1.ontologies.models.SearchJsonQuery


SearchJsonQuery

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchJsonQuery: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "OrQuery",
        "PrefixQuery",
        "LtQuery",
        "AllTermsQuery",
        "EqualsQuery",
        "GtQuery",
        "ContainsQuery",
        "NotQuery",
        "PhraseQuery",
        "AndQuery",
        "IsNullQuery",
        "GteQuery",
        "AnyTermQuery",
        "LteQuery",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v1.ontologies.models.AllTermsQuery](AllTermsQuery.md)
- [foundry_sdk.v1.ontologies.models.AndQuery](AndQuery.md)
- [foundry_sdk.v1.ontologies.models.AnyTermQuery](AnyTermQuery.md)
- [foundry_sdk.v1.ontologies.models.ContainsQuery](ContainsQuery.md)
- [foundry_sdk.v1.ontologies.models.EqualsQuery](EqualsQuery.md)
- [foundry_sdk.v1.ontologies.models.GtQuery](GtQuery.md)
- [foundry_sdk.v1.ontologies.models.GteQuery](GteQuery.md)
- [foundry_sdk.v1.ontologies.models.IsNullQuery](IsNullQuery.md)
- [foundry_sdk.v1.ontologies.models.LtQuery](LtQuery.md)
- [foundry_sdk.v1.ontologies.models.LteQuery](LteQuery.md)
- [foundry_sdk.v1.ontologies.models.NotQuery](NotQuery.md)
- [foundry_sdk.v1.ontologies.models.OrQuery](OrQuery.md)
- [foundry_sdk.v1.ontologies.models.PhraseQuery](PhraseQuery.md)
- [foundry_sdk.v1.ontologies.models.PrefixQuery](PrefixQuery.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchJsonQuery.md)

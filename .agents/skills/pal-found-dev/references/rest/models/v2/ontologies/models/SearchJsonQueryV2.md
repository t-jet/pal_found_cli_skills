# foundry_sdk.v2.ontologies.models.SearchJsonQueryV2


SearchJsonQueryV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchJsonQueryV2: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "LtQueryV2",
        "DoesNotIntersectBoundingBoxQuery",
        "RelativeDateRangeQuery",
        "WildcardQuery",
        "WithinDistanceOfQuery",
        "WithinBoundingBoxQuery",
        "NotQueryV2",
        "IntersectsBoundingBoxQuery",
        "AndQueryV2",
        "ContainsAllTermsInOrderPrefixLastTerm",
        "GteQueryV2",
        "ContainsAllTermsInOrderQuery",
        "WithinPolygonQuery",
        "IntersectsPolygonQuery",
        "LteQueryV2",
        "OrQueryV2",
        "InQuery",
        "DoesNotIntersectPolygonQuery",
        "EqualsQueryV2",
        "ContainsAllTermsQuery",
        "GtQueryV2",
        "ContainsQueryV2",
        "RegexQuery",
        "IsNullQueryV2",
        "ContainsAnyTermQuery",
        "IntervalQuery",
        "GeoShapeV2Query",
        "StartsWithQuery",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.AndQueryV2](AndQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderPrefixLastTerm](ContainsAllTermsInOrderPrefixLastTerm.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderQuery](ContainsAllTermsInOrderQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsQuery](ContainsAllTermsQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAnyTermQuery](ContainsAnyTermQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsQueryV2](ContainsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectBoundingBoxQuery](DoesNotIntersectBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectPolygonQuery](DoesNotIntersectPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.EqualsQueryV2](EqualsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Query](GeoShapeV2Query.md)
- [foundry_sdk.v2.ontologies.models.GtQueryV2](GtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.GteQueryV2](GteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.InQuery](InQuery.md)
- [foundry_sdk.v2.ontologies.models.IntersectsBoundingBoxQuery](IntersectsBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.IntersectsPolygonQuery](IntersectsPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQuery](IntervalQuery.md)
- [foundry_sdk.v2.ontologies.models.IsNullQueryV2](IsNullQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LtQueryV2](LtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LteQueryV2](LteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.NotQueryV2](NotQueryV2.md)
- [foundry_sdk.v2.ontologies.models.OrQueryV2](OrQueryV2.md)
- [foundry_sdk.v2.ontologies.models.RegexQuery](RegexQuery.md)
- [foundry_sdk.v2.ontologies.models.RelativeDateRangeQuery](RelativeDateRangeQuery.md)
- [foundry_sdk.v2.ontologies.models.StartsWithQuery](StartsWithQuery.md)
- [foundry_sdk.v2.ontologies.models.WildcardQuery](WildcardQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxQuery](WithinBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinDistanceOfQuery](WithinDistanceOfQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinPolygonQuery](WithinPolygonQuery.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchJsonQueryV2.md)

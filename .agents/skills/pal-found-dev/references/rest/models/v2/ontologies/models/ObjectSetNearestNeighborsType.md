# foundry_sdk.v2.ontologies.models.ObjectSetNearestNeighborsType


ObjectSet containing the top `numNeighbors` objects with `propertyIdentifier` nearest to the input vector or
text. This can only be performed on a property with type vector that has been configured to be searched with
approximate nearest neighbors using a similarity function configured in the Ontology.

A non-zero score for each resulting object is returned when the `orderType` in the `orderBy` field is set to
`relevance`. Note that:
  - Scores will not be returned if a nearestNeighbors object set is composed through union, subtraction
    or intersection with non-nearestNeighbors object sets.
  - If results have scores, the order of the scores will be decreasing (duplicate scores are possible).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set | objectSet | ObjectSet | required; no default | No additional field description in SDK source. |
| property_identifier | propertyIdentifier | PropertyIdentifier | required; no default | No additional field description in SDK source. |
| num_neighbors | numNeighbors | int | required; no default | The number of objects to return. If the number of documents in the objectType is less than the provided<br>    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500. |
| similarity_threshold | similarityThreshold | typing.Optional[float] | default None | The similarity threshold results must be above to be included in the returned in the object set.<br>    0 &lt;= Threshold &lt;= 1. Where 1 is identical and 0 is least similar. |
| query | query | NearestNeighborsQuery | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['nearestNeighbors'] | 'nearestNeighbors' | No additional field description in SDK source. |

```python
class ObjectSetNearestNeighborsType(core.ModelBase):
    """
    ObjectSet containing the top `numNeighbors` objects with `propertyIdentifier` nearest to the input vector or
    text. This can only be performed on a property with type vector that has been configured to be searched with
    approximate nearest neighbors using a similarity function configured in the Ontology.

    A non-zero score for each resulting object is returned when the `orderType` in the `orderBy` field is set to
    `relevance`. Note that:
      - Scores will not be returned if a nearestNeighbors object set is composed through union, subtraction
        or intersection with non-nearestNeighbors object sets.
      - If results have scores, the order of the scores will be decreasing (duplicate scores are possible).
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    property_identifier: PropertyIdentifier = pydantic.Field(alias=str("propertyIdentifier"))  # type: ignore[literal-required]
    num_neighbors: int = pydantic.Field(alias=str("numNeighbors"))  # type: ignore[literal-required]
    """
    The number of objects to return. If the number of documents in the objectType is less than the provided
    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.
    """

    similarity_threshold: typing.Optional[float] = pydantic.Field(alias=str("similarityThreshold"), default=None)  # type: ignore[literal-required]
    """
    The similarity threshold results must be above to be included in the returned in the object set.
    0 &lt;= Threshold &lt;= 1. Where 1 is identical and 0 is least similar.
    """

    query: NearestNeighborsQuery
    type: typing.Literal["nearestNeighbors"] = "nearestNeighbors"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NearestNeighborsQuery](NearestNeighborsQuery.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](ObjectSet.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetNearestNeighborsType.md)

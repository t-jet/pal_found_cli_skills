# foundry_sdk.v2.ontologies.models.LoadObjectSetV2ObjectsOrInterfacesResponse


Represents the API response when loading an `ObjectSet`. Objects in the returned set can either have properties
defined by an interface that the objects belong to or properties defined by the object type of the object.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[OntologyObjectV2] | required; no default | The list of objects in the current page. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| total_count | totalCount | core_models.TotalCount | required; no default | No additional field description in SDK source. |
| transaction_id | transactionId | typing.Optional[OntologyTransactionId] | default None | No additional field description in SDK source. |

```python
class LoadObjectSetV2ObjectsOrInterfacesResponse(core.ModelBase):
    """
    Represents the API response when loading an `ObjectSet`. Objects in the returned set can either have properties
    defined by an interface that the objects belong to or properties defined by the object type of the object.
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    transaction_id: typing.Optional[OntologyTransactionId] = pydantic.Field(alias=str("transactionId"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.core.models.TotalCount](../../core/models/TotalCount.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](OntologyObjectV2.md)
- [foundry_sdk.v2.ontologies.models.OntologyTransactionId](OntologyTransactionId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LoadObjectSetV2ObjectsOrInterfacesResponse.md)

# foundry_sdk.v2.ontologies.models.ListScenarioEditedObjectsResponse


The objects that have been edited within a scenario for a given object type.

The Ontology Objects in this response will only ever have the `__primaryKey` and `__apiName`
fields present, thus functioning as object locators rather than full objects.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[OntologyObjectV2] | required; no default | The list of objects that have been edited within the scenario. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |

```python
class ListScenarioEditedObjectsResponse(core.ModelBase):
    """
    The objects that have been edited within a scenario for a given object type.

    The Ontology Objects in this response will only ever have the `__primaryKey` and `__apiName`
    fields present, thus functioning as object locators rather than full objects.
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects that have been edited within the scenario."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](OntologyObjectV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ListScenarioEditedObjectsResponse.md)

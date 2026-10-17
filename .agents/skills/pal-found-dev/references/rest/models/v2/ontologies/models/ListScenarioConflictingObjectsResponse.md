# foundry_sdk.v2.ontologies.models.ListScenarioConflictingObjectsResponse


The objects that have a conflicting edit within a scenario for a given object type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[ObjectLocator] | required; no default | The list of objects that have a conflicting edit within the scenario. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |

```python
class ListScenarioConflictingObjectsResponse(core.ModelBase):
    """The objects that have a conflicting edit within a scenario for a given object type."""

    data: typing.List[ObjectLocator]
    """The list of objects that have a conflicting edit within the scenario."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.ObjectLocator](ObjectLocator.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ListScenarioConflictingObjectsResponse.md)

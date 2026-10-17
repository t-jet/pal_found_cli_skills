# foundry_sdk.v2.ontologies.models.SearchActionTypesOrderByV2


Specifies the ordering of action type search results by a field and an ordering direction. If not provided,
results are ordered by relevance of the match.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | ActionTypeSortByV2 | required; no default | No additional field description in SDK source. |
| direction | direction | typing.Optional[str] | None | Specifies the ordering direction (can be either `asc` or `desc`) |

```python
class SearchActionTypesOrderByV2(core.ModelBase):
    """
    Specifies the ordering of action type search results by a field and an ordering direction. If not provided,
    results are ordered by relevance of the match.
    """

    field: ActionTypeSortByV2
    direction: typing.Optional[str] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeSortByV2](ActionTypeSortByV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchActionTypesOrderByV2.md)

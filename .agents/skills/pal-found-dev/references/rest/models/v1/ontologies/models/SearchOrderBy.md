# foundry_sdk.v1.ontologies.models.SearchOrderBy


Specifies the ordering of search results by a field and an ordering direction.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| fields | fields | typing.List[SearchOrdering] | required; no default | No additional field description in SDK source. |

```python
class SearchOrderBy(core.ModelBase):
    """Specifies the ordering of search results by a field and an ordering direction."""

    fields: typing.List[SearchOrdering]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.SearchOrdering](SearchOrdering.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchOrderBy.md)

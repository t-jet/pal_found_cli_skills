# foundry_sdk.v2.models.models.SearchExperimentsOrderBy


Ordering configuration for experiment search results.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | SearchExperimentsOrderByField | required; no default | No additional field description in SDK source. |
| direction | direction | core_models.OrderByDirection | required; no default | No additional field description in SDK source. |

```python
class SearchExperimentsOrderBy(core.ModelBase):
    """Ordering configuration for experiment search results."""

    field: SearchExperimentsOrderByField
    direction: core_models.OrderByDirection
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.OrderByDirection](../../core/models/OrderByDirection.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrderByField](SearchExperimentsOrderByField.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsOrderBy.md)

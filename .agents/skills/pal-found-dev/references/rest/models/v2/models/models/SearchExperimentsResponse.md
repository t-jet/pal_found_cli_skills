# foundry_sdk.v2.models.models.SearchExperimentsResponse


Response from searching experiments.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[Experiment] | required; no default | List of experiments matching the search criteria. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | Token for retrieving the next page of results, if more results are available. |

```python
class SearchExperimentsResponse(core.ModelBase):
    """Response from searching experiments."""

    data: typing.List[Experiment]
    """List of experiments matching the search criteria."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    """Token for retrieving the next page of results, if more results are available."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.models.models.Experiment](Experiment.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsResponse.md)

# foundry_sdk.v2.aip_agents.models.AgentsSessionsPage


A page of results for sessions across all accessible Agents for the calling user.
Sessions are returned in order of most recently updated first.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | The page token that should be used when requesting the next page of results.<br>    Empty if there are no more results to retrieve. |
| data | data | typing.List[Session] | required; no default | No additional field description in SDK source. |

```python
class AgentsSessionsPage(core.ModelBase):
    """
    A page of results for sessions across all accessible Agents for the calling user.
    Sessions are returned in order of most recently updated first.
    """

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    """
    The page token that should be used when requesting the next page of results.
    Empty if there are no more results to retrieve.
    """

    data: typing.List[Session]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.Session](Session.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AgentsSessionsPage.md)

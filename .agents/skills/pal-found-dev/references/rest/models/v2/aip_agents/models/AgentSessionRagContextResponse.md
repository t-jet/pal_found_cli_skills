# foundry_sdk.v2.aip_agents.models.AgentSessionRagContextResponse


Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_contexts | objectContexts | typing.List[ObjectContext] | required; no default | No additional field description in SDK source. |
| function_retrieved_contexts | functionRetrievedContexts | typing.List[FunctionRetrievedContext] | required; no default | No additional field description in SDK source. |

```python
class AgentSessionRagContextResponse(core.ModelBase):
    """Context retrieved from an Agent's configured context data sources which was relevant to the supplied user message."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    function_retrieved_contexts: typing.List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.FunctionRetrievedContext](FunctionRetrievedContext.md)
- [foundry_sdk.v2.aip_agents.models.ObjectContext](ObjectContext.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AgentSessionRagContextResponse.md)

# foundry_sdk.v2.aip_agents.models.SessionExchangeContexts


Retrieved context which was passed to the Agent as input for the exchange.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_contexts | objectContexts | typing.List[ObjectContext] | required; no default | Relevant object context for the user's message that was included in the prompt to the Agent. |
| function_retrieved_contexts | functionRetrievedContexts | typing.List[FunctionRetrievedContext] | required; no default | Context retrieved from running a function that was included as additional context in the prompt to the Agent. |

```python
class SessionExchangeContexts(core.ModelBase):
    """Retrieved context which was passed to the Agent as input for the exchange."""

    object_contexts: typing.List[ObjectContext] = pydantic.Field(alias=str("objectContexts"))  # type: ignore[literal-required]
    """Relevant object context for the user's message that was included in the prompt to the Agent."""

    function_retrieved_contexts: typing.List[FunctionRetrievedContext] = pydantic.Field(alias=str("functionRetrievedContexts"))  # type: ignore[literal-required]
    """Context retrieved from running a function that was included as additional context in the prompt to the Agent."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.FunctionRetrievedContext](FunctionRetrievedContext.md)
- [foundry_sdk.v2.aip_agents.models.ObjectContext](ObjectContext.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionExchangeContexts.md)

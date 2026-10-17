# foundry_sdk.v2.aip_agents.models.FunctionRetrievedContext


Context retrieved from running a function to include as additional context in the prompt to the Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| function_rid | functionRid | functions_models.FunctionRid | required; no default | No additional field description in SDK source. |
| function_version | functionVersion | functions_models.FunctionVersion | required; no default | No additional field description in SDK source. |
| retrieved_prompt | retrievedPrompt | str | required; no default | String content returned from a context retrieval function. |
| type | type | typing.Literal['functionRetrievedContext'] | 'functionRetrievedContext' | No additional field description in SDK source. |

```python
class FunctionRetrievedContext(core.ModelBase):
    """Context retrieved from running a function to include as additional context in the prompt to the Agent."""

    function_rid: functions_models.FunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]
    function_version: functions_models.FunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]
    retrieved_prompt: str = pydantic.Field(alias=str("retrievedPrompt"))  # type: ignore[literal-required]
    """String content returned from a context retrieval function."""

    type: typing.Literal["functionRetrievedContext"] = "functionRetrievedContext"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.functions.models.FunctionRid](../../functions/models/FunctionRid.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](../../functions/models/FunctionVersion.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FunctionRetrievedContext.md)

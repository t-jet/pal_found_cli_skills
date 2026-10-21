# foundry_sdk.v2.aip_agents.models.SessionTrace


SessionTrace

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | SessionTraceId | required; no default | The unique identifier for the trace. |
| status | status | SessionTraceStatus | required; no default | This indicates whether the Agent has finished generating the final response. Clients should keep polling<br>    the `getSessionTrace` endpoint until the status is `COMPLETE`. |
| contexts | contexts | typing.Optional[SessionExchangeContexts] | None | Any additional context which was provided by the client or retrieved automatically by the agent, grouped<br>    by context type. Empty if no additional context was provided or configured to be automatically<br>    retrieved. A present SessionExchangeContexts object with empty lists indicates that context retrieval<br>    was attempted but no context was found.<br>    Note that this field will only be populated once the response generation has completed. |
| tool_call_groups | toolCallGroups | typing.List[ToolCallGroup] | required; no default | List of tool call groups that were triggered at the same point in the trace for the agent response<br>    generation. The groups are returned in the same order as they were triggered by the agent. |

```python
class SessionTrace(core.ModelBase):
    """SessionTrace"""

    id: SessionTraceId
    """The unique identifier for the trace."""

    status: SessionTraceStatus
    """
    This indicates whether the Agent has finished generating the final response. Clients should keep polling
    the `getSessionTrace` endpoint until the status is `COMPLETE`.
    """

    contexts: typing.Optional[SessionExchangeContexts] = None
    """
    Any additional context which was provided by the client or retrieved automatically by the agent, grouped
    by context type. Empty if no additional context was provided or configured to be automatically
    retrieved. A present SessionExchangeContexts object with empty lists indicates that context retrieval
    was attempted but no context was found.
    Note that this field will only be populated once the response generation has completed.
    """

    tool_call_groups: typing.List[ToolCallGroup] = pydantic.Field(alias=str("toolCallGroups"))  # type: ignore[literal-required]
    """
    List of tool call groups that were triggered at the same point in the trace for the agent response
    generation. The groups are returned in the same order as they were triggered by the agent.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeContexts](SessionExchangeContexts.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceId](SessionTraceId.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceStatus](SessionTraceStatus.md)
- [foundry_sdk.v2.aip_agents.models.ToolCallGroup](ToolCallGroup.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionTrace.md)

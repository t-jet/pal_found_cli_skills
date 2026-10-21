# foundry_sdk.v2.aip_agents.models.AgentMetadata


Metadata for an Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | str | required; no default | The name of the Agent. |
| description | description | typing.Optional[str] | None | The description for the Agent. |
| input_placeholder | inputPlaceholder | typing.Optional[str] | default None | The default text to show as the placeholder input for chats with the Agent. |
| suggested_prompts | suggestedPrompts | typing.List[str] | required; no default | Prompts to show to the user as example messages to start a conversation with the Agent. |

```python
class AgentMetadata(core.ModelBase):
    """Metadata for an Agent."""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The name of the Agent."""

    description: typing.Optional[str] = None
    """The description for the Agent."""

    input_placeholder: typing.Optional[str] = pydantic.Field(alias=str("inputPlaceholder"), default=None)  # type: ignore[literal-required]
    """The default text to show as the placeholder input for chats with the Agent."""

    suggested_prompts: typing.List[str] = pydantic.Field(alias=str("suggestedPrompts"))  # type: ignore[literal-required]
    """Prompts to show to the user as example messages to start a conversation with the Agent."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AgentMetadata.md)

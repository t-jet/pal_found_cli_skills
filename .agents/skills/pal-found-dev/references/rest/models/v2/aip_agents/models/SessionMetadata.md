# foundry_sdk.v2.aip_agents.models.SessionMetadata


Metadata for a conversation session with an Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| title | title | str | required; no default | The title of the session. |
| created_time | createdTime | core.AwareDatetime | required; no default | The time the session was created. |
| updated_time | updatedTime | core.AwareDatetime | required; no default | The time the session was last updated. |
| message_count | messageCount | int | required; no default | The count of messages in the session.<br>    Includes both user messages and Agent replies, so each complete exchange counts as two messages. |
| estimated_expires_time | estimatedExpiresTime | core.AwareDatetime | required; no default | The estimated time at which the session is due to expire.<br>    Once a session has expired, it can no longer be accessed and a new session must be created.<br>    The expiry time is automatically extended when new exchanges are added to the session. |

```python
class SessionMetadata(core.ModelBase):
    """Metadata for a conversation session with an Agent."""

    title: str
    """The title of the session."""

    created_time: core.AwareDatetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The time the session was created."""

    updated_time: core.AwareDatetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """The time the session was last updated."""

    message_count: int = pydantic.Field(alias=str("messageCount"))  # type: ignore[literal-required]
    """
    The count of messages in the session.
    Includes both user messages and Agent replies, so each complete exchange counts as two messages.
    """

    estimated_expires_time: core.AwareDatetime = pydantic.Field(alias=str("estimatedExpiresTime"))  # type: ignore[literal-required]
    """
    The estimated time at which the session is due to expire.
    Once a session has expired, it can no longer be accessed and a new session must be created.
    The expiry time is automatically extended when new exchanges are added to the session.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionMetadata.md)

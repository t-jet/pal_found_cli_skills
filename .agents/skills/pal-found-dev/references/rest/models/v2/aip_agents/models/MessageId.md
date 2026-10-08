# foundry_sdk.v2.aip_agents.models.MessageId



An ephemeral client-generated Universally Unique Identifier (UUID) to identify a message for streamed session responses.
This can be used by clients to cancel a streamed exchange.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MessageId: typing_extensions.TypeAlias = core.UUID
```

## Referenced definitions

- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MessageId.md)

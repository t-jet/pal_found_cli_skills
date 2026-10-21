# foundry_sdk.v2.aip_agents.models.CancelSessionResponse


CancelSessionResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| result | result | typing.Optional[SessionExchangeResult] | None | If the `response` field was specified, this returns the result that was added to the session for the canceled exchange, with the client-provided response.<br>    If no `response` was specified in the request, this returns an empty response, as no exchange was added to the session. |

```python
class CancelSessionResponse(core.ModelBase):
    """CancelSessionResponse"""

    result: typing.Optional[SessionExchangeResult] = None
    """
    If the `response` field was specified, this returns the result that was added to the session for the canceled exchange, with the client-provided response.
    If no `response` was specified in the request, this returns an empty response, as no exchange was added to the session.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeResult](SessionExchangeResult.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CancelSessionResponse.md)

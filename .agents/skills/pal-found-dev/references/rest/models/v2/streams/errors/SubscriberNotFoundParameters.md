# foundry_sdk.v2.streams.errors.SubscriberNotFoundParameters


No subscriber with the given ID was found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subscriberId | subscriberId | streams_models.SubscriberId | TypedDict key required | No additional field description in SDK source. |

```python
class SubscriberNotFoundParameters(typing_extensions.TypedDict):
    """No subscriber with the given ID was found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subscriberId: streams_models.SubscriberId
```

## Referenced definitions

- [foundry_sdk.v2.streams.models.SubscriberId](../models/SubscriberId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SubscriberNotFoundParameters.md)

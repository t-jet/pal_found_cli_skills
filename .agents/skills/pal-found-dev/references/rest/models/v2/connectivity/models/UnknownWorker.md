# foundry_sdk.v2.connectivity.models.UnknownWorker


A ConnectionWorker that is not supported in the Platform APIs. This can happen because either the
ConnectionWorker configuration is malformed, or because the ConnectionWorker is a legacy one.
The ConnectionWorker should be updated to use the [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker)
with either direct egress policies or agent proxy egress policies.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['unknownWorker'] | 'unknownWorker' | No additional field description in SDK source. |

```python
class UnknownWorker(core.ModelBase):
    """
    A ConnectionWorker that is not supported in the Platform APIs. This can happen because either the
    ConnectionWorker configuration is malformed, or because the ConnectionWorker is a legacy one.
    The ConnectionWorker should be updated to use the [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker)
    with either direct egress policies or agent proxy egress policies.
    """

    type: typing.Literal["unknownWorker"] = "unknownWorker"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UnknownWorker.md)

# foundry_sdk.v2.functions.models.GetResultExecutionRequest


GetResultExecutionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| timeout | timeout | typing.Optional[int] | None | Maximum time in seconds to hold the connection open while waiting<br>    for execution to complete. Default: 0 (immediate status check).<br>    Values above 280 are clamped to 280. |

```python
class GetResultExecutionRequest(core.ModelBase):
    """GetResultExecutionRequest"""

    timeout: typing.Optional[int] = None
    """
    Maximum time in seconds to hold the connection open while waiting
    for execution to complete. Default: 0 (immediate status check).
    Values above 280 are clamped to 280.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetResultExecutionRequest.md)

# foundry_sdk.v2.streams.models.LatestPosition


Start reading from the current end of the stream. Sets offsets to the latest available
offset for each partition, meaning the subscriber will only receive records published
after this point.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['latest'] | 'latest' | No additional field description in SDK source. |

```python
class LatestPosition(core.ModelBase):
    """
    Start reading from the current end of the stream. Sets offsets to the latest available
    offset for each partition, meaning the subscriber will only receive records published
    after this point.
    """

    type: typing.Literal["latest"] = "latest"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LatestPosition.md)

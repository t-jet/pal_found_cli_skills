# foundry_sdk.v2.streams.models.RecordWithOffset


A record retrieved from a stream, including its offset within the partition.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| offset | offset | core.Long | required; no default | The offset of the record within the partition. |
| value | value | Record | required; no default | The record value as a map of field names to values. |

```python
class RecordWithOffset(core.ModelBase):
    """A record retrieved from a stream, including its offset within the partition."""

    offset: core.Long
    """The offset of the record within the partition."""

    value: Record
    """The record value as a map of field names to values."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)
- [foundry_sdk.v2.streams.models.Record](Record.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RecordWithOffset.md)

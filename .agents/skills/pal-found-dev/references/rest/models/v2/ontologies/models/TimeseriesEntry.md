# foundry_sdk.v2.ontologies.models.TimeseriesEntry


A time and value pair.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| time | time | core.AwareDatetime | required; no default | An ISO 8601 timestamp |
| value | value | typing.Any | required; no default | An object which is either an enum String, double number, or a geopoint. |

```python
class TimeseriesEntry(core.ModelBase):
    """A time and value pair."""

    time: core.AwareDatetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String, double number, or a geopoint."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeseriesEntry.md)

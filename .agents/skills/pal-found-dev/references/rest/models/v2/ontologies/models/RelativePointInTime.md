# foundry_sdk.v2.ontologies.models.RelativePointInTime


A point in time specified relative to query execution time.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value | value | int | required; no default | The numeric value of the time offset. Negative values indicate the past, positive values the future. |
| time_unit | timeUnit | RelativeTimeUnit | required; no default | The unit of time for the value. |
| type | type | typing.Literal['relativePoint'] | 'relativePoint' | No additional field description in SDK source. |

```python
class RelativePointInTime(core.ModelBase):
    """A point in time specified relative to query execution time."""

    value: int
    """The numeric value of the time offset. Negative values indicate the past, positive values the future."""

    time_unit: RelativeTimeUnit = pydantic.Field(alias=str("timeUnit"))  # type: ignore[literal-required]
    """The unit of time for the value."""

    type: typing.Literal["relativePoint"] = "relativePoint"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.RelativeTimeUnit](RelativeTimeUnit.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RelativePointInTime.md)

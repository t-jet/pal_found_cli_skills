# foundry_sdk.v2.ontologies.models.NumberFormatDuration


Format numeric values representing time durations.
- Human readable: 3661 seconds displays as "1h 1m 1s"
- Timecode: 3661 seconds displays as "01:01:01"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format_style | formatStyle | DurationFormatStyle | required; no default | No additional field description in SDK source. |
| precision | precision | typing.Optional[DurationPrecision] | None | No additional field description in SDK source. |
| base_value | baseValue | DurationBaseValue | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['duration'] | 'duration' | No additional field description in SDK source. |

```python
class NumberFormatDuration(core.ModelBase):
    """
    Format numeric values representing time durations.
    - Human readable: 3661 seconds displays as "1h 1m 1s"
    - Timecode: 3661 seconds displays as "01:01:01"
    """

    format_style: DurationFormatStyle = pydantic.Field(alias=str("formatStyle"))  # type: ignore[literal-required]
    precision: typing.Optional[DurationPrecision] = None
    base_value: DurationBaseValue = pydantic.Field(alias=str("baseValue"))  # type: ignore[literal-required]
    type: typing.Literal["duration"] = "duration"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DurationBaseValue](DurationBaseValue.md)
- [foundry_sdk.v2.ontologies.models.DurationFormatStyle](DurationFormatStyle.md)
- [foundry_sdk.v2.ontologies.models.DurationPrecision](DurationPrecision.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatDuration.md)

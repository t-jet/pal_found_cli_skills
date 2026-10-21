# foundry_sdk.v2.ontologies.models.RelativeDateRangeQuery


This query filters a date or timestamp property against a range evaluated at query time. Supply either `field` or `property_identifier`, inclusive start and exclusive end bounds as needed, and a valid IANA time-zone ID such as `Etc/UTC`. Bounds are rounded to midnight in that zone, so the zone can change which records match.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | typing.Optional[PropertyApiName] | None | The property API name to filter on (either field or propertyIdentifier must be provided). |
| property_identifier | propertyIdentifier | typing.Optional[PropertyIdentifier] | default None | The property identifier to filter on (either field or propertyIdentifier must be provided). |
| relative_start_time | relativeStartTime | typing.Optional[RelativeDateRangeBound] | default None | The lower bound relative to query time (inclusive). Negative values go into the past.<br>    For example, { value: -7, timeUnit: DAY } means 7 days ago. |
| relative_end_time | relativeEndTime | typing.Optional[RelativeDateRangeBound] | default None | The upper bound relative to query time (exclusive). Negative values go into the past.<br>    For example, { value: 1, timeUnit: MONTH } means the start of next month. |
| time_zone_id | timeZoneId | str | required; no default | Time zone ID for midnight calculation (e.g., "America/New_York", "Europe/London", "Etc/UTC").<br>    Use an IANA time-zone ID such as Etc/UTC, Europe/London or America/New_York. |
| type | type | typing.Literal['relativeDateRange'] | 'relativeDateRange' | No additional field description in SDK source. |

```python
class RelativeDateRangeQuery(core.ModelBase):
    """
    Returns objects where the specified date or timestamp property falls within a relative date range.
    The bounds are calculated relative to query execution time and rounded to midnight in the specified timezone.
    """

    field: typing.Optional[PropertyApiName] = None
    """The property API name to filter on (either field or propertyIdentifier must be provided)."""

    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    """The property identifier to filter on (either field or propertyIdentifier must be provided)."""

    relative_start_time: typing.Optional[RelativeDateRangeBound] = pydantic.Field(alias=str("relativeStartTime"), default=None)  # type: ignore[literal-required]
    """
    The lower bound relative to query time (inclusive). Negative values go into the past.
    For example, { value: -7, timeUnit: DAY } means 7 days ago.
    """

    relative_end_time: typing.Optional[RelativeDateRangeBound] = pydantic.Field(alias=str("relativeEndTime"), default=None)  # type: ignore[literal-required]
    """
    The upper bound relative to query time (exclusive). Negative values go into the past.
    For example, { value: 1, timeUnit: MONTH } means the start of next month.
    """

    time_zone_id: str = pydantic.Field(alias=str("timeZoneId"))  # type: ignore[literal-required]
    """
    Time zone ID for midnight calculation (e.g., "America/New_York", "Europe/London", "Etc/UTC").
    See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid values.
    """

    type: typing.Literal["relativeDateRange"] = "relativeDateRange"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.RelativeDateRangeBound](RelativeDateRangeBound.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RelativeDateRangeQuery.md)

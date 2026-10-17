# foundry_sdk.v2.ontologies.models.RelativeTimeRange


A relative time range for a time series query.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| start_time | startTime | typing.Optional[RelativeTime] | default None | No additional field description in SDK source. |
| end_time | endTime | typing.Optional[RelativeTime] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['relative'] | 'relative' | No additional field description in SDK source. |

```python
class RelativeTimeRange(core.ModelBase):
    """A relative time range for a time series query."""

    start_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["relative"] = "relative"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.RelativeTime](RelativeTime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RelativeTimeRange.md)

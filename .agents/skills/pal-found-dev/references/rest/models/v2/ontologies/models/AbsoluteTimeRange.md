# foundry_sdk.v2.ontologies.models.AbsoluteTimeRange


ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| start_time | startTime | typing.Optional[core.AwareDatetime] | default None | No additional field description in SDK source. |
| end_time | endTime | typing.Optional[core.AwareDatetime] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['absolute'] | 'absolute' | No additional field description in SDK source. |

```python
class AbsoluteTimeRange(core.ModelBase):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    start_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["absolute"] = "absolute"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AbsoluteTimeRange.md)

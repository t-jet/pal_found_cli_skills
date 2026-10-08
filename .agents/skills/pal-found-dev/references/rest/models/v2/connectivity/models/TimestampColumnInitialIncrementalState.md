# foundry_sdk.v2.connectivity.models.TimestampColumnInitialIncrementalState


TimestampColumnInitialIncrementalState

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| column_name | columnName | str | required; no default | No additional field description in SDK source. |
| current_value | currentValue | core.AwareDatetime | required; no default | The initial incremental state value for the timestamp column in UTC to reference in the query. |
| type | type | typing.Literal['timestampColumnInitialIncrementalState'] | 'timestampColumnInitialIncrementalState' | No additional field description in SDK source. |

```python
class TimestampColumnInitialIncrementalState(core.ModelBase):
    """TimestampColumnInitialIncrementalState"""

    column_name: str = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    current_value: core.AwareDatetime = pydantic.Field(alias=str("currentValue"))  # type: ignore[literal-required]
    """The initial incremental state value for the timestamp column in UTC to reference in the query."""

    type: typing.Literal["timestampColumnInitialIncrementalState"] = (
        "timestampColumnInitialIncrementalState"
    )
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimestampColumnInitialIncrementalState.md)

# foundry_sdk.v2.data_health.models.ReplaceTimeSinceLastUpdatedCheckConfig


ReplaceTimeSinceLastUpdatedCheckConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| time_check_config | timeCheckConfig | TransactionTimeCheckConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['timeSinceLastUpdated'] | 'timeSinceLastUpdated' | No additional field description in SDK source. |

```python
class ReplaceTimeSinceLastUpdatedCheckConfig(core.ModelBase):
    """ReplaceTimeSinceLastUpdatedCheckConfig"""

    time_check_config: TransactionTimeCheckConfig = pydantic.Field(alias=str("timeCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["timeSinceLastUpdated"] = "timeSinceLastUpdated"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.TransactionTimeCheckConfig](TransactionTimeCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceTimeSinceLastUpdatedCheckConfig.md)

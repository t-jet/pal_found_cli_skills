# foundry_sdk.v2.data_health.models.NullPercentageCheckConfig


Checks the percentage of null values in a specific column.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subject | subject | DatasetSubject | required; no default | No additional field description in SDK source. |
| percentage_check_config | percentageCheckConfig | PercentageCheckConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['nullPercentage'] | 'nullPercentage' | No additional field description in SDK source. |

```python
class NullPercentageCheckConfig(core.ModelBase):
    """Checks the percentage of null values in a specific column."""

    subject: DatasetSubject
    percentage_check_config: PercentageCheckConfig = pydantic.Field(alias=str("percentageCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["nullPercentage"] = "nullPercentage"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.DatasetSubject](DatasetSubject.md)
- [foundry_sdk.v2.data_health.models.PercentageCheckConfig](PercentageCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NullPercentageCheckConfig.md)

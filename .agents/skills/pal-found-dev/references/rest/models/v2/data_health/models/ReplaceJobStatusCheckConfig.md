# foundry_sdk.v2.data_health.models.ReplaceJobStatusCheckConfig


ReplaceJobStatusCheckConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| status_check_config | statusCheckConfig | StatusCheckConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['jobStatus'] | 'jobStatus' | No additional field description in SDK source. |

```python
class ReplaceJobStatusCheckConfig(core.ModelBase):
    """ReplaceJobStatusCheckConfig"""

    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["jobStatus"] = "jobStatus"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.StatusCheckConfig](StatusCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceJobStatusCheckConfig.md)

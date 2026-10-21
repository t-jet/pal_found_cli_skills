# foundry_sdk.v2.data_health.models.BuildStatusCheckConfig


Checks the status of the most recent build of the dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subject | subject | DatasetSubject | required; no default | No additional field description in SDK source. |
| status_check_config | statusCheckConfig | StatusCheckConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['buildStatus'] | 'buildStatus' | No additional field description in SDK source. |

```python
class BuildStatusCheckConfig(core.ModelBase):
    """Checks the status of the most recent build of the dataset."""

    subject: DatasetSubject
    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["buildStatus"] = "buildStatus"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.DatasetSubject](DatasetSubject.md)
- [foundry_sdk.v2.data_health.models.StatusCheckConfig](StatusCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BuildStatusCheckConfig.md)

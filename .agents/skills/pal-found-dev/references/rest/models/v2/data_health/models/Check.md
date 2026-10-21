# foundry_sdk.v2.data_health.models.Check


Check

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.CheckRid | required; no default | No additional field description in SDK source. |
| groups | groups | typing.List[CheckGroupRid] | required; no default | No additional field description in SDK source. |
| config | config | CheckConfig | required; no default | No additional field description in SDK source. |
| intent | intent | typing.Optional[CheckIntent] | None | No additional field description in SDK source. |
| created_by | createdBy | typing.Optional[core_models.CreatedBy] | default None | The user that created the Check. |
| updated_time | updatedTime | typing.Optional[core_models.UpdatedTime] | default None | The timestamp when the Check was last updated. |

```python
class Check(core.ModelBase):
    """Check"""

    rid: core_models.CheckRid
    groups: typing.List[CheckGroupRid]
    config: CheckConfig
    intent: typing.Optional[CheckIntent] = None
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    """The user that created the Check."""

    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the Check was last updated."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CheckRid](../../core/models/CheckRid.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../core/models/UpdatedTime.md)
- [foundry_sdk.v2.data_health.models.CheckConfig](CheckConfig.md)
- [foundry_sdk.v2.data_health.models.CheckGroupRid](CheckGroupRid.md)
- [foundry_sdk.v2.data_health.models.CheckIntent](CheckIntent.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Check.md)

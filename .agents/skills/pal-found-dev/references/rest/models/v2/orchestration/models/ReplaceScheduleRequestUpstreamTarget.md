# foundry_sdk.v2.orchestration.models.ReplaceScheduleRequestUpstreamTarget


ReplaceScheduleRequestUpstreamTarget

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ignored_rids | ignoredRids | typing.Optional[typing.List[BuildableRid]] | default None | The datasets to ignore when calculating the final set of dataset to build. |
| target_rids | targetRids | typing.List[BuildableRid] | required; no default | The target datasets. |
| type | type | typing.Literal['upstream'] | 'upstream' | No additional field description in SDK source. |

```python
class ReplaceScheduleRequestUpstreamTarget(core.ModelBase):
    """ReplaceScheduleRequestUpstreamTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets to ignore when calculating the final set of dataset to build."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The target datasets."""

    type: typing.Literal["upstream"] = "upstream"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.orchestration.models.BuildableRid](BuildableRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceScheduleRequestUpstreamTarget.md)

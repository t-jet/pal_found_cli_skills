# foundry_sdk.v2.orchestration.models.CreateScheduleRequestConnectingTarget


CreateScheduleRequestConnectingTarget

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ignored_rids | ignoredRids | typing.Optional[typing.List[BuildableRid]] | default None | The datasets between the input datasets and target datasets to exclude. |
| target_rids | targetRids | typing.List[BuildableRid] | required; no default | The downstream target datasets (inclusive). |
| input_rids | inputRids | typing.List[BuildableRid] | required; no default | The upstream input datasets (exclusive). |
| type | type | typing.Literal['connecting'] | 'connecting' | No additional field description in SDK source. |

```python
class CreateScheduleRequestConnectingTarget(core.ModelBase):
    """CreateScheduleRequestConnectingTarget"""

    ignored_rids: typing.Optional[typing.List[BuildableRid]] = pydantic.Field(alias=str("ignoredRids"), default=None)  # type: ignore[literal-required]
    """The datasets between the input datasets and target datasets to exclude."""

    target_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("targetRids"))  # type: ignore[literal-required]
    """The downstream target datasets (inclusive)."""

    input_rids: typing.List[BuildableRid] = pydantic.Field(alias=str("inputRids"))  # type: ignore[literal-required]
    """The upstream input datasets (exclusive)."""

    type: typing.Literal["connecting"] = "connecting"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.orchestration.models.BuildableRid](BuildableRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateScheduleRequestConnectingTarget.md)

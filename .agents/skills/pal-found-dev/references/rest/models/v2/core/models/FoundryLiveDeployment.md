# foundry_sdk.v2.core.models.FoundryLiveDeployment


FoundryLiveDeployment

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | typing.Optional[core.RID] | None | The live deployment identifier. This rid is of the format 'ri.foundry-ml-live.main.live-deployment.<uuid>'. |
| input_param_name | inputParamName | typing.Optional[str] | default None | The name of the input parameter to the model which should contain the query string. |
| output_param_name | outputParamName | typing.Optional[str] | default None | The name of the output parameter to the model which should contain the computed embedding. |
| type | type | typing.Literal['foundryLiveDeployment'] | 'foundryLiveDeployment' | No additional field description in SDK source. |

```python
class FoundryLiveDeployment(core.ModelBase):
    """FoundryLiveDeployment"""

    rid: typing.Optional[core.RID] = None
    """The live deployment identifier. This rid is of the format 'ri.foundry-ml-live.main.live-deployment.<uuid>'."""

    input_param_name: typing.Optional[str] = pydantic.Field(alias=str("inputParamName"), default=None)  # type: ignore[literal-required]
    """The name of the input parameter to the model which should contain the query string."""

    output_param_name: typing.Optional[str] = pydantic.Field(alias=str("outputParamName"), default=None)  # type: ignore[literal-required]
    """The name of the output parameter to the model which should contain the computed embedding."""

    type: typing.Literal["foundryLiveDeployment"] = "foundryLiveDeployment"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FoundryLiveDeployment.md)

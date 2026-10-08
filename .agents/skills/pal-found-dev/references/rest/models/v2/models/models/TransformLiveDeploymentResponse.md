# foundry_sdk.v2.models.models.TransformLiveDeploymentResponse


The response from transforming input data using a live deployment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| output | output | typing.Dict[str, typing.Any] | required; no default | The output data from the model inference. The structure depends on the model's defined API specification, where each key is an output name and the value is the corresponding output data. |

```python
class TransformLiveDeploymentResponse(core.ModelBase):
    """The response from transforming input data using a live deployment."""

    output: typing.Dict[str, typing.Any]
    """The output data from the model inference. The structure depends on the model's defined API specification, where each key is an output name and the value is the corresponding output data."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TransformLiveDeploymentResponse.md)

# foundry_sdk.v2.models.errors.InferenceTimeoutParameters


The live deployment took longer than 5 minutes to respond to the inference request.
This typically indicates the model execution is taking too long or the deployment is under heavy load.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| liveDeploymentRid | liveDeploymentRid | models_models.LiveDeploymentRid | TypedDict key required | No additional field description in SDK source. |

```python
class InferenceTimeoutParameters(typing_extensions.TypedDict):
    """
    The live deployment took longer than 5 minutes to respond to the inference request.
    This typically indicates the model execution is taking too long or the deployment is under heavy load.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid
```

## Referenced definitions

- [foundry_sdk.v2.models.models.LiveDeploymentRid](../models/LiveDeploymentRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InferenceTimeoutParameters.md)

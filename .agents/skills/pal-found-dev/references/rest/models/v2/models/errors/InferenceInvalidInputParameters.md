# foundry_sdk.v2.models.errors.InferenceInvalidInputParameters


The inference request contains invalid input data that does not match the model's API specification.
Check the error type for specific validation failure details.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| liveDeploymentRid | liveDeploymentRid | models_models.LiveDeploymentRid | TypedDict key required | No additional field description in SDK source. |
| errorType | errorType | models_models.InferenceInputErrorType | TypedDict key required | The specific type and details of the input validation error |

```python
class InferenceInvalidInputParameters(typing_extensions.TypedDict):
    """
    The inference request contains invalid input data that does not match the model's API specification.
    Check the error type for specific validation failure details.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    liveDeploymentRid: models_models.LiveDeploymentRid
    errorType: models_models.InferenceInputErrorType
    """The specific type and details of the input validation error"""
```

## Referenced definitions

- [foundry_sdk.v2.models.models.InferenceInputErrorType](../models/InferenceInputErrorType.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRid](../models/LiveDeploymentRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InferenceInvalidInputParameters.md)

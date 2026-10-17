# foundry_sdk.v2.models.errors.GpuTypeNotAvailableParameters


The requested GPU type is not available. Use a GPU type that is available in
the deployment's resource queue.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| requestedGpuType | requestedGpuType | models_models.GpuType | TypedDict key required | The GPU type that was requested. |
| availableGpuTypes | availableGpuTypes | typing.List[models_models.GpuType] | TypedDict key required | The GPU types available in the resource queue. |

```python
class GpuTypeNotAvailableParameters(typing_extensions.TypedDict):
    """
    The requested GPU type is not available. Use a GPU type that is available in
    the deployment's resource queue.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestedGpuType: models_models.GpuType
    """The GPU type that was requested."""

    availableGpuTypes: typing.List[models_models.GpuType]
    """The GPU types available in the resource queue."""
```

## Referenced definitions

- [foundry_sdk.v2.models.models.GpuType](../models/GpuType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GpuTypeNotAvailableParameters.md)

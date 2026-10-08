# foundry_sdk.v2.models.models.ModelApi


The Model API is a specification that describes the inputs and outputs of a machine learning model. It is used to define the interface for the model, including the types of data that can be passed to it and the types of data that it will return.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| inputs | inputs | typing.List[ModelApiInput] | required; no default | No additional field description in SDK source. |
| outputs | outputs | typing.List[ModelApiOutput] | required; no default | No additional field description in SDK source. |

```python
class ModelApi(core.ModelBase):
    """The Model API is a specification that describes the inputs and outputs of a machine learning model. It is used to define the interface for the model, including the types of data that can be passed to it and the types of data that it will return."""

    inputs: typing.List[ModelApiInput]
    outputs: typing.List[ModelApiOutput]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelApiInput](ModelApiInput.md)
- [foundry_sdk.v2.models.models.ModelApiOutput](ModelApiOutput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelApi.md)

# foundry_sdk.v2.models.models.ModelStudioWorkerConfig


Configuration for the Model Studio worker.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| custom_config | customConfig | typing.Optional[typing.Dict[str, typing.Any]] | default None | Custom configuration matching the trainer's JSON schema. |
| inputs | inputs | typing.Dict[InputAlias, ModelStudioInput] | required; no default | Input configurations keyed by alias. |
| outputs | outputs | typing.Dict[OutputAlias, ModelStudioOutput] | required; no default | Output configurations keyed by alias. |

```python
class ModelStudioWorkerConfig(core.ModelBase):
    """Configuration for the Model Studio worker."""

    custom_config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(alias=str("customConfig"), default=None)  # type: ignore[literal-required]
    """Custom configuration matching the trainer's JSON schema."""

    inputs: typing.Dict[InputAlias, ModelStudioInput]
    """Input configurations keyed by alias."""

    outputs: typing.Dict[OutputAlias, ModelStudioOutput]
    """Output configurations keyed by alias."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.InputAlias](InputAlias.md)
- [foundry_sdk.v2.models.models.ModelStudioInput](ModelStudioInput.md)
- [foundry_sdk.v2.models.models.ModelStudioOutput](ModelStudioOutput.md)
- [foundry_sdk.v2.models.models.OutputAlias](OutputAlias.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelStudioWorkerConfig.md)

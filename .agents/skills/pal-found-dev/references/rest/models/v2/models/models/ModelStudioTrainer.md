# foundry_sdk.v2.models.models.ModelStudioTrainer


ModelStudioTrainer

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| trainer_id | trainerId | TrainerId | required; no default | No additional field description in SDK source. |
| version | version | TrainerVersion | required; no default | The version of this trainer. |
| name | name | TrainerName | required; no default | Human-readable name of the trainer. |
| type | type | TrainerType | required; no default | The category of machine learning task this trainer is designed to solve. |
| description | description | TrainerDescription | required; no default | Description of what this trainer does and its capabilities. |
| custom_config_schema | customConfigSchema | TrainerSchemaDefinition | required; no default | JSON schema defining the custom configuration parameters for this trainer. |
| inputs | inputs | TrainerInputsSpecification | required; no default | Input specifications for this trainer. |
| outputs | outputs | TrainerOutputsSpecification | required; no default | Output specifications for this trainer. |
| experimental | experimental | ModelStudioTrainerExperimental | required; no default | Whether this trainer is experimental and may have breaking changes. |

```python
class ModelStudioTrainer(core.ModelBase):
    """ModelStudioTrainer"""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    version: TrainerVersion
    """The version of this trainer."""

    name: TrainerName
    """Human-readable name of the trainer."""

    type: TrainerType
    """The category of machine learning task this trainer is designed to solve."""

    description: TrainerDescription
    """Description of what this trainer does and its capabilities."""

    custom_config_schema: TrainerSchemaDefinition = pydantic.Field(alias=str("customConfigSchema"))  # type: ignore[literal-required]
    """JSON schema defining the custom configuration parameters for this trainer."""

    inputs: TrainerInputsSpecification
    """Input specifications for this trainer."""

    outputs: TrainerOutputsSpecification
    """Output specifications for this trainer."""

    experimental: ModelStudioTrainerExperimental
    """Whether this trainer is experimental and may have breaking changes."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelStudioTrainerExperimental](ModelStudioTrainerExperimental.md)
- [foundry_sdk.v2.models.models.TrainerDescription](TrainerDescription.md)
- [foundry_sdk.v2.models.models.TrainerId](TrainerId.md)
- [foundry_sdk.v2.models.models.TrainerInputsSpecification](TrainerInputsSpecification.md)
- [foundry_sdk.v2.models.models.TrainerName](TrainerName.md)
- [foundry_sdk.v2.models.models.TrainerOutputsSpecification](TrainerOutputsSpecification.md)
- [foundry_sdk.v2.models.models.TrainerSchemaDefinition](TrainerSchemaDefinition.md)
- [foundry_sdk.v2.models.models.TrainerType](TrainerType.md)
- [foundry_sdk.v2.models.models.TrainerVersion](TrainerVersion.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelStudioTrainer.md)

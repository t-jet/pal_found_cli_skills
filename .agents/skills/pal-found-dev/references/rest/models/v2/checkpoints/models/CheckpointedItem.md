# foundry_sdk.v2.checkpoints.models.CheckpointedItem


Snapshot of the entity that was captured in a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckpointedItem: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "CheckpointedIssue",
        "CheckpointedJob",
        "CheckpointedSchedule",
        "CheckpointedResource",
        "CheckpointedJobSpecification",
        "CheckpointedLanguageModel",
        "CheckpointedGroup",
        "CheckpointedUserIntakeSubmission",
        "CheckpointedObjectSet",
        "CheckpointedMarking",
        "CheckpointedMarketplaceProduct",
        "CheckpointedPeeringJob",
        "CheckpointedRole",
        "CheckpointedIntervention",
        "CheckpointedLanguageModelSession",
        "CheckpointedToken",
        "CheckpointedUserIntakeFormInput",
        "CheckpointedPrincipal",
        "CheckpointedActionType",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.checkpoints.models.CheckpointedActionType](CheckpointedActionType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedGroup](CheckpointedGroup.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIntervention](CheckpointedIntervention.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIssue](CheckpointedIssue.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJob](CheckpointedJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobSpecification](CheckpointedJobSpecification.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModel](CheckpointedLanguageModel.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelSession](CheckpointedLanguageModelSession.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarketplaceProduct](CheckpointedMarketplaceProduct.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarking](CheckpointedMarking.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSet](CheckpointedObjectSet.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJob](CheckpointedPeeringJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipal](CheckpointedPrincipal.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResource](CheckpointedResource.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedRole](CheckpointedRole.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedSchedule](CheckpointedSchedule.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedToken](CheckpointedToken.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeFormInput](CheckpointedUserIntakeFormInput.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeSubmission](CheckpointedUserIntakeSubmission.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedItem.md)

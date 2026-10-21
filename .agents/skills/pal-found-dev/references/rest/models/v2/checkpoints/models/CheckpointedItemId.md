# foundry_sdk.v2.checkpoints.models.CheckpointedItemId



Identifier for a checkpointed item. This union type explicitly identifies the type of item
being referenced, eliminating ambiguity between RIDs and string IDs.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckpointedItemId: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "CheckpointedJobRid",
        "CheckpointedMarkingId",
        "CheckpointedTokenId",
        "CheckpointedGroupId",
        "CheckpointedObjectSetVersionedRid",
        "CheckpointedObjectSetTypesProxyRids",
        "CheckpointedResourceRid",
        "CheckpointedPeeringJobId",
        "CheckpointedIssueRid",
        "CheckpointedInterventionRid",
        "CheckpointedJobSpecRid",
        "CheckpointedActionTypeRid",
        "CheckpointedScheduleRid",
        "CheckpointedRoleId",
        "CheckpointedUserIntakeFormInputId",
        "CheckpointedMarketplaceProductId",
        "CheckpointedLanguageModelRid",
        "CheckpointedPrincipalId",
        "CheckpointedLanguageModelSessionRid",
        "CheckpointedUserIntakeSubmissionRid",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.checkpoints.models.CheckpointedActionTypeRid](CheckpointedActionTypeRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedGroupId](CheckpointedGroupId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedInterventionRid](CheckpointedInterventionRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIssueRid](CheckpointedIssueRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobRid](CheckpointedJobRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobSpecRid](CheckpointedJobSpecRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelRid](CheckpointedLanguageModelRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelSessionRid](CheckpointedLanguageModelSessionRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarketplaceProductId](CheckpointedMarketplaceProductId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarkingId](CheckpointedMarkingId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetTypesProxyRids](CheckpointedObjectSetTypesProxyRids.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetVersionedRid](CheckpointedObjectSetVersionedRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJobId](CheckpointedPeeringJobId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipalId](CheckpointedPrincipalId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResourceRid](CheckpointedResourceRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedRoleId](CheckpointedRoleId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedScheduleRid](CheckpointedScheduleRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedTokenId](CheckpointedTokenId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeFormInputId](CheckpointedUserIntakeFormInputId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeSubmissionRid](CheckpointedUserIntakeSubmissionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedItemId.md)

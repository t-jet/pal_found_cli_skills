# foundry_sdk.v2.checkpoints.models.Record


Record

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | RecordRid | required; no default | No additional field description in SDK source. |
| config_rid | configRid | typing.Optional[ConfigRid] | default None | No additional field description in SDK source. |
| type | type | CheckpointType | required; no default | No additional field description in SDK source. |
| scope | scope | Scope | required; no default | No additional field description in SDK source. |
| acting_user | actingUser | ActingUser | required; no default | No additional field description in SDK source. |
| delegate_user_id | delegateUserId | typing.Optional[core_models.UserId] | default None | No additional field description in SDK source. |
| created_at | createdAt | RecordCreatedAt | required; no default | No additional field description in SDK source. |
| checkpointed_items | checkpointedItems | typing.List[CheckpointedItem] | required; no default | No additional field description in SDK source. |
| justification | justification | Justification | required; no default | No additional field description in SDK source. |
| project_rid | projectRid | typing.Optional[ProjectRid] | default None | No additional field description in SDK source. |
| organization_rid | organizationRid | typing.Optional[OrganizationRid] | default None | No additional field description in SDK source. |
| namespace_rid | namespaceRid | typing.Optional[NamespaceRid] | default None | No additional field description in SDK source. |
| interaction_rid | interactionRid | typing.Optional[InteractionRid] | default None | No additional field description in SDK source. |
| approvals_metadata | approvalsMetadata | typing.Optional[ApprovalsMetadata] | default None | No additional field description in SDK source. |

```python
class Record(core.ModelBase):
    """Record"""

    rid: RecordRid
    config_rid: typing.Optional[ConfigRid] = pydantic.Field(alias=str("configRid"), default=None)  # type: ignore[literal-required]
    type: CheckpointType
    scope: Scope
    acting_user: ActingUser = pydantic.Field(alias=str("actingUser"))  # type: ignore[literal-required]
    delegate_user_id: typing.Optional[core_models.UserId] = pydantic.Field(alias=str("delegateUserId"), default=None)  # type: ignore[literal-required]
    created_at: RecordCreatedAt = pydantic.Field(alias=str("createdAt"))  # type: ignore[literal-required]
    checkpointed_items: typing.List[CheckpointedItem] = pydantic.Field(alias=str("checkpointedItems"))  # type: ignore[literal-required]
    justification: Justification
    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    organization_rid: typing.Optional[OrganizationRid] = pydantic.Field(alias=str("organizationRid"), default=None)  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    interaction_rid: typing.Optional[InteractionRid] = pydantic.Field(alias=str("interactionRid"), default=None)  # type: ignore[literal-required]
    approvals_metadata: typing.Optional[ApprovalsMetadata] = pydantic.Field(alias=str("approvalsMetadata"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.ActingUser](ActingUser.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsMetadata](ApprovalsMetadata.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointType](CheckpointType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedItem](CheckpointedItem.md)
- [foundry_sdk.v2.checkpoints.models.ConfigRid](ConfigRid.md)
- [foundry_sdk.v2.checkpoints.models.InteractionRid](InteractionRid.md)
- [foundry_sdk.v2.checkpoints.models.Justification](Justification.md)
- [foundry_sdk.v2.checkpoints.models.NamespaceRid](NamespaceRid.md)
- [foundry_sdk.v2.checkpoints.models.OrganizationRid](OrganizationRid.md)
- [foundry_sdk.v2.checkpoints.models.ProjectRid](ProjectRid.md)
- [foundry_sdk.v2.checkpoints.models.RecordCreatedAt](RecordCreatedAt.md)
- [foundry_sdk.v2.checkpoints.models.RecordRid](RecordRid.md)
- [foundry_sdk.v2.checkpoints.models.Scope](Scope.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Record.md)

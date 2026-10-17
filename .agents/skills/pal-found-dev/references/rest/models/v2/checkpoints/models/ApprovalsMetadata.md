# foundry_sdk.v2.checkpoints.models.ApprovalsMetadata


Metadata linking a checkpoint record to an Approvals workflow.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| approvals_task_id | approvalsTaskId | ApprovalsTaskId | required; no default | No additional field description in SDK source. |
| approvals_subtask_ids | approvalsSubtaskIds | typing.List[ApprovalsSubtaskId] | required; no default | No additional field description in SDK source. |

```python
class ApprovalsMetadata(core.ModelBase):
    """Metadata linking a checkpoint record to an Approvals workflow."""

    approvals_task_id: ApprovalsTaskId = pydantic.Field(alias=str("approvalsTaskId"))  # type: ignore[literal-required]
    approvals_subtask_ids: typing.List[ApprovalsSubtaskId] = pydantic.Field(alias=str("approvalsSubtaskIds"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsSubtaskId](ApprovalsSubtaskId.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsTaskId](ApprovalsTaskId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ApprovalsMetadata.md)

# foundry_sdk.v2.orchestration.models.MediaSetUpdatedTrigger


Trigger whenever an update is made to a media set on the target
branch. For transactional media sets, this happens when a transaction
is committed. For non-transactional media sets, this event happens
eventually (but not necessary immediately) after an update.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| media_set_rid | mediaSetRid | core_models.MediaSetRid | required; no default | No additional field description in SDK source. |
| branch_name | branchName | core_models.BranchName | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['mediaSetUpdated'] | 'mediaSetUpdated' | No additional field description in SDK source. |

```python
class MediaSetUpdatedTrigger(core.ModelBase):
    """
    Trigger whenever an update is made to a media set on the target
    branch. For transactional media sets, this happens when a transaction
    is committed. For non-transactional media sets, this event happens
    eventually (but not necessary immediately) after an update.
    """

    media_set_rid: core_models.MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["mediaSetUpdated"] = "mediaSetUpdated"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../core/models/MediaSetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MediaSetUpdatedTrigger.md)

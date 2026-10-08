# foundry_sdk.v2.media_sets.models.GetMediaSetResponse


Information about a media set.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.MediaSetRid | required; no default | No additional field description in SDK source. |
| media_schema | mediaSchema | MediaSchema | required; no default | No additional field description in SDK source. |
| default_branch_name | defaultBranchName | BranchName | required; no default | No additional field description in SDK source. |
| transaction_policy | transactionPolicy | TransactionPolicy | required; no default | No additional field description in SDK source. |
| paths_required | pathsRequired | bool | required; no default | Whether media items in this media set require paths. |

```python
class GetMediaSetResponse(core.ModelBase):
    """Information about a media set."""

    rid: core_models.MediaSetRid
    media_schema: MediaSchema = pydantic.Field(alias=str("mediaSchema"))  # type: ignore[literal-required]
    default_branch_name: BranchName = pydantic.Field(alias=str("defaultBranchName"))  # type: ignore[literal-required]
    transaction_policy: TransactionPolicy = pydantic.Field(alias=str("transactionPolicy"))  # type: ignore[literal-required]
    paths_required: bool = pydantic.Field(alias=str("pathsRequired"))  # type: ignore[literal-required]
    """Whether media items in this media set require paths."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../core/models/MediaSetRid.md)
- [foundry_sdk.v2.media_sets.models.BranchName](BranchName.md)
- [foundry_sdk.v2.media_sets.models.MediaSchema](MediaSchema.md)
- [foundry_sdk.v2.media_sets.models.TransactionPolicy](TransactionPolicy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetMediaSetResponse.md)

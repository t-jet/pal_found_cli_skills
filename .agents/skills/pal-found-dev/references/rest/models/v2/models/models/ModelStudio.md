# foundry_sdk.v2.models.models.ModelStudio


ModelStudio

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ModelStudioRid | required; no default | No additional field description in SDK source. |
| folder_rid | folderRid | filesystem_models.FolderRid | required; no default | The parent folder containing this Model Studio. |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |

```python
class ModelStudio(core.ModelBase):
    """ModelStudio"""

    rid: ModelStudioRid
    folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("folderRid"))  # type: ignore[literal-required]
    """The parent folder containing this Model Studio."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](ModelStudioRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelStudio.md)

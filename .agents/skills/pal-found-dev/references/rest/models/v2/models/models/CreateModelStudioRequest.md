# foundry_sdk.v2.models.models.CreateModelStudioRequest


CreateModelStudioRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | str | required; no default | The name of the Model Studio. |
| parent_folder_rid | parentFolderRid | filesystem_models.FolderRid | required; no default | The RID of the parent folder where the studio will be created. |

```python
class CreateModelStudioRequest(core.ModelBase):
    """CreateModelStudioRequest"""

    name: str
    """The name of the Model Studio."""

    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The RID of the parent folder where the studio will be created."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateModelStudioRequest.md)

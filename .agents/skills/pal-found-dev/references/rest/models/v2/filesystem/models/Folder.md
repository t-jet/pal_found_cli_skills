# foundry_sdk.v2.filesystem.models.Folder


Folder

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | FolderRid | required; no default | No additional field description in SDK source. |
| display_name | displayName | ResourceDisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description associated with the Folder. |
| documentation | documentation | typing.Optional[str] | None | The documentation associated with the Folder. |
| path | path | ResourcePath | required; no default | No additional field description in SDK source. |
| type | type | FolderType | required; no default | No additional field description in SDK source. |
| created_by | createdBy | core_models.CreatedBy | required; no default | No additional field description in SDK source. |
| updated_by | updatedBy | core_models.UpdatedBy | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |
| updated_time | updatedTime | core_models.UpdatedTime | required; no default | No additional field description in SDK source. |
| trash_status | trashStatus | TrashStatus | required; no default | The trash status of the Folder. If trashed, this could either be because the Folder itself has been<br>    trashed or because one of its ancestors has been trashed. |
| parent_folder_rid | parentFolderRid | FolderRid | required; no default | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,<br>    this value will be the root folder (`ri.compass.main.folder.0`). |
| project_rid | projectRid | typing.Optional[ProjectRid] | default None | The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will<br>    not be defined. |
| space_rid | spaceRid | SpaceRid | required; no default | The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will<br>    be the same as the Folder RID. |

```python
class Folder(core.ModelBase):
    """Folder"""

    rid: FolderRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description associated with the Folder."""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Folder."""

    path: ResourcePath
    type: FolderType
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the Folder. If trashed, this could either be because the Folder itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """
    The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
    this value will be the root folder (`ri.compass.main.folder.0`).
    """

    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    not be defined.
    """

    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """
    The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    be the same as the Folder RID.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../core/models/UpdatedTime.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](FolderRid.md)
- [foundry_sdk.v2.filesystem.models.FolderType](FolderType.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](TrashStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Folder.md)

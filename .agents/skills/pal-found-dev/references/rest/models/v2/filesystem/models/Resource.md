# foundry_sdk.v2.filesystem.models.Resource


Resource

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ResourceRid | required; no default | No additional field description in SDK source. |
| display_name | displayName | ResourceDisplayName | required; no default | The display name of the resource |
| description | description | typing.Optional[str] | None | The description of the resource |
| documentation | documentation | typing.Optional[str] | None | The documentation associated with the resource |
| path | path | ResourcePath | required; no default | The full path to the resource, including the resource name itself |
| type | type | ResourceType | required; no default | The type of the resource derived from the Resource Identifier (RID). |
| created_by | createdBy | core_models.CreatedBy | required; no default | The user that created the resource |
| updated_by | updatedBy | core_models.UpdatedBy | required; no default | The user that last updated the resource. |
| created_time | createdTime | core_models.CreatedTime | required; no default | The timestamp that the resource was last created. |
| updated_time | updatedTime | core_models.UpdatedTime | required; no default | The timestamp that the resource was last modified. For folders, this includes any of its descendants. For<br>    top level folders (spaces and projects), this is not updated by child updates for performance reasons. |
| trash_status | trashStatus | TrashStatus | required; no default | The trash status of the resource. If trashed, this could either be because the resource itself has been<br>    trashed or because one of its ancestors has been trashed. |
| parent_folder_rid | parentFolderRid | FolderRid | required; no default | The parent folder Resource Identifier (RID). For projects, this will be the Space RID. |
| project_rid | projectRid | ProjectRid | required; no default | The Project Resource Identifier (RID) that the resource lives in. If the resource itself is a<br>    Project, this value will still be populated with the Project RID. |
| space_rid | spaceRid | SpaceRid | required; no default | The Space Resource Identifier (RID) that the resource lives in. |

```python
class Resource(core.ModelBase):
    """Resource"""

    rid: ResourceRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the resource"""

    description: typing.Optional[str] = None
    """The description of the resource"""

    documentation: typing.Optional[str] = None
    """The documentation associated with the resource"""

    path: ResourcePath
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the resource derived from the Resource Identifier (RID)."""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The user that created the resource"""

    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    """The user that last updated the resource."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp that the resource was last created."""

    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """
    The timestamp that the resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the resource. If trashed, this could either be because the resource itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    project_rid: ProjectRid = pydantic.Field(alias=str("projectRid"))  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the resource lives in. If the resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The Space Resource Identifier (RID) that the resource lives in."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../core/models/UpdatedTime.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceType](ResourceType.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](TrashStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Resource.md)

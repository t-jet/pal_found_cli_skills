# foundry_sdk.v2.connectivity.models.Connection


Connection

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ConnectionRid | required; no default | No additional field description in SDK source. |
| parent_folder_rid | parentFolderRid | filesystem_models.FolderRid | required; no default | No additional field description in SDK source. |
| display_name | displayName | ConnectionDisplayName | required; no default | The display name of the Connection. The display name must not be blank. |
| export_settings | exportSettings | ConnectionExportSettings | required; no default | No additional field description in SDK source. |
| worker | worker | ConnectionWorker | required; no default | No additional field description in SDK source. |
| configuration | configuration | ConnectionConfiguration | required; no default | No additional field description in SDK source. |

```python
class Connection(core.ModelBase):
    """Connection"""

    rid: ConnectionRid
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    display_name: ConnectionDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Connection. The display name must not be blank."""

    export_settings: ConnectionExportSettings = pydantic.Field(alias=str("exportSettings"))  # type: ignore[literal-required]
    worker: ConnectionWorker
    configuration: ConnectionConfiguration
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.ConnectionConfiguration](ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.ConnectionDisplayName](ConnectionDisplayName.md)
- [foundry_sdk.v2.connectivity.models.ConnectionExportSettings](ConnectionExportSettings.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.ConnectionWorker](ConnectionWorker.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Connection.md)

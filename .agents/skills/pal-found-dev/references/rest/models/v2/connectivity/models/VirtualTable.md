# foundry_sdk.v2.connectivity.models.VirtualTable


VirtualTable

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | TableRid | required; no default | No additional field description in SDK source. |
| name | name | TableName | required; no default | No additional field description in SDK source. |
| parent_rid | parentRid | filesystem_models.FolderRid | required; no default | No additional field description in SDK source. |
| config | config | VirtualTableConfig | required; no default | No additional field description in SDK source. |
| markings | markings | typing.Optional[typing.List[core_models.MarkingId]] | None | No additional field description in SDK source. |

```python
class VirtualTable(core.ModelBase):
    """VirtualTable"""

    rid: TableRid
    name: TableName
    parent_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentRid"))  # type: ignore[literal-required]
    config: VirtualTableConfig
    markings: typing.Optional[typing.List[core_models.MarkingId]] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.TableName](TableName.md)
- [foundry_sdk.v2.connectivity.models.TableRid](TableRid.md)
- [foundry_sdk.v2.connectivity.models.VirtualTableConfig](VirtualTableConfig.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../filesystem/models/FolderRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VirtualTable.md)

# foundry_sdk.v2.connectivity.models.ReplaceTableImportRequest


ReplaceTableImportRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| import_mode | importMode | TableImportMode | required; no default | No additional field description in SDK source. |
| display_name | displayName | TableImportDisplayName | required; no default | No additional field description in SDK source. |
| allow_schema_changes | allowSchemaChanges | typing.Optional[TableImportAllowSchemaChanges] | default None | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
| config | config | ReplaceTableImportRequestTableImportConfig | required; no default | No additional field description in SDK source. |

```python
class ReplaceTableImportRequest(core.ModelBase):
    """ReplaceTableImportRequest"""

    import_mode: TableImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]
    display_name: TableImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    allow_schema_changes: typing.Optional[TableImportAllowSchemaChanges] = pydantic.Field(alias=str("allowSchemaChanges"), default=None)  # type: ignore[literal-required]
    """Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""

    config: ReplaceTableImportRequestTableImportConfig
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestTableImportConfig](ReplaceTableImportRequestTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.TableImportAllowSchemaChanges](TableImportAllowSchemaChanges.md)
- [foundry_sdk.v2.connectivity.models.TableImportDisplayName](TableImportDisplayName.md)
- [foundry_sdk.v2.connectivity.models.TableImportMode](TableImportMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceTableImportRequest.md)

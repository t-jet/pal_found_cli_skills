# foundry_sdk.v2.connectivity.models.CreateTableImportRequest


CreateTableImportRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The RID of the output dataset. Can not be modified after the table import is created. |
| import_mode | importMode | TableImportMode | required; no default | No additional field description in SDK source. |
| display_name | displayName | TableImportDisplayName | required; no default | No additional field description in SDK source. |
| allow_schema_changes | allowSchemaChanges | typing.Optional[TableImportAllowSchemaChanges] | default None | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
| branch_name | branchName | typing.Optional[core_models.BranchName] | default None | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. Can not be modified after the table import is created. |
| config | config | CreateTableImportRequestTableImportConfig | required; no default | No additional field description in SDK source. |

```python
class CreateTableImportRequest(core.ModelBase):
    """CreateTableImportRequest"""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the output dataset. Can not be modified after the table import is created."""

    import_mode: TableImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]
    display_name: TableImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    allow_schema_changes: typing.Optional[TableImportAllowSchemaChanges] = pydantic.Field(alias=str("allowSchemaChanges"), default=None)  # type: ignore[literal-required]
    """Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""

    branch_name: typing.Optional[core_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. Can not be modified after the table import is created."""

    config: CreateTableImportRequestTableImportConfig
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestTableImportConfig](CreateTableImportRequestTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.TableImportAllowSchemaChanges](TableImportAllowSchemaChanges.md)
- [foundry_sdk.v2.connectivity.models.TableImportDisplayName](TableImportDisplayName.md)
- [foundry_sdk.v2.connectivity.models.TableImportMode](TableImportMode.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateTableImportRequest.md)

# foundry_sdk.v2.connectivity.models.ConnectionExportSettings


The [export settings of a Connection](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| exports_enabled | exportsEnabled | bool | required; no default | Allow exporting datasets from Foundry to this Connection. |
| export_enabled_without_markings_validation | exportEnabledWithoutMarkingsValidation | bool | required; no default | In certain interactive workflows the Connection can be used in, it is not currently possible to validate the <br>    security markings of the data being exported. <br>    By enabling exports without markings validation, you acknowledge that you are responsible for ensuring <br>    that the data being exported is compliant with your organization's policies. |

```python
class ConnectionExportSettings(core.ModelBase):
    """The [export settings of a Connection](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source)."""

    exports_enabled: bool = pydantic.Field(alias=str("exportsEnabled"))  # type: ignore[literal-required]
    """Allow exporting datasets from Foundry to this Connection."""

    export_enabled_without_markings_validation: bool = pydantic.Field(alias=str("exportEnabledWithoutMarkingsValidation"))  # type: ignore[literal-required]
    """
    In certain interactive workflows the Connection can be used in, it is not currently possible to validate the 
    security markings of the data being exported. 
    By enabling exports without markings validation, you acknowledge that you are responsible for ensuring 
    that the data being exported is compliant with your organization's policies.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ConnectionExportSettings.md)

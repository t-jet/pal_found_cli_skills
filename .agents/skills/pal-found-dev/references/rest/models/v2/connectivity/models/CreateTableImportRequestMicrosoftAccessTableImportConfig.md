# foundry_sdk.v2.connectivity.models.CreateTableImportRequestMicrosoftAccessTableImportConfig


CreateTableImportRequestMicrosoftAccessTableImportConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| initial_incremental_state | initialIncrementalState | typing.Optional[TableImportInitialIncrementalState] | default None | No additional field description in SDK source. |
| query | query | TableImportQuery | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['microsoftAccessImportConfig'] | 'microsoftAccessImportConfig' | No additional field description in SDK source. |

```python
class CreateTableImportRequestMicrosoftAccessTableImportConfig(core.ModelBase):
    """CreateTableImportRequestMicrosoftAccessTableImportConfig"""

    initial_incremental_state: typing.Optional[TableImportInitialIncrementalState] = pydantic.Field(alias=str("initialIncrementalState"), default=None)  # type: ignore[literal-required]
    query: TableImportQuery
    type: typing.Literal["microsoftAccessImportConfig"] = "microsoftAccessImportConfig"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.TableImportInitialIncrementalState](TableImportInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.TableImportQuery](TableImportQuery.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateTableImportRequestMicrosoftAccessTableImportConfig.md)

# foundry_sdk.v2.ontologies.models.ObjectTypeTableDatasource


An object type datasource backed by a Foundry table.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| table_rid | tableRid | TableRid | required; no default | No additional field description in SDK source. |
| branch | branch | typing.Optional[DatasourceBranchId] | None | No additional field description in SDK source. |
| property_mapping | propertyMapping | typing.Dict[PropertyApiName, PropertyTypeMappingInfo] | required; no default | A mapping from property API name to a description of how that property is bound to the table. Properties<br>    whose mapping info cannot be modeled are omitted. |
| type | type | typing.Literal['table'] | 'table' | No additional field description in SDK source. |

```python
class ObjectTypeTableDatasource(core.ModelBase):
    """An object type datasource backed by a Foundry table."""

    table_rid: TableRid = pydantic.Field(alias=str("tableRid"))  # type: ignore[literal-required]
    branch: typing.Optional[DatasourceBranchId] = None
    property_mapping: typing.Dict[PropertyApiName, PropertyTypeMappingInfo] = pydantic.Field(alias=str("propertyMapping"))  # type: ignore[literal-required]
    """
    A mapping from property API name to a description of how that property is bound to the table. Properties
    whose mapping info cannot be modeled are omitted.
    """

    type: typing.Literal["table"] = "table"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DatasourceBranchId](DatasourceBranchId.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeMappingInfo](PropertyTypeMappingInfo.md)
- [foundry_sdk.v2.ontologies.models.TableRid](TableRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeTableDatasource.md)

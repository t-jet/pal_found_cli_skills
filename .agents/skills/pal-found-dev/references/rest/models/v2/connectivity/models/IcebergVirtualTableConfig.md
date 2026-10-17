# foundry_sdk.v2.connectivity.models.IcebergVirtualTableConfig


Pointer to the Iceberg table.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| table_identifier | tableIdentifier | str | required; no default | The identifier of the Iceberg table. |
| warehouse_path | warehousePath | typing.Optional[str] | default None | The path to the folder in the file system containing the Iceberg table. Can be omitted when the<br>    connection is configured with a catalog that does not rely on warehouse path. |
| type | type | typing.Literal['iceberg'] | 'iceberg' | No additional field description in SDK source. |

```python
class IcebergVirtualTableConfig(core.ModelBase):
    """Pointer to the Iceberg table."""

    table_identifier: str = pydantic.Field(alias=str("tableIdentifier"))  # type: ignore[literal-required]
    """The identifier of the Iceberg table."""

    warehouse_path: typing.Optional[str] = pydantic.Field(alias=str("warehousePath"), default=None)  # type: ignore[literal-required]
    """
    The path to the folder in the file system containing the Iceberg table. Can be omitted when the
    connection is configured with a catalog that does not rely on warehouse path.
    """

    type: typing.Literal["iceberg"] = "iceberg"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](IcebergVirtualTableConfig.md)

# foundry_sdk.v2.connectivity.models.BigQueryVirtualTableConfig


Pointer to the table in BigQuery. Uses the BigQuery table identifier of project, dataset and table.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| project | project | str | required; no default | The BigQuery project name. |
| dataset | dataset | str | required; no default | The BigQuery dataset name. |
| table | table | str | required; no default | The BigQuery table name. |
| type | type | typing.Literal['bigquery'] | 'bigquery' | No additional field description in SDK source. |

```python
class BigQueryVirtualTableConfig(core.ModelBase):
    """Pointer to the table in BigQuery. Uses the BigQuery table identifier of project, dataset and table."""

    project: str
    """The BigQuery project name."""

    dataset: str
    """The BigQuery dataset name."""

    table: str
    """The BigQuery table name."""

    type: typing.Literal["bigquery"] = "bigquery"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BigQueryVirtualTableConfig.md)

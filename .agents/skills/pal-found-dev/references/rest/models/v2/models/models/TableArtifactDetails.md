# foundry_sdk.v2.models.models.TableArtifactDetails


Details about a table artifact.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| row_count | rowCount | core.Long | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['table'] | 'table' | No additional field description in SDK source. |

```python
class TableArtifactDetails(core.ModelBase):
    """Details about a table artifact."""

    row_count: core.Long = pydantic.Field(alias=str("rowCount"))  # type: ignore[literal-required]
    type: typing.Literal["table"] = "table"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TableArtifactDetails.md)

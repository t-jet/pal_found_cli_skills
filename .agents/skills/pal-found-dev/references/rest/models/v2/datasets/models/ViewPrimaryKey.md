# foundry_sdk.v2.datasets.models.ViewPrimaryKey


The primary key of the dataset. Primary keys are treated as guarantees provided by the creator of the
dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| columns | columns | typing.List[str] | required; no default | The columns that constitute the primary key. These columns must satisfy the following constraints:<br>    - The list of columns must be non-empty.<br>    - The list must not contain duplicate columns after applying column normalization.<br>    - Each referenced column must exist in the schema.<br>    - The type of each referenced column must be one of the following: `BYTE`, `SHORT`, `DECIMAL`, `INTEGER`,<br>      `LONG`, `STRING`, `BOOLEAN`, `TIMESTAMP` or `DATE`. |
| resolution | resolution | ViewPrimaryKeyResolution | required; no default | The semantics of the primary key within the dataset. For example, the unique resolution means that every<br>    row in the dataset has a distinct primary key. The value of this field represents a contract for writers<br>    of the dataset. Writers are responsible for maintaining any related invariants, and readers may make<br>    optimizations based on this. Violating the assumptions of the resolution can cause undefined behavior,<br>    for example, having duplicate primary keys with the unique resolution. |

```python
class ViewPrimaryKey(core.ModelBase):
    """
    The primary key of the dataset. Primary keys are treated as guarantees provided by the creator of the
    dataset.
    """

    columns: typing.List[str]
    """
    The columns that constitute the primary key. These columns must satisfy the following constraints:
    - The list of columns must be non-empty.
    - The list must not contain duplicate columns after applying column normalization.
    - Each referenced column must exist in the schema.
    - The type of each referenced column must be one of the following: `BYTE`, `SHORT`, `DECIMAL`, `INTEGER`,
      `LONG`, `STRING`, `BOOLEAN`, `TIMESTAMP` or `DATE`.
    """

    resolution: ViewPrimaryKeyResolution
    """
    The semantics of the primary key within the dataset. For example, the unique resolution means that every
    row in the dataset has a distinct primary key. The value of this field represents a contract for writers
    of the dataset. Writers are responsible for maintaining any related invariants, and readers may make
    optimizations based on this. Violating the assumptions of the resolution can cause undefined behavior,
    for example, having duplicate primary keys with the unique resolution.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKeyResolution](ViewPrimaryKeyResolution.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ViewPrimaryKey.md)

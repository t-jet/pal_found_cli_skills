# foundry_sdk.v2.datasets.models.PrimaryKeyResolutionDuplicate


Duplicate primary key values may exist within the dataset – resolution required.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| deletion_column | deletionColumn | typing.Optional[str] | default None | The name of the boolean column that indicates whether a row should be considered deleted. Based on the<br>    `resolutionStrategy`, if the final row selected for a given primary key has `true` in this column, that<br>    row will be excluded from the results. Otherwise, it will be included. |
| resolution_strategy | resolutionStrategy | PrimaryKeyResolutionStrategy | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['duplicate'] | 'duplicate' | No additional field description in SDK source. |

```python
class PrimaryKeyResolutionDuplicate(core.ModelBase):
    """Duplicate primary key values may exist within the dataset – resolution required."""

    deletion_column: typing.Optional[str] = pydantic.Field(alias=str("deletionColumn"), default=None)  # type: ignore[literal-required]
    """
    The name of the boolean column that indicates whether a row should be considered deleted. Based on the
    `resolutionStrategy`, if the final row selected for a given primary key has `true` in this column, that
    row will be excluded from the results. Otherwise, it will be included.
    """

    resolution_strategy: PrimaryKeyResolutionStrategy = pydantic.Field(alias=str("resolutionStrategy"))  # type: ignore[literal-required]
    type: typing.Literal["duplicate"] = "duplicate"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionStrategy](PrimaryKeyResolutionStrategy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PrimaryKeyResolutionDuplicate.md)

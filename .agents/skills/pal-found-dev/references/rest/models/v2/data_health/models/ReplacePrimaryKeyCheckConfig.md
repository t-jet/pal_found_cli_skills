# foundry_sdk.v2.data_health.models.ReplacePrimaryKeyCheckConfig


ReplacePrimaryKeyCheckConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| primary_key_config | primaryKeyConfig | ReplacePrimaryKeyConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['primaryKey'] | 'primaryKey' | No additional field description in SDK source. |

```python
class ReplacePrimaryKeyCheckConfig(core.ModelBase):
    """ReplacePrimaryKeyCheckConfig"""

    primary_key_config: ReplacePrimaryKeyConfig = pydantic.Field(alias=str("primaryKeyConfig"))  # type: ignore[literal-required]
    type: typing.Literal["primaryKey"] = "primaryKey"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.ReplacePrimaryKeyConfig](ReplacePrimaryKeyConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplacePrimaryKeyCheckConfig.md)

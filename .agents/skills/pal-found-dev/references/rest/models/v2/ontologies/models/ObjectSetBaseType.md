# foundry_sdk.v2.ontologies.models.ObjectSetBaseType


ObjectSetBaseType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_type | objectType | str | required; no default | The API name of the object type. |
| type | type | typing.Literal['base'] | 'base' | No additional field description in SDK source. |

```python
class ObjectSetBaseType(core.ModelBase):
    """ObjectSetBaseType"""

    object_type: str = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    """The API name of the object type."""

    type: typing.Literal["base"] = "base"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetBaseType.md)

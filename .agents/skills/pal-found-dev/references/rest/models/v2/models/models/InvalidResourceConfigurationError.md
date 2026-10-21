# foundry_sdk.v2.models.models.InvalidResourceConfigurationError


A resource configuration field has an invalid format.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | str | required; no default | The name of the invalid field (e.g. "cpu", "memory"). |
| message | message | str | required; no default | A description of why the value is invalid. |
| type | type | typing.Literal['invalidResourceConfiguration'] | 'invalidResourceConfiguration' | No additional field description in SDK source. |

```python
class InvalidResourceConfigurationError(core.ModelBase):
    """A resource configuration field has an invalid format."""

    field: str
    """The name of the invalid field (e.g. "cpu", "memory")."""

    message: str
    """A description of why the value is invalid."""

    type: typing.Literal["invalidResourceConfiguration"] = "invalidResourceConfiguration"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidResourceConfigurationError.md)

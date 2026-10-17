# foundry_sdk.v2.models.models.JsonSchemaValidationError


The custom configuration failed JSON schema validation.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | str | required; no default | The field in the provided JSON that is invalid. |
| message | message | str | required; no default | A description of the validation failure. |
| type | type | typing.Literal['jsonSchemaValidationFailure'] | 'jsonSchemaValidationFailure' | No additional field description in SDK source. |

```python
class JsonSchemaValidationError(core.ModelBase):
    """The custom configuration failed JSON schema validation."""

    field: str
    """The field in the provided JSON that is invalid."""

    message: str
    """A description of the validation failure."""

    type: typing.Literal["jsonSchemaValidationFailure"] = "jsonSchemaValidationFailure"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](JsonSchemaValidationError.md)

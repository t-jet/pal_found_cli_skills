# foundry_sdk.v2.models.models.MissingWorkerConfigInputError


The worker configuration is missing an input required by the trainer.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| input_alias | inputAlias | InputAlias | required; no default | The alias of the missing input. |
| type | type | typing.Literal['missingWorkerConfigInput'] | 'missingWorkerConfigInput' | No additional field description in SDK source. |

```python
class MissingWorkerConfigInputError(core.ModelBase):
    """The worker configuration is missing an input required by the trainer."""

    input_alias: InputAlias = pydantic.Field(alias=str("inputAlias"))  # type: ignore[literal-required]
    """The alias of the missing input."""

    type: typing.Literal["missingWorkerConfigInput"] = "missingWorkerConfigInput"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.InputAlias](InputAlias.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MissingWorkerConfigInputError.md)

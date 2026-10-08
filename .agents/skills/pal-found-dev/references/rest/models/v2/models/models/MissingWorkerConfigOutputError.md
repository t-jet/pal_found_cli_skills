# foundry_sdk.v2.models.models.MissingWorkerConfigOutputError


The worker configuration is missing an output required by the trainer.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| output_alias | outputAlias | OutputAlias | required; no default | The alias of the missing output. |
| type | type | typing.Literal['missingWorkerConfigOutput'] | 'missingWorkerConfigOutput' | No additional field description in SDK source. |

```python
class MissingWorkerConfigOutputError(core.ModelBase):
    """The worker configuration is missing an output required by the trainer."""

    output_alias: OutputAlias = pydantic.Field(alias=str("outputAlias"))  # type: ignore[literal-required]
    """The alias of the missing output."""

    type: typing.Literal["missingWorkerConfigOutput"] = "missingWorkerConfigOutput"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.OutputAlias](OutputAlias.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MissingWorkerConfigOutputError.md)
